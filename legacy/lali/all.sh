cd /tmp/claude-0/-home-user/96f63366-517a-5367-82f7-d6acd5276a59/scratchpad
cat lali/list.txt | xargs -P 3 -L 1 bash -c 'lali/mk.sh "$0" "$1" "$2" "$3" "$4"' 
echo ALLDONE
