BG='#070203'
SUBW='900'
SUBX='text-transform:uppercase'
RED='у*бок'
LINES=[
 [["ну",0.0],["я",.4],["думаю,",.6],["это",.9],["как-то",1.1],["так,",1.4],["пацаны",1.8]],
 [["она",2.0],["знает,",2.3],["я",2.8],["у*бок",3.0],["(но)",3.5]],
 [["но",3.9],["листает",4.1],["моё",4.6],["фото",5.0],["на",5.3],["своём",5.6],["iPhone",6.0],["(да)",6.6]],
 [["мы",6.8],["разные",7.1],["люди,",7.6],["я",8.1],["просто",8.4],["хочу",8.7],["свободу",9.0]],
 [["ничего",9.9],["не",10.4],["помню,",10.6],["опять",11.3],["под",11.7],["алкоголем",12.0]],
 [["я",12.75],["не",13.0],["знаю",13.1],["твоё",13.5],["имя",13.9]],
 [["и",14.5],["я",14.6],["точно",14.75],["не",15.0],["запомню",15.2]],
]
SC=[[-0.3,1.95],[1.95,3.85],[3.85,6.75],[6.75,9.85],[9.85,12.65],[12.65,14.4],[14.4,99]]
GLOW=['#3a0a0a','#7a0a0a','#5a0a1a','#0a4a2a','#4a1a3a','#5a0a0a','#7a0a0a']
PEMO=['🎙️','🤡','📸','🕊️','🌀','❓','✕']
END=[15.35,15.7]
CSS='''.ph{width:150px;height:150px;border-radius:8px;flex:none;display:flex;align-items:center;justify-content:center;font-size:70px}'''
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr" style="color:#ff453a">Диктофон</div><div class="ttl">Новая запись</div>
 <div id="wf1" style="position:absolute;left:30px;right:30px;top:200px;height:200px;display:flex;align-items:center;gap:4px"></div>
 <div id="tm1" class="c mono" style="top:430px;font-size:56px;font-weight:300">00:00,00</div>
 <div style="position:absolute;left:50%;bottom:50px;margin-left:-50px;width:100px;height:100px;border-radius:50%;border:6px solid #fff;display:flex;align-items:center;justify-content:center"><div style="width:44px;height:44px;border-radius:10px;background:#ff3b30"></div></div>
</div>
<div class="card" id="c2" style="background:#1c1c1e">
 <div class="hdr" style="color:#0a84ff">‹ Контакты · её телефон</div>
 <div style="position:absolute;top:110px;left:50%;margin-left:-90px;width:180px;height:180px;border-radius:50%;background:#48484a;display:flex;align-items:center;justify-content:center;font-size:96px" id="av2">😎</div>
 <div class="box" style="position:absolute;left:30px;right:30px;top:330px"><div style="font-size:20px;color:#8e8e93;font-weight:700">имя</div><div style="font-size:40px;font-weight:900;margin-top:6px"><span id="nm2">Любимый ❤️</span><span id="cu2" style="display:inline-block;width:3px;height:40px;background:#0a84ff;vertical-align:middle;margin-left:3px"></span></div></div>
 <div id="sv2" class="c" style="bottom:60px;font-size:26px;font-weight:800;color:#ff453a;opacity:0">она знает ✓ сохранено</div>
