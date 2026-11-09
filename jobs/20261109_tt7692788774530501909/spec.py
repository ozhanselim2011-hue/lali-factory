DUR=19.9
FADE=19.5
START=0
SONG='МАЯК — Украсть тебя'
BG='linear-gradient(180deg,#0a0c16,#030306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Чтобы",0.0],["стать",0.3],["счастливым,",0.66],["мне",1.48],["надо",1.64],["просто",2.04],["украсть",2.64],["тебя",3.3]],
 [["я",3.62],["хочу",4.1],["с",4.52],["тобой",4.78],["состариться",5.04],["в",6.1],["тесном",6.24],["уютном",6.82],["доме",7.38]],
 [["спать,",7.96],["пока",8.52],["мы",8.8],["не",9.08],["выспимся",9.36]],
 [["жить,",10.02],["будто",10.48],["мы",10.78],["затворники",11.04]],
 [["пить,",11.98],["танцевать",12.52],["по",13.2],["вторникам",13.3]],
 [["утром",14.14],["прямо",14.66],["до",14.88],["полдня",15.28]],
 [["целоваться",15.88],["под",17.04],["звёздами",17.28]],
 [["с",17.92],["чувством,",18.08],["что",18.58],["мы",18.7],["свободны",18.94]],
]
SC=[[-0.3,3.55],[3.55,7.9],[7.9,9.95],[9.95,11.9],[11.9,14.05],[14.05,15.8],[15.8,17.85],[17.85,99]]
GLOW=['#3a3a3a','#7a4a1a','#1a2a7a','#3a3a5a','#7a1f6a','#7a6a1a','#1a1a6a','#1a6a5a']
PEMO=['💰','🏡','😴','🔒','🪩','☀️','✨','🕊️']
END=[19.5,19.9]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr">План операции</div><div class="ttl">Ограбление века</div>
 <div id="pl1" style="position:absolute;left:30px;right:30px;top:150px;font-size:26px;font-weight:800;line-height:1.7"></div>
 <div class="ch" data-p="a"></div><div id="bg1" style="position:absolute;left:400px;top:470px;font-size:80px;z-index:6">💰</div>
</div>
<div class="card" id="c2" style="background:#fff;color:#111">
 <div style="height:260px;background:linear-gradient(180deg,#9fd3ff,#d8f0ff);position:relative"><div style="position:absolute;left:200px;top:40px;font-size:190px">🏡</div></div>
 <div style="padding:16px 24px"><div style="font-size:32px;font-weight:900">Уютный домик · 18 м²</div><div style="font-size:22px;color:#8e8e93;font-weight:700">тесно, но вдвоём ❤️</div>
 <div style="font-size:24px;font-weight:800;margin-top:10px">Вместе: <span id="yr2" class="mono" style="color:#ff2d55">0 лет</span></div></div>
 <div class="ch" data-p="b"></div><div class="ch" data-p="c"></div>
</div>
<div class="card" id="c3" style="background:#000">
 <div class="hdr" style="color:#ff9f0a">Будильники</div>
 <div id="al3" style="position:absolute;left:24px;right:24px;top:80px"></div>
 <div class="ch" data-p="d"></div><div id="zz3" style="position:absolute;left:330px;top:440px;font-size:50px;z-index:6">💤</div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div class="hdr">Статус</div><div class="ttl" style="font-size:36px">🔕 был(а) давно</div>
 <div id="lk4" style="position:absolute;left:380px;top:200px;font-size:120px">🚪</div>
 <div id="nt4" style="position:absolute;left:24px;right:24px;top:140px;background:rgba(60,60,64,.95);border-radius:22px;padding:14px 18px;font-size:22px;font-weight:800;opacity:0;z-index:7">📦 Доставка: «оставьте у двери, не звоните»</div>
 <div class="ch" data-p="e"></div>
