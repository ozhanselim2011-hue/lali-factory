DUR=22.0
FADE=21.6
START=37.0
SONG='ENZRO — Я буду рядом'
BG='linear-gradient(180deg,#0a0e1a,#030408)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Я",37.36],["буду",38.76],["рядом,",40.16]],
 [["даже",40.98],["когда",41.44],["темнота",41.94]],
 [["окутает",44.46],["наш",45.64],["дом,",46.64]],
 [["и",47.2],["мир",48.14],["весь",48.52],["будет",48.92],["против",49.4],["тебя",50.66]],
 [["я",55.4],["буду",56.8],["рядом",58.04]],
]
SC=[[36.7,40.9],[40.9,47.1],[47.1,55.3],[55.3,99]]
GLOW=['#1d3a5a','#1a1a3a','#5a1d1d','#7a4a1a']
PEMO=['📍','🔦','🛡️','🌅']
END=[58.6,59.0]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#e8eef4;color:#111">
 <div style="position:absolute;inset:0;background-image:linear-gradient(#d0d8e0 2px,transparent 2px),linear-gradient(90deg,#d0d8e0 2px,transparent 2px);background-size:80px 80px"></div>
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#fff;border-radius:22px;padding:14px 18px;font:900 26px Inter;box-shadow:0 6px 16px rgba(0,0,0,.1)">📍 Локатор · <span style="color:#ff2d78">она</span><span id="ds1" style="float:right;color:#0a84ff">2 км</span></div>
 <div class="ch" data-p="g"></div><div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#1a2a4a,#0a1020)">
 <div style="position:absolute;left:150px;top:200px;width:300px;height:220px;background:#8a5a32"></div>
 <div style="position:absolute;left:120px;top:110px;width:0;height:0;border-left:180px solid transparent;border-right:180px solid transparent;border-bottom:100px solid #5a3a1a"></div>
 <div id="w2a" style="position:absolute;left:190px;top:250px;width:70px;height:70px;background:#ffd60a"></div><div id="w2b" style="position:absolute;left:340px;top:250px;width:70px;height:70px;background:#ffd60a"></div>
 <div id="dk2" style="position:absolute;inset:0;background:radial-gradient(circle at var(--x,50%) 70%,rgba(0,0,0,0) 0,rgba(0,0,0,0) var(--r,0px),rgba(0,0,10,.92) calc(var(--r,0px) + 60px));opacity:0;z-index:4"></div>
 <div class="ch" data-p="b"></div><div class="ch" data-p="g2"></div>
</div>
<div class="card" id="c3" style="background:#2a1a1a">
 <div id="cr3" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="g3"></div><div class="ch" data-p="c"></div>
 <div id="sh3" style="position:absolute;left:345px;top:430px;width:150px;height:200px;border:8px solid #64d2ff;border-radius:20px 20px 75px 75px;opacity:0;z-index:6;box-shadow:0 0 30px #64d2ff"></div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#ff9f43,#ffd6a0 60%,#3a2a1a 60%)">
 <div id="sn4" style="position:absolute;left:220px;top:250px;width:160px;height:160px;border-radius:50%;background:#ffd60a;box-shadow:0 0 80px #ffb000"></div>
 <div class="ch" data-p="d"></div><div class="ch" data-p="g4"></div>
 <div id="hh4" style="position:absolute;inset:0;z-index:6"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...(p.startsWith('g')?['#ff2d78','#ff8ac4','#ff2d78']:['#111','#64d2ff','#0a84ff']));});})();'''
RENDER='''
 {const k=eo(seg(t,37.36,40.16));place('g',380,690,.95,true);pose('g',{aL:8,aR:-8});place('a',lerp(-100,250,k),690,.95,false);pose('a',k<1?walk(t,8):{aL:8,aR:-60,open:1});const d=lerp(2000,0,k);$('ds1').textContent=d<1?'рядом · 0 м':(d>=1000?(d/1000).toFixed(1)+' км':Math.round(d)+' м');}
 {const dk=seg(t,40.98,41.94);$('dk2').style.opacity=dk;$('dk2').style.setProperty('--r',(t>=44.46?lerp(0,140,seg(t,44.46,45.0)):0)+'px');$('dk2').style.setProperty('--x','50%');$('w2a').style.background=t>=41.44?'#222':'#ffd60a';$('w2b').style.background=t>=41.94?'#222':'#ffd60a';
  place('b',260,690,.85,false);pose('b',{aL:8,aR:t>=44.46?-120:-8,hd:-6});place('g2',360,690,.85,true);pose('g2',{aL:8,aR:-8,hd:t>=44.46?6:0});}
 {let c='';const n=Math.floor(lerp(0,12,seg(t,47.2,50.66)));for(let i=0;i<n;i++){const x=20+(i%6)*95,y=i<6?40:150;c+=`<div style="position:absolute;left:${x}px;top:${y}px;transform:rotate(${Math.sin(t*6+i)*6}deg)"><div style="width:56px;height:56px;border-radius:50%;background:#555"></div><div style="width:80px;height:90px;margin-left:-12px;border-radius:40px 40px 0 0;background:#555"></div><div style="position:absolute;left:20px;top:60px;font:900 32px Inter;color:#ff453a">👉</div></div>`}$('cr3').innerHTML=c;
  place('g3',420,690,.85,true);pose('g3',{aL:30,aR:-30,hd:20});place('c',220,690,1.0,false);pose('c',t>=49.4?{aL:100,aR:-100,open:1}:{aL:8,aR:-8});$('sh3').style.opacity=seg(t,50.66,50.8);$('sh3').style.transform=`scale(${1+.1*pop(t,50.66,6)})`;}
 {const k=eo(seg(t,55.4,58.04));$('sn4').style.top=lerp(380,180,k)+'px';place('d',lerp(180,260,k),690,1.0,false);place('g4',lerp(420,340,k),690,1.0,true);const hug={aL:lerp(8,110,k),aR:-lerp(8,110,k),open:t>=58.04};pose('d',hug);pose('g4',hug);
  let h='';for(let i=0;i<10;i++){const s=56+i*.18;if(t>=s){const p=(t-s)/1.4;h+=`<div style="position:absolute;left:${200+rnd(i)*200}px;top:${300-p*260}px;font-size:${28+rnd(i+2)*24}px;opacity:${1-p}">💗</div>`}}$('hh4').innerHTML=h;}
'''
