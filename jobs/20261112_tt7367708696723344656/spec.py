DUR=15.8
FADE=15.4
START=32.0
SONG='XOLIDAYBOY — Пожары'
BG='linear-gradient(180deg,#160806,#050202)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["С",32.14],["ума",32.62],["мы",33.04],["сошли,",33.24],["в",34.02],["голове",34.3],["иллюстрации",35.0]],
 [["как",36.32],["мы",36.68],["полетим?",36.86],["Мне",37.88],["нужна",38.24],["гравитация",38.72]],
 [["пожары",43.84],["любви —",44.8],["это",45.8],["эвакуация",46.28]],
]
SC=[[31.7,36.25],[36.25,40.1],[40.1,43.78],[43.78,99]]
GLOW=['#5a1d7a','#1a2a6a','#7a2a0a','#1a5c2e']
PEMO=['🌀','🚀','🔥','🚨']
END=[47.4,47.8]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#f4ecd8">
 <div id="dr1" style="position:absolute;inset:0;z-index:4"></div>
 <div class="ch" data-p="a"></div><div class="ch" data-p="b"></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#02031a,#1a2a6a)">
 <div id="st2" style="position:absolute;inset:0"></div>
 <div class="c mono" id="gv2" style="top:40px;font-size:40px;font-weight:900;color:#64d2ff;z-index:6">гравитация: 1.0 g</div>
 <div class="ch" data-p="c"></div><div class="ch" data-p="d"></div>
</div>
<div class="card" id="c3" style="background:#1c1c1e">
 <div class="c" style="top:80px;font-size:150px" id="ht3">💖</div>
 <div id="fi3" style="position:absolute;inset:0;z-index:5"></div>
 <div class="c mono" id="tp3" style="top:330px;font-size:44px;font-weight:900;color:#ff9f0a;z-index:6">36.6°</div>
</div>
<div class="card" id="c4" style="background:#0f3a1f">
 <div style="position:absolute;left:60px;right:60px;top:60px;height:180px;border-radius:20px;background:#30d158;display:flex;align-items:center;justify-content:center;gap:20px;font-size:90px">🏃<span style="font-size:60px;color:#fff;font-weight:900">ВЫХОД</span></div>
 <div id="al4" style="position:absolute;inset:0;background:#ff0000;opacity:0"></div>
 <div id="fi4" style="position:absolute;inset:0;z-index:3"></div>
 <div class="ch" data-p="e"></div><div class="ch" data-p="f"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML='bdf'.includes(p)?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 let d='';['💭','🎨','🦄','🌈','💫','🎠','🪐','🖍️'].forEach((e,i)=>d+=`<div id="d1_${i}" style="position:absolute;font-size:56px;opacity:0">${e}</div>`);$('dr1').innerHTML=d;
 let s='';for(let i=0;i<30;i++)s+=`<div style="position:absolute;left:${rnd(i)*590}px;top:${rnd(i+9)*680}px;width:3px;height:3px;border-radius:50%;background:#fff"></div>`;$('st2').innerHTML=s;
 const F=(id,n)=>{let f='';for(let i=0;i<n;i++)f+=`<div id="${id}_${i}" style="position:absolute;font-size:${40+rnd(i)*40}px">🔥</div>`;$(id).innerHTML=f;};F('fi3',12);F('fi4',10);})();
'''
RENDER='''
 {for(let i=0;i<8;i++){const a=t*1.5+i*Math.PI/4;const e=$('d1_'+i);e.style.opacity=seg(t,34.3+i*.08,34.5+i*.08);e.style.left=(275+Math.cos(a)*200)+'px';e.style.top=(260+Math.sin(a)*130)+'px';}
  place('a',240,700,1.0,false,Math.sin(t*3)*8);place('b',360,700,1.0,true,-Math.sin(t*3)*8);pose('a',{aL:60,aR:-60,hd:Math.sin(t*5)*14,open:1});pose('b',{aL:60,aR:-60,hd:-Math.sin(t*5)*14,open:1});}
 {const k=eo(seg(t,36.86,38.7));$('gv2').textContent='гравитация: '+(1-k).toFixed(1)+' g';place('c',240,lerp(700,360,k)+Math.sin(t*3)*12,1.0,false,k*20);place('d',360,lerp(700,380,k)+Math.cos(t*3)*12,1.0,true,-k*20);pose('c',{aL:120,aR:-120,open:1});pose('d',{aL:120,aR:-120,open:1});}
 {const k=seg(t,40.2,43.6);$('tp3').textContent=Math.round(lerp(36.6,1000,k))+'°';$('ht3').style.transform=`scale(${1+k*.4+.05*Math.sin(t*12)})`;for(let i=0;i<12;i++){const ph=(t*.9+rnd(i))%1;const e=$('fi3_'+i);e.style.left=(rnd(i+2)*560)+'px';e.style.top=(640-ph*(200+k*350))+'px';e.style.opacity=(1-ph)*k;}}
 {$('al4').style.opacity=.25*Math.abs(Math.sin(t*8));for(let i=0;i<10;i++){const e=$('fi4_'+i);e.style.left=(rnd(i)*560)+'px';e.style.top=(560+Math.sin(t*8+i)*20)+'px';}
  const k=eo(seg(t,44.0,47.0));place('e',lerp(150,230,k),lerp(700,480,k),lerp(1,.6,k),false);place('f',lerp(300,370,k),lerp(700,480,k),lerp(1,.6,k),true);pose('e',run(t,14));pose('f',run(t,14));}
'''
