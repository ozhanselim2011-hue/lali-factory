exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#3a1d5a'];PEMO=['💬']
HTML='''
<div class="card" id="c1" style="background:#1a1d21;color:#d1d2d3">
 <div style="position:absolute;left:0;right:0;top:0;height:70px;background:#3f0e40;display:flex;align-items:center;padding:0 24px;font-size:26px;font-weight:900;color:#fff"># рабочий-чат <span style="margin-left:auto;font-size:18px;opacity:.7">👥 4</span></div>
 <div id="ms" style="position:absolute;left:20px;right:20px;bottom:20px;display:flex;flex-direction:column;gap:14px"></div>
</div>'''
BUILD=''
RENDER='''
 const M=[[0.9,'🧑‍💼','Начальник','Сколько задач на тебе сейчас?'],[2.75,'😎','Я','во мне все четыре'],[4.5,'👩‍💻','Тимлид','а дедлайн по проекту?'],[6.25,'😎','Я','взрыв, как C4 💥'],[7.75,'🎧','HR','на созвоне кто-то читал твой отчёт как свой'],[10.0,'😎','Я','они чё, тырят?'],[11.0,'🧑‍💼','Начальник','премия одобрена ✅'],[12.25,'😎','Я','делает хорошо мне 😌'],[13.25,'🧑‍💼','Начальник','оценка за квартал: 4. садись.']];
 const vis=M.filter(m=>t>=m[0]).slice(-5);
 $('ms').innerHTML=vis.map(m=>`<div style="display:flex;gap:12px;transform:translateY(${(1-eb(seg(t,m[0],m[0]+.25)))*30}px);opacity:${seg(t,m[0],m[0]+.15)}"><div style="width:52px;height:52px;border-radius:10px;background:#2c2d30;display:flex;align-items:center;justify-content:center;font-size:30px;flex:none">${m[1]}</div><div><div style="font-size:19px;font-weight:900;color:${m[2]=='Я'?'#36c5f0':'#fff'}">${m[2]} <span style="font-weight:600;color:#888;font-size:15px">10:4${Math.floor(m[0])%10}</span></div><div style="font-size:24px;font-weight:600;line-height:1.25">${m[3]}</div></div></div>`).join('');
'''
