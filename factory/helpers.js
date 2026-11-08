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
function pose(p,o){const R=(id,a,x,y)=>$(p+'_'+id).setAttribute('transform',`rotate(${a||0} ${x} ${y})`);
 R('armL',o.aL,50,135);R('armR',o.aR,150,135);R('legL',o.lL,88,210);R('legR',o.lR,112,210);R('head',o.hd,100,110);
 $(p+'_all').setAttribute('transform',`translate(0 ${o.bob||0})`);
 $(p+'_mouth').setAttribute('d',o.open?'M86 102 Q100 122 114 102 Z':'M88 104 Q100 112 112 104');$(p+'_mouth').setAttribute('fill',o.open?'#7a2a2a':'none');}
function place(p,x,y,s,flip,rot){const e=$('ch_'+p);e.style.left=(x-100)+'px';e.style.top=(y-290)+'px';e.style.transform=`scale(${s*(flip?-1:1)},${s}) rotate(${rot||0}deg)`;}
const run=(t,f)=>{const q=Math.sin(t*f);return {lL:q*38,lR:-q*38,aL:-q*45,aR:-q*45,bob:-Math.abs(Math.cos(t*f))*8}};
const walk=(t,f)=>{const q=Math.sin(t*f);return {lL:q*22,lR:-q*22,aL:-q*20,aR:-q*20,bob:-Math.abs(Math.cos(t*f))*4}};
