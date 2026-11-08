BG='#070506'
SUBW='900'
SUBX='text-transform:uppercase'
RED='наполовину'
LINES=[
 [["есть",0.0],["101",0.4],["причина",1.0]],
 [["сказать,",1.8],["что",2.7],["любишь",2.8],["меня",3.4]],
 [["только",3.6],["лишь",4.1],["наполовину",4.5]],
 [["я",5.7],["не",6.2],["могу",6.4],["это",6.8],["скрывать",7.3]],
 [["деньги",8.0],["меняют",8.5],["сильно",9.1]],
 [["хотел",9.5],["её",10.4],["нарисовать",10.7]],
 [["неполная",11.8],["картина",12.6]],
 [["лишь",13.4],["о",13.9],["тебе,",14.0],["тебе,",14.6],["тебе",15.5]],
 [["я",16.2],["думал",16.4],["лишь",17.5],["о",17.7],["тебе…",18.0]],
]
SC=[[-0.3,1.7],[1.7,5.6],[5.6,7.95],[7.95,9.45],[9.45,11.75],[11.75,13.35],[13.35,16.15],[16.15,99]]
GLOW=['#3a1d3a','#5a0a1a','#3a3a3a','#1a5c2e','#3a2a5a','#6a2a0a','#5a0a2a','#3a0a1a']
PEMO=['📝','🔋','🙈','💸','✏️','🔥','💭','🖤']
END=[18.6,19.1]
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr" style="color:#ffd60a">Заметки</div><div class="ttl">Причины</div>
 <div id="cn1" class="c mono" style="top:170px;font-size:140px;font-weight:800">0</div>
 <div id="ls1" style="position:absolute;left:30px;right:30px;top:360px;font-size:24px;font-weight:600;color:#aeaeb2;line-height:1.7"></div>
</div>
<div class="card" id="c2" style="background:#000">
 <div class="hdr">Аккумулятор</div><div class="ttl">Любовь ко мне</div>
 <div style="position:absolute;left:90px;top:190px;width:400px;height:180px;border-radius:36px;border:8px solid #48484a;padding:10px"><div id="bt" style="height:100%;border-radius:24px;background:#30d158;width:0"></div>
  <div style="position:absolute;right:-26px;top:58px;width:16px;height:48px;border-radius:0 8px 8px 0;background:#48484a"></div></div>
 <div id="bp" class="c mono" style="top:400px;font-size:64px;font-weight:800">0%</div>
 <div id="opt" style="position:absolute;left:30px;right:30px;bottom:30px;background:#1c1c1e;border-radius:24px;padding:18px 22px;font-size:23px;font-weight:700;opacity:0">⚡️ Оптимизированная зарядка<div style="font-size:20px;color:#8e8e93;font-weight:600;margin-top:4px">заряд остановлен на 50% · только наполовину</div></div>
</div>
<div class="card" id="c3" style="background:#1c1c1e">
 <div class="hdr" style="color:#0a84ff">‹ Настройки · Фото</div><div class="ttl">Скрытое</div>
 <div style="padding:30px 30px 0"><div class="row" style="background:#2c2c2e">🙈 <span>Скрыть чувства</span><div class="tg" id="tg3"><b></b></div></div></div>
 <div id="er3" style="position:absolute;left:30px;right:30px;top:300px;background:#3a0d12;border-radius:24px;padding:22px;opacity:0"><div style="font-size:28px;font-weight:900;color:#ff453a">✕ Не удаётся скрыть</div><div style="font-size:21px;color:#ffb3ad;font-weight:600;margin-top:6px">слишком заметно. попробуйте никогда.</div></div>
</div>
<div class="card" id="c4" style="background:#000">
 <div class="hdr">Wallet</div>
 <div id="bl4" class="c mono" style="top:90px;font-size:64px;font-weight:800;color:#30d158">$0</div>
 <div class="c" style="top:200px;font-size:200px;line-height:1" id="fc4">🙂</div>
 <div id="t4" class="c" style="bottom:50px;font-size:30px;font-weight:900;opacity:0">меняют сильно</div>
</div>
<div class="card" id="c5" style="background:#f5f3ee;color:#111">
 <div class="hdr" style="color:#ff9f0a">Freeform · без названия</div>
 <svg width="600" height="520" style="position:absolute;top:90px;left:0"><g fill="none" stroke="#111" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" id="drw">
  <path d="M300 60 C 200 60 160 140 170 220 C 180 300 230 350 300 360 C 370 350 420 300 430 220 C 440 140 400 60 300 60"/>
  <path d="M170 180 C 150 100 230 30 300 40 C 380 30 460 100 430 190"/>
  <path d="M240 200 q 15 -12 30 0"/><path d="M330 200 q 15 -12 30 0"/><path d="M295 230 q -8 30 8 40"/><path d="M265 300 q 35 22 70 0"/>
  <path d="M300 360 L300 420 M220 420 C 260 400 340 400 380 420 L420 520 M220 420 L180 520"/></g></svg>
 <div id="pen" style="position:absolute;font-size:60px;margin:-50px 0 0 -6px">✏️</div>
