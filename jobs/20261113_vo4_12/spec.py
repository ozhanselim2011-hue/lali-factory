exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#0a3a7a'];PEMO=['🔧']
HTML='''
<div class="card" id="c1" style="background:#fff;color:#111">
 <div style="position:absolute;left:24px;right:24px;top:20px;display:flex;justify-content:space-between;font-size:34px;font-weight:900"><span style="background:#0058a3;color:#ffdb00;padding:2px 14px;border-radius:4px">ВОМНЕ</span><span id="sn" style="border:4px solid #111;border-radius:50%;width:56px;height:56px;display:flex;align-items:center;justify-content:center">1</span></div>
 <div id="pic" style="position:absolute;left:40px;right:40px;top:110px;height:380px;display:flex;align-items:center;justify-content:center;gap:20px;font-size:100px"></div>
 <div id="cp" style="position:absolute;left:24px;right:24px;bottom:30px;text-align:center;font-size:26px;font-weight:800;font-family:'JetBrains Mono'"></div>
</div>'''
BUILD=''
RENDER='''
 const box=n=>`<div style="width:110px;height:110px;border:5px solid #111;display:flex;align-items:center;justify-content:center;font-size:60px;font-weight:900">${n}</div>`;
 const S=[[0,1,()=>[1,2,3,4].filter((x,i)=>t>=[0.9,1.25,1.6,2.0][i]).map(box).join(''),'4× детали'],[2.75,2,()=>'<div style="font-size:150px">🧍</div><div style="font-size:60px">+ 4×</div>','вставить все 4 внутрь'],[4.5,3,()=>`<div style="font-size:130px;transform:rotate(${t*400}deg)">🔧</div>`,'закрутить (ключ в зубах)'],[7.0,4,()=>'<div style="font-size:180px">💥</div>','⚠️ не перекручивать'],[7.75,5,()=>'<div style="font-size:120px">🧍</div><div style="font-size:60px">≠</div><div style="font-size:120px">🕵️</div>','строчки — только ваши'],[10.0,6,()=>'<div style="font-size:150px">🚫</div>','✕ не тырить'],[11.0,7,()=>'<div style="font-size:150px">😌</div>','готово. хорошо.'],[13.25,8,()=>'<div style="font-size:180px;font-weight:900">4</div>','собрано на 4/5']];
 let c=S[0];for(const s of S)if(t>=s[0])c=s;$('sn').textContent=c[1];$('pic').innerHTML=c[2]();$('cp').textContent=c[3];$('pic').style.transform=`scale(${1+.1*pop(t,c[0],6)})`;
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
