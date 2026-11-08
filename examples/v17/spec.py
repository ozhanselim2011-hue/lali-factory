BG='linear-gradient(180deg,#070a18,#030409)'
SUBW='800'
LINES=[
 [["она",0.0],["писала",0.3],["мне",0.9],["о",1.2],["том,",1.4],["что",1.8],["хочет",1.9]],
 [["я",2.2],["выжидал",2.7],["паузу",3.5],["и",4.2],["отвечал",4.4],["ей:",5.1],["«клёво»,",5.3],["как",5.6],["будто",5.7],["мне",5.9],["по*уй",6.1]],
 [["она",6.5],["бесилась,",7.0],["будто",7.8],["бы",8.0],["злилась",8.2]],
 [["так",8.6],["что,",8.9],["леди,",9.1],["извините,",9.5],["но",10.3],["не",10.5],["бесите",10.6],["вопросами,",11.0],["типа:",11.7]],
 [["«тебе",14.3],["нравится",14.9],["это?»",15.4]],
 [["«ты",16.1],["накурен",16.4],["сейчас?»",17.0]],
 [["«ты",17.8],["когда-нибудь",18.1],["злишься?»",18.8]],
 [["«ты",19.5],["встречаешься",19.7],["с",20.6],["ней?»",20.7]],
 [["«ты",20.9],["с",21.4],["ней",21.5],["спал,",21.7],["это",22.1],["так?»",22.3]],
 [["«ты",22.8],["барыжил?",23.2],["никто",23.9],["из",24.5],["твоих",24.7],["вас",25.2],["не",25.5],["сдал?»",25.7]],
 [["и",26.0],["я:",26.15],["«бл*ть,",26.4],["да!",27.2],["бл*ть,",27.6],["да!",28.4],["бл*ть,",28.8],["да!»",29.2]],
 [["с*ка,",29.5],["только",30.1],["так,",30.4],["только",30.9],["так,",31.6],["вот",32.2],["так",32.5]],
 [["бл*ть,",32.9],["да!",33.9],["бл*ть,",34.3],["да!",35.1],["бл*ть,",35.5],["да!",35.9]],
]
SC=[[-0.3,2.15],[2.15,6.45],[6.45,8.55],[8.55,14.2],[14.2,26.0],[26.0,29.4],[29.4,32.85],[32.85,99]]
GLOW=['#1d2a6a','#1d3a5a','#6a0a1a','#3a1d6a','#2a2a5a','#0a5a2a','#5a3a0a','#0a6a2a']
PEMO=['💬','⏳','😡','🙅','❓','✅','🔁','🔥']
END=[36.3,36.69]
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#141a2e,#05060c)">
 <div class="c" style="top:60px;font-size:130px;font-weight:700;letter-spacing:-4px">02:14</div>
 <div id="nt1" style="position:absolute;left:24px;right:24px;top:240px"></div>
</div>
<div class="card" id="c2" style="background:#000">
 <div style="padding:30px 40px 20px;display:flex;align-items:center;gap:16px;border-bottom:1px solid #222"><div style="width:62px;height:62px;border-radius:50%;background:linear-gradient(135deg,#ff9ac1,#ff2d78);display:flex;align-items:center;justify-content:center;font-size:34px">👸</div><div style="font-size:28px;font-weight:800">Она</div></div>
 <div style="padding:24px 34px 0"><div class="bub" style="background:#262628">хочу тебя увидеть 🥺</div><div id="rd2" style="font-size:18px;color:#8e8e93;font-weight:600;margin:6px 6px 0">Прочитано 02:14</div></div>
 <div id="tm2" class="c" style="top:280px"><div style="font-size:22px;color:#8e8e93;font-weight:700">выжидаю паузу</div><div id="tmv" class="mono" style="font-size:72px;font-weight:800">00:00</div></div>
 <div id="kl" style="position:absolute;right:34px;top:440px;opacity:0;text-align:right"><div class="bub" style="background:#0a84ff;font-weight:700">клёво 👍</div><div style="font-size:18px;color:#8e8e93;font-weight:600;margin-top:6px">Доставлено</div></div>
 <div id="pz" class="c" style="bottom:40px;font-size:26px;font-weight:900;color:#8e8e93;opacity:0">режим: как будто мне по*уй 😐</div>
