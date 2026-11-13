exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#0a4a7a'];PEMO=['⭕']
HTML='''<div class="card" id="c1" style="background:#0e1621"><div style="position:absolute;left:0;right:0;top:0;height:64px;background:#17212b;display:flex;align-items:center;padding:0 20px;font:800 22px Inter">← Рэп-тусовка <span style="margin-left:auto;font-size:16px;color:#6c7883">4 участника</span></div><div id="ms" style="position:absolute;left:16px;right:16px;bottom:16px;display:flex;flex-direction:column;gap:12px"></div></div>'''
BUILD=''
RENDER='''
 const M=[[0.9,1,'😮','0:03'],[2.75,0,'4️⃣','0:02'],[4.5,1,'🦷','0:04'],[7.0,0,'💥','0:01'],[7.75,1,'🎧','0:03'],[10.0,0,'😡','0:02'],[11.0,1,'😌','0:03'],[13.25,0,'4️⃣','0:01']];
 const v=M.filter(m=>t>=m[0]).slice(-3);
 $('ms').innerHTML=v.map((m,j)=>{const last=j==v.length-1;const sz=last?250:150;const p=last?seg(t,m[0],m[0]+1.2):1;return `<div style="align-self:${m[1]?'flex-start':'flex-end'};position:relative;width:${sz}px;height:${sz}px;transform:scale(${eb(seg(t,m[0],m[0]+.3))})"><svg width="${sz}" height="${sz}" style="position:absolute;inset:0;transform:rotate(-90deg)"><circle cx="${sz/2}" cy="${sz/2}" r="${sz/2-4}" fill="none" stroke="#5288c1" stroke-width="6" stroke-dasharray="${Math.PI*(sz-8)}" stroke-dashoffset="${Math.PI*(sz-8)*(1-p)}"/></svg><div style="position:absolute;inset:10px;border-radius:50%;background:radial-gradient(circle at 40% 35%,${m[1]?'#2b5278':'#5a2b78'},#111);display:flex;align-items:center;justify-content:center;font-size:${sz*.5}px;transform:rotate(${Math.sin(t*6+j)*6}deg)">${m[2]}</div><div style="position:absolute;left:8px;bottom:0;background:rgba(0,0,0,.6);border-radius:8px;padding:1px 8px;font:700 15px Inter">${m[3]}</div></div>`}).join('');
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
