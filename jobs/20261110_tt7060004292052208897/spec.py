DUR=22.6
FADE=22.2
START=31.8
SONG='SEVENROSE — Чёрная смородина'
BG='linear-gradient(180deg,#0a0614,#030206)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Расцвела",32.04],["смородина",33.44]],
 [["в",34.68],["городском",35.18],["саду",36.84]],
 [["чувства",39.94],["я",41.34],["не",41.62],["скрою,",41.84]],
 [["мимо",42.64],["не",44.68],["пройду",45.28]],
 [["нежные",48.0],["слова",49.4],["любви",49.84]],
 [["под",50.88],["хмельным",52.2],["дождём",53.26]],
]
SC=[[31.5,34.6],[34.6,39.85],[39.85,42.58],[42.58,47.9],[47.9,50.8],[50.8,99]]
GLOW=['#2a1a4a','#1a5c2e','#7a1f4a','#1a4a7a','#7a1f4a','#3a3a6a']
PEMO=['🫐','🌳','💖','🧭','💌','☔']
END=[54.0,54.4]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#d8f0ff,#a8e0a0)">
 <div class="hdr" style="color:rgba(0,0,0,.5)">Куст «Смородина» · рост</div>
 <div style="position:absolute;left:150px;top:200px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,#4caf50,#2e7d32)"></div>
 <div id="br1" style="position:absolute;inset:0;z-index:3"></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#d8e6d0">
 <svg width="600" height="690" style="position:absolute"><path d="M0 250 L600 300 M0 520 L600 450 M200 0 L240 690 M430 0 L400 690" stroke="#fff" stroke-width="20"/></svg>
 <div style="position:absolute;left:250px;top:300px;width:150px;height:130px;border-radius:30px;background:#6cbf5a;display:flex;align-items:center;justify-content:center;font-size:60px">🌳🫐</div>
 <div id="pn2" style="position:absolute;left:290px;top:250px;font-size:60px;z-index:6">📍</div>
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#fff;color:#111;border-radius:22px;padding:12px 18px;font-size:24px;font-weight:800;z-index:7">🌳 Городской сад · <span style="color:#0a84ff">вы здесь</span></div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#1c1c1e">
 <div class="hdr">Скрыть чувства?</div>
 <div style="position:absolute;left:40px;right:40px;top:100px;display:flex;justify-content:space-between;align-items:center;background:#2c2c2e;border-radius:20px;padding:16px 20px;font-size:28px;font-weight:800">Режим «скромный»<div style="width:90px;height:52px;border-radius:26px;background:#3a3a3c;position:relative"><div id="tg3" style="position:absolute;top:4px;left:42px;width:44px;height:44px;border-radius:50%;background:#fff"></div></div></div>
 <div id="hr3" class="c" style="top:220px;font-size:130px;opacity:0;z-index:6">💖</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:#e8eef4;color:#111">
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#0a84ff;color:#fff;border-radius:22px;padding:14px 18px;font-size:26px;font-weight:800;z-index:6" id="nv4">➡️ Проехать мимо</div>
 <svg width="600" height="690" style="position:absolute"><path id="rt4" d="M300 650 L300 300 L560 300" stroke="#0a84ff" stroke-width="14" fill="none"/></svg>
 <div style="position:absolute;left:40px;top:250px;font-size:70px">🏡</div><div style="position:absolute;left:40px;top:180px;background:#ff2d78;color:#fff;border-radius:12px;padding:4px 10px;font-size:20px;font-weight:900">она</div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c5" style="background:#000">
 <div class="hdr">Чат · она 💖</div>
 <div id="cm5" style="position:absolute;left:24px;right:24px;top:80px"></div>
 <div class="ch" data-p="e"></div>
</div>
<div class="card" id="c6" style="background:linear-gradient(180deg,#3a4a6a,#1a2030)">
 <div id="rn6" style="position:absolute;inset:0"></div>
 <div style="position:absolute;left:180px;top:270px;font-size:200px;z-index:4">☂️</div>
 <div class="ch" data-p="f"></div><div class="ch" data-p="g"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=p=='g'?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 let b='';for(let i=0;i<16;i++){const a=i*2.4,r=40+(i%4)*28;b+=`<div id="b1_${i}" style="position:absolute;left:${290+Math.cos(a)*r}px;top:${340+Math.sin(a)*r}px;width:22px;height:22px;border-radius:50%;background:#1a1030;box-shadow:inset -4px -4px 0 #3a2a60;opacity:0"></div>`;}$('br1').innerHTML=b;
 $('cm5').innerHTML=['ты как ягодка 🫐','самая нежная 🥺','скучаю каждую минуту'].map((s,i)=>`<div id="m5_${i}" style="margin-left:auto;width:fit-content;background:#0a84ff;border-radius:22px;padding:12px 18px;font-size:28px;font-weight:800;margin-bottom:12px;opacity:0">${s}</div>`).join('');
 let r='';for(let i=0;i<24;i++)r+=`<div id="r6_${i}" style="position:absolute;font-size:${18+i%3*8}px">${i%3?'💧':'💖'}</div>`;$('rn6').innerHTML=r;})();
'''
RENDER='''
 {for(let i=0;i<16;i++){const s=32.1+i*.15;$('b1_'+i).style.opacity=seg(t,s,s+.1);$('b1_'+i).style.transform=`scale(${eb(seg(t,s,s+.3))})`;}place('a',130,690,.9,false);pose('a',t>=33.44?{aL:60,aR:-60,open:1}:{aL:8,aR:-60});}
 {$('pn2').style.transform=`translateY(${-Math.abs(Math.sin(t*4))*20}px)`;const k=eo(seg(t,34.7,36.8));place('b',lerp(80,240,k),lerp(680,560,k),.7,false);pose('b',k<1?walk(t,10):{aL:8,aR:-120,open:1});}
 {const on=t>=41.84;$('tg3').style.left=on?'4px':'42px';$('tg3').parentNode.style.background=on?'#3a3a3c':'#30d158';$('hr3').style.opacity=seg(t,41.84,41.95);$('hr3').style.transform=`scale(${1+.15*Math.sin(t*8)})`;
  place('c',300,700,1.0,false);pose('c',on?{aL:150,aR:-150,open:1}:{aL:8,aR:-8,hd:-8});}
 {const tr=t>=44.68;$('nv4').textContent=tr?'↩️ Разворот: к ней 💖':'➡️ Проехать мимо';$('nv4').style.background=tr?'#ff2d78':'#0a84ff';
  $('rt4').setAttribute('d',tr?'M300 650 L300 300 L110 300':'M300 650 L300 300 L560 300');const k=eo(seg(t,45.28,47.8));place('d',tr?lerp(300,170,k):300,tr?lerp(560,420,k):560,.7,tr);pose('d',walk(t,10));}
 {for(let i=0;i<3;i++){const s=[48.2,49.4,49.84][i];$('m5_'+i).style.opacity=seg(t,s,s+.1);$('m5_'+i).style.transform=`scale(${eb(seg(t,s,s+.25))})`;}place('e',150,700,.9,false);pose('e',{aL:8,aR:-100,hd:-8});}
 {for(let i=0;i<24;i++){const ph=(t*.8+rnd(i))%1;$('r6_'+i).style.left=(rnd(i+3)*580)+'px';$('r6_'+i).style.top=(-30+ph*720)+'px';}
  place('f',240,700,1.0,false);place('g',360,700,1.0,true);pose('f',{aL:8,aR:-150,hd:8});pose('g',{aL:8,aR:-60,hd:8});}
'''
