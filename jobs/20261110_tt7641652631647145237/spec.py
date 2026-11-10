DUR=17.6
FADE=17.2
START=40.6
SONG='By Индия, Xcho & МОТ — Шадэ'
BG='linear-gradient(180deg,#070a1a,#020306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Сонными",40.82],["глазами",41.64],["твоими",42.66],["лунными",43.32]],
 [["ночами,",44.1],["днями",45.14],["безумными",45.5]],
 [["я",46.48],["проживаю",47.12],["с",47.92],["тобой",48.08]],
 [["играя",48.46],["струнами",50.46],["моей",51.32],["души",52.16]],
 [["и",52.64],["минутами",52.78],["передвигая",53.8],["маршрутами",55.06]],
 [["снова",56.08],["любуюсь",56.86],["тобой",57.72]],
]
SC=[[40.3,44.05],[44.05,46.42],[46.42,48.42],[48.42,52.6],[52.6,56.02],[56.02,99]]
GLOW=['#1a2a6a','#5a3a1a','#7a1f4a','#5a1d7a','#1a5c4e','#7a1f4a']
PEMO=['🌙','🔄','🏠','🎸','🗺️','😍']
END=[57.8,58.2]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:radial-gradient(circle at 50% 30%,#1a2a5a,#02030a)">
 <div id="st1" style="position:absolute;inset:0"></div>
 <div id="mn1" style="position:absolute;left:230px;top:70px;font-size:130px">🌙</div>
 <div class="ch" data-p="a"></div>
 <div id="ey1" class="c" style="top:300px;font-size:30px;font-weight:900;color:#ffd60a;opacity:0;z-index:6">её глаза: лунный режим 🌕</div>
</div>
<div class="card" id="c2" style="background:#87ceeb" id2="sky">
 <div id="sk2" style="position:absolute;inset:0"></div>
 <div id="sn2" style="position:absolute;font-size:100px;z-index:3">☀️</div><div id="mo2" style="position:absolute;font-size:90px;z-index:3">🌙</div>
 <div class="c mono" id="dc2" style="top:30px;font-size:36px;font-weight:900;z-index:6">день 1</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#f4ecd8;color:#2a1f10">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Совместная жизнь</div><div class="ttl mono" id="dy3">0 дней</div>
 <div style="position:absolute;left:180px;top:200px;font-size:200px">🏠</div>
 <div class="ch" data-p="c"></div><div class="ch" data-p="d"></div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#3a1a0a,#140802)">
 <div class="hdr" style="color:#ffb340">Струны души</div>
 <svg id="sg4" width="600" height="300" style="position:absolute;left:0;top:90px"></svg>
 <div id="ht4" class="c" style="top:420px;font-size:90px">💖</div>
 <div class="ch" data-p="e"></div>
</div>
<div class="card" id="c5" style="background:#d8e6d0">
 <svg width="600" height="690" style="position:absolute"><path d="M0 220 L600 280 M0 480 L600 400 M170 0 L230 690 M430 0 L390 690" stroke="#fff" stroke-width="18"/><path id="rt5" d="M80 600 L200 250 L420 280 L500 120" stroke="#0a84ff" stroke-width="12" fill="none" stroke-dasharray="900" stroke-dashoffset="900"/></svg>
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#fff;color:#111;border-radius:22px;padding:12px 18px;font-size:26px;font-weight:800;z-index:7">🕒 <span id="mn5" class="mono">0</span> мин · маршрут «к ней»</div>
 <div id="pn5" style="position:absolute;font-size:56px;z-index:6">📍</div>
</div>
<div class="card" id="c6" style="background:#000">
 <div class="hdr">Галерея · Избранное</div>
 <div id="gl6" style="position:absolute;left:20px;right:20px;top:70px;display:grid;grid-template-columns:repeat(4,1fr);gap:6px"></div>
 <div id="ct6" class="c" style="top:470px;font-size:30px;font-weight:900;opacity:0;z-index:6;text-shadow:0 2px 10px #000">фото с ней: <span class="mono" id="n6">0</span> 😍</div>
 <div class="ch" data-p="f"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=p=='d'?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 let s='';for(let i=0;i<40;i++)s+=`<div style="position:absolute;left:${rnd(i)*590}px;top:${rnd(i+9)*500}px;width:3px;height:3px;border-radius:50%;background:#fff;opacity:${.3+rnd(i+2)*.7}"></div>`;$('st1').innerHTML=s;
 let g='';for(let i=0;i<12;i++)g+=`<div id="g6_${i}" style="aspect-ratio:1;border-radius:10px;background:linear-gradient(135deg,#ff8ac4,#5e2cff);display:flex;align-items:center;justify-content:center;font-size:40px;opacity:0">👩</div>`;$('gl6').innerHTML=g;})();