</div>
<div class="card" id="c3" style="background:#000">
 <div style="padding:30px 30px 10px;display:flex;justify-content:space-between;align-items:baseline"><div style="font-size:40px;font-weight:800">Фото</div><div id="cnt3" class="mono" style="font-size:22px;color:#ff453a;font-weight:700">просмотрено: 0</div></div>
 <div style="position:absolute;left:0;right:0;top:100px;bottom:110px;overflow:hidden"><div id="grid3" style="position:absolute;left:0;right:0;top:0;display:flex;flex-wrap:wrap;gap:4px;padding:0 4px"></div></div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:110px;background:rgba(20,20,22,.95);display:flex;align-items:center;justify-content:center;gap:16px;font-size:24px;font-weight:700"><span>📱</span><span id="ip3">на своём iPhone</span></div>
 <div id="fg3" style="position:absolute;width:70px;height:70px;border-radius:50%;background:rgba(255,255,255,.3);border:3px solid rgba(255,255,255,.8);left:265px;top:420px"></div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div class="hdr" style="color:#0a84ff">‹ Настройки</div><div class="ttl">Жизнь</div>
 <div style="padding:30px 30px 0">
  <div class="row" style="background:#2c2c2e">🫂 <span>Мы — одинаковые</span><div class="tg" id="tg1"><b></b></div></div>
  <div class="row" style="background:#2c2c2e">💍 <span>Отношения</span><div class="tg" id="tg2"><b></b></div></div>
  <div class="row" id="fr4" style="background:#2c2c2e">🕊️ <span>Свобода</span><div class="tg" id="tg3"><b></b></div></div>
 </div>
 <div id="bird" style="position:absolute;font-size:90px;left:250px;top:520px;opacity:0">🕊️</div>
 <div id="rz4" class="c" style="bottom:40px;font-size:26px;font-weight:800;color:#8e8e93;opacity:0">мы разные люди</div>
</div>
<div class="card" id="c5" style="background:#000">
 <div class="hdr">Фото › Вчера</div><div class="ttl">23:00 – 05:00</div>
 <div id="g5" style="position:absolute;left:30px;right:30px;top:180px;display:grid;grid-template-columns:repeat(3,1fr);gap:8px"></div>
 <div class="c" style="bottom:50px"><div id="t5a" style="font-size:34px;font-weight:900">загрузка…</div><div id="t5b" style="font-size:22px;color:#8e8e93;font-weight:600;margin-top:6px"></div></div>
</div>
<div class="card" id="c6" style="background:#1c1c1e">
 <div style="position:absolute;top:70px;left:50%;margin-left:-90px;width:180px;height:180px;border-radius:50%;background:#636366;display:flex;align-items:center;justify-content:center;font-size:96px;font-weight:800;color:#fff">?</div>
 <div class="c mono" style="top:280px;font-size:26px;color:#8e8e93;font-weight:600">+7 9•• ••• •• ••</div>
 <div class="box" style="position:absolute;left:30px;right:30px;top:340px"><div style="font-size:20px;color:#8e8e93;font-weight:700">имя</div><div id="nm6" style="font-size:40px;font-weight:900;margin-top:6px;color:#636366">Без имени</div></div>
 <div id="sr6" class="c" style="bottom:50px;font-size:26px;font-weight:700;color:#ff9f0a;opacity:0">Siri: «я не знаю её имени»</div>
</div>
<div class="card" id="c7" style="background:#1c1c1e">
 <div class="hdr" style="color:#ff9f0a">Напоминания</div><div class="ttl">Сегодня</div>
 <div style="padding:26px 30px 0"><div class="row" id="r7" style="background:#2c2c2e"><div id="cb7" style="width:40px;height:40px;border-radius:50%;border:3px solid #636366;flex:none"></div><span id="rt7" style="position:relative">Запомнить её имя<span id="sk7" style="position:absolute;left:-4px;top:50%;height:4px;background:#ff453a;width:0"></span></span></div></div>
 <div id="nt7" style="position:absolute;left:30px;right:30px;top:300px;background:#3a0d12;border-radius:26px;padding:24px;opacity:0"><div style="font-size:30px;font-weight:900;color:#ff453a">✕ Не запомнено</div><div style="font-size:22px;color:#ffb3ad;font-weight:600;margin-top:6px">Напоминание удалено. Точно.</div></div>
