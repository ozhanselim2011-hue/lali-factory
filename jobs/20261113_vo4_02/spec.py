exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,4.4],[4.4,7.6],[7.6,10.95],[10.95,13.15],[13.15,99]];GLOW=['#5a1d4a','#6a3a0a','#1d3a7a','#5a1d4a','#1d5a2a'];PEMO=['📱','💥','🎧','😌','📒']
def card(i,bg,inner):
  return f'''<div class="card" id="c{i}" style="background:{bg}"><div style="position:absolute;left:14px;right:14px;top:14px;display:flex;gap:6px;z-index:6">{''.join(f'<div style="flex:1;height:5px;border-radius:3px;background:rgba(255,255,255,{1 if j<i else .35})"></div>' for j in range(5))}</div>
 <div style="position:absolute;left:18px;top:30px;display:flex;align-items:center;gap:10px;font-size:20px;font-weight:800;z-index:6"><div style="width:44px;height:44px;border-radius:50%;background:linear-gradient(45deg,#feda75,#d62976);display:flex;align-items:center;justify-content:center">🧢</div>rap_4ever <span style="opacity:.6">{i*2} ч</span></div>{inner}</div>'''
HTML=card(1,'linear-gradient(160deg,#833ab4,#fd1d1d)','<div id="s1" class="c" style="top:200px;font-size:150px;font-weight:900">4/4</div><div class="c" style="top:400px;font-size:34px;font-weight:900">во мне все четыре 🔥</div><div id="pl1" class="c" style="top:470px"></div>')+\
 card(2,'linear-gradient(160deg,#f77737,#000)','<div id="s2" class="c" style="top:180px;font-size:200px">🦷</div><div class="c" style="top:450px;font-size:34px;font-weight:900;background:#fff;color:#000;margin:0 80px;padding:8px;border-radius:10px">закрутил 💥 C4</div>')+\
 card(3,'linear-gradient(160deg,#405de6,#000)','<div class="c" style="top:150px;font-size:120px">🎧</div><div style="position:absolute;left:40px;right:40px;top:330px;background:#fff;color:#111;border-radius:22px;padding:18px;font-size:24px;font-weight:800">🔁 <b>mc_kto_to</b> отметил(а) вас: <i>«мои строчки»</i> 🤔</div><div id="q3" style="position:absolute;left:60px;right:60px;top:470px;background:#fff;color:#111;border-radius:22px;padding:16px;text-align:center;font-size:24px;font-weight:900;opacity:0">ОПРОС: они чё, тырят?<div style="display:flex;gap:10px;margin-top:10px"><div style="flex:1;background:#ff375f;color:#fff;border-radius:12px;padding:8px">ДА 97%</div><div style="flex:1;background:#eee;border-radius:12px;padding:8px">нет 3%</div></div></div>')+\
 card(4,'linear-gradient(160deg,#fcaf45,#e1306c)','<div class="c" style="top:190px;font-size:170px">😌</div><div class="c" style="top:430px;font-size:40px;font-weight:900">мне хорошо</div><div id="hs4" style="position:absolute;inset:0"></div>')+\
 card(5,'linear-gradient(160deg,#1d5a2a,#000)','<div class="c" style="top:150px;font-size:34px;font-weight:900">ОЦЕНИТЕ МОЙ ТРЕК</div><div id="sl5" style="position:absolute;left:60px;right:60px;top:260px;height:20px;border-radius:10px;background:rgba(255,255,255,.3)"><div id="sf5" style="height:100%;border-radius:10px;background:#30d158;width:0"></div></div><div id="sn5" class="c" style="top:330px;font-size:180px;font-weight:900">0</div>')
BUILD=''
RENDER='''
 $('s1').textContent=[0.9,1.25,1.6,2.0].filter(x=>t>=x).length+'/4';$('s1').style.transform=`scale(${1+.2*pop(t,3.5,6)})`;
 $('s2').textContent=t>=7?'💥':'🦷';$('s2').style.transform=`rotate(${t<7?t*200:0}deg) scale(${1+.5*pop(t,7,6)})`;
 $('q3').style.opacity=seg(t,10.0,10.15);
 let h='';for(let i=0;i<12;i++){const s=11.0+i*.18;if(t>=s)h+=`<div style="position:absolute;left:${80+rnd(i)*420}px;top:${600-(t-s)*260}px;font-size:${40+rnd(i+3)*30}px;opacity:${1-seg(t,s+1.2,s+1.8)}">${['❤️','🔥','😍'][i%3]}</div>`}$('hs4').innerHTML=h;
 const v=t>=13.75?80:lerp(0,100,seg(t,13.25,13.6));$('sf5').style.width=v+'%';$('sn5').textContent=t>=13.75?'4':Math.round(v/20);
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
