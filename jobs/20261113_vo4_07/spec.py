exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#1a1a1a'];PEMO=['📹']
HTML='''
<div class="card" id="c1" style="background:#111;filter:grayscale(.85) contrast(1.2)">
 <div id="room" style="position:absolute;inset:0;background:linear-gradient(180deg,#3a3a3a 0 60%,#222 60%)"></div>
 <div style="position:absolute;left:60px;top:150px;width:160px;height:220px;background:#4a4a4a;border:6px solid #2a2a2a"></div>
 <div id="guy" style="position:absolute;left:300px;top:250px;font-size:150px">🧍</div>
 <div id="mc" style="position:absolute;left:30px;top:270px;font-size:110px;opacity:0">🕵️</div>
 <div id="fx" style="position:absolute;inset:0;background:#fff;opacity:0"></div>
 <div style="position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(0,0,0,.25) 0 2px,transparent 2px 4px);pointer-events:none"></div>
 <div style="position:absolute;left:20px;top:16px;font-family:'JetBrains Mono';font-size:22px;font-weight:900;color:#fff">CAM 04 · <span id="rec" style="color:#ff3b30">● REC</span></div>
 <div id="ts" style="position:absolute;right:20px;top:16px;font-family:'JetBrains Mono';font-size:22px;font-weight:900;color:#fff"></div>
 <div id="lb" style="position:absolute;left:20px;right:20px;bottom:20px;background:rgba(0,0,0,.75);border:2px solid #ffd60a;color:#ffd60a;font-family:'JetBrains Mono';font-size:22px;font-weight:900;padding:10px;opacity:0"></div>
</div>'''
BUILD=''
RENDER='''
 $('rec').style.opacity=Math.sin(t*6)>0?1:.2;$('ts').textContent='03:44:'+String(Math.floor(t)).padStart(2,'0');
 const L=[[0.9,'ОБНАРУЖЕНО: ОБЪЕКТ 1/4'],[2.0,'ОБНАРУЖЕНО: ОБЪЕКТЫ 4/4'],[4.5,'ПОДОЗРИТЕЛЬНОЕ ДВИЖЕНИЕ'],[7.0,'⚠️ ВЗРЫВ · МОЩНОСТЬ C4'],[7.75,'ПОСТОРОННИЙ МС В КАДРЕ'],[10.0,'КРАЖА: «МОИ СТРОЧКИ»'],[11.0,'ОБЪЕКТ: ЕМУ ХОРОШО'],[13.25,'ИНЦИДЕНТ ЗАКРЫТ · ОЦЕНКА 4']];
 let c='';for(const l of L)if(t>=l[0])c=l[1];$('lb').textContent=c;$('lb').style.opacity=c?1:0;
 $('fx').style.opacity=t>=7.0?Math.max(0,1-(t-7.0)*3):0;$('guy').style.transform=`translateX(${t>=7&&t<7.6?Math.sin(t*80)*14:0}px) rotate(${t>=11&&t<13.2?Math.sin(t*4)*8:0}deg)`;
 $('mc').style.opacity=t>=7.75&&t<11?1:0;$('mc').style.left=lerp(30,200,seg(t,7.75,9.5))+'px';
 if(t>=10.5&&t<11)$('mc').style.left=lerp(200,-200,seg(t,10.5,11))+'px';
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
