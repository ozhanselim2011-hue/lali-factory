#!/bin/bash
# mk.sh name dir dur fadeStart start
S=/tmp/claude-0/-home-user/96f63366-517a-5367-82f7-d6acd5276a59/scratchpad;cd $S
n=$1;d=$2;dur=$3;fs=$4;st=$5;fr=$S/$d/frl;rm -rf "$fr";mkdir -p "$fr"
START=$st node rend3.js $d/scene_lali.html $fr $dur || exit 1
fd=$(python3 -c "print(round($dur-$fs,2))")
ffmpeg -v error -y -framerate 30 -i $fr/f_%04d.jpg -ss $st -i $d/in.mp4 -i wm.png -filter_complex "[2:v]format=rgba,colorchannelmixer=aa=0.85[w];[0:v][w]overlay=(W-w)/2:H-h-26[v]" -map "[v]" -map 1:a -t $dur -c:v libx264 -preset medium -crf 19 -pix_fmt yuv420p -c:a aac -b:a 192k -af "afade=t=out:st=$fs:d=$fd" -movflags +faststart /home/user/lali/${n}_lali.mp4 && rm -rf "$fr" && echo DONE $n