</div>
<div class="card" id="c6" style="background:#000">
 <div class="hdr">Фото</div>
 <div style="position:absolute;left:60px;right:60px;top:90px;height:440px;border-radius:24px;overflow:hidden;background:#1c1c1e">
  <div id="img6" style="position:absolute;left:0;right:0;top:0;height:0;background:linear-gradient(180deg,#f5f3ee,#e8e4da);overflow:hidden"><svg width="480" height="440"><g fill="none" stroke="#111" stroke-width="5"><path d="M240 50 C 160 50 120 120 130 190 C 140 260 180 300 240 310 C 300 300 340 260 350 190 C 360 120 320 50 240 50"/><path d="M190 175 q 12 -10 24 0"/><path d="M265 175 q 12 -10 24 0"/></g></svg></div>
  <div id="fire" style="position:absolute;left:0;right:0;bottom:0;height:120px;background:linear-gradient(0deg,#ff3b00,#ff9f0a 40%,transparent);opacity:0"></div></div>
 <div class="c" style="bottom:50px"><div id="t6" style="font-size:30px;font-weight:900">загрузка…</div><div id="t6b" class="mono" style="font-size:22px;color:#8e8e93;font-weight:700;margin-top:6px">0%</div></div>
</div>
<div class="card" id="c7" style="background:#1c1c1e">
 <div class="hdr">Экранное время</div><div class="ttl">Мысли</div>
 <div id="rows7" style="position:absolute;left:30px;right:30px;top:180px"></div>
</div>
<div class="card" id="c8" style="background:#000">
 <div id="hb" class="c" style="top:120px;font-size:220px">🖤</div>
 <div class="c" style="top:420px"><div id="t8" style="font-size:40px;font-weight:900"></div><div style="font-size:22px;color:#8e8e93;font-weight:600;margin-top:8px">последняя мысль · только что</div></div>
</div>
'''
BUILD='''(function(){$('ls1').innerHTML=['1. ты врёшь красиво','2. ты рядом, но не вся','3. ты отвечаешь через час','…'].map((l,i)=>`<div id="l1_${i}" style="opacity:0">${l}</div>`).join('');
 $('rows7').innerHTML=[0,1,2].map(i=>`<div id="r7_${i}" style="margin-bottom:18px;opacity:0"><div style="display:flex;justify-content:space-between;font-size:28px;font-weight:800"><span>💭 о тебе</span><span class="mono" style="color:#ff2d55">${['8 ч','16 ч','24 ч'][i]}</span></div><div style="height:16px;border-radius:8px;background:#3a3a3c;margin-top:10px;overflow:hidden"><div id="rb7_${i}" style="height:16px;background:#ff2d55;width:0"></div></div></div>`).join('');})();'''
RENDER='''
 {const n=t<0.4?0:(t<1.0?Math.round(seg(t,0.4,1.0)*100):101);$('cn1').textContent=n;$('cn1').style.transform=`scale(${1+.2*pop(t,1.0,6)})`;[0.4,0.7,1.0,1.3].forEach((s,i)=>$('l1_'+i).style.opacity=seg(t,s,s+.1));}
 {const p=t<2.8?seg(t,1.9,2.8)*.3:(t<4.5?lerp(.3,.5,seg(t,2.8,4.5)):.5);$('bt').style.width=(p*100)+'%';$('bp').textContent=Math.round(p*100)+'%';$('bt').style.background=t>=4.5?'#ffd60a':'#30d158';$('opt').style.opacity=seg(t,4.5,4.65);$('bp').style.transform=`scale(${1+.2*pop(t,4.5,6)})`;}
 {const tr=t>=6.4&&t<7.3;tog('tg3',tr);$('er3').style.opacity=seg(t,7.3,7.45);if(si==2)shake('c3',t,7.3,10);}
 {const b=t<8.5?0:lerp(0,999999,eo(seg(t,8.5,9.2)));$('bl4').textContent='$'+fmt(b);$('fc4').textContent=t>=9.1?'😈':(t>=8.5?'😏':'🙂');$('fc4').style.transform=`scale(${1+.3*pop(t,9.1,5)})`;$('t4').style.opacity=seg(t,9.1,9.2);}
 {const ps=[...$('drw').children];const p=seg(t,10.0,11.7);ps.forEach((e,i)=>{const L=e.getTotalLength();e.style.strokeDasharray=L;const q=cl(p*ps.length-i);e.style.strokeDashoffset=L*(1-q);});
  const k=Math.min(ps.length-1,Math.floor(p*ps.length));try{const e=ps[k];const L=e.getTotalLength();const pt=e.getPointAtLength(L*cl(p*ps.length-k));$('pen').style.left=pt.x+'px';$('pen').style.top=(pt.y+90)+'px';}catch(e){}$('pen').style.opacity=t>=10.0&&t<11.7?1:0;}
 {const h=t<12.6?seg(t,11.8,12.6)*.5:.5;$('img6').style.height=(h*440)+'px';$('t6').textContent=t>=12.6?'неполная картина':'загрузка…';$('t6').style.color=t>=12.6?'#ff9f0a':'#fff';$('t6b').textContent=Math.round(h*100)+'%'+(t>=12.6?' · сбой':'');$('fire').style.opacity=t>=12.6?.6+.3*Math.sin(t*20):0;}
 {[14.0,14.6,15.5].forEach((s,i)=>{$('r7_'+i).style.opacity=seg(t,s,s+.1);$('rb7_'+i).style.width=(eo(seg(t,s,s+.4))*[33,66,100][i])+'%';});}
 {const q='думал о тебе…';$('t8').textContent=q.slice(0,Math.max(0,Math.min(q.length,Math.floor((t-16.4)*8))));$('hb').textContent=t>=18.0?'❤️':'🖤';$('hb').style.transform=`scale(${1+.08*Math.abs(Math.sin(t*4))+.3*pop(t,18.0,4)})`;}
'''
