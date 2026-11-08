BG='linear-gradient(180deg,#0a1222,#05070d)'
SUBW='900'
SUBX='text-transform:uppercase'
RED='гламурно'
REDC='#ffd60a'
LINES=[
 [["и",0.0],["на",0.5],["лугу",0.8],["резвится",1.5],["тусовка",2.6],["зайцев,",3.7]],
 [["ушами",4.4],["хлопая",5.4],["под",6.1],["праздничный",6.5],["бит",7.5]],
 [["сегодня",8.8],["party,",9.5],["все",10.6],["хотят",10.9],["потусоваться",11.9]],
 [["и",13.2],["песня",13.6],["Шнуфеля",14.3],["гламурно",14.9],["звучит",15.9]],
]
SC=[[-0.3,4.3],[4.3,8.6],[8.6,13.05],[13.05,99]]
GLOW=['#1a5c2e','#5a1d7a','#7a3a0a','#7a6a10']
PEMO=['🐰','🎵','🎉','✨']
END=[16.6,17.0]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#5aa8e8 0%,#9fd3ff 45%,#4caf50 46%,#2e7d32 100%)">
 <div style="padding:30px 36px 0;color:#fff"><div style="font-size:28px;font-weight:600">Луг</div><div style="font-size:80px;font-weight:200;line-height:1">☀️ 24°</div></div>
 <div id="fl1" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="a"></div><div class="ch" data-p="b"></div><div class="ch" data-p="c"></div>
 <div style="position:absolute;left:24px;right:24px;bottom:24px;background:rgba(0,0,0,.35);border-radius:24px;padding:16px 22px;color:#fff;font-size:24px;font-weight:800">🐰 Тусовка зайцев · <span id="cnt1">0</span> рядом</div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#2a0a3a,#0a0410)">
 <div class="hdr" style="color:#bf5af2">Музыка · сейчас играет</div>
 <div style="position:absolute;left:40px;top:80px;font-size:34px;font-weight:900">Праздничный бит</div>
 <div id="bpm2" class="mono" style="position:absolute;right:40px;top:84px;font-size:26px;font-weight:800;color:#bf5af2">0 BPM</div>
 <div id="eq2" style="position:absolute;left:40px;right:40px;top:130px;height:120px;display:flex;align-items:flex-end;opacity:.8;gap:8px"></div>
 <div class="ch" data-p="d"></div>
 <div id="cl2" class="c" style="bottom:30px;font-size:24px;font-weight:800;color:#d0a0ff">хлопков ушами: 0</div>
</div>
<div class="card" id="c3" style="background:#1c1c1e">
 <div style="position:absolute;left:30px;right:30px;top:30px;border-left:8px solid #ff9f0a;background:#2c2c2e;border-radius:20px;padding:18px 22px">
  <div style="font-size:20px;color:#ff9f0a;font-weight:800">Приглашение · сегодня</div><div style="font-size:42px;font-weight:900">🎉 PARTY</div>
  <div style="display:flex;justify-content:space-between;margin-top:6px;font-size:22px;font-weight:700"><span>пойдут:</span><span id="go3" class="mono" style="color:#30d158">0</span></div></div>
 <div class="ch" data-p="e"></div><div class="ch" data-p="f"></div><div class="ch" data-p="g"></div>
 <div id="ball3" style="position:absolute;left:250px;top:200px;font-size:100px;opacity:0">🪩</div>
</div>
<div class="card" id="c4" style="background:radial-gradient(circle at 50% 40%,#4a3a0a,#0c0a02)">
 <div id="sp4" style="position:absolute;inset:0"></div>
 <div style="position:absolute;left:30px;right:30px;top:30px;background:rgba(0,0,0,.4);border-radius:24px;padding:16px 20px;display:flex;gap:16px;align-items:center">
  <div style="width:72px;height:72px;border-radius:16px;background:linear-gradient(135deg,#ffd6e8,#ff8ac4);display:flex;align-items:center;justify-content:center;font-size:44px">🐰</div>
  <div><div style="font-size:28px;font-weight:900">Песня Шнуфеля</div><div id="gl4" style="font-size:22px;font-weight:800;color:#8e8e93">качество: обычное</div></div></div>
 <div class="ch" data-p="h"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){const C={b:['#ffd60a','#a0f0ff','#0a84ff'],c:['#30d158','#ffe27a','#ff9f0a'],f:['#ffd60a','#a0f0ff','#0a84ff'],g:['#30d158','#ffe27a','#ff9f0a']};
 document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...(C[p]||['#64d2ff','#ff8ac4','#ff2d78']));
  const hd=document.getElementById(p+'_head');const ns='http://www.w3.org/2000/svg';
  ['L','R'].forEach((s,i)=>{const g=document.createElementNS(ns,'g');g.id=p+'_ear'+s;g.innerHTML=`<ellipse cx="${i?118:82}" cy="2" rx="13" ry="34" fill="#fff"/><ellipse cx="${i?118:82}" cy="6" rx="6" ry="24" fill="#ffb3cf"/>`;hd.insertBefore(g,hd.firstChild);});});
 let f='';for(let i=0;i<18;i++)f+=`<div style="position:absolute;left:${rnd(i)*560}px;top:${330+rnd(i+5)*300}px;font-size:${24+rnd(i+2)*14}px">${['🌼','🌷','🍀'][i%3]}</div>`;$('fl1').innerHTML=f;
 let q='';for(let i=0;i<20;i++)q+=`<div id="eq${i}" style="flex:1;border-radius:6px;background:linear-gradient(0deg,#bf5af2,#ff2d78)"></div>`;$('eq2').innerHTML=q;
 let s='';for(let i=0;i<40;i++)s+=`<div id="s4_${i}" style="position:absolute;left:${rnd(i)*580}px;top:${rnd(i+77)*670}px;font-size:${14+rnd(i+4)*26}px;color:#ffd60a">✦</div>`;$('sp4').innerHTML=s;})();
