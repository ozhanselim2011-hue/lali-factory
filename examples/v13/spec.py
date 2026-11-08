BG='linear-gradient(180deg,#0e0818,#050309)'
SUBW='800'
LINES=[
 [["я",0.0],["не",.2],["узнаю,",.3],["я",.9],["не",1.2],["поеду,",1.5],["если",2.0],["меня",2.2],["зовут",2.4],["куда-то",2.7]],
 [["хаслю",3.3],["в",3.8],["интернете,",3.85],["мне",4.3],["не",4.5],["приходит",4.6],["зарплата",5.1]],
 [["да,",5.5],["раньше",6.4],["делал",6.6],["много",7.0],["грязи",7.2]],
 [["и",7.7],["он",7.9],["ответит",8.1],["за",8.6],["слово,",8.7],["по*уй",9.0],["на",9.3],["его",9.4],["связи",9.7]],
 [["но",10.2],["потом",11.0],["его",11.3],["увезут",11.6],["в",12.2],["лес",12.3]],
 [["пару",12.7],["ешек",12.9],["у",13.3],["клуба",13.4],["и",13.8],["потом",13.85],["запрыгнул",14.1],["в",14.55],["Benz",14.6]],
 [["кто",14.9],["ты",15.7],["такой,",15.9],["я",16.4],["тебя",16.5],["не",16.7],["знаю",16.9]],
 [["надеюсь,",17.2],["я",17.9],["не",18.0],["буду",18.1],["знать,",18.3],["я",18.8],["не",18.9],["знаю,",19.0],["кто",19.3],["ты",19.5]],
 [["со",19.8],["мной",20.5],["Оксана,",20.7],["я",21.2],["засыпаю",21.4]],
 [["честно,",22.1],["за*бался",22.4],["уже",22.9],["жить",23.2],["с",23.4],["субботы",23.45],["по",23.9],["субботу",24.0]],
]
SC=[[-0.3,3.2],[3.2,5.4],[5.4,7.6],[7.6,10.1],[10.1,12.35],[12.35,14.8],[14.8,17.1],[17.1,19.65],[19.65,21.95],[21.95,99]]
GLOW=['#3a1d6a','#1a5c2e','#4a3a2a','#5a1d3a','#1a4a2a','#3a1d7a','#5a1a1a','#2a2a4a','#1d2a6a','#5a1d6a']
PEMO=['🚫','💻','🔒','🤝','🌲','🌃','📵','🙈','💤','🔁']
END=[24.25,24.6]
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr" style="color:#ff453a">Календарь</div><div class="ttl">Приглашения</div>
 <div id="inv" style="position:absolute;left:24px;right:24px;top:170px"></div>
</div>
<div class="card" id="c2" style="background:#000">
 <div class="hdr">Банк · Зачисления</div>
 <div id="zp" class="c mono" style="top:100px;font-size:84px;font-weight:800">0 ₽</div>
 <div id="zp2" class="c" style="top:200px;font-size:26px;font-weight:800;color:#8e8e93">зарплата · ожидается…</div>
 <div class="box" style="position:absolute;left:30px;right:30px;top:290px;background:#1c1c1e"><div style="display:flex;justify-content:space-between;font-size:26px;font-weight:800"><span>💻 Хаслю в интернете</span><span id="hs" class="mono" style="color:#30d158">0 ч</span></div>
  <div style="height:14px;border-radius:7px;background:#3a3a3c;margin-top:14px;overflow:hidden"><div id="hsb" style="height:14px;background:#30d158;width:0"></div></div></div>
 <div id="nz" style="position:absolute;left:30px;right:30px;top:440px;background:#3a0d12;border-radius:24px;padding:22px;font-size:28px;font-weight:900;color:#ff453a;opacity:0">✕ Зарплата не пришла<div style="font-size:21px;color:#ffb3ad;font-weight:600;margin-top:6px">и не придёт. хаслим дальше.</div></div>
