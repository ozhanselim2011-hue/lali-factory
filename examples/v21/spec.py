BG='linear-gradient(180deg,#140c06,#050302)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["и",0.4],["бездонные",0.6],["глаза",1.3]],
 [["ты",2.0],["актриса",2.3],["моих",3.0],["снов",3.7]],
 [["мы",4.0],["с",4.3],["тобою",4.5],["не",4.9],["друзья",5.3]],
 [["притворившись",6.1],["тишиной",7.1]],
 [["ты",7.8],["приехала",8.3],["на",9.3],["час",9.5]],
 [["но",10.1],["останешься",10.4]],
]
SC=[[-0.3,1.95],[1.95,3.95],[3.95,6.0],[6.0,7.75],[7.75,10.05],[10.05,99]]
GLOW=['#5a3a10','#2a1d5a','#5a1a1a','#2a2a3a','#5a3a0a','#7a1f4a']
PEMO=['👁️','🌙','🚫','🔕','🚕','💗']
END=[11.45,11.84]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#000">
 <div class="hdr" style="color:#ff9f0a">Лупа</div>
 <div style="position:absolute;left:0;right:0;top:120px;display:flex;justify-content:center;gap:40px">
  <div class="eye" style="width:230px;height:230px;border-radius:50%;background:radial-gradient(circle,#000 0 38%,#5a3a1a 40%,#2a1a0a 68%,#f2ece0 70%);position:relative;overflow:hidden" id="eyeL"><div style="position:absolute;left:58px;top:56px;width:34px;height:34px;border-radius:50%;background:#fff"></div></div>
  <div class="eye" style="width:230px;height:230px;border-radius:50%;background:radial-gradient(circle,#000 0 38%,#5a3a1a 40%,#2a1a0a 68%,#f2ece0 70%);position:relative;overflow:hidden" id="eyeR"><div style="position:absolute;left:58px;top:56px;width:34px;height:34px;border-radius:50%;background:#fff"></div></div></div>
 <div class="ch" data-p="a"></div>
 <div class="c" style="bottom:36px"><div style="font-size:20px;color:#8e8e93;font-weight:700">глубина</div><div id="dp" class="mono" style="font-size:52px;font-weight:800;color:#ff9f0a">0 м</div></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#120c2a,#05030c)">
 <div class="hdr" style="color:#5e5ce6">Здоровье · Сон</div>
 <div id="dream" style="position:absolute;left:150px;top:90px;width:320px;height:210px;border-radius:110px;background:#fff;color:#111;display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0">
  <div style="font-size:90px;line-height:1">👩‍🎤</div><div style="font-size:22px;font-weight:900;margin-top:4px">в главной роли: ты ⭐</div>
  <div style="position:absolute;left:30px;bottom:-30px;width:34px;height:34px;border-radius:50%;background:#fff"></div><div style="position:absolute;left:6px;bottom:-56px;width:18px;height:18px;border-radius:50%;background:#fff"></div></div>
 <div style="position:absolute;left:60px;right:60px;top:520px;height:60px;border-radius:20px;background:#3a2a5a"></div>
 <div style="position:absolute;left:60px;top:470px;width:110px;height:60px;border-radius:24px;background:#e5e5ea"></div>
 <div class="ch" data-p="b"></div>
 <div id="zz2" style="position:absolute;inset:0"></div>
 <div class="c mono" style="bottom:30px;font-size:24px;font-weight:700;color:#aeaeb2" id="sl2">сон: 0 ч 00 мин</div>
