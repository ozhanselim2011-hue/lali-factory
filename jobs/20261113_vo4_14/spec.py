exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#0a5a2a'];PEMO=['⚽']
HTML='''
<div class="card" id="c1" style="background:repeating-linear-gradient(90deg,#2a8a3a 0 60px,#248030 60px 120px)">
 <div style="position:absolute;left:50%;top:0;bottom:0;width:6px;background:rgba(255,255,255,.7)"></div><div style="position:absolute;left:200px;top:245px;width:200px;height:200px;border:6px solid rgba(255,255,255,.7);border-radius:50%"></div>
 <div style="position:absolute;left:20px;top:20px;display:flex;font-weight:900;font-size:26px;z-index:6"><span style="background:#111;padding:6px 12px">Я</span><span id="sc" style="background:#d0021b;padding:6px 14px;font-family:'JetBrains Mono'">0:0</span><span style="background:#111;padding:6px 12px">МС</span><span id="mn" style="background:#fff;color:#111;padding:6px 10px;font-family:'JetBrains Mono'">00'</span></div>
 <div id="ball" style="position:absolute;font-size:60px;z-index:5">⚽</div>
 <div id="pl" style="position:absolute;left:120px;top:330px;font-size:100px;z-index:4">🏃</div>
 <div id="big" class="c" style="top:220px;font-size:80px;font-weight:900;color:#fff;text-shadow:0 6px 0 #000;opacity:0;z-index:7"></div>
 <div id="cm" style="position:absolute;left:0;right:0;bottom:0;background:rgba(0,0,0,.75);padding:14px 20px;font-size:23px;font-weight:800;z-index:6"></div>
</div>'''
BUILD=''
RENDER='''
 const C=[[0,'🎙 Комментатор: начинаем!'],[0.9,'🎙 Раз, два, три, ЧЕТЫРЕ касания!'],[4.5,'🎙 Закручивает мяч…'],[7.0,'🎙 УДАР! КАК C4!'],[7.75,'🎙 МС соперника исполняет его же финт'],[10.0,'🎙 ВАР: они чё, тырят?! Гол отменён'],[11.0,'🎙 Но ему хорошо'],[13.25,'🎙 Итог матча: оценка 4']];
 let c='';for(const x of C)if(t>=x[0])c=x[1];$('cm').textContent=c;
 const g=t>=7.0?(t>=10.5?'4:1':'4:0'):(t>=2.0?'0:0':'0:0');$('sc').textContent=t>=13.25?'4:4':g;$('mn').textContent=String(Math.floor(t*6)).padStart(2,'0')+"'";
 let bx=lerp(160,420,seg(t,0.9,2.0)),by=360-Math.abs(Math.sin(t*9))*80*(t<2.2);if(t>=4.5&&t<7){bx=200+Math.cos(t*8)*60;by=330+Math.sin(t*8)*60}if(t>=7&&t<7.75){bx=lerp(240,640,seg(t,7,7.3));by=lerp(330,150,seg(t,7,7.3))}if(t>=7.75){bx=300;by=380}
 $('ball').style.left=bx+'px';$('ball').style.top=by+'px';$('pl').style.left=(t<2.2?lerp(60,340,seg(t,0.9,2.0)):150)+'px';
 const B=t>=7&&t<7.75?'ГОООЛ!':t>=10.25&&t<11?'ВАР 🖥':t>=12.25&&t<13.2?'😌':t>=13.75?'4':'';$('big').textContent=B;$('big').style.opacity=B?1:0;$('big').style.transform=`scale(${1+.3*pop(t,t>=13.75?13.75:t>=12.25?12.25:t>=10.25?10.25:7,6)})`;
'''
