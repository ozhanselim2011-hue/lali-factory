BG='linear-gradient(180deg,#1a0c16,#08040a)'
SUBW='700'
LINES=[
 [["и",0.0],["я",.1],["в",.2],["неё",.35],["влюблён,",.5],["но",1.2],["не",1.4],["могу",1.6],["сказать",2.1],["«люблю»",2.4]],
 [["прыгаю",3.1],["в",4.0],["бумер,",4.3],["рядом",5.1],["Пэрис",5.6],["Хилтон",6.2]],
 [["конечно",6.8],["же",7.3],["не",7.7],["настоящая,",7.9],["а",9.0],["только",9.1],["с",9.5],["виду",9.9]],
 [["она",10.5],["любит",11.0],["кокер,",11.7],["делает",12.5],["дороги",13.1]],
 [["а",14.3],["я",14.6],["всё",14.9],["прощаю",15.1],["ей",15.8],["за",16.1],["длинные",16.3],["ноги",16.9]],
]
SC=[[-0.3,3.0],[3.0,6.7],[6.7,10.4],[10.4,12.4],[12.4,14.2],[14.2,99]]
GLOW=['#7a1f4a','#1d2a6a','#5a3a1a','#6a4a1a','#1a4a3a','#7a2a4a']
PEMO=['💗','🎆','🪞','🐾','🛣️','🌸']
END=[18.2,18.69]
HTML='''
<div class="card" id="c1" style="background:#000">
 <div style="padding:30px 40px 20px;display:flex;align-items:center;gap:16px;border-bottom:1px solid #222"><div style="width:62px;height:62px;border-radius:50%;background:linear-gradient(135deg,#ff9ac1,#ff2d78);display:flex;align-items:center;justify-content:center;font-size:34px">👸</div><div style="font-size:28px;font-weight:800">Она 🌸</div></div>
 <div style="padding:26px 34px 0"><div class="bub" style="background:#262628">ты где?</div></div>
 <div id="sent1" style="position:absolute;right:34px;top:250px;opacity:0"><div class="bub" style="background:#0a84ff">скоро буду 🙂</div></div>
 <div id="del1" class="c" style="top:360px;font-size:24px;font-weight:700;color:#ff6fa8;opacity:0">«люблю» · удалено ×17</div>
 <div style="position:absolute;left:24px;right:24px;bottom:24px;height:76px;border-radius:38px;border:2px solid #3a3a3c;display:flex;align-items:center;padding:0 26px;font-size:28px;font-weight:500"><span id="in1"></span><span id="cu1" style="width:3px;height:30px;background:#0a84ff;margin-left:2px"></span></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#14182a,#05060c)">
 <div class="hdr">Wallet · Ключ от машины</div>
 <div id="key" style="position:absolute;left:40px;right:40px;top:90px;height:230px;border-radius:30px;background:linear-gradient(135deg,#1c3a7a,#0a1430);box-shadow:0 20px 50px rgba(0,0,0,.6),inset 0 0 0 2px rgba(255,255,255,.12);padding:28px">
  <div style="font-size:34px;font-weight:900">БУМЕР</div><div id="ks" style="font-size:22px;color:#aeaeb2;font-weight:700;margin-top:6px">🔒 закрыто</div><div style="position:absolute;right:28px;bottom:16px;font-size:110px">🚘</div></div>
 <div id="seat" style="position:absolute;left:30px;right:30px;top:360px;background:#1c1c1e;border-radius:26px;padding:22px 24px;display:flex;gap:18px;align-items:center;opacity:0">
  <div style="width:90px;height:90px;border-radius:50%;background:linear-gradient(135deg,#ffe0f0,#ff9ac1);display:flex;align-items:center;justify-content:center;font-size:54px">👱‍♀️</div>
  <div><div style="font-size:20px;color:#8e8e93;font-weight:700">рядом</div><div id="ph" style="font-size:34px;font-weight:900"></div></div></div>
</div>
<div class="card" id="c3" style="background:#000">
 <div class="c" style="top:44px;font-size:24px;font-weight:700;color:#8e8e93">Проверка подлинности</div>
 <div style="position:absolute;left:150px;top:110px;width:300px;height:300px;border-radius:30px;background:radial-gradient(circle at 50% 40%,#3a2a3a,#0a060a);display:flex;align-items:center;justify-content:center;font-size:190px;overflow:hidden" id="fc3">👱‍♀️
  <div id="scan3" style="position:absolute;left:0;right:0;height:6px;background:#64d2ff;box-shadow:0 0 30px #64d2ff"></div></div>
 <div class="c" style="top:450px"><div id="r3" style="font-size:40px;font-weight:900">сканирование…</div><div id="r3b" style="font-size:24px;color:#8e8e93;font-weight:600;margin-top:8px"></div></div>
</div>
<div class="card" id="c4" style="background:#000">
 <div class="hdr">Фото › Люди и питомцы</div>
 <div style="position:absolute;left:100px;top:90px;width:400px;height:400px;border-radius:30px;background:radial-gradient(circle at 50% 40%,#4a3420,#140c06);display:flex;align-items:center;justify-content:center;font-size:250px" id="dog">🐕</div>
 <div class="c" style="top:520px"><div style="font-size:22px;color:#8e8e93;font-weight:700">она любит</div><div id="dn" style="font-size:54px;font-weight:900;color:#ff9f0a"></div></div>
 <div id="hh" style="position:absolute;inset:0;pointer-events:none"></div>
</div>
<div class="card" id="c5" style="background:#1d2620">
 <svg width="600" height="690" style="position:absolute;inset:0"><g id="roads" fill="none" stroke="#e5e5ea" stroke-width="14" stroke-linecap="round"></g></svg>
 <div id="cr" style="position:absolute;font-size:52px;margin:-26px">🚧</div>
 <div style="position:absolute;left:24px;right:24px;bottom:24px;background:rgba(30,30,32,.95);border-radius:28px;padding:22px 28px"><div style="font-size:30px;font-weight:800">Карты · новые дороги</div><div id="rc" class="mono" style="font-size:22px;color:#30d158;font-weight:700;margin-top:4px">построено: 0 км</div></div>
</div>
<div class="card" id="c6" style="background:#1c1c1e">
 <div id="al6" style="position:absolute;left:50px;right:50px;top:60px;background:rgba(44,44,46,.98);border-radius:30px;text-align:center;overflow:hidden">
  <div style="padding:28px"><div style="font-size:30px;font-weight:900">Простить всё?</div><div style="font-size:21px;color:#aeaeb2;margin-top:6px;font-weight:500">Обиды будут удалены без возможности восстановления.</div></div>
  <div style="display:flex;border-top:1px solid #48484a"><div style="flex:1;padding:20px;font-size:26px;color:#0a84ff;border-right:1px solid #48484a">Отмена</div><div id="fg" style="flex:1;padding:20px;font-size:26px;font-weight:800;color:#ff2d78">Простить</div></div></div>
 <div style="position:absolute;left:40px;right:40px;top:330px">
  <div style="font-size:22px;color:#8e8e93;font-weight:700">📏 Рулетка · её ноги</div>
  <div style="position:relative;height:90px;margin-top:16px"><div style="position:absolute;left:0;right:0;top:40px;height:4px;background:#3a3a3c"></div><div id="ml" style="position:absolute;left:0;top:34px;height:16px;border-radius:8px;background:#ffd60a;width:0;box-shadow:0 0 20px #ffd60a"></div></div>
  <div id="mv" class="c mono" style="position:relative;font-size:56px;font-weight:800">0 см</div></div>
 <div id="pr6" class="c" style="bottom:40px;font-size:28px;font-weight:900;color:#ff6fa8;opacity:0">всё прощено 🌸</div>
</div>
'''
BUILD='''(function(){let h='';for(let i=0;i<8;i++)h+=`<div id="hh${i}" style="position:absolute;left:${80+rnd(i)*440}px;top:480px;font-size:50px;opacity:0">${['💗','🐾','💗','🦴','💗','🐾','💗','🦴'][i]}</div>`;$('hh').innerHTML=h;
 const R=['M-10 120 C 150 160 300 80 610 140','M80 -10 C 120 200 60 400 140 700','M-10 420 C 200 380 400 460 610 380','M420 -10 C 380 200 480 400 400 700','M-10 260 L 610 300'];
 $('roads').innerHTML=R.map((d,i)=>`<path id="rd${i}" d="${d}" stroke-dasharray="1200" stroke-dashoffset="1200"/>`).join('');})();'''
