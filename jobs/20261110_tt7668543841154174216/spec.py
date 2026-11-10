DUR=22.6
FADE=22.2
START=0
SONG='Zivert — GAZ'
BG='linear-gradient(180deg,#10080a,#040203)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Но",0.0],["есть",0.5],["у",1.48],["меня",1.72],["один",2.2],["момент",3.16]],
 [["в",4.18],["запасе",4.84],["на",5.76],["каждый",5.92],["случай",6.6]],
 [["я",7.78],["газую,",8.42],["когда",9.12],["нету",9.48]],
 [["газую,",10.34],["когда",11.14],["есть",11.54],["всё",12.06]],
 [["везёт",12.4],["тому,",13.0],["кто",13.46],["везёт",13.62]],
 [["я",14.4],["газую,",16.3],["чтобы",17.14],["было",17.52]],
 [["газую,",18.14],["как",19.12],["машина",19.42]],
 [["кто",20.28],["может,",20.74],["так",21.24],["скажи",21.48],["мне",22.1]],
]
SC=[[-0.3,4.1],[4.1,7.7],[7.7,10.28],[10.28,12.35],[12.35,14.35],[14.35,18.08],[18.08,20.22],[20.22,99]]
GLOW=['#3a3a5a','#5a5a1a','#7a1f1f','#1a5c2e','#7a5a1a','#1a4a7a','#7a2a0a','#5a1d7a']
PEMO=['☝️','🎒','💸','💰','🛒','📈','🏎️','🤷']
END=[22.2,22.6]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr">Секретный план</div>
 <div id="sp1" class="c" style="top:150px;font-size:110px">⏳</div>
 <div id="mm1" class="c" style="top:300px;font-size:40px;font-weight:900;opacity:0">☝️ один момент…</div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#3a2a1a">
 <div class="hdr" style="color:#ffd60a">Рюкзак · на каждый случай</div>
 <div id="bp2" style="position:absolute;left:30px;right:30px;top:80px;display:grid;grid-template-columns:repeat(4,1fr);gap:10px"></div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#0d1a12">
 <div class="hdr" style="color:#30d158">Баланс</div><div class="ttl mono" style="color:#ff453a">0 ₽</div>
 <div id="pd3" style="position:absolute;left:380px;top:400px;width:110px;height:170px;border-radius:16px;background:#2c2c2e;border:6px solid #555;transform-origin:50% 100%;z-index:4"><div class="c" style="top:60px;font-size:24px;font-weight:900;color:#aaa">GAS</div></div>
 <div id="sm3" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:#0d1a12">
 <div class="hdr" style="color:#30d158">Баланс</div><div class="ttl mono" id="bl4" style="color:#30d158">0 ₽</div>
 <div id="pd4" style="position:absolute;left:380px;top:400px;width:110px;height:170px;border-radius:16px;background:#2c2c2e;border:6px solid #555;transform-origin:50% 100%;z-index:4"><div class="c" style="top:60px;font-size:24px;font-weight:900;color:#aaa">GAS</div></div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c5" style="background:linear-gradient(180deg,#9fd3ff,#d8f0ff 60%,#8bc34a 61%,#5a8a2a)">
 <div class="hdr" style="color:rgba(0,0,0,.5)">Везение</div><div class="ttl mono" id="lk5" style="color:#1f8a3a">+0%</div>
 <div id="ct5" style="position:absolute;top:360px;width:260px;height:100px;z-index:4"><div style="position:absolute;left:0;top:30px;width:260px;height:70px;background:#c0c0c0;border-radius:10px"></div><div style="position:absolute;left:30px;top:-40px;font-size:60px">🧢</div><div style="position:absolute;left:110px;top:-40px;font-size:60px">👩</div><div style="position:absolute;left:180px;top:-40px;font-size:60px">🐶</div></div>
 <div class="ch" data-p="e"></div>
</div>
<div class="card" id="c6" style="background:#111214">
 <div class="hdr">Цель «чтобы было»</div>
 <div id="gl6" style="position:absolute;left:30px;right:30px;top:90px;font-size:26px;font-weight:800;line-height:1.9"></div>
 <div style="position:absolute;left:40px;right:40px;top:330px;height:26px;border-radius:13px;background:#2c2c2e;overflow:hidden"><div id="pb6" style="height:26px;background:linear-gradient(90deg,#ff9f0a,#ff453a);width:0"></div></div>
 <div class="ch" data-p="f"></div>
</div>
<div class="card" id="c7" style="background:linear-gradient(180deg,#2a0505,#1a1a1a 60%,#333 61%)">
 <div id="ln7" style="position:absolute;inset:0"></div>
 <div id="cr7" style="position:absolute;left:180px;top:330px;font-size:190px;transform:scaleX(-1);z-index:4;opacity:0">🏎️</div>
 <div id="sk7" style="position:absolute;inset:0;z-index:5"></div>
 <div class="ch" data-p="g"></div>
</div>
<div class="card" id="c8" style="background:#000">
 <div class="hdr">Опрос в чате</div><div class="ttl" style="font-size:34px">Кто может так же? 🏎️</div>
 <div id="pl8" style="position:absolute;left:24px;right:24px;top:150px;font-size:26px;font-weight:800"></div>
 <div class="ch" data-p="h"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 $('bp2').innerHTML=['🩹','🔦','🍫','🧯','🔋','☂️','🧦','🗝️'].map((e,i)=>`<div id="b2_${i}" style="height:90px;border-radius:16px;background:#5a3a1a;display:flex;align-items:center;justify-content:center;font-size:50px;opacity:0">${e}</div>`).join('');
 let s='';for(let i=0;i<10;i++)s+=`<div id="s3_${i}" style="position:absolute;width:60px;height:60px;border-radius:50%;background:rgba(200,200,200,.6);opacity:0"></div>`;$('sm3').innerHTML=s;
 $('gl6').innerHTML=['🏠 дом','🚗 тачка','✈️ отпуск','💍 она'].map((g,i)=>`<div id="g6_${i}" style="opacity:.3">⬜ ${g}</div>`).join('');
 let l='';for(let i=0;i<8;i++)l+=`<div id="l7_${i}" style="position:absolute;height:6px;width:${80+rnd(i)*120}px;border-radius:3px;background:#ff9f0a;opacity:.7;top:${100+i*60}px"></div>`;$('ln7').innerHTML=l;
 let k='';for(let i=0;i<10;i++)k+=`<div id="k7_${i}" style="position:absolute;width:50px;height:50px;border-radius:50%;background:rgba(220,220,220,.6)"></div>`;$('sk7').innerHTML=k;
 $('pl8').innerHTML=['🙋 я','🙅 никто','🤡 сосед (врёт)'].map((s,i)=>`<div style="background:#1c1c1e;border-radius:16px;padding:12px 16px;margin-bottom:10px;position:relative;overflow:hidden"><div id="pv8_${i}" style="position:absolute;left:0;top:0;bottom:0;width:0;background:rgba(10,132,255,.4)"></div><span style="position:relative">${s}</span><span id="pp8_${i}" class="mono" style="position:relative;float:right">0%</span></div>`).join('');})();
