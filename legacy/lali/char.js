(function(){
const Q=id=>document.getElementById(id);
const st=Q('stage');
const P='lc';
const w=document.createElement('div');w.id='lc_wrap';
w.style.cssText='position:absolute;left:0;top:0;width:200px;height:300px;transform-origin:100px 290px;z-index:45;filter:drop-shadow(0 18px 22px rgba(0,0,0,.6))';
w.innerHTML=`<svg viewBox="0 0 200 300" width="200" height="300" style="overflow:visible">
<defs><linearGradient id="${P}_jg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" id="${P}_s1"/><stop offset=".5" id="${P}_s2"/><stop offset="1" id="${P}_s3"/></linearGradient></defs>
<g id="${P}_all">
<g id="${P}_legL"><rect x="77" y="205" width="21" height="70" rx="10" fill="#26262e"/><ellipse cx="84" cy="280" rx="19" ry="10" fill="#fff"/></g>
<g id="${P}_legR"><rect x="102" y="205" width="21" height="70" rx="10" fill="#26262e"/><ellipse cx="116" cy="280" rx="19" ry="10" fill="#fff"/></g>
<g id="${P}_armL"><rect x="40" y="128" width="21" height="72" rx="10" fill="url(#${P}_jg)"/><circle cx="50" cy="202" r="10" fill="#f2c6a0"/></g>
<rect x="54" y="116" width="92" height="104" rx="32" fill="url(#${P}_jg)"/>
<path d="M58 150 H142 M58 182 H142" stroke="rgba(0,0,0,.16)" stroke-width="4"/>
<path d="M78 120 Q100 152 122 120" fill="none" stroke="#ffd60a" stroke-width="5"/><circle cx="100" cy="146" r="7" fill="#ffd60a"/>
<g id="${P}_armR"><rect x="139" y="128" width="21" height="72" rx="10" fill="url(#${P}_jg)"/><circle cx="150" cy="202" r="10" fill="#f2c6a0"/></g>
<g id="${P}_head"><circle cx="100" cy="80" r="42" fill="#f2c6a0"/>
<path d="M56 66 Q58 26 100 26 Q142 26 144 66 L162 72 Q100 54 38 72 Z" fill="#64d2ff"/>
<rect x="64" y="74" width="32" height="19" rx="9" fill="#111"/><rect x="104" y="74" width="32" height="19" rx="9" fill="#111"/><rect x="94" y="78" width="12" height="4" fill="#111"/>
<rect x="70" y="77" width="8" height="4" rx="2" fill="rgba(255,255,255,.5)"/><rect x="110" y="77" width="8" height="4" rx="2" fill="rgba(255,255,255,.5)"/>
<path id="${P}_mouth" d="M88 104 Q100 112 112 104" fill="none" stroke="#7a3a2a" stroke-width="4" stroke-linecap="round"/></g>
</g></svg>`;
st.appendChild(w);
const fx=document.createElement('div');fx.style.cssText='position:absolute;inset:0;z-index:46;pointer-events:none';
let fh=`<div id="lc_bub" style="position:absolute;min-width:86px;height:76px;padding:0 14px;border-radius:24px;background:#fff;color:#111;display:flex;align-items:center;justify-content:center;font-size:46px;font-weight:900;font-family:Inter,'Apple Color Emoji';box-shadow:0 8px 20px rgba(0,0,0,.45);opacity:0;transform-origin:20% 100%"></div>
<div id="lc_hold" style="position:absolute;font-size:64px;line-height:1;opacity:0;font-family:'Apple Color Emoji'"></div>`;
for(let i=0;i<10;i++)fh+=`<div id="lc_p${i}" style="position:absolute;font-size:34px;opacity:0;font-family:'Apple Color Emoji',Inter;font-weight:900;color:#fff"></div>`;
fx.innerHTML=fh;st.appendChild(fx);

const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)),sg=(t,a,b)=>cl((t-a)/(b-a)),eo=x=>1-Math.pow(1-x,3),lp=(a,b,x)=>a+(b-a)*x;
const S=Math.sin,A=Math.abs;
const POSE={
 idle:t=>({aL:8,aR:-8,hd:S(t*2)*3,bob:S(t*3)*1.5}),
 wave:t=>({aL:8,aR:-150+S(t*12)*22,hd:-4,open:1}),
 up:t=>({aL:150+S(t*9)*12,aR:-150+S(t*9+1)*12,open:1,hd:-8}),
 chest:t=>({aL:8,aR:58}),
 heart:t=>({aL:-58,aR:58,hd:6+S(t*3)*4}),
 hug:t=>({aL:-40,aR:40,hd:4}),
 point:t=>({aL:8,aR:-95+S(t*6)*4}),
 eyes:t=>({aL:-150,aR:-8,hd:4}),
 face:t=>({aL:-150,aR:150,hd:10}),
 facepalm:t=>({aL:8,aR:145,hd:12}),
 phone:t=>({aL:8,aR:166,hd:-6,open:S(t*14)>0}),
 think:t=>({aL:-40,aR:112,hd:-8+S(t*2)*3}),
 shrug:t=>({aL:55,aR:-55,hd:12,open:1}),
 angry:t=>({aL:-14,aR:14,hd:S(t*40)*4,jx:S(t*60)*3}),
 sad:t=>({aL:2,aR:-2,hd:20,bob:6}),
 dance:t=>{const q=S(t*8);return{aL:lp(20,150,(q+1)/2),aR:-lp(20,150,(1-q)/2),lL:q*14,lR:-q*14,bob:-A(q)*10,hd:q*8,open:1}},
 run:t=>{const q=S(t*22);return{lL:q*38,lR:-q*38,aL:-q*45,aR:-q*45,bob:-A(Math.cos(t*22))*8}},
 hold:t=>({aL:8,aR:-60}),
 show:t=>({aL:8,aR:-135+S(t*5)*6,open:1,hd:-6}),
 sleep:t=>({aL:4,aR:-4,hd:26,bob:8}),
 cool:t=>({aL:8,aR:-8,hd:-6,rot:-5}),
 fist:t=>({aL:8,aR:-165+S(t*16)*12,open:1,hd:-6}),
 tpose:t=>({aL:90,aR:-90,hd:14}),
 fall:t=>({aL:140+S(t*20)*20,aR:-140-S(t*20)*20,lL:S(t*14)*25,lR:-S(t*14)*25,open:1,rot:S(t*3)*14}),
 float:t=>({aL:70,aR:-70,lL:-15,lR:15,bob:-30+S(t*3)*14,hd:-10,rot:S(t*2)*8}),
};
const COL={pink:['#ff8ac4','#ff2d78'],green:['#7affa0','#30d158'],red:['#ff7a6e','#c4000c'],blue:['#9ad8ff','#0a5ad8'],black:['#55555e','#141418'],gold:['#ffe27a','#d4a017'],white:['#ffffff','#bfc4cc'],purple:['#d0a0ff','#7a2cff'],grey:['#9a9a9a','#4a4a4e']};
const FX={tears:'💧',sweat:'💦',hearts:'💗',zzz:'z',money:'💵',stars:'✨',fire:'🔥',music:'🎵'};
function vals(k,t){const v=Object.assign({aL:0,aR:0,lL:0,lR:0,hd:0,bob:0,rot:0,jx:0,open:0},(POSE[k.p]||POSE.idle)(t));return v;}
function blend(a,b,x){const o={};for(const k in b)o[k]=typeof b[k]==='number'?lp(a[k]??0,b[k],x):b[k];return o;}
function handPos(side,ang){const px=side?150:50,r=ang*Math.PI/180;return[px-67*Math.sin(r),135+67*Math.cos(r)];}
window.charRender=function(t){
 const K=window.LK;let i=0;for(let j=0;j<K.length;j++)if(t>=K[j].t)i=j;const k=K[i],pk=K[Math.max(0,i-1)];
 const x=eo(sg(t,k.t,k.t+.2));let v=blend(vals(pk,t),vals(k,t),x);
 let lastW=-9;try{LINES.flat().forEach(([w,s])=>{if(s<=t)lastW=s})}catch(e){}
 const bop=k.p==='sleep'?0:Math.exp(-(t-lastW)*9);
 const jump=k.j?Math.exp(-Math.max(0,t-k.t)*5)*Math.min(1,(t-k.t)*20):0;
 v.bob+=-bop*10-jump*70;
 const side=(k.s||window.LSIDE||'L')==='R';const X=(side?940:140)+v.jx,Y=1000,s=1.15,f=side?-1:1;
 const R=(id,a,x0,y0)=>Q(P+'_'+id).setAttribute('transform',`rotate(${a} ${x0} ${y0})`);
 R('armL',v.aL,50,135);R('armR',v.aR,150,135);R('legL',v.lL,88,210);R('legR',v.lR,112,210);R('head',v.hd,100,110);
 Q(P+'_all').setAttribute('transform',`translate(0 ${v.bob})`);
 const m=Q(P+'_mouth');m.setAttribute('d',v.open>.5?'M86 102 Q100 122 114 102 Z':(k.p==='sad'||k.p==='sleep'?'M88 110 Q100 102 112 110':'M88 104 Q100 112 112 104'));m.setAttribute('fill',v.open>.5?'#7a2a2a':'none');
 w.style.left=(X-100)+'px';w.style.top=(Y-290)+'px';w.style.transform=`scale(${s*f},${s}) rotate(${v.rot}deg)`;
 // outfit
 let c=k.c||'pink';if(c==='rainbow'){const h=(t*240)%360;[1,2,3].forEach((n,ix)=>Q(P+'_s'+n).setAttribute('stop-color',`hsl(${(h+ix*120)%360},100%,62%)`));}
 else{const C=COL[c]||COL.pink;Q(P+'_s1').setAttribute('stop-color',C[0]);Q(P+'_s2').setAttribute('stop-color',C[1]);Q(P+'_s3').setAttribute('stop-color',C[1]);}
 w.style.filter=c==='rainbow'?`drop-shadow(0 0 ${22+10*Math.sin(t*8)}px #bf5af2)`:'drop-shadow(0 18px 22px rgba(0,0,0,.6))';
 const sx=hx=>X+(hx-100)*s*f,sy=hy=>Y+(hy-290+v.bob)*s;
 // held prop
 const ho=Q('lc_hold');if(k.h){const [hx,hy]=handPos(true,v.aR);ho.textContent=k.h;ho.style.opacity=1;ho.style.left=(sx(hx)-32)+'px';ho.style.top=(sy(hy)-40)+'px';ho.style.transform=`scale(${1+.3*Math.exp(-(t-k.t)*7)})`;}else ho.style.opacity=0;
 // bubble
 const b=Q('lc_bub');if(k.e){b.textContent=k.e;const p=eo(sg(t,k.t,k.t+.18));b.style.opacity=p;b.style.left=(X+(side?-140:40))+'px';b.style.top=(sy(10)-70)+'px';b.style.transform=`scale(${lp(.3,1,p)+.15*Math.exp(-(t-k.t)*8)})`;}else b.style.opacity=0;
 // particles
 const fxk=k.fx;for(let n=0;n<10;n++){const e=Q('lc_p'+n);if(!fxk){e.style.opacity=0;continue}
  const ph=((t-k.t)*(fxk==='tears'||fxk==='sweat'?1.4:.7)+n/10)%1;e.textContent=FX[fxk];e.style.fontSize=fxk==='zzz'?(26+n%3*10)+'px':'34px';
  let px,py;if(fxk==='tears'){px=sx(n%2?84:116)+(n%3-1)*4;py=sy(96)+ph*160;}else if(fxk==='sweat'){px=sx(140)+n%2*10;py=sy(50)+ph*90;}
  else if(fxk==='money'){px=X-140+((n*53)%280);py=sy(-60)+ph*330;}else{px=sx(100)+(Math.sin(n*2.3+ph*4))*70;py=sy(20)-ph*220;}
  e.style.left=px+'px';e.style.top=py+'px';e.style.opacity=(t>=k.t?1:0)*(1-ph)*.95;e.style.transform=`rotate(${fxk==='money'?ph*360:0}deg)`;}
};
const _r=window.render;window.render=function(t){_r(t);window.charRender(t);};
})();
