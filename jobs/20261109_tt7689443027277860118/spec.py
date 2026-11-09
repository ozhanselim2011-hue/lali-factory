DUR=11.9
FADE=11.5
START=23.9
SONG='GATASKI — ПЕРВЫЙ РАЗ'
BG='linear-gradient(180deg,#140a0a,#050303)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["и",24.1],["всё,",24.3],["как",24.6],["и",24.8],["в",24.9],["первый",25.06],["раз",25.2],["—",25.5],["с*ка",25.7]],
 [["один",26.42],["раз",27.68],["послать,",27.9],["чем",28.5],["два",28.74],["сказать",28.98]],
 [["надоело",29.48],["за",30.78],["двоих",30.98],["тянуть",31.44]],
 [["спасать",31.8]],
 [["надоело",32.62],["за",33.62],["двоих",33.86],["тянуть",34.24]],
 [["спасать",34.64]],
]
SC=[[23.6,26.35],[26.35,29.42],[29.42,32.55],[32.55,34.58],[34.58,99]]
GLOW=['#5a1d7a','#1a4a7a','#7a3a1a','#7a5a1a','#7a1f1f']
PEMO=['🔁','👋','🪢','🔋','🆘']
END=[35.4,35.8]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr">Отношения · история</div><div class="ttl">Попытка №<span id="n1" class="mono">1</span></div>
 <div id="rp1" class="c" style="top:170px;font-size:150px">🔁</div>
 <div id="dj1" class="c" style="top:370px;font-size:28px;font-weight:900;color:#ff9f0a;opacity:0">⚠️ всё как в первый раз</div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#000">
 <div class="hdr">Новое сообщение · ей</div>
 <div id="tx2" style="position:absolute;left:24px;right:24px;top:80px;min-height:60px;background:#0a84ff;border-radius:22px;padding:14px 18px;font-size:22px;font-weight:700;line-height:1.35"></div>
 <div id="sn2" style="position:absolute;right:30px;top:420px;font-size:22px;color:#8e8e93;font-weight:700;opacity:0">Доставлено ✓✓</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:linear-gradient(180deg,#9fd3ff,#d8f0ff 60%,#8bc34a 61%,#5a8a2a)">
 <div class="hdr" style="color:rgba(0,0,0,.5)">Нагрузка</div><div class="ttl mono" id="ld3" style="color:#d0021b">100%</div>
 <div id="cr3" style="position:absolute;left:300px;top:380px;width:220px;height:90px;background:#8a5a32;border-radius:12px;z-index:3"><div style="position:absolute;left:30px;top:-70px;font-size:70px">🧳</div><div style="position:absolute;left:110px;top:-70px;font-size:70px">🧳</div><div style="position:absolute;left:30px;top:80px;width:40px;height:40px;border-radius:50%;background:#333"></div><div style="position:absolute;left:150px;top:80px;width:40px;height:40px;border-radius:50%;background:#333"></div></div>
 <div style="position:absolute;left:215px;top:420px;width:90px;height:6px;background:#5a3a1a;z-index:3"></div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:#111214">
 <div class="hdr" style="color:#ff453a">Заряд сил</div>
 <div style="position:absolute;left:160px;top:110px;width:280px;height:130px;border:8px solid #fff;border-radius:22px;padding:8px"><div id="bt4" style="height:100%;border-radius:12px;background:#30d158;width:60%"></div></div>
 <div style="position:absolute;left:448px;top:150px;width:20px;height:50px;background:#fff;border-radius:6px"></div>
 <div class="c mono" id="pc4" style="top:270px;font-size:54px;font-weight:900">60%</div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c5" style="background:#2a0505">
 <div id="al5" style="position:absolute;inset:0;background:#ff0000;opacity:0"></div>
 <div id="so5" class="c" style="top:120px;font-size:140px;z-index:6">🆘</div>
 <div class="c" style="top:320px;font-size:30px;font-weight:900;z-index:6">кто спасёт спасателя?</div>
 <div class="ch" data-p="e"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});})();
'''
RENDER='''
 {const n=Math.min(7,1+Math.floor(seg(t,24.0,25.2)*6));$('n1').textContent=n;$('rp1').style.transform=`rotate(${t*-360}deg)`;$('dj1').style.opacity=seg(t,25.2,25.3);
  place('a',300,690,1.0,false);pose('a',t>=25.7?{aL:60,aR:-60,hd:12,open:1}:{aL:8,aR:-8,hd:-6});}
 {const long='Слушай, я долго думал и хочу сказать, что нам нужно серьёзно поговорить о нас, о том, что происходит, потому что я чувствую, что…';
  const del=seg(t,27.68,28.4),ty=t>=28.5;$('tx2').textContent=ty?'пока 👋':long.slice(0,Math.round(long.length*(1-del)))||'…';$('tx2').style.fontSize=ty?'44px':'22px';$('tx2').style.textAlign=ty?'center':'left';
  $('sn2').style.opacity=seg(t,28.98,29.1);place('b',300,700,1.0,false);pose('b',t>=28.98?{aL:8,aR:-150,open:1}:{aL:8,aR:-60,hd:-8});}
 {const s=Math.sin(t*6)*6;$('ld3').textContent=(t>=30.98?'200':'100')+'%';place('c',170,690,1.0,false,8);pose('c',{aL:-60,aR:-60,hd:10,lL:Math.sin(t*8)*15,lR:-Math.sin(t*8)*15,bob:Math.abs(Math.sin(t*8))*-5});
  $('cr3').style.transform=`translateX(${s}px)`;}
 {const v=lerp(60,3,eo(seg(t,32.62,34.3)));$('bt4').style.width=v+'%';$('bt4').style.background=v<20?'#ff453a':'#30d158';$('pc4').textContent=Math.round(v)+'%';
  place('d',300,690,1.0,false);pose('d',{aL:8,aR:-8,hd:lerp(0,22,seg(t,32.6,34.3)),bob:lerp(0,14,seg(t,32.6,34.3))});}
 {$('al5').style.opacity=.3*Math.abs(Math.sin(t*10));$('so5').style.transform=`scale(${1+.15*Math.abs(Math.sin(t*10))})`;const f=eo(seg(t,34.8,35.4));place('e',lerp(300,380,f),lerp(690,640,f),1.0,false,f*-90);pose('e',{aL:150,aR:-150,open:1});}
'''
