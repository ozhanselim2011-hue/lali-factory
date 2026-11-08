BG='linear-gradient(180deg,#0e0a10,#050306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["…кидаю",0.3],["палку",0.9],["и",1.2],["говорю:",1.3],["«апорт»",1.5]],
 [["твоя",1.9],["с*ка",2.3],["меня",2.6],["хочет,",2.8],["я",3.4],["в",3.6],["тик-токе",3.7],["в",4.2],["сохранёнках",4.25]],
 [["дам",5.0],["три",5.2],["круга",5.4],["ей",5.8],["закинуть,",6.0]],
 [["а",6.6],["потом",6.8],["мы",7.2],["п*ёмся",7.4]],
 [["на",8.2],["мне",8.4],["эта",8.6],["ювелирка",8.9],["стоит",9.8],["дороже",10.1],["твоей",10.5],["трёшки",11.0]],
 [["на",11.4],["мне",11.5],["кошки",11.7],["хэллоу",12.2],["китти",12.6]],
 [["на",13.0],["тебе",13.1],["ничё",13.4],["—",13.9],["ты",14.0],["додик",14.2]],
]
SC=[[-0.3,1.85],[1.85,4.95],[4.95,6.55],[6.55,8.1],[8.1,11.35],[11.35,12.95],[12.95,99]]
GLOW=['#1a5c2e','#7a1f4a','#1a5c2e','#5a1d7a','#5a5a7a','#7a2a5a','#3a3a3a']
PEMO=['🦴','📌','⭕','🔞','💎','🐱','🤡']
END=[14.7,15.06]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#5aa8e8,#9fd3ff 45%,#4caf50 46%,#2e7d32)">
 <div class="ch" data-p="a"></div><div id="st1" style="position:absolute;font-size:60px;z-index:6">🦴</div><div id="dg1" style="position:absolute;font-size:110px;z-index:6;transform:scaleX(-1)">🐕</div>
 <div id="ap1" style="position:absolute;left:150px;top:200px;background:#fff;color:#111;border-radius:22px;padding:10px 20px;font-size:34px;font-weight:900;opacity:0">апорт!</div>
</div>
<div class="card" id="c2" style="background:#000">
 <div class="hdr">Сохранённое · её профиль</div>
 <div id="gr2" style="position:absolute;left:20px;right:20px;top:80px;display:grid;grid-template-columns:repeat(3,1fr);gap:6px"></div>
 <div id="nt2" style="position:absolute;left:24px;right:24px;top:500px;background:rgba(60,60,64,.95);border-radius:22px;padding:14px 18px;font-size:22px;font-weight:800;opacity:0">📌 она сохранила твоё видео ×47</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#000">
 <div class="hdr" style="color:#30d158">Активность</div><div class="ttl">3 круга</div>
 <svg width="360" height="360" style="position:absolute;left:120px;top:180px">
  <circle cx="180" cy="180" r="160" fill="none" stroke="#3a0d12" stroke-width="34"/><circle id="ra" cx="180" cy="180" r="160" fill="none" stroke="#ff2d55" stroke-width="34" stroke-linecap="round" stroke-dasharray="1005" stroke-dashoffset="1005" transform="rotate(-90 180 180)"/>
  <circle cx="180" cy="180" r="118" fill="none" stroke="#1d3a0d" stroke-width="34"/><circle id="rb" cx="180" cy="180" r="118" fill="none" stroke="#a6ff00" stroke-width="34" stroke-linecap="round" stroke-dasharray="741" stroke-dashoffset="741" transform="rotate(-90 180 180)"/>
  <circle cx="180" cy="180" r="76" fill="none" stroke="#0d2a3a" stroke-width="34"/><circle id="rc" cx="180" cy="180" r="76" fill="none" stroke="#00e5ff" stroke-width="34" stroke-linecap="round" stroke-dasharray="477" stroke-dashoffset="477" transform="rotate(-90 180 180)"/></svg>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div style="position:absolute;inset:0;backdrop-filter:blur(2px)"></div>
 <div class="ch" data-p="c"></div>
 <div id="bl4" style="position:absolute;inset:0;background:rgba(20,20,24,.6);backdrop-filter:blur(26px);display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0;z-index:8">
  <div style="font-size:110px">🔞</div><div style="font-size:34px;font-weight:900;margin-top:10px">Контент скрыт</div><div style="font-size:22px;color:#aeaeb2;font-weight:600;margin-top:6px">🌙 Не беспокоить · до утра</div></div>
