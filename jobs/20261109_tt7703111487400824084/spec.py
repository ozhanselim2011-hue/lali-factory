DUR=19.2
FADE=18.8
START=27.7
SONG='SLAVA MARLOW — Ты горишь как огонь 2'
BG='linear-gradient(180deg,#160806,#050202)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Ты",27.92],["горишь",28.46],["как",29.04],["огонь,",29.34]],
 [["у",29.9],["меня",30.2],["агония",30.76]],
 [["это",31.68],["любовь",32.02],["или",32.94],["это",33.32],["паранойя?",33.62]],
 [["ты",34.94],["горишь",36.06],["как",38.28],["огонь,",38.54]],
 [["у",39.28],["меня",39.52],["агония",42.9]],
 [["это",43.92],["любовь",44.24],["или",45.1],["это",45.34],["паранойя?",45.76]],
]
SC=[[27.4,29.85],[29.85,31.62],[31.62,34.88],[34.88,39.2],[39.2,43.86],[43.86,99]]
GLOW=['#7a2a0a','#7a1f1f','#5a1d7a','#7a3a0a','#1a5c2e','#3a3a5a']
PEMO=['🔥','🫠','🎰','🧯','📈','🔍']
END=[46.5,46.9]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:radial-gradient(circle at 50% 30%,#5a1a0a,#140402)">
 <div class="hdr" style="color:#ff9f0a">Тепловизор · она</div>
 <div class="c" style="top:110px;font-size:170px;filter:sepia(1) saturate(6) hue-rotate(-30deg)">👩</div>
 <div class="c mono" id="tp1" style="top:330px;font-size:64px;font-weight:900;color:#ff9f0a">36.6°</div>
 <div id="fl1" style="position:absolute;inset:0;z-index:6"></div>
</div>
<div class="card" id="c2" style="background:#1c1c1e">
 <div class="hdr">Состояние</div><div class="ttl">HP: <span id="hp2" class="mono" style="color:#30d158">100</span></div>
 <div style="position:absolute;left:40px;right:40px;top:150px;height:24px;border-radius:12px;background:#2c2c2e;overflow:hidden"><div id="hb2" style="height:24px;background:#30d158;width:100%"></div></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c3" style="background:linear-gradient(180deg,#2a0a3a,#0a0214)">
 <div class="c" style="top:40px;font-size:30px;font-weight:900">Диагноз</div>
 <div style="position:absolute;left:60px;right:60px;top:110px;height:120px;border-radius:24px;background:#000;border:4px solid #ffd60a;overflow:hidden"><div id="rl3" class="c" style="top:28px;font-size:46px;font-weight:900">💖 любовь</div></div>
 <div id="rs3" class="c" style="top:260px;font-size:26px;font-weight:800;color:#ffd60a;opacity:0">результат: 50 / 50 🤷</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c4" style="background:#2a0505">
 <div id="al4" style="position:absolute;inset:0;background:#ff0000;opacity:0"></div>
 <div class="c" style="top:40px;font-size:36px;font-weight:900;z-index:6">🚨 ПОЖАРНАЯ ТРЕВОГА</div>
 <div class="c" style="top:100px;font-size:24px;font-weight:700;color:#ffb3b3;z-index:6">источник возгорания: она 💃</div>
 <div id="fi4" style="position:absolute;left:380px;top:300px;font-size:130px;z-index:4">🔥</div>
 <div id="fm4" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="c"></div><div id="ex4" style="position:absolute;left:250px;top:400px;font-size:70px;z-index:6">🧯</div>
</div>
<div class="card" id="c5" style="background:#000">
 <div class="hdr" style="color:#30d158">Монитор пациента</div>
 <svg width="560" height="200" style="position:absolute;left:20px;top:100px"><polyline id="ek5" fill="none" stroke="#30d158" stroke-width="5" points=""/></svg>
 <div class="c mono" id="bp5" style="top:310px;font-size:60px;font-weight:900;color:#30d158">80 ❤</div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c6" style="background:#3a2a1a">
 <div class="hdr" style="color:#ffd60a">Расследование: её лайки</div>
 <div id="bd6" style="position:absolute;inset:0"></div>
 <svg id="th6" width="600" height="690" style="position:absolute;z-index:3"></svg>
 <div class="ch" data-p="e"></div><div id="mg6" style="position:absolute;left:330px;top:420px;font-size:70px;z-index:6">🔍</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 let f='';for(let i=0;i<14;i++)f+=`<div id="f1_${i}" style="position:absolute;font-size:${40+rnd(i)*40}px;opacity:0">🔥</div>`;$('fl1').innerHTML=f;
 let m='';for(let i=0;i<14;i++)m+=`<div id="m4_${i}" style="position:absolute;width:${20+rnd(i)*20}px;height:${20+rnd(i)*20}px;border-radius:50%;background:#fff;opacity:0"></div>`;$('fm4').innerHTML=m;
 const P=[[60,90,'📸 лайк в 3:12'],[340,80,'👀 онлайн 4 раза'],[70,300,'🫥 «ок» без смайла'],[360,300,'💬 ответила через 2 мин']];
 $('bd6').innerHTML=P.map((p,i)=>`<div id="p6_${i}" style="position:absolute;left:${p[0]}px;top:${p[1]}px;width:180px;background:#f4ecd8;color:#111;padding:12px;font-size:20px;font-weight:800;transform:rotate(${i%2?4:-4}deg);opacity:0;box-shadow:0 6px 20px rgba(0,0,0,.4)">📌 ${p[2]}</div>`).join('');})();
