exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#5a4a0a'];PEMO=['😀']
HTML='''<div class="card" id="c1" style="background:#fffbe6;color:#111"><div class="hdr" style="color:#b08a00">песня в эмодзи</div><div id="em" style="position:absolute;left:20px;right:20px;top:90px;bottom:20px;display:flex;flex-wrap:wrap;align-content:flex-start;gap:6px;font-size:76px"></div></div>'''
BUILD=''
RENDER='''
 const E=[[0.9,'❓'],[1.25,'❓'],[1.6,'❓'],[2.0,'❓'],[2.75,'🫵'],[3.25,'💯'],[3.5,'4️⃣'],[4.5,'🦷'],[5.25,'🪵'],[5.75,'🌀'],[6.25,'💥'],[7.0,'🧨'],[7.75,'👂'],[8.5,'🎤'],[9.4,'📝'],[10.0,'👀'],[10.5,'🥷'],[11.0,'🐕'],[11.5,'👉'],[12.25,'😌'],[12.9,'🙋'],[13.25,'🪑'],[13.75,'4️⃣']];
 $('em').innerHTML=E.filter(e=>t>=e[0]).map(e=>`<span style="display:inline-block;transform:scale(${eb(seg(t,e[0],e[0]+.25))}) rotate(${(1-seg(t,e[0],e[0]+.25))*-40}deg);">${e[1]}</span>`).join('');
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
