DUR=22.4
FADE=22.0
START=0
SONG='FORTUNA 812 — sexy supra'
BG='linear-gradient(180deg,#140a0a,#050303)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["когда",0.1],["3",0.4],["года",0.6],["копил",0.9],["на",1.2],["мечту",1.35]],
 [["и",1.8],["наконец",2.2],["забрал",2.9],["её",3.4],["🏎️",4.0]],
 [["первым",5.25],["делом",5.7],["—",6.1],["фото",6.2],["в",6.9],["сторис",7.0]],
 [["бывшая",8.7],["через",9.4],["минуту:",9.7],["«привет,",10.5],["как",11.0],["дела?»",11.2]],
 [["мама:",12.15],["«а",12.9],["где",13.1],["деньги",13.4],["на",14.0],["квартиру?»",14.1]],
 [["страховка",15.6],["за",16.4],["год:",16.6],["400",17.0],["000",17.3],["₽",17.6]],
 [["зато",19.05],["как",19.6],["она",19.9],["звучит",20.4],["🔥",21.2]],
]
SC=[[-0.3,1.75],[1.75,5.2],[5.2,8.65],[8.65,12.1],[12.1,15.55],[15.55,18.95],[18.95,99]]
GLOW=['#7a6a1a','#7a1f1f','#5a1d7a','#7a1f4a','#1a5c2e','#7a3a1a','#7a1f0a']
PEMO=['🐷','🏎️','📸','💬','👩','🧾','🔥']
END=[22.0,22.4]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#ffd6e8,#ff9ac1);color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Копилка «Мечта»</div><div class="ttl mono" id="sv1">0 ₽</div>
 <div id="pg1" style="position:absolute;left:330px;top:250px;font-size:170px">🐷</div>
 <div id="cn1" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#1a1a22,#000)">
 <div class="hdr" style="color:#ff453a">Автосалон · выдача</div>
 <div id="sp2" style="position:absolute;left:0;right:0;top:330px;height:200px;background:radial-gradient(ellipse at 50% 50%,rgba(255,255,255,.25),transparent 70%)"></div>
 <div id="cr2" style="position:absolute;top:280px;font-size:200px;transform:scaleX(-1);z-index:4">🏎️</div>
 <div class="ch" data-p="b"></div>
 <div id="wo2" style="position:absolute;left:60px;top:80px;background:#fff;color:#111;border-radius:22px;padding:10px 18px;font-size:34px;font-weight:900;opacity:0">ОНА МОЯ 😭</div>
</div>
<div class="card" id="c3" style="background:#000">
 <div style="position:absolute;left:30px;right:30px;top:30px;height:500px;border-radius:30px;background:linear-gradient(180deg,#2a0a0a,#5a1010);overflow:hidden"><div class="c" style="top:150px;font-size:200px;transform:scaleX(-1)">🏎️</div>
  <div style="position:absolute;left:20px;top:20px;font-size:22px;font-weight:800">● Ваша история</div>
  <div id="lk3" style="position:absolute;right:20px;bottom:20px;font-size:30px;font-weight:900">❤️ <span id="ln3" class="mono">0</span></div></div>
 <div id="fl3" style="position:absolute;inset:0;background:#fff;opacity:0;z-index:8"></div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:#000">
 <div class="hdr">Сообщения</div>
 <div id="nt4" style="position:absolute;left:24px;right:24px;top:90px;background:rgba(60,60,64,.95);border-radius:22px;padding:14px 18px;opacity:0">
  <div style="font-size:20px;color:#aeaeb2;font-weight:700">💔 Бывшая · сейчас</div><div style="font-size:30px;font-weight:800">привет, как дела? 🥺</div></div>
 <div id="sn4" style="position:absolute;left:24px;top:240px;font-size:22px;color:#8e8e93;font-weight:700;opacity:0">не писала 2 года · 1 минута после сторис</div>
 <div class="ch" data-p="d"></div>
 <div id="sm4" style="position:absolute;left:380px;top:430px;font-size:70px;opacity:0;z-index:6">😏</div>
</div>
<div class="card" id="c5" style="background:#0d1a12">
 <div class="hdr" style="color:#30d158">Банк · Накопления</div>
 <div class="c mono" id="bl5" style="top:90px;font-size:60px;font-weight:800">0 ₽</div>
 <div class="c" style="top:170px;font-size:22px;color:#8e8e93;font-weight:700">цель «квартира» · 0%</div>
 <div id="mm5" style="position:absolute;left:24px;right:24px;top:230px;background:#2c2c2e;border-radius:22px;padding:12px 16px;font-size:26px;font-weight:800;opacity:0">👩 Мама: а где деньги на квартиру?</div>
 <div class="ch" data-p="e"></div>
 <div id="sw5" style="position:absolute;left:350px;top:420px;font-size:50px;opacity:0;z-index:6">💦</div>
