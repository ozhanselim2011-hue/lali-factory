exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
BG='#0a0a0c'
HTML=''.join([f'''<div class="card" id="c{i+1}" style="background:#fff;color:#202124">
 <div style="position:absolute;left:0;right:0;top:50px;text-align:center;font-size:64px;font-weight:800;letter-spacing:-1px"><span style="color:#4285f4">G</span><span style="color:#ea4335">o</span><span style="color:#fbbc05">o</span><span style="color:#4285f4">g</span><span style="color:#34a853">l</span><span style="color:#ea4335">e</span></div>
 <div style="position:absolute;left:30px;right:30px;top:150px;height:70px;border-radius:35px;border:2px solid #dfe1e5;box-shadow:0 2px 8px rgba(0,0,0,.12);padding:0 24px;display:flex;align-items:center;font-size:27px;font-weight:600">🔍&nbsp;<span id="q{i+1}"></span><span id="cu{i+1}" style="border-left:2px solid #202124;height:30px;margin-left:2px"></span></div>
 <div id="sg{i+1}" style="position:absolute;left:40px;right:30px;top:240px;font-size:25px;line-height:2.2"></div>
</div>''' for i in range(6)])
BUILD=''
RENDER='''
 const Q=[['во мне все четыре',['во мне все четыре что это','во мне все четыре это нормально?','во мне все четыре врач рядом']],
  ['взрыв как C4',['взрыв как C4 это сколько','взрыв как C4 в зубах','взрыв как C4 как успокоиться']],
  ['слышу у эмси мои строчки',['слышу у эмси мои строчки что делать','как доказать что строчки мои','шазам нашёл мой трек у другого']],
  ['они чё тырят',['они чё тырят — в суд','авторское право рэп','сколько стоит адвокат']],
  ['мне хорошо',['почему мне так хорошо','мне хорошо это нормально','мне хорошо как продлить']],
  ['садись четыре',['садись четыре это хорошо','как исправить четыре на пять','четыре — оценка или количество']]];
 const ST=[0.9,4.5,7.75,10.0,11.0,13.25],DT=[1.6,1.2,1.0,0.4,1.0,0.4];
 for(let i=0;i<6;i++){const q=Q[i][0];const s=ST[i];const e=s+DT[i];const k=seg(t,s,e);$('q'+(i+1)).textContent=q.slice(0,Math.round(q.length*k));$('cu'+(i+1)).style.opacity=Math.sin(t*12)>0?1:0;
  $('sg'+(i+1)).innerHTML=k>=1?Q[i][1].map((x,j)=>`<div style="opacity:${seg(t,e+j*.12,e+.08+j*.12)}">🔍 <b>${x}</b></div>`).join(''):'';}
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
