DUR=14.3
FADE=13.9
START=0
SONG='ARTIK & ASTI — Лампочки'
BG='linear-gradient(180deg,#120a14,#040306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Я",0.0],["помню,",0.58],["как",1.26],["мы",1.54],["висели",1.88]],
 [["под",2.5],["мои",2.96],["новые",3.34],["треки",3.98]],
 [["на",5.02],["твоей",5.26],["маленькой",5.9],["кухне",6.74]],
 [["цветные",7.32],["лампочки",8.06]],
 [["я",9.5],["помню,",9.92],["как",10.58],["же",10.88],["бесили",11.16]],
 [["твои",11.82],["несносные",12.62],["кошки",13.64]],
]
SC=[[-0.3,2.45],[2.45,4.95],[4.95,7.25],[7.25,9.45],[9.45,11.78],[11.78,99]]
GLOW=['#5a1d7a','#1a4a7a','#7a5a1a','#7a1f4a','#3a3a5a','#7a3a1a']
PEMO=['📷','🎧','🍳','💡','😤','🐈']
END=[13.9,14.3]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr">Воспоминания · 2 года назад</div>
 <div id="ph1" style="position:absolute;left:70px;top:90px;width:460px;height:420px;background:#fff;padding:16px 16px 60px;transform:rotate(-4deg);box-shadow:0 10px 40px rgba(0,0,0,.6)"><div style="width:100%;height:100%;background:linear-gradient(135deg,#ff9a3d,#bf5af2);display:flex;align-items:flex-end;justify-content:center;font-size:120px">🧢👩</div></div>
 <div style="position:absolute;left:110px;top:540px;font-size:26px;font-weight:800;color:#111;transform:rotate(-4deg);z-index:3">мы и вайб ✨</div>
</div>
<div class="card" id="c2" style="background:#000">
 <div class="hdr" style="color:#30d158">Сейчас играет</div>
 <div style="position:absolute;left:150px;top:80px;width:300px;height:300px;border-radius:24px;background:linear-gradient(135deg,#64d2ff,#ff2d78);display:flex;align-items:center;justify-content:center;font-size:120px">🎧</div>
 <div class="c" style="top:400px;font-size:30px;font-weight:900">Лали — новый трек (демо)</div>
 <div style="position:absolute;left:60px;right:60px;top:460px;height:8px;border-radius:4px;background:#333"><div id="pg2" style="height:8px;border-radius:4px;background:#fff;width:0"></div></div>
 <div class="ch" data-p="a"></div><div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#f4ecd8;color:#2a1f10">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Её кухня · площадь</div><div class="ttl mono" id="m3">6 м²</div>
 <div style="position:absolute;left:30px;top:220px;width:540px;height:180px;background:#c8b890;border-radius:12px"></div>
 <div style="position:absolute;left:60px;top:150px;font-size:90px">🍳</div><div style="position:absolute;left:420px;top:150px;font-size:90px">🧊</div>
 <div class="ch" data-p="c"></div><div class="ch" data-p="d"></div>
 <div id="sq3" class="c" style="top:150px;font-size:26px;font-weight:900;color:#d0021b;opacity:0">тесно, но уютно 🫶</div>
</div>
<div class="card" id="c4" style="background:#0a0610">
 <svg width="600" height="200" style="position:absolute;left:0;top:40px"><path d="M0 40 Q150 140 300 60 T600 70" stroke="#444" stroke-width="3" fill="none"/></svg>
 <div id="lb4" style="position:absolute;left:0;right:0;top:40px;height:200px"></div>
 <div class="ch" data-p="e"></div><div class="ch" data-p="f"></div>
</div>
<div class="card" id="c5" style="background:#1c1c1e">
 <div class="hdr">Раздражение</div><div class="ttl mono" id="an5" style="color:#ff453a">0%</div>
 <div style="position:absolute;left:40px;right:40px;top:150px;height:26px;border-radius:13px;background:#2c2c2e;overflow:hidden"><div id="ab5" style="height:26px;background:linear-gradient(90deg,#ffd60a,#ff453a);width:0"></div></div>
 <div class="ch" data-p="g"></div>
 <div id="st5" style="position:absolute;left:330px;top:380px;font-size:60px;opacity:0;z-index:6">💢</div>