RENDER='''
 {const q='люблю';let s='';const cyc=[[1.2,1.6],[1.7,2.0],[2.1,2.7]];for(const [a,b] of cyc){if(t>=a&&t<b){const u=(t-a)/(b-a);s=u<.6?q.slice(0,Math.ceil(u/.6*5)):q.slice(0,Math.max(0,Math.ceil((1-u)/.4*5)))}}
  $('in1').textContent=t>=2.4&&t<2.7?q:s;$('cu1').style.opacity=Math.floor(t*4)%2?1:.2;$('del1').style.opacity=seg(t,2.6,2.75);$('sent1').style.opacity=seg(t,2.75,2.9);}
 {const o=t>=3.1;$('ks').textContent=o?'🔓 открыто · прыгай':'🔒 закрыто';$('ks').style.color=o?'#30d158':'#aeaeb2';$('key').style.transform=`scale(${1+.06*pop(t,3.1,6)}) rotate(${Math.sin(t*2)*2}deg)`;
  $('seat').style.opacity=seg(t,5.1,5.25);const n='Пэрис Хилтон';$('ph').textContent=t<5.6?'…':n.slice(0,Math.min(n.length,Math.floor((t-5.6)*20)));}
 {$('scan3').style.top=(Math.abs(Math.sin(t*3))*290)+'px';const f=t>=7.9;$('r3').textContent=f?'✕ НЕ НАСТОЯЩАЯ':'сканирование…';$('r3').style.color=f?'#ff453a':'#fff';
  $('r3b').textContent=t>=9.9?'совпадение только с виду · 51%':(f?'копия':'');$('fc3').style.filter=f?`hue-rotate(${Math.sin(t*20)*30}deg)`:'none';if(si==2)shake('c3',t,7.9,8);}
 {const n='Кокер ❤️';$('dn').textContent=t<11.7?'':n.slice(0,Math.min(n.length,Math.floor((t-11.7)*25)+1));$('dog').style.transform=`scale(${1+.15*pop(t,11.7,5)}) rotate(${Math.sin(t*6)*5}deg)`;
  for(let i=0;i<8;i++){const st=11.75+i*.07;const ph=seg(t,st,st+.6);$('hh'+i).style.opacity=ph>0&&ph<1?1-ph:0;$('hh'+i).style.transform=`translateY(${-ph*240}px)`;}}
 {let km=0;for(let i=0;i<5;i++){const st=12.5+i*.25;const p=eo(seg(t,st,st+.6));$('rd'+i).setAttribute('stroke-dashoffset',1200*(1-p));km+=p*12;}
  const L=$('rd'+Math.min(4,Math.max(0,Math.floor((t-12.5)/.25))));try{const len=L.getTotalLength();const p=eo(seg(t,12.5+Math.min(4,Math.max(0,Math.floor((t-12.5)/.25)))*.25,12.5+Math.min(4,Math.max(0,Math.floor((t-12.5)/.25)))*.25+.6));const pt=L.getPointAtLength(len*p);$('cr').style.left=pt.x+'px';$('cr').style.top=pt.y+'px';}catch(e){}
  $('rc').textContent='построено: '+km.toFixed(0)+' км';}
 {const f=t>=15.1;$('fg').style.background=f?'#ff2d78':'transparent';$('fg').style.color=f?'#fff':'#ff2d78';$('fg').textContent=f?'Прощено ✓':'Простить';
  const m=eo(seg(t,16.3,16.95));$('ml').style.width=(m*100)+'%';$('mv').textContent=Math.round(m*120)+' см';$('mv').style.color=t>=16.9?'#ffd60a':'#fff';$('mv').style.transform=`scale(${1+.2*pop(t,16.9,5)})`;$('pr6').style.opacity=seg(t,16.95,17.1);}
'''
