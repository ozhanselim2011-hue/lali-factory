exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,4.4],[4.4,7.6],[7.6,10.95],[10.95,13.15],[13.15,99]];GLOW=['#1d3a7a','#6a3a0a','#1d3a7a','#5a1d4a','#1d5a2a'];PEMO=['❓','❓','❓','❓','❓']
def rb(i,pics,ans):
  return f'''<div class="card" id="c{i}" style="background:#f5f5f0;color:#111"><div class="hdr" style="color:#888">Ребус №{i}</div>
 <div style="position:absolute;left:20px;right:20px;top:120px;height:260px;display:flex;align-items:center;justify-content:center;gap:10px;font-size:90px;font-weight:900">{pics}</div>
 <div class="c" style="top:420px;font-size:28px;font-weight:800;color:#888">угадай строчку</div>
 <div id="a{i}" class="c" style="top:480px;font-size:34px;font-weight:900;color:#0a84ff;opacity:0;padding:0 20px">{ans}</div></div>'''
HTML=rb(1,'🫵<span style="font-size:60px">+</span>🏠<span style="font-size:60px">+</span>4️⃣','«ВО МНЕ ВСЕ ЧЕТЫРЕ»')+rb(2,'🦷<span style="font-size:60px">+</span>🪵<span style="font-size:60px">=</span>💥','«ВЗРЫВ, КАК C4»')+rb(3,'👂<span style="font-size:60px">+</span>🎤<span style="font-size:60px">+</span>📝','«СЛЫШУ У ЭМСИ МОИ СТРОЧКИ»')+rb(4,'🐕<span style="font-size:60px">→</span>😌','«ДЕЛАЕТ ХОРОШО МНЕ»')+rb(5,'🪑<span style="font-size:60px">+</span>4️⃣','«САДИСЬ, ЧЕТЫРЕ»')
BUILD=''
RENDER='''
 [[1,3.25],[2,6.6],[3,9.4],[4,12.25],[5,13.75]].forEach(([i,s])=>{$('a'+i).style.opacity=seg(t,s,s+.1);$('a'+i).style.transform=`scale(${1+.3*pop(t,s,7)})`});
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
