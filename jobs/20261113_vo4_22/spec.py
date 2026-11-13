exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#3a0a5a'];PEMO=['🔎']
HTML='''<div class="card" id="c1" style="background:#000"><div id="zm" style="position:absolute;inset:0"></div><div id="lb" style="position:absolute;left:0;right:0;bottom:24px;text-align:center;font:900 30px Inter;z-index:5;text-shadow:0 3px 10px #000"></div></div>'''
BUILD=''
RENDER='''
 const L=[['🌍','Земля'],['🏙','город'],['🏠','дом'],['🧍','я'],['🫀','во мне'],['4️⃣','все четыре'],['💥','взрыв C4'],['🎤','чужой МС'],['📝','МОИ строчки'],['😌','мне хорошо'],['4️⃣','садись, четыре']];
 const K=[0,0.9,2.0,2.75,3.25,3.5,7.0,8.5,9.4,12.25,13.75];let i=0;K.forEach((k,j)=>{if(t>=k)i=j});
 const f=i<K.length-1?seg(t,K[i],K[i+1]):0;let h='';
 for(let d=0;d<2;d++){const j=i+d;if(j>=L.length)break;const s=Math.pow(9,f-d)*(d?1:1);const sc=d==0?1+f*8:f*1;
  h+=`<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) scale(${d==0?1+f*f*12:Math.max(.02,f*f)});opacity:${d==0?1-seg(f,.75,1):1};font-size:300px;line-height:1">${L[j][0]}</div>`}
 $('zm').innerHTML=h;$('lb').textContent='🔎 '+L[i][1];$('c1').style.background=`hsl(${i*33},45%,${12+f*6}%)`;
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
