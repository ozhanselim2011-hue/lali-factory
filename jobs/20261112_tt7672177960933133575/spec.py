DUR=16.7
FADE=16.3
START=20.6
SONG='Полка & YASMI — Омут'
BG='linear-gradient(180deg,#140606,#050202)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Помни,",20.76],["черти",21.24],["кругом",21.66],["водят",22.16],["нас",22.58]],
 [["я",22.84],["прошу,",23.38],["останься",23.92],["в",24.5],["этот",24.7],["раз",24.96]],
 [["ты",25.28],["ведь",25.72],["любишь,",26.0],["значит,",26.52],["дашь",26.9],["мне",27.28],["шанс",27.4]],
 [["ты",27.72],["мой",28.16],["талисман…",28.38]],
 [["помни,",30.16],["черти",30.86],["кругом",31.28],["водят",31.78],["нас",32.22]],
 [["я",32.48],["прошу,",32.98],["останься",33.56],["в",34.22],["этот",34.32],["раз",34.58]],
 [["ты",34.9],["ведь",35.34],["любишь,",35.64],["значит,",36.16],["дашь",36.58],["мне",36.9],["шанс",37.1]],
]
SC=[[20.3,22.8],[22.8,25.22],[25.22,27.66],[27.66,30.1],[30.1,32.42],[32.42,34.84],[34.84,99]]
GLOW=['#7a1f1f','#1a4a7a','#5a5a1a','#1a5c2e','#3a1a5a','#5a3a1a','#7a1f4a']
PEMO=['😈','🚕','🎮','🍀','🌀','🧳','💬']
END=[36.9,37.3]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:radial-gradient(circle at 50% 60%,#3a0a0a,#0a0202)">
 <div id="dv1" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="a"></div><div class="ch" data-p="b"></div>
</div>
<div class="card" id="c2" style="background:#ffd60a;color:#111">
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#fff;border-radius:22px;padding:14px 18px;font-size:26px;font-weight:900;z-index:6">🚕 Она: поездка «от тебя» <div id="cn2" style="font-size:24px;color:#d0021b;opacity:0">❌ поездка отменена</div></div>
 <div class="ch" data-p="c"></div><div class="ch" data-p="d"></div>
</div>
<div class="card" id="c3" style="background:#000">
 <div class="c" style="top:90px;font-size:56px;font-weight:900;color:#ff453a;font-family:'JetBrains Mono'">GAME OVER?</div>
 <div class="c" style="top:190px;font-size:34px;font-weight:900;color:#fff;font-family:'JetBrains Mono'">CONTINUE?</div>
 <div id="ys3" class="c" style="top:260px;font-size:44px;font-weight:900;color:#30d158;font-family:'JetBrains Mono'">▶ YES</div>
 <div id="hp3" class="c" style="top:340px;font-size:40px;opacity:0">❤️ +1 шанс</div>
 <div class="ch" data-p="e"></div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#d8f5d0,#7acb6a)">
 <div id="am4" style="position:absolute;left:200px;top:110px;width:200px;height:200px;border-radius:50%;background:#c9a227;border:10px solid #8a6a10;display:flex;align-items:center;justify-content:center;font-size:100px">🍀</div>
 <div class="c" style="top:330px;font-size:30px;font-weight:900;color:#1a4a10">удача: <span id="lk4" class="mono">0</span>%</div>
 <div class="ch" data-p="f"></div>
</div>
<div class="card" id="c5" style="background:#05050f">
 <div id="wp5" style="position:absolute;left:100px;top:120px;width:400px;height:400px;border-radius:50%;background:repeating-conic-gradient(#1a2a6a 0 15deg,#3a1a5a 15deg 30deg)"></div>
 <div id="dv5" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="g"></div><div class="ch" data-p="h"></div>
</div>
<div class="card" id="c6" style="background:#f4ecd8;color:#2a1f10">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Её чемодан</div>
 <div id="sc6" style="position:absolute;left:330px;top:300px;font-size:150px">🧳</div>
 <div id="it6" style="position:absolute;inset:0;z-index:4"></div>
 <div class="ch" data-p="i"></div>
 <div id="st6" class="c" style="top:90px;font-size:32px;font-weight:900;color:#1f8a3a;opacity:0">✅ осталась</div>
</div>
<div class="card" id="c7" style="background:#000">
 <div class="hdr">Чат · она 💖</div>
 <div id="m7a" style="position:absolute;right:24px;top:90px;background:#0a84ff;border-radius:22px;padding:12px 18px;font-size:30px;font-weight:800;opacity:0">дашь мне шанс? 🥺</div>
 <div id="ty7" style="position:absolute;left:24px;top:180px;background:#2c2c2e;border-radius:22px;padding:12px 18px;font-size:30px;font-weight:800;opacity:0">печатает…</div>
 <div class="ch" data-p="j"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML='bdh'.includes(p)?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 const D=(id)=>{let s='';for(let i=0;i<6;i++)s+=`<div id="${id}_${i}" style="position:absolute;font-size:56px">😈</div>`;$(id).innerHTML=s;};D('dv1');D('dv5');
 let s='';['👗','👠','💄','🧸'].forEach((e,i)=>s+=`<div id="i6_${i}" style="position:absolute;font-size:56px;opacity:0">${e}</div>`);$('it6').innerHTML=s;})();
