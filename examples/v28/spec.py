BG='linear-gradient(180deg,#0e0a14,#050307)'
SUBW='900'
SUBX='text-transform:uppercase'
RED='Dolce'
REDC='#ffd60a'
LINES=[
 [["йоу,",0.0],["я",0.4],["ношу",0.6],["на",1.0],["себе",1.1],["ремень",1.4],["Dolce",2.0],["&",2.3],["Gabbana",2.4]],
 [["стиль,",3.0],["меня",3.4],["мама",3.7],["приучила",4.1],["круто",5.0],["одеваться",5.5]],
 [["мама,",6.1],["мама",6.6],["учила",7.1],["меня",7.6],["никогда",7.7],["не",8.1],["сдаваться",8.4]],
 [["у",8.8],["моей",9.0],["мамы",9.2],["красивые",9.5],["глаза",10.0]],
 [["она",10.5],["мне",10.6],["говорит",10.8],["тёплые",11.1],["слова",11.6]],
]
SC=[[-0.3,2.95],[2.95,6.05],[6.05,8.7],[8.7,10.4],[10.4,99]]
GLOW=['#6a5a10','#7a1f5a','#1a5c2e','#5a1d7a','#7a2a4a']
PEMO=['✨','👗','💪','👁️','💗']
END=[12.15,12.54]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:radial-gradient(circle at 50% 70%,#3a2a08,#0a0802)">
 <div class="ch" data-p="a"></div>
 <div id="tag1" style="position:absolute;left:24px;top:24px;background:#fff;color:#111;border-radius:18px;padding:12px 18px;box-shadow:0 10px 30px rgba(0,0,0,.4);opacity:0;z-index:8">
  <div style="font-size:18px;font-weight:800;color:#8e8e93">🏷 ремень</div><div style="font-size:30px;font-weight:900">Dolce &amp; Gabbana</div><div style="font-size:20px;font-weight:800;color:#30d158">✓ оригинал · на мне</div></div>
 <div id="spk1" style="position:absolute;inset:0;z-index:7;pointer-events:none"></div>
</div>
<div class="card" id="c2" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Гардероб</div><div class="ttl" style="color:#111">Стиль</div>
 <div class="ch" data-p="b"></div><div class="ch" data-p="m1"></div>
 <div id="ok2" style="position:absolute;left:300px;top:150px;background:#30d158;color:#fff;border-radius:18px;padding:10px 18px;font-size:24px;font-weight:900;opacity:0">мама одобряет ✓</div>
 <div id="cn2" class="c mono" style="bottom:20px;font-size:22px;font-weight:800;color:#8e8e93">образ 1/5</div>
</div>
<div class="card" id="c3" style="background:#000">
 <div class="hdr" style="color:#a6ff00">Цели</div><div class="ttl">Не сдаваться</div>
 <div style="position:absolute;left:30px;right:30px;top:160px"><div style="height:22px;border-radius:11px;background:#2c2c2e;overflow:hidden"><div id="pg3" style="height:22px;background:#a6ff00;width:0"></div></div>
  <div style="display:flex;justify-content:space-between;align-items:center;margin-top:20px;background:#1c1c1e;border-radius:20px;padding:14px 20px;font-size:24px;font-weight:700;opacity:.6">🏳️ Сдаться<div class="tg" id="tg3"><b></b></div></div></div>
 <div class="ch" data-p="c"></div><div class="ch" data-p="m2"></div>
</div>
<div class="card" id="c4" style="background:linear-gradient(160deg,#3a1a5a,#1a0a2a)">
 <div class="hdr" style="color:#d0a0ff">Постер контакта</div>
 <div class="c" style="top:70px;font-size:80px;font-weight:900;letter-spacing:-2px">МАМА ❤️</div>
 <div class="ch" data-p="m3"></div>
 <div id="sp4" style="position:absolute;inset:0;z-index:7"></div>
</div>
<div class="card" id="c5" style="background:#000">
 <div style="padding:26px 34px 16px;display:flex;align-items:center;gap:14px;border-bottom:1px solid #222"><div style="width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#d0a0ff,#bf5af2);display:flex;align-items:center;justify-content:center;font-size:30px">👩</div><div style="font-size:26px;font-weight:800">Мама ❤️</div></div>
 <div id="ms5" style="position:absolute;left:30px;right:30px;top:110px"></div>
 <div class="ch" data-p="d"></div>
 <div id="hh5" style="position:absolute;inset:0;z-index:7"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
const MOM=['#bf5af2','#ffe9a8','#e0a020'];
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;const m=p[0]=='m';e.id='ch_'+p;e.innerHTML=CH(p,...(m?MOM:['#64d2ff','#ff8ac4','#ff2d78']));
 const ns='http://www.w3.org/2000/svg';
 if(!m){const g=document.createElementNS(ns,'g');g.id=p+'_belt';g.innerHTML=`<rect x="54" y="196" width="92" height="18" fill="#111"/><rect x="88" y="192" width="24" height="26" rx="5" fill="#ffd60a" stroke="#b8860b" stroke-width="3"/><rect x="96" y="199" width="8" height="12" rx="2" fill="#b8860b"/>`;
  const ar=document.getElementById(p+'_armR');ar.parentNode.insertBefore(g,ar);}
 else{const hd=document.getElementById(p+'_head');hd.querySelectorAll('rect').forEach(r=>r.setAttribute('opacity','0'));
  const g=document.createElementNS(ns,'g');g.innerHTML=`<ellipse cx="80" cy="82" rx="11" ry="13" fill="#fff"/><ellipse cx="120" cy="82" rx="11" ry="13" fill="#fff"/><circle cx="81" cy="84" r="7" fill="#4a2a10" id="${p}_pl"/><circle cx="121" cy="84" r="7" fill="#4a2a10" id="${p}_pr"/><circle cx="83" cy="81" r="2.5" fill="#fff"/><circle cx="123" cy="81" r="2.5" fill="#fff"/><path d="M68 70 l-6 -6 M72 67 l-3 -8 M132 70 l6 -6 M128 67 l3 -8" stroke="#111" stroke-width="3" stroke-linecap="round"/><path d="M58 70 Q 50 120 70 140 M142 70 Q150 120 130 140" stroke="#5a3a1a" stroke-width="12" fill="none" stroke-linecap="round"/>`;hd.appendChild(g);}});
 let s='';for(let i=0;i<12;i++)s+=`<div id="k1_${i}" style="position:absolute;font-size:${24+i%3*12}px;opacity:0">✨</div>`;$('spk1').innerHTML=s;
 let s4='';for(let i=0;i<10;i++)s4+=`<div id="k4_${i}" style="position:absolute;font-size:${22+i%3*12}px;opacity:0">✨</div>`;$('sp4').innerHTML=s4;
 $('ms5').innerHTML=['ты у меня самый лучший 💗','одевайся теплее 🧣','горжусь тобой ❤️'].map((m,i)=>`<div id="m5_${i}" style="margin-bottom:12px;opacity:0"><div class="bub" style="background:#262628;font-size:26px">${m}</div></div>`).join('');
 let h='';for(let i=0;i<10;i++)h+=`<div id="h5_${i}" style="position:absolute;font-size:38px;opacity:0">💗</div>`;$('hh5').innerHTML=h;})();