</div>
<div class="card" id="c3" style="background:#000">
 <div style="padding:30px 40px 20px;display:flex;align-items:center;gap:16px;border-bottom:1px solid #222"><div style="width:62px;height:62px;border-radius:50%;background:linear-gradient(135deg,#ff453a,#ff2d78);display:flex;align-items:center;justify-content:center;font-size:34px">😡</div><div style="font-size:28px;font-weight:800">Она</div></div>
 <div id="ang" style="position:absolute;left:34px;right:34px;top:130px"></div>
 <div id="mt3" class="c" style="bottom:40px"><div style="font-size:22px;color:#8e8e93;font-weight:700">уровень злости</div><div id="mtb" style="height:18px;border-radius:9px;background:#3a3a3c;margin:10px 60px 0;overflow:hidden"><div id="mtv" style="height:18px;background:linear-gradient(90deg,#ff9f0a,#ff453a);width:0"></div></div></div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div class="hdr">Пункт управления</div><div class="ttl">Фокусирование</div>
 <div style="padding:30px 30px 0"><div id="fq" style="display:flex;align-items:center;gap:20px;background:#2c2c2e;border-radius:26px;padding:24px;font-size:30px;font-weight:800"><div id="fqi" style="width:64px;height:64px;border-radius:50%;background:#3a3a3c;display:flex;align-items:center;justify-content:center;font-size:34px">🙅‍♂️</div><div>Без вопросов<div id="fqs" style="font-size:20px;color:#8e8e93;font-weight:600">Выкл.</div></div></div></div>
 <div id="fl4" style="position:absolute;left:30px;right:30px;top:330px;background:#2c2c2e;border-radius:24px;padding:22px;font-size:24px;font-weight:700;opacity:0">🔕 Скрывать сообщения с «?»<div style="font-size:20px;color:#8e8e93;font-weight:600;margin-top:6px">леди, извините 🎩</div></div>
 <div id="ty" class="c" style="bottom:50px;font-size:40px;font-weight:900;color:#bf5af2;opacity:0">типа:</div>
</div>
<div class="card" id="c5" style="background:#000">
 <div style="padding:26px 40px 16px;display:flex;align-items:center;gap:16px;border-bottom:1px solid #222"><div style="width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#ff9ac1,#ff2d78);display:flex;align-items:center;justify-content:center;font-size:30px">👸</div><div style="font-size:26px;font-weight:800">Она</div><div id="qc" class="mono" style="margin-left:auto;font-size:20px;color:#ff453a;font-weight:700">❓ 0</div></div>
 <div style="position:absolute;left:0;right:0;top:100px;bottom:0;overflow:hidden"><div id="qs" style="position:absolute;left:30px;right:30px;bottom:20px"></div></div>
</div>
<div class="card" id="c6" style="background:#000">
 <div style="padding:26px 40px 16px;display:flex;align-items:center;gap:16px;border-bottom:1px solid #222"><div style="font-size:26px;font-weight:800">Ответ на всё</div></div>
 <div id="ys" style="position:absolute;left:30px;right:30px;top:110px"></div>
 <div id="al6" class="c" style="bottom:40px;font-size:28px;font-weight:900;color:#30d158;opacity:0">✓✓ отвечено на все вопросы</div>
</div>
<div class="card" id="c7" style="background:#1c1c1e">
 <div class="hdr" style="color:#ff9f0a">Команды › Автоматизация</div><div class="ttl">Автоответ</div>
 <div style="margin:30px 30px 0;background:#2c2c2e;border-radius:26px;padding:24px">
  <div style="font-size:22px;color:#8e8e93;font-weight:700">Когда приходит вопрос от «Она»</div>
  <div style="font-size:34px;font-weight:900;margin-top:10px">↩︎ Ответить: «да!»</div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-top:18px;font-size:24px;font-weight:700"><span>Только так</span><div class="tg" id="tg7"><b></b></div></div></div>
 <div id="lp" class="c" style="top:420px;font-size:120px">🔁</div>
 <div id="vt" class="c" style="bottom:40px;font-size:34px;font-weight:900;color:#ff9f0a;opacity:0">вот так.</div>
</div>
<div class="card" id="c8" style="background:#000">
 <div id="das" style="position:absolute;inset:0"></div>
 <div id="fin8" class="c" style="bottom:50px;font-size:30px;font-weight:900;color:#30d158;opacity:0">прочитано · да · да · да</div>
