"""Распознать трек: python3 factory/shazam.py jobs/<id>/in.mp4  ->  'Артист — Трек' или пусто"""
import asyncio, os, subprocess, sys, tempfile
from shazamio import Shazam
async def main(src):
    sh = Shazam(); px = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    for st in (2, 6, 0):
        w = tempfile.mktemp(suffix=".wav")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(st), "-t", "10", "-i", src, "-ac", "1", "-ar", "44100", w])
        try:
            tr = (await sh.recognize(w, proxy=px)).get("track")
        except Exception as e:
            print("ERR", str(e)[:100], file=sys.stderr); tr = None
        if tr:
            print(f"{tr.get('subtitle')} — {tr.get('title')}"); return
    print("")
asyncio.run(main(sys.argv[1]))
