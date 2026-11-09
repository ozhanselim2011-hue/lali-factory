DUR=16.9
FADE=16.5
START=1.7
SONG='FORTUNA 812 — sexy supra'
BG='linear-gradient(180deg,#140a0a,#050303)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Она",1.98],["говорит,",2.5],["я",3.04],["секси",3.22],["(секси)",3.76]],
 [["мы",4.26],["едем",4.68],["белой",5.02],["Супре",5.42],["(Supra)",6.0]],
 [["она",6.4],["говорит,",6.88],["чтоб",7.46],["я",7.6],["ехал",7.74],["быстрей",7.98]],
 [["и",8.48],["чтоб",8.86],["завязывал",9.04],["ей",9.66],["руки",9.76],["(с*чка)",10.24]],
 [["детка,",10.84],["ты",11.36],["же",11.48],["не",11.54],["в",11.68],["порядке",11.78],["(sexy)",12.48]],
 [["я",12.92],["всё",13.32],["скажу",13.38],["твоей",13.7],["подруге",13.96],["(Supra)",14.76]],
 [["I",15.28],["want",15.62],["it,",15.74],["I",16.02],["want",16.16],["it",16.36]],
 [["(Supra)",16.58],["I",17.38],["want",17.8],["it,",18.0],["I",18.18],["want",18.24],["it",18.46]],
]
SC=[[1.4,4.2],[4.2,6.35],[6.35,8.42],[8.42,10.8],[10.8,12.88],[12.88,15.22],[15.22,99]]
GLOW=['#7a1f4a','#5a5a6a','#7a1f1f','#7a5a1a','#7a1f2a','#5a1d7a','#7a1f0a']
PEMO=['🔥','🚗','🏁','🪢','🚨','🤫','🛒']
END=[18.2,18.6]
CSS='''.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}
.bub{position:absolute;max-width:400px;border-radius:24px;padding:12px 18px;font-size:28px;font-weight:800;opacity:0}'''
HTML='''
<div class="card" id="c1" style="background:#000">
 <div class="hdr">Чат · она 💋</div>
 <div class="bub" id="b1a" style="left:24px;top:90px;background:#2c2c2e">ты такой секси 🥵</div>
 <div class="bub" id="b1b" style="left:24px;top:170px;background:#2c2c2e">прям СЕКСИ 🔥🔥</div>
 <div id="sp1" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#ff8a3d,#ffb36b 50%,#333 51%,#1a1a1a)">
 <div id="rl2" style="position:absolute;inset:0"></div>
 <div id="cr2" style="position:absolute;left:150px;top:300px;width:300px;height:110px;z-index:4">
  <div style="position:absolute;left:0;top:40px;width:300px;height:60px;border-radius:30px 40px 14px 14px;background:#f5f5f7;box-shadow:inset 0 -8px 0 #cfcfd4"></div>
  <div style="position:absolute;left:80px;top:6px;width:140px;height:50px;border-radius:40px 50px 0 0;background:#f5f5f7"></div>
  <div style="position:absolute;left:95px;top:14px;width:110px;height:36px;border-radius:30px 40px 0 0;background:#9fd3ff"></div>
  <div style="position:absolute;left:40px;top:80px;width:44px;height:44px;border-radius:50%;background:#111;border:6px solid #888"></div>
  <div style="position:absolute;left:220px;top:80px;width:44px;height:44px;border-radius:50%;background:#111;border:6px solid #888"></div>
  <div style="position:absolute;left:115px;top:18px;font-size:26px">😎</div><div style="position:absolute;left:160px;top:18px;font-size:26px">👩</div></div>
 <div class="c" id="sp2" style="top:40px;font-size:40px;font-weight:900;color:#fff;opacity:0;text-shadow:0 4px 20px #000">белая SUPRA 🤍</div>
</div>
<div class="card" id="c3" style="background:#0a0a0c">
 <div class="hdr" style="color:#ff453a">Спидометр</div>
 <svg width="440" height="260" style="position:absolute;left:80px;top:120px"><path d="M30 230 A190 190 0 0 1 410 230" fill="none" stroke="#2c2c2e" stroke-width="28"/><path id="ar3" d="M30 230 A190 190 0 0 1 410 230" fill="none" stroke="#ff453a" stroke-width="28" stroke-dasharray="597" stroke-dashoffset="597"/>
  <line id="nd3" x1="220" y1="230" x2="60" y2="230" stroke="#fff" stroke-width="8" stroke-linecap="round"/></svg>
 <div class="c mono" id="kmh3" style="top:390px;font-size:70px;font-weight:900">60</div><div class="c" style="top:470px;font-size:24px;color:#8e8e93;font-weight:700">км/ч · «быстрее!» 👩</div>
 <div id="sh3" style="position:absolute;inset:0;pointer-events:none"></div>
</div>
<div class="card" id="c4" style="background:#f4ecd8;color:#2a1f10">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Урок 1 · узлы</div><div class="ttl">Как завязать бантик 🎀</div>
 <div id="st4" style="position:absolute;left:30px;right:30px;top:150px;font-size:26px;font-weight:800;line-height:1.8"></div>
 <div class="ch" data-p="b"></div>
 <div id="rp4" style="position:absolute;left:350px;top:440px;font-size:80px;z-index:6">🪢</div>
 <div id="ng4" style="position:absolute;left:300px;top:360px;font-size:60px;opacity:0;z-index:7">😵‍💫</div>
</div>
<div class="card" id="c5" style="background:#1c1c1e">
 <div class="hdr">Проверка адекватности</div>
 <div class="c" style="top:90px;font-size:110px">👩</div>
 <div id="rs5" class="c" style="top:260px;font-size:38px;font-weight:900;color:#ff453a;opacity:0">❌ не в порядке</div>
 <div style="position:absolute;left:60px;right:60px;top:330px;height:26px;border-radius:13px;background:#2c2c2e;overflow:hidden"><div id="mt5" style="height:26px;width:0;background:linear-gradient(90deg,#30d158,#ffd60a,#ff453a)"></div></div>
 <div class="c mono" id="pc5" style="top:370px;font-size:30px;font-weight:900">кринж: 0%</div>
 <div class="ch" data-p="c"></div>
 <div id="al5" style="position:absolute;inset:0;background:#ff0000;opacity:0;z-index:2"></div>
</div>
<div class="card" id="c6" style="background:#000">
 <div class="hdr">Чат · Её подруга Катя 👯</div>
 <div class="bub" id="b6a" style="right:24px;top:90px;background:#0a84ff">катя, нам надо поговорить</div>
 <div class="bub" id="b6b" style="right:24px;top:170px;background:#0a84ff">про твою подружку… 👀</div>
 <div class="bub" id="b6c" style="left:24px;top:260px;background:#2c2c2e">ЧТОО?? рассказывай 😳</div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c7" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Хочу · список желаний</div>
 <div style="position:absolute;left:30px;right:30px;top:80px;height:200px;border-radius:26px;background:linear-gradient(135deg,#dfe6ee,#fff);display:flex;align-items:center;justify-content:center"><div id="cr7" style="font-size:150px;filter:grayscale(1) brightness(1.7)">🚗</div></div>
 <div class="c" style="top:295px;font-size:30px;font-weight:900">белая Supra · 1 шт.</div>
 <div id="bt7" style="position:absolute;left:60px;right:60px;top:350px;height:70px;border-radius:35px;background:#ff2d55;color:#fff;font-size:30px;font-weight:900;display:flex;align-items:center;justify-content:center;z-index:7">I WANT IT · <span id="cn7" class="mono" style="margin-left:8px">0</span></div>
 <div class="ch" data-p="e"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 let s='';for(let i=0;i<12;i++)s+=`<div id="s1_${i}" style="position:absolute;font-size:${24+i%3*12}px;opacity:0">✨</div>`;$('sp1').innerHTML=s;
 let r='';for(let i=0;i<6;i++)r+=`<div id="r2_${i}" style="position:absolute;top:560px;width:70px;height:10px;border-radius:5px;background:#fff"></div>`;$('rl2').innerHTML=r;
 $('st4').innerHTML=['1. сделай петлю','2. ещё петлю','3. ???','4. узел на 40 минут'].map((s,i)=>`<div id="t4_${i}" style="opacity:0">${s}</div>`).join('');
 let l='';for(let i=0;i<8;i++)l+=`<div id="l3_${i}" style="position:absolute;height:4px;border-radius:2px;background:rgba(255,255,255,.5)"></div>`;$('sh3').innerHTML=l;})();
'''
RENDER='''
 {$('b1a').style.opacity=seg(t,3.04,3.15);$('b1b').style.opacity=seg(t,3.76,3.87);$('b1b').style.transform=`scale(${1+.2*pop(t,3.76,6)})`;
  place('a',300,690,1.15,false);const p=t>=3.22;pose('a',p?{aL:40,aR:-150,hd:-10,open:1}:{aL:8,aR:-8});
  for(let i=0;i<12;i++){const e=$('s1_'+i);e.style.opacity=p?Math.abs(Math.sin(t*8+i)):0;e.style.left=(300+Math.cos(i*.55)*(150+i*6))+'px';e.style.top=(450+Math.sin(i*.55)*(150+i*4))+'px';}}
 {for(let i=0;i<6;i++){const e=$('r2_'+i);e.style.left=((((-t*900+i*130)%780)+780)%780-90)+'px';}$('cr2').style.transform=`translateY(${Math.sin(t*25)*2}px)`;
  $('sp2').style.opacity=seg(t,6.0,6.1);$('sp2').style.transform=`scale(${1+.2*pop(t,6.0,6)})`;}
 {const k=eo(seg(t,6.9,8.3));const v=Math.round(lerp(60,280,k));$('kmh3').textContent=v;$('kmh3').style.color=v>200?'#ff453a':'#fff';$('ar3').setAttribute('stroke-dashoffset',597*(1-k));
  const a=Math.PI*(1-k);$('nd3').setAttribute('x2',220+Math.cos(a)*160);$('nd3').setAttribute('y2',230-Math.sin(a)*160);
  for(let i=0;i<8;i++){const e=$('l3_'+i);e.style.opacity=k*.8;e.style.top=(80+i*75)+'px';e.style.width=(60+k*200)+'px';e.style.left=((((-t*2000+i*190)%800)+800)%800-100)+'px';}}
 {[8.86,9.04,9.66,9.76].forEach((s,i)=>$('t4_'+i).style.opacity=seg(t,s,s+.1));place('b',220,690,1.0,false);const c=t>=10.24;pose('b',c?{aL:40,aR:-40,hd:Math.sin(t*14)*10,open:1}:{aL:8,aR:-60,hd:-6});
  $('rp4').style.transform=`rotate(${t*200}deg)`;$('ng4').style.opacity=seg(t,10.24,10.35);}
 {const k=eo(seg(t,11.0,11.78));$('mt5').style.width=(k*100)+'%';$('pc5').textContent='кринж: '+Math.round(k*100)+'%';$('rs5').style.opacity=seg(t,11.78,11.9);
  $('al5').style.opacity=t>=12.48?.25*Math.abs(Math.sin(t*12)):0;place('c',300,690,1.0,false);pose('c',t>=11.78?{aL:60,aR:-60,hd:12,open:1}:{aL:8,aR:-8,hd:-6});}
 {['b6a','b6b','b6c'].forEach((id,i)=>{const s=[13.32,13.96,14.76][i];$(id).style.opacity=seg(t,s,s+.1);$(id).style.transform=`scale(${eb(seg(t,s,s+.25))})`;});
  place('d',130,690,.9,false);pose('d',t>=14.76?{aL:8,aR:-150,hd:-6}:{aL:8,aR:-80,hd:-6});}
 {const hits=[15.62,16.16,16.58,17.8,18.24];let n=0;let pp=0;hits.forEach(h=>{if(t>=h)n++;pp+=pop(t,h,10);});$('cn7').textContent=n;
  $('bt7').style.transform=`scale(${1-.08*Math.min(1,pp)})`;$('cr7').style.transform=`scale(${1+.15*Math.min(1,pp)}) rotate(${Math.sin(t*6)*4}deg)`;
  place('e',480,690,.85,true);pose('e',{aL:8,aR:-90+40*Math.min(1,pp),open:pp>.3?1:0,bob:-Math.abs(Math.sin(t*9))*8});}
'''
