exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]]
GLOW=['#5a4a0a']
PEMO=['✈️']
HTML='''
<div class="card" id="c1" style="background:#0a0a0a">
 <div style="position:absolute;left:24px;right:24px;top:24px;font-size:30px;font-weight:900;color:#ffd60a;font-family:'JetBrains Mono'">✈ ВЫЛЕТ · DEPARTURES</div>
 <div style="position:absolute;left:24px;right:24px;top:80px;display:flex;font-family:'JetBrains Mono';font-size:18px;color:#8e8e93;font-weight:800"><span style="width:100px">РЕЙС</span><span style="flex:1">НАПРАВЛЕНИЕ</span><span style="width:180px;text-align:right">СТАТУС</span></div>
 <div id="bd" style="position:absolute;left:24px;right:24px;top:112px"></div>
</div>
'''
BUILD='''(function(){const R=[['4-01','ВО МНЕ ВСЕ ЧЕТЫРЕ'],['C4-07','ЗУБЫ → ВЗРЫВ'],['MC-77','МОИ СТРОЧКИ'],['TR-00','«ОНИ ЧЁ, ТЫРЯТ?»'],['OK-10','МНЕ ХОРОШО'],['44-44','САДИСЬ, ЧЕТЫРЕ']];
 document.getElementById('bd').innerHTML=R.map((r,i)=>`<div id="r${i}" style="display:flex;align-items:center;height:86px;border-bottom:1px solid #222;font-family:'JetBrains Mono';font-weight:900;font-size:22px;color:#ffd60a"><span style="width:100px">${r[0]}</span><span style="flex:1">${r[1]}</span><span id="s${i}" style="width:180px;text-align:right;color:#8e8e93">ПО ПЛАНУ</span></div>`).join('');})();'''
RENDER='''
 const T=[0.9,4.5,7.75,10.0,11.0,13.25];const S=[['ПОСАДКА','#30d158'],['ВЗОРВАН 💥','#ff453a'],['ЗАДЕРЖАН','#ff9f0a'],['ОТМЕНЁН','#ff453a'],['ВЫЛЕТЕЛ ✓','#30d158'],['ОЦЕНКА: 4','#64d2ff']];
 for(let i=0;i<6;i++){const on=t>=T[i];const e=$('s'+i);const flip=t>=T[i]&&t<T[i]+.35;e.textContent=flip?'▓▓▓▓▓▓':(on?S[i][0]:'ПО ПЛАНУ');e.style.color=on?S[i][1]:'#8e8e93';
  const cur=on&&(i==5||t<T[i+1]);$('r'+i).style.background=cur?'rgba(255,214,10,.15)':'transparent';}
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
