# Комбинация — А я люблю военных (TikTok-тренд): анкета, качалка, деловой, медали, чек-лист «мэтч»
DUR=15.4; FADE=15.0; START=0
SONG='Комбинация — А я люблю военных'
BG='linear-gradient(180deg,#14100a,#050306)'
SUBW='900'
SUBX='text-transform:uppercase'
RED='военных'
LINES=[
 [["а",0.0],["я",0.44],["люблю",0.7],["военных,",1.06]],
 [["красивых,",1.96],["здоровенных",2.96]],
 [["ещё",3.84],["люблю",4.58],["крутых",4.86],["и",5.78],["всяких",6.04],["деловых",6.84]],
 [["а",7.56],["я",8.12],["люблю",8.5],["военных,",8.92],["красивых,",9.94],["здоровенных",10.76]],
 [["ещё",11.7],["люблю",12.4],["крутых",12.78],["и",13.6],["всяких",13.84],["деловых",14.66]],
]
SC=[[-0.3,1.95],[1.95,3.8],[3.8,7.5],[7.5,11.65],[11.65,99]]
GLOW=['#7a1f4a','#7a4a1a','#1a4a7a','#3a5a1a','#7a1f4a']
PEMO=['💘','💪','💼','🎖️','✅']
END=[15.05,15.4]
CSS='''.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}
.pill{position:absolute;padding:10px 22px;border-radius:30px;font-size:34px;font-weight:900;opacity:0;z-index:9}
.chk{display:flex;align-items:center;gap:14px;background:#2c2c2e;border-radius:20px;padding:14px 18px;margin-bottom:10px;font-size:28px;font-weight:800;opacity:.35}
.chk b{margin-left:auto;width:40px;height:40px;border-radius:50%;background:#3a3a3c;display:flex;align-items:center;justify-content:center;font-size:24px}'''
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div id="pf1" style="position:absolute;left:40px;right:40px;top:40px;height:520px;border-radius:34px;overflow:hidden;background:linear-gradient(180deg,#4b5d3a,#1f2a16)">
  <div class="ch" data-p="a"></div>
  <div style="position:absolute;left:0;right:0;bottom:0;padding:24px;background:linear-gradient(transparent,rgba(0,0,0,.85));z-index:6">
   <div style="font-size:40px;font-weight:900">Лали, 24 🪖</div><div style="font-size:22px;color:#c7c7cc;font-weight:600">военный · 2 км от тебя</div></div>
  <div id="lk1" style="position:absolute;left:40px;top:40px;border:6px solid #30d158;color:#30d158;border-radius:14px;padding:0 16px;font-size:54px;font-weight:900;opacity:0;z-index:7;transform:rotate(-16deg)">LIKE</div></div>
 <div style="position:absolute;left:0;right:0;bottom:34px;display:flex;justify-content:center;gap:60px;font-size:52px">
  <div style="width:96px;height:96px;border-radius:50%;background:#2c2c2e;display:flex;align-items:center;justify-content:center">✖️</div>
  <div id="hb1" style="width:96px;height:96px;border-radius:50%;background:#2c2c2e;display:flex;align-items:center;justify-content:center">💚</div></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#2a2a2e,#111114)">
 <div class="hdr">Качалка · сет 4/4</div><div class="ttl">здоровенность</div>
 <div style="position:absolute;left:40px;right:40px;top:150px;height:26px;border-radius:13px;background:#3a3a3c;overflow:hidden"><div id="mb2" style="height:26px;width:0;background:linear-gradient(90deg,#ff9f0a,#ff375f)"></div></div>
 <div id="mp2" class="mono" style="position:absolute;right:40px;top:186px;font-size:30px;font-weight:900;color:#ff9f0a">0%</div>
 <div class="ch" data-p="b"></div>
 <div id="db2" style="position:absolute;font-size:80px;z-index:6">🏋️</div>
</div>
<div class="card" id="c3" style="background:#0b1220">
 <div class="hdr">Брокер · портфель</div><div class="ttl" id="bal3" class="mono">0 ₽</div>
 <svg width="600" height="300" style="position:absolute;left:0;top:150px"><path id="ln3" d="M30 260 L110 230 L190 240 L270 170 L350 185 L430 110 L510 60 L570 30" fill="none" stroke="#30d158" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="700" stroke-dashoffset="700"/></svg>
 <div class="ch" data-p="c"></div>
 <div id="bc3" style="position:absolute;font-size:70px;z-index:6;opacity:0">💼</div>
 <div id="kr3" class="pill" style="background:#0a84ff;color:#fff">😎 КРУТОЙ</div><div id="dl3" class="pill" style="background:#30d158;color:#06210f">💼 ДЕЛОВОЙ</div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#56653f,#2b331f)">
 <div class="hdr" style="color:#e6f0c8">Парад</div><div class="ttl" style="color:#fff">наградной лист</div>
 <div class="ch" data-p="d"></div>
 <div id="md4_0" class="pill" style="background:#ffd60a;color:#111">🎖️ военный</div><div id="md4_1" class="pill" style="background:#ff8ac4;color:#111">✨ красивый</div><div id="md4_2" class="pill" style="background:#ff9f0a;color:#111">💪 здоровенный</div>