</div>
<div class="card" id="c5" style="background:linear-gradient(180deg,#2a0a3a,#0a0214)">
 <div id="wk5" style="position:absolute;left:20px;right:20px;top:30px;display:grid;grid-template-columns:repeat(7,1fr);gap:6px"></div>
 <div id="db5" style="position:absolute;left:250px;top:120px;font-size:100px">🪩</div>
 <div class="ch" data-p="f"></div><div class="ch" data-p="g"></div>
</div>
<div class="card" id="c6" style="background:linear-gradient(180deg,#ffe29a,#ffb347);color:#3a2000">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Утро</div><div class="ttl mono" id="ck6">06:00</div>
 <div id="sn6" style="position:absolute;font-size:110px">☀️</div>
 <div class="ch" data-p="h"></div><div style="position:absolute;left:330px;top:520px;font-size:60px;z-index:6">☕</div>
</div>
<div class="card" id="c7" style="background:linear-gradient(180deg,#05082a,#1a1050)">
 <div id="st7" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="i"></div><div class="ch" data-p="j"></div>
 <div id="hr7" style="position:absolute;left:265px;top:330px;font-size:70px;opacity:0;z-index:6">💋</div>
</div>
<div class="card" id="c8" style="background:linear-gradient(180deg,#7fd4ff,#e9f8ff);color:#06243a">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Уведомления</div>
 <div id="n8a" style="position:absolute;left:24px;right:24px;top:80px;background:#fff;border-radius:22px;padding:14px 18px;font-size:24px;font-weight:800;opacity:0">💼 Дедлайны: 0</div>
 <div id="n8b" style="position:absolute;left:24px;right:24px;top:160px;background:#fff;border-radius:22px;padding:14px 18px;font-size:24px;font-weight:800;opacity:0">⏰ Будильники: удалены</div>
 <div id="n8c" style="position:absolute;left:24px;right:24px;top:240px;background:#30d158;color:#fff;border-radius:22px;padding:14px 18px;font-size:26px;font-weight:900;opacity:0">🕊️ Свобода: 100%</div>
 <div id="bd8" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="k"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 $('pl1').innerHTML=['1. найти самую лучшую','2. отвлечь шутками','3. украсть её сердце 💖'].map((s,i)=>`<div id="p1_${i}" style="opacity:0">${s}</div>`).join('');
 $('al3').innerHTML=['07:00','07:05','07:10','07:15'].map((s,i)=>`<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #2c2c2e;padding:8px 0"><span class="mono" style="font-size:44px">${s}</span><div style="width:80px;height:46px;border-radius:23px;background:#2c2c2e;position:relative"><div id="a3_${i}" style="position:absolute;top:3px;width:40px;height:40px;border-radius:50%;background:#fff"></div></div></div>`).join('');
 $('wk5').innerHTML=['пн','вт','ср','чт','пт','сб','вс'].map((d,i)=>`<div id="w5_${i}" style="border-radius:12px;padding:8px 0;text-align:center;font-size:22px;font-weight:900;background:#2c2c2e">${d}</div>`).join('');
 let s='';for(let i=0;i<40;i++)s+=`<div id="s7_${i}" style="position:absolute;left:${rnd(i)*580}px;top:${rnd(i+7)*400}px;font-size:${10+rnd(i+3)*20}px;color:#fff">✦</div>`;$('st7').innerHTML=s;
 let b='';for(let i=0;i<6;i++)b+=`<div id="b8_${i}" style="position:absolute;font-size:44px">🕊️</div>`;$('bd8').innerHTML=b;})();
