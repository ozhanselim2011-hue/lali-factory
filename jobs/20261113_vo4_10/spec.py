exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#3a4a1a'];PEMO=['🦎']
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#8fb35a,#4a6a2a)">
 <div style="position:absolute;left:0;right:0;bottom:0;height:200px;background:#5a4a2a;border-radius:50% 50% 0 0/30% 30% 0 0"></div>
 <div style="position:absolute;left:30px;top:120px;font-size:120px">🌳</div><div style="position:absolute;right:20px;top:90px;font-size:150px">🌴</div>
 <div id="sp" style="position:absolute;left:230px;top:300px;font-size:150px">🧍</div>
 <div id="rv" style="position:absolute;left:-200px;top:330px;font-size:110px">🦜</div>
 <div style="position:absolute;inset:0;border:16px solid rgba(0,0,0,.0);box-shadow:inset 0 0 120px rgba(0,0,0,.6)"></div>
 <div style="position:absolute;left:20px;top:18px;background:#ffcc00;color:#000;font-weight:900;font-size:20px;padding:4px 10px">ДИКАЯ ПРИРОДА</div>
 <div id="sb" style="position:absolute;left:24px;right:24px;bottom:24px;background:rgba(0,0,0,.65);padding:14px 18px;font-size:23px;font-weight:700;font-style:italic;color:#fff;line-height:1.3"></div>
</div>'''
BUILD=''
RENDER='''
 const N=[[0,'Перед нами — редкая особь рэпера в естественной среде.'],[2.75,'Учёные выяснили: в ней обитают сразу четыре вида.'],[4.5,'Особь берёт палку в зубы — так она метит территорию.'],[6.6,'Брачный ритуал завершается взрывом.'],[7.75,'Но в саванне появляется конкурент — эмси-попугай.'],[10.0,'Попугай повторяет чужие строчки. Природа жестока.'],[11.0,'Особь греется на солнце. Ей хорошо.'],[13.25,'Жюри National Geographic ставит ей 4.']];
 let c='';for(const n of N)if(t>=n[0])c=n[1];$('sb').textContent=c;
 $('sp').style.transform=`translateY(${Math.abs(Math.sin(t*3))*-8}px) rotate(${t>=6.25&&t<7.6?Math.sin(t*40)*10:0}deg) scale(${t>=11&&t<13.2?1.1:1})`;
 $('rv').style.left=(t<7.75?-200:t<10.5?lerp(-200,40,seg(t,7.75,8.6)):lerp(40,-250,seg(t,10.5,11)))+'px';$('rv').style.transform=`rotate(${Math.sin(t*12)*8}deg)`;
 $('c1').style.filter=t>=6.9&&t<7.3?'brightness(2.5)':'none';
'''
