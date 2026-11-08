"""Telegram-бот фабрики Лали.

Владелец (factory/config.json): звуки, идеи (текст), отзывы на видео (ответом на видео).
Гости (любой другой в личке бота): ТОЛЬКО звуки, не больше guest_daily_limit в сутки; получают лишь «Звук принят».
Готовые видео и исходные звуки отправляются ТОЛЬКО владельцу, с подписью, кто прислал звук.

Команды:
  python3 factory/tg.py pull            забрать новые сообщения владельца (звуки -> state/tg.json pending)
  python3 factory/tg.py fetch           скачать все pending-звуки в jobs/<id>/in.mp4
  python3 factory/tg.py jobs            показать задания и их статус
  python3 factory/tg.py text <file|->   отправить текст владельцу
  python3 factory/tg.py video <mp4> [подпись] [job_id]   (с job_id: + автор звука, + исходный звук следом)
  python3 factory/tg.py status <job_id> <new|rendered|sent|skipped>

Токен берётся из переменной окружения TG_BOT_TOKEN, владелец — из factory/config.json.
"""
import json, os, subprocess, sys, time, pathlib, requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / "factory/config.json").read_text())
OWNER = int(CFG["owner_chat_id"])
STATE_F = ROOT / "state/tg.json"
API = f"https://api.telegram.org/bot{os.environ['TG_BOT_TOKEN']}"
FILE_API = f"https://api.telegram.org/file/bot{os.environ['TG_BOT_TOKEN']}"
GUEST_DAILY_LIMIT = int(CFG.get("guest_daily_limit", 5))  # звуков в сутки от одного гостя


def load():
    if STATE_F.exists():
        return json.loads(STATE_F.read_text())
    return {"offset": 0, "pending": [], "jobs": {}, "notes": []}


def save(s):
    STATE_F.parent.mkdir(exist_ok=True)
    STATE_F.write_text(json.dumps(s, ensure_ascii=False, indent=1))


def call(method, **params):
    for i in range(4):
        try:
            r = requests.post(f"{API}/{method}", data=params, timeout=60).json()
            if r.get("ok"):
                return r["result"]
            raise RuntimeError(r.get("description"))
        except requests.RequestException:
            time.sleep(2 ** i)
    raise RuntimeError(f"{method}: network error")


def send_text(text):
    for i in range(0, len(text), 4000):
        call("sendMessage", chat_id=OWNER, text=text[i:i + 4000], disable_web_page_preview="true")


def media_of(m):
    """Вернуть (file_id, kind, title) если в сообщении звук/видео."""
    for kind in ("audio", "voice", "video", "video_note"):
        if kind in m:
            a = m[kind]
            title = " — ".join(x for x in (a.get("performer"), a.get("title")) if x) or a.get("file_name", "")
            return a["file_id"], kind, title, a.get("file_size", 0)
    d = m.get("document")
    if d and (d.get("mime_type", "").startswith(("audio/", "video/"))):
        return d["file_id"], "document", d.get("file_name", ""), d.get("file_size", 0)
    return None


def tiktok_link(m):
    """Ссылка на TikTok в тексте/подписи -> (url, 'tiktok', '', 0)."""
    import re
    mt = re.search(r"https?://(?:www\.|vm\.|vt\.|m\.)?tiktok\.com/[^\s]+", (m.get("text") or "") + " " + (m.get("caption") or ""))
    return (mt.group(0), "tiktok", "", 0) if mt else None


