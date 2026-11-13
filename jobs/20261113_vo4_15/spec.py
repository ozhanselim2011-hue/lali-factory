exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
BG='#020608'
HTML='''
<div class="card" id="c1" style="background:#000">
 <div class="hdr" style="color:#64d2ff">Рентген · пациент Л.</div>
 <svg width="600" height="600" style="position:absolute;left:0;top:60px"><g stroke="#cfe8ff" stroke-width="10" fill="none" opacity=".55"><circle cx="300" cy="90" r="55"/><path d="M300 145 V430 M300 200 L200 300 M300 200 L400 300 M300 430 L230 570 M300 430 L370 570"/><path d="M240 230 Q300 250 360 230 M235 270 Q300 290 365 270 M240 310 Q300 330 360 310"/></g></svg>
 <div id="ob1" style="position:absolute;inset:0;z-index:4"></div>
 <div id="cn1" class="c mono" style="top:600px;font-size:34px;font-weight:900;color:#ff453a;opacity:0;z-index:6">обнаружено объектов: <span id="n1">0</span>/4</div>
</div>
<div class="card" id="c2" style="background:#000">
 <div class="hdr" style="color:#64d2ff">Стоматология · снимок</div>
 <div class="c" style="top:120px;font-size:200px;filter:grayscale(1) brightness(1.6)">🦷</div>
 <div id="bm2" class="c" style="top:120px;font-size:220px;opacity:0">💥</div>
 <div id="dg2" class="c mono" style="top:470px;font-size:30px;font-weight:900;color:#ff9f0a;opacity:0">диагноз: мощность C4 🧨</div>
</div>
<div class="card" id="c3" style="background:#0a1420">
 <div class="hdr" style="color:#64d2ff">Аудиограмма</div>
 <svg id="au3" width="560" height="260" style="position:absolute;left:20px;top:120px"></svg>
 <div id="tx3" class="c" style="top:420px;font-size:30px;font-weight:900;color:#30d158;opacity:0">🎧 распознано: МОИ строчки</div>
</div>
<div class="card" id="c4" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Анализ на плагиат</div>
 <div style="position:absolute;left:60px;right:60px;top:150px;height:300px;border-radius:24px;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center">
  <div style="font-size:120px">🧪</div><div id="rs4" style="font-size:40px;font-weight:900;color:#ff453a;opacity:0">ПОЛОЖИТЕЛЬНЫЙ</div></div>
</div>
<div class="card" id="c5" style="background:#000">
 <div class="hdr" style="color:#30d158">Монитор · самочувствие</div>
 <svg width="560" height="220" style="position:absolute;left:20px;top:110px"><polyline id="ek5" fill="none" stroke="#30d158" stroke-width="5" points=""/></svg>
 <div class="c mono" id="mo5" style="top:380px;font-size:50px;font-weight:900;color:#30d158">норм</div>
</div>
<div class="card" id="c6" style="background:#f4ecd8;color:#2a1f10">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Медкарта · заключение</div>
 <div style="position:absolute;left:40px;right:40px;top:90px;font-size:26px;font-weight:800;line-height:1.9">Внутри: 4 объекта ✔️<br>Взрывоопасность: C4 ✔️<br>Строчки: свои ✔️<br>Самочувствие: хорошо ✔️</div>
 <div id="gr6" style="position:absolute;left:330px;top:330px;width:200px;height:200px;border:10px solid #d0021b;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:130px;font-weight:900;color:#d0021b;transform:rotate(-12deg);opacity:0">4</div>
</div>
'''
BUILD='''(function(){let o='';const P=[[230,250],[370,250],[250,360],[350,360]];P.forEach((p,i)=>o+=`<div id="o1_${i}" style="position:absolute;left:${p[0]-35}px;top:${p[1]+60}px;width:70px;height:70px;border-radius:50%;background:rgba(255,69,58,.35);border:4px solid #ff453a;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:900;color:#fff;opacity:0">?</div>`);document.getElementById('ob1').innerHTML=o;})();'''
RENDER='''
 {const T=[0.9,1.25,1.6,2.0];let n=0;for(let i=0;i<4;i++){const on=t>=T[i];if(on)n++;$('o1_'+i).style.opacity=on?1:0;$('o1_'+i).style.transform=`scale(${eb(seg(t,T[i],T[i]+.25))})`;}
  $('n1').textContent=n;$('cn1').style.opacity=seg(t,0.9,1.0);$('cn1').style.transform=`scale(${1+.25*pop(t,3.5,6)})`;}
 {$('bm2').style.opacity=t>=7.0?1-seg(t,7.4,7.6):0;$('bm2').style.transform=`scale(${eb(seg(t,7.0,7.3))})`;$('dg2').style.opacity=seg(t,7.0,7.1);}
 {let p='';const a=Math.max(0,Math.min(110,(t-7.6)*80));for(let x=0;x<=560;x+=8){const y=130+Math.sin(x*.05+t*10)*a*Math.sin(x*.01);p+=`${x},${y} `;}$('au3').innerHTML=`<polyline points="${p}" fill="none" stroke="#64d2ff" stroke-width="5"/>`;$('tx3').style.opacity=seg(t,9.0,9.1);}
 {$('rs4').style.opacity=seg(t,10.5,10.6);$('rs4').style.transform=`scale(${1+.4*pop(t,10.5,8)})`;}
 {const k=seg(t,11.5,12.3);let p='';const bpm=lerp(70,40,k);for(let x=0;x<=560;x+=8){const ph=((x/560)*4+t*bpm/60)%1;const y=ph>.45&&ph<.5?40:(ph>.5&&ph<.55?180:110);p+=`${x},${y} `;}$('ek5').setAttribute('points',p);
  $('mo5').textContent=t<12.25?'норм':'ХОРОШО 😌';$('mo5').style.transform=`scale(${1+.3*pop(t,12.25,6)})`;}
 {$('gr6').style.opacity=seg(t,13.75,13.85);$('gr6').style.transform=`rotate(-12deg) scale(${1+.6*pop(t,13.75,8)})`;}
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
