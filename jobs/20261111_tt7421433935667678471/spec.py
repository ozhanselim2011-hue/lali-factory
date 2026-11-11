DUR=17.3
FADE=16.9
START=15.5
SONG='Джиган, Artik & Asti, NILETTO — Худи'
BG='linear-gradient(180deg,#0a0c14,#030306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Закину",15.74],["худи,",16.26],["прыгну",17.0],["в",18.04],["Импрезу,",18.2]],
 [["мотор",18.78],["поёт",18.96],["и",19.36],["ветер",19.58],["дует",20.5]],
 [["пока",21.4],["ты",21.88],["где-то",22.28],["там…",22.82]],
 [["а",24.76],["мне",25.74],["уже",25.98],["по",26.46],["барабану,",26.76]],
 [["Господи,",28.04],["я",28.86],["еду",29.04],["прямо",29.22]],
 [["очищаю",29.6],["карму",31.24]],
]
SC=[[15.2,18.72],[18.72,21.35],[21.35,24.7],[24.7,27.98],[27.98,29.55],[29.55,99]]
GLOW=['#3a3a5a','#1a4a7a','#5a1d7a','#7a5a1a','#1a5c4e','#3a5a7a']
PEMO=['🧥','🏎️','🤷','🥁','🛣️','🧘']
END=[32.4,32.8]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr">Гардероб</div>
 <div id="hd1" style="position:absolute;left:230px;top:-160px;font-size:150px;z-index:6">🧥</div>
 <div class="ch" data-p="a"></div>
 <div id="cr1" style="position:absolute;left:620px;top:470px;font-size:120px;transform:scaleX(-1);z-index:4">🚙</div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#ff8a3d,#ffb36b 55%,#333 56%,#1a1a1a)">
 <div id="ln2" style="position:absolute;inset:0"></div>
 <div id="cr2" style="position:absolute;left:170px;top:350px;font-size:170px;transform:scaleX(-1);z-index:4">🚙</div>
 <div id="wd2" style="position:absolute;inset:0;z-index:5"></div>
 <div class="c" id="sp2" style="top:40px;font-size:36px;font-weight:900;color:#fff;text-shadow:0 3px 12px #000">🔊 врум-врум</div>
</div>
<div class="card" id="c3" style="background:#000">
 <div class="hdr">Где она?</div>
 <div style="position:absolute;left:40px;right:40px;top:90px;height:320px;border-radius:24px;background:#d8e6d0;overflow:hidden"><div id="pn3" style="position:absolute;font-size:50px">📍</div><div class="c" style="top:130px;font-size:40px;font-weight:900;color:#8e8e93">❓❓❓</div></div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c4" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Переживания</div><div class="ttl mono" id="cr4" style="color:#30d158">100%</div>
 <div id="dr4" style="position:absolute;left:380px;top:300px;font-size:120px">🥁</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c5" style="background:linear-gradient(180deg,#87ceeb,#d8f0ff 55%,#555 56%,#333)">
 <div style="position:absolute;left:270px;top:380px;width:60px;height:310px;background:repeating-linear-gradient(180deg,#fff 0 40px,transparent 40px 80px)" id="rd5"></div>
 <div id="cr5" style="position:absolute;left:220px;top:470px;font-size:140px;z-index:4">🚙</div>
</div>
<div class="card" id="c6" style="background:radial-gradient(circle at 50% 40%,#1a3a5a,#05101a)">
 <div class="hdr" style="color:#64d2ff">Карма · очистка</div>
 <div style="position:absolute;left:40px;right:40px;top:90px;height:26px;border-radius:13px;background:#2c2c2e;overflow:hidden"><div id="kb6" style="height:26px;background:linear-gradient(90deg,#64d2ff,#30d158);width:0"></div></div>
 <div class="c mono" id="kp6" style="top:130px;font-size:40px;font-weight:900;color:#64d2ff">0%</div>
 <div class="ch" data-p="d"></div>
 <div id="au6" style="position:absolute;left:150px;top:200px;width:300px;height:300px;border-radius:50%;box-shadow:0 0 80px #64d2ff;opacity:0"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 let l='';for(let i=0;i<6;i++)l+=`<div id="l2_${i}" style="position:absolute;top:560px;width:70px;height:10px;border-radius:5px;background:#fff"></div>`;$('ln2').innerHTML=l;
 let w='';for(let i=0;i<8;i++)w+=`<div id="w2_${i}" style="position:absolute;height:4px;width:${80+rnd(i)*100}px;border-radius:2px;background:rgba(255,255,255,.7)"></div>`;$('wd2').innerHTML=w;})();
'''
RENDER='''
 {$('hd1').style.top=lerp(-160,260,eo(seg(t,15.74,16.3)))+'px';$('hd1').style.opacity=t<16.6?1:0;$('cr1').style.left=lerp(620,360,eo(seg(t,17.0,18.2)))+'px';
  place('a',lerp(200,330,eo(seg(t,17.0,18.4))),700,1.0,false);pose('a',t>=16.6?{aL:40,aR:-40,hd:-6,open:1}:{aL:8,aR:-8});$('ch_a').style.filter=t>=16.3?'hue-rotate(160deg)':'none';}
 {for(let i=0;i<6;i++)$('l2_'+i).style.left=((((-t*1100+i*130)%780)+780)%780-90)+'px';for(let i=0;i<8;i++){const e=$('w2_'+i);e.style.top=(100+i*50)+'px';e.style.left=((((-t*1600+i*190)%800)+800)%800-100)+'px';e.style.opacity=t>=19.58?.8:0;}
  $('cr2').style.transform=`scaleX(-1) translateY(${Math.sin(t*30)*3}px)`;$('sp2').style.opacity=t>=18.96?1:0;}
 {const a=t*2;$('pn3').style.left=(240+Math.cos(a)*180)+'px';$('pn3').style.top=(130+Math.sin(a*1.3)*100)+'px';place('b',300,700,1.0,false);pose('b',{aL:8,aR:-8,hd:Math.sin(t*3)*14});}
 {const k=eo(seg(t,26.0,27.5));$('cr4').textContent=Math.round(100*(1-k))+'%';$('cr4').style.color=k>.5?'#ff453a':'#30d158';$('dr4').style.transform=`rotate(${Math.sin(t*20)*10}deg)`;
  place('c',200,700,1.0,false);pose('c',t>=26.76?{aL:150*Math.sin(t*10),aR:-150*Math.cos(t*10),open:1}:{aL:8,aR:-8});}
 {$('rd5').style.backgroundPosition=`0 ${t*600}px`;$('cr5').style.transform=`scale(${1+.03*Math.sin(t*20)})`;}
 {const k=eo(seg(t,29.6,31.6));$('kb6').style.width=(k*100)+'%';$('kp6').textContent=Math.round(k*100)+'%';$('au6').style.opacity=k;place('d',300,700,1.0,false);pose('d',{aL:120,aR:-120,hd:0,bob:-Math.sin(t*2)*6});}
'''
