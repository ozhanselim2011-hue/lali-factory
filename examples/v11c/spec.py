BG='linear-gradient(180deg,#0a1222,#05070d)'
SUBW='900'
SUBX='text-transform:uppercase'
RED='суперфреш'
REDC='#64d2ff'
LINES=[
 [["деньги",1.75],["падают",2.25],["с",2.8],["небес,",3.0],["и",3.5],["я",3.75]],
 [["забираю",5.0],["снова",5.5],["этот",6.0],["кэш",6.25]],
 [["мы",8.0],["бросаемся",8.25],["по",8.75],["кругу,",9.0]],
 [["не",9.5],["смотря",9.75],["на",10.0],["амбразуру",10.25]],
 [["я",10.5],["сегодня",10.75],["Лали",11.25],["суперфреш",12.0]],
]
SC=[[-0.3,4.4],[4.4,7.8],[7.8,9.45],[9.45,10.45],[10.45,99]]
GLOW=['#1d3a7a','#1a5c2e','#3a1d6a','#7a3a0a','#5a1d7a']
PEMO=['💸','💵','🔁','⚠️','✨']
END=[12.55,12.9]
CSS='''.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}
.bill{position:absolute;font-size:44px}'''
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#3d7fc4,#1a3a6a)">
 <div style="padding:30px 36px 0;display:flex;justify-content:space-between;align-items:flex-start">
  <div><div style="font-size:28px;font-weight:600">Небеса</div><div style="font-size:96px;font-weight:200;line-height:1">$∞</div><div id="w1" style="font-size:24px;font-weight:600">Облачно</div></div>
  <div style="background:rgba(0,0,0,.18);border-radius:22px;padding:14px 18px;font-size:22px;font-weight:700;text-align:right">💸 осадки<div id="pr1" class="mono" style="font-size:34px;font-weight:800">0%</div></div></div>
 <div style="position:absolute;left:50%;top:150px;margin-left:-70px;font-size:120px;line-height:1">☁️</div>
 <div id="rain" style="position:absolute;inset:0;overflow:hidden"></div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:70px;background:linear-gradient(0deg,rgba(0,0,0,.25),transparent)"></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#000">
 <div class="hdr">Apple Cash</div>
 <div id="sum2" class="c mono" style="top:70px;font-size:76px;font-weight:800;color:#30d158">$0</div>
 <div id="toast2" style="position:absolute;left:30px;right:30px;top:180px;background:rgba(60,60,64,.9);border-radius:22px;padding:14px 18px;font-size:22px;font-weight:700;opacity:0">💵 Apple Cash · <span id="tt2"></span></div>
 <div id="fly2" style="position:absolute;inset:0"></div>
 <div id="bag" style="position:absolute;font-size:80px;z-index:6;transform-origin:center">💰</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#000">
 <div class="hdr" style="color:#a6ff00">Фитнес · Тренировка</div><div class="ttl">Бег по кругу</div>
 <svg width="600" height="420" style="position:absolute;top:170px;left:0"><ellipse cx="300" cy="230" rx="240" ry="140" fill="none" stroke="#2c2c2e" stroke-width="56"/><ellipse cx="300" cy="230" rx="240" ry="140" fill="none" stroke="#a6ff00" stroke-width="5" stroke-dasharray="20 16"/></svg>
 <div class="ch" data-p="r1"></div><div class="ch" data-p="r2"></div>
 <div id="lp3" class="c mono" style="top:120px;left:auto;right:40px;text-align:right;font-size:44px;font-weight:800;color:#a6ff00">круг 1</div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div style="position:absolute;left:40px;right:40px;top:40px;background:rgba(44,44,46,.98);border-radius:30px;text-align:center;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.6)">
  <div style="padding:24px 24px 18px"><div style="font-size:56px">⚠️</div><div style="font-size:30px;font-weight:900;margin-top:6px">Впереди амбразура</div><div style="font-size:21px;color:#aeaeb2;font-weight:500;margin-top:6px">Посмотреть перед тем как идти?</div></div>
  <div style="display:flex;border-top:1px solid #48484a"><div id="no4" style="flex:1;padding:20px;font-size:26px;color:#0a84ff;border-right:1px solid #48484a">Посмотреть</div><div id="go4" style="flex:1;padding:20px;font-size:26px;font-weight:800;color:#0a84ff">Вперёд</div></div></div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:120px;background:repeating-linear-gradient(90deg,#2c2c2e 0 40px,#242426 40px 80px)"></div>
 <div id="boom4" style="position:absolute;left:380px;bottom:70px;font-size:120px;opacity:0">💥</div>
 <div class="ch" data-p="d"></div>
 <div id="nl4" class="c" style="top:330px;font-size:30px;font-weight:900;color:#ff9f0a;opacity:0">не смотря ✓</div>
</div>
<div class="card" id="c5" style="background:linear-gradient(160deg,#0a2a4a,#1a0a3a 60%,#3a0a3a)">
 <div id="sp5" style="position:absolute;inset:0"></div>
 <div class="hdr" style="color:#64d2ff">Постер контакта</div>
 <div class="c" style="top:80px"><div id="n5a" style="font-size:96px;font-weight:900;letter-spacing:-3px;line-height:.95;opacity:0">ЛАЛИ</div>
  <div id="n5b" style="font-size:76px;font-weight:900;letter-spacing:-2px;line-height:1;background:linear-gradient(90deg,#64d2ff,#bf5af2,#ff2d78);-webkit-background-clip:text;color:transparent;opacity:0">СУПЕРФРЕШ</div></div>
 <div class="ch" data-p="e"></div>
 <div id="st5" class="c" style="bottom:24px;font-size:22px;font-weight:700;color:#aeaeb2">статус: обычный</div>
</div>
'''
BUILD='''
const CH=(p,hat,j1,j2)=>`<svg viewBox="0 0 200 300" width="200" height="300" style="overflow:visible">
<defs><linearGradient id="${p}_jg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${j1}" id="${p}_s1"/><stop offset=".5" stop-color="${j2}" id="${p}_s2"/><stop offset="1" stop-color="${j2}" id="${p}_s3"/></linearGradient></defs>
<g id="${p}_all">
<g id="${p}_legL"><rect x="77" y="205" width="21" height="70" rx="10" fill="#26262e"/><ellipse cx="84" cy="280" rx="19" ry="10" fill="#fff"/></g>
<g id="${p}_legR"><rect x="102" y="205" width="21" height="70" rx="10" fill="#26262e"/><ellipse cx="116" cy="280" rx="19" ry="10" fill="#fff"/></g>
<g id="${p}_armL"><rect x="40" y="128" width="21" height="72" rx="10" fill="url(#${p}_jg)"/><circle cx="50" cy="202" r="10" fill="#f2c6a0"/></g>
<rect x="54" y="116" width="92" height="104" rx="32" fill="url(#${p}_jg)"/>
<path d="M58 150 H142 M58 182 H142" stroke="rgba(0,0,0,.16)" stroke-width="4"/>
<path d="M78 120 Q100 152 122 120" fill="none" stroke="#ffd60a" stroke-width="5"/><circle cx="100" cy="146" r="7" fill="#ffd60a"/>
<g id="${p}_armR"><rect x="139" y="128" width="21" height="72" rx="10" fill="url(#${p}_jg)"/><circle cx="150" cy="202" r="10" fill="#f2c6a0"/></g>
<g id="${p}_head"><circle cx="100" cy="80" r="42" fill="#f2c6a0"/>
<path d="M56 66 Q58 26 100 26 Q142 26 144 66 L162 72 Q100 54 38 72 Z" fill="${hat}"/>
<rect x="64" y="74" width="32" height="19" rx="9" fill="#111"/><rect x="104" y="74" width="32" height="19" rx="9" fill="#111"/><rect x="94" y="78" width="12" height="4" fill="#111"/>
<rect x="70" y="77" width="8" height="4" rx="2" fill="rgba(255,255,255,.5)"/><rect x="110" y="77" width="8" height="4" rx="2" fill="rgba(255,255,255,.5)"/>
<path id="${p}_mouth" d="M88 104 Q100 112 112 104" fill="none" stroke="#7a3a2a" stroke-width="4" stroke-linecap="round"/></g>
</g></svg>`;
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;const c={r2:['#ffd60a','#30d158','#0a8a3a']}[p]||['#64d2ff','#ff8ac4','#ff2d78'];e.id='ch_'+p;e.innerHTML=CH(p,...c);});
 let r='';for(let i=0;i<22;i++)r+=`<div class="bill" id="rb${i}" style="left:${10+rnd(i)*540}px">💵</div>`;$('rain').innerHTML=r;
 let f='';for(let i=0;i<4;i++)f+=`<div class="bill" id="fb${i}" style="opacity:0">💵</div>`;$('fly2').innerHTML=f;
 let s='';for(let i=0;i<40;i++)s+=`<div id="s5_${i}" style="position:absolute;left:${rnd(i)*580}px;top:${rnd(i+77)*670}px;font-size:${14+rnd(i+4)*26}px;color:${['#64d2ff','#bf5af2','#ff2d78','#fff'][i%4]}">✦</div>`;$('sp5').innerHTML=s;})();
