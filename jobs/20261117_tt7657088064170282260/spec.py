DUR=19.4
FADE=19.0
START=0
SONG='ENZRO — А я по ночам не сплю'
BG='linear-gradient(180deg,#0a0a1e,#030308)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["А",0.0],["я",0.74],["по",1.08],["ночам",1.34],["не",2.24],["сплю,",2.56]],
 [["не",3.34],["могу",3.66]],
 [["без",4.3],["твоего",5.96],["люба",6.72]],
 [["а",8.18],["я",8.88],["молчу",10.92],["и",11.82],["жду,",12.1]],
 [["всё",12.94],["жду",13.28]],
 [["жду",14.16],["только",15.36],["тебя",15.92]],
]
SC=[[-0.3,4.2],[4.2,8.0],[8.0,14.0],[14.0,99]]
GLOW=['#1d1d5a','#7a0a0a','#1d3a5a','#7a1f4a']
PEMO=['🐑','🔋','⏳','💐']
END=[19.0,19.4]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#141432,#0a0a1e)">
 <div id="ck1" class="c mono" style="top:40px;font-size:80px;font-weight:300">00:00</div>
 <div style="position:absolute;right:30px;top:160px;font:900 26px Inter;color:#d1c4ff">🐑 овец: <span id="sh1">0</span></div>
 <div id="sp1" style="position:absolute;inset:0"></div>
 <div style="position:absolute;left:60px;top:470px;width:480px;height:120px;background:#3a3a6a;border-radius:20px"></div><div style="position:absolute;left:60px;top:420px;width:120px;height:70px;background:#eee;border-radius:20px"></div>
 <div class="ch" data-p="a"></div>
 <div style="position:absolute;left:250px;top:450px;width:290px;height:90px;background:#5e5ce6;border-radius:20px;z-index:6"></div>
</div>
<div class="card" id="c2" style="background:#000">
 <div class="hdr" style="color:#ff453a">Заряд любви</div>
 <div style="position:absolute;left:120px;top:120px;width:340px;height:170px;border:10px solid #fff;border-radius:30px"><div id="bt2" style="position:absolute;left:10px;top:10px;bottom:10px;width:300px;border-radius:16px;background:#30d158"></div></div>
 <div style="position:absolute;left:470px;top:175px;width:24px;height:60px;background:#fff;border-radius:0 10px 10px 0"></div>
 <div id="pc2" class="c mono" style="top:320px;font-size:70px;font-weight:900">100%</div>
 <div id="wr2" class="c" style="top:410px;font:900 26px Inter;color:#ff453a;opacity:0">⚠️ нужен её «люб»</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:linear-gradient(180deg,#1a2a4a,#0a1020)">
 <div style="position:absolute;left:300px;top:60px;width:250px;height:300px;background:linear-gradient(#0a0a2a,#2a2a5a);border:12px solid #6a4a2a"><div style="position:absolute;left:0;right:0;top:50%;height:10px;background:#6a4a2a"></div><div style="position:absolute;left:50%;top:0;bottom:0;width:10px;background:#6a4a2a"></div><div style="position:absolute;left:150px;top:30px;font-size:50px">🌙</div></div>
 <div id="hg3" style="position:absolute;left:60px;top:80px;font-size:120px">⏳</div>
 <div id="dy3" style="position:absolute;left:40px;top:240px;font:900 28px Inter;color:#d1c4ff">ждёт уже: <span id="dd3">1</span> дн.</div>
 <div style="position:absolute;left:24px;right:24px;top:380px;background:#1c1c1e;border-radius:20px;padding:14px 18px;font:800 22px Inter;color:#8e8e93">она: <span id="st3">была в сети давно</span></div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#3a2a1a,#1a120a)">
 <div id="dr4" style="position:absolute;left:330px;top:90px;width:220px;height:480px;background:#8a5a32;border:10px solid #5a3a1a;transform-origin:220px 50%"><div style="position:absolute;left:20px;top:230px;width:20px;height:20px;border-radius:50%;background:#ffd60a"></div></div>
 <div id="lt4" style="position:absolute;left:340px;top:100px;width:200px;height:460px;background:linear-gradient(#ffe8b0,#ffb0d0);opacity:0"></div>
 <div class="ch" data-p="g"></div>
 <div class="ch" data-p="d"></div>
 <div id="fl4" style="position:absolute;font-size:64px;z-index:6">💐</div>
 <div id="dn4" style="position:absolute;left:30px;top:30px;font:900 34px Inter;color:#ffd60a;opacity:0">🔔 дзынь!</div>
 <div id="hh4" style="position:absolute;inset:0;z-index:7"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...(p=='g'?['#ff2d78','#ff8ac4','#ff2d78']:['#111','#64d2ff','#0a84ff']));});})();'''
RENDER='''
 {const k=seg(t,0,4.1);const m=Math.floor(k*300);$('ck1').textContent=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0');$('sh1').textContent=Math.floor(k*k*458);
  let s='';for(let i=0;i<4;i++){const p=((t*.9)+i/4)%1;s+=`<div style="position:absolute;left:${-60+p*700}px;top:${250-Math.abs(Math.sin(p*Math.PI*3))*60}px;font-size:56px">🐑</div>`}$('sp1').innerHTML=s;
  place('a',300,520,.75,false,-90);pose('a',{aL:8,aR:t>=2.56?-150:-8,hd:Math.sin(t*3)*10,open:t>=3.66});}
 {const v=t<4.3?100:lerp(100,1,eo(seg(t,4.3,6.8)));$('bt2').style.width=(3*v)+'px';$('bt2').style.background=v<20?'#ff453a':(v<50?'#ffd60a':'#30d158');$('pc2').textContent=Math.round(v)+'%';$('pc2').style.color=v<20?'#ff453a':'#fff';$('wr2').style.opacity=seg(t,6.72,6.8);
  place('b',300,690,.8,false);pose('b',{aL:8,aR:-8,hd:lerp(0,25,seg(t,4.3,6.8)),bob:lerp(0,20,seg(t,4.3,6.8))});}
 {$('hg3').style.transform=`rotate(${Math.floor(t)%2?180:0}deg)`;$('dd3').textContent=Math.max(1,Math.floor(seg(t,8.18,13.8)*99));$('st3').textContent=t>=12.94?'печатает…':'была в сети давно';$('st3').style.color=t>=12.94?'#30d158':'#8e8e93';
  place('c',150,690,.95,false);pose('c',{aL:60,aR:-8,hd:-15+Math.sin(t*2)*4});}
 {const op=eo(seg(t,15.36,15.92));$('dr4').style.transform=`perspective(600px) rotateY(${op*70}deg)`;$('lt4').style.opacity=op*.9;$('dn4').style.opacity=seg(t,15.36,15.45)*(1-seg(t,16.5,16.8));
  place('g',440,560,.85,true);$('ch_g').style.opacity=op;pose('g',{aL:120,aR:-120,open:1});
  place('d',180,690,1.05,false);pose('d',t>=15.92?{aL:120,aR:-120,open:1}:{aL:8,aR:-90,hd:Math.sin(t*3)*5});$('fl4').style.left=(t>=15.92?190:250)+'px';$('fl4').style.top=(t>=15.92?250:400)+'px';
  let h='';for(let i=0;i<10;i++){const s=15.92+i*.14;if(t>=s){const p=(t-s)/1.4;h+=`<div style="position:absolute;left:${200+rnd(i)*260}px;top:${400-p*340}px;font-size:${28+rnd(i+2)*24}px;opacity:${1-p}">💗</div>`}}$('hh4').innerHTML=h;}
'''