</div>
<div class="card" id="c6" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Счёт</div><div class="ttl">Страховка КАСКО</div>
 <div class="c mono" id="pr6" style="top:170px;font-size:72px;font-weight:900;color:#d0021b">0 ₽</div>
 <div class="c" style="top:260px;font-size:22px;color:#8e8e93;font-weight:700">водитель 19 лет · стаж 0 · спорткар</div>
 <div class="ch" data-p="f"></div>
</div>
<div class="card" id="c7" style="background:linear-gradient(180deg,#1a0505,#3a0a0a 60%,#222 61%,#111)">
 <div id="ln7" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="g"></div>
 <div id="cr7" style="position:absolute;left:180px;top:300px;font-size:200px;transform:scaleX(-1);z-index:4">🏎️</div>
 <div id="fi7" style="position:absolute;left:430px;top:400px;font-size:90px;z-index:3">🔥</div>
  <div class="c" id="db7" style="top:60px;font-size:60px;font-weight:900;color:#ff9f0a;opacity:0">🔊 120 дБ</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 let c='';for(let i=0;i<8;i++)c+=`<div id="m1_${i}" style="position:absolute;font-size:44px;opacity:0">🪙</div>`;$('cn1').innerHTML=c;
 let l='';for(let i=0;i<10;i++)l+=`<div id="l7_${i}" style="position:absolute;height:6px;width:${80+rnd(i)*120}px;border-radius:3px;background:#ff9f0a;opacity:.7"></div>`;$('ln7').innerHTML=l;})();
'''
RENDER='''
 {const k=seg(t,0.1,1.6);$('sv1').textContent=fmt(k*3500000)+' ₽';for(let i=0;i<8;i++){const ph=((t-0.1)*3+i/8)%1;const e=$('m1_'+i);e.style.opacity=t>0.1?1:0;e.style.left='395px';e.style.top=(80+ph*200)+'px';}
  $('pg1').style.transform=`scale(${1+.05*Math.sin(t*20)})`;place('a',170,690,1.0,false);pose('a',{aL:8,aR:-80,hd:-6});}
 {const k=eo(seg(t,1.75,2.8));$('cr2').style.left=lerp(620,160,k)+'px';place('b',110,690,.9,false);const b=t>=2.9;pose('b',b?{aL:150,aR:-150,open:1,bob:-Math.abs(Math.sin(t*9))*14}:{aL:8,aR:-8});
  $('wo2').style.opacity=seg(t,3.4,3.5);$('wo2').style.transform=`scale(${1+.3*pop(t,3.4,6)})`;}
 {$('fl3').style.opacity=.9*pop(t,6.2,8);const n=t<6.2?0:Math.floor(eo(seg(t,6.3,8.5))*1488);$('ln3').textContent=fmt(n);place('c',110,690,.8,false);pose('c',{aL:8,aR:-120,hd:-6});}
 {$('nt4').style.opacity=seg(t,9.4,9.55);$('nt4').style.transform=`translateY(${(1-eo(seg(t,9.4,9.8)))*-30}px)`;$('sn4').style.opacity=seg(t,10.0,10.2);
  place('d',260,690,1.05,false);pose('d',t>=10.5?{aL:8,aR:-60,hd:12}:{aL:8,aR:-8});$('sm4').style.opacity=seg(t,10.5,10.6);}
 {$('mm5').style.opacity=seg(t,12.9,13.0);place('e',260,690,1.05,false);const s=t>=13.4;pose('e',s?{aL:20,aR:-20,hd:Math.sin(t*16)*8}:{aL:8,aR:-8});
  $('sw5').style.opacity=s?1:0;$('sw5').style.top=(420+((t*2)%1)*40)+'px';}
 {const v=eo(seg(t,17.0,17.6))*400000;$('pr6').textContent=fmt(v)+' ₽';$('pr6').style.transform=`scale(${1+.2*pop(t,17.6,6)})`;
  const f=seg(t,17.7,18.3);place('f',300,690,1.05,false,f*-90);pose('f',t>=17.6?{aL:60,aR:-60,open:1}:{aL:8,aR:-8});}
 {const d=t>=19.0;$('cr7').style.transform=`scaleX(-1) translateY(${d?Math.sin(t*30)*4:0}px)`;$('fi7').style.opacity=d?(.6+.4*Math.abs(Math.sin(t*12))):0;$('fi7').style.transform=`scale(${1+.3*Math.abs(Math.sin(t*12))})`;
  for(let i=0;i<10;i++){const e=$('l7_'+i);e.style.top=(120+i*55)+'px';e.style.left=(((-t*1400+i*170)%800)+800)%800-100+'px';e.style.opacity=d?.7:0;}
  place('g',330,440,.55,false);pose('g',d?{aL:150*Math.sin(t*10),aR:-150*Math.cos(t*10),open:1,bob:-Math.abs(Math.sin(t*10))*10}:{aL:8,aR:-8});
  $('db7').style.opacity=seg(t,20.4,20.5);$('db7').style.transform=`scale(${1+.15*Math.abs(Math.sin(t*12))})`;}
'''
