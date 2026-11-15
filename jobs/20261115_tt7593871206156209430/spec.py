DUR=10.2
FADE=9.8
START=0
SONG='Damir Mate — думаю о тебе'
BG='linear-gradient(180deg,#0a1420,#030508)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Погружаюсь",0.0],["в",0.96],["детали",1.4]],
 [["думаю",4.24],["о",5.24],["тебе",5.64]],
 [["каждый",6.04],["день,",6.88],["каждый",7.38],["день,",7.84],["каждый",8.38],["день",8.9]],
]
SC=[[-0.3,4.1],[4.1,5.95],[5.95,99]]
GLOW=['#0a3a5a','#5a1d4a','#7a1f4a']
PEMO=['🫧','🧠','📅']
END=[9.8,10.2]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#3aa0d8,#0a3a6a 50%,#020a1a)">
 <div id="bu1" style="position:absolute;inset:0"></div>
 <div style="position:absolute;right:24px;top:24px;background:rgba(0,0,0,.5);border-radius:16px;padding:10px 16px;font:900 26px 'JetBrains Mono'">глубина: <span id="dp1">0</span> м</div>
 <div id="dt1" style="position:absolute;left:24px;top:90px;font:800 24px Inter;line-height:2;color:#cfefff"></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#0a0a0a">
 <div class="hdr" style="color:#ff375f">МРТ · мысли</div>
 <svg width="360" height="360" style="position:absolute;left:120px;top:110px"><circle cx="180" cy="180" r="140" fill="none" stroke="#2c2c2e" stroke-width="60"/><circle id="pc2" cx="180" cy="180" r="140" fill="none" stroke="#ff2d78" stroke-width="60" stroke-dasharray="880" stroke-dashoffset="880" transform="rotate(-90 180 180)"/></svg>
 <div class="c" style="top:235px"><div id="pv2" class="mono" style="font-size:64px;font-weight:900">0%</div><div style="font:800 22px Inter;color:#ff8ac4">о тебе</div></div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#fff;color:#111">
 <div class="hdr" style="color:#ff2d78">Календарь</div><div class="ttl" style="color:#111">Ноябрь</div>
 <div id="cg3" style="position:absolute;left:30px;right:30px;top:160px;display:grid;grid-template-columns:repeat(7,1fr);gap:8px"></div>
 <div id="cn3" class="c" style="top:560px;font:900 30px Inter;color:#ff2d78;opacity:0"></div>
 <div class="ch" data-p="c"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#111','#64d2ff','#0a84ff');});
 let g='';for(let i=0;i<30;i++)g+=`<div id="d3_${i}" style="aspect-ratio:1;border-radius:12px;background:#f2f2f7;display:flex;align-items:center;justify-content:center;font:800 20px Inter;position:relative">${i+1}<span id="h3_${i}" style="position:absolute;font-size:30px;opacity:0">❤️</span></div>`;$('cg3').innerHTML=g;})();'''
RENDER='''
 {const k=seg(t,0,4.0);$('dp1').textContent=Math.round(k*40);place('a',300,lerp(330,690,eo(k)),.9,false,Math.sin(t*1.5)*10);pose('a',{aL:150+Math.sin(t*3)*20,aR:-150-Math.sin(t*3)*20,lL:Math.sin(t*4)*20,lR:-Math.sin(t*4)*20});
  let b='';for(let i=0;i<12;i++){const p=((t*.6)+rnd(i))%1;b+=`<div style="position:absolute;left:${240+rnd(i+2)*140}px;top:${600-p*560}px;width:${8+rnd(i)*14}px;height:${8+rnd(i)*14}px;border-radius:50%;border:2px solid rgba(255,255,255,.6)"></div>`}$('bu1').innerHTML=b;
  const D=[[0.96,'· её улыбка'],[1.4,'· её смех'],[2.3,'· родинка на щеке'],[3.2,'· как пишет «ахах»']];$('dt1').innerHTML=D.filter(d=>t>=d[0]).map(d=>`<div style="opacity:${seg(t,d[0],d[0]+.15)}">${d[1]}</div>`).join('');}
 {const v=eo(seg(t,4.24,5.7));$('pc2').setAttribute('stroke-dashoffset',880*(1-v));$('pv2').textContent=Math.round(v*100)+'%';place('b',300,690,.75,false);pose('b',{aL:150,aR:-150,hd:-10,open:t>=5.64});}
 {const T=[6.04,6.88,7.38,7.84,8.38,8.9];let n=0;T.forEach(s=>{if(t>=s)n+=5});if(t>=8.9)n=30;for(let i=0;i<30;i++){const on=i<n;const s=T[Math.min(5,Math.floor(i/5))];$('h3_'+i).style.opacity=on?1:0;$('h3_'+i).style.transform=`scale(${on?1+.6*pop(t,s+(i%5)*.04,10):0})`;$('d3_'+i).style.background=on?'#ffe0ec':'#f2f2f7';}
  $('cn3').textContent=n+'/30 дней — о тебе';$('cn3').style.opacity=t>=6.04?1:0;place('c',520,690,.6,true);pose('c',t>=8.9?{aL:150,aR:-150,open:1}:{aL:8,aR:-90});}
'''