function pose(p,o){const R=(id,a,x,y)=>$(p+'_'+id).setAttribute('transform',`rotate(${a||0} ${x} ${y})`);
 R('armL',o.aL,50,135);R('armR',o.aR,150,135);R('legL',o.lL,88,210);R('legR',o.lR,112,210);R('head',o.hd,100,110);
 $(p+'_all').setAttribute('transform',`translate(0 ${o.bob||0})`);
 $(p+'_mouth').setAttribute('d',o.open?'M86 102 Q100 122 114 102 Z':'M88 104 Q100 112 112 104');$(p+'_mouth').setAttribute('fill',o.open?'#7a2a2a':'none');}
function place(p,x,y,s,flip,rot){const e=$('ch_'+p);e.style.left=(x-100)+'px';e.style.top=(y-290)+'px';e.style.transform=`scale(${s*(flip?-1:1)},${s}) rotate(${rot||0}deg)`;}
const run=(t,f)=>{const q=Math.sin(t*f);return {lL:q*38,lR:-q*38,aL:-q*45,aR:-q*45,bob:-Math.abs(Math.cos(t*f))*8}};
const walk=(t,f)=>{const q=Math.sin(t*f);return {lL:q*22,lR:-q*22,aL:-q*20,aR:-q*20,bob:-Math.abs(Math.cos(t*f))*4}};
'''
RENDER='''
 // ---- S1 sky
 {const r=seg(t,1.75,3.0);$('pr1').textContent=Math.round(r*100)+'%';$('w1').textContent=t>=3.0?'Денежный дождь':'Облачно';
  for(let i=0;i<22;i++){const e=$('rb'+i);const ph=((t-1.75)*.75+rnd(i+9))%1;e.style.top=(-60+ph*720)+'px';e.style.opacity=t>=1.75?1:0;e.style.transform=`rotate(${(rnd(i)-.5)*80+t*60}deg)`;}
  let x=300,o;if(t<1.6){x=lerp(-80,300,seg(t,0,1.5));o=walk(t,14);if(t>=1.5){o={hd:-10}}}
  else if(t<3.5){const w=Math.sin(t*9);o={aL:150+w*15,aR:-150+w*15,hd:-12,open:t>=2.25,lL:0,lR:0};}
  else{o={aL:20,aR:58,hd:0,open:false};}
  const j=pop(t,3.0,5);o.bob=(o.bob||0)-j*70;place('a',x,650,1.15,false);pose('a',o);}
 // ---- S2 cash
 {const T=[5.0,5.5,6.0,6.25],V=[500,1000,2500,5000];let s=0,last=-9,k=-1;T.forEach((ti,i)=>{if(t>=ti){s+=V[i]*eo(seg(t,ti,ti+.3));last=ti;k=i}});
  $('sum2').textContent='$'+fmt(s);$('sum2').style.transform=`scale(${1+.15*pop(t,last,6)})`;
  $('toast2').style.opacity=k>=0?1:0;$('tt2').textContent=k>=0?(k?'снова':'получено')+' +$'+V[k]+' с небес':'';
  const sling=eo(seg(t,6.25,6.6));const bx=lerp(368,385,sling),by=lerp(470,370,sling);$('bag').style.left=(bx-40)+'px';$('bag').style.top=(by-50)+'px';
  $('bag').style.transform=`scale(${1+(k+1)*.12+.25*pop(t,last,6)}) rotate(${sling*-20}deg)`;
  T.forEach((ti,i)=>{const e=$('fb'+i);const p=seg(t,ti-.35,ti);e.style.opacity=p>0&&p<1?1:0;e.style.left=lerp(100+i*120,bx-20,eo(p))+'px';e.style.top=lerp(150,by-20,eo(p))+'px';e.style.transform=`rotate(${p*360}deg) scale(${1-p*.4})`;});
  const b=pop(t,last,7);pose('b',{aL:-10+Math.sin(t*6)*8,aR:lerp(-40,-165,sling),open:b>.3,bob:-b*22,hd:Math.sin(t*3)*4});place('b',300,640,1.1,false);}
 // ---- S3 run
 {const go=t>=8.0?(t-8.0):0;[['r1',0],['r2',.5]].forEach(([p,o])=>{const a=(go*0.9+o)*2*Math.PI+Math.PI/2;const x=300+240*Math.cos(a),y=400+140*Math.sin(a);
   const vx=-Math.sin(a);place(p,x,y+15,.58*(0.85+0.15*Math.sin(a)),vx<0);$('ch_'+p).style.zIndex=Math.round(y);pose(p,t>=8.0?run(t,22):{});});
  $('lp3').textContent='круг '+(1+Math.floor(go*1.8));}
 // ---- S4 ambrazura
 {const p=seg(t,9.5,10.45);const x=lerp(-60,680,p);const o=run(t,24);o.aL=-150;o.hd=8;place('d',x,650,.9,false);pose('d',o);
  $('no4').style.opacity=t>=9.75?.3:1;const g=t>=10.25;$('go4').style.background=g?'#ff9f0a':'transparent';$('go4').style.color=g?'#000':'#0a84ff';
  $('boom4').style.opacity=t>=10.25?1-seg(t,10.35,10.45):0;$('boom4').style.transform=`scale(${eo(seg(t,10.25,10.35))*1.3})`;$('nl4').style.opacity=seg(t,10.1,10.25);if(si==3)shake('c4',t,10.25,8);}
 // ---- S5 superfresh
 {const f=t>=12.0;$('n5a').style.opacity=seg(t,11.25,11.35);$('n5a').style.transform=`scale(${1+.25*pop(t,11.25,6)})`;$('n5b').style.opacity=seg(t,12.0,12.1);$('n5b').style.transform=`scale(${1+.3*pop(t,12.0,5)})`;
  let o;if(t<11.25)o={aL:10,aR:58,hd:Math.sin(t*3)*5};else if(t<12.0)o={aL:10,aR:-120,hd:-6,open:true};else o={aL:150,aR:-150,open:true,hd:0};
  o.bob=-pop(t,12.0,5)*45-Math.abs(Math.sin(t*5))*(f?6:0);place('e',300,675,1.25,false);pose('e',o);
  $('ch_e').style.filter=f?`drop-shadow(0 0 ${20+10*Math.sin(t*8)}px #bf5af2)`:'none';
  if(f){const h=(t*240)%360;$('e_s1').setAttribute('stop-color',`hsl(${h},100%,65%)`);$('e_s2').setAttribute('stop-color',`hsl(${(h+120)%360},100%,60%)`);$('e_s3').setAttribute('stop-color',`hsl(${(h+240)%360},100%,60%)`);}
  $('st5').textContent=f?'статус: суперфреш ✨':'статус: обычный';$('st5').style.color=f?'#64d2ff':'#aeaeb2';
  for(let i=0;i<40;i++)$('s5_'+i).style.opacity=f?(.3+.7*Math.abs(Math.sin(t*4+i))):.08;}
'''
