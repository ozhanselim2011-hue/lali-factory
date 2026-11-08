BG='#060606'
SUBW='800'
LINES=[
 [["boy,",0.45],["убиваю",0.8],["себя",1.2],["в",1.4],["мае",1.6]],
 [["ты",1.8],["куришь",2.2],["дерьмо,",2.5],["но",2.8],["пока",2.9],["мама",3.1],["не",3.4],["узнает",3.6]],
 [["не",4.2],["давай",4.4],["мне…",4.6],["f*ck,",4.85],["не",5.0],["давай",5.2],["мне",5.4],["обещаний",5.6]],
 [["ведь",6.3],["ты",6.35],["их",6.45],["не",6.6],["выполняешь,",6.7],["это",7.4],["я",7.5],["запоминаю",7.7]],
 [["можешь",9.4],["отдавать",9.8],["мне",10.2],["лирами",10.3]],
 [["я",10.8],["люблю",11.0],["это",11.3],["музло,",11.5],["любишь",11.9],["его",12.2],["копировать",12.3]],
 [["просто",13.0],["ты",13.3],["е*лан,",13.5],["и",13.9],["я",14.0],["не",14.1],["стал",14.2],["аргументировать",14.3]],
]
SC=[[-0.3,1.75],[1.75,4.1],[4.1,6.2],[6.2,9.3],[9.3,10.75],[10.75,12.9],[12.9,99]]
GLOW=['#5a0a0a','#2a2a4a','#5a3a0a','#3a2a5a','#5a1a1a','#7a1f4a','#3a3a3a']
PEMO=['🥀','🤫','🤞','🧠','💷','📋','💬']
END=[14.75,15.07]
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr" style="color:#ff453a">Календарь</div><div class="ttl">Май</div>
 <div id="cal" style="position:absolute;left:30px;right:30px;top:160px;display:grid;grid-template-columns:repeat(7,1fr);gap:8px"></div>
 <div id="bt1" style="position:absolute;left:30px;right:30px;bottom:30px;background:#2c2c2e;border-radius:22px;padding:18px 22px;display:flex;justify-content:space-between;align-items:center;font-size:26px;font-weight:800"><span>🔋 Я</span><span id="bp" class="mono">100%</span></div>
</div>
<div class="card" id="c2" style="background:#1c1c1e">
 <div class="hdr" style="color:#30d158">Локатор</div><div class="ttl">Мама</div>
 <div style="position:absolute;top:170px;left:50%;margin-left:-80px;width:160px;height:160px;border-radius:50%;background:linear-gradient(135deg,#ffd6a5,#ff9f0a);display:flex;align-items:center;justify-content:center;font-size:90px">👩‍🦳</div>
 <div style="position:absolute;left:30px;right:30px;top:370px"><div class="row" style="background:#2c2c2e">📍 <span>Делиться с мамой</span><div class="tg" id="tg2"><b></b></div></div></div>
 <div id="mn" class="c" style="bottom:60px;font-size:34px;font-weight:900;opacity:0">мама не узнает 🤫</div>
</div>
<div class="card" id="c3" style="background:#1c1c1e">
 <div class="hdr" style="color:#ff9f0a">Напоминания</div><div class="ttl">Её обещания</div>
 <div id="pl" style="position:absolute;left:30px;right:30px;top:170px"></div>
 <div id="st3" style="position:absolute;left:30px;right:30px;bottom:30px;height:80px;border-radius:24px;background:#3a0d12;display:flex;align-items:center;justify-content:center;font-size:28px;font-weight:900;color:#ff453a;opacity:0">✋ не давай мне обещаний</div>
</div>
<div class="card" id="c4" style="background:#000">
 <div class="hdr">Заметки</div><div class="ttl">Я запоминаю</div>
 <div class="c" style="top:190px"><div style="font-size:22px;color:#8e8e93;font-weight:700">выполнено обещаний</div><div id="ex" class="mono" style="font-size:110px;font-weight:800;color:#ff453a">0/0</div></div>
 <div id="br" style="position:absolute;left:30px;right:30px;top:400px;display:flex;flex-wrap:wrap;gap:8px"></div>
 <div id="sv4" class="c" style="bottom:36px;font-size:24px;font-weight:800;color:#30d158;opacity:0">☁️ сохранено в iCloud навсегда</div>
</div>
<div class="card" id="c5" style="background:#1c1c1e">
 <div class="hdr">Конвертер</div><div class="ttl">Отдавай лирами</div>
 <div class="box" style="position:absolute;left:30px;right:30px;top:200px;padding:28px">
  <div style="display:flex;justify-content:space-between;font-size:32px;font-weight:800"><span>🇷🇺 RUB</span><span class="mono">10 000</span></div>
  <div id="sw" style="text-align:center;font-size:40px;margin:14px 0">⇅</div>
  <div style="display:flex;justify-content:space-between;font-size:32px;font-weight:800"><span>🇹🇷 TRY</span><span id="try" style="color:#ff453a">₺0</span></div></div>
 <div id="ok5" class="c" style="bottom:60px;font-size:30px;font-weight:900;opacity:0">можно лирами ✓</div>
</div>
<div class="card" id="c6" style="background:linear-gradient(180deg,#2a0a1a,#0a0408)">
 <div id="art" style="position:absolute;left:150px;top:50px;width:300px;height:300px;border-radius:24px;background:linear-gradient(135deg,#ff2d55,#5e2cff);display:flex;align-items:center;justify-content:center;font-size:140px;box-shadow:0 20px 50px rgba(255,45,85,.4)">🎧</div>
 <div style="position:absolute;left:50px;right:50px;top:380px;display:flex;justify-content:space-between;align-items:center"><div><div style="font-size:32px;font-weight:900">Моё музло</div><div style="font-size:22px;color:#aeaeb2;font-weight:600">я</div></div><div id="lk6" style="font-size:52px">🤍</div></div>
 <div id="toasts" style="position:absolute;left:0;right:0;top:470px;height:200px"></div>
