DUR=28.3
FADE=27.9
START=0
SONG='BUINAGOLOVUSHKA — Ты лети'
BG='linear-gradient(180deg,#14101e,#050307)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Ты",0.0],["лучше",0.12],["подари",0.48],["мне",1.38]],
 [["один",1.68],["прекрасный",2.3],["сон,",3.34]],
 [["в",3.78],["котором",4.2],["громко",8.22]],
 [["играет",9.08],["Марш",9.84],["Мендельсона",10.5]],
 [["и",14.9],["ты",16.14],["в",16.4],["белом",16.52],["платье",17.1]],
 [["настолько",17.94],["красива",18.24]],
 [["а",21.78],["я",23.02],["на",24.02],["фоне",24.26],["твоей",24.8],["нежности",25.3]],
 [["кажусь",25.88],["очень",26.62],["сильным",26.9]],
]
SC=[[-0.3,3.7],[3.7,14.7],[14.7,21.6],[21.6,99]]
GLOW=['#3a1d5a','#5a4a2a','#5a5a7a','#7a1f4a']
PEMO=['🎁','🎶','👰','💪']
END=[27.9,28.3]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:radial-gradient(circle at 50% 40%,#3a2a6a,#100a20)">
 <div id="bx1" style="position:absolute;left:200px;top:300px;width:200px;height:170px;background:#ff2d78;border-radius:12px"><div style="position:absolute;left:88px;top:0;width:24px;height:100%;background:#ffd60a"></div></div>
 <div id="ld1" style="position:absolute;left:185px;top:270px;width:230px;height:46px;background:#ff5a95;border-radius:10px;transform-origin:0 46px"><div style="position:absolute;left:103px;top:0;width:24px;height:100%;background:#ffd60a"></div></div>
 <div id="cl1" style="position:absolute;left:140px;top:60px;width:320px;height:180px;opacity:0"><div style="position:absolute;inset:0;border-radius:90px;background:#fff"></div><div class="c" style="top:50px;font:900 34px Inter;color:#5e2cff">прекрасный сон ✨</div></div>
 <div id="sr1" style="position:absolute;inset:0"></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#f4ecd8,#d9c9a8);color:#3a2a10">
 <div class="hdr" style="color:#8a6a3a">ЗАГС · зал торжеств</div>
 <div style="position:absolute;left:30px;right:30px;top:80px;background:#fff;border-radius:22px;padding:16px 20px;box-shadow:0 6px 16px rgba(0,0,0,.1)"><div style="font:900 24px Inter">▶ Марш Мендельсона</div><div style="font:700 18px Inter;color:#888">Ф. Мендельсон · свадьба</div>
  <div style="margin-top:12px;height:14px;border-radius:7px;background:#eee;overflow:hidden"><div id="vl2" style="height:100%;width:10%;background:#ff2d78"></div></div><div id="vt2" style="font:900 18px Inter;color:#ff2d78;margin-top:6px">🔈 громкость 10%</div></div>
 <div id="nt2" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c3" style="background:radial-gradient(circle at 50% 30%,#fff,#e8e0f0)">
 <div id="sp3" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="w"></div>
 <div id="vl3" style="position:absolute;width:150px;height:200px;border-radius:70px 70px 10px 10px;background:rgba(255,255,255,.7);border:3px solid #ddd;z-index:4"></div>
 <div id="rt3" style="position:absolute;right:30px;top:40px;background:#ff2d78;color:#fff;border-radius:18px;padding:10px 18px;font:900 40px Inter;opacity:0">10/10</div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#ffd6e8,#ffb0d0)">
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#fff;border-radius:20px;padding:12px 18px;font:900 24px Inter;color:#111">💪 сила: <span id="pw4" class="mono">10</span><div style="margin-top:8px;height:14px;border-radius:7px;background:#eee;overflow:hidden"><div id="pb4" style="height:100%;width:5%;background:#ff2d78"></div></div></div>
 <div class="ch" data-p="b"></div><div class="ch" data-p="w2"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...(p.startsWith('w')?['#fff','#ffffff','#e8e8f0']:['#111','#3a3a3c','#111']));});})();'''
RENDER='''
 {const o=eo(seg(t,0.48,1.3));$('ld1').style.transform=`rotate(${-o*40}deg) translateY(${-o*60}px)`;$('cl1').style.opacity=seg(t,1.68,1.9);$('cl1').style.transform=`scale(${lerp(.4,1,eb(seg(t,1.68,2.1)))})`;
  let s='';if(t>=2.3)for(let i=0;i<14;i++)s+=`<div style="position:absolute;left:${rnd(i)*560}px;top:${rnd(i+4)*400}px;font-size:${18+rnd(i+1)*18}px;color:#ffd60a;opacity:${.4+.6*Math.abs(Math.sin(t*4+i))}">✦</div>`;$('sr1').innerHTML=s;}
 {const v=t<8.22?10:lerp(10,100,eo(seg(t,8.22,9.0)));$('vl2').style.width=v+'%';$('vt2').textContent=(v>=100?'🔊 громкость 100%':'🔈 громкость '+Math.round(v)+'%');
  let n='';if(t>=9.08)for(let i=0;i<10;i++){const p=((t-9.08)*.6+i/10)%1;n+=`<div style="position:absolute;left:${60+rnd(i)*480}px;top:${640-p*400}px;font-size:${34+rnd(i+3)*20}px;opacity:${1-p};color:#8a6a3a">${i%2?'♪':'♫'}</div>`}$('nt2').innerHTML=n;
  place('a',300,690,1.1,false);pose('a',t>=10.5?{aL:120+Math.sin(t*4)*20,aR:-120+Math.sin(t*4)*20,hd:Math.sin(t*2)*8}:(t>=8.22?{aL:8,aR:-8,hd:-12,open:1}:{aL:8,aR:-8}));}
 {const k=eb(seg(t,14.9,15.6));place('w',300,690,lerp(.6,1.2,k),false);pose('w',{aL:30,aR:-30,hd:t>=17.94?-8:0});$('vl3').style.left=(300-75)+'px';$('vl3').style.top=(690-290*lerp(.6,1.2,k)+10)+'px';$('vl3').style.transform=`scale(${lerp(.6,1.2,k)/1.2})`;
  $('ch_w').style.opacity=seg(t,14.9,15.1);$('vl3').style.opacity=seg(t,16.52,16.7);$('rt3').style.opacity=seg(t,18.24,18.3);$('rt3').style.transform=`rotate(6deg) scale(${1+.3*pop(t,18.24,7)})`;
  let s='';if(t>=17.94)for(let i=0;i<12;i++)s+=`<div style="position:absolute;left:${80+rnd(i)*440}px;top:${100+rnd(i+6)*450}px;font-size:${24+rnd(i)*20}px;color:#ffd60a;opacity:${Math.abs(Math.sin(t*5+i))}">✦</div>`;$('sp3').innerHTML=s;}
 {const p=t<25.88?lerp(10,30,seg(t,21.78,25.3)):lerp(30,999,eo(seg(t,25.88,26.9)));$('pw4').textContent=Math.round(p);$('pb4').style.width=Math.min(100,p/10)+'%';
  const fl=t>=26.62;place('b',fl?300:220,690,1.15,false);pose('b',fl?{aL:120,aR:-120,open:1,hd:-6}:{aL:60,aR:-8,hd:10});place('w2',fl?300:420,fl?380:690,fl?.75:1.0,true,0);pose('w2',{aL:fl?150:8,aR:fl?-150:-8});}
'''
