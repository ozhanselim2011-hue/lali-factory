DUR=17.0
FADE=16.6
START=0
SONG='WokkHelly — До-Ре-Ми 2'
BG='linear-gradient(180deg,#0e0a16,#040306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Хочу",0.0],["тебя",0.34],["сыграть,",0.62],["но",1.4],["не",1.64],["нужны",1.8],["твои",2.28]],
 [["ноты",2.72],["—",3.0],["свои",3.26],["покажи",3.54]],
 [["до-ре-ми,",4.54],["фа-соль,",5.24],["ля-си",5.82]],
 [["устроился",6.44],["в",7.3],["такси,",7.52],["чтобы",8.02],["тебя",8.4],["довезти",8.94]],
 [["не",9.84],["из",10.12],["точки,",10.26],["а",10.74],["в",10.96],["точку",11.1],["G",11.5]],
 [["оп,",11.64],["не",12.08],["в",12.24],["сказке,",12.34],["но",12.86],["жил-был",12.98]],
 [["киса,",13.54],["куплю",13.98],["Miu",14.56],["Miu",14.82]],
 [["на",15.12],["тачке",15.28],["врум-врум,",15.9],["би-би",16.44]],
]
SC=[[-0.3,2.65],[2.65,4.45],[4.45,6.38],[6.38,9.78],[9.78,11.58],[11.58,13.48],[13.48,15.05],[15.05,99]]
GLOW=['#5a1d7a','#7a1f4a','#1a4a7a','#7a6a0a','#1a5c4e','#7a5a1a','#7a1f4a','#7a1f1f']
PEMO=['🎹','🎼','🎵','🚕','📍','📖','👜','🚗']
END=[16.6,17.0]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr">Пианино · новый трек</div><div class="ttl">Сыграть: <span style="color:#ff8ac4">она 💖</span></div>
 <div style="position:absolute;left:40px;right:40px;top:150px;height:200px;background:#fff;border-radius:16px;color:#111;padding:16px"><div style="font-size:20px;font-weight:800;color:#8e8e93">её ноты</div><div style="font-size:60px;letter-spacing:6px">♩♪♫♬♩</div></div>
 <div id="no1" style="position:absolute;left:150px;top:200px;border:6px solid #ff453a;color:#ff453a;border-radius:14px;padding:4px 16px;font-size:40px;font-weight:900;transform:rotate(-10deg);opacity:0;z-index:6">НЕ НУЖНЫ</div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#ffd6e8,#ff9ac1);color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Мои ноты</div>
 <div id="sh2" style="position:absolute;left:60px;right:60px;top:90px;height:220px;background:#fff;border-radius:18px;padding:16px;transform-origin:50% 100%"><div style="font-size:20px;font-weight:800;color:#ff2d78">для тебя 💌</div><div style="font-size:60px;letter-spacing:6px">💖♪💖♫💖</div></div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#111214">
 <div class="hdr">Гамма</div>
 <div id="ky3" style="position:absolute;left:30px;right:30px;top:200px;height:300px;display:flex;gap:6px"></div>
</div>
<div class="card" id="c4" style="background:#ffd60a;color:#111">
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#fff;border-radius:22px;padding:14px 18px;z-index:6"><div style="font-size:20px;color:#8e8e93;font-weight:700">Такси · водитель</div><div style="font-size:30px;font-weight:900">🧢 Лали · ⭐ 5.0</div><div id="ps4" style="font-size:22px;font-weight:800;color:#ff2d78;opacity:0">пассажир: она 💖 · бесплатно</div></div>
 <div id="rd4" style="position:absolute;left:0;right:0;top:470px;height:120px;background:#333"></div><div id="ln4" style="position:absolute;inset:0"></div>
 <div id="tx4" style="position:absolute;left:160px;top:350px;font-size:180px;transform:scaleX(-1);z-index:4">🚕</div>
</div>
<div class="card" id="c5" style="background:#d8e6d0">
 <svg width="600" height="690" style="position:absolute"><path d="M0 220 L600 280 M0 480 L600 400 M170 0 L230 690 M430 0 L390 690" stroke="#fff" stroke-width="18"/><path id="rt5" d="M120 560 Q300 120 470 260" stroke="#0a84ff" stroke-width="12" fill="none" stroke-dasharray="700" stroke-dashoffset="700"/></svg>
 <div id="pa5" style="position:absolute;left:90px;top:500px;background:#fff;border-radius:16px;padding:6px 12px;font-size:28px;font-weight:900;color:#111">📍 A</div>
 <div id="xa5" style="position:absolute;left:96px;top:470px;font-size:70px;opacity:0">❌</div>
 <div id="pg5" style="position:absolute;left:430px;top:200px;background:#ff2d78;border-radius:16px;padding:6px 14px;font-size:30px;font-weight:900;color:#fff;opacity:0">📍 G</div>
