DUR=15.0
FADE=14.6
START=0
SONG='LOVV66 — 10М ОТ ДОМА'
BG='linear-gradient(180deg,#0e0a10,#050306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Да,",0.0],["никого",0.26],["кроме",0.96],["своих",1.42],["не",1.82],["впускал",2.32],["в",3.02],["свой",3.06],["дом",3.32]],
 [["никому",4.02],["кроме",4.64],["своих",5.06],["не",5.6],["смогу",6.04],["простить",6.58],["долг",7.16]],
 [["называй",7.68],["нас",8.38],["как",8.58],["хочешь,",8.94],["банда,",9.58],["гэнг",10.02],["или",10.46],["моб",10.6]],
 [["разговор",11.28],["будет",12.1],["коротким,",12.3],["если",13.26],["ты",13.54],["долбо*б",13.78]],
]
SC=[[-0.3,3.95],[3.95,7.6],[7.6,11.2],[11.2,99]]
GLOW=['#2a4a7a','#1a5c2e','#5a1d7a','#7a1f2a']
PEMO=['🚪','📒','🏴','📵']
END=[14.6,15.0]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#1c1c1e,#0a0a0c)">
 <div class="hdr">Домофон · Face ID</div><div class="ttl" style="font-size:36px">Вход: только свои</div>
 <div id="dr1" style="position:absolute;left:330px;top:170px;width:220px;height:420px;background:#5a3a1a;border:8px solid #3a2410;border-radius:12px;z-index:3"><div style="position:absolute;right:20px;top:200px;width:18px;height:18px;border-radius:50%;background:#ffd60a"></div></div>
 <div class="ch" data-p="a"></div><div class="ch" data-p="b"></div>
 <div id="ok1" style="position:absolute;left:330px;top:120px;background:#0f3a1f;color:#30d158;border-radius:16px;padding:8px 14px;font-size:24px;font-weight:900;opacity:0;z-index:8">✅ свой</div>
 <div id="no1" style="position:absolute;left:40px;top:150px;background:#3a0d12;color:#ff453a;border-radius:16px;padding:10px 16px;font-size:30px;font-weight:900;opacity:0;z-index:8">⛔ ОТКАЗАНО</div>
</div>
<div class="card" id="c2" style="background:#f4ecd8;color:#2a1f10">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Тетрадь долгов</div><div class="ttl">Кто сколько должен</div>
 <div id="ls2" style="position:absolute;left:30px;right:30px;top:150px"></div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c3" style="background:#000">
 <div class="hdr">Название группы</div>
 <div class="c" id="nm3" style="top:80px;font-size:60px;font-weight:900">…</div>
 <div class="c" style="top:165px;font-size:22px;color:#8e8e93;font-weight:700">3 участника · только свои</div>
 <div class="ch" data-p="d"></div><div class="ch" data-p="e"></div><div class="ch" data-p="f"></div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#2c2c2e,#0a0a0c)">
 <div class="c" style="top:60px;font-size:26px;color:#8e8e93;font-weight:700">Входящий вызов</div>
 <div class="c" style="top:100px;font-size:46px;font-weight:900">🤡 Незнакомец</div>
 <div class="c mono" id="tm4" style="top:170px;font-size:34px;color:#30d158">00:00</div>
 <div id="en4" class="c" style="top:220px;font-size:30px;font-weight:900;color:#ff453a;opacity:0">📵 Вызов завершён · 2 сек</div>
 <div class="ch" data-p="g"></div>
 <div id="hb4" style="position:absolute;left:430px;top:420px;width:100px;height:100px;border-radius:50%;background:#ff453a;display:flex;align-items:center;justify-content:center;font-size:50px;z-index:7">📞</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=p=='b'?CH(p,'#8e8e93','#c8c8cc','#8e8e93'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 const L=[['🧢 Брат','5 000 ₽',1],['🧢 Кореш','12 000 ₽',1],['🤡 Сосед','300 ₽',0],['🤡 Одноклассник','150 ₽',0]];
 $('ls2').innerHTML=L.map((r,i)=>`<div style="display:flex;align-items:center;justify-content:space-between;border-bottom:2px dashed rgba(0,0,0,.15);padding:10px 0;font-size:26px;font-weight:800;position:relative"><span>${r[0]}</span><span class="mono">${r[1]}</span><div id="st2_${i}" style="position:absolute;right:120px;top:2px;border:4px solid ${r[2]?'#1f8a3a':'#d0021b'};color:${r[2]?'#1f8a3a':'#d0021b'};border-radius:10px;padding:2px 10px;font-size:22px;font-weight:900;transform:rotate(-8deg);opacity:0">${r[2]?'ПРОЩЕНО':'НЕ ПРОЩЕНО'}</div></div>`).join('');})();
'''
RENDER='''
 {place('a',220,670,.9,false);place('b',lerp(-60,180,eo(seg(t,1.4,2.0))),670,.9,false);
  const inA=eo(seg(t,0.5,1.2));place('a',lerp(220,440,inA),670,.9,false);$('ok1').style.opacity=seg(t,0.4,0.5)*(1-seg(t,1.3,1.4));
  $('dr1').style.transform=`perspective(600px) rotateY(${(t>0.4&&t<1.3?-50:0)}deg)`;$('dr1').style.transformOrigin='left center';
  pose('a',walk(t,10));pose('b',t>=3.32?{aL:30,aR:-30,hd:10,open:1}:walk(t,10));$('no1').style.opacity=seg(t,3.32,3.45);$('no1').style.transform=`scale(${1+.3*pop(t,3.32,6)})`;
  $('ch_a').style.opacity=1-seg(t,1.2,1.35);}
 {[4.6,5.06,6.58,7.16].forEach((s,i)=>{$('st2_'+i).style.opacity=seg(t,s,s+.08);$('st2_'+i).style.transform=`rotate(-8deg) scale(${1+.6*pop(t,s,10)})`;});
  place('c',300,690,1.0,false);pose('c',t>=6.58?{aL:8,aR:-140,hd:-6}:{aL:8,aR:-30});}
 {$('nm3').textContent=t<9.58?'Без названия':(t<10.02?'🏴 Банда':(t<10.6?'⚡ Гэнг':'🕶 МОБ'));$('nm3').style.transform=`scale(${1+.2*(pop(t,9.58)+pop(t,10.02)+pop(t,10.6))})`;
  [['d',150,.0],['e',300,.15],['f',450,.3]].forEach(([p,x,d])=>{const k=eo(seg(t,7.8+d,8.4+d));place(p,x,lerp(900,690,k),1.0,p=='f');pose(p,t>=10.6?{aL:60,aR:-60,hd:0}:{aL:8,aR:-8,hd:-6});});}
 {const s=Math.min(2,Math.max(0,Math.floor(t-11.6)));$('tm4').textContent=t<11.6?'вызов…':'00:0'+s;
  place('g',300,690,1.1,false);const hu=t>=13.78;pose('g',hu?{aL:8,aR:-150,hd:-8}:{aL:8,aR:-30,hd:6});
  $('hb4').style.transform=`scale(${1+.3*pop(t,13.78,8)})`;$('en4').style.opacity=seg(t,13.85,13.95);$('tm4').style.opacity=hu?.3:1;}
'''
