exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]]
GLOW=['#7a0a0a']
PEMO=['📺']
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#0a1a3a,#02060f)">
 <div style="position:absolute;left:24px;top:24px;background:#d0021b;color:#fff;font-weight:900;font-size:24px;padding:6px 14px;border-radius:6px;z-index:6">🔴 СРОЧНО</div>
 <div style="position:absolute;right:24px;top:24px;color:#fff;font-weight:800;font-size:22px;z-index:6" class="mono" id="cl">LIVE 00:00</div>
 <div id="pic" style="position:absolute;left:40px;right:40px;top:80px;height:300px;border-radius:16px;background:#1a2a4a;display:flex;align-items:center;justify-content:center;font-size:170px"></div>
 <div style="position:absolute;left:0;right:0;top:400px;height:130px;background:#fff;color:#111;padding:14px 22px;z-index:5"><div style="font-size:18px;font-weight:900;color:#d0021b">ЭКСТРЕННЫЙ ВЫПУСК</div><div id="hl" style="font-size:30px;font-weight:900;line-height:1.15"></div></div>
 <div style="position:absolute;left:0;right:0;top:530px;height:44px;background:#d0021b;overflow:hidden;z-index:5"><div id="tk" style="white-space:nowrap;color:#fff;font-weight:800;font-size:22px;line-height:44px">ЭКСПЕРТЫ ПОТРЯСЕНЫ • УЧЁНЫЕ НЕ МОГУТ ОБЪЯСНИТЬ • ВО МНЕ ВСЕ ЧЕТЫРЕ • ЭКСПЕРТЫ ПОТРЯСЕНЫ • УЧЁНЫЕ НЕ МОГУТ ОБЪЯСНИТЬ • ВО МНЕ ВСЕ ЧЕТЫРЕ • ЭКСПЕРТЫ ПОТРЯСЕНЫ •</div></div>
</div>
'''
BUILD=''
RENDER='''
 const H=[[0,'4️⃣','В человеке обнаружены сразу ЧЕТЫРЕ'],[4.5,'💥','В районе зубов прогремел взрыв мощностью C4'],[7.75,'🎧','Рэпер услышал свои строчки у другого МС'],[10.0,'©️','Плагиат года: «они чё, тырят?»'],[11.0,'😌','Источник сообщает: ему хорошо'],[13.25,'📒','Итоговая оценка: ЧЕТЫРЕ']];
 let c=H[0];for(const h of H)if(t>=h[0])c=h;$('pic').textContent=c[1];$('hl').textContent=c[2];$('pic').style.transform=`scale(${1+.12*pop(t,c[0],6)})`;
 $('tk').style.transform=`translateX(${-((t*120)%900)}px)`;$('cl').textContent='LIVE 00:'+String(Math.floor(t)).padStart(2,'0');
'''
