"""TikTok через tikwm.com: тренды и скачивание звуков.

  python3 factory/tiktok.py trends [BY] [страниц]  самые новые+популярные звуки (≤3 дней, по скорости просмотров) + хештеги. BY — свежий русскоязычный фид, RU заморожен с 2022, сгруппированные по звуку
  python3 factory/tiktok.py chart [RU] [15]      САМЫЕ ИЗВЕСТНЫЕ: чарт Shazam России -> официальный звук в TikTok + хештеги
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


def _cyr(t):
    return sum(1 for c in t if "\u0400" <= c <= "\u04ff")


def trends(region="BY", count=30, pages=4, max_age_days=3):
    """Самые новые и самые популярные звуки: несколько страниц фида, только ролики не старше max_age_days.
    Рейтинг = просмотры в час с момента публикации (скорость набора), русскоязычное и известные треки выше."""
    vids, seen = [], set()
    for _ in range(pages):
        for v in api("/api/feed/list", region=region, count=count) or []:
            if v.get("video_id") not in seen:
                seen.add(v.get("video_id")); vids.append(v)
    now = time.time()
    by = collections.OrderedDict()
    for v in vids:
        age_h = max(1.0, (now - v.get("create_time", now)) / 3600)
        if age_h > max_age_days * 24:
            continue
        m = v.get("music_info") or {}
        k = m.get("id") or v.get("video_id")
        sound = f"{m.get('author', '')} — {m.get('title', '')}".strip(" —")
        e = by.setdefault(k, {"sound": sound, "music_id": m.get("id"),
                              "original": bool(m.get("original")) or "original sound" in (m.get("title") or ""),
                              "plays": 0, "speed": 0.0, "age_h": age_h, "cyr": 0, "tags": collections.Counter(), "videos": []})
        e["plays"] += v.get("play_count", 0)
        e["speed"] += v.get("play_count", 0) / age_h
        e["age_h"] = min(e["age_h"], age_h)
        e["cyr"] += _cyr((v.get("title") or "") + sound)
        e["tags"].update(t.lower() for t in re.findall(r"#([\w\u0400-\u04ff]+)", v.get("title") or ""))
        e["videos"].append({"video_id": v.get("video_id"), "title": (v.get("title") or "")[:80], "plays": v.get("play_count", 0),
                            "url": f"https://www.tiktok.com/@{(v.get('author') or {}).get('unique_id', '_')}/video/{v.get('video_id')}"})
    for e in by.values():
        e["score"] = e["speed"] * (1.5 if e["cyr"] >= 3 else 1) * (1.3 if not e["original"] else 1)
        e["videos"].sort(key=lambda x: -x["plays"])
    return sorted(by.values(), key=lambda e: -e["score"])


def hot_tags(items, n=15):
    """Самые частые хештеги в свежем фиде (для подписи под видео)."""
    c = collections.Counter()
    for e in items:
        c.update(e["tags"])
    return [t for t, _ in c.most_common(n)]


def search(q, count=20):
    """Поиск видео TikTok (tikwm: POST на /api/feed/search/ — без слэша отдаёт капчу)."""
    for i in range(3):
        wait = 1.3 - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()
        try:
            d = requests.post(f"{TIKWM}/api/feed/search/", data={"keywords": q, "count": count, "cursor": 0},
                              headers=UA, timeout=40).json()
            if d.get("code") == 0:
                return (d.get("data") or {}).get("videos") or []
        except (requests.RequestException, ValueError):
            pass
        time.sleep(2 ** i)
    return []


def shazam_chart(country="RU", limit=20):
    import asyncio, os
    from shazamio import Shazam
    async def go():
        return await Shazam().top_country_tracks(country, limit=limit, proxy=os.environ.get("HTTPS_PROXY"))
    out = []
    for t in asyncio.run(go()):
        d = t.model_dump() if hasattr(t, "model_dump") else t.__dict__
        out.append({"artist": d.get("artist") or d.get("subtitle") or "", "title": d.get("title") or ""})
    return out


def _norm(x):
    return re.sub(r"[^\w]+", " ", (x or "").lower()).strip()


def chart(country="RU", limit=15):
    """Самые известные свежие треки: чарт Shazam страны -> официальный звук этого трека в TikTok + хештеги."""
    res = []
    for pos, tr in enumerate(shazam_chart(country, limit), 1):
        base = re.sub(r"\s*[\(\[].*?[\)\]]", "", tr["title"])
        vids = search(f"{tr['artist'].split('&')[0].split(',')[0]} {base}")
        if not vids:
            continue
        nt = _norm(base)
        official = [v for v in vids if nt and nt in _norm((v.get("music_info") or {}).get("title"))]
        pick = max(official or vids, key=lambda v: v.get("play_count", 0))
        tags = collections.Counter()
        for v in vids:
            tags.update(t.lower() for t in re.findall(r"#([\w\u0400-\u04ff]+)", v.get("title") or ""))
        m = pick.get("music_info") or {}
        res.append({"pos": pos, "track": f"{tr['artist']} — {tr['title']}", "official": bool(official),
                    "tiktok_sound": f"{m.get('author', '')} — {m.get('title', '')}",
                    "plays": sum(v.get("play_count", 0) for v in vids), "tags": tags,
                    "url": f"https://www.tiktok.com/@{(pick.get('author') or {}).get('unique_id', '_')}/video/{pick.get('video_id')}",
                    "cyr": _cyr(tr["artist"] + tr["title"]) > 0})
    return res


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
        items = trends(a[0] if a else "BY", pages=int(a[1]) if len(a) > 1 else 4)
        print("#  | просм/час | всего     | возраст | тип   | звук | ссылка")
        for i, e in enumerate(items[:25], 1):
            print(f"{i:<2} | {int(e['speed']):>9,} | {e['plays']:>9,} | {e['age_h']/24:>5.1f}д | {'ориг ' if e['original'] else 'трек '} | "
                  f"{e['sound'][:50]} | {e['videos'][0]['url']}")
            if e["tags"]:
                print("     теги:", " ".join("#" + t for t, _ in e["tags"].most_common(8)))
        print("\nГорячие хештеги фида:", " ".join("#" + t for t in hot_tags(items)))
    elif cmd == "chart":
        for e in chart(a[0] if a else "RU", int(a[1]) if len(a) > 1 else 15):
            print(f"{e['pos']:<2} | {e['track'][:55]} | TikTok: {e['plays']:>10,} просм. | {'офиц. звук' if e['official'] else 'похожий'} | {e['url']}")
            if e["tags"]:
                print("     теги:", " ".join("#" + t for t, _ in e["tags"].most_common(10)))
    elif cmd == "get":
        get(a[0], a[1] if len(a) > 1 else "TikTok")
    else:
        print(__doc__)