</div>
<div class="card" id="c3" style="background:#000">
 <div class="hdr">Фото › Альбомы</div><div class="ttl">Скрытые</div>
 <div style="position:absolute;left:30px;right:30px;top:170px;height:300px;border-radius:26px;background:#1c1c1e;overflow:hidden">
  <div id="dg" style="position:absolute;inset:0;display:grid;grid-template-columns:repeat(4,1fr);gap:4px;padding:4px;filter:blur(14px)"></div>
  <div id="lk3" style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:90px">🔒<div style="font-size:24px;font-weight:800;margin-top:6px">Face ID</div></div></div>
 <div class="c" style="bottom:70px"><div style="font-size:34px;font-weight:900">Грязь · раньше</div><div id="cn3" class="mono" style="font-size:24px;color:#8e8e93;font-weight:700;margin-top:6px">0 объектов</div></div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div style="position:absolute;top:50px;left:50%;margin-left:-75px;width:150px;height:150px;border-radius:50%;background:#48484a;display:flex;align-items:center;justify-content:center;font-size:80px">🕴️</div>
 <div class="c" style="top:215px;font-size:38px;font-weight:800">Он</div>
 <div class="box" style="position:absolute;left:30px;right:30px;top:290px"><div style="display:flex;justify-content:space-between;font-size:26px;font-weight:800"><span>🤝 Связи</span><span id="sv" class="mono">0</span></div><div id="svs" style="font-size:22px;font-weight:800;color:#ff453a;margin-top:8px;opacity:0">по*уй ✕</div></div>
 <div id="ans" style="position:absolute;left:30px;right:30px;top:440px;height:90px;border-radius:26px;background:#0a84ff;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:900">↩︎ Ответит за слово</div>
</div>
<div class="card" id="c5" style="background:#1f2a22">
 <svg width="600" height="460" style="position:absolute;inset:0"><rect x="0" y="0" width="600" height="460" fill="#1d2620"/><g fill="#24402a">
  <circle cx="120" cy="90" r="70"/><circle cx="470" cy="120" r="90"/><circle cx="380" cy="300" r="110"/><circle cx="80" cy="330" r="80"/></g>
  <path id="rt5" d="M90 420 C 200 360 180 250 300 230 S 440 140 480 70" fill="none" stroke="#0a84ff" stroke-width="10" stroke-linecap="round" stroke-dasharray="1000" stroke-dashoffset="1000"/></svg>
 <div style="position:absolute;left:455px;top:28px;font-size:56px">🌲</div><div id="car5" style="position:absolute;font-size:44px;margin:-22px">🚙</div>
 <div style="position:absolute;left:24px;right:24px;bottom:24px;background:rgba(30,30,32,.95);border-radius:28px;padding:22px 28px"><div style="font-size:30px;font-weight:800">Его → Лес 🌲</div><div id="et5" style="font-size:21px;color:#8e8e93;font-weight:600;margin-top:4px">маршрут строится…</div></div>
</div>
<div class="card" id="c6" style="background:#000">
 <div id="cl6" class="c" style="top:60px;font-size:160px">🪩</div>
 <div class="c" style="top:250px;font-size:30px;font-weight:800">у клуба · 03:12</div>
 <div id="cp" style="position:absolute;left:30px;right:30px;top:330px;background:#1c1c1e;border-radius:28px;padding:26px;display:flex;gap:20px;align-items:center;opacity:0">
  <div style="width:90px;height:90px;border-radius:22px;background:linear-gradient(135deg,#30d158,#0a84ff);display:flex;align-items:center;justify-content:center;font-size:50px">🚘</div>
  <div><div style="font-size:30px;font-weight:900">CarPlay</div><div id="cpt" style="font-size:22px;color:#8e8e93;font-weight:600">подключение к «Benz»…</div></div></div>
</div>
<div class="card" id="c7" style="background:linear-gradient(180deg,#2a2a3a,#0c0c12)">
 <div class="c" style="top:80px;font-size:26px;font-weight:600;color:#aeaeb2">возможно, спам</div>
 <div class="c" style="top:120px;font-size:52px;font-weight:700">Неизвестный</div>
 <div class="c" style="top:200px;font-size:26px;font-weight:600;color:#aeaeb2" id="wh">кто ты такой?</div>
 <div style="position:absolute;left:0;right:0;bottom:80px;display:flex;justify-content:space-around">
  <div style="text-align:center"><div id="dec" style="width:120px;height:120px;border-radius:50%;background:#ff3b30;display:flex;align-items:center;justify-content:center;font-size:56px">📵</div><div style="font-size:22px;margin-top:8px;font-weight:600">Отклонить</div></div>
  <div style="text-align:center" id="accw"><div style="width:120px;height:120px;border-radius:50%;background:#30d158;display:flex;align-items:center;justify-content:center;font-size:56px">📞</div><div style="font-size:22px;margin-top:8px;font-weight:600">Принять</div></div></div>
 <div id="nk" class="c" style="top:300px;font-size:44px;font-weight:900;color:#ff453a;opacity:0">я тебя не знаю</div>