</div>
<div class="card" id="c5" style="background:radial-gradient(circle at 50% 40%,#2a2a3a,#08080c)">
 <div class="ch" data-p="d"></div><div id="sp5" style="position:absolute;inset:0;z-index:7"></div>
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#1c1c1e;border-radius:22px;padding:16px 20px;z-index:8">
  <div style="display:flex;justify-content:space-between;font-size:22px;font-weight:800"><span>💎 ювелирка</span><span id="j5" class="mono" style="color:#64d2ff">0 ₽</span></div>
  <div style="height:12px;border-radius:6px;background:#2c2c2e;margin:6px 0 12px;overflow:hidden"><div id="jb5" style="height:12px;background:#64d2ff;width:0"></div></div>
  <div style="display:flex;justify-content:space-between;font-size:22px;font-weight:800"><span>🏢 твоя трёшка</span><span id="k5" class="mono" style="color:#8e8e93">0 ₽</span></div>
  <div style="height:12px;border-radius:6px;background:#2c2c2e;margin-top:6px;overflow:hidden"><div id="kb5" style="height:12px;background:#8e8e93;width:0"></div></div></div>
</div>
<div class="card" id="c6" style="background:linear-gradient(180deg,#ffd6e8,#ff9ac1);color:#111">
 <div id="ct6" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="e"></div>
 <div class="c" style="top:40px;font-size:40px;font-weight:900;color:#ff2d78">🐱 мяу-образ</div>
</div>
<div class="card" id="c7" style="background:#1c1c1e">
 <div class="hdr">Сканер образа</div>
 <div class="ch" data-p="f"></div><div class="ch" data-p="g"></div>
 <div id="sc7" style="position:absolute;left:30px;width:260px;height:6px;background:#64d2ff;box-shadow:0 0 30px #64d2ff;opacity:0"></div>
 <div id="r7" style="position:absolute;left:30px;top:120px;background:#3a0d12;border-radius:18px;padding:12px 16px;font-size:22px;font-weight:900;color:#ff453a;opacity:0">на тебе: 0 ₽<div style="font-size:30px">додик 🤡</div></div>
 <div id="m7" style="position:absolute;right:30px;top:120px;background:#0f3a1f;border-radius:18px;padding:12px 16px;font-size:22px;font-weight:900;color:#30d158;opacity:0">на мне: ∞ ₽<div style="font-size:30px">💎</div></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...(p=='g'?['#8e8e93','#c8c8cc','#8e8e93']:['#64d2ff','#ff8ac4','#ff2d78']));});
 $('gr2').innerHTML=[0,1,2,3,4,5,6,7,8].map(i=>`<div id="g2_${i}" style="aspect-ratio:9/12;border-radius:10px;background:linear-gradient(135deg,#ff8ac4,#5e2cff);display:flex;align-items:center;justify-content:center;font-size:44px;position:relative;opacity:0">😎<div style="position:absolute;right:6px;bottom:4px;font-size:18px">📌</div></div>`).join('');
 let s='';for(let i=0;i<14;i++)s+=`<div id="d5_${i}" style="position:absolute;font-size:${20+i%3*10}px">✦</div>`;$('sp5').innerHTML=s;
 let c='';for(let i=0;i<24;i++)c+=`<div style="position:absolute;left:${rnd(i)*560}px;top:${rnd(i+4)*640}px;font-size:${30+rnd(i+2)*30}px;opacity:.5">${i%2?'🐱':'🎀'}</div>`;$('ct6').innerHTML=c;
 // cat ears + bow on e
 const hd=$('e_head');const g=document.createElementNS('http://www.w3.org/2000/svg','g');g.innerHTML='<path d="M62 44 L58 4 L92 30 Z" fill="#fff" stroke="#ff2d78" stroke-width="4"/><path d="M138 44 L142 4 L108 30 Z" fill="#fff" stroke="#ff2d78" stroke-width="4"/><path d="M118 30 l22 -14 l0 28 Z M118 30 l-2 0" fill="#ff2d78"/><circle cx="118" cy="30" r="7" fill="#ff2d78"/><path d="M118 30 l-22 -14 l0 28 Z" fill="#ff2d78"/>';hd.appendChild(g);})();
