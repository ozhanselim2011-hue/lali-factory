exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#1d4a8a'];PEMO=['🌦']
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#4a90d9,#1d4a8a)">
 <div style="position:absolute;left:0;right:0;top:30px;text-align:center;font-size:30px;font-weight:700">Внутри меня</div>
 <div id="tp" style="position:absolute;left:0;right:0;top:70px;text-align:center;font-size:130px;font-weight:300">4°</div>
 <div id="cd" style="position:absolute;left:0;right:0;top:230px;text-align:center;font-size:30px;font-weight:800"></div>
 <div id="hr" style="position:absolute;left:24px;right:24px;top:310px;height:150px;border-radius:24px;background:rgba(0,0,0,.18);display:flex;justify-content:space-around;align-items:center"></div>
 <div id="al" style="position:absolute;left:24px;right:24px;top:480px;border-radius:24px;background:rgba(255,59,48,.85);padding:16px 20px;font-size:23px;font-weight:800;opacity:0"></div>
</div>'''
BUILD=''
RENDER='''
 const W=[[0,'4°','облачно, 4 осадка','',''],[4.5,'C4°','закручивает','💨',''],[7.0,'💥°','ВЗРЫВНО','💥','⚠️ Штормовое: взрыв мощностью C4'],[7.75,'🎧°','слышно чужого МС','🎧','⚠️ В эфире МС с вашими строчками'],[10.0,'??°','кража строчек','🌪','⚠️ Они чё, тырят? Порывы до 100%'],[11.0,'😌°','хорошо','☀️',''],[13.25,'4°','садись, четыре','📒','']];
 let c=W[0];for(const w of W)if(t>=w[0])c=w;$('tp').textContent=c[1];$('cd').textContent=c[2];$('tp').style.transform=`scale(${1+.15*pop(t,c[0],6)})`;
 const H=['☁️','🌫','🌧','⛈'];$('hr').innerHTML=H.map((h,i)=>`<div style="text-align:center;font-size:20px;font-weight:800;opacity:${t>=[0.9,1.25,1.6,2.0][i]?1:.25}">${['сейч.','+1ч','+2ч','+3ч'][i]}<div style="font-size:54px;margin:6px 0">${c[3]||h}</div>${i+1}°</div>`).join('');
 $('al').textContent=c[4];$('al').style.opacity=c[4]?1:0;
 $('c1').style.background=t>=11&&t<13.25?'linear-gradient(180deg,#ffb347,#ff7e5f)':(t>=7&&t<11?'linear-gradient(180deg,#3a3a4a,#111)':'linear-gradient(180deg,#4a90d9,#1d4a8a)');
'''