</div>
<div class="card" id="c6" style="background:linear-gradient(180deg,#3a1a0a,#1a0a04)">
 <div style="position:absolute;left:60px;right:60px;top:80px;height:360px;background:#f4ecd8;border-radius:10px 24px 24px 10px;color:#3a2410;padding:24px;box-shadow:inset 18px 0 0 #c8b890"><div style="font-size:24px;font-weight:700;font-style:italic">Жили-были…</div><div style="font-size:90px;text-align:center;margin-top:20px">🏰</div></div>
 <div id="st6" style="position:absolute;left:180px;top:200px;border:6px solid #d0021b;color:#d0021b;border-radius:14px;padding:4px 16px;font-size:36px;font-weight:900;transform:rotate(-8deg);opacity:0;z-index:6">НЕ СКАЗКА</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c7" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Корзина</div>
 <div style="position:absolute;left:30px;right:30px;top:80px;height:200px;border-radius:26px;background:#fff;display:flex;align-items:center;gap:20px;padding:0 24px"><div style="font-size:110px">👜</div><div><div style="font-size:30px;font-weight:900">Miu Miu</div><div style="font-size:22px;color:#8e8e93;font-weight:700">для кисы 🐱</div><div class="mono" style="font-size:30px;font-weight:900">189 990 ₽</div></div></div>
 <div id="bt7" style="position:absolute;left:60px;right:60px;top:300px;height:70px;border-radius:35px;background:#000;color:#fff;font-size:28px;font-weight:900;display:flex;align-items:center;justify-content:center">Оплатить</div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c8" style="background:linear-gradient(180deg,#ff8a3d,#ffb36b 55%,#333 56%,#1a1a1a)">
 <div id="ln8" style="position:absolute;inset:0"></div>
 <div id="cr8" style="position:absolute;left:150px;top:330px;font-size:180px;transform:scaleX(-1);z-index:4">🚗</div>
 <div id="bb8" style="position:absolute;left:380px;top:150px;background:#fff;color:#111;border-radius:22px;padding:10px 18px;font-size:40px;font-weight:900;opacity:0;z-index:6">БИ-БИ! 📯</div>
 <div class="ch" data-p="e"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 $('ky3').innerHTML=['ДО','РЕ','МИ','ФА','СОЛЬ','ЛЯ','СИ'].map((n,i)=>`<div id="k3_${i}" style="flex:1;background:#fff;border-radius:0 0 12px 12px;color:#111;display:flex;align-items:flex-end;justify-content:center;padding-bottom:14px;font-size:20px;font-weight:900">${n}</div>`).join('');
 let l='';for(let i=0;i<6;i++)l+=`<div id="l4_${i}" style="position:absolute;top:525px;width:70px;height:10px;border-radius:5px;background:#fff"></div>`;$('ln4').innerHTML=l;
 let m='';for(let i=0;i<6;i++)m+=`<div id="l8_${i}" style="position:absolute;top:560px;width:70px;height:10px;border-radius:5px;background:#fff"></div>`;$('ln8').innerHTML=m;})();
'''
RENDER='''
 {$('no1').style.opacity=seg(t,1.8,1.9);$('no1').style.transform=`rotate(-10deg) scale(${1+.4*pop(t,1.8,8)})`;place('a',300,700,1.0,false);pose('a',t>=1.4?{aL:8,aR:-8,hd:12}:{aL:8,aR:-60});}
 {const s=eb(seg(t,3.26,3.6));$('sh2').style.transform=`scale(${s})`;place('b',300,700,1.0,false);pose('b',t>=3.26?{aL:8,aR:-150,open:1}:{aL:8,aR:-30});}
 {const T=[4.54,4.8,5.04,5.24,5.5,5.82,6.1];for(let i=0;i<7;i++){const on=t>=T[i]&&t<T[i]+.35;const e=$('k3_'+i);e.style.background=on?['#ff453a','#ff9f0a','#ffd60a','#30d158','#64d2ff','#0a84ff','#bf5af2'][i]:'#fff';e.style.transform=`translateY(${on?10:0}px)`;}}
 {for(let i=0;i<6;i++){$('l4_'+i).style.left=((((-t*800+i*130)%780)+780)%780-90)+'px';}$('ps4').style.opacity=seg(t,8.4,8.5);$('tx4').style.transform=`scaleX(-1) translateY(${Math.sin(t*25)*2}px)`;}
 {$('xa5').style.opacity=seg(t,10.26,10.36);$('rt5').setAttribute('stroke-dashoffset',700*(1-eo(seg(t,10.74,11.4))));$('pg5').style.opacity=seg(t,11.4,11.5);$('pg5').style.transform=`scale(${1+.4*pop(t,11.5,6)})`;}
 {$('st6').style.opacity=seg(t,12.34,12.44);$('st6').style.transform=`rotate(-8deg) scale(${1+.4*pop(t,12.34,8)})`;place('c',470,700,.8,true);pose('c',t>=11.64?{aL:60,aR:-60,open:1}:{aL:8,aR:-8});}
 {const pd=t>=14.82;$('bt7').textContent=pd?'✅ Оплачено':'Оплатить';$('bt7').style.background=pd?'#30d158':'#000';$('bt7').style.transform=`scale(${1-.08*pop(t,14.6,10)})`;
  place('d',300,700,1.0,false);pose('d',pd?{aL:60,aR:-60,open:1,bob:-Math.abs(Math.sin(t*10))*10}:{aL:8,aR:-100});}
 {for(let i=0;i<6;i++){$('l8_'+i).style.left=((((-t*900+i*130)%780)+780)%780-90)+'px';}$('cr8').style.transform=`scaleX(-1) translateY(${Math.sin(t*25)*2}px)`;
  $('bb8').style.opacity=seg(t,16.44,16.5);$('bb8').style.transform=`scale(${1+.3*pop(t,16.44,8)})`;place('e',90,700,.75,false);pose('e',{aL:8,aR:-150+Math.sin(t*12)*25,open:1});}
'''
