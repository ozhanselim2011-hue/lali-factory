"""Собрать финальную сцену: python3 factory/build.py jobs/<id>
Читает jobs/<id>/spec.py (формат как examples/v*/spec.py + LK, SONG, DUR, FADE, START),
пишет scene.html и scene_final.html (сцена + персонаж Лали + плашка трека + VPN-плашка)."""
import json, re, subprocess, sys, pathlib
F = pathlib.Path(__file__).resolve().parent
jd = pathlib.Path(sys.argv[1])
spec = {"HELPERS": str(F / "helpers.js")}; exec((jd / "spec.py").read_text(), spec)
subprocess.run([sys.executable, str(F / "gen.py"), str(jd / "spec.py"), str(jd / "scene.html")], check=True)
h = (jd / "scene.html").read_text()
lk = []
for x in spec.get("LK", []):
    d = {"t": x[0], "p": x[1]}
    if len(x) > 2: d.update(x[2])
    lk.append(d)
start = float(spec.get("START", 0)); dur = float(spec["DUR"])
if lk: h = h.replace("</body>", f"<script>window.LK={json.dumps(lk, ensure_ascii=False)};"
              f"window.LSIDE={json.dumps(spec.get('LSIDE', 'L'))};</script><script>{(F / 'char.js').read_text()}</script></body>")
h = re.sub(r"(#sub\{position:absolute;top:)\d+px", r"\g<1>88px", h)
h = h.replace("</body>", f"<script>window.SONG={json.dumps(spec.get('SONG', ''), ensure_ascii=False)};"
              f"window.DUR={dur + start};</script><script>{(F / 'bars.js').read_text()}</script></body>")
(jd / "scene_final.html").write_text(h)
print("ok", jd, "DUR", dur, "FADE", spec["FADE"], "START", start)
