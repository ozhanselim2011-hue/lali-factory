BG='#0b0b0d'
SUBW='800'
LINES=[
 [["я",3.75],["когда-то",4.0],["чуть",4.25],["не",4.5],["сдох",4.75],["и",5.0],["больше",5.25],["не",6.0],["кидаю",6.25],["круг",6.6]],
 [["ты",7.0],["услышишь",7.25],["двери",7.75],["стук,",8.25],["потом",8.5],["мы",9.0],["забираем",9.25],["лут",9.5]],
 [["чиркнул",10.0],["лоха,",10.5],["снял",10.75],["часы,",11.0]],
 [["смотрю",11.25],["на",11.75],["ся:",12.0],["«как",12.25],["же",12.5],["я",12.75],["крут!»",13.0]],
]
SC=[[3.4,6.9],[6.9,9.9],[9.9,11.2],[11.2,99]]
GLOW=['#5a0a0a','#1d3a6a','#3a3a3a','#6a5a10']
PEMO=['🫀','🚪','⌚️','😎']
END=[13.05,13.37]
HTML='''
<div class="card" id="c1" style="background:#000">
 <div class="hdr" style="color:#ff375f">❤ ЭКГ</div>
 <svg width="600" height="230" style="position:absolute;top:90px;left:0"><path id="ecg" fill="none" stroke="#ff375f" stroke-width="5" stroke-linejoin="round"/></svg>
 <div class="c" style="top:320px"><div id="st1" style="font-size:40px;font-weight:900">ритм: норма</div></div>
 <div id="gr" style="position:absolute;left:30px;right:30px;bottom:30px;background:#1c1c1e;border-radius:24px;padding:20px 22px;display:flex;gap:16px;align-items:center;opacity:0">
  <div style="width:60px;height:60px;border-radius:50%;background:#3a3a3c;display:flex;align-items:center;justify-content:center;font-size:32px">⭕️</div>
  <div><div style="font-size:26px;font-weight:800">Группа «Круг»</div><div id="grs" style="font-size:21px;color:#8e8e93;font-weight:600">12 участников</div></div></div>
</div>
<div class="card" id="c2" style="background:#1c1c1e">
 <div class="hdr" style="color:#ff9f0a">Дом · Входная дверь</div>
 <div style="position:absolute;left:30px;right:30px;top:90px;height:300px;border-radius:26px;background:linear-gradient(180deg,#2a2620,#0e0c0a);overflow:hidden;display:flex;align-items:center;justify-content:center"><div id="dr" style="font-size:200px">🚪</div>
  <div style="position:absolute;left:14px;top:14px;padding:4px 12px;border-radius:8px;background:#ff3b30;font-size:18px;font-weight:800" class="mono">● LIVE</div></div>
 <div id="kn" style="position:absolute;left:24px;right:24px;top:410px;background:rgba(60,60,64,.95);border-radius:24px;padding:16px 20px;display:flex;gap:14px;align-items:center;opacity:0"><div style="font-size:40px">🔔</div><div><div style="font-size:24px;font-weight:800">Стук в дверь</div><div style="font-size:20px;color:#d1d1d6;font-weight:600">кто-то у входа</div></div></div>
 <div id="lt" style="position:absolute;left:24px;right:24px;top:520px;background:#0f3a1f;border-radius:24px;padding:16px 20px;display:flex;gap:14px;align-items:center;opacity:0"><div style="font-size:40px">📦</div><div><div style="font-size:24px;font-weight:800;color:#30d158">Лут получен</div><div style="font-size:20px;color:#9fe3b4;font-weight:600">+1 · забрали</div></div></div>
</div>
<div class="card" id="c3" style="background:#000">
 <div class="c" style="top:60px;font-size:28px;font-weight:700">Apple Watch</div>
 <div id="wt" class="c" style="top:120px;font-size:220px">⌚️</div>
 <div class="c" style="top:400px"><div id="w3" style="font-size:36px;font-weight:900">Подключено</div><div id="w3b" style="font-size:22px;color:#8e8e93;font-weight:600;margin-top:8px">на запястье</div></div>
</div>
<div class="card" id="c4" style="background:#000">
 <div style="position:absolute;left:0;right:0;top:0;height:520px;background:radial-gradient(circle at 50% 45%,#3a3428,#0c0a08);display:flex;align-items:center;justify-content:center"><div id="me" style="font-size:240px">😎</div>
  <div style="position:absolute;left:20px;top:20px;padding:6px 14px;border-radius:10px;background:rgba(255,214,10,.9);color:#000;font-size:20px;font-weight:900">ПОРТРЕТ</div></div>
 <div class="c" style="top:540px"><div style="font-size:20px;color:#8e8e93;font-weight:700">уровень крутости</div><div id="kr" class="mono" style="font-size:56px;font-weight:800;color:#ffd60a">0%</div></div>
</div>
'''
RENDER='''
 {const flat=t>=4.5&&t<5.25;let d='M0 115';for(let x=0;x<=600;x+=4){const ph=((x/600*3+t*1.6)%1);let v=0;if(!flat){if(ph>.4&&ph<.44)v=-80;else if(ph>.44&&ph<.47)v=55;}d+=` L${x} ${115+v}`}$('ecg').setAttribute('d',d);$('ecg').setAttribute('stroke',flat?'#8e8e93':'#ff375f');
  $('st1').textContent=t<4.5?'ритм: норма':(flat?'чуть не сдох…':'восстановлено ✓');$('st1').style.color=flat?'#8e8e93':(t>=5.25?'#30d158':'#fff');
  $('gr').style.opacity=seg(t,6.0,6.15);const l=t>=6.6;$('grs').textContent=l?'вы покинули группу':'12 участников';$('grs').style.color=l?'#ff453a':'#8e8e93';if(si==0)shake('c1',t,4.75,8);}
 {$('kn').style.opacity=seg(t,8.25,8.35);$('dr').style.transform=`translateX(${t>=7.75&&t<8.6?Math.sin(t*60)*8:0}px)`;$('lt').style.opacity=seg(t,9.5,9.6);$('lt').style.transform=`scale(${1+.15*pop(t,9.5,6)})`;}
 {const o=t>=10.75;$('w3').textContent=o?'Часы сняты':'Подключено';$('w3').style.color=o?'#ff453a':'#fff';$('w3b').textContent=o?'пара разорвана · теперь у нас':'на запястье';$('wt').style.transform=`translateY(${o?-eo(seg(t,10.75,11.1))*60:0}px) rotate(${o?-15:0}deg)`;}
 {const k=t<12.25?0:Math.round(lerp(0,100,eo(seg(t,12.25,13.0))));$('kr').textContent=k+'%'+(t>=13.0?' 🔥':'');$('me').style.transform=`scaleX(-1) scale(${1+.25*pop(t,13.0,5)})`;}
'''