def pull():
    s = load()
    ups = call("getUpdates", offset=s["offset"], timeout=0, allowed_updates='["message"]')
    got = 0
    guests = []
    reviewed = []
    today = time.strftime("%Y%m%d")
    quota = s.setdefault("guest_quota", {})
    if quota.get("day") != today:
        quota.clear(); quota["day"] = today
    for u in ups:
        s["offset"] = u["update_id"] + 1
        m = u.get("message") or {}
        frm = m.get("from") or {}
        chat = m.get("chat") or {}
        if frm.get("id") != OWNER or chat.get("id") != OWNER:
            # Гости: принимаем ТОЛЬКО звуки в личке. Тексты, отзывы, команды — игнор.
            # Готовое видео гостю не отправляется никогда — только владельцу.
            md = media_of(m) or tiktok_link(m)
            if chat.get("type") != "private" or not md or frm.get("is_bot"):
                continue
            fid, kind, title, size = md
            uid = str(frm["id"])
            if quota.get(uid, 0) >= GUEST_DAILY_LIMIT or (size and size > 20 * 1024 * 1024):
                continue
            quota[uid] = quota.get(uid, 0) + 1
            s["pending"].append({"file_id": fid, "kind": kind, "title": title, "caption": m.get("caption", ""),
                                 "msg_id": m["message_id"], "date": m["date"], "chat_id": chat["id"],
                                 "from": {"id": frm["id"], "username": frm.get("username", ""),
                                          "name": " ".join(x for x in (frm.get("first_name"), frm.get("last_name")) if x)}})
            try:
                call("sendMessage", chat_id=chat["id"], text="🎧 Звук принят, спасибо!")
            except Exception:
                pass
            guests.append(who(s["pending"][-1]))
            continue
        rep = (m.get("reply_to_message") or {}).get("message_id")
        job = next((k for k, v in s["jobs"].items() if v.get("msg_id") == rep), None) if rep else None
        if job and m.get("text"):
            t = m["text"].strip()
            j = s["jobs"][job]
            if t[:1] in ("✅", "👍", "+") or t.lower() in ("да", "ок", "ok", "оставить", "беру"):
                j["status"] = "approved"
            elif t[:1] in ("❌", "👎", "-") or t.lower() in ("нет", "убрать", "мимо"):
                j["status"] = "rejected"
            else:
                j["status"] = "fix"
                j.setdefault("feedback", []).append(t)
            reviewed.append(f"{job}: {j['status']}")
            continue
        md = media_of(m) or tiktok_link(m)
        if md:
            fid, kind, title, size = md
            if size and size > 20 * 1024 * 1024:
                send_text("⚠️ Файл больше 20 МБ — Telegram не даёт боту его скачать. Пришли покороче/сжатый.")
                continue
            s["pending"].append({"file_id": fid, "kind": kind, "title": title, "caption": m.get("caption", ""),
                                 "msg_id": m["message_id"], "date": m["date"]})
            got += 1
        elif m.get("text") and not m["text"].startswith("/start"):
            s["notes"].append({"date": m["date"], "text": m["text"]})
    save(s)
    if ups:  # подтверждаем получение у Telegram
        call("getUpdates", offset=s["offset"], timeout=0)
    if got:
        send_text(f"🎧 Принял звуков: {got}. Делаю видео.")
    if guests:
        from collections import Counter
        send_text("📨 Звуки от других: " + ", ".join(f"{k} ×{v}" if v > 1 else k for k, v in Counter(guests).items())
                  + ". Видео пришлю тебе.")
    print(f"updates={len(ups)} new_sounds={got} guest_sounds={len(guests)} pending={len(s['pending'])} "
          f"notes={len(s['notes'])} reviews={reviewed}")


def who(p):
    """Подпись автора звука: @username (Имя) или 'ты'."""
    f = p.get("from")
    if not f:
        return "ты"
    return (f"@{f['username']}" if f.get("username") else f"id{f['id']}") + (f" ({f['name']})" if f.get("name") else "")


def send_hashtags(jid):
    """Хештеги из jobs/<id>/hashtags.txt — отдельным сообщением, копируются одним нажатием."""
    import html
    f = ROOT / "jobs" / jid / "hashtags.txt"
    if not f.exists():
        print("WARN: нет hashtags.txt для", jid); return
    tags = " ".join(f.read_text().split())
    call("sendMessage", chat_id=OWNER, parse_mode="HTML",
         text=f"#️⃣ Хештеги под видео (нажми, чтобы скопировать):\n<code>{html.escape(tags)}</code>")


def send_source(jid):
    """Отправить владельцу исходный звук задания (по file_id) с подписью автора."""
    meta = json.loads((ROOT / "jobs" / jid / "meta.json").read_text())
    if meta["kind"] == "tiktok":
        src = next((ROOT / "jobs" / jid).glob("src.*"), None) or (ROOT / "jobs" / jid / "in.mp4")
        with open(src, "rb") as f:
            requests.post(f"{API}/sendAudio", data={"chat_id": OWNER, "title": meta.get("title", "")[:60],
                          "caption": f"🎧 Исходный звук · от {who(meta) if meta.get('from') else meta.get('by', 'TikTok')}\n{meta['tiktok_url']}"},
                          files={"audio": (f"{jid}.mp3" if src.suffix == ".mp3" else f"{jid}.m4a", f)}, timeout=120)
        return
    method, field = {"audio": ("sendAudio", "audio"), "voice": ("sendVoice", "voice"), "video": ("sendVideo", "video"),
                     "video_note": ("sendVideoNote", "video_note")}.get(meta["kind"], ("sendDocument", "document"))
    params = {"chat_id": OWNER, field: meta["file_id"]}
    if method != "sendVideoNote":
        params["caption"] = f"🎧 Исходный звук · от {who(meta)}"
    call(method, **params)


