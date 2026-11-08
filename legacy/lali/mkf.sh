#!/bin/bash
S=/tmp/claude-0/-home-user/96f63366-517a-5367-82f7-d6acd5276a59/scratchpad;cd $S
n=$1;d=$2;h=$3;dur=$4;fs=$5;st=$6;fr=$S/frames_final/$n;mkdir -p $fr
START=$st node rend3.js $h $fr $dur || exit 1
fd=$(python3 -c "print(round($dur-$fs,2))")
ffmpeg -v error -y -framerate 30 -i $fr/f_%04d.jpg -ss $st -i $d/in.mp4 -map 0:v -map 1:a -t $dur -c:v libx264 -preset medium -crf 19 -pix_fmt yuv420p -c:a aac -b:a 192k -af "afade=t=out:st=$fs:d=$fd" -movflags +faststart /home/user/final/${n%_lali}.mp4 && echo DONE $n
