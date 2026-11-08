#!/bin/bash
# factory/make.sh jobs/<id>   ->  jobs/<id>/out.mp4   (нужен jobs/<id>/spec.py)
set -e
F=$(cd "$(dirname "$0")" && pwd); jd=$(cd "$1" && pwd)
read dur fs st < <(python3 -c "s={'HELPERS':'$F/helpers.js'};exec(open('$jd/spec.py').read(),s);print(s['DUR'],s['FADE'],s.get('START',0))")
python3 "$F/build.py" "$jd"
fr="$jd/frames"; rm -rf "$fr"; mkdir -p "$fr"
node "$F/render.js" "$jd/scene_final.html" "$fr" "$dur" "$st"
fd=$(python3 -c "print(round($dur-$fs,2))")
ffmpeg -v error -y -framerate 30 -i "$fr/f_%04d.jpg" -ss "$st" -i "$jd/in.mp4" -map 0:v -map 1:a -t "$dur" \
  -c:v libx264 -preset medium -crf 19 -pix_fmt yuv420p -c:a aac -b:a 192k -af "afade=t=out:st=$fs:d=$fd" \
  -movflags +faststart "$jd/out.mp4"
rm -rf "$fr"
# Контроль: ролик не должен быть чёрным (кроме финального затемнения ~0.4 с)
blk=$(ffmpeg -v info -i "$jd/out.mp4" -vf "blackdetect=d=0.3:pix_th=0.08" -an -f null - 2>&1 | grep -o 'black_duration:[0-9.]*' | cut -d: -f2 | python3 -c "import sys;print(round(sum(float(x) for x in sys.stdin.read().split() or [0]),2))")
if python3 -c "import sys;sys.exit(0 if float('$blk')>1.0 else 1)"; then
  echo "ОШИБКА: в ролике ${blk} с чёрного экрана — проверь таймкоды spec.py (START, END, SC). Видео НЕ отправлять."; exit 3
fi
echo "DONE $jd/out.mp4 (чёрного: ${blk} с)"
