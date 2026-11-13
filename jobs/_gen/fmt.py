# Универсальные полноэкранные форматы с Лали (без смайликов, без фона вокруг).
# spec.py:  exec(open('/home/user/lali-factory/jobs/_gen/fmt.py').read()); SRC='20261110_tt...'; KIND='cut'; MAKE()
import os
def MAKE():
  g=globals();src={'HELPERS':HELPERS};exec(open(f'/home/user/lali-factory/jobs/{g["SRC"]}/spec.py').read(),src)
  for k in ['LINES','START','DUR','FADE','END','SONG']:g[k]=src[k]
  S=float(src['START']);g['SC']=[[S-0.3,9999]];g['PEMO']=[''];g['GLOW']=['#000']
  g['SUBX']='text-transform:uppercase;font-size:58px;-webkit-text-stroke:5px #000;paint-order:stroke fill;letter-spacing:-1px'
  g['CSS']='''.card{left:0!important;top:0!important;width:1080px!important;height:1080px!important;margin:0!important;border-radius:0!important;box-shadow:none!important}
#glow,#pts,#vign,#grain{display:none!important}.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}
.ab{position:absolute}.big{position:absolute;left:0;right:0;text-align:center;font-weight:900;letter-spacing:-4px;line-height:.9}.ol{-webkit-text-stroke:6px #000;paint-order:stroke fill}'''
  K=g['KIND'];h,b,r=F[K];g['HTML']='<div class="card" id="c1" style="background:#000">'+h+'</div>'
  if K=='kar':g['SUBFROM']=99999
  g['BUILD']=open(HELPERS).read()+COMMON_JS+b
  g['RENDER']='{'+PRE+r+'}'