</div>
<div class="card" id="c3" style="background:#1c1c1e">
 <div class="hdr" style="color:#0a84ff">‹ Контакты · Она</div>
 <div style="position:absolute;left:30px;right:30px;top:90px;background:#2c2c2e;border-radius:24px;padding:20px 24px">
  <div style="font-size:20px;color:#8e8e93;font-weight:700">отношения</div>
  <div style="font-size:40px;font-weight:900;margin-top:6px;position:relative;display:inline-block"><span id="fr3">друзья 🤝</span><span id="sk3" style="position:absolute;left:-6px;top:50%;height:6px;background:#ff453a;width:0;border-radius:3px"></span></div>
  <div id="nf3" style="font-size:30px;font-weight:900;color:#ff2d55;margin-top:8px;opacity:0">не друзья 💗</div></div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:#0c0c0e">
 <div class="hdr">Пункт управления</div>
 <div id="sw4" style="position:absolute;left:50%;top:110px;margin-left:-70px;width:140px;height:240px;border-radius:40px;background:#2c2c2e;box-shadow:inset 0 0 0 3px #3a3a3c">
  <div id="kn4" style="position:absolute;left:14px;right:14px;height:100px;border-radius:30px;background:#fff;top:14px;display:flex;align-items:center;justify-content:center;font-size:54px">🔔</div></div>
 <div id="t4" class="c" style="top:370px;font-size:30px;font-weight:900">Звонок</div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c5" style="background:#1d2620">
 <svg width="600" height="690" style="position:absolute;inset:0"><path d="M-10 520 C 150 470 260 560 420 500 S 560 420 610 440" fill="none" stroke="#3b434c" stroke-width="60"/></svg>
 <div style="position:absolute;left:430px;top:330px;font-size:140px;line-height:1">🏠</div>
 <div id="taxi" style="position:absolute;font-size:90px;line-height:1">🚕</div>
 <div class="ch" data-p="e"></div>
 <div style="position:absolute;left:24px;right:24px;top:24px;background:rgba(30,30,32,.95);border-radius:26px;padding:18px 24px;display:flex;justify-content:space-between;align-items:center">
  <div><div id="t5a" style="font-size:28px;font-weight:800">Она едет…</div><div style="font-size:20px;color:#8e8e93;font-weight:600">визит</div></div><div id="tm5" class="mono" style="font-size:40px;font-weight:800;color:#ff9f0a">—</div></div>
