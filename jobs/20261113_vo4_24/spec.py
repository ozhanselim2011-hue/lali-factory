exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,4.4],[4.4,7.6],[7.6,9.95],[9.95,10.95],[10.95,13.15],[13.15,99]];GLOW=['#5a0a0a','#6a3a0a','#1d3a7a','#7a0a0a','#5a1d4a','#1d5a2a'];PEMO=['🪆','🥢','👂','🦝','🐕','🪑']
def lc(i,bg,inner,cap):return f'<div class="card" id="c{i}" style="background:{bg}"><div class="hdr">буквально:</div>{inner}<div class="c" style="bottom:30px;font:900 28px Inter;padding:0 20px">{cap}</div></div>'
HTML=lc(1,'#2a1a3a','<div id="mt" style="position:absolute;left:0;right:0;top:140px;display:flex;justify-content:center;align-items:flex-end;gap:8px"></div>','«во мне все четыре» — матрёшка')+\
 lc(2,'#3a2a1a','<div id="st2" class="c" style="top:150px;font-size:180px">🫦</div><div id="st2b" style="position:absolute;left:150px;top:230px;width:300px;height:22px;background:#a0522d;border-radius:10px"></div>','палку в зубы и закрутил')+\
 lc(3,'#1a2a4a','<div class="c" style="top:130px;font-size:170px">👂</div><div id="w3" style="position:absolute;left:0;right:0;top:360px;text-align:center;font:900 30px Inter"></div>','слышу у МС мои строчки')+\
 lc(4,'#3a0a0a','<div id="r4" style="position:absolute;top:180px;font-size:170px">🦝</div><div class="c" style="top:400px;font:800 24px Inter;color:#ffb3ad">несёт чужие строчки</div>','«они чё, тырят?» — енот')+\
 lc(5,'#3a1a3a','<div id="d5" class="c" style="top:150px;font-size:180px">🐕</div><div id="h5" class="c" style="top:380px;font-size:60px">👍</div>','с*ка (собака) делает хорошо')+\
 lc(6,'#1a3a2a','<div class="c" style="top:150px;font-size:200px">🪑</div><div id="f6" class="c" style="top:150px;font:900 150px Inter;color:#ffd60a;opacity:0">4</div>','садись на четыре ножки')
BUILD=''
RENDER='''
 {const T=[0.9,1.25,1.6,2.0];$('mt').innerHTML=T.map((s,i)=>`<div style="font-size:${150-i*22}px;opacity:${t>=s?1:.15};transform:scale(${1+.3*pop(t,s,8)})">🪆</div>`).join('');}
 {$('st2b').style.transform=`rotate(${t>=5.75?t*900:0}deg)`;$('st2').textContent=t>=7?'💥':'🫦';}
 {const w=['мои','строчки','мои','строчки'];$('w3').innerHTML=t>=9?w.map((x,i)=>`<span style="display:inline-block;margin:4px;opacity:${seg(t,9+i*.1,9.1+i*.1)}">${x}</span>`).join(''):'';}
 {$('r4').style.left=lerp(-200,620,seg(t,10.0,10.95))+'px';}
 {$('d5').style.transform=`rotate(${Math.sin(t*14)*10}deg)`;$('h5').style.transform=`scale(${1+.4*pop(t,12.25,6)})`;}
 {$('f6').style.opacity=seg(t,13.75,13.85);}
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