COMMON_JS='''
const dn=(t,k=12.57,a=1)=>{const q=Math.sin(t*k);return {aL:(110+q*40)*a,aR:(-110+q*40)*a,lL:q*14*a,lR:-q*14*a,hd:q*8*a,bob:-Math.abs(q)*14*a}};
const MV=[t=>dn(t),t=>{const q=Math.sin(t*12.57);return {aL:90,aR:-90,lL:q*25,lR:-q*25,hd:q*10,bob:-Math.abs(q)*10}},t=>({aL:150+Math.sin(t*6)*15,aR:-150+Math.sin(t*6)*15,hd:-8,bob:Math.sin(t*3)*6}),
 t=>{const q=Math.sin(t*6.28);return {aL:8+Math.max(0,q)*150,aR:-8-Math.max(0,-q)*150,hd:q*8,bob:-Math.abs(q)*8}},t=>({aL:8,aR:-90+Math.sin(t*12.57)*20,hd:-6,lL:Math.sin(t*12.57)*10,bob:-Math.abs(Math.sin(t*12.57))*8}),
 t=>{const q=Math.sin(t*9.4);return {aL:120,aR:-120,lL:q*30,lR:-q*30,hd:q*12,bob:-Math.abs(q)*20}}];
const ACC=[{aL:150,aR:-8,open:1},{aL:8,aR:-150,open:1},{aL:150,aR:-150,open:1},{aL:90,aR:-90,lL:-25,lR:25,open:1}];
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;const c=e.dataset.c?e.dataset.c.split(','):['#64d2ff','#ff8ac4','#ff2d78'];e.innerHTML=CH(p,...c);});})();
'''
PRE='''
 const W=LINES.flat();let wi=-1;W.forEach((w,k)=>{if(t>=w[1])wi=k});let li=-1;LINES.forEach((L,k)=>{if(t>=L[0][1]-.05)li=k});
 const wb=wi<0?0:pop(t,W[wi][1],9),ls=li<0?-9:LINES[li][0][1],lb=pop(t,ls,6),fin=t>=END[0]-0.5;
 const word=wi<0?'':W[wi][0].replace(/[,?!.«»—]/g,'').toUpperCase();
 const isLast=li<0?false:(wi>=0&&W[wi]===LINES[li][LINES[li].length-1]);
 let MO=li<0?{aL:8,aR:-8}:MV[li%MV.length](t);if(wb>.35&&wi%4==0)MO=ACC[(wi>>2)%4];if(fin)MO={aL:150,aR:-150,open:1};
 const ce=$('c1');ce.style.opacity=1;ce.style.filter='none';ce.style.transform=`scale(${1+.025*wb+.04*lb})`;
'''
F={}
OUT='filter:drop-shadow(8px 0 0 #fff) drop-shadow(-8px 0 0 #fff) drop-shadow(0 8px 0 #fff) drop-shadow(0 -8px 0 #fff) drop-shadow(0 30px 30px rgba(0,0,0,.4))'
F['cut']=(f'<div id="bg" class="ab" style="inset:0"></div><div id="wd" class="big" style="color:transparent;-webkit-text-stroke:7px rgba(255,255,255,.95)"></div><div class="ch" data-p="a" style="{OUT}"></div>','','''
 const P=['#ff2d55','#ffd60a','#30d158','#0a84ff','#bf5af2','#ff9f0a','#00c7be','#ff375f'];$('bg').style.background=wi<0?'#111':P[wi%8];
 const fs=Math.min(330,Math.floor(1000/(Math.max(2,word.length)*.64)));$('wd').textContent=word;$('wd').style.fontSize=fs+'px';$('wd').style.top=(600-fs*.5)+'px';$('wd').style.transform=`scale(${1+.25*wb}) rotate(${(wi%3-1)*5}deg)`;
 place('a',540,1070,2.3+.12*wb,wi%2==1);pose('a',MO);
''')
F['neon']=('<div id="bg" class="ab" style="inset:0"></div><div id="lz" class="ab" style="inset:0"></div><div class="ch" data-p="a"></div>','','''
 const h=(li*67+t*30)%360,st=lb>.55&&li%3==1;let bg=`radial-gradient(circle at 50% 62%,hsl(${h},100%,${55+25*wb}%) 0%,hsl(${(h+70)%360},100%,28%) 38%,#000 78%)`;if(st)bg=(Math.floor(t*16)%2)?'#fff':'#000';$('bg').style.background=bg;
 let L='';if(!st)for(let i=0;i<8;i++){const a=22+(i%4)*13+Math.sin(t*2+i)*14,c=`hsl(${(h+i*45)%360},100%,60%)`;L+=`<div class="ab" style="left:${i<4?0:1080}px;top:1080px;width:1700px;height:6px;background:${c};box-shadow:0 0 24px ${c};transform-origin:0 50%;transform:rotate(${i<4?-a:180+a}deg);opacity:${.45+.55*wb}"></div>`}$('lz').innerHTML=L;
 $('ch_a').style.filter=`brightness(0) drop-shadow(0 0 ${18+30*wb}px hsl(${h},100%,70%))`;place('a',540,1090,2.7,false);pose('a',MO);
''')
F['dance']=('''<div id="nb" class="big" style="top:200px;font-size:300px;color:rgba(255,255,255,.13)"></div>
<div class="ab" style="left:-300px;right:-300px;top:640px;height:700px;transform:perspective(700px) rotateX(58deg);transform-origin:50% 0"><div id="fl" style="display:grid;grid-template-columns:repeat(10,1fr);grid-template-rows:repeat(6,1fr);height:100%;gap:8px"></div></div>
<div id="mb" class="ab" style="left:475px;top:175px;width:130px;height:130px;border-radius:50%;background:repeating-conic-gradient(#eee 0 12deg,#777 12deg 24deg);box-shadow:0 0 60px rgba(255,255,255,.7)"></div><div id="sp" class="ab" style="inset:0"></div><div class="ch" data-p="a"></div>''','','''
 const fs=Math.min(300,Math.floor(1000/(Math.max(2,word.length)*.64)));$('nb').textContent=word;$('nb').style.fontSize=fs+'px';
 const wh=lb>.6&&li%3==2;let f='';for(let i=0;i<60;i++){const on=rnd(i*3+Math.floor(t*4))>.55;const c=wh?'#fff':(on?`hsl(${(i*37+Math.floor(t*4)*60)%360},100%,60%)`:'#15101f');f+=`<div style="background:${c};box-shadow:${on||wh?'0 0 30px '+c:'none'}"></div>`}$('fl').innerHTML=f;
 $('mb').style.transform=`rotate(${t*90}deg)`;let s='';for(let i=0;i<26;i++){const a=i*0.9+t*1.4;s+=`<div class="ab" style="left:${540+Math.cos(a)*(250+rnd(i)*300)}px;top:${400+Math.sin(a*1.3)*(150+rnd(i+5)*120)}px;width:8px;height:8px;border-radius:50%;background:#fff;box-shadow:0 0 12px #fff;opacity:${.4+.6*Math.abs(Math.sin(t*5+i))}"></div>`}$('sp').innerHTML=s;
 $('c1').style.background='#0a0614';place('a',540,960,2.2,li%2==1&&Math.floor(t*4)%2==1);pose('a',MO);
''')
MONO="font-family:'JetBrains Mono';color:#fff;text-shadow:3px 3px 0 #000;z-index:13"
CHF='filter:drop-shadow(6px 0 0 rgba(255,0,0,.55)) drop-shadow(-6px 0 0 rgba(0,255,255,.55))'
F['vhs']=(f'''<div class="ab" style="inset:0;background:repeating-linear-gradient(90deg,#6b5442 0 60px,#5e4a3a 60px 120px)"></div>
<div class="ab" style="left:660px;top:260px;width:300px;height:240px;background:linear-gradient(#9fd3ff,#cfe9ff);border:14px solid #3a2a1e"></div><div class="ab" style="left:0;right:0;top:770px;bottom:0;background:#4a3a2a"></div>
<div class="ab" style="left:110px;top:600px;width:860px;height:240px;background:#7a2a2a;border-radius:50px 50px 20px 20px;box-shadow:inset 0 -30px 0 #5a1a1a"></div>
<div class="ch" data-p="a" style="{CHF}"></div><div id="bsod" class="ab" style="inset:0;background:#0018a8;opacity:0;z-index:7"></div><div id="v4" class="big" style="top:420px;font:400 150px 'JetBrains Mono';color:#fff;opacity:0;z-index:8"></div>
<div class="ab" style="inset:0;background:repeating-linear-gradient(0deg,rgba(0,0,0,.22) 0 2px,transparent 2px 5px);z-index:10"></div><div id="trk" class="ab" style="left:0;right:0;height:60px;background:linear-gradient(rgba(255,255,255,0),rgba(255,255,255,.3),rgba(255,255,255,0));z-index:11"></div>
<div id="nz" class="ab" style="inset:0;z-index:12"></div><div id="osd" class="ab" style="left:60px;top:250px;font-size:56px;{MONO}">PLAY</div><div id="tc" class="ab" style="right:60px;top:256px;font-size:40px;{MONO}"></div>
<div class="ab" style="left:60px;top:890px;font-size:40px;{MONO}">13 НОЯ 2006</div>''','','''
 const rt=t-(SC[0][0]+.3);$('osd').textContent=fin?'STOP':'PLAY';$('tc').textContent='SP 0:00:'+String(Math.floor(rt)).padStart(2,'0');$('trk').style.top=((t*260)%1200-100)+'px';
 const gl=(lb>.45&&li%2==1&&li>0)||(t>=END[0]-.5&&t<END[0]-.25);let n='';if(gl)for(let i=0;i<16;i++)n+=`<div class="ab" style="left:0;right:0;top:${rnd(i+Math.floor(t*30))*1080}px;height:${10+rnd(i+3)*50}px;background:rgba(255,255,255,${.2+rnd(i)*.5});transform:translateX(${(rnd(i+9)-.5)*120}px)"></div>`;$('nz').innerHTML=n;
 if(gl)ce.style.transform+=` translateX(${Math.sin(t*80)*24}px) skewX(${Math.sin(t*50)*5}deg)`;
 const lw=W[W.length-1][0].replace(/[,?!.«»—]/g,'').toUpperCase();$('bsod').style.opacity=t>=END[0]-.25?1:0;$('v4').style.opacity=t>=END[0]-.25?1:0;$('v4').textContent=lw;$('v4').style.fontSize=Math.min(150,Math.floor(900/(lw.length*.62)))+'px';
 place('a',540,900,1.9,false);pose('a',MO);
''')
F['concert']=('''<div id="scr" class="ab" style="left:250px;top:180px;width:580px;height:190px;background:#0a0a14;border:8px solid #222;display:flex;align-items:center;justify-content:center;font:900 130px Inter;letter-spacing:-4px;color:#fff;overflow:hidden"></div>
<div id="spt" class="ab" style="inset:0"></div><div class="ab" style="left:0;right:0;top:760px;height:140px;background:linear-gradient(#2a1d3a,#120c1a)"></div>
<div id="pyL" class="ab" style="left:50px;width:130px;top:760px;height:0;background:linear-gradient(0deg,#ff3b00,#ffd60a 55%,rgba(255,255,255,0));border-radius:65px 65px 0 0"></div><div id="pyR" class="ab" style="right:50px;width:130px;top:760px;height:0;background:linear-gradient(0deg,#ff3b00,#ffd60a 55%,rgba(255,255,255,0));border-radius:65px 65px 0 0"></div>
<div class="ch" data-p="a"></div><div id="crowd" class="ab" style="left:0;right:0;top:850px;height:230px;z-index:6"></div>''','','''
 $('c1').style.background='radial-gradient(ellipse at 50% 30%,#2a1a4a,#07050f 70%)';
 $('scr').textContent=word;$('scr').style.fontSize=Math.min(130,Math.floor(540/(Math.max(1,word.length)*.66)))+'px';$('scr').style.transform=`scale(${1+.08*wb})`;$('scr').style.color=isLast?'#ffd60a':'#fff';
 const SX=[110,380,700,970];let sp='';SX.forEach((x,i)=>{if(li>=0){const a=Math.sin(t*1.6+i*1.3)*25;const c=i%2?'120,200,255':'255,230,150';sp+=`<div class="ab" style="left:${x-170}px;top:170px;width:340px;height:900px;clip-path:polygon(45% 0,55% 0,100% 100%,0 100%);background:linear-gradient(rgba(${c},${.35+.3*wb}),rgba(${c},0) 85%);transform-origin:50% 0;transform:rotate(${a}deg)"></div>`}});$('spt').innerHTML=sp;
 const pk=li%3==2?Math.max(0,Math.sin(seg(t,ls,ls+.9)*Math.PI))*620:0;$('pyL').style.height=$('pyR').style.height=pk+'px';$('pyL').style.top=$('pyR').style.top=(760-pk)+'px';
 let cr='';for(let i=0;i<20;i++){const x=i*56-10+(i%2)*20,j=Math.abs(Math.sin(t*12.57+i))*30*(.6+rnd(i)*.4);const y=(i%2?40:0)-j;const arm=i%3!=1?`<div style="position:absolute;left:${i%2?0:56}px;top:-70px;width:16px;height:90px;border-radius:8px;background:#000;transform:rotate(${i%2?-20:20}deg)"></div>`:'';
  cr+=`<div style="position:absolute;left:${x}px;top:${y}px">${arm}<div style="width:76px;height:76px;border-radius:50%;background:#000"></div><div style="width:110px;height:200px;margin-left:-17px;border-radius:50px 50px 0 0;background:#000"></div></div>`}$('crowd').innerHTML=cr;
 place('a',540,800,1.5,false);pose('a',MO);
''')
F['kar']=('''<div class="ab" style="inset:0;background:radial-gradient(circle at 50% 30%,#3a1a6a,#0a0418 75%)"></div><div id="sp" class="ab" style="inset:0"></div>
<div class="ab" style="left:60px;right:60px;top:130px;height:480px;background:#06060c;border:14px solid #222;border-radius:30px;box-shadow:0 0 80px rgba(120,80,255,.5)"></div>
<div id="kl" class="ab" style="left:100px;right:100px;top:200px;height:340px;display:flex;flex-direction:column;justify-content:center;gap:24px;z-index:3"></div>
<div id="bl" class="ab" style="width:34px;height:34px;border-radius:50%;background:#ffd60a;box-shadow:0 0 20px #ffd60a;z-index:4"></div>
<div id="scb" class="ab" style="left:80px;top:650px;font:900 44px 'JetBrains Mono';color:#ffd60a;text-shadow:0 0 20px #ffb000">0000</div><div class="ch" data-p="a"></div>''','','''
 const cur=Math.max(0,li),nx=cur+1;const ln=(k,on)=>k<LINES.length?`<div style="text-align:center;font:900 ${on?64:44}px Inter;letter-spacing:-1px;line-height:1.15;color:${on?'#fff':'rgba(255,255,255,.35)'}">${LINES[k].map(([w,s],j)=>`<span id="${on?'kw'+j:''}" style="color:${on&&t>=s?'#ff2d78':''};text-shadow:${on&&t>=s?'0 0 18px #ff2d78':'none'}">${w}</span>`).join(' ')}</div>`:'';
 $('kl').innerHTML=ln(cur,1)+ln(nx,0);
 let bx=-99,by=0;if(li>=0){const L=LINES[cur];let j=0;L.forEach(([w,s],k)=>{if(t>=s)j=k});const e=$('kw'+j);if(e){const r=e.getBoundingClientRect(),c=$('c1').getBoundingClientRect();const nxt=j+1<L.length?L[j+1][1]:L[j][1]+.4;const p=seg(t,L[j][1],nxt);bx=r.left-c.left+r.width/2-17;by=r.top-c.top-44-Math.sin(p*Math.PI)*30;}}
 $('bl').style.left=bx+'px';$('bl').style.top=by+'px';$('scb').textContent='СЧЁТ '+String(Math.min(9999,Math.max(0,wi+1)*137)).padStart(4,'0');
 let s='';for(let i=0;i<20;i++)s+=`<div class="ab" style="left:${rnd(i)*1080}px;top:${rnd(i+7)*1080}px;width:6px;height:6px;border-radius:50%;background:#fff;opacity:${.2+.6*Math.abs(Math.sin(t*3+i))}"></div>`;$('sp').innerHTML=s;
 place('a',820,1060,1.45,true);pose('a',{...MO,aR:-150,open:wb>.3});
''')
