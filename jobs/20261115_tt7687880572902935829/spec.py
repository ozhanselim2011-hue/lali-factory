DUR=13.2
FADE=12.8
START=0
SONG='NAVAI — Сгореть'
BG='linear-gradient(180deg,#1a0806,#050202)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["И",0.0],["если",0.58],["это",1.38],["и",2.16],["есть",2.36],["любовь,",2.92]],
 [["то",4.04],["я",4.16],["хочу",4.46],["в",4.88],["ней",4.95],["сегодня",5.4],["сгореть",6.0]],
 [["в",6.82],["ней",6.9],["сегодня",7.34],["сгореть",7.96]],
 [["в",10.08],["ней",10.2],["сегодня",11.2],["сгореть",11.72]],
]
SC=[[-0.3,3.9],[3.9,6.6],[6.6,9.9],[9.9,99]]
GLOW=['#7a1f4a','#7a2a0a','#7a4a0a','#7a0a0a']
PEMO=['💘','🌡️','🔥','🚨']
END=[12.8,13.2]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#fff0f4;color:#111">
 <div class="hdr" style="color:#ff2d55">Тест</div><div class="ttl" style="color:#111">Это любовь?</div>
 <div style="position:absolute;left:30px;right:30px;top:170px;background:#fff;border-radius:24px;padding:4px 24px;font-size:26px;font-weight:800;box-shadow:0 6px 20px rgba(0,0,0,.06)">
  <div id="q1_0" style="padding:16px 0;border-bottom:1px solid #f2f2f2">☐ бабочки в животе</div><div id="q1_1" style="padding:16px 0;border-bottom:1px solid #f2f2f2">☐ не сплю до 4 утра</div><div id="q1_2" style="padding:16px 0;border-bottom:1px solid #f2f2f2">☐ пишу первым</div><div id="q1_3" style="padding:16px 0">☐ улыбаюсь телефону</div></div>
 <div id="r1" style="position:absolute;left:220px;top:470px;background:#ff2d55;color:#fff;border-radius:22px;padding:14px 22px;font-size:34px;font-weight:900;opacity:0">ДА, ЛЮБОВЬ 💘</div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#111">
 <div class="hdr" style="color:#ff9f0a">Температура</div>
 <div style="position:absolute;left:420px;top:90px;width:60px;height:440px;border-radius:30px;background:#2c2c2e;overflow:hidden"><div id="tm2" style="position:absolute;left:0;right:0;bottom:0;height:10%;background:linear-gradient(0deg,#ff3b30,#ff9f0a)"></div></div>
 <div style="position:absolute;left:400px;top:510px;width:100px;height:100px;border-radius:50%;background:#ff3b30"></div>
 <div id="tv2" class="mono" style="position:absolute;left:250px;top:120px;font-size:56px;font-weight:900">36.6°</div>
 <div id="fl2" style="position:absolute;left:30px;bottom:30px;font-size:90px;opacity:0">🔥🔥</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:radial-gradient(circle at 50% 30%,#3a1a0a,#0a0402)">
 <div style="position:absolute;left:285px;top:150px;width:30px;height:420px;background:linear-gradient(90deg,#e8c48a,#c49a5a);border-radius:6px"></div>
 <div id="bn3" style="position:absolute;left:285px;top:150px;width:30px;height:0;background:#1a1a1a;border-radius:6px"></div>
 <div id="mh3" style="position:absolute;left:278px;top:130px;width:44px;height:50px;border-radius:50%;background:#c0392b"></div>
 <div id="fr3" style="position:absolute;left:250px;top:40px;font-size:100px;opacity:0">🔥</div>
 <div id="tx3" class="c" style="top:590px;font-size:30px;font-weight:900;color:#ff9f0a">чиркаю…</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div id="al4" style="position:absolute;left:24px;right:24px;top:30px;background:#3a0d12;border:3px solid #ff453a;border-radius:24px;padding:18px 22px;opacity:0">
  <div style="font-size:26px;font-weight:900;color:#ff453a">🚨 Датчик дыма</div><div style="font-size:24px;font-weight:700;margin-top:6px">Обнаружено возгорание: <b>в сердце</b></div></div>
 <div id="fs4" style="position:absolute;inset:0"></div>
 <div id="dn4" class="c" style="top:200px;font-size:40px;font-weight:900;color:#30d158;opacity:0">сгорел ✓ и счастлив</div>
 <div class="ch" data-p="d"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#ff2d55','#ff8ac4','#ff2d78');});})();'''
RENDER='''
 {const T=[0.58,1.38,2.16,2.36];const Q=['бабочки в животе','не сплю до 4 утра','пишу первым','улыбаюсь телефону'];T.forEach((s,i)=>{const on=t>=s;$('q1_'+i).textContent=(on?'☑ ':'☐ ')+Q[i];$('q1_'+i).style.color=on?'#ff2d55':'#111'});
  $('r1').style.opacity=seg(t,2.92,3.0);$('r1').style.transform=`scale(${lerp(1.8,1,eb(seg(t,2.92,3.2)))}) rotate(-5deg)`;
  place('a',110,690,.9,false);pose('a',t>=2.92?{aL:150,aR:-150,open:1}:{aL:8,aR:-8,hd:Math.sin(t*3)*6});}
 {const k=eo(seg(t,4.04,6.0));const v=lerp(36.6,100,k);$('tm2').style.height=lerp(10,100,k)+'%';$('tv2').textContent=(v>=100?'100':v.toFixed(1))+'°';$('tv2').style.color=v>60?'#ff453a':'#fff';
  $('fl2').style.opacity=seg(t,6.0,6.1);$('fl2').style.transform=`scale(${1+.3*pop(t,6.0,6)})`;
  place('b',180,690,1.0,false);$('ch_b').style.filter=`hue-rotate(${-k*30}deg) saturate(${1+k})`;pose('b',t>=6.0?{aL:150,aR:-150,open:1}:{aL:8,aR:-8,hd:k*10});}
 {const lit=t>=6.9;const b=seg(t,7.0,9.9);$('fr3').style.opacity=lit?1:0;$('fr3').style.top=(40+b*380)+'px';$('fr3').style.transform=`scale(${1+.15*Math.sin(t*20)})`;$('bn3').style.height=(b*400)+'px';$('mh3').style.opacity=lit?0:1;
  $('tx3').textContent=t>=7.96?'сгораю… '+Math.round(b*100)+'%':(lit?'горит':'чиркаю…');
  place('c',470,690,.85,true);pose('c',t>=7.96?{aL:120,aR:-120,hd:-8,bob:Math.sin(t*3)*4}:{aL:8,aR:-8});}
 {$('al4').style.opacity=seg(t,10.08,10.2);$('al4').style.transform=`translateY(${(1-eb(seg(t,10.08,10.35)))*-60}px)`;if(t>=10.08)$('al4').style.borderColor=Math.sin(t*14)>0?'#ff453a':'#7a1d1d';
  let f='';if(t>=11.2)for(let i=0;i<9;i++){const p=((t-11.2)*1.4+rnd(i))%1;f+=`<div style="position:absolute;left:${40+i*62}px;top:${690-p*260}px;font-size:${60+rnd(i+3)*40}px;opacity:${1-p}">🔥</div>`}$('fs4').innerHTML=f;
  $('dn4').style.opacity=seg(t,11.72,11.8);$('dn4').style.transform=`scale(${1+.3*pop(t,11.72,6)})`;
  place('d',300,690,1.15,false);pose('d',t>=11.2?{aL:150+Math.sin(t*12)*15,aR:-150+Math.sin(t*12)*15,open:1,bob:-Math.abs(Math.sin(t*12))*10}:{aL:8,aR:-8,hd:t>=10.08?12:0});}
'''
