exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]]
GLOW=['#1a3a6a']
PEMO=['🎮']
HTML='''
<div class="card" id="c1" style="background:#5aa8e8">
 <div style="position:absolute;left:0;right:0;bottom:0;height:150px;background:repeating-linear-gradient(90deg,#4a8a2a 0 40px,#3a7a1a 40px 80px);border-top:10px solid #2a5a10"></div>
 <div style="position:absolute;left:20px;top:20px;font-family:'JetBrains Mono';font-weight:900;font-size:22px;color:#fff;text-shadow:3px 3px 0 #000;z-index:6">HP <span id="hp">❤❤❤❤</span><br>LVL <span id="lv">1</span> · XP <span id="xp">0</span></div>
 <div id="qs" style="position:absolute;right:20px;top:20px;width:250px;background:rgba(0,0,0,.6);border:3px solid #fff;padding:10px;font-family:'JetBrains Mono';font-size:17px;font-weight:800;color:#fff;z-index:6">КВЕСТ:<br><span id="qt">собери все 4</span></div>
 <div id="it" style="position:absolute;inset:0;z-index:4"></div>
 <div id="hero" style="position:absolute;bottom:150px;font-size:90px;z-index:5">🧍</div>
 <div id="boss" style="position:absolute;right:60px;bottom:150px;font-size:130px;opacity:0;z-index:5">👾</div>
 <div id="ach" style="position:absolute;left:60px;right:60px;top:200px;background:#111;border:4px solid #ffd60a;padding:12px;font-family:'JetBrains Mono';font-weight:900;font-size:22px;color:#ffd60a;text-align:center;opacity:0;z-index:7"></div>
 <div id="lc" class="c" style="top:260px;font-size:50px;font-weight:900;color:#ffd60a;font-family:'JetBrains Mono';text-shadow:4px 4px 0 #000;opacity:0;z-index:8">LEVEL 4 COMPLETE</div>
</div>
'''
BUILD='''(function(){let s='';for(let i=0;i<4;i++)s+=`<div id="c_${i}" style="position:absolute;left:${140+i*90}px;bottom:260px;font-size:50px;font-family:'JetBrains Mono';font-weight:900;color:#ffd60a;text-shadow:3px 3px 0 #000">${i+1}</div>`;document.getElementById('it').innerHTML=s;})();'''
RENDER='''
 const T=[0.9,1.25,1.6,2.0];let got=0;for(let i=0;i<4;i++){if(t>=T[i])got++;$('c_'+i).style.opacity=t>=T[i]?0:1;$('c_'+i).style.bottom=(260+Math.sin(t*5+i)*10)+'px';}
 const x=t<2.2?lerp(40,420,seg(t,0.5,2.2)):(t<7.75?420:lerp(420,200,seg(t,7.75,8.5)));$('hero').style.left=x+'px';$('hero').style.bottom=(150+Math.abs(Math.sin(t*10))*(t<2.2?40:0))+'px';
 let ach='';if(t>=3.5&&t<4.5)ach='🏆 ДОСТИЖЕНИЕ: «ВСЕ ЧЕТЫРЕ»';if(t>=7.0&&t<7.75)ach='💥 КРИТ: C4 ×999';if(t>=10.5&&t<11.0)ach='⚠️ ВРАГ УКРАЛ: «мои строчки»';if(t>=12.25&&t<13.2)ach='😌 БАФ: «хорошо» +100';
 $('ach').textContent=ach;$('ach').style.opacity=ach?1:0;
 $('boss').style.opacity=t>=7.75&&t<11.0?1:0;$('boss').style.transform=`translateX(${Math.sin(t*6)*10}px) scale(${t>=10.5?1-seg(t,10.5,11):1})`;
 $('qt').textContent=t<3.5?'собери все 4 ('+got+'/4)':(t<7.75?'взорви как C4':(t<11?'победи МС-вора':(t<13.25?'кайфуй':'сдай на 4')));
 $('lv').textContent=t<3.5?1:(t<7.75?2:(t<11?3:4));$('xp').textContent=Math.round(t*68);$('hp').textContent=t>=10.5&&t<11?'❤❤❤🖤':'❤❤❤❤';
 $('lc').style.opacity=seg(t,13.75,13.9);$('lc').style.transform=`scale(${1+.3*pop(t,13.75,6)})`;
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
