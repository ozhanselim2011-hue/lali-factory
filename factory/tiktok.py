"""TikTok через tikwm.com: тренды и скачивание звуков.

  python3 factory/tiktok.py trends [BY] [30]      трендовые видео (BY: свежий русскоязычный фид; RU заморожен с 2022), сгруппированные по звуку
  python3 factory/tiktok.py get <ссылка|video_id> [автор]   скачать звук в jobs/<id>/in.mp4 и поставить в очередь

Сеть: www.tikwm.com + файловые серверы *.tiktokcdn.com / *.tiktokcdn-us.com (должны быть разрешены в среде).
"""
import json, re, subprocess, sys, time, pathlib, collections, urllib.parse, requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
TIKWM = "https://www.tikwm.com"
UA = {"User-Agent": "Mozilla/5.0 (lali-factory)"}
LINK_RE = re.compile(r"https?://(?:www\.|vm\.|vt\.|m\.)?tiktok\.com/[^\s]+")
_last = [0.0]


def api(path, **params):
    """tikwm бесплатно разрешает ~1 запрос в секунду."""
    for i in range(4):
        wait = 1.3 - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()
        try:
            d = requests.get(f"{TIKWM}{path}", params=params, headers=UA, timeout=40).json()
        except (requests.RequestException, ValueError):
            time.sleep(2 ** i); continue
        if d.get("code") == 0:
            return d.get("data")
        if "limit" in str(d.get("msg", "")).lower():
            time.sleep(2 ** i); continue
        raise RuntimeError(f"tikwm: {d.get('msg')}")
    raise RuntimeError("tikwm: нет ответа")


def trends(region="BY", count=30):
    vids = api("/api/feed/list", region=region, count=count) or []
    by = collections.OrderedDict()
    for v in vids:
        m = v.get("music_info") or {}
        k = m.get("id") or v.get("video_id")
        e = by.setdefault(k, {"sound": f"{m.get('author', '')} — {m.get('title', '')}".strip(" —"),
                              "music_id": m.get("id"), "original": bool(m.get("original")) or "original sound" in (m.get("title") or ""), "plays": 0, "videos": []})
        e["plays"] += v.get("play_count", 0)
        e["videos"].append({"video_id": v.get("video_id"), "title": (v.get("title") or "")[:80],
                            "url": f"https://www.tiktok.com/@{(v.get('author') or {}).get('unique_id', '_')}/video/{v.get('video_id')}"})
    return sorted(by.values(), key=lambda e: -e["plays"])


def info(link_or_id):
    url = link_or_id if link_or_id.startswith("http") else f"https://www.tiktok.com/@_/video/{link_or_id}"
    return api("/api/", url=url, hd=0)


def download_audio(d, out_dir):
    """Скачать звук ролика: сначала music, иначе видео (play) и вытащить дорожку. -> путь к src-файлу."""
    errs = []
    for key in ("music", "play", "wmplay"):
        u = d.get(key)
        if not u:
            continue
        if u.startswith("/"):
            u = TIKWM + u
        try:
            r = requests.get(u, headers=UA, timeout=120)
            if r.status_code == 200 and len(r.content) > 10000:
                p = out_dir / ("src.mp3" if key == "music" else "src.mp4")
                p.write_bytes(r.content)
                return p
            errs.append(f"{key}: HTTP {r.status_code}")
        except requests.RequestException as e:
            errs.append(f"{key}: {urllib.parse.urlparse(u).hostname} недоступен ({type(e).__name__})")
    raise RuntimeError("; ".join(errs) or "нет ссылок на звук")


def get(link_or_id, by="TikTok"):
    """Скачать звук в новое задание и добавить его в state/tg.json. Вернуть job id."""
    sys.path.insert(0, str(ROOT / "factory"))
    import tg
    d = info(link_or_id)
    vid = d.get("id") or d.get("video_id")
    m = d.get("music_info") or {}
    jid = time.strftime("%Y%m%d") + f"_tt{vid}"
    jd = ROOT / "jobs" / jid
    jd.mkdir(parents=True, exist_ok=True)
    src = download_audio(d, jd)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vn", "-c:a", "aac", "-b:a", "192k", str(jd / "in.mp4")], check=True)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(jd / "in.mp4")],
                               capture_output=True, text=True).stdout.strip())
    title = f"{m.get('author', '')} — {m.get('title', '')}".strip(" —")
    url = f"https://www.tiktok.com/@{(d.get('author') or {}).get('unique_id', '_')}/video/{vid}"
    meta = {"job": jid, "kind": "tiktok", "tiktok_url": url, "title": title, "caption": d.get("title", ""),
            "duration": round(dur, 2), "by": by, "date": int(time.time())}
    (jd / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1))
    s = tg.load()
    s["jobs"][jid] = {"status": "new", "title": title, "duration": round(dur, 2), "by": by}
    tg.save(s)
    print("fetched", jid, title, dur)
    return jid


if __name__ == "__main__":
    cmd, *a = sys.argv[1:] or ["help"]
    if cmd == "trends":
        for e in trends(a[0] if a else "BY", int(a[1]) if len(a) > 1 else 30):
            print(f"{e['plays']:>11,} | {e['sound'][:60]} | {'оригинальный' if e['original'] else 'трек'} | {e['videos'][0]['url']}")
            for v in e["videos"][:2]:
                print("            ·", v["title"])
    elif cmd == "get":
        get(a[0], a[1] if len(a) > 1 else "TikTok")
    else:
        print(__doc__)
