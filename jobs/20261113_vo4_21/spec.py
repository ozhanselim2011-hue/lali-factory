exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#5a2a0a'];PEMO=['🔍']
HTML='''<div class="card" id="c1" style="background:#8a5a32;background-image:radial-gradient(#7a4a22 2px,transparent 2px);background-size:16px 16px">
 <svg id="th" width="600" height="690" style="position:absolute;inset:0;z-index:3"></svg><div id="nt" style="position:absolute;inset:0;z-index:2"></div>
 <div style="position:absolute;left:0;right:0;bottom:16px;text-align:center;z-index:4"><span style="background:#111;color:#ffd60a;font:900 24px 'JetBrains Mono';padding:6px 14px">ДЕЛО №4 · «ВО МНЕ ВСЕ ЧЕТЫРЕ»</span></div></div>'''
BUILD=''
RENDER='''
 const N=[[0.9,60,40,'🕵️','подозреваемый'],[2.75,330,30,'4️⃣','улика: «все четыре»'],[4.5,40,250,'🦷','палка в зубах'],[7.0,340,230,'💥','взрыв C4'],[7.75,190,400,'🎤','МС-подражатель'],[10.0,380,430,'📝','украденные строчки'],[12.25,60,470,'😌','мотив: хорошо']];
 const vis=N.filter(n=>t>=n[0]);
 $('nt').innerHTML=vis.map((n,i)=>`<div style="position:absolute;left:${n[1]}px;top:${n[2]}px;width:180px;background:${i%2?'#fff8b0':'#fff'};padding:10px;box-shadow:0 6px 14px rgba(0,0,0,.4);transform:rotate(${(rnd(i)-.5)*12}deg) scale(${eb(seg(t,n[0],n[0]+.25))});text-align:center;color:#111"><div style="width:18px;height:18px;border-radius:50%;background:#d0021b;margin:-18px auto 4px"></div><div style="font-size:70px">${n[3]}</div><div style="font:800 16px Inter">${n[4]}</div></div>`).join('');
 let s='';for(let i=1;i<vis.length;i++){const a=vis[i-1],b=vis[i];const k=seg(t,b[0],b[0]+.4);const x1=a[1]+90,y1=a[2]+2,x2=b[1]+90,y2=b[2]+2;s+=`<line x1="${x1}" y1="${y1}" x2="${lerp(x1,x2,k)}" y2="${lerp(y1,y2,k)}" stroke="#d0021b" stroke-width="4"/>`}
 if(t>=13.75)s+=`<text x="300" y="370" text-anchor="middle" font-size="120" font-weight="900" fill="#d0021b" transform="rotate(-12 300 340)" opacity="${seg(t,13.75,13.85)}">ВИНОВЕН: 4</text>`;$('th').innerHTML=s;
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