const DRESS=[['#ff8ac4','#ff2d78'],['#7affa0','#30d158'],['#9ad8ff','#0a5ad8'],['#ffe27a','#d4a017'],['#ff8ac4','#ff2d78']];
function dress(p,c){$(p+'_s1').setAttribute('stop-color',c[0]);$(p+'_s2').setAttribute('stop-color',c[1]);$(p+'_s3').setAttribute('stop-color',c[1]);}
'''
RENDER='''
 {// S1 belt close-up: zoom from full body to waist
  const z=eo(seg(t,1.1,1.6));const s=lerp(1.2,3.2,z);const y=lerp(660,720,z);place('a',300,y,s,false);
  const show=t>=1.4;pose('a',t<0.4?{aL:8,aR:-150+Math.sin(t*12)*20,open:1}:(show?{aL:-33+Math.sin(t*6)*4,aR:33-Math.sin(t*6)*4,hd:-6,bob:-pop(t,2.0,6)*20}:{aL:8,aR:-8}));
  $('a_belt').querySelectorAll('rect')[1].setAttribute('fill',`hsl(48,100%,${50+25*Math.max(pop(t,2.0,4),pop(t,2.4,4),Math.max(0,Math.sin(t*6))*.4)}%)`);
  $('tag1').style.opacity=seg(t,2.0,2.15);$('tag1').style.transform=`scale(${1+.15*pop(t,2.0,6)})`;
  const bx=300,by=y+(205-290)*s;for(let i=0;i<12;i++){const ph=((t-1.4)*1.2+i/12)%1;const e=$('k1_'+i);e.style.opacity=show?(1-ph):0;e.style.left=(bx+Math.cos(i*.52)*(60+ph*150)-15)+'px';e.style.top=(by+Math.sin(i*.52)*(30+ph*90)-15)+'px';}}
 {// S2 mom dresses Lali
  const T=[3.0,3.4,4.1,5.0,5.5];let k=0;T.forEach((s,i)=>{if(t>=s)k=i});dress('b',DRESS[k]);$('cn2').textContent='образ '+(k+1)+'/5'+(k==4?' · идеально':'');
  place('b',230,660,1.15,false);pose('b',k==4?{aL:-33,aR:33,hd:-6,bob:-pop(t,5.5,6)*30}:{aL:8,aR:-8,bob:-pop(t,T[k],8)*14});
  place('m1',450,660,1.0,true);pose('m1',t>=5.5?{aL:8,aR:-150,open:1}:{aL:8,aR:-95+Math.sin(t*8)*10});$('ok2').style.opacity=seg(t,5.5,5.65);}
 {// S3 never give up
  const p=seg(t,6.6,8.4);$('pg3').style.width=(p*100)+'%';tog('tg3',false);
  place('c',lerp(140,300,p),680,1.0,false);pose('c',t<8.4?run(t,20):{aL:150,aR:-150,open:1,bob:-pop(t,8.4,5)*50});
  place('m2',470,680,.95,true);pose('m2',{aL:150+Math.sin(t*10)*15,aR:-150-Math.sin(t*10)*15,open:1});}
 {// S4 mom beautiful eyes
  place('m3',300,700,1.55,false);const e=t>=9.5;pose('m3',{aL:-58,aR:58,hd:-4+Math.sin(t*2)*3});
  const bl=Math.abs(Math.sin(t*1.7))<.06?.2:1;['m3_pl','m3_pr'].forEach(id=>$(id).setAttribute('transform',`scale(1 ${bl})`));
  for(let i=0;i<10;i++){const ph=((t-9.5)*1.1+i/10)%1;const el=$('k4_'+i);el.style.opacity=e&&t>=10.0?1-ph:(e?.4*(1-ph):0);el.style.left=(300+(i%2?65:-65)+Math.cos(i*1.3)*(30+ph*80)-14)+'px';el.style.top=(700+(82-290)*1.55+Math.sin(i*1.3)*(20+ph*60)-14)+'px';}}
 {// S5 warm words
  [10.6,11.1,11.6].forEach((s,i)=>{$('m5_'+i).style.opacity=seg(t,s,s+.1);$('m5_'+i).style.transform=`scale(${eb(seg(t,s,s+.25))})`;$('m5_'+i).style.transformOrigin='left';});
  place('d',420,680,1.0,true);pose('d',t>=11.1?{aL:-40,aR:40,hd:10}:{aL:8,aR:166,open:1});
  for(let i=0;i<10;i++){const ph=((t-11.1)*.7+i/10)%1;const el=$('h5_'+i);el.style.opacity=t>=11.1?1-ph:0;el.style.left=(420+Math.sin(i*2.3+ph*4)*90)+'px';el.style.top=(480-ph*260)+'px';}}
'''