</div>
<div class="card" id="c8" style="background:#1c1c1e">
 <div class="hdr" style="color:#0a84ff">‹ Телефон</div><div class="ttl">Неизвестные</div>
 <div style="padding:30px 30px 0"><div class="row" style="background:#2c2c2e">🙈 <span>Заглушать неизвестных</span><div class="tg" id="tg8"><b></b></div></div>
  <div class="row" style="background:#2c2c2e">🔍 <span>Узнавать, кто это</span><div class="tg" id="tg9"><b></b></div></div></div>
 <div id="t8" class="c" style="bottom:70px;font-size:30px;font-weight:800;opacity:0">надеюсь, и не узнаю</div>
</div>
<div class="card" id="c9" style="background:#05050c">
 <div id="dim9" style="position:absolute;inset:0;background:radial-gradient(circle at 50% 30%,#1d2a6a,#05050c 70%)"></div>
 <div class="c" style="top:90px;font-size:130px;font-weight:700;letter-spacing:-4px" id="clk9">03:40</div>
 <div id="sl9" style="position:absolute;left:30px;right:30px;top:300px;background:rgba(60,60,80,.6);border-radius:28px;padding:20px 24px;display:flex;gap:16px;align-items:center;opacity:0"><div style="font-size:44px">🛏️</div><div><div style="font-size:26px;font-weight:800">Режим сна</div><div style="font-size:20px;color:#aeaeb2;font-weight:600">включён</div></div></div>
 <div id="ox" style="position:absolute;left:30px;right:30px;top:410px;background:rgba(60,60,80,.6);border-radius:28px;padding:20px 24px;display:flex;gap:16px;align-items:center;opacity:0"><div style="width:56px;height:56px;border-radius:50%;background:#bf5af2;display:flex;align-items:center;justify-content:center;font-size:30px">👩</div><div><div style="font-size:26px;font-weight:800">Оксана</div><div style="font-size:20px;color:#aeaeb2;font-weight:600">рядом с вами · 0 м</div></div></div>
 <div id="zz" class="c" style="bottom:60px;font-size:60px;opacity:0">💤</div>
</div>
<div class="card" id="c10" style="background:#1c1c1e">
 <div class="hdr" style="color:#ff453a">Календарь · Неделя</div>
 <div id="wk" style="position:absolute;left:24px;right:24px;top:90px"></div>
 <div id="rp" class="c" style="bottom:36px;font-size:26px;font-weight:900;color:#ff453a;opacity:0">🔁 повтор: суббота · всегда</div>
