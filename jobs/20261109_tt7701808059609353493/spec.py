DUR=16.9
FADE=16.5
START=18.2
SONG='NEXTIME & Даник — КИС Ю'
BG='linear-gradient(180deg,#140a14,#050306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["I",18.36],["wanna",18.6],["kiss",18.84],["you,",19.9],["в",20.38],["смысле,",20.46],["я",20.84],["по-английски",21.04]],
 [["но",22.42],["мы",22.6],["с",22.92],["тобой",23.0],["разные,",23.34],["как",24.36],["пёсики",24.72],["и",25.42],["киски",25.68]],
 [["а",26.56],["помнишь,",26.78],["были",27.44],["близки,",27.64],["а",28.78],["теперь",28.96],["далеки",29.4]],
 [["как",30.92],["тут",31.36],["плохо",31.78],["уже",32.46],["знают",32.88],["все",33.58],["таксисты",33.82]],
]
SC=[[17.9,22.35],[22.35,26.5],[26.5,30.85],[30.85,99]]
GLOW=['#2a4a7a','#7a5a1a','#1a5c4e','#7a6a0a']
PEMO=['💋','🐶','📍','🚕']
END=[34.7,35.1]
CSS='''.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}
.bub{position:absolute;left:24px;max-width:420px;border-radius:22px;padding:10px 16px;font-size:22px;font-weight:700;background:#2c2c2e;opacity:0}'''
HTML='''
<div class="card" id="c1" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Переводчик</div>
 <div style="position:absolute;left:24px;right:24px;top:80px;background:#fff;border-radius:22px;padding:16px 20px"><div style="font-size:18px;color:#8e8e93;font-weight:700">АНГЛИЙСКИЙ</div><div id="en1" style="font-size:36px;font-weight:800">I wanna kiss you</div></div>
 <div style="position:absolute;left:24px;right:24px;top:210px;background:#0a84ff;color:#fff;border-radius:22px;padding:16px 20px;opacity:0" id="ru1"><div style="font-size:18px;opacity:.7;font-weight:700">РУССКИЙ</div><div style="font-size:34px;font-weight:800">я хочу тебя поцеловать 💋</div></div>
 <div class="ch" data-p="a"></div>
 <div id="bl1" style="position:absolute;left:330px;top:380px;font-size:50px;opacity:0;z-index:6">😳</div>
</div>
<div class="card" id="c2" style="background:linear-gradient(90deg,#ffd9a8 50%,#ffc2e0 50%);color:#111">
 <div class="c" style="top:30px;font-size:30px;font-weight:900">Тест на совместимость</div>
 <div id="dg2" style="position:absolute;left:60px;top:150px;font-size:150px">🐶</div><div id="ct2" style="position:absolute;right:60px;top:150px;font-size:150px">🐱</div>
 <div class="c mono" id="pc2" style="top:370px;font-size:70px;font-weight:900;color:#d0021b">100%</div>
 <div class="ch" data-p="b"></div><div class="ch" data-p="c"></div>
</div>
<div class="card" id="c3" style="background:#d8e6d0">
 <svg width="600" height="690" style="position:absolute;left:0;top:0"><path d="M0 200 L600 260 M0 450 L600 380 M150 0 L220 690 M420 0 L380 690" stroke="#fff" stroke-width="18"/><path d="M0 560 Q300 500 600 600" stroke="#ffd60a" stroke-width="14" fill="none"/></svg>
 <div id="pa3" style="position:absolute;font-size:60px">📍</div><div id="pb3" style="position:absolute;font-size:60px;filter:hue-rotate(200deg)">📍</div>
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#fff;color:#111;border-radius:22px;padding:14px 20px;font-size:26px;font-weight:800;z-index:6">Расстояние до неё: <span id="km3" class="mono" style="color:#0a84ff">0,1 км</span></div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c4" style="background:#111214">
 <div class="hdr" style="color:#ffd60a">🚕 Такси · чаты с водителями</div>
 <div class="bub" id="m1" style="top:80px">Ашот: опять на её улицу? 🤨</div>
 <div class="bub" id="m2" style="top:150px">Сергей: брат, она не стоит того</div>
 <div class="bub" id="m3" style="top:220px">Тимур: я в курсе, мне Ашот рассказал</div>
 <div class="bub" id="m4" style="top:290px;background:#ffd60a;color:#111">⭐ 5 водителей знают твою историю</div>
 <div class="ch" data-p="e"></div>
 <div id="tr4" style="position:absolute;left:300px;top:520px;font-size:40px;opacity:0;z-index:6">💧</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});})();
'''
RENDER='''
 {$('ru1').style.opacity=seg(t,19.9,20.05);$('ru1').style.transform=`scale(${eb(seg(t,19.9,20.2))})`;place('a',220,690,1.0,false);
  pose('a',t>=20.46?{aL:40,aR:-40,hd:Math.sin(t*10)*6}:{aL:8,aR:-30});$('bl1').style.opacity=seg(t,19.95,20.1);}
 {const v=Math.round(lerp(100,12,eo(seg(t,23.3,25.9))));$('pc2').textContent=v+'%';$('pc2').style.color=v>50?'#1f8a3a':'#d0021b';
  $('dg2').style.transform=`translateY(${-Math.abs(Math.sin(t*8))*14*(t>=24.72?1:0)}px)`;$('ct2').style.transform=`translateY(${-Math.abs(Math.sin(t*8))*14*(t>=25.68?1:0)}px)`;
  place('b',170,690,.9,false);place('c',430,690,.9,true);const s=t>=24.36;pose('b',s?{aL:8,aR:-8,hd:-14}:{aL:8,aR:-8});pose('c',s?{aL:8,aR:-8,hd:-14}:{aL:8,aR:-8});}
 {const d=eo(seg(t,28.8,30.6));$('pa3').style.left=lerp(270,60,d)+'px';$('pa3').style.top=lerp(330,200,d)+'px';$('pb3').style.left=lerp(300,500,d)+'px';$('pb3').style.top=lerp(340,560,d)+'px';
  $('km3').textContent=(t<28.8?'0,1':fmt(lerp(0,1240,d)))+' км';place('d',140,690,.9,false);pose('d',t>=29.4?{aL:8,aR:-8,hd:14}:{aL:8,aR:-60});}
 {['m1','m2','m3','m4'].forEach((id,i)=>{const s=[31.3,32.4,33.2,33.8][i];$(id).style.opacity=seg(t,s,s+.1);$(id).style.transform=`translateY(${(1-eo(seg(t,s,s+.25)))*20}px)`;});
  place('e',300,700,1.05,false);pose('e',{aL:8,aR:-8,hd:14});$('tr4').style.opacity=t>31.78?1:0;$('tr4').style.top=(520+((t*1.6)%1)*80)+'px';}
'''
