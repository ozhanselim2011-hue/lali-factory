"""Telegram-бот фабрики Лали. Отвечает и принимает файлы ТОЛЬКО от владельца.

Команды:
  python3 factory/tg.py pull            забрать новые сообщения владельца (звуки -> state/tg.json pending)
  python3 factory/tg.py fetch           скачать все pending-звуки в jobs/<id>/in.mp4
  python3 factory/tg.py jobs            показать задания и их статус
  python3 factory/tg.py text <file|->   отправить текст владельцу
  python3 factory/tg.py video <mp4> [подпись] [job_id]   (с job_id запоминает сообщение для отбора)
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


def pull():
    s = load()
    ups = call("getUpdates", offset=s["offset"], timeout=0, allowed_updates='["message"]')
    got = 0
    reviewed = []
    for u in ups:
        s["offset"] = u["update_id"] + 1
        m = u.get("message") or {}
        if (m.get("from") or {}).get("id") != OWNER or m.get("chat", {}).get("id") != OWNER:
            continue  # чужие сообщения молча игнорируем
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
        md = media_of(m)
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
    print(f"updates={len(ups)} new_sounds={got} pending={len(s['pending'])} notes={len(s['notes'])} reviews={reviewed}")


def fetch():
    s = load()
    left = []
    for p in s["pending"]:
        jid = time.strftime("%Y%m%d", time.gmtime(p["date"])) + f"_{p['msg_id']}"
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
            s["jobs"][jid] = {"status": "new", "title": p["title"], "duration": round(dur, 2)}
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
        with open(a[0], "rb") as f:
            r = requests.post(f"{API}/sendVideo", data={"chat_id": OWNER, "caption": a[1] if len(a) > 1 else "",
                                                        "supports_streaming": "true", "width": 1080, "height": 1080},
                              files={"video": f}, timeout=300).json()
        if r.get("ok") and len(a) > 2:
            s = load(); s["jobs"].setdefault(a[2], {})
            s["jobs"][a[2]].update(msg_id=r["result"]["message_id"], status="sent"); save(s)
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