</div>
'''
BUILD='''(function(){let w='';for(let i=0;i<60;i++)w+=`<div id="w1_${i}" style="flex:1;border-radius:3px;background:#ff453a;height:4px"></div>`;$('wf1').innerHTML=w;
 const E=['🤳','🕶️','🎧','🏎️','🌃','🤳','🍾','🎤','🖤','🤳','📸','🌆','🤳','🔥','🕶️','🤳','🌃','🎤','🤳','🏎️','🖤'];
 $('grid3').innerHTML=E.map((e,i)=>`<div class="ph" style="width:194px;height:194px;background:hsl(${(i*37)%360},25%,${18+i%3*6}%)">${e}</div>`).join('');
 let g='';for(let i=0;i<9;i++)g+=`<div id="q5_${i}" style="aspect-ratio:1;border-radius:10px;background:hsl(${280+i*10},30%,${15+i%3*5}%);display:flex;align-items:center;justify-content:center;font-size:56px;filter:blur(8px)">${['🌀','🥴','🌃','🎶','🌀','📸','🥴','🌃','🌀'][i]}</div>`;$('g5').innerHTML=g;})();'''
RENDER='''
 for(let i=0;i<60;i++){const on=i/60<seg(t,0,1.95);$('w1_'+i).style.height=on?(6+Math.abs(Math.sin(i*1.3+t*2)*Math.cos(i*.7))*170)+'px':'4px';}
 {const ms=Math.max(0,t)*100;$('tm1').textContent='00:0'+Math.floor(Math.max(0,t))+','+String(Math.floor(ms%100)).padStart(2,'0');}
 {const a='Любимый ❤️',b='У*бок 🤡';let s;if(t<2.6)s=a;else if(t<3.0){s=a.slice(0,Math.max(0,Math.floor((3.0-t)/.4*a.length)))}else{s=b.slice(0,Math.min(b.length,Math.floor((t-3.0)*30)))}
  $('nm2').textContent=s;$('nm2').style.color=t>=3.0?'#ff453a':'#fff';$('cu2').style.opacity=Math.floor(t*4)%2?1:.2;$('sv2').style.opacity=seg(t,3.5,3.65);$('av2').textContent=t>=3.0?'🤡':'😎';$('av2').style.transform=`scale(${1+.3*pop(t,3.0,6)})`;}
 {const sc=eo(seg(t,4.1,6.2))*700;$('grid3').style.top=(-sc)+'px';$('cnt3').textContent='просмотрено: '+Math.round(seg(t,4.1,6.6)*37);
  $('fg3').style.top=(420-((t*3)%1)*200)+'px';$('fg3').style.opacity=t>=4.1?1:0;$('ip3').style.color=t>=6.0?'#ff453a':'#fff';$('ip3').textContent=t>=6.0?'на своём iPhone · 2 ч 14 мин':'на своём iPhone';}
 {tog('tg1',t<7.1);tog('tg2',t<8.4);tog('tg3',t>=9.0);$('fr4').style.background=t>=9.0?'#0f3a1f':'#2c2c2e';$('rz4').style.opacity=seg(t,7.1,7.3);
  const b=seg(t,9.0,9.8);$('bird').style.opacity=b>0&&b<1?1:0;$('bird').style.transform=`translate(${b*200}px,${-b*400}px) rotate(${-b*20}deg)`;}
 {const n=t>=10.6;for(let i=0;i<9;i++){$('q5_'+i).style.opacity=t>=11.3?.25:1;$('q5_'+i).style.transform=`rotate(${Math.sin(t*3+i)*(t>=11.7?6:0)}deg)`}
  $('t5a').textContent=n?'Ничего не помню':'загрузка…';$('t5a').style.color=n?'#ff453a':'#fff';$('t5b').textContent=t>=11.3?'опять. 214 фото, 0 воспоминаний':'';if(si==4)shake('c5',t,12.0,8);}
 {const k=t>=13.1;$('nm6').textContent=k?'???':'Без имени';$('nm6').style.color=k?'#ff9f0a':'#636366';$('nm6').style.transform=`scale(${1+.25*pop(t,13.9,6)})`;$('sr6').style.opacity=seg(t,13.9,14.05);}
 {$('sk7').style.width=(eo(seg(t,15.0,15.2))*105)+'%';$('nt7').style.opacity=seg(t,15.2,15.3);$('nt7').style.transform=`scale(${1+.1*pop(t,15.2)})`;$('cb7').style.borderColor=t>=14.75?'#ff453a':'#636366';if(si==6)shake('c7',t,15.2,10);}
'''
