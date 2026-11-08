# NBS • Друзья — Кто пчёлок уважает (TikTok-тренд): подписка на пчёлку, не пристаёт, не жалят, доставка мёда
DUR=14.2; FADE=13.8; START=0
SONG='NBS • Друзья — Кто пчёлок уважает'
BG='linear-gradient(180deg,#141005,#050402)'
SUBW='900'
SUBX='text-transform:uppercase'
RED='мёд'
LINES=[
 [["кто",0.0],["пчёлок",0.26],["уважает,",1.02]],
 [["кто",2.18],["к",3.9],["ним",4.1],["не",4.34],["пристаёт",4.52]],
 [["того",5.86],["они",7.74],["не",8.2],["жалят,",8.5]],
 [["тому",10.06],["приносят",11.18],["мёд",12.02]],
]
SC=[[-0.3,2.15],[2.15,5.8],[5.8,10.0],[10.0,99]]
GLOW=['#7a5a0a','#3a3a5a','#1a5c2e','#8a5a0a']
PEMO=['🐝','🙅','🛡️','🍯']
END=[13.85,14.2]
CSS='''.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}
.msg{position:absolute;max-width:440px;padding:14px 20px;border-radius:24px;font-size:28px;font-weight:600}
.bee{position:absolute;font-size:46px;z-index:7}'''
HTML='''
<div class="card" id="c1" style="background:#fff7d6;color:#111">
 <div style="position:absolute;left:0;right:0;top:40px;text-align:center">
  <div style="width:150px;height:150px;margin:0 auto;border-radius:50%;background:conic-gradient(#ffd60a,#ff9f0a,#ffd60a);padding:6px"><div style="width:100%;height:100%;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;font-size:90px">🐝</div></div>
  <div style="font-size:36px;font-weight:900;margin-top:12px">pchyolka_official</div>
  <div style="font-size:22px;color:#8a7a3a;font-weight:700">🌼 улей №1 · мёд без сахара</div>
  <div style="display:flex;justify-content:center;gap:40px;margin-top:14px;font-size:22px;font-weight:700"><div><b id="fl1" class="mono" style="font-size:30px">9 999</b><br>уважают</div><div><b class="mono" style="font-size:30px">0</b><br>укусов</div></div>
  <div id="fb1" style="display:inline-block;margin-top:16px;padding:14px 60px;border-radius:16px;background:#0a84ff;color:#fff;font-size:28px;font-weight:900">Уважать</div></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#0e1621">
 <div style="position:absolute;left:0;right:0;top:0;height:86px;background:#17212b;display:flex;align-items:center;gap:16px;padding:0 26px;font-size:26px;font-weight:800">
  <div style="width:54px;height:54px;border-radius:50%;background:#ffd60a;display:flex;align-items:center;justify-content:center;font-size:30px">🐝</div>Пчёлка</div>
 <div style="position:absolute;left:20px;right:20px;bottom:24px;height:76px;border-radius:38px;background:#17212b;display:flex;align-items:center;padding:0 26px;font-size:28px;color:#fff">
  <span id="ty2"></span><span id="cr2" style="display:inline-block;width:3px;height:34px;background:#64b5ef;margin-left:2px"></span></div>
 <div class="ch" data-p="b"></div>
 <div id="np2" style="position:absolute;left:300px;top:150px;border:6px solid #ff453a;color:#ff453a;border-radius:16px;padding:4px 16px;font-size:36px;font-weight:900;opacity:0;z-index:8;transform:rotate(-10deg)">НЕ ПРИСТАЮ 🙅</div>
</div>
<div class="card" id="c3" style="background:linear-gradient(180deg,#bfe8ff,#e8f8d8 60%,#7ac65a 60%)">
 <div style="position:absolute;left:24px;right:24px;top:24px;background:rgba(255,255,255,.9);border-radius:22px;padding:14px 20px;color:#111;font-size:24px;font-weight:800;z-index:8">🩺 Здоровье · укусы сегодня: <span id="bt3" class="mono" style="color:#30a14e">0</span></div>
 <div class="ch" data-p="c"></div>
 <div id="sh3" style="position:absolute;left:150px;top:250px;width:300px;height:380px;border-radius:50%;border:5px solid rgba(48,209,88,.8);background:rgba(48,209,88,.12);opacity:0;z-index:6"></div>
 <div id="bees3"></div>
 <div id="ok3" style="position:absolute;left:330px;top:170px;background:#30d158;color:#06210f;border-radius:20px;padding:10px 18px;font-size:28px;font-weight:900;opacity:0;z-index:9">✅ не жалят — уважает</div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#ffd60a;color:#111;border-radius:22px;padding:14px 20px;font-size:24px;font-weight:900;z-index:8">
  🛵 Пчело-доставка<div id="st4" style="font-size:34px">курьер в пути…</div></div>
 <div class="ch" data-p="d"></div>
 <div id="cb4" class="bee" style="font-size:70px">🐝</div><div id="jr4" style="position:absolute;font-size:80px;z-index:8">🍯</div>
 <div id="drips4"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#ffd60a','#ffe27a','#d4a017');});
 let b='';for(let i=0;i<6;i++)b+=`<div class="bee" id="b3_${i}">🐝</div>`;$('bees3').innerHTML=b;
 let d='';for(let i=0;i<12;i++)d+=`<div id="h4_${i}" style="position:absolute;font-size:30px;z-index:7;opacity:0">💛</div>`;$('drips4').innerHTML=d;})();
'''
RENDER='''
 {// c1: подписка-уважение
  const on=t>=1.02;$('fb1').textContent=on?'Вы уважаете ✓':'Уважать';$('fb1').style.background=on?'#e5e5ea':'#0a84ff';$('fb1').style.color=on?'#111':'#fff';
  $('fb1').style.transform=`scale(${1+.15*pop(t,1.02,7)})`;$('fl1').textContent=on?'10 000':'9 999';
  place('a',300,690,0.95,false);pose('a',t<1.02?{aL:8,aR:-60,hd:-4}:{aL:-40,aR:40,hd:22});}
 {// c2: печатает «привет красивая» и стирает
  const full='привет, красивая 🐝 го гулять?';let n;
  if(t<3.9)n=Math.floor(full.length*seg(t,2.3,3.8));else n=Math.floor(full.length*(1-seg(t,3.9,4.4)));
  $('ty2').textContent=[...full].slice(0,Math.max(0,n)).join('');$('cr2').style.opacity=Math.sin(t*12)>0?1:0;
  place('b',300,560,1.0,false);pose('b',t<3.9?{aL:8,aR:166,hd:-6}:{aL:8,aR:-8,hd:-10,rot:-4});
  const np=seg(t,4.52,4.65);$('np2').style.opacity=np;$('np2').style.transform=`rotate(-10deg) scale(${lerp(2.2,1,eo(np))})`;}
 {// c3: пчёлы кружат, но не жалят
  place('c',300,640,1.1,false);pose('c',t<8.5?{aL:8,aR:-8,hd:Math.sin(t*3)*6}:{aL:55,aR:-55,hd:-6,open:1});
  for(let i=0;i<6;i++){const a=t*(1.6+i*.15)+i*1.05,r=150+20*Math.sin(t*2+i);const near=i==0?eo(seg(t,7.7,8.4))*(1-seg(t,8.5,9.0)):0;
   const e=$('b3_'+i);e.style.left=(275+Math.cos(a)*r*(1-near*.6))+'px';e.style.top=(400+Math.sin(a)*r*.7*(1-near*.6))+'px';e.style.transform=`scaleX(${Math.sin(a)>0?-1:1})`;}
  const sh=seg(t,8.5,8.7);$('sh3').style.opacity=sh*(.6+.4*Math.sin(t*10));$('ok3').style.opacity=seg(t,8.6,8.75);$('ok3').style.transform=`scale(${eb(seg(t,8.6,8.85))})`;}
 {// c4: курьер-пчела приносит мёд
  const fl=eo(seg(t,10.06,11.9));$('cb4').style.left=lerp(560,330,fl)+'px';$('cb4').style.top=(lerp(160,330,fl)+Math.sin(t*14)*8)+'px';
  const got=t>=12.02;$('st4').textContent=t<11.18?'курьер в пути…':(got?'доставлено ✅':'прилетел к двери');
  $('jr4').style.left=(got?250:lerp(560,330,fl)+10)+'px';$('jr4').style.top=(got?(340+4*Math.sin(t*5)):(lerp(160,330,fl)+60))+'px';$('jr4').style.transform=`scale(${1+.3*pop(t,12.02,6)})`;
  place('d',190,680,1.1,false);pose('d',got?{aL:150,aR:-150,open:1,bob:-Math.abs(Math.sin(t*9))*12}:{aL:8,aR:-95,hd:-4});
  for(let i=0;i<12;i++){const e=$('h4_'+i);const ph=((t-12.02)*.8+i/12)%1;e.style.opacity=got?(1-ph):0;e.style.left=(260+Math.sin(i*2.1+ph*3)*160)+'px';e.style.top=(560-ph*380)+'px';}}
'''