def fetch():
    s = load()
    left = []
    for p in s["pending"]:
        if p["kind"] == "tiktok":
            try:
                import tiktok
                save(s)  # tiktok.get пишет state сам — сначала сохраняем уже скачанное
                jid = tiktok.get(p["file_id"], who(p))
                s = load()  # tiktok.get уже записал задание
                meta_f = ROOT / "jobs" / jid / "meta.json"
                meta = json.loads(meta_f.read_text()); meta["from"] = p.get("from"); meta_f.write_text(json.dumps(meta, ensure_ascii=False, indent=1))
            except Exception as e:
                print("FAILED tiktok", p["file_id"], e)
                if p.get("tries", 0) < 2:
                    p["tries"] = p.get("tries", 0) + 1; left.append(p)
                else:
                    send_text(f"⚠️ Не смог скачать звук из TikTok ({who(p)}): {p['file_id']}\n{str(e)[:200]}")
            continue
        jid = time.strftime("%Y%m%d", time.gmtime(p["date"])) + (f"_u{p['from']['id']}" if p.get("from") else "") + f"_{p['msg_id']}"
        jd = ROOT / "jobs" / jid
        jd.mkdir(parents=True, exist_ok=True)
        try:
            fp = call("getFile", file_id=p["file_id"])["file_path"]
            raw = jd / ("src" + pathlib.Path(fp).suffix)
            raw.write_bytes(requests.get(f"{FILE_API}/{fp}", timeout=120).content)
            # нормализуем в in.mp4 (только аудио) — так ждут скрипты рендера
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-vn", "-c:a", "aac", "-b:a", "192k",
                            str(jd / "in.mp4")], check=True)
            dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                        str(jd / "in.mp4")], capture_output=True, text=True).stdout.strip())
            meta = dict(p, job=jid, duration=round(dur, 2))
            (jd / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1))
            s["jobs"][jid] = {"status": "new", "title": p["title"], "duration": round(dur, 2), "by": who(p)}
            print("fetched", jid, p["title"], dur)
        except Exception as e:
            print("FAILED", p.get("title"), e)
            left.append(p)
    s["pending"] = left
    save(s)


def main():
    cmd, *a = sys.argv[1:] or ["help"]
    if cmd == "pull":
        pull()
    elif cmd == "fetch":
        fetch()
    elif cmd == "jobs":
        s = load()
        for k, v in s["jobs"].items():
            print(k, v)
        print("pending:", len(s["pending"]), "notes:", s["notes"][-10:])
    elif cmd == "text":
        send_text(sys.stdin.read() if a[0] == "-" else pathlib.Path(a[0]).read_text())
    elif cmd == "video":
        cap = a[1] if len(a) > 1 else ""
        if len(a) > 2:  # подписываем автора звука
            cap += f"\n🎧 Звук от {load()['jobs'].get(a[2], {}).get('by', 'ты')}"
        with open(a[0], "rb") as f:
            r = requests.post(f"{API}/sendVideo", data={"chat_id": OWNER, "caption": cap,
                                                        "supports_streaming": "true", "width": 1080, "height": 1080},
                              files={"video": f}, timeout=300).json()
        if r.get("ok") and len(a) > 2:
            s = load(); s["jobs"].setdefault(a[2], {})
            s["jobs"][a[2]].update(msg_id=r["result"]["message_id"], status="sent"); save(s)
            try:
                send_source(a[2])  # следом — исходный звук
            except Exception as e:
                print("source not sent:", e)
            send_hashtags(a[2])
        print("ok" if r.get("ok") else r)
    elif cmd == "status":
        s = load()
        s["jobs"][a[0]]["status"] = a[1]
        save(s)
    elif cmd == "clear-notes":
        s = load(); s["notes"] = []; save(s)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
