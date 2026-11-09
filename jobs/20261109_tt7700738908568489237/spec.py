DUR=14.1
FADE=13.7
START=6.3
SONG='dabbackwood — назад в кресты'
BG='linear-gradient(180deg,#0a0a12,#030306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Бэквуд",6.46],["вернулся",7.02],["обратно",7.52],["в",7.86],["кресты",7.92]],
 [["я",8.24],["дарил",8.4],["цветы,",8.74],["но",9.14],["нет",9.26],["доброты",9.48]],
 [["в",9.88],["мире,",10.18],["где",10.44],["сотни",10.6],["таких",10.92],["же",11.12],["уродов",11.38]],
 [["я",11.86],["отличился",11.98],["среди",12.58],["идиотов",13.02]],
 [["мама",13.56],["не",13.88],["знает,",14.04],["что",14.34],["бэквуд",14.5],["сезон",14.76]],
 [["я",15.18],["правда",15.32],["был",15.6],["лучше,",15.82],["но",16.16],["не",16.26],["повезло",16.36]],
 [["просто",16.86],["работал",17.28],["и",17.88],["сделал",17.94],["всё",18.16],["сам",18.3]],
 [["но",18.58],["менты,",18.74],["как",18.94],["Москва,",19.08],["не",19.52],["верят",19.66],["слезам",19.94]],
]
SC=[[6.0,8.2],[8.2,9.85],[9.85,11.83],[11.83,13.52],[13.52,15.15],[15.15,16.83],[16.83,18.55],[18.55,99]]
GLOW=['#3a3a5a','#7a1f4a','#3a3a3a','#7a6a1a','#1a5c2e','#5a1d7a','#1a4a7a','#7a1f1f']
PEMO=['🔁','🥀','👥','👑','📱','🎲','🛠️','😢']
END=[20.0,20.4]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#e8eef4;color:#111">
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#0a84ff;color:#fff;border-radius:22px;padding:14px 18px;font-size:26px;font-weight:800;z-index:6">↩️ Маршрут: обратно<div id="ar1" style="font-size:20px;opacity:.85">через 3 мин</div></div>
 <svg width="600" height="690" style="position:absolute"><path d="M80 600 Q300 200 520 300" stroke="#0a84ff" stroke-width="14" fill="none" stroke-dasharray="20 14"/></svg>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#fff0f4;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Подарок</div>
 <div id="fl2" style="position:absolute;font-size:110px;z-index:6">💐</div>
 <div id="rt2" class="c" style="top:120px;font-size:30px;font-weight:900;color:#d0021b;opacity:0">↩️ возврат · доброты: 0</div>
 <div class="ch" data-p="b"></div><div class="ch" data-p="c"></div>
</div>
<div class="card" id="c3" style="background:#1c1c1e">
 <div class="hdr">Население мира</div>
 <div id="gr3" style="position:absolute;left:20px;right:20px;top:70px;display:grid;grid-template-columns:repeat(5,1fr);gap:4px"></div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div class="hdr">Население мира · поиск</div>
 <div id="gr4" style="position:absolute;left:20px;right:20px;top:70px;display:grid;grid-template-columns:repeat(5,1fr);gap:4px"></div>
 <div id="fd4" style="position:absolute;left:24px;right:24px;top:600px;background:#ffd60a;color:#111;border-radius:18px;padding:10px 14px;font-size:24px;font-weight:900;opacity:0;z-index:7">👑 найден 1 особенный</div>