</div>
<div class="card" id="c7" style="background:#000">
 <div style="padding:30px 40px 20px;display:flex;align-items:center;gap:16px;border-bottom:1px solid #222"><div style="width:62px;height:62px;border-radius:50%;background:#48484a;display:flex;align-items:center;justify-content:center;font-size:34px">🤡</div><div style="font-size:28px;font-weight:800">Он</div></div>
 <div style="padding:26px 34px 0"><div class="bub" style="background:#262628">докажи что я не прав</div></div>
 <div id="ok7" style="position:absolute;right:34px;top:250px;opacity:0"><div class="bub" style="background:#0a84ff;font-weight:700">ок.</div></div>
 <div id="ar7" class="c" style="top:360px;font-size:24px;font-weight:800;color:#8e8e93;opacity:0">аргументов отправлено: 0</div>
 <div style="position:absolute;left:24px;right:24px;bottom:24px;min-height:76px;border-radius:30px;border:2px solid #3a3a3c;padding:18px 24px;font-size:22px;font-weight:500;line-height:1.3"><span id="in7"></span></div>
</div>
'''
BUILD='''(function(){let c='';for(let i=1;i<=31;i++)c+=`<div id="dy${i}" style="aspect-ratio:1;border-radius:10px;background:#2c2c2e;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:700">${i}</div>`;$('cal').innerHTML=c;
 const P=['позвоню вечером','больше не буду','приду в 8','это последний раз'];$('pl').innerHTML=P.map((p,i)=>`<div class="row" id="p3_${i}" style="background:#2c2c2e;opacity:0"><div style="width:36px;height:36px;border-radius:50%;border:3px solid #ff9f0a;flex:none"></div><span>🤞 ${p}</span></div>`).join('');
 let b='';for(let i=0;i<37;i++)b+=`<div id="b4_${i}" style="width:30px;height:30px;border-radius:8px;background:#2c2c2e;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:900;color:#fff;opacity:0">✕</div>`;$('br').innerHTML=b;
 let to='';for(let i=0;i<6;i++)to+=`<div id="to${i}" style="position:absolute;left:50%;top:${i*30}px;transform:translateX(-50%);background:rgba(60,60,64,.95);border-radius:20px;padding:10px 20px;font-size:22px;font-weight:800;white-space:nowrap;opacity:0">📋 Скопировано</div>`;$('toasts').innerHTML=to;})();'''
RENDER='''
 {for(let i=1;i<=31;i++){const on=t>=0.8+i*.025;const e=$('dy'+i);e.style.background=on?'#5a0a0a':'#2c2c2e';e.style.color=on?'#ff8a80':'#fff';}const b=Math.round(lerp(100,1,eo(seg(t,0.8,1.7))));$('bp').textContent=b+'%';$('bp').style.color=b<20?'#ff453a':'#30d158';}
 {tog('tg2',t<3.1);$('mn').style.opacity=seg(t,3.6,3.75);$('mn').style.transform=`scale(${1+.2*pop(t,3.6,6)})`;}
 {for(let i=0;i<4;i++){const ti=4.2+i*.25;$('p3_'+i).style.opacity=seg(t,ti,ti+.1);$('p3_'+i).style.transform=`translateY(${(1-eb(seg(t,ti,ti+.25)))*-30}px)`;}$('st3').style.opacity=seg(t,5.6,5.7);if(si==2)shake('c3',t,4.85,8);}
 {let n=0;for(let i=0;i<37;i++){const ti=6.4+i*.035;const on=t>=ti;if(on)n++;const e=$('b4_'+i);e.style.opacity=on?1:0;e.style.background=on?'#5a0a0a':'#2c2c2e';}$('ex').textContent='0/'+n;$('sv4').style.opacity=seg(t,7.7,7.85);$('ex').style.transform=`scale(${1+.15*pop(t,7.7,5)})`;}
 {const v=t<10.3?0:lerp(0,3700,eo(seg(t,10.3,10.6)));$('try').textContent='₺'+fmt(v);$('sw').style.transform=`rotate(${seg(t,9.8,10.2)*180}deg)`;$('ok5').style.opacity=seg(t,10.35,10.5);}
 {const l=t>=11.0;$('lk6').textContent=l?'❤️':'🤍';$('lk6').style.transform=`scale(${1+.5*pop(t,11.0,5)})`;$('art').style.transform=`scale(${1+.03*Math.sin(t*8)})`;
  for(let i=0;i<6;i++){const ti=12.3+i*.08;const ph=seg(t,ti,ti+.5);$('to'+i).style.opacity=ph>0&&ph<1?1:0;$('to'+i).textContent=i<5?'📋 Скопировано':'📋 Скопировано ×99';}}
 {const a='во-первых, ты сам начал, во-вторых, это моё музло, в-третьих…';const n=t<13.0?0:(t<14.0?Math.floor((t-13.0)*60):Math.max(0,Math.floor(a.length-(t-14.0)*200)));$('in7').textContent=a.slice(0,Math.min(a.length,n));
  $('ok7').style.opacity=seg(t,14.3,14.4);$('ar7').style.opacity=seg(t,14.35,14.5);}
'''
