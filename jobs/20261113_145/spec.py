DUR=15.1
FADE=14.7
START=0
SONG='ARTIK & ASTI — Всё мимо'
BG='linear-gradient(180deg,#140a14,#050307)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Парни,",0.0],["оставьте",0.4],["меня",0.88],["в",1.12],["покое",1.38]],
 [["я",1.92],["не",2.32],["знакомлюсь,",2.52],["меня",3.22],["и",3.38],["так",3.5],["кроет",3.7]],
 [["лишь",4.2],["по",4.74],["рекламе",4.8],["в",5.42],["директ",5.5],["и",5.8],["ВК",5.94]],
 [["я",6.2],["всё",6.78],["решила",7.0],["наверняка",7.54]],
 [["всё",8.5],["мимо!",8.8]],
 [["я",9.2],["никогда",10.26],["ещё",10.94],["так",11.66],["сильно",12.1],["не",12.5],["любила",12.88]],
 [["всё",13.98],["мимо!",14.3]],
]
SC=[[-0.3,1.85],[1.85,4.1],[4.1,6.1],[6.1,8.4],[8.4,9.1],[9.1,13.9],[13.9,99]]
GLOW=['#5a1d4a','#7a1f4a','#1d3a7a','#1a5c2e','#7a4a0a','#7a0a2a','#5a1d4a']
PEMO=['🔕','💔','📩','✅','🏀','❤️','🏹']
END=[14.7,15.1]
CSS='''.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}
.nt{position:absolute;left:24px;right:24px;background:rgba(60,60,64,.92);border-radius:22px;padding:12px 16px;font-size:21px;font-weight:700;display:flex;gap:12px;align-items:center}
.nt i{font-style:normal;width:44px;height:44px;border-radius:12px;background:#30d158;display:flex;align-items:center;justify-content:center;font-size:24px;flex:none}'''
NT=[('Артём','привет красотка 😏'),('Денис','го гулять?'),('Макс','ты где живёшь'),('Тимур','можно познакомиться?'),('Кирилл','ау 👋👋👋')]
PR=[('Олег, 24','🧔'),('Влад, 27','👨‍🦱'),('Эмиль, 22','🧑‍🎤'),('Руслан, 30','🤵')]
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#2a1a4a,#0a0614)">
 <div class="c" style="top:30px;font-size:90px;font-weight:300">23:47</div>
 '''+''.join(f'<div class="nt" id="n1_{i}" style="top:{150+i*70}px;opacity:0"><i>💬</i><div><b>{a}</b> <span style="color:#d1d1d6;font-weight:600">{b}</span></div></div>' for i,(a,b) in enumerate(NT))+'''
 <div id="dnd1" style="position:absolute;left:150px;right:150px;top:170px;background:#5e5ce6;border-radius:30px;padding:14px;text-align:center;font-size:26px;font-weight:900;opacity:0">🌙 Не беспокоить</div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#fff;color:#111">
 <div class="hdr" style="color:#ff2d55">Знакомства</div>
 '''+''.join(f'<div id="p2_{i}" style="position:absolute;left:90px;top:80px;width:420px;height:420px;border-radius:30px;background:linear-gradient(160deg,#c7c7cc,#8e8e93);box-shadow:0 10px 30px rgba(0,0,0,.25);z-index:{10-i}"><div class="c" style="top:70px;font-size:170px">{e}</div><div style="position:absolute;left:24px;bottom:20px;font-size:32px;font-weight:900;color:#fff">{n}</div><div id="x2_{i}" style="position:absolute;inset:0;border-radius:30px;background:rgba(255,45,85,.55);display:flex;align-items:center;justify-content:center;font-size:150px;color:#fff;font-weight:900;opacity:0">✕</div></div>' for i,(n,e) in enumerate(PR))+'''
 <div class="c" style="top:250px;font-size:30px;font-weight:800;color:#8e8e93">анкеты закончились 🙅‍♀️</div>
 <div id="m2" style="position:absolute;left:30px;right:30px;top:520px;background:#ffe5ec;border-radius:22px;padding:14px 18px;font-size:24px;font-weight:900;color:#ff2d55;opacity:0">💘 уже влюблена: <span id="m2v">0</span>%</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#000">
 <div style="display:flex;align-items:center;gap:20px;padding:34px 30px 0"><div style="width:110px;height:110px;border-radius:50%;background:linear-gradient(45deg,#feda75,#d62976,#4f5bd5);display:flex;align-items:center;justify-content:center;font-size:56px">🧢</div><div><div style="font-size:30px;font-weight:900">lali.official</div><div style="font-size:21px;color:#aeaeb2;font-weight:600;margin-top:6px">📩 По рекламе — директ / ВК<br>❌ не знакомлюсь</div></div></div>
 <div id="d3a" class="row" style="position:absolute;left:24px;right:24px;top:220px;opacity:0"><span>👤 «привет, познакомимся?»</span><span id="d3as" style="margin-left:auto;color:#8e8e93;font-size:20px"></span></div>
 <div id="d3b" class="row" style="position:absolute;left:24px;right:24px;top:310px;opacity:0"><span>💼 «реклама? прайс?»</span><span id="d3bs" style="margin-left:auto;color:#30d158;font-size:20px"></span></div>
 <div id="vk3" style="position:absolute;left:24px;top:400px;background:#0077ff;border-radius:18px;padding:10px 20px;font-size:28px;font-weight:900;opacity:0">ВК ✓</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:#30d158">Решение</div><div class="ttl" style="color:#111">Что делаем?</div>
 <div style="position:absolute;left:30px;right:30px;top:170px;background:#fff;border-radius:24px;padding:4px 24px;font-size:28px;font-weight:800">
  <div style="padding:18px 0;border-bottom:1px solid #eee">☐ подумать</div><div style="padding:18px 0;border-bottom:1px solid #eee">☐ может быть</div><div id="ok4" style="padding:18px 0">☐ наверняка</div></div>
 <div id="st4" style="position:absolute;left:250px;top:400px;border:8px solid #30d158;border-radius:18px;padding:8px 18px;font-size:44px;font-weight:900;color:#30d158;transform:rotate(-10deg);opacity:0">НАВЕРНЯКА</div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c5" style="background:linear-gradient(180deg,#ff9f43,#c45a10)">
 <div style="position:absolute;right:60px;top:110px;width:150px;height:110px;border:8px solid #fff;border-top:none;background:repeating-linear-gradient(90deg,rgba(255,255,255,.5) 0 4px,transparent 4px 18px)"></div>
 <div style="position:absolute;right:40px;top:100px;width:190px;height:12px;background:#ff3b30;border-radius:6px"></div>
 <div id="bl5" style="position:absolute;font-size:70px;z-index:6">🏀</div>
 <div id="mm5" class="c" style="top:300px;font-size:110px;font-weight:900;color:#fff;text-shadow:0 8px 0 #7a2a00;opacity:0">МИМО</div>
 <div class="ch" data-p="e"></div>
</div>
<div class="card" id="c6" style="background:radial-gradient(circle at 50% 40%,#5a0a2a,#14040a)">
 <div class="hdr" style="color:#ff375f">Любовь · уровень</div>
 <div style="position:absolute;left:150px;top:90px;width:300px;height:300px;overflow:hidden;-webkit-mask:radial-gradient(circle at 30% 30%,#000 29%,transparent 30%),radial-gradient(circle at 70% 30%,#000 29%,transparent 30%),linear-gradient(45deg,transparent 30%,#000 30%,#000 70%,transparent 70%)"></div>
 <div id="hb6" class="c" style="top:80px;font-size:280px;line-height:1;filter:grayscale(1) brightness(.5)">❤️</div>
 <div id="hf6" class="c" style="top:80px;font-size:280px;line-height:1;clip-path:inset(100% 0 0 0)">❤️</div>
 <div id="pc6" class="c mono" style="top:390px;font-size:70px;font-weight:900">0%</div>
 <div id="er6" class="c" style="top:470px;font-size:26px;font-weight:900;color:#ff453a;opacity:0">⚠️ ПЕРЕПОЛНЕНИЕ</div>
 <div id="hh6" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="f"></div>
</div>
<div class="card" id="c7" style="background:linear-gradient(180deg,#3a2a4a,#1a1024)">
 <div id="tg7" style="position:absolute;left:180px;top:90px;width:240px;height:240px;border-radius:50%;background:repeating-radial-gradient(circle,#ff375f 0 20px,#fff 20px 40px);box-shadow:0 10px 30px rgba(0,0,0,.4)"></div>
 <div id="ar7" style="position:absolute;inset:0;z-index:6"></div>
 <div id="mm7" class="c" style="top:360px;font-size:70px;font-weight:900;color:#ff375f;opacity:0">ВСЁ МИМО 💘</div>
 <div class="ch" data-p="g"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#ff2d78','#ff8ac4','#ff2d78');});})();'''
RENDER='''
 {const T=[0.0,0.2,0.4,0.6,0.88];const off=seg(t,1.38,1.6);T.forEach((s,i)=>{const e=$('n1_'+i);e.style.opacity=seg(t,s,s+.1)*(1-off);e.style.transform=`translateY(${(1-eb(seg(t,s,s+.25)))*-30}px) translateX(${off*(i%2?600:-600)}px)`});
  $('dnd1').style.opacity=seg(t,1.38,1.5);$('dnd1').style.transform=`scale(${1+.2*pop(t,1.38,6)})`;
  place('a',300,700,.85,false);pose('a',t<1.38?{aL:150,aR:-150,hd:Math.sin(t*20)*6,open:1}:{aL:8,aR:-8,hd:-5});}
 {const T=[1.92,2.32,2.52,3.22];T.forEach((s,i)=>{const k=seg(t,s,s+.3);$('p2_'+i).style.transform=`translateX(${-eo(k)*700}px) rotate(${-k*30}deg)`;$('x2_'+i).style.opacity=t>=s-.05?1:0});
  $('m2').style.opacity=seg(t,3.7,3.8);$('m2v').textContent=Math.round(100*eo(seg(t,3.7,4.0)));
  place('b',500,690,.75,true);pose('b',{aL:8,aR:-8,hd:t<3.7?Math.sin(t*14)*14:0,open:t>=3.7});}
 {$('d3a').style.opacity=seg(t,4.3,4.4);$('d3as').textContent=t>=4.8?'игнор 🙈':'';$('d3a').style.filter=t>=4.8?'opacity(.45)':'none';
  $('d3b').style.opacity=seg(t,5.0,5.1);$('d3bs').textContent=t>=5.5?'✓ отвечаю':'';$('vk3').style.opacity=seg(t,5.94,6.0);$('vk3').style.transform=`scale(${1+.3*pop(t,5.94,8)})`;
  place('c',450,690,1.0,true);pose('c',t>=5.42?{aL:8,aR:-90,open:1}:{aL:8,aR:-8});}
 {const on=t>=7.54;$('ok4').textContent=on?'☑ наверняка':'☐ наверняка';$('ok4').style.color=on?'#30d158':'#111';$('st4').style.opacity=seg(t,7.54,7.6);$('st4').style.transform=`rotate(-10deg) scale(${lerp(2,1,eb(seg(t,7.54,7.8)))})`;
  place('d',130,690,.95,false);pose('d',{aL:8,aR:-8,hd:t>=7.0?Math.sin(t*16)*12:0});}
 {const k=seg(t,8.5,9.05);const x=lerp(180,600,k),y=lerp(470,20,k)-Math.sin(k*Math.PI)*120;$('bl5').style.left=(t<8.5?170:x)+'px';$('bl5').style.top=(t<8.5?420:y)+'px';$('bl5').style.transform=`rotate(${k*720}deg)`;
  $('mm5').style.opacity=seg(t,8.8,8.85);$('mm5').style.transform=`scale(${1+.4*pop(t,8.8,8)}) rotate(-6deg)`;
  place('e',170,690,1.1,false);pose('e',t<8.5?{aL:8,aR:-150}:(t<8.8?{aL:8,aR:-120}:{aL:60,aR:-60,hd:12,open:1}));}
 {const v=t<12.1?100*eo(seg(t,9.2,12.1)):lerp(100,250,seg(t,12.1,12.88));$('pc6').textContent=Math.round(v)+'%';$('hf6').style.clipPath=`inset(${100-Math.min(100,v)}% 0 0 0)`;
  $('hf6').style.transform=$('hb6').style.transform=`scale(${1+.08*Math.abs(Math.sin(t*(4+v/30)))+(v>100?(v-100)/600:0)})`;$('er6').style.opacity=v>100?1:0;$('pc6').style.color=v>100?'#ff453a':'#fff';
  let h='';for(let i=0;i<10;i++){const s=9.4+i*.35;if(t>=s){const p=(t-s)/1.6;h+=`<div style="position:absolute;left:${200+rnd(i)*250}px;top:${600-p*500}px;font-size:${30+rnd(i+2)*24}px;opacity:${1-p}">❤️</div>`}}$('hh6').innerHTML=h;
  place('f',500,700,.7,true);pose('f',{aL:120,aR:-120,hd:-8,bob:Math.sin(t*3)*4});}
 {const A=[[13.98,90,140,-30],[14.1,470,380,25],[14.3,520,110,-15]];let a='';A.forEach(([s,x,y,r])=>{if(t>=s){const k=eo(seg(t,s,s+.15));a+=`<div style="position:absolute;left:${lerp(300,x,k)}px;top:${lerp(700,y,k)}px;font-size:70px;transform:rotate(${r}deg)">🏹</div>`}});$('ar7').innerHTML=a;
  $('mm7').style.opacity=seg(t,14.3,14.35);$('mm7').style.transform=`scale(${1+.3*pop(t,14.3,6)})`;
  place('g',300,690,1.0,false);pose('g',t>=14.3?{aL:60,aR:-60,hd:12,open:1}:{aL:8,aR:-8});}
'''
