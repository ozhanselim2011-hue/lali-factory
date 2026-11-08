#!/bin/bash
# usage: make.sh <dir> <duration> <fadeStart> <out.mp4>
S=/tmp/claude-0/-home-user/96f63366-517a-5367-82f7-d6acd5276a59/scratchpad
d=$1; dur=$2; fs=$3; out=$4
mkdir -p $S/$d/fr && cd $S && node rend2.js $d/scene.html $S/$d/fr $dur && \
ffmpeg -v error -y -framerate 30 -i $S/$d/fr/f_%04d.jpg -i $S/$d/in.mp4 -i $S/wm.png -filter_complex "[2:v]format=rgba,colorchannelmixer=aa=0.85[w];[0:v][w]overlay=(W-w)/2:H-h-26[v]" -map "[v]" -map 1:a -t $dur -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -af "afade=t=out:st=$fs:d=$(python3 -c "print(round($dur-$fs,2))")" -movflags +faststart $out && echo DONE $out