'''
RENDER='''
 {const th=seg(t,0.9,1.3);place('a',150,640,.95,false);pose('a',t<0.9?{aL:8,aR:150}:(t<1.3?{aL:8,aR:-120}:{aL:8,aR:-95,open:1}));
  const sx=lerp(190,470,th),sy=lerp(420,440,th)-Math.sin(th*Math.PI)*200;$('st1').style.left=(t<0.9?150:sx)+'px';$('st1').style.top=(t<0.9?380:sy)+'px';$('st1').style.transform=`rotate(${th*720}deg)`;
  const dg=seg(t,1.2,1.7);$('dg1').style.left=lerp(620,420,eo(seg(t,0.6,1.3)))+'px';$('dg1').style.top=(510-Math.abs(Math.sin(t*12))*20)+'px';$('ap1').style.opacity=seg(t,1.5,1.6);}
 {for(let i=0;i<9;i++){const ti=3.7+i*.07;$('g2_'+i).style.opacity=seg(t,ti,ti+.1);$('g2_'+i).style.transform=`scale(${eb(seg(t,ti,ti+.2))})`;}$('nt2').style.opacity=seg(t,4.25,4.4);
  place('b',470,680,.8,true);pose('b',t>=2.8?{aL:8,aR:-8,hd:-6,rot:-5}:{aL:8,aR:-8});}
 {[5.2,5.4,5.8].forEach((s,i)=>{const id=['ra','rb','rc'][i],L=[1005,741,477][i];$(id).setAttribute('stroke-dashoffset',L*(1-eo(seg(t,s,s+.5))));});}
 {place('c',300,680,1.15,false);pose('c',{aL:8,aR:-8,hd:-6,rot:-5});$('bl4').style.opacity=seg(t,7.2,7.45);}
 {const j=eo(seg(t,8.9,9.8))*30,k=eo(seg(t,10.5,11.0))*12;$('j5').textContent=fmt(j*1e6)+' ₽';$('k5').textContent=fmt(k*1e6)+' ₽';$('jb5').style.width=(j/30*100)+'%';$('kb5').style.width=(k/30*100)+'%';
  place('d',300,690,1.35,false);pose('d',t>=8.9?{aL:8,aR:58,hd:-6}:{aL:8,aR:-8});const g=t>=8.9;
  for(let i=0;i<14;i++){const e=$('d5_'+i);const on=g&&Math.sin(t*9+i*2)>.3;e.style.opacity=on?1:0;e.style.left=(300+Math.cos(i*.9)*(40+i*6))+'px';e.style.top=(690+(130-290)*1.35+Math.sin(i*.9)*(20+i*4))+'px';e.style.color='#bff4ff';}
  $('d_head').parentNode.querySelectorAll('path')[1].setAttribute('stroke',g?'#e8faff':'#ffd60a');$('ch_d').style.filter=g?'drop-shadow(0 0 30px #64d2ff)':'none';}
 {place('e',300,680,1.25,false);pose('e',t>=12.2?{aL:150,aR:-150,open:1,bob:-Math.abs(Math.sin(t*8))*14}:{aL:8,aR:-8});}
 {place('f',430,680,1.0,true);place('g',170,680,1.0,false);pose('g',{aL:4,aR:-4,hd:6});pose('f',t>=14.2?{aL:55,aR:-55,hd:12,open:1}:{aL:8,aR:-8,hd:-6});
  const sc=seg(t,13.0,13.8);$('sc7').style.opacity=sc>0&&sc<1?1:0;$('sc7').style.top=(380+Math.sin(sc*Math.PI*2)*200)+'px';$('r7').style.opacity=seg(t,13.4,13.5);$('m7').style.opacity=seg(t,13.8,13.9);$('r7').style.transform=`scale(${1+.2*pop(t,14.2,6)})`;}
'''
