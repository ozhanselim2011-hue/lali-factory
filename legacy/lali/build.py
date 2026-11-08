import json,sys
sys.path.insert(0,'lali')
from scripts import V
js=open('lali/char.js').read()
for name,(d,dur,fs,start,keys) in V.items():
    h=open(f'{d}/scene.html').read()
    inj=f'<script>window.LK={json.dumps(keys,ensure_ascii=False)};</script><script>{js}</script>'
    h=h.replace('</body>',inj+'</body>')
    open(f'{d}/scene_lali.html','w').write(h)
    print(name,d,dur,fs,start)
