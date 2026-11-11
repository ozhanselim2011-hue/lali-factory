DUR=17.9
FADE=17.5
START=4.5
SONG='BRVZ — Отпускаю'
BG='linear-gradient(180deg,#0a0c14,#030306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Отпускаю,",4.74],["иди",5.86],["с",7.88],["Богом",8.1]],
 [["у",8.78],["нас",8.86],["разные",9.22],["дороги",9.92]],
 [["не",11.4],["держу",11.6],["тебя,",12.36],["не",12.78],["трогай",13.2]],
 [["ждать",14.06],["не",14.48],["буду",14.66],["на",15.04],["пороге",15.64]],
 [["у",16.78],["любви",17.0],["все",17.68],["вышли",18.02],["сроки",18.78]],
 [["отпускаю,",19.44],["иди",20.66],["с",21.52],["Богом",21.64]],
]
SC=[[4.2,8.7],[8.7,11.35],[11.35,14.0],[14.0,16.7],[16.7,19.38],[19.38,99]]
GLOW=['#1a4a7a','#1a5c4e','#7a1f1f','#5a3a1a','#7a5a1a','#3a5a7a']
PEMO=['🎈','🛣️','✋','🚪','🏷️','🕊️']
END=[22.0,22.4]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#87ceeb,#d8f0ff 60%,#8bc34a 61%,#5a8a2a)">
 <div id="bl1" style="position:absolute;left:330px;top:250px;z-index:4"><div style="width:120px;height:150px;border-radius:50%;background:#ff2d78;display:flex;align-items:center;justify-content:center;font-size:60px">👩</div><div style="width:2px;height:150px;background:#555;margin-left:60px"></div></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#d8e6d0">
 <svg width="600" height="690" style="position:absolute"><path d="M300 690 L300 420" stroke="#0a84ff" stroke-width="14" fill="none"/><path id="r2a" d="M300 420 L80 120" stroke="#ff2d78" stroke-width="14" fill="none" stroke-dasharray="380" stroke-dashoffset="380"/><path id="r2b" d="M300 420 L520 120" stroke="#0a84ff" stroke-width="14" fill="none" stroke-dasharray="380" stroke-dashoffset="380"/></svg>
 <div style="position:absolute;left:30px;top:70px;background:#ff2d78;color:#fff;border-radius:12px;padding:6px 12px;font-size:22px;font-weight:900">она → куда хочет</div>
 <div style="position:absolute;right:30px;top:70px;background:#0a84ff;color:#fff;border-radius:12px;padding:6px 12px;font-size:22px;font-weight:900">я → своей дорогой</div>
</div>
<div class="card" id="c3" style="background:#f4ecd8;color:#2a1f10">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Экспонат</div>
 <div style="position:absolute;left:60px;right:60px;top:420px;height:14px;background:#a00;border-radius:7px;z-index:6"></div>
 <div style="position:absolute;left:60px;top:400px;width:20px;height:200px;background:#c9a227"></div><div style="position:absolute;right:60px;top:400px;width:20px;height:200px;background:#c9a227"></div>
 <div id="sg3" style="position:absolute;left:180px;top:120px;background:#d0021b;color:#fff;border-radius:16px;padding:10px 20px;font-size:34px;font-weight:900;opacity:0">✋ НЕ ТРОГАТЬ</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c4" style="background:#2a2a2e">
 <div style="position:absolute;left:70px;top:120px;width:200px;height:420px;background:#5a3a1a;border:8px solid #3a2410;border-radius:10px"></div>
 <div id="mt4" style="position:absolute;left:60px;top:560px;width:220px;height:40px;background:#8a6a4a;border-radius:6px;color:#fff;font-size:20px;font-weight:900;display:flex;align-items:center;justify-content:center">WELCOME</div>
 <div id="cl4" class="c mono" style="top:60px;font-size:40px;font-weight:900;color:#ffd60a">00:00</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c5" style="background:#f2f2f7;color:#111">
 <div style="position:absolute;left:100px;top:100px;width:400px;height:300px;background:#fff;border-radius:20px;box-shadow:0 10px 30px rgba(0,0,0,.15);padding:24px">
  <div style="font-size:36px;font-weight:900">💖 Любовь</div><div style="font-size:22px;color:#8e8e93;font-weight:700;margin-top:8px">изготовлено: давно</div><div style="font-size:26px;font-weight:900;margin-top:12px">годен до: <span id="dt5" class="mono">—</span></div></div>
 <div id="st5" style="position:absolute;left:160px;top:240px;border:8px solid #d0021b;color:#d0021b;border-radius:16px;padding:6px 20px;font-size:44px;font-weight:900;transform:rotate(-12deg);opacity:0;z-index:6">ПРОСРОЧЕНО</div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c6" style="background:linear-gradient(180deg,#87ceeb,#fff7c2)">
 <div style="position:absolute;left:200px;top:300px;width:200px;height:220px;border:6px solid #c9a227;border-radius:100px 100px 10px 10px;background:repeating-linear-gradient(90deg,transparent 0 26px,#c9a227 26px 32px)"></div>
 <div id="bd6" style="position:absolute;left:270px;top:400px;font-size:70px;z-index:4">🕊️</div>
 <div class="ch" data-p="e"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});})();
'''
RENDER='''
 {const k=eo(seg(t,4.8,8.6));$('bl1').style.top=lerp(250,-280,k)+'px';$('bl1').style.left=(330+Math.sin(t*2)*20)+'px';place('a',260,700,1.0,false);pose('a',t>=4.74?{aL:8,aR:-150+Math.sin(t*10)*20,hd:-10}:{aL:8,aR:-60});}
 {$('r2a').setAttribute('stroke-dashoffset',380*(1-eo(seg(t,9.22,10.2))));$('r2b').setAttribute('stroke-dashoffset',380*(1-eo(seg(t,9.22,10.2))));}
 {$('sg3').style.opacity=seg(t,12.78,12.9);$('sg3').style.transform=`scale(${1+.3*pop(t,13.2,6)})`;place('b',300,690,1.0,false);pose('b',t>=11.6?{aL:8,aR:-150,hd:0}:{aL:8,aR:-8});}
 {const k=seg(t,14.1,16.5);const m=Math.floor(k*600);$('cl4').textContent=String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0');$('mt4').style.opacity=1-seg(t,15.64,16.0);
  const w=eo(seg(t,15.04,16.6));place('c',lerp(330,460,w),690,.9,false);pose('c',w>0&&w<1?walk(t,10):{aL:8,aR:-8,hd:-8});}
 {$('dt5').textContent=t<17.68?'—':'вчера';$('st5').style.opacity=seg(t,18.78,18.88);$('st5').style.transform=`rotate(-12deg) scale(${1+.4*pop(t,18.78,8)})`;place('d',480,700,.8,true);pose('d',t>=18.78?{aL:8,aR:-8,hd:14}:{aL:8,aR:-60});}
 {const k=eo(seg(t,19.5,22.2));$('bd6').style.left=lerp(270,520,k)+'px';$('bd6').style.top=lerp(400,40,k)+'px';$('bd6').style.transform=`scaleX(-1) rotate(${Math.sin(t*12)*12}deg)`;place('e',130,700,.9,false);pose('e',{aL:8,aR:-150+Math.sin(t*10)*20,open:t>=21.64?1:0});}
'''
