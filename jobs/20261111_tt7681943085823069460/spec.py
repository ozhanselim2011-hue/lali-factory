DUR=14.4
FADE=14.0
START=31.4
SONG='Mary Gu & ЛСП — искра'
BG='linear-gradient(180deg,#160806,#050202)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Бензин",31.64],["из",33.32],["канистры",33.58],["влюблённых",34.54],["сердец",35.34]],
 [["и",36.44],["горят",36.48],["наши",37.26],["чувства",37.64],["огнём",38.52],["до",39.22],["небес",39.34]],
 [["звоните",40.1],["101,",40.62],["двое",41.34],["выжигают",43.42],["на",44.48],["танцполе",44.68]],
]
SC=[[31.1,36.4],[36.4,40.05],[40.05,99]]
GLOW=['#7a5a0a','#7a2a0a','#7a1f1f']
PEMO=['⛽','🔥','🚒']
END=[45.4,45.8]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr" style="color:#ffd60a">АЗС «Влюблённые сердца»</div>
 <div style="position:absolute;left:60px;top:120px;width:180px;height:360px;border-radius:20px;background:#ff2d78;display:flex;flex-direction:column;align-items:center;padding-top:20px;color:#fff;font-weight:900"><div style="font-size:26px">АИ-❤️</div><div id="lt1" class="mono" style="font-size:40px;margin-top:20px;background:#000;border-radius:10px;padding:6px 12px">0.0 л</div><div style="font-size:60px;margin-top:30px">⛽</div></div>
 <div style="position:absolute;left:300px;top:120px;width:240px;height:60px;border-radius:30px;background:#2c2c2e;overflow:hidden"><div id="fg1" style="height:60px;background:linear-gradient(90deg,#ff2d78,#ff9f0a);width:5%"></div></div>
 <div class="c" style="top:190px;left:300px;right:auto;width:240px;font-size:20px;color:#8e8e93;font-weight:700">бак чувств</div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#0a1030,#3a1030 60%,#7a2a0a)">
 <div id="fl2" style="position:absolute;inset:0"></div>
 <div class="c mono" id="al2" style="top:30px;font-size:36px;font-weight:900;color:#ff9f0a;z-index:6">высота пламени: 0 м</div>
 <div class="ch" data-p="b"></div><div class="ch" data-p="c"></div>
</div>
<div class="card" id="c3" style="background:#120414">
 <div id="dl3" style="position:absolute;left:24px;right:24px;top:24px;background:#1c1c1e;border-radius:20px;padding:12px 18px;font-size:28px;font-weight:900;z-index:7">📞 <span id="nm3" class="mono">…</span></div>
 <div id="df3" style="position:absolute;left:0;right:0;top:360px;height:330px;display:grid;grid-template-columns:repeat(6,1fr)"></div>
 <div id="ff3" style="position:absolute;inset:0;z-index:4"></div>
 <div class="ch" data-p="d"></div><div class="ch" data-p="e"></div>
 <div id="tr3" style="position:absolute;top:120px;font-size:110px;z-index:6">🚒</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML='ce'.includes(p)?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 let f='';for(let i=0;i<18;i++)f+=`<div id="f2_${i}" style="position:absolute;font-size:${40+rnd(i)*50}px">🔥</div>`;$('fl2').innerHTML=f;
 let d='';for(let i=0;i<36;i++)d+=`<div id="d3_${i}" style="border:1px solid #000"></div>`;$('df3').innerHTML=d;
 let g='';for(let i=0;i<10;i++)g+=`<div id="g3_${i}" style="position:absolute;font-size:${40+rnd(i)*30}px">🔥</div>`;$('ff3').innerHTML=g;})();
'''
RENDER='''
 {const k=eo(seg(t,33.3,35.6));$('lt1').textContent=(k*40).toFixed(1)+' л';$('fg1').style.width=(5+k*95)+'%';place('a',400,700,1.0,true);pose('a',{aL:8,aR:-90,hd:-6});}
 {const k=eo(seg(t,36.5,39.4));$('al2').textContent='высота пламени: '+fmt(k*10000)+' м';for(let i=0;i<18;i++){const ph=(t*.8+rnd(i))%1;const e=$('f2_'+i);e.style.left=(rnd(i+4)*560)+'px';e.style.top=(640-ph*(200+k*450))+'px';e.style.opacity=(1-ph)*(.4+k*.6);}
  place('b',240,700,1.0,false);place('c',360,700,1.0,true);pose('b',{aL:8,aR:-110,hd:-6});pose('c',{aL:8,aR:-110,hd:-6});}
 {const n='101';$('nm3').textContent=t<40.62?'набираю…':n+' · «двое горят на танцполе!»';
  for(let i=0;i<36;i++){const c=['#ff2d78','#64d2ff','#ffd60a','#30d158','#bf5af2'][(i+Math.floor(t*6))%5];$('d3_'+i).style.background=c;$('d3_'+i).style.opacity=.6;}
  const d=t>=41.34;place('d',230,690,.95,false);place('e',370,690,.95,true);pose('d',d?{aL:150*Math.sin(t*10),aR:-150*Math.cos(t*10),open:1,bob:-Math.abs(Math.sin(t*10))*12}:{aL:8,aR:-8});pose('e',d?{aL:150*Math.cos(t*10),aR:-150*Math.sin(t*10),open:1,bob:-Math.abs(Math.cos(t*10))*12}:{aL:8,aR:-8});
  for(let i=0;i<10;i++){const e=$('g3_'+i);e.style.opacity=t>=43.42?.6+.4*Math.abs(Math.sin(t*8+i)):0;e.style.left=(180+i*25)+'px';e.style.top=(560-Math.abs(Math.sin(t*6+i))*60)+'px';}
  $('tr3').style.left=lerp(620,400,eo(seg(t,44.4,45.6)))+'px';}
'''
