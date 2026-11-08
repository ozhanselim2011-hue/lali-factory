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
# Проверка таймкодов: все времена — АБСОЛЮТНЫЕ секунды исходного звука (от START до START+DUR).
# Частая ошибка: START>0, а LINES/SC/END посчитаны от нуля -> весь ролик проходит после END = чёрный экран.
words = [w[1] for line in spec["LINES"] for w in line]
end = spec["END"]
errs = []
if words and (min(words) < start - 1.0 or max(words) > start + dur + 0.5):
    errs.append(f"слова LINES в {min(words):.2f}..{max(words):.2f}, а ролик идёт {start:.2f}..{start + dur:.2f}")
if not (start + dur - 2.0 <= end[0] <= start + dur):
    errs.append(f"END={end} должен быть в конце ролика (~{start + dur - 0.4:.2f}..{start + dur:.2f})")
sc_starts = [a for a, b in spec["SC"]]
if sc_starts and (sc_starts[0] > start + 0.5 or sc_starts[-1] > start + dur):
    errs.append(f"SC начинаются в {sc_starts[0]:.2f}..{sc_starts[-1]:.2f}, ролик {start:.2f}..{start + dur:.2f}")
if errs:
    sys.exit("ОШИБКА ТАЙМКОДОВ в spec.py (все времена должны быть абсолютными секундами звука, START..START+DUR):\n  - "
             + "\n  - ".join(errs) + ("\n  Похоже, времена посчитаны от нуля — прибавь START ко всем таймкодам." if start > 1 and words and max(words) < dur else ""))
if lk: h = h.replace("</body>", f"<script>window.LK={json.dumps(lk, ensure_ascii=False)};"
              f"window.LSIDE={json.dumps(spec.get('LSIDE', 'L'))};</script><script>{(F / 'char.js').read_text()}</script></body>")
h = re.sub(r"(#sub\{position:absolute;top:)\d+px", r"\g<1>88px", h)
h = h.replace("</body>", f"<script>window.SONG={json.dumps(spec.get('SONG', ''), ensure_ascii=False)};"
              f"window.DUR={dur + start};</script><script>{(F / 'bars.js').read_text()}</script></body>")
(jd / "scene_final.html").write_text(h)
print("ok", jd, "DUR", dur, "FADE", spec["FADE"], "START", start)
