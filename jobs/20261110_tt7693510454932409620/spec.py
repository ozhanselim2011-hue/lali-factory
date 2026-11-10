DUR=12.9
FADE=12.5
START=45.9
SONG='Jakone & Kiliana — Была, не была'
BG='linear-gradient(180deg,#0a0a14,#030306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["то",46.04],["мутки,",46.18],["темы,",46.98],["схемы,",47.44]],
 [["то",47.92],["где-то",48.06],["стены,",48.82],["стены",49.24]],
 [["между",49.64],["нами",50.1],["стены,",50.46],["стены,",51.06]],
 [["будто",51.5],["горы,",51.78],["степи,",52.48],["степи",53.0]],
 [["отпускаю",53.46],["это",54.3],["с",54.66],["богом,",54.88],["у",55.32],["нас",55.54],["разная",55.74],["дорога",56.42]],
 [["ты",57.14],["гуляй,",57.28],["где",57.86],["хочешь",58.0]],
]
SC=[[45.6,47.85],[47.85,49.58],[49.58,53.4],[53.4,57.08],[57.08,99]]
GLOW=['#5a5a1a','#3a3a3a','#1a4a7a','#7a5a1a','#1a5c2e']
PEMO=['📋','🧱','⛰️','🛣️','🚶']
END=[58.4,58.8]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Доска · план недели</div>
 <div id="nt1" style="position:absolute;left:30px;right:30px;top:80px;display:grid;grid-template-columns:repeat(3,1fr);gap:12px"></div>
 <svg id="ar1" width="600" height="690" style="position:absolute;left:0;top:0;z-index:3"></svg>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#1c1c1e">
 <div class="hdr">Уведомления</div>
 <div id="wl2" style="position:absolute;left:0;right:0;top:80px;height:520px"></div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:linear-gradient(180deg,#9fd3ff,#d8f0ff 55%,#c8b07a 56%,#a8905a)">
 <div id="mt3" style="position:absolute;left:210px;top:180px;font-size:150px;z-index:3;opacity:0">⛰️</div>
 <div id="wl3" style="position:absolute;left:270px;top:690px;width:60px;height:420px;background:repeating-linear-gradient(0deg,#b5651d 0 30px,#8a4a12 30px 34px);z-index:4"></div>
 <div class="ch" data-p="c"></div><div class="ch" data-p="d"></div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#ffb36b,#ffd9a8 50%,#8bc34a 51%,#5a8a2a)">
 <svg width="600" height="690" style="position:absolute"><path d="M300 690 L300 470 L80 360" stroke="#555" stroke-width="60" fill="none"/><path d="M300 470 L520 360" stroke="#555" stroke-width="60" fill="none"/></svg>
 <div style="position:absolute;left:250px;top:250px;width:16px;height:200px;background:#6b4a2a;z-index:3"></div>
 <div style="position:absolute;left:120px;top:250px;background:#fff;color:#111;border-radius:8px;padding:6px 12px;font-size:22px;font-weight:900;z-index:3">← твоя</div>
 <div style="position:absolute;left:280px;top:290px;background:#fff;color:#111;border-radius:8px;padding:6px 12px;font-size:22px;font-weight:900;z-index:3">моя →</div>
 <div id="bl4" style="position:absolute;font-size:70px;z-index:6">🎈</div>
 <div class="ch" data-p="e"></div><div class="ch" data-p="f"></div>
</div>
<div class="card" id="c5" style="background:#d8e6d0">
 <svg width="600" height="690" style="position:absolute"><path d="M0 220 L600 280 M0 480 L600 400 M170 0 L230 690 M430 0 L390 690" stroke="#fff" stroke-width="18"/></svg>
 <div id="hp5" style="position:absolute;font-size:60px;z-index:6">📍</div>
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#fff;color:#111;border-radius:22px;padding:12px 18px;font-size:24px;font-weight:800;z-index:7">📍 Она: <span style="color:#0a84ff">где хочет</span> · 🔕 геолокация не отслеживается</div>
 <div class="ch" data-p="g"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=(p=='d'||p=='f')?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 $('nt1').innerHTML=['📦 мутки','💡 темы','🗺️ схемы','💰 ещё схема','📞 созвон','🔁 перезвон'].map((s,i)=>`<div id="n1_${i}" style="height:90px;background:#ffd60a;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:900;transform:rotate(${i%2?3:-3}deg);opacity:0">${s}</div>`).join('');
 $('wl2').innerHTML=['🧱 стена: «занят»','🧱 стена: «перезвоню»','🧱 стена: «не сейчас»','🧱 стена: «потом»'].map((s,i)=>`<div id="s2_${i}" style="margin:0 24px 14px;background:repeating-linear-gradient(90deg,#b5651d 0 60px,#8a4a12 60px 64px);border-radius:12px;padding:14px 18px;font-size:24px;font-weight:900;opacity:0">${s}</div>`).join('');})();
'''
RENDER='''
 {const T=[46.18,46.5,46.98,47.2,47.44,47.6];for(let i=0;i<6;i++){$('n1_'+i).style.opacity=seg(t,T[i],T[i]+.1);}
  let s='';if(t>=47.44)s='<path d="M120 130 L300 260 L480 130 M300 260 L300 330" stroke="#d0021b" stroke-width="5" fill="none"/>';$('ar1').innerHTML=s;place('a',300,700,1.0,false);pose('a',t>=47.44?{aL:40,aR:-40,hd:Math.sin(t*12)*10,open:1}:{aL:8,aR:-60,hd:-6});}
 {const T=[48.06,48.82,49.24,49.4];for(let i=0;i<4;i++){$('s2_'+i).style.opacity=seg(t,T[i],T[i]+.1);$('s2_'+i).style.transform=`translateY(${(1-eo(seg(t,T[i],T[i]+.2)))*-20}px)`;}place('b',300,700,1.0,false);pose('b',{aL:8,aR:-8,hd:12});}
 {const w=eo(seg(t,50.1,51.0));$('wl3').style.top=lerp(690,190,w)+'px';const m=seg(t,51.78,52.2);$('mt3').style.opacity=m;$('wl3').style.opacity=1-m;
  const d=eo(seg(t,52.48,53.3));place('c',lerp(170,80,d),700,lerp(1,.7,d),false);place('d',lerp(430,520,d),700,lerp(1,.7,d),true);pose('c',{aL:8,aR:-60,hd:8});pose('d',{aL:8,aR:-60,hd:8});}
 {const k=seg(t,54.88,57.0);$('bl4').style.left=(280+Math.sin(t*3)*20)+'px';$('bl4').style.top=lerp(400,-80,k)+'px';
  const g=eo(seg(t,55.32,56.9));place('e',lerp(300,150,g),lerp(680,560,g),lerp(.8,.5,g),false);place('f',lerp(330,460,g),lerp(680,560,g),lerp(.8,.5,g),true);pose('e',walk(t,8));pose('f',walk(t,8));}
 {const a=t*1.5;$('hp5').style.left=(280+Math.cos(a)*180)+'px';$('hp5').style.top=(330+Math.sin(a*1.3)*130)+'px';place('g',150,700,.9,false);pose('g',{aL:8,aR:-150+Math.sin(t*12)*25,open:1});}
'''