'''
RENDER='''
 {$('sp1').style.transform=`rotate(${t*120}deg)`;$('mm1').style.opacity=seg(t,2.2,2.35);place('a',300,700,1.0,false);pose('a',t>=1.48?{aL:8,aR:-160,hd:-6}:{aL:8,aR:-8});}
 {for(let i=0;i<8;i++){$('b2_'+i).style.opacity=seg(t,4.6+i*.25,4.75+i*.25);$('b2_'+i).style.transform=`scale(${eb(seg(t,4.6+i*.25,4.9+i*.25))})`;}place('b',300,700,1.0,false);pose('b',t>=6.6?{aL:60,aR:-60,open:1}:{aL:8,aR:-60});}
 {const g=t>=8.42;$('pd3').style.transform=`rotateX(${g?40:0}deg)`;place('c',230,700,1.0,false);pose('c',g?{aL:8,aR:-8,lR:-40,hd:-6,open:1}:{aL:8,aR:-8});
  for(let i=0;i<10;i++){const ph=(t*1.5+i/10)%1;const e=$('s3_'+i);e.style.opacity=g?(1-ph)*.8:0;e.style.left=(100-ph*80+rnd(i)*40)+'px';e.style.top=(600-ph*120)+'px';e.style.transform=`scale(${1+ph*2})`;}}
 {$('bl4').textContent=fmt(eo(seg(t,10.4,11.6))*10000000)+' ₽';$('pd4').style.transform=`rotateX(${t>=10.34?40:0}deg)`;place('d',230,700,1.0,false);pose('d',{aL:60,aR:-60,lR:-40,open:1});}
 {const k=eo(seg(t,12.4,14.3));$('ct5').style.left=lerp(320,180,k)+'px';$('lk5').textContent='+'+Math.round(k*100)+'%';place('e',lerp(560,420,k),690,.9,true);pose('e',{aL:-70,aR:-70,hd:10,lL:Math.sin(t*10)*20,lR:-Math.sin(t*10)*20});}
 {const k=eo(seg(t,16.3,17.9));$('pb6').style.width=(k*100)+'%';for(let i=0;i<4;i++){const on=k>(i+1)/4.2;const e=$('g6_'+i);e.style.opacity=on?1:.3;e.innerHTML=(on?'✅ ':'⬜ ')+e.innerHTML.slice(2);}
  place('f',300,700,1.0,false);pose('f',t>=16.3?{aL:8,aR:-8,lR:-40,open:1,bob:Math.sin(t*20)*2}:{aL:8,aR:-8});}
 {const m=seg(t,18.6,19.42);for(let i=0;i<8;i++){$('l7_'+i).style.left=((((-t*1600+i*170)%800)+800)%800-100)+'px';}
  $('cr7').style.opacity=m;place('g',300,700,1.0*(1-m)+.01,false);pose('g',{aL:60,aR:-60,lR:-40,open:1});
  for(let i=0;i<10;i++){const ph=(t*2+i/10)%1;const e=$('k7_'+i);e.style.opacity=m*(1-ph);e.style.left=(470+ph*120)+'px';e.style.top=(470-ph*60)+'px';e.style.transform=`scale(${1+ph*2})`;}}
 {const V=[[100,1],[0,0],[0,0]];for(let i=0;i<3;i++){const k=eo(seg(t,21.24,22.0));const v=Math.round(V[i][0]*k);$('pv8_'+i).style.width=v+'%';$('pp8_'+i).textContent=v+'%';}
  place('h',300,700,1.0,false);pose('h',t>=22.1?{aL:60,aR:-60,open:1,hd:-8}:{aL:8,aR:-60,hd:-8});}
'''