</div>
<div class="card" id="c6" style="background:linear-gradient(180deg,#2a0a1a,#0a0408)">
 <div class="c" style="top:50px"><div style="font-size:22px;color:#aeaeb2;font-weight:700">⏱ осталось</div><div id="tm6" class="mono" style="font-size:96px;font-weight:800;color:#ff9f0a">0:12</div></div>
 <div id="hh6" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="f"></div><div class="ch" data-p="g"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;const c={g:['#ff9ac1','#f3e8ff','#b38cff']}[p]||['#64d2ff','#ff8ac4','#ff2d78'];e.id='ch_'+p;e.innerHTML=CH(p,...c);});
 let z='';for(let i=0;i<4;i++)z+=`<div id="z2_${i}" style="position:absolute;font-size:${28+i*8}px;font-weight:900;color:#9a9aff">z</div>`;$('zz2').innerHTML=z;
 let h='';for(let i=0;i<10;i++)h+=`<div id="h6_${i}" style="position:absolute;font-size:40px">💗</div>`;$('hh6').innerHTML=h;})();'''
RENDER='''
 // S1 eyes: Lali falls into the eyes
 {const z=eo(seg(t,0.6,1.9));['eyeL','eyeR'].forEach(id=>{$(id).style.transform=`scale(${1+z*.25})`;});
  const f=seg(t,1.3,1.95);const o=f>0?{aL:150+Math.sin(t*20)*20,aR:-150-Math.sin(t*20)*20,lL:Math.sin(t*14)*25,lR:-Math.sin(t*14)*25,open:1}:{aL:8,aR:-8,hd:-15};
  place('a',lerp(300,180+0,eo(f)),lerp(600,260,eo(f)),lerp(1.0,.15,eo(f)),false,f*540);pose('a',o);
  $('dp').textContent=t<1.3?Math.round(seg(t,0.4,1.3)*300)+' м':'∞ м';$('dp').style.transform=`scale(${1+.2*pop(t,1.3,6)})`;}
 // S2 sleep + dream
 {place('b',330,505,.85,false,-90);pose('b',{aL:10,aR:-30,hd:4});$('dream').style.opacity=seg(t,2.3,2.5);$('dream').style.transform=`scale(${eb(seg(t,2.3,2.6))}) translateY(${Math.sin(t*2)*6}px)`;
  for(let i=0;i<4;i++){const ph=((t*.8)+i/4)%1;const e=$('z2_'+i);e.style.left=(230+ph*60)+'px';e.style.top=(420-ph*120)+'px';e.style.opacity=1-ph;}
  const m=Math.round(seg(t,2.0,3.9)*480);$('sl2').textContent='сон: '+Math.floor(m/60)+' ч '+String(m%60).padStart(2,'0')+' мин · о тебе';}
 // S3 not friends
 {$('sk3').style.width=(eo(seg(t,4.9,5.2))*110)+'%';$('nf3').style.opacity=seg(t,5.3,5.45);$('nf3').style.transform=`scale(${1+.2*pop(t,5.3,6)})`;
  let o;if(t<4.9)o={aL:8,aR:-95,hd:0};else if(t<5.3)o={aL:8,aR:-8,hd:Math.sin(t*30)*14};else o={aL:-58,aR:58,hd:8,open:1};
  o.bob=-pop(t,5.3,6)*40;place('c',300,650,1.25,false);pose('c',o);}
 // S4 silent
 {const on=t>=7.1;$('kn4').style.top=(on?126:14)+'px';$('kn4').textContent=on?'🔕':'🔔';$('kn4').style.background=on?'#ff9f0a':'#fff';$('sw4').style.transform=`scale(${1+.06*pop(t,7.1,6)})`;
  $('t4').textContent=on?'Бесшумный · тишина':'Звонок';$('t4').style.color=on?'#ff9f0a':'#fff';
  const o=t<6.9?{aL:8,aR:-120+Math.sin(t*6)*5}:{aL:8,aR:112,hd:-8};place('d',460,670,1.0,true);pose('d',o);}
 // S5 she arrives for an hour
 {const p=eo(seg(t,7.8,8.8));$('taxi').style.left=lerp(-120,250,p)+'px';$('taxi').style.top=lerp(450,430,p)+'px';$('taxi').style.transform=`scaleX(-1) translateY(${p<1?Math.sin(t*30)*2:0}px)`;
  const o=t<8.8?{aL:8,aR:-150+Math.sin(t*12)*22,open:1}:{aL:-58,aR:58,hd:6};o.bob=-pop(t,8.8,5)*40;place('e',420,640,.95,true);pose('e',o);
  const a=t>=8.8;$('t5a').textContent=a?'Она приехала 💗':'Она едет…';const r=t<9.5?(a?3600:0):3600-(t-9.5)*900;$('tm5').textContent=t<9.3?'—':'на '+Math.floor(r/3600)+':'+String(Math.floor(r%3600/60)).padStart(2,'0');}
 // S6 stays
 {const st=t>=10.4;const r=Math.max(0,12-(t-10.05)*20);$('tm6').textContent=st?'∞':'0:'+String(Math.floor(r)).padStart(2,'0');$('tm6').style.color=st?'#ff2d55':'#ff9f0a';$('tm6').style.transform=`scale(${1+.35*pop(t,10.4,5)})`;
  const c=eo(seg(t,10.4,10.9));place('f',lerp(200,262,c),640,1.05,false);place('g',lerp(400,338,c),640,1.0,true);
  pose('f',st?{aL:-40,aR:-120,hd:8}:{aL:8,aR:-8});pose('g',st?{aL:-40,aR:-120,hd:8,open:1}:{aL:8,aR:-8});
  for(let i=0;i<10;i++){const ph=((t-10.4)*.7+i/10)%1;const e=$('h6_'+i);e.style.left=(300+Math.sin(i*2.3+ph*4)*120)+'px';e.style.top=(420-ph*300)+'px';e.style.opacity=st?1-ph:0;}}
'''