'''
RENDER='''
 {$('mn1').style.transform=`rotate(${Math.sin(t*1.5)*10}deg)`;$('ey1').style.opacity=seg(t,43.32,43.45);place('a',300,700,1.0,false);pose('a',{aL:8,aR:-8,hd:Math.sin(t*1.2)*10+8});}
 {const ph=(t-44.1)*1.6;const a=ph*Math.PI*2;$('sn2').style.left=(250+Math.cos(a)*230)+'px';$('sn2').style.top=(300+Math.sin(a)*230)+'px';$('mo2').style.left=(250-Math.cos(a)*230)+'px';$('mo2').style.top=(300-Math.sin(a)*230)+'px';
  const day=Math.sin(a)<0;$('c2').style.background=day?'#87ceeb':'#0a1030';$('dc2').textContent='день '+Math.max(1,Math.floor(ph+1));$('dc2').style.color=day?'#111':'#fff';
  place('b',300,700,1.0,false,Math.sin(t*10)*6);pose('b',{aL:60*Math.sin(t*8),aR:-60*Math.cos(t*8),open:1});}
 {const d=Math.round(eo(seg(t,47.12,48.3))*365);$('dy3').textContent=d+' дней';place('c',240,700,1.0,false);place('d',360,700,1.0,true);pose('c',{aL:8,aR:-60,hd:-8});pose('d',{aL:8,aR:-60,hd:-8});}
 {let s='';const k=t>=50.46?1:.2;for(let i=0;i<6;i++){let p='';for(let x=0;x<=600;x+=10){const y=40+i*42+Math.sin(x*.05+t*30+i)*12*k*Math.exp(-((x-300)**2)/40000);p+=`${x},${y} `;}s+=`<polyline points="${p}" fill="none" stroke="#ffd9a8" stroke-width="${2+i*.6}"/>`;}$('sg4').innerHTML=s;
  $('ht4').style.transform=`scale(${1+.25*Math.abs(Math.sin(t*8))*(t>=52.16?1:.3)})`;place('e',120,700,.9,false);pose('e',{aL:8,aR:-90+Math.sin(t*14)*20,hd:-6});}
 {const k=seg(t,52.78,55.8);$('rt5').setAttribute('stroke-dashoffset',900*(1-k));$('mn5').textContent=Math.round(k*42);
  const P=[[80,600],[200,250],[420,280],[500,120]];const seg3=Math.min(2,Math.floor(k*3)),f=k*3-seg3;const x=lerp(P[seg3][0],P[seg3+1][0],f),y=lerp(P[seg3][1],P[seg3+1][1],f);$('pn5').style.left=(x-28)+'px';$('pn5').style.top=(y-56)+'px';}
 {for(let i=0;i<12;i++){$('g6_'+i).style.opacity=seg(t,56.1+i*.05,56.2+i*.05);}$('ct6').style.opacity=seg(t,56.86,56.96);$('n6').textContent=fmt(eo(seg(t,56.9,57.8))*999);
  place("f",470,720,.75,true);pose("f",t>=57.72?{aL:60,aR:-60,open:1,hd:-10}:{aL:8,aR:-100,hd:-10});}
'''
