DUR=13.2
FADE=12.8
START=21.2
SONG='Settlers — Светлое чувство'
BG='linear-gradient(180deg,#141008,#050403)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Самое-самое",21.44],["светлое",23.56],["чувство",24.34]],
 [["самое-самое",25.22],["светлое",27.18],["чувство",28.04]],
 [["ты",29.02],["как",29.52],["искусство,",29.76],["ты",30.78],["как",31.26],["искусство",31.6]],
 [["ты",32.64],["яркий",33.06],["свет",33.78]],
]
SC=[[20.9,25.15],[25.15,28.95],[28.95,32.58],[32.58,99]]
GLOW=['#7a6a1a','#7a5a1a','#5a1d7a','#7a7a2a']
PEMO=['💡','☀️','🖼️','✨']
END=[34.0,34.4]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#0a0a0c">
 <div class="hdr" style="color:#ffd60a">Яркость чувства</div>
 <div style="position:absolute;left:40px;right:40px;top:100px;height:30px;border-radius:15px;background:#2c2c2e;overflow:hidden"><div id="sl1" style="height:30px;background:linear-gradient(90deg,#ffb340,#fff7c2);width:10%"></div></div>
 <div class="c mono" id="pc1" style="top:150px;font-size:44px;font-weight:900;color:#ffd60a">10%</div>
 <div id="gl1" style="position:absolute;inset:0;background:radial-gradient(circle at 50% 70%,rgba(255,230,150,.7),transparent 60%);opacity:0"></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#87ceeb">
 <div id="sn2" style="position:absolute;left:200px;top:600px;font-size:200px">☀️</div>
 <div class="c" id="tx2" style="top:40px;font-size:30px;font-weight:900;color:#3a2a00;opacity:0">рассвет внутри 🌅</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#f4ecd8;color:#2a1f10">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Музей · главный зал</div>
 <div style="position:absolute;left:150px;top:90px;width:300px;height:360px;border:20px solid #c9a227;box-shadow:inset 0 0 0 6px #8a6a10,0 10px 30px rgba(0,0,0,.4);background:linear-gradient(135deg,#ffd6e8,#ff8ac4);display:flex;align-items:center;justify-content:center;font-size:170px">👩</div>
 <div id="lb3" style="position:absolute;left:180px;top:480px;background:#fff;border-radius:8px;padding:6px 12px;font-size:20px;font-weight:800;opacity:0">«Ты» · бесценно</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:#000">
 <div id="fl4" style="position:absolute;inset:0;background:radial-gradient(circle at 50% 45%,#fffbe0,#ffd60a 30%,transparent 70%);opacity:0"></div>
 <div id="sp4" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="d"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 let s='';for(let i=0;i<16;i++)s+=`<div id="s4_${i}" style="position:absolute;font-size:${24+i%3*12}px">✨</div>`;$('sp4').innerHTML=s;})();
'''
RENDER='''
 {const k=eo(seg(t,22.68,24.6));const v=Math.round(lerp(10,100,k));$('sl1').style.width=v+'%';$('pc1').textContent=v+'%';$('gl1').style.opacity=k;place('a',300,700,1.0,false);pose('a',k>.9?{aL:120,aR:-120,open:1}:{aL:8,aR:-8});
  $('ch_a').style.filter=`drop-shadow(0 0 ${k*40}px #ffd60a)`;}
 {const k=eo(seg(t,25.3,28.0));$('sn2').style.top=lerp(600,90,k)+'px';$('c2').style.background=`linear-gradient(180deg,${k>.5?'#87ceeb':'#2a1a4a'},${k>.5?'#fff7c2':'#ff8a3d'})`;$('tx2').style.opacity=seg(t,28.04,28.15);
  place('b',300,700,1.0,false);pose('b',t>=28.04?{aL:150,aR:-150,open:1}:{aL:8,aR:-60,hd:-10});}
 {$('lb3').style.opacity=seg(t,31.6,31.7);place('c',480,700,.85,true);pose('c',t>=29.76?{aL:8,aR:-90,hd:-12,open:1}:{aL:8,aR:-8});}
 {const k=seg(t,33.06,33.9);$('fl4').style.opacity=k;place('d',300,700,1.1,false);pose('d',{aL:150,aR:-150,open:1});$('ch_d').style.filter=`drop-shadow(0 0 ${k*60}px #fff)`;
  for(let i=0;i<16;i++){const a=i*Math.PI/8+t;const r=120+k*150;$('s4_'+i).style.left=(285+Math.cos(a)*r)+'px';$('s4_'+i).style.top=(380+Math.sin(a)*r)+'px';$('s4_'+i).style.opacity=k;}}
'''