</div>
'''
BUILD='''(function(){
 $('nt1').innerHTML=['хочу к тебе','хочу чтоб ты приехал','хочу поговорить 🥺'].map((n,i)=>`<div id="n1_${i}" style="display:flex;gap:14px;align-items:center;background:rgba(60,60,64,.8);border-radius:24px;padding:16px 18px;margin-bottom:10px;opacity:0"><div style="width:52px;height:52px;border-radius:14px;background:#30d158;display:flex;align-items:center;justify-content:center;font-size:28px">💬</div><div><div style="font-size:22px;font-weight:800">Она</div><div style="font-size:22px;font-weight:600;color:#d1d1d6">${n}</div></div></div>`).join('');
 $('ang').innerHTML=['???','алло','ты серьёзно?','«клёво» и всё?? 😡'].map((a,i)=>`<div id="a3_${i}" style="margin-bottom:12px;opacity:0"><div class="bub" style="background:#262628;font-weight:700">${a}</div></div>`).join('');
 const Q=['тебе нравится это?','ты накурен сейчас?','ты когда-нибудь злишься?','ты встречаешься с ней?','ты с ней спал, это так?','ты барыжил? никто из твоих вас не сдал?'];
 $('qs').innerHTML=Q.map((q,i)=>`<div id="q5_${i}" style="margin-top:12px;display:none"><div class="bub" style="background:#262628;font-size:26px">${q}</div></div>`).join('');
 $('ys').innerHTML=[0,1,2].map(i=>`<div id="y6_${i}" style="text-align:right;margin-bottom:16px;opacity:0"><div class="bub" style="background:#0a84ff;font-size:54px;font-weight:900;padding:16px 34px">да!</div></div>`).join('');
 let d='';for(let i=0;i<3;i++)d+=`<div id="d8_${i}" style="position:absolute;left:${[60,250,150][i]}px;top:${[90,230,380][i]}px;transform:rotate(${[-12,8,-5][i]}deg);border:10px solid #30d158;color:#30d158;border-radius:24px;padding:4px 40px;font-size:110px;font-weight:900;opacity:0">ДА!</div>`;$('das').innerHTML=d;})();'''
RENDER='''
 {[0.3,0.9,1.9].forEach((s,i)=>{const p=eb(seg(t,s,s+.25));$('n1_'+i).style.opacity=seg(t,s,s+.1);$('n1_'+i).style.transform=`translateY(${(1-p)*-50}px)`;});}
 {const w=t<2.7?0:(t<4.4?seg(t,2.7,4.4)*299:299);const m=Math.floor(w/60),s=Math.floor(w%60);$('tmv').textContent='0'+m+':'+String(s).padStart(2,'0');$('tm2').style.opacity=1-seg(t,4.4,4.7)*.6;
  $('kl').style.opacity=seg(t,5.3,5.4);$('kl').style.transform=`translateY(${(1-eo(seg(t,5.3,5.5)))*40}px)`;$('pz').style.opacity=seg(t,6.1,6.25);}
 {[6.6,7.0,7.5,8.0].forEach((s,i)=>{$('a3_'+i).style.opacity=seg(t,s,s+.1);$('a3_'+i).style.transform=`scale(${eb(seg(t,s,s+.2))})`;});$('mtv').style.width=(eo(seg(t,6.6,8.3))*100)+'%';if(si==2)shake('c3',t,8.2,10);}
 {const on=t>=9.5;$('fq').style.background=on?'#5e2cff':'#2c2c2e';$('fqi').style.background=on?'#fff':'#3a3a3c';$('fqs').textContent=on?'Вкл.':'Выкл.';$('fqs').style.color=on?'#fff':'#8e8e93';$('fq').style.transform=`scale(${1+.06*pop(t,9.5,6)})`;
  $('fl4').style.opacity=seg(t,10.6,10.8);$('ty').style.opacity=seg(t,11.7,11.85);$('ty').style.transform=`scale(${1+.1*Math.sin(t*4)})`;}
 {const T=[14.3,16.1,17.8,19.5,20.9,22.8];let n=0;T.forEach((s,i)=>{const e=$('q5_'+i);const v=t>=s;if(v)n++;e.style.display=v?'block':'none';e.style.transform=`scale(${v?lerp(.6,1,eb(seg(t,s,s+.2))):1})`;e.style.transformOrigin='left';});
  $('qc').textContent='❓ '+n+(t>=23.9?' · ещё 47':'');if(si==4)shake('c5',t,22.8,6);}
 {[27.2,28.4,29.2].forEach((s,i)=>{$('y6_'+i).style.opacity=seg(t,s,s+.08);$('y6_'+i).style.transform=`scale(${lerp(1.6,1,eb(seg(t,s,s+.2)))})`;$('y6_'+i).style.transformOrigin='right';});$('al6').style.opacity=seg(t,29.2,29.35);if(si==5){shake('c6',t,27.2,8);shake('c6',t,28.4,8);}}
 {tog('tg7',t>=30.4);$('lp').style.transform=`rotate(${t*360}deg) scale(${1+.2*pop(t,31.6,5)})`;$('vt').style.opacity=seg(t,32.2,32.35);}
 {[33.9,35.1,35.9].forEach((s,i)=>{const e=$('d8_'+i);e.style.opacity=seg(t,s,s+.05);e.style.transform=`rotate(${[-12,8,-5][i]}deg) scale(${lerp(2.2,1,eo(seg(t,s,s+.15)))})`;});$('fin8').style.opacity=seg(t,35.9,36.05);if(si==7){shake('c8',t,33.9,12);shake('c8',t,35.1,12);shake('c8',t,35.9,12);}}
'''
