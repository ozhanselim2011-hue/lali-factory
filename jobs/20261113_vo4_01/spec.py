exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#2a4a1a'];PEMO=['📍']
HTML='''
<div class="card" id="c1" style="background:#e9e4d8;color:#111">
 <svg width="600" height="690" style="position:absolute;inset:0"><g stroke="#fff" stroke-width="26" fill="none"><path d="M-20 560 L200 460 L300 300 L480 220 L640 120"/><path d="M80 -20 L200 460"/><path d="M300 300 L620 420"/></g><rect x="360" y="460" width="160" height="140" fill="#cfe3b5"/><rect x="40" y="80" width="120" height="160" fill="#cfe3b5"/>
 <path id="rt" d="M40 590 L200 460 L300 300 L480 220 L560 170" stroke="#ff3d00" stroke-width="12" fill="none" stroke-dasharray="900" stroke-dashoffset="900" stroke-linecap="round"/></svg>
 <div id="pins"></div>
 <div id="me" style="position:absolute;font-size:50px;margin:-25px 0 0 -25px">🔵</div>
 <div style="position:absolute;left:16px;right:16px;top:16px;background:#fff;border-radius:18px;padding:12px 16px;box-shadow:0 4px 14px rgba(0,0,0,.15)"><div id="nv" style="font-size:24px;font-weight:900"></div><div id="eta" style="font-size:18px;color:#666;font-weight:700"></div></div>
</div>'''
BUILD='''(function(){const P=[[200,460,'1'],[300,300,'2'],[480,220,'3'],[560,170,'4']];document.getElementById('pins').innerHTML=P.map((p,i)=>`<div id="pn${i}" style="position:absolute;left:${p[0]-24}px;top:${p[1]-60}px;width:48px;height:56px;border-radius:24px 24px 24px 4px;transform:rotate(-45deg);background:#ff3d00;opacity:0;display:flex;align-items:center;justify-content:center"><b style="transform:rotate(45deg);color:#fff;font-size:24px">${p[2]}</b></div>`).join('');})();'''
RENDER='''
 const T=[0.9,1.25,1.6,2.0];T.forEach((s,i)=>{$('pn'+i).style.opacity=t>=s?1:0;$('pn'+i).style.transform=`rotate(-45deg) scale(${eb(seg(t,s,s+.25))})`});
 const k=seg(t,2.75,13.25);$('rt').setAttribute('stroke-dashoffset',900-900*Math.min(1,seg(t,2.0,3.5)));
 const P=[[40,590],[200,460],[300,300],[480,220],[560,170]];const q=Math.min(3.999,k*4);const a=P[Math.floor(q)],b=P[Math.floor(q)+1],f=q%1;$('me').style.left=lerp(a[0],b[0],f)+'px';$('me').style.top=lerp(a[1],b[1],f)+'px';
 const N=[[0,'Маршрут построен','4 остановки'],[0.9,'Остановка 1 из 4','добавлено'],[2.75,'Во мне все четыре','маршрут через все 4'],[4.5,'Через 200 м закрутите налево','крутой поворот'],[7.0,'💥 ДТП мощностью C4','объезд'],[7.75,'Впереди: МС с вашими строчками','перекрытие'],[10.0,'Камера: они чё, тырят?','штраф'],[11.0,'Вы едете хорошо','без пробок 😌'],[13.25,'Вы прибыли. Оценка поездки: 4','садись']];
 let c=N[0];for(const n of N)if(t>=n[0])c=n;$('nv').textContent=c[1];$('eta').textContent=c[2];
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
