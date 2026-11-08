BG='#050507'
SUBW='700'
LINES=[
 [["алко,",0.9],["трава,",1.25],["заны,",1.6],["никотин",2.0]],
 [["во",2.75],["мне",3.0],["все",3.25],["четыре",3.5]],
 [["в",4.5],["зубы",4.75],["палку",5.25],["закрутил",5.75]],
 [["взрыв,",6.25],["как",6.6],["C4",7.0]],
 [["слышу",7.75],["у",8.4],["эмси",8.5],["мои",9.0],["строчки",9.4]],
 [["они",10.0],["чё,",10.25],["тырят?",10.5]],
 [["с*ка",11.0],["делает",11.5],["хорошо",12.25],["мне",12.9]],
 [["садись,",13.25],["четыре",13.75]],
]
SC=[[-0.3,4.4],[4.4,7.6],[7.6,9.95],[9.95,10.95],[10.95,13.15],[13.15,99]]
GLOW=['#5a0a0a','#6a3a0a','#1d3a7a','#7a0a0a','#5a1d4a','#1d5a2a']
PEMO=['⚠️','💥','🎧','©️','🥵','📒']
END=[14.35,14.7]
HTML='''
<div class="card" id="c1" style="background:#000">
 <div class="hdr" style="color:#ff375f">Здоровье</div><div class="ttl">Во мне</div>
 <div style="display:flex;justify-content:center;gap:24px;margin-top:70px" id="dots"></div>
 <div class="c" style="top:360px"><div id="n1" class="mono" style="font-size:110px;font-weight:800">0/4</div><div id="w1" style="font-size:26px;font-weight:800;color:#ff453a;opacity:0">⚠️ все четыре</div></div>
</div>
<div class="card" id="c2" style="background:#0a0a0a">
 <div id="sp2" style="position:absolute;left:50%;top:150px;margin-left:-110px;width:220px;height:220px;border-radius:50%;border:18px solid #2c2c2e;border-top-color:#ff9f0a"></div>
 <div id="tm2" class="c mono" style="top:225px;font-size:64px;font-weight:800">C4</div>
 <div id="cd2" class="c" style="top:420px;font-size:30px;font-weight:800;color:#ff9f0a">закручиваю…</div>
 <div id="boom" style="position:absolute;inset:0;background:radial-gradient(circle,#fff 0%,#ffd60a 25%,#ff3b30 55%,transparent 75%);opacity:0;display:flex;align-items:center;justify-content:center;font-size:220px">💥</div>
 <svg id="crk" width="600" height="690" style="position:absolute;inset:0;opacity:0"><g stroke="rgba(255,255,255,.85)" stroke-width="3" fill="none">
  <path d="M300 345 L120 80 M300 345 L520 120 M300 345 L560 470 M300 345 L60 520 M300 345 L330 690 M300 345 L20 300 M300 345 L420 10"/>
  <path d="M210 210 L260 180 M420 240 L460 300 M180 430 L230 470 M400 420 L450 400"/></g></svg>
</div>
<div class="card" id="c3" style="background:linear-gradient(180deg,#0a4aff,#0a1a5a)">
 <div id="sz" style="position:absolute;left:50%;top:140px;width:240px;height:240px;margin-left:-120px;border-radius:50%;background:#fff;color:#0a4aff;display:flex;align-items:center;justify-content:center;font-size:150px;font-weight:900">S</div>
 <div id="rg" style="position:absolute;inset:0"></div>
 <div class="c" style="top:430px"><div id="t3a" style="font-size:34px;font-weight:900">Слушаю…</div><div id="t3b" style="font-size:24px;font-weight:600;color:#cfe0ff;margin-top:8px"></div></div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div style="position:absolute;left:40px;right:40px;top:140px;background:#3a0d12;border:3px solid #ff453a;border-radius:30px;padding:34px;text-align:center">
  <div style="font-size:90px">©️</div><div style="font-size:32px;font-weight:900;color:#ff453a;margin-top:10px">Нарушение авторских прав</div>
  <div style="font-size:22px;color:#ffb3ad;font-weight:600;margin-top:10px">Ваши строчки найдены у другого MC</div></div>
 <div id="cp4" class="c" style="bottom:60px;font-size:40px;font-weight:900;opacity:0">они чё, тырят? 🤨</div>
</div>
<div class="card" id="c5" style="background:#000">
 <div id="dnd" style="position:absolute;left:30px;right:30px;top:40px;background:#2c2c2e;border-radius:26px;padding:18px 22px;display:flex;align-items:center;gap:16px;font-size:26px;font-weight:800"><div id="dndi" style="width:56px;height:56px;border-radius:50%;background:#3a3a3c;display:flex;align-items:center;justify-content:center;font-size:30px">🌙</div><div>Не беспокоить<div id="dnds" style="font-size:19px;color:#8e8e93;font-weight:600">выкл.</div></div></div>
 <div class="c" style="top:190px"><div id="hr" style="font-size:150px;line-height:1">❤️</div><div id="bpm5" class="mono" style="font-size:72px;font-weight:800;margin-top:10px">72</div><div style="font-size:22px;color:#8e8e93;font-weight:700">уд/мин</div></div>
 <div id="w5" style="position:absolute;left:24px;right:24px;bottom:30px;background:rgba(60,60,64,.92);border-radius:26px;padding:18px 22px;display:flex;gap:16px;align-items:center;opacity:0">
  <div style="width:56px;height:56px;border-radius:14px;background:#ff2d55;display:flex;align-items:center;justify-content:center;font-size:30px">⌚️</div>
  <div><div style="font-size:22px;font-weight:800">Высокий пульс 🥵</div><div style="font-size:19px;color:#d1d1d6;font-weight:600">160 уд/мин, хотя вы не тренируетесь 👀</div></div></div>
</div>
<div class="card" id="c6" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:#0a84ff">Электронный дневник</div><div class="ttl" style="color:#111">Оценки</div>
 <div style="position:absolute;left:30px;right:30px;top:180px;background:#fff;border-radius:24px;padding:0 24px;box-shadow:0 6px 20px rgba(0,0,0,.08)">
  <div style="display:flex;justify-content:space-between;padding:22px 0;border-bottom:1px solid #eee;font-size:26px;font-weight:700"><span>Рэп</span><span style="color:#30d158">5</span></div>
  <div style="display:flex;justify-content:space-between;padding:22px 0;border-bottom:1px solid #eee;font-size:26px;font-weight:700"><span>Ночь 🔞</span><span style="color:#30d158">5</span></div>
  <div style="display:flex;justify-content:space-between;padding:22px 0;border-bottom:1px solid #eee;font-size:26px;font-weight:700"><span>Поведение</span><span style="color:#ff453a">2</span></div>
  <div style="display:flex;justify-content:space-between;padding:22px 0;font-size:26px;font-weight:700"><span>Ответ у доски</span><span id="g6" style="color:#8e8e93">—</span></div></div>
 <div id="big6" class="c" style="top:470px;font-size:140px;font-weight:900;color:#ff9f0a;opacity:0;line-height:1">4</div>
 <div id="sd6" class="c" style="bottom:30px;font-size:30px;font-weight:900;color:#111;opacity:0">садись.</div>
</div>
'''
BUILD='''(function(){$('dots').innerHTML=[0,1,2,3].map(i=>`<div id="d1_${i}" style="width:90px;height:90px;border-radius:50%;border:6px solid #3a3a3c"></div>`).join('');})();'''
RENDER='''
 {const T=[0.9,1.25,1.6,2.0];let n=0;T.forEach((s,i)=>{const on=t>=s;if(on)n++;const e=$('d1_'+i);e.style.background=on?'#ff453a':'transparent';e.style.borderColor=on?'#ff453a':'#3a3a3c';e.style.transform=`scale(${1+.3*pop(t,s,6)})`;e.style.boxShadow=on?'0 0 30px #ff453a':'none'});
  $('n1').textContent=n+'/4';$('n1').style.color=t>=3.5?'#ff453a':'#fff';$('w1').style.opacity=seg(t,3.5,3.65);if(si==0)shake('c1',t,3.5,8);}
 {$('sp2').style.transform=`rotate(${t*(t>=5.75?900:300)}deg)`;$('cd2').textContent=t>=6.25?'3… 2… 1…':(t>=5.75?'закрутил ✓':'закручиваю…');
  const b=seg(t,7.0,7.15);$('boom').style.opacity=t>=7.0?(1-seg(t,7.25,7.6))*1:0;$('boom').style.transform=`scale(${lerp(.3,1.4,eo(b))})`;$('crk').style.opacity=t>=7.15?1:0;if(si==1)shake('c2',t,7.0,16);}
 {let h='';for(let k=0;k<3;k++){const ph=((t*1.2)+k/3)%1;h+=`<div style="position:absolute;left:50%;top:260px;width:${240+ph*500}px;height:${240+ph*500}px;margin-left:-${(240+ph*500)/2}px;margin-top:-${(240+ph*500)/2}px;border-radius:50%;border:4px solid rgba(255,255,255,${(1-ph)*.5})"></div>`}$('rg').innerHTML=h;
  $('sz').style.transform=`scale(${1+.06*Math.sin(t*10)})`;const f=t>=9.4;$('t3a').textContent=f?'Совпадение найдено':'Слушаю…';$('t3b').textContent=f?'MC Кто-то · «мои строчки» · 100% моё':(t>=8.5?'у эмси…':'');}
 {$('cp4').style.opacity=seg(t,10.5,10.6);$('cp4').style.transform=`scale(${1+.3*pop(t,10.5,6)})`;if(si==3)shake('c4',t,10.0,10);}
 {const on=t>=11.0;$('dndi').style.background=on?'#5e5ce6':'#3a3a3c';$('dnds').textContent=on?'вкл. 🔞':'выкл.';$('dnd').style.background=on?'#2a2850':'#2c2c2e';
  const b=t<11.5?72:Math.round(lerp(72,160,eo(seg(t,11.5,12.9))));$('bpm5').textContent=b;$('bpm5').style.color=b>120?'#ff2d55':'#fff';$('hr').style.transform=`scale(${1+.12*Math.abs(Math.sin(t*b/60*Math.PI))})`;
  $('w5').style.opacity=seg(t,12.25,12.4);$('w5').style.transform=`translateY(${(1-eb(seg(t,12.25,12.5)))*40}px)`;}
 {const g=t>=13.75;$('g6').textContent=g?'4':'—';$('g6').style.color=g?'#ff9f0a':'#8e8e93';$('big6').style.opacity=seg(t,13.75,13.85);$('big6').style.transform=`scale(${lerp(2,1,eb(seg(t,13.75,13.95)))}) rotate(-8deg)`;$('sd6').style.opacity=seg(t,13.25,13.4);}
'''