function ears(p,a){$(p+'_earL').setAttribute('transform',`rotate(${-a} 82 30)`);$(p+'_earR').setAttribute('transform',`rotate(${a} 118 30)`);}
function hop(t,ph){const q=Math.abs(Math.sin(t*5+ph));return{bob:-q*60,lL:-q*20,lR:q*20,aL:40*q,aR:-40*q,open:q>.6}}
'''
RENDER='''
 {[['a',300,.95,0],['b',140,.75,1.3],['c',460,.75,2.4]].forEach(([p,x,s,ph],i)=>{const on=t>=[0.8,1.5,2.6][i];const o=on?hop(t,ph):{aL:8,aR:-8};place(p,x+(on?Math.sin(t*1.5+ph)*30:0),620-(i?40:0),s,i==2);pose(p,o);ears(p,on?Math.sin(t*10+ph)*15:0);
   $('ch_'+p).style.opacity=t>=[0,1.5,2.6][i]-.01?1:0;});$('cnt1').textContent=t<1.5?1:(t<2.6?2:(t<3.7?3:'3 + ещё 40'));}
 {const b=t>=4.4;for(let i=0;i<20;i++)$('eq'+i).style.height=(10+(b?Math.abs(Math.sin(t*7+i*1.3))*110:5))+'px';$('bpm2').textContent=b?'128 BPM':'0 BPM';
  const fl=b?Math.sin(t*16)*40:0;place('d',300,640,1.25,false);pose('d',b?{aL:60+Math.sin(t*8)*30,aR:-60-Math.sin(t*8)*30,bob:-Math.abs(Math.sin(t*8))*14,open:1,lL:Math.sin(t*8)*10,lR:-Math.sin(t*8)*10}:{aL:8,aR:-8});ears('d',fl);
  $('cl2').textContent='хлопков ушами: '+(b?Math.floor((t-4.4)*16/Math.PI):0);}
 {const n=t<10.6?0:Math.round(lerp(0,999,eo(seg(t,10.6,12.3))));$('go3').textContent=n>=999?'ВСЕ 🐰':n;const pt=t>=9.5;$('ball3').style.opacity=pt?1:0;$('ball3').style.transform=`rotate(${t*90}deg)`;
  [['e',300,1.0,0],['f',140,.8,1],['g',460,.8,2]].forEach(([p,x,s,ph],i)=>{const on=t>=[8.8,10.6,10.9][i];place(p,x,650-(i?20:0),s,i==2);$('ch_'+p).style.opacity=on?1:0;
   const q=Math.sin(t*8+ph);pose(p,pt?{aL:lerp(20,150,(q+1)/2),aR:-lerp(20,150,(1-q)/2),lL:q*14,lR:-q*14,bob:-Math.abs(q)*12,open:1}:{aL:8,aR:-150+Math.sin(t*12)*20});ears(p,q*20);});}
 {const g=t>=14.9;$('gl4').textContent=g?'качество: ГЛАМУРНО ✨':'качество: обычное';$('gl4').style.color=g?'#ffd60a':'#8e8e93';
  const q=Math.sin(t*7);place('h',300,660,1.35,false);pose('h',g?{aL:150,aR:-150+q*10,open:1,bob:-Math.abs(q)*10}:{aL:8,aR:58,hd:Math.sin(t*3)*5});ears('h',g?q*25:Math.sin(t*4)*6);
  $('ch_h').style.filter=g?`drop-shadow(0 0 ${25+10*Math.sin(t*8)}px #ffd60a)`:'none';
  if(g){const h=40+Math.sin(t*4)*10;$('h_s1').setAttribute('stop-color','#fff3b0');$('h_s2').setAttribute('stop-color',`hsl(${h},95%,55%)`);$('h_s3').setAttribute('stop-color','#d4a017');}
  for(let i=0;i<40;i++)$('s4_'+i).style.opacity=g?(.3+.7*Math.abs(Math.sin(t*4+i))):.06;}
'''