</div>
'''
BUILD='''(function(){
 const I=['🎉 Туса у Димы','🍾 ДР Кати','🌃 Выйдем?'];$('inv').innerHTML=I.map((n,i)=>`<div id="iv${i}" style="background:#2c2c2e;border-radius:22px;padding:18px 22px;margin-bottom:12px;opacity:0"><div style="font-size:26px;font-weight:800">${n}</div><div style="font-size:20px;color:#8e8e93;font-weight:600;margin-top:4px">тебя зовут · сегодня</div><div style="display:flex;gap:10px;margin-top:12px"><div style="flex:1;padding:10px;border-radius:12px;background:#3a3a3c;text-align:center;font-weight:800;color:#30d158">Поеду</div><div id="nd${i}" style="flex:1;padding:10px;border-radius:12px;background:#3a3a3c;text-align:center;font-weight:800;color:#ff453a">Не поеду</div></div></div>`).join('');
 let g='';for(let i=0;i<12;i++)g+=`<div style="background:hsl(${20+i*9},25%,${20+i%3*6}%);border-radius:6px"></div>`;$('dg').innerHTML=g;
 const D=['Пн','Вт','Ср','Чт','Пт','Сб','Вс'];$('wk').innerHTML=D.map((d,i)=>`<div style="display:flex;align-items:center;gap:16px;padding:10px 0;border-bottom:1px solid #2c2c2e"><span style="width:60px;font-size:22px;font-weight:800;color:#8e8e93">${d}</span><span id="wd${i}" style="flex:1;background:#2c2c2e;border-radius:12px;padding:10px 14px;font-size:22px;font-weight:700">${d=='Сб'?'Суббота':'—'}</span></div>`).join('');})();'''
RENDER='''
 {const T=[[.3,1.5],[.9,2.0],[1.5,2.7]];for(let i=0;i<3;i++){const [a,b]=T[i];const p=eb(seg(t,a,a+.25));$('iv'+i).style.opacity=seg(t,a,a+.1);$('iv'+i).style.transform=`translateY(${(1-p)*-40}px)`;const n=t>=b;$('nd'+i).style.background=n?'#ff453a':'#3a3a3c';$('nd'+i).style.color=n?'#fff':'#ff453a';}}
 {const h=seg(t,3.3,5.1);$('hs').textContent=Math.round(h*16)+' ч';$('hsb').style.width=(h*100)+'%';$('zp2').textContent=t>=5.1?'зарплата · ✕ не поступила':'зарплата · ожидается…';$('zp2').style.color=t>=5.1?'#ff453a':'#8e8e93';$('nz').style.opacity=seg(t,5.1,5.2);if(si==1)shake('c2',t,5.1,8);}
 {const u=t>=6.4;$('lk3').style.opacity=1-seg(t,6.4,6.7);$('dg').style.filter=`blur(${lerp(14,4,seg(t,6.4,6.8))}px)`;$('cn3').textContent=(t<7.0?Math.round(seg(t,6.4,7.0)*120):Math.round(lerp(120,999,seg(t,7.0,7.3))))+' объектов';}
 {const s=t<9.0?Math.round(seg(t,7.7,9.0)*47):47;$('sv').textContent=s;$('sv').style.textDecoration=t>=9.0?'line-through':'none';$('sv').style.color=t>=9.0?'#8e8e93':'#fff';$('svs').style.opacity=seg(t,9.0,9.15);
  $('ans').style.transform=`scale(${1+.08*pop(t,8.1,6)+.06*pop(t,8.7,6)})`;$('ans').style.background=t>=8.7?'#30d158':'#0a84ff';}
 {const p=eo(seg(t,10.6,12.3));$('rt5').setAttribute('stroke-dashoffset',1000*(1-p));const L=document.getElementById('rt5');const len=L.getTotalLength();const pt=L.getPointAtLength(len*p);$('car5').style.left=pt.x+'px';$('car5').style.top=pt.y+'px';
  $('et5').textContent=t>=12.3?'прибытие · в лес':(t>=11.0?'1 ч 12 мин · через трассу':'маршрут строится…');}
 {$('cl6').style.transform=`rotate(${t*60}deg) scale(${1+.05*Math.sin(t*12)})`;$('cp').style.opacity=seg(t,14.1,14.25);$('cpt').textContent=t>=14.6?'подключено: Benz ✓':'подключение к «Benz»…';$('cpt').style.color=t>=14.6?'#30d158':'#8e8e93';}
 {$('dec').style.transform=`scale(${1+.15*Math.sin(t*10)})`;$('nk').style.opacity=seg(t,16.9,17.0);$('accw').style.opacity=t>=16.4?.3:1;$('wh').textContent=t>=15.9?'кто ты такой?':'…';}
 {tog('tg8',t>=18.3);tog('tg9',t<19.0);$('t8').style.opacity=seg(t,19.3,19.45);}
 {$('sl9').style.opacity=seg(t,20.5,20.65);$('ox').style.opacity=seg(t,20.7,20.85);$('dim9').style.opacity=1-seg(t,21.4,21.9)*.7;$('zz').style.opacity=seg(t,21.4,21.6);$('zz').style.transform=`translateY(${-Math.sin(t*3)*10}px)`;}
 {for(let i=0;i<7;i++){const s=t>=23.45+i*.07;const e=$('wd'+i);e.textContent=s||i==5?'Суббота':'—';e.style.background=s?'#3a0d12':'#2c2c2e';e.style.color=s?'#ff6f61':'#fff';}$('rp').style.opacity=seg(t,24.0,24.1);}
'''
