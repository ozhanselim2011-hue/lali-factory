BG='#050505'
SUBW='600'
LINES=[
 [["я",0.15],["не",.5],["хочу",.75],["больше",1.25],["думать",1.75],["о",2.15],["прошлом",2.25]],
 [["падаю",4.25],["так",5.0],["многоэтажно",5.75]],
 [["кажется,",7.5],["у",8.6],["меня",8.75],["не",9.1],["будет",9.3],["завтра",10.0]],
 [["ты",12.75],["не",13.0],["про",13.25],["всех,",13.75],["как",14.0],["и",14.25],["я",14.5],["тоже",14.75]],
]
SC=[[-0.3,3.95],[3.95,7.25],[7.25,12.5],[12.5,99]]
GLOW=['#2a2a2a','#2a2a3a','#1a2a3a','#2a2a2a']
PEMO=['🖤','⬇️','🌫️','🤍']
END=[16.6,18.1]
CSS='#stage{filter:grayscale(.85)}'
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr" style="color:#0a84ff">‹ Настройки · Фото</div><div class="ttl">Воспоминания</div>
 <div id="mem" style="position:absolute;left:30px;right:30px;top:170px;height:260px;border-radius:26px;background:linear-gradient(135deg,#5a4a3a,#2a3a4a);overflow:hidden;display:flex;align-items:flex-end;padding:22px">
  <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:130px">🌅</div>
  <div style="position:relative;font-size:30px;font-weight:900">Прошлое · 2023</div></div>
 <div style="position:absolute;left:30px;right:30px;top:460px">
  <div class="row" style="background:#2c2c2e">🕰 <span>Показывать прошлое</span><div class="tg" id="tg1"><b></b></div></div>
  <div class="row" style="background:#2c2c2e">💭 <span>Думать о нём</span><div class="tg" id="tg2"><b></b></div></div></div>
</div>
<div class="card" id="c2" style="background:#000">
 <div class="hdr">Здоровье · Состояние</div><div class="ttl">Настроение</div>
 <svg width="600" height="380" style="position:absolute;top:150px;left:0"><g id="flr" stroke="#2c2c2e" stroke-width="2"></g><path id="stair" fill="none" stroke="#e5e5ea" stroke-width="7" stroke-linejoin="round"/><circle id="dot2" r="12" fill="#fff"/></svg>
 <div class="c" style="bottom:40px"><div id="fl2" class="mono" style="font-size:52px;font-weight:800">25 эт.</div><div id="fl2b" style="font-size:22px;color:#8e8e93;font-weight:600">падаю</div></div>
</div>
<div class="card" id="c3" style="background:linear-gradient(180deg,#3a3f48,#1a1d22)">
 <div style="text-align:center;padding-top:30px"><div style="font-size:30px;font-weight:600">Мой город</div><div style="font-size:120px;font-weight:200;line-height:1">4°</div><div style="font-size:26px;font-weight:600;opacity:.8">Туман</div></div>
 <div style="position:absolute;left:24px;right:24px;top:260px;background:rgba(0,0,0,.2);border-radius:26px;padding:10px 24px">
  <div style="font-size:19px;font-weight:700;opacity:.6;padding:10px 0;border-bottom:1px solid rgba(255,255,255,.12)">🗓 ПРОГНОЗ НА 10 ДНЕЙ</div>
  <div id="fc"></div></div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div class="hdr" style="color:#0a84ff">‹ Основные</div><div class="ttl">AirDrop</div>
 <div style="padding:30px 30px 0"><div style="font-size:20px;color:#8e8e93;font-weight:700;margin:0 6px 10px">ПРИНИМАТЬ ОТ</div>
  <div style="background:#2c2c2e;border-radius:24px;padding:0 24px" id="opts"></div></div>
 <div id="t4" class="c" style="bottom:70px;font-size:30px;font-weight:700;opacity:0">ты не про всех.</div>
 <div id="t4b" class="c" style="bottom:30px;font-size:24px;font-weight:600;color:#8e8e93;opacity:0">как и я тоже 🤍</div>
</div>
'''
BUILD='''(function(){let f='';for(let i=0;i<=5;i++)f+=`<line x1="40" x2="560" y1="${40+i*60}" y2="${40+i*60}"/>`;$('flr').innerHTML=f;
 const D=[['Сегодня','☁️','4° / 1°'],['Завтра','—','нет данных'],['Чт','',''],['Пт','',''],['Сб','',''],['Вс','','']];
 $('fc').innerHTML=D.map(([d,e,v],i)=>`<div id="fc${i}" style="display:flex;justify-content:space-between;align-items:center;padding:14px 0;border-bottom:1px solid rgba(255,255,255,.08);font-size:26px;font-weight:700;opacity:0"><span style="width:140px">${d}</span><span>${e}</span><span id="fv${i}" style="width:170px;text-align:right">${v}</span></div>`).join('');
 const O=['Никого','Только контакты','Все (10 мин)','Только ты'];
 $('opts').innerHTML=O.map((o,i)=>`<div style="display:flex;justify-content:space-between;padding:22px 0;${i<3?'border-bottom:1px solid #3a3a3c;':''}font-size:28px;font-weight:600" id="o${i}"><span>${o}</span><span id="ck${i}" style="color:#0a84ff;font-weight:900"></span></div>`).join('');})();'''
RENDER='''
 {tog('tg1',t<1.75);tog('tg2',t<2.25);$('mem').style.filter=`grayscale(${seg(t,1.25,2.4)}) blur(${seg(t,2.25,2.9)*14}px)`;$('mem').style.opacity=1-seg(t,2.5,3.4)*.8;}
 {const p=seg(t,4.25,6.4);const steps=5;let d='M40 40';let cx=40,cy=40;for(let k=0;k<steps;k++){const sp=cl(p*steps-k);if(sp<=0)break;const nx=40+(k+1)*104;const hx=lerp(cx,nx,cl(sp*2));d+=` L${hx} ${cy}`;cx=hx;if(sp>.5){const ny=lerp(cy,cy+60,cl((sp-.5)*2));d+=` L${cx} ${ny}`;cy=ny}}
  $('stair').setAttribute('d',d);$('dot2').setAttribute('cx',cx);$('dot2').setAttribute('cy',cy);const fl=Math.round(lerp(25,1,eo(p)));$('fl2').textContent=fl+' эт.';$('fl2b').textContent=t>=5.75?'многоэтажно':'падаю';if(si==1)shake('c2',t,5.75,6);}
 {for(let i=0;i<6;i++){const ti=7.5+i*.25;const e=$('fc'+i);let o=seg(t,ti,ti+.15);if(i>=2)o*=(1-seg(t,10.0,10.6))*.5;e.style.opacity=o;}
  const z=t>=10.0;$('fv1').style.color=z?'#ff453a':'#fff';$('fc1').style.transform=`scale(${1+.08*pop(t,10.0,5)})`;$('fc1').style.filter=z?`blur(${seg(t,10.6,12.0)*3}px)`:'none';}
 {const sel=t<13.75?2:3;for(let i=0;i<4;i++){$('ck'+i).textContent=i==sel?'✓':'';}$('o2').style.opacity=t>=13.75?.35:1;$('t4').style.opacity=seg(t,13.75,13.95);$('t4b').style.opacity=seg(t,14.75,14.95);}
'''
