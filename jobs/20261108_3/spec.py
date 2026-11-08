# Shluzov & NeShluzov — Её парень (Hardstyle Remix): голосовое «забери меня» -> припев «её парень лох»
DUR=19.4; FADE=19.0; START=7.6
SONG='Shluzov & NeShluzov — Её парень (Hardstyle Remix)'
BG='linear-gradient(180deg,#120a14,#050306)'
SUBW='900'
SUBX='text-transform:uppercase'
RED='лох'
LINES=[
 [["сможешь",7.82],["приехать",9.06],["домой?",9.6]],
 [["забери",10.1],["меня,",10.56],["пожалуйста,",10.84],["отсюда",11.34]],
 [["её",12.84],["парень",13.54],["лох,",13.98],["е*ать",14.26],["у",14.7],["тебя",14.86],["ноги",15.14],["топ",15.7],["топ",16.0],["топ",16.48]],
 [["её",16.8],["парень",17.0],["лох,",17.42],["е*ать",17.74],["у",18.14],["тебя",18.28],["с*ськи",18.6],["хоп",19.04],["хоп",19.5],["хоп",19.92]],
 [["её",20.24],["парень",20.4],["лох,",20.8],["да",21.12],["двигай",21.22],["своей",21.68],["ж*пой",21.8],["оп",22.58],["оп",22.92],["оп",23.26]],
 [["её",23.58],["парень",23.84],["лох,",24.26],["но",24.56],["ты",24.68],["его",24.8],["так",25.14],["любишь",25.52],["ок",25.98],["ок",26.28],["ок",26.68]],
]
SC=[[7.3,10.0],[10.0,12.8],[12.8,16.75],[16.75,20.2],[20.2,23.55],[23.55,99]]
GLOW=['#1d4a7a','#1a5c2e','#7a1f2a','#7a2a5a','#5a1d7a','#3a3a5a']
PEMO=['🎙️','🚕','🤡','🦘','🪩','💔']
END=[26.6,27.0]
CSS='''.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}
.pill{position:absolute;padding:10px 22px;border-radius:30px;font-size:40px;font-weight:900;opacity:0;z-index:9}
.msg{position:absolute;max-width:440px;padding:14px 20px;border-radius:24px;font-size:28px;font-weight:600;opacity:0}'''
HTML='''
<div class="card" id="c1" style="background:#0e1621">
 <div style="position:absolute;left:0;right:0;top:0;height:86px;background:#17212b;display:flex;align-items:center;gap:16px;padding:0 26px;font-size:26px;font-weight:800">
  <div style="width:54px;height:54px;border-radius:50%;background:linear-gradient(135deg,#ff8ac4,#ff2d78);display:flex;align-items:center;justify-content:center;font-size:30px">👧</div>
  <div>Она 💔<div id="st1" style="font-size:19px;color:#64b5ef;font-weight:600">записывает голосовое…</div></div></div>
 <div id="vm1" style="position:absolute;left:24px;top:120px;width:430px;height:84px;background:#182533;border-radius:26px;display:flex;align-items:center;gap:14px;padding:0 18px">
  <div style="width:54px;height:54px;border-radius:50%;background:#64b5ef;display:flex;align-items:center;justify-content:center;font-size:24px;color:#0e1621;flex:none">▶</div>
  <div id="wf1" style="display:flex;align-items:center;gap:3px;height:50px"></div>
  <div id="tm1" class="mono" style="font-size:18px;color:#7d8e9e;margin-left:auto">0:07</div></div>
 <div class="msg" id="m1" style="left:24px;top:226px;background:#182533">сможешь приехать домой? 🥺</div>
 <div class="msg" id="r1" style="right:24px;top:420px;background:#2b5278">ща буду 🫡</div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#e9e5dc;color:#111">
 <svg width="600" height="690" style="position:absolute;left:0;top:0">
  <path d="M0 200 H600 M0 470 H600 M170 0 V690 M420 0 V690" stroke="#fff" stroke-width="26"/>
  <path d="M60 640 L60 470 L420 470 L420 200 L540 200 L540 90" stroke="#c9c3b5" stroke-width="12" fill="none" stroke-linecap="round"/>
  <path id="rt2" d="M60 640 L60 470 L420 470 L420 200 L540 200 L540 90" stroke="#ffcc00" stroke-width="12" fill="none" stroke-linecap="round" stroke-dasharray="1120" stroke-dashoffset="1120"/></svg>
 <div style="position:absolute;left:510px;top:50px;font-size:56px">🏚️</div>
 <div id="car2" style="position:absolute;font-size:60px;z-index:6">🚕</div>
 <div style="position:absolute;left:20px;right:20px;top:20px;background:#111;color:#fff;border-radius:22px;padding:14px 20px;font-size:24px;font-weight:800;z-index:7;max-width:330px">
  🚕 Лали едет за тобой<div style="font-size:40px;color:#ffcc00" id="eta2">5 мин</div></div>
 <div id="sos2" class="pill" style="left:330px;top:300px;background:#ff3b30;color:#fff;font-size:30px">🆘 забери!!</div>
</div>
<div class="card" id="c3" style="background:#1c1c1e">
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#2c2c2e;border-radius:26px;padding:18px 22px;display:flex;align-items:center;gap:18px;z-index:6">
  <div style="width:96px;height:96px;border-radius:50%;background:#48484a;display:flex;align-items:center;justify-content:center;font-size:58px">🤓</div>
  <div style="font-size:32px;font-weight:900">её парень<div style="font-size:22px;color:#8e8e93;font-weight:600">рейтинг: <span id="rk3" class="mono" style="color:#ff453a">10/10</span></div></div></div>
 <div id="stp3" style="position:absolute;left:330px;top:120px;border:7px solid #ff3b30;color:#ff3b30;border-radius:16px;padding:2px 18px;font-size:58px;font-weight:900;opacity:0;z-index:8">ЛОХ</div>
 <div class="ch" data-p="b"></div>
 <div id="t3_0" class="pill" style="background:#ff2d78;color:#fff">👠 ТОП</div><div id="t3_1" class="pill" style="background:#ff2d78;color:#fff">👠 ТОП</div><div id="t3_2" class="pill" style="background:#ff2d78;color:#fff">👠 ТОП</div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#5aa8e8,#9fd3ff 70%,#3a3a44 70%)">
 <div class="hdr" style="color:#0b2a4a">Батут-центр</div><div class="ttl" style="color:#0b2a4a">прыжки: <span id="hc4" class="mono">0</span></div>
 <div style="position:absolute;left:110px;top:560px;width:380px;height:40px;border-radius:50%;background:#111;box-shadow:0 0 0 10px #2d6cdf inset"></div>
 <div class="ch" data-p="c"></div>
 <div id="h4_0" class="pill" style="background:#ffd60a;color:#111">ХОП</div><div id="h4_1" class="pill" style="background:#ffd60a;color:#111">ХОП</div><div id="h4_2" class="pill" style="background:#ffd60a;color:#111">ХОП</div>
</div>
<div class="card" id="c5" style="background:#0a0612">
 <div id="fl5" style="position:absolute;left:0;right:0;bottom:0;height:300px;display:grid;grid-template-columns:repeat(6,1fr);transform:perspective(500px) rotateX(55deg);transform-origin:50% 100%"></div>
 <div id="ball5" style="position:absolute;left:250px;top:30px;font-size:100px">🪩</div>
 <div id="bm5" style="position:absolute;inset:0;pointer-events:none"></div>
 <div class="ch" data-p="d"></div>
 <div id="o5_0" class="pill" style="background:#bf5af2;color:#fff">ОП</div><div id="o5_1" class="pill" style="background:#bf5af2;color:#fff">ОП</div><div id="o5_2" class="pill" style="background:#bf5af2;color:#fff">ОП</div>
</div>
<div class="card" id="c6" style="background:#0e1621">
 <div style="position:absolute;left:0;right:0;top:0;height:86px;background:#17212b;display:flex;align-items:center;gap:16px;padding:0 26px;font-size:26px;font-weight:800">
  <div style="width:54px;height:54px;border-radius:50%;background:linear-gradient(135deg,#ff8ac4,#ff2d78);display:flex;align-items:center;justify-content:center;font-size:30px">👧</div>Она 💔</div>
 <div class="msg" id="q6" style="right:24px;top:116px;background:#2b5278">он же лох 🤡 бросай его</div>
 <div class="msg" id="k6_0" style="left:24px;top:196px;background:#182533">ок</div>
 <div class="msg" id="k6_1" style="left:24px;top:262px;background:#182533">ок</div>
 <div class="msg" id="k6_2" style="left:24px;top:328px;background:#182533">ок ❤️ люблю его</div>
 <div class="ch" data-p="e"></div>
 <div id="br6" style="position:absolute;left:380px;top:430px;font-size:110px;opacity:0;z-index:7">💔</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 let w='';for(let i=0;i<30;i++)w+=`<i id="w1_${i}" style="display:block;width:5px;border-radius:3px;background:#64b5ef"></i>`;$('wf1').innerHTML=w;
 let f='';for(let i=0;i<24;i++)f+=`<div id="f5_${i}" style="border:1px solid rgba(255,255,255,.1)"></div>`;$('fl5').innerHTML=f;
 let b='';for(let i=0;i<4;i++)b+=`<div id="b5_${i}" style="position:absolute;left:300px;top:90px;width:16px;height:700px;transform-origin:8px 0;background:linear-gradient(180deg,rgba(255,255,255,.5),transparent)"></div>`;$('bm5').innerHTML=b;
})();
const popPill=(id,t,s,x,y)=>{const e=$(id);const p=eb(seg(t,s,s+.18));e.style.opacity=t>=s?1:0;e.style.left=x+'px';e.style.top=y+'px';e.style.transform=`scale(${p}) rotate(${(rnd(s)-.5)*16}deg)`;};
'''
RENDER='''
 {// c1: голосовое + сообщение
  const pl=seg(t,7.3,10);for(let i=0;i<30;i++){const e=$('w1_'+i);const on=i/30<pl;e.style.height=(8+Math.abs(Math.sin(i*1.7+rnd(i)*3))*36*(on?1+.25*Math.sin(t*14+i):1))+'px';e.style.background=on?'#64b5ef':'#3d5266';}
  $('tm1').textContent='0:0'+Math.max(0,Math.ceil(7-pl*7));$('st1').style.opacity=t<9.6?.6+.4*Math.sin(t*8):0;
  $('m1').style.opacity=seg(t,9.6,9.75);$('m1').style.transform=`scale(${eb(seg(t,9.6,9.85))})`;
  $('r1').style.opacity=seg(t,9.85,9.95);
  place('a',140,670,1.0,false);pose('a',t<9.6?{aL:8,aR:166,hd:-6}:{aL:8,aR:-150+Math.sin(t*12)*20,open:1});}
 {// c2: такси едет по маршруту
  const p=eo(seg(t,10.0,12.7));$('rt2').setAttribute('stroke-dashoffset',1120*(1-p));
  const pts=[[60,640],[60,470],[420,470],[420,200],[540,200],[540,90]];let L=[0];for(let i=1;i<pts.length;i++)L.push(L[i-1]+Math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]));
  const d=p*L[L.length-1];let k=1;while(k<pts.length-1&&L[k]<d)k++;const q=(d-L[k-1])/(L[k]-L[k-1]);
  $('car2').style.left=(lerp(pts[k-1][0],pts[k][0],q)-30)+'px';$('car2').style.top=(lerp(pts[k-1][1],pts[k][1],q)-40)+'px';
  $('car2').style.transform=`scaleX(${pts[k][0]<pts[k-1][0]?1:-1})`;
  $('eta2').textContent=Math.max(1,Math.ceil(5*(1-p)))+' мин';popPill('sos2',t,10.56,330,300);$('sos2').style.transform+=` translateX(${Math.sin(t*50)*4*pop(t,10.56,3)}px)`;}
 {// c3: рейтинг парня падает, штамп ЛОХ, три ТОП
  const r=Math.round(lerp(10,0,eo(seg(t,13.0,13.98))));$('rk3').textContent=r+'/10';
  const sp=seg(t,13.98,14.1);$('stp3').style.opacity=sp;$('stp3').style.transform=`rotate(-14deg) scale(${lerp(2.4,1,eo(sp))})`;shake('c3',t,13.98,8);
  [15.7,16.0,16.48].forEach((s,i)=>popPill('t3_'+i,t,s,[40,370,60][i],[200,240,330][i]));
  place('b',300,680,1.15,false);pose('b',t<15.6?{aL:55,aR:-55,hd:12,open:1}:{aL:150,aR:-150,open:1,bob:-Math.abs(Math.sin(t*10))*14});}
 {// c4: батут, три прыжка
  const J=[19.04,19.5,19.92];let h=0,n=0;J.forEach((s,i)=>{if(t>=s){n=i+1;const x=(t-s)/.42;if(x<1)h=Math.sin(x*Math.PI)*170;}});
  if(t<J[0])h=Math.abs(Math.sin((t-16.75)*6))*25;$('hc4').textContent=n;
  place('c',300,570-h,1.1,false);pose('c',h>40?{aL:150,aR:-150,lL:-20,lR:20,open:1}:{aL:20,aR:-20,lL:8,lR:-8});
  J.forEach((s,i)=>popPill('h4_'+i,t,s,[60,380,220][i],[230,200,150][i]));}
 {// c5: дискотека
  for(let i=0;i<24;i++){$('f5_'+i).style.background=`hsla(${(i*47+t*200)%360},90%,55%,${.25+.5*Math.max(0,Math.sin(t*8+i))})`;}
  $('ball5').style.transform=`rotate(${t*90}deg)`;for(let i=0;i<4;i++)$('b5_'+i).style.transform=`rotate(${Math.sin(t*1.5+i*1.6)*50}deg)`;
  place('d',300,660,1.2,false);const q=Math.sin(t*12);pose('d',{aL:lerp(20,150,(q+1)/2),aR:-lerp(20,150,(1-q)/2),lL:q*14,lR:-q*14,bob:-Math.abs(q)*12,hd:q*8,open:1});
  $('ch_d').style.transform+=` rotate(${q*6}deg)`;[22.58,22.92,23.26].forEach((s,i)=>popPill('o5_'+i,t,s,[60,380,220][i],[180,220,120][i]));}
 {// c6: «ок ок ок» и разбитое сердце
  $('q6').style.opacity=seg(t,24.26,24.4);[25.98,26.28,26.68].forEach((s,i)=>{const e=$('k6_'+i);e.style.opacity=seg(t,s,s+.08);e.style.transform=`scale(${eb(seg(t,s,s+.2))})`;});
  place('e',150,700,1.0,false);pose('e',t<25.98?{aL:8,aR:166,hd:-6}:{aL:8,aR:145,hd:12});
  const bp=seg(t,26.68,26.85);$('br6').style.opacity=bp;$('br6').style.transform=`scale(${eb(bp)*1.2})`;}
'''