'''
RENDER='''
 {const k=eo(seg(t,28.46,29.5));$('tp1').textContent=lerp(36.6,1000,k).toFixed(1)+'°';$('tp1').style.color=k>.5?'#ff453a':'#ff9f0a';
  for(let i=0;i<14;i++){const e=$('f1_'+i);e.style.opacity=k*(.5+.5*Math.abs(Math.sin(t*6+i)));e.style.left=(rnd(i+3)*540)+'px';e.style.top=(520-((t*.8+rnd(i))%1)*300)+'px';}}
 {const v=Math.round(lerp(100,3,eo(seg(t,30.2,31.3))));$('hp2').textContent=v;$('hb2').style.width=v+'%';$('hb2').style.background=v<30?'#ff453a':'#30d158';$('hp2').style.color=v<30?'#ff453a':'#30d158';
  const m=seg(t,30.76,31.5);place('a',300,690,1.0,false);$('ch_a').style.transform=`scale(${1+m*.3},${1-m*.5})`;pose('a',{aL:40,aR:-40,hd:10,open:1});}
 {const sp=t<33.62;$('rl3').textContent=sp?(Math.floor(t*10)%2?'💖 любовь':'🌀 паранойя'):'💖🌀 и то и то';$('rs3').style.opacity=seg(t,33.7,33.8);
  place('b',300,690,1.0,false);pose('b',sp?{aL:8,aR:-8,hd:Math.sin(t*8)*10}:{aL:60,aR:-60,open:1});}
 {const a=t>=36.06;$('al4').style.opacity=a?.3*Math.abs(Math.sin(t*8)):0;place('c',170,690,1.0,false);pose('c',a?{aL:8,aR:-90,hd:-6}:{aL:8,aR:-8});
  const sp=seg(t,38.28,39.2);$('fi4').style.transform=`scale(${1-sp*.3+.1*Math.sin(t*10)})`;
  for(let i=0;i<14;i++){const ph=(t*2+i/14)%1;const e=$('m4_'+i);e.style.opacity=t>=38.28?1-ph:0;e.style.left=(300+ph*130)+'px';e.style.top=(440-ph*80+Math.sin(i)*30)+'px';}}
 {let p='';const bpm=lerp(80,200,seg(t,39.3,42.9));for(let x=0;x<=560;x+=8){const ph=((x/560)*4+t*bpm/60)%1;const y=ph>.45&&ph<.5?20:(ph>.5&&ph<.55?180:100);p+=`${x},${y} `;}$('ek5').setAttribute('points',p);
  $('bp5').textContent=Math.round(bpm)+' ❤';$('bp5').style.color=bpm>150?'#ff453a':'#30d158';$('ek5').setAttribute('stroke',bpm>150?'#ff453a':'#30d158');place('d',300,700,.9,false);pose('d',{aL:8,aR:-8,hd:6,bob:Math.sin(t*bpm/9)*3});}
 {const T=[44.0,44.5,45.1,45.5];let s='';for(let i=0;i<4;i++){$('p6_'+i).style.opacity=seg(t,T[i],T[i]+.1);}
  const pts=[[150,140],[430,130],[160,350],[450,350]];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)if(t>=Math.max(T[i],T[j])+.1)s+=`<line x1="${pts[i][0]}" y1="${pts[i][1]}" x2="${pts[j][0]}" y2="${pts[j][1]}" stroke="#d0021b" stroke-width="3"/>`;$('th6').innerHTML=s;
  place('e',250,700,.95,false);pose('e',t>=45.76?{aL:60,aR:-60,open:1,hd:Math.sin(t*14)*10}:{aL:8,aR:-90,hd:-6});$('mg6').style.transform=`translate(${Math.sin(t*3)*20}px,${Math.cos(t*3)*10}px)`;}
'''