</div>
<div class="card" id="c5" style="background:#000">
 <div class="hdr">Чат · Мама ❤️</div>
 <div id="m5a" style="position:absolute;left:24px;top:90px;background:#2c2c2e;border-radius:22px;padding:12px 18px;font-size:28px;font-weight:800;opacity:0">сынок, ты покушал? 🥺</div>
 <div id="m5b" style="position:absolute;right:24px;top:170px;background:#0a84ff;border-radius:22px;padding:12px 18px;font-size:28px;font-weight:800;opacity:0">да мам ☺️</div>
 <div id="po5" style="position:absolute;left:24px;right:24px;top:260px;background:linear-gradient(135deg,#ff9f0a,#ff2d55);border-radius:22px;padding:14px;font-size:30px;font-weight:900;text-align:center;opacity:0">🔥 СЕЗОН БЭКВУДА 🔥</div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c6" style="background:linear-gradient(180deg,#2a0a3a,#0a0214)">
 <div class="hdr">Рейтинг кандидатов</div>
 <div style="position:absolute;left:24px;right:24px;top:80px;font-size:28px;font-weight:900;line-height:1.8"><div>🧢 я — <span style="color:#30d158">9.9 ⭐</span></div><div>🤡 он — <span style="color:#ff453a">2.1 ⭐</span></div></div>
 <div id="dc6" style="position:absolute;left:380px;top:280px;font-size:110px">🎲</div>
 <div id="wn6" class="c" style="top:200px;font-size:30px;font-weight:900;color:#ff453a;opacity:0">выбрали: 🤡 он</div>
 <div class="ch" data-p="e"></div>
</div>
<div class="card" id="c7" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Проект «жизнь»</div><div class="ttl">Сделано сам: <span id="pc7" class="mono">0%</span></div>
 <div style="position:absolute;left:40px;right:40px;top:150px;height:24px;border-radius:12px;background:#ddd;overflow:hidden"><div id="pb7" style="height:24px;background:#30d158;width:0"></div></div>
 <div class="ch" data-p="f"></div><div id="hm7" style="position:absolute;left:390px;top:380px;font-size:80px;z-index:6">🔨</div>
</div>
<div class="card" id="c8" style="background:linear-gradient(180deg,#3a4a6a,#1a2030)">
 <div class="c" style="top:30px;font-size:26px;font-weight:800;color:#aeaeb2">Детектор слёз</div>
 <div id="nt8" class="c" style="top:70px;font-size:40px;font-weight:900;color:#ff453a;opacity:0">❌ НЕ ВЕРИМ</div>
 <div class="c" style="top:150px;font-size:110px;opacity:.5">🏙️</div>
 <div class="ch" data-p="g"></div>
 <div id="te8" style="position:absolute;inset:0;z-index:6"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=p=='c'?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 const cell=(id,i,g)=>`<div id="${id}_${i}" style="height:100px;border-radius:12px;background:#2c2c2e;display:flex;align-items:center;justify-content:center;font-size:56px;opacity:0">${g}</div>`;
 let a='',b='';for(let i=0;i<25;i++){a+=cell('q3',i,'🧍');b+=cell('q4',i,i==12?'😎':'🧍');}$('gr3').innerHTML=a;$('gr4').innerHTML=b;
 let t='';for(let i=0;i<10;i++)t+=`<div id="t8_${i}" style="position:absolute;font-size:30px">💧</div>`;$('te8').innerHTML=t;})();
'''
RENDER='''
 {const k=eo(seg(t,6.4,8.1));place('a',lerp(520,120,k),lerp(320,620,k),.7,true);pose('a',walk(t,10));$('ar1').textContent=t>=7.92?'📍 вы прибыли туда же, где были':'через 3 мин';}
 {const g=eo(seg(t,8.3,8.74)),r=eo(seg(t,9.14,9.6));$('fl2').style.left=lerp(150,330,g-r)+'px';$('fl2').style.top='330px';$('rt2').style.opacity=seg(t,9.26,9.4);
  place('b',150,690,.95,false);place('c',450,690,.95,true);pose('b',t>=9.48?{aL:8,aR:-8,hd:14}:{aL:8,aR:-70});pose('c',t>=9.14?{aL:8,aR:-150,hd:-10}:{aL:8,aR:-8});}
 {for(let i=0;i<25;i++){const s=10.0+i*.05;$('q3_'+i).style.opacity=seg(t,s,s+.1);}}
 {for(let i=0;i<25;i++){const e=$('q4_'+i);e.style.opacity=1;const sp=i==12&&t>=11.98;e.style.background=sp?'#ffd60a':'#2c2c2e';e.style.transform=`scale(${sp?1.2:1})`;e.style.filter=(!sp&&t>=12.58)?'grayscale(1) brightness(.5)':'none';}
  $('fd4').style.opacity=seg(t,13.02,13.15);}
 {$('m5a').style.opacity=seg(t,13.56,13.66);$('m5b').style.opacity=seg(t,14.04,14.14);$('po5').style.opacity=seg(t,14.5,14.6);$('po5').style.transform=`scale(${1+.15*pop(t,14.76,6)})`;
  place('d',300,700,1.0,false);pose('d',t>=14.76?{aL:60,aR:-60,open:1,bob:-Math.abs(Math.sin(t*10))*10}:{aL:8,aR:-80,hd:-6});}
 {$('dc6').style.transform=`rotate(${t<16.2?t*900:0}deg)`;$('wn6').style.opacity=seg(t,16.36,16.46);place('e',170,690,1.0,false);pose('e',t>=16.36?{aL:8,aR:-8,hd:16}:{aL:8,aR:-60});}
 {const k=eo(seg(t,17.28,18.3));$('pc7').textContent=Math.round(k*100)+'%';$('pb7').style.width=(k*100)+'%';$('hm7').style.transform=`rotate(${-30+Math.abs(Math.sin(t*12))*60}deg)`;
  place('f',230,690,1.0,false);pose('f',{aL:8,aR:-100+Math.sin(t*12)*30,hd:-6,open:t>=18.3?1:0});}
 {$('nt8').style.opacity=seg(t,19.52,19.62);$('nt8').style.transform=`scale(${1+.3*pop(t,19.52,6)})`;place('g',300,690,1.1,false);pose('g',{aL:8,aR:-8,hd:10,open:1});
  for(let i=0;i<10;i++){const ph=(t*1.8+i/10)%1;const e=$('t8_'+i);e.style.opacity=t>18.6?1-ph:0;e.style.left=(i%2?330:255)+'px';e.style.top=(390+ph*200)+'px';}}
'''
