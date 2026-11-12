DUR=16.9
FADE=16.5
START=43.0
SONG='АлСми — Танцуешь на поминках'
BG='linear-gradient(180deg,#0e0a14,#040306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["А",43.18],["я",44.08],["не",44.44],["верю",44.56],["никому,",45.0],["все",45.46],["и",45.62],["так",45.78],["это",45.96],["знают",46.16]],
 [["но",46.74],["почему",47.02],["тебе",47.88],["поверил,",48.24],["зая?",48.94]],
 [["ты",49.32],["на",49.86],["оружие",50.0],["не",50.62],["сдала",50.96],["экзамен",51.24]],
 [["поэтому",51.82],["стреляешь",52.42],["глазами",53.92]],
 [["вроде",54.54],["разошлись,",55.0],["и",55.84],["я",56.18],["рад",56.4]],
 [["у",56.66],["нас",57.0],["без",57.5],["ипотеки",57.66],["многоэтажный",58.44],["мат",59.48]],
]
SC=[[42.7,46.68],[46.68,49.26],[49.26,51.76],[51.76,54.48],[54.48,56.6],[56.6,99]]
GLOW=['#3a3a5a','#7a1f4a','#5a5a1a','#7a1f1f','#1a5c2e','#5a3a1a']
PEMO=['🕵️','🐰','📝','👀','✌️','🏢']
END=[59.5,59.9]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr">Доверие · список</div>
 <div id="ls1" style="position:absolute;left:30px;right:30px;top:80px;font-size:26px;font-weight:800;line-height:1.9"></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#ffd6e8,#ff9ac1);color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Доверие · исключение</div>
 <div style="position:absolute;left:30px;right:30px;top:80px;background:#fff;border-radius:20px;padding:14px 18px;font-size:30px;font-weight:900">🐰 зая — <span id="tr2" style="color:#1f8a3a">доверяю</span></div>
 <div id="qq2" style="position:absolute;left:360px;top:300px;font-size:100px;opacity:0;z-index:6">❓</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Экзамен на лицензию</div>
 <div style="position:absolute;left:40px;right:40px;top:90px;background:#fff;border-radius:20px;padding:18px;font-size:24px;font-weight:800;line-height:1.8">Кандидат: <u>она</u><br>Стрельба в тире: <span id="sc3" class="mono">—</span></div>
 <div id="st3" style="position:absolute;left:160px;top:300px;border:8px solid #d0021b;color:#d0021b;border-radius:16px;padding:6px 20px;font-size:46px;font-weight:900;transform:rotate(-10deg);opacity:0">НЕ СДАЛА</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:#000">
 <div id="ey4" class="c" style="top:110px;font-size:150px">👀</div>
 <div id="bm4" style="position:absolute;inset:0;z-index:5"></div>
 <div class="ch" data-p="d"></div>
 <div id="hp4" class="c" style="top:60px;font-size:28px;font-weight:900;color:#ff2d78;opacity:0">💘 прямое попадание</div>
</div>
<div class="card" id="c5" style="background:linear-gradient(180deg,#9fd3ff,#d8f0ff 60%,#8bc34a 61%,#5a8a2a)">
 <div class="ch" data-p="e"></div><div class="ch" data-p="f"></div>
 <div id="ok5" class="c" style="top:60px;font-size:36px;font-weight:900;color:#1f8a3a;opacity:0">😌 свобода</div>
</div>
<div class="card" id="c6" style="background:#e8eef4;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Новостройка «Отношения»</div>
 <div id="bl6" style="position:absolute;left:180px;bottom:40px;width:240px;display:flex;flex-direction:column-reverse;gap:4px"></div>
 <div id="ip6" style="position:absolute;right:24px;top:80px;background:#30d158;color:#fff;border-radius:14px;padding:8px 14px;font-size:22px;font-weight:900;opacity:0">ипотека: 0 ₽ ✅</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML='cdf'.includes(p)?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 $('ls1').innerHTML=['👨 друзья','👩 бывшие','📺 новости','🌦️ прогноз погоды'].map((s,i)=>`<div id="l1_${i}" style="opacity:0">${s} — <span style="color:#ff453a">❌ не верю</span></div>`).join('');
 let b='';for(let i=0;i<6;i++)b+=`<div id="b4_${i}" style="position:absolute;font-size:44px;opacity:0">💘</div>`;$('bm4').innerHTML=b;
 const W=['#$%!','@*&!','#!?','%$#@','!*#','@#$%','&%!','#@!'];$('bl6').innerHTML=W.map((w,i)=>`<div id="f6_${i}" style="height:52px;background:#8e8e93;border-radius:6px;display:flex;align-items:center;justify-content:space-around;color:#fff;font-weight:900;font-size:22px;opacity:0">🪟 ${w} 🪟</div>`).join('');})();
'''
RENDER='''
 {for(let i=0;i<4;i++)$('l1_'+i).style.opacity=seg(t,43.3+i*.7,43.4+i*.7);place('a',300,700,1.0,false);pose('a',{aL:8,aR:-8,hd:Math.sin(t*3)*10});}
 {$('tr2').textContent=t<48.94?'доверяю':'ПОЧЕМУ?!';$('tr2').style.color=t<48.94?'#1f8a3a':'#d0021b';$('qq2').style.opacity=seg(t,48.94,49.05);place('b',220,700,1.0,false);pose('b',t>=48.24?{aL:60,aR:-60,hd:10,open:1}:{aL:8,aR:-8});}
 {$('sc3').textContent=t<50.62?'—':'0 из 10 🎯';$('st3').style.opacity=seg(t,51.24,51.34);$('st3').style.transform=`rotate(-10deg) scale(${1+.4*pop(t,51.24,8)})`;place('c',470,700,.85,true);pose('c',{aL:8,aR:-8,hd:12});}
 {for(let i=0;i<6;i++){const s=52.42+i*.2;const k=seg(t,s,s+.4);const e=$('b4_'+i);e.style.opacity=k>0&&k<1?1:0;e.style.left=lerp(300,250,k)+'px';e.style.top=lerp(200,430,k)+'px';}
  $('hp4').style.opacity=seg(t,53.92,54.0);place('d',300,700,1.0,false);pose('d',t>=53.92?{aL:60,aR:-60,hd:14,open:1}:{aL:8,aR:-8});}
 {const k=eo(seg(t,54.6,55.8));place('e',lerp(260,120,k),700,.9,false);place('f',lerp(340,480,k),700,.9,true);pose('e',t>=56.18?{aL:150,aR:-150,open:1}:walk(t,8));pose('f',walk(t,8));$('ok5').style.opacity=seg(t,56.4,56.5);}
 {for(let i=0;i<8;i++)$('f6_'+i).style.opacity=seg(t,58.44+i*.12,58.5+i*.12);$('ip6').style.opacity=seg(t,57.66,57.76);}
'''