</div>
<div class="card" id="c5" style="background:#1c1c1e">
 <div class="hdr">Её список «идеальный парень»</div>
 <div style="position:absolute;left:30px;right:30px;top:80px">
  <div class="chk" id="k5_0">🪖 военный<b>✓</b></div><div class="chk" id="k5_1">💪 здоровенный<b>✓</b></div>
  <div class="chk" id="k5_2">😎 крутой<b></b></div><div class="chk" id="k5_3">💼 деловой<b></b></div></div>
 <div class="ch" data-p="e"></div>
 <div id="mt5" style="position:absolute;left:330px;top:480px;font-size:44px;font-weight:900;color:#ff2d78;opacity:0;z-index:8">МЭТЧ 💘</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;const mil=(p=='a'||p=='d');e.id='ch_'+p;e.innerHTML=CH(p,mil?'#3d4a2a':'#64d2ff',mil?'#7a8a50':'#ff8ac4',mil?'#4b5d3a':'#ff2d78');});})();
const popPill=(id,t,s,x,y)=>{const e=$(id);const p=eb(seg(t,s,s+.18));e.style.opacity=t>=s?1:0;e.style.left=x+'px';e.style.top=y+'px';e.style.transform=`scale(${p}) rotate(${(rnd(s*7)-.5)*14}deg)`;};
'''
RENDER='''
 {// c1: анкета, лайк на «военных»
  place('a',260,470,1.25,false);pose('a',{aL:8,aR:-150,hd:-4});
  const lk=seg(t,1.06,1.2);$('lk1').style.opacity=lk;$('lk1').style.transform=`rotate(-16deg) scale(${lerp(1.8,1,eo(lk))})`;
  $('hb1').style.transform=`scale(${1+.35*pop(t,1.06,6)})`;$('hb1').style.background=t>=1.06?'#30d158':'#2c2c2e';
  $('pf1').style.transform=`translateX(${eo(seg(t,1.5,1.95))*80}px) rotate(${eo(seg(t,1.5,1.95))*8}deg)`;}
 {// c2: качалка — шкала и рост
  const m=eo(seg(t,1.96,3.0));$('mb2').style.width=(m*100)+'%';$('mp2').textContent=Math.round(m*100)+'%';
  const big=1+.35*eo(seg(t,2.96,3.2));place('b',300,650,1.05*big,false);
  const lift=Math.abs(Math.sin(t*9));pose('b',{aL:150-lift*40,aR:-150+lift*40,open:t>=2.96?1:0,hd:-6});
  $('db2').style.left='255px';$('db2').style.top=(650-300*1.05*big-40-lift*30)+'px';$('ch_b').style.filter=t>=2.96?'drop-shadow(0 0 30px #ff9f0a)':'none';}
 {// c3: деловой — график и баланс
  const g=eo(seg(t,3.84,6.9));$('ln3').setAttribute('stroke-dashoffset',700*(1-g));$('bal3').textContent=fmt(g*12500000)+' ₽';
  place('c',150,680,1.05,false);pose('c',t<4.86?{aL:8,aR:58}:{aL:8,aR:-8,hd:-6,rot:-5});
  $('bc3').style.opacity=t>=6.84?1:0;$('bc3').style.left='170px';$('bc3').style.top=(500+6*Math.sin(t*6))+'px';
  popPill('kr3',t,4.86,300,470);popPill('dl3',t,6.84,280,560);}
 {// c4: парад — честь и медали
  place('d',300,680,1.2,false);pose('d',t<8.5?{aL:8,aR:-8,lL:Math.sin(t*14)*16,lR:-Math.sin(t*14)*16}:{aL:8,aR:150,hd:-4});
  [8.92,9.94,10.76].forEach((s,i)=>popPill('md4_'+i,t,s,[40,320,140][i],[170,220,290][i]));}
 {// c5: чек-лист
  [[11.7,0],[12.0,1],[12.78,2],[14.66,3]].forEach(([s,i])=>{const e=$('k5_'+i);const on=t>=s;e.style.opacity=on?1:.35;
   const b=e.querySelector('b');b.textContent=on?'✓':'';b.style.background=on?'#30d158':'#3a3a3c';e.style.transform=`scale(${1+.06*pop(t,s,8)})`;});
  place('e',150,690,1.0,false);pose('e',t<14.66?{aL:8,aR:166,hd:-6}:{aL:150,aR:-150,open:1,bob:-Math.abs(Math.sin(t*10))*14});
  const m=seg(t,14.7,14.85);$('mt5').style.opacity=m;$('mt5').style.transform=`scale(${eb(m)})`;}
'''