'''
RENDER='''
 {for(let i=0;i<6;i++){const a=t*2+i*Math.PI/3;const e=$('dv1_'+i);e.style.left=(275+Math.cos(a)*230)+'px';e.style.top=(400+Math.sin(a)*120)+'px';}place('a',240,690,.9,false);place('b',360,690,.9,true);pose('a',{aL:8,aR:-60,hd:Math.sin(t*4)*10});pose('b',{aL:8,aR:-60,hd:-Math.sin(t*4)*10});}
 {$('cn2').style.opacity=seg(t,24.96,25.06);const k=eo(seg(t,22.9,23.8));place('d',lerp(380,460,k),700,.95,true);pose('d',{aL:8,aR:-8,hd:-6});place('c',200,700,.95,false);pose('c',t>=23.38?{aL:150,aR:-150,open:1,bob:20}:{aL:8,aR:-60});}
 {$('ys3').style.opacity=Math.sin(t*10)>0?1:.4;$('hp3').style.opacity=seg(t,27.4,27.5);place('e',300,700,.9,false);pose('e',t>=27.4?{aL:150,aR:-150,open:1}:{aL:8,aR:-90});}
 {$('lk4').textContent=Math.round(eo(seg(t,28.2,29.6))*100);$('am4').style.transform=`rotate(${Math.sin(t*3)*10}deg) scale(${1+.05*Math.sin(t*6)})`;place('f',300,700,1.0,false);pose('f',{aL:8,aR:-120,hd:-6});}
 {$('wp5').style.transform=`rotate(${t*200}deg)`;for(let i=0;i<6;i++){const a=t*2.5+i*Math.PI/3;const e=$('dv5_'+i);e.style.left=(275+Math.cos(a)*240)+'px';e.style.top=(300+Math.sin(a)*240)+'px';}
  place('g',260,560,.7,false,Math.sin(t*4)*20);place('h',340,560,.7,true,-Math.sin(t*4)*20);pose('g',{aL:60,aR:-60,open:1});pose('h',{aL:60,aR:-60,open:1});}
 {for(let i=0;i<4;i++){const k=eo(seg(t,32.6+i*.35,33.0+i*.35));const e=$('i6_'+i);e.style.opacity=k>0?1:0;e.style.left=lerp(380,40+i*130,k)+'px';e.style.top=lerp(340,160,k)+'px';}$('st6').style.opacity=seg(t,34.58,34.7);
  place('i',160,700,.95,false);pose('i',t>=34.58?{aL:150,aR:-150,open:1}:{aL:8,aR:-90});}
 {$('m7a').style.opacity=seg(t,35.0,35.1);$('ty7').style.opacity=seg(t,36.2,36.3);$('ty7').textContent=t<37.1?'печатает…':'да 💖';place('j',300,700,1.0,false);pose('j',t>=37.1?{aL:150,aR:-150,open:1}:{aL:8,aR:-100,hd:-8});}
'''
