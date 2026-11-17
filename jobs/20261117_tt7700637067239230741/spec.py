DUR=16.2
FADE=15.8
START=22.9
SONG='VITA CHIKOVANI — Сирена'
BG='linear-gradient(180deg,#06121e,#020408)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Согрей",23.14],["меня,",24.1],["море,",24.72]],
 [["согрей,",25.28],["согрей,",26.18],["согрей",27.12]],
 [["согрей",27.98],["меня,",28.52],["море,",28.66],["моё",29.16],["сердце",29.52],["согрей",30.16]],
 [["Я",30.84],["сирена,",31.3],["я",32.4],["уже",33.0],["в",33.9],["твоей",34.06],["голове",34.58]],
 [["Я",35.3],["сирена,",35.8],["я",36.6],["затащу",37.0],["тебя",37.8],["к",38.2],["себе",38.4]],
]
SC=[[22.6,27.9],[27.9,30.7],[30.7,35.2],[35.2,99]]
GLOW=['#1d3a5a','#7a0a2a','#1d5a5a','#0a3a6a']
PEMO=['🥶','❤️‍🔥','🧜‍♀️','🌊']
END=[38.7,39.1]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#9fc4e0,#5a8ab0 55%,#d9c9a8 55%)">
 <div class="hdr" style="color:#0a2a4a">Пляж · ноябрь</div>
 <div id="tm1" class="mono" style="position:absolute;right:30px;top:30px;font-size:60px;font-weight:900;color:#0a84ff">−5°</div>
 <div id="sr1" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="a"></div>
 <div id="sn1" style="position:absolute;left:30px;top:30px;font-size:80px;opacity:.3">☀️</div>
</div>
<div class="card" id="c2" style="background:radial-gradient(circle at 50% 40%,#3a0a1a,#0a0408)">
 <div id="ic2" class="c" style="top:120px;font-size:240px;filter:hue-rotate(180deg) saturate(.4) brightness(1.4)">❤️</div>
 <div id="ht2" class="c" style="top:120px;font-size:240px;opacity:0">❤️</div>
 <div id="dr2" style="position:absolute;inset:0"></div>
 <div id="tx2" class="c" style="top:450px;font:900 34px Inter;color:#ff453a;opacity:0">разморожено ✓</div>
</div>
<div class="card" id="c3" style="background:#0a1420">
 <div class="hdr" style="color:#64d2ff">Скан головы · Лали</div>
 <div style="position:absolute;left:150px;top:90px;width:300px;height:340px;border-radius:150px 150px 120px 120px;border:6px solid #64d2ff;box-shadow:0 0 30px #64d2ff inset"></div>
 <div id="mm3" class="c" style="top:190px;font-size:130px;opacity:0">🧜‍♀️</div>
 <div id="pc3" class="c" style="top:460px;font:900 34px Inter;color:#64d2ff">в голове: <span id="pv3">0</span>% сирена</div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#5ac8fa,#0a3a6a)">
 <div id="wv4" style="position:absolute;left:-40px;right:-40px;top:420px;height:300px;background:#0a4a8a;border-radius:50% 50% 0 0/30% 30% 0 0"></div>
 <div id="mm4" style="position:absolute;font-size:110px;z-index:6">🧜‍♀️</div>
 <svg id="rp4" width="600" height="690" style="position:absolute;inset:0;z-index:4"></svg>
 <div class="ch" data-p="b"></div>
 <div id="bu4" style="position:absolute;inset:0;z-index:7"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#111','#64d2ff','#0a84ff');});})();'''
RENDER='''
 {place('a',300,690,1.1,false,Math.sin(t*40)*2);pose('a',{aL:120,aR:-120,hd:Math.sin(t*30)*4,open:t>=24.1});$('ch_a').style.filter=`hue-rotate(${10*Math.sin(t)}deg) brightness(1.1) saturate(.7)`;
  const T=[25.28,26.18,27.12];$('sn1').style.opacity=.3+.2*T.filter(s=>t>=s).length;$('sn1').style.transform=`scale(${1+.3*T.reduce((a,s)=>a+pop(t,s,6),0)})`;$('tm1').textContent=(t>=27.12?'−2°':(t>=26.18?'−3°':(t>=25.28?'−4°':'−5°')));
  let s='';for(let i=0;i<20;i++){const p=((t*.4)+rnd(i))%1;s+=`<div style="position:absolute;left:${rnd(i+2)*600}px;top:${p*690}px;color:#fff;font-size:${14+rnd(i)*14}px">❄</div>`}$('sr1').innerHTML=s;}
 {const k=seg(t,28.52,30.16);$('ht2').style.opacity=k;$('ic2').style.opacity=1-k;$('ht2').style.transform=`scale(${1+.15*Math.abs(Math.sin(t*6))*k})`;$('tx2').style.opacity=seg(t,30.16,30.3);
  let d='';for(let i=0;i<8;i++){const p=((t-27.98)*1.2+rnd(i))%1;if(t>=27.98&&k<1)d+=`<div style="position:absolute;left:${200+rnd(i+3)*200}px;top:${350+p*200}px;width:10px;height:16px;border-radius:50%;background:#9fd3ff;opacity:${1-p}"></div>`}$('dr2').innerHTML=d;}
 {const v=t<31.3?0:Math.round(100*eo(seg(t,31.3,34.58)));$('pv3').textContent=v;$('mm3').style.opacity=seg(t,31.3,31.6);$('mm3').style.transform=`rotate(${Math.sin(t*3)*10}deg) scale(${.6+.4*v/100})`;}
 {const k=eo(seg(t,36.6,38.6));const lx=lerp(150,380,k),ly=lerp(690,760,k);place('b',lx,ly,1.0,false,lerp(0,-60,k));pose('b',{aL:150,aR:-150,open:1,lL:Math.sin(t*10)*20,lR:-Math.sin(t*10)*20});
  const mx=430,my=380+Math.sin(t*3)*12;$('mm4').style.left=mx+'px';$('mm4').style.top=my+'px';$('wv4').style.transform=`translateX(${Math.sin(t*2)*20}px)`;
  $('rp4').innerHTML=t>=35.8?`<path d="M${mx+20} ${my+60} Q${(mx+lx)/2} ${my+100+Math.sin(t*5)*20} ${lx+20} ${ly-300}" stroke="#ff2d78" stroke-width="6" fill="none"/>`:'';
  let b='';if(t>=37.8)for(let i=0;i<10;i++){const p=((t-37.8)*1.2+i/10)%1;b+=`<div style="position:absolute;left:${300+rnd(i)*160}px;top:${600-p*200}px;width:${8+rnd(i)*12}px;height:${8+rnd(i)*12}px;border-radius:50%;border:2px solid #fff;opacity:${1-p}"></div>`}$('bu4').innerHTML=b;}
'''