</div>
<div class="card" id="c6" style="background:#2a1a10">
 <div id="ct6" style="position:absolute;inset:0;z-index:4"></div>
 <div class="ch" data-p="h"></div>
 <div id="sc6" style="position:absolute;left:24px;right:24px;top:24px;background:#fff;color:#111;border-radius:18px;padding:10px 14px;font-size:24px;font-weight:900;opacity:0;z-index:7">🐈 захват территории: 100%</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML='bdf'.includes(p)?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 let l='';const C=['#ff453a','#ffd60a','#30d158','#64d2ff','#bf5af2','#ff9f0a','#ff2d78','#30d158'];for(let i=0;i<8;i++){const x=30+i*72,y=40+Math.sin(i*.9)*40+40;l+=`<div id="l4_${i}" style="position:absolute;left:${x}px;top:${y}px;width:28px;height:40px;border-radius:50% 50% 45% 45%;background:${C[i]}"></div>`;}$('lb4').innerHTML=l;
 let c='';for(let i=0;i<6;i++)c+=`<div id="k6_${i}" style="position:absolute;font-size:70px;opacity:0">🐈</div>`;$('ct6').innerHTML=c;})();
'''
RENDER='''
 {$('ph1').style.transform=`rotate(${-4+Math.sin(t*2)*1}deg) scale(${1+.02*Math.sin(t*3)})`;}
 {$('pg2').style.width=(seg(t,2.5,4.9)*100)+'%';const b=Math.sin(t*9);place('a',200,700,.9,false);place('b',400,700,.9,true);
  pose('a',{aL:8,aR:-60,hd:b*8,bob:-Math.abs(b)*8});pose('b',{aL:8,aR:-60,hd:-b*8,bob:-Math.abs(b)*8});}
 {const s=eo(seg(t,5.9,6.8));$('m3').textContent=(6-s*2).toFixed(0)+' м²';$('sq3').style.opacity=seg(t,6.74,6.85);
  place('c',lerp(200,265,s),700,1.0,false);place('d',lerp(400,335,s),700,1.0,true);pose('c',{aL:8,aR:-8,hd:-6});pose('d',{aL:8,aR:-8,hd:-6});}
 {for(let i=0;i<8;i++){const on=t>=8.06?(Math.sin(t*6+i*1.3)>-.3):t>=7.32+i*.08;const e=$('l4_'+i);e.style.opacity=on?1:.15;e.style.boxShadow=on?`0 0 30px ${e.style.background}`:'none';}
  place('e',230,700,1.0,false);place('f',370,700,1.0,true);pose('e',{aL:8,aR:-60,hd:-10});pose('f',{aL:8,aR:-60,hd:-10});}
 {const a=Math.round(eo(seg(t,10.58,11.7))*100);$('an5').textContent=a+'%';$('ab5').style.width=a+'%';$('st5').style.opacity=seg(t,11.16,11.26);$('st5').style.transform=`scale(${1+.3*Math.abs(Math.sin(t*10))})`;
  place('g',300,700,1.0,false);pose('g',t>=11.16?{aL:60,aR:-60,hd:Math.sin(t*16)*6,open:1}:{aL:8,aR:-8});}
 {const P=[[60,420],[440,420],[250,140],[60,180],[460,180],[250,520]];for(let i=0;i<6;i++){const s=11.9+i*.18;const e=$('k6_'+i);e.style.opacity=seg(t,s,s+.1);e.style.left=P[i][0]+'px';e.style.top=P[i][1]+'px';e.style.transform=`scale(${eb(seg(t,s,s+.3))})`;}
  $('sc6').style.opacity=seg(t,13.64,13.75);place('h',300,690,1.0,false);pose('h',t>=13.64?{aL:60,aR:-60,hd:12,open:1}:{aL:8,aR:-8,hd:-8});}
'''