'''
RENDER='''
 {[0.66,1.64,2.64].forEach((s,i)=>$('p1_'+i).style.opacity=seg(t,s,s+.12));place('a',230,690,1.0,false);pose('a',t>=3.3?{aL:8,aR:-120,open:1}:walk(t,8));
  $('bg1').style.transform=`scale(${1+.3*pop(t,3.3,6)})`;}
 {const y=Math.round(eo(seg(t,5.04,7.4))*60);$('yr2').textContent=y+' лет';place('b',230,690,.85,false);place('c',370,690,.85,true);
  const old=y>30;pose('b',old?{aL:8,aR:-8,hd:6,bob:4}:{aL:8,aR:-8});pose('c',old?{aL:8,aR:-8,hd:6,bob:4}:{aL:8,aR:-8});
  ['b','c'].forEach(p=>$('ch_'+p).style.filter=`grayscale(${y/100})`);}
 {for(let i=0;i<4;i++){const o=seg(t,8.2+i*.3,8.35+i*.3);$('a3_'+i).style.left=(39-o*36)+'px';$('a3_'+i).parentNode.style.background=o<.5?'#30d158':'#2c2c2e';}
  place('d',340,600,1.0,false,-90);pose('d',{aL:8,aR:-8});$('zz3').style.transform=`translateY(${-((t*1.2)%1)*40}px)`;$('zz3').style.opacity=1-((t*1.2)%1);}
 {$('nt4').style.opacity=seg(t,11.04,11.15);place('e',180,690,1.0,false);pose('e',t>=10.48?{aL:8,aR:-8,hd:8}:walk(t,8));
  $('lk4').textContent=t>=10.78?'🔒':'🚪';$('lk4').style.transform=`scale(${1+.3*pop(t,10.78,6)})`;}
 {for(let i=0;i<7;i++){const on=i==1&&t>=13.3;$('w5_'+i).style.background=on?'#ff2d78':'#2c2c2e';$('w5_'+i).style.transform=`scale(${on?1.15:1})`;}
  $('db5').style.transform=`rotate(${t*90}deg)`;const d=t>=12.52;place('f',190,690,.95,false);place('g',410,690,.95,true);
  pose('f',d?{aL:150*Math.sin(t*10),aR:-150*Math.cos(t*10),bob:-Math.abs(Math.sin(t*10))*12,open:1}:{aL:8,aR:-60});pose('g',d?{aL:150*Math.cos(t*10),aR:-150*Math.sin(t*10),bob:-Math.abs(Math.cos(t*10))*12,open:1}:{aL:8,aR:-60});}
 {const m=seg(t,14.14,15.7);const mins=360+m*360;$('ck6').textContent=String(Math.floor(mins/60)).padStart(2,'0')+':'+String(Math.floor(mins%60)).padStart(2,'0');
  $('sn6').style.left=lerp(40,440,m)+'px';$('sn6').style.top=(300-Math.sin(m*Math.PI)*180)+'px';place('h',230,690,1.0,false);pose('h',{aL:8,aR:-100,hd:-6});}
 {for(let i=0;i<40;i++)$('s7_'+i).style.opacity=.4+.6*Math.abs(Math.sin(t*3+i));const k=eo(seg(t,15.9,16.8));
  place('i',lerp(150,245,k),690,1.0,false);place('j',lerp(450,355,k),690,1.0,true);pose('i',{aL:8,aR:-50,hd:-8});pose('j',{aL:8,aR:-50,hd:-8});$('hr7').style.opacity=seg(t,16.8,17.0);$('hr7').style.transform=`scale(${1+.15*Math.sin(t*10)})`;}
 {['n8a','n8b','n8c'].forEach((id,i)=>{const s=[18.0,18.4,18.94][i];$(id).style.opacity=seg(t,s,s+.1);$(id).style.transform=`scale(${eb(seg(t,s,s+.25))})`;});
  place('k',300,690,1.1,false);pose('k',t>=18.94?{aL:120,aR:-120,open:1}:{aL:8,aR:-8});
  for(let i=0;i<6;i++){const k=seg(t,18.94+i*.05,19.9);const e=$('b8_'+i);e.style.opacity=k>0?1:0;e.style.left=(300+Math.cos(i)*k*300-20)+'px';e.style.top=(600-k*280-i*15)+'px';}}
'''
