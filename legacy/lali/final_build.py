import re,json
songs=dict(l.strip().split('|',1) for l in open('final_list.txt') if l.strip())
rows=[l.split() for l in open('lali/list.txt')]
V=[(n+'_lali',d,f'{d}/scene_lali.html',dur,fs,st) for n,d,dur,fs,st in rows]
V+=[('lali_superfresh_lali','v11c','v11c/scene.html','12.9','12.55','0'),('aktrisa_moih_snov_lali','v21','v21/scene.html','11.84','11.45','0'),
('zaytsy_lali','v22','v22/scene.html','17.0','16.6','0'),('butik_lali','v23','v23/scene.html','17.1','16.75','0'),('sneg_idet_lali','v24','v24/scene.html','27.4','26.9','0'),
('puli_lali','v25','v25/scene.html','17.88','17.45','0'),('sledopyt_lali','v26','v26/scene.html','14.95','14.6','0'),('tayny_klan_lali','v27','v27/scene.html','17.65','17.3','0'),
('remen_lali','v28','v28/scene.html','12.54','12.15','0'),('ne_mogu_proigrat_lali','v29','v29/scene.html','18.93','18.45','0'),('yuvelirka_lali','v30','v30/scene.html','15.06','14.7','0')]
js=open('lali/bars.js').read();out=open('lali/final_jobs.txt','w')
for n,d,h,dur,fs,st in V:
    s=open(h).read()
    s=re.sub(r'(#sub\{position:absolute;top:)\d+px',r'\g<1>88px',s)
    inj=f'<script>window.SONG={json.dumps(songs.get(n,""),ensure_ascii=False)};window.DUR={float(dur)+float(st)};</script><script>{js}</script>'
    s=s.replace('</body>',inj+'</body>')
    fh=f'{d}/scene_final_{n}.html';open(fh,'w').write(s)
    out.write(f'{n} {d} {fh} {dur} {fs} {st}\n')
print(len(V))
