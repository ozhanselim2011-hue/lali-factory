exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#2a0a5a'];PEMO=['🔤']
HTML='''<div class="card" id="c1" style="background:#000"><div id="ty" style="position:absolute;inset:0"></div></div>'''
BUILD=''
RENDER='''
 const W=[];LINES.forEach(l=>l.forEach(w=>W.push(w)));let i=-1;W.forEach((w,k)=>{if(t>=w[1])i=k});
 const pal=['#ff375f','#ffd60a','#30d158','#64d2ff','#bf5af2','#ff9f0a'];let h='';
 if(i>=0){const w=W[i][0].replace(/[,?]/g,'').toUpperCase(),k=seg(t,W[i][1],W[i][1]+.2),col=pal[i%6],r=(i%3-1)*8;
  const big=w=='ЧЕТЫРЕ'||w=='C4'||w=='4';const fs=Math.min(big?140:130,Math.floor(540/(w.length*.68)));
  if(w=='ЧЕТЫРЕ'&&t<4)h=`<div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr;align-items:center;justify-items:center">${[0,1,2,3].map(j=>`<div style="font-size:220px;font-weight:900;color:${pal[j]};transform:scale(${eb(seg(t,W[i][1]+j*.06,W[i][1]+j*.06+.25))})">4</div>`).join('')}</div>`;
  else h=`<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:${fs}px;font-weight:900;color:${col};letter-spacing:-3px;transform:rotate(${r}deg) scale(${lerp(2.2,1,eo(k))});opacity:${k};text-align:center;line-height:.95">${w}</div>`;
  if(w=='C4')h+=`<div style="position:absolute;inset:0;background:radial-gradient(circle,#fff,#ff9f0a 30%,transparent 70%);opacity:${1-seg(t,7.0,7.5)}"></div>`;}
 $('ty').innerHTML=h;$('c1').style.background=i>=0&&W[i][0]=='C4'?'#2a0a00':'#000';
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
