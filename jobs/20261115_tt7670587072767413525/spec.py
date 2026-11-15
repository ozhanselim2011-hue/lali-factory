DUR=14.6
FADE=14.2
START=9.2
SONG='Фара Ночи — Не буди меня'
BG='linear-gradient(180deg,#0a0a1e,#030308)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Не",9.46],["буди",10.5],["меня,",11.04]],
 [["я",11.56],["сплю,",11.76]],
 [["ведь",12.42],["я",13.66],["во",13.92],["сне",14.1],["тебя",14.34],["ищу",15.0]],
 [["я",16.18],["долго-долго",17.88],["буду",18.88],["спать,",19.24]],
 [["я",20.38],["не",21.28],["хочу",21.48],["тебя",21.96],["терять",22.7]],
]
SC=[[8.9,11.4],[11.4,12.3],[12.3,16.0],[16.0,20.2],[20.2,99]]
GLOW=['#1d1d5a','#3a1d5a','#5a1d7a','#1d3a5a','#7a1f4a']
PEMO=['⏰','💤','🌙','😴','❤️']
END=[23.4,23.8]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#141432,#0a0a1e)">
 <div style="position:absolute;left:60px;top:430px;width:480px;height:120px;background:#3a3a6a;border-radius:20px"></div><div style="position:absolute;left:60px;top:380px;width:120px;height:70px;background:#eee;border-radius:20px"></div>
 <div class="ch" data-p="a"></div>
 <div style="position:absolute;left:250px;top:410px;width:290px;height:90px;background:#5e5ce6;border-radius:20px;z-index:6"></div>
 <div id="al1" style="position:absolute;left:80px;right:80px;top:40px;background:rgba(40,40,44,.95);border-radius:26px;padding:20px;text-align:center;z-index:7">
  <div class="mono" style="font-size:70px;font-weight:300">07:00</div><div style="font-size:24px;font-weight:800;color:#ff9f0a">⏰ Будильник</div>
  <div id="bt1" style="margin-top:12px;background:#ff453a;border-radius:16px;padding:10px;font-size:24px;font-weight:900">Отложить</div></div>
</div>
<div class="card" id="c2" style="background:#2a1a10">
 <div style="position:absolute;left:150px;top:40px;width:300px;height:640px;background:#8a5a32;border-radius:10px;border:10px solid #5a3a1a"></div>
 <div id="sg2" style="position:absolute;left:170px;top:150px;width:260px;padding:22px;background:#fff;border-radius:14px;text-align:center;color:#111;transform-origin:50% -40px;box-shadow:0 10px 20px rgba(0,0,0,.4)"><div style="font-size:60px">💤</div><div style="font:900 28px Inter;color:#ff453a">НЕ БУДИТЬ</div><div style="font:800 22px Inter">я сплю</div></div>
 <div style="position:absolute;left:186px;top:110px;width:228px;height:40px;border:4px solid #ccc;border-bottom:none;border-radius:114px 114px 0 0"></div>
 <div id="zz2" style="position:absolute;inset:0"></div>
</div>
<div class="card" id="c3" style="background:radial-gradient(circle at 50% 40%,#4a2a7a,#140a24)">
 <div id="cl3" style="position:absolute;inset:0"></div>
 <div style="position:absolute;left:24px;right:24px;top:30px;background:rgba(255,255,255,.12);border-radius:30px;padding:14px 22px;font:800 24px Inter">🔍 <span id="q3"></span><span style="opacity:.5">|</span></div>
 <div id="rs3" style="position:absolute;left:24px;right:24px;top:110px;font:700 22px Inter;color:#d1c4ff;line-height:1.8"></div>
 <div class="ch" data-p="b"></div>
 <div id="fl3" style="position:absolute;width:220px;height:220px;border-radius:50%;background:radial-gradient(circle,rgba(255,240,150,.55),rgba(255,240,150,0) 70%);z-index:4"></div>
</div>
<div class="card" id="c4" style="background:#000">
 <div class="hdr" style="color:#64d2ff">Сон · сегодня</div>
 <div id="hr4" class="c mono" style="top:110px;font-size:120px;font-weight:900;color:#64d2ff">0 ч</div>
 <div style="position:absolute;left:40px;right:40px;top:290px;height:24px;border-radius:12px;background:#1c1c1e;overflow:hidden"><div id="br4" style="height:100%;background:linear-gradient(90deg,#5e5ce6,#64d2ff);width:0"></div></div>
 <div id="rc4" class="c" style="top:340px;font-size:30px;font-weight:900;color:#ffd60a;opacity:0">🏆 новый рекорд сна</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c5" style="background:#e8eef4;color:#111">
 <div style="position:absolute;inset:0;background-image:linear-gradient(#d0d8e0 2px,transparent 2px),linear-gradient(90deg,#d0d8e0 2px,transparent 2px);background-size:80px 80px"></div>
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#fff;border-radius:22px;padding:14px 18px;font:900 24px Inter;box-shadow:0 6px 16px rgba(0,0,0,.1)">📍 Локатор · <span style="color:#30d158">она</span> <span id="ds5" style="float:right;color:#888">5 км</span></div>
 <div id="pn5" style="position:absolute;left:400px;top:200px;width:70px;height:70px;border-radius:50%;background:#ff2d78;border:6px solid #fff;box-shadow:0 0 0 0 rgba(255,45,120,.5);display:flex;align-items:center;justify-content:center;font-size:34px">❤️</div>
 <div class="ch" data-p="d"></div>
 <div id="lk5" class="c" style="top:110px;font:900 32px Inter;color:#ff2d78;opacity:0">не отпускаю 🔒</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#111','#ff8ac4','#ff2d78');});
 let c='';for(let i=0;i<8;i++)c+=`<div style="position:absolute;left:${rnd(i)*520}px;top:${200+rnd(i+3)*420}px;width:${120+rnd(i+1)*120}px;height:60px;border-radius:30px;background:rgba(255,255,255,.12)"></div>`;$('cl3').innerHTML=c;})();'''
RENDER='''
 {place('a',300,480,.75,false,-90);pose('a',{aL:8,aR:t>=10.5?-150:-8,hd:0});const sn=t>=11.04;$('bt1').textContent=sn?'Не будить до обеда ✓':'Отложить';$('bt1').style.background=sn?'#30d158':'#ff453a';
  $('al1').style.transform=`translateX(${t<11.04?Math.sin(t*60)*6:0}px) scale(${1+.08*pop(t,11.04,8)})`;}
 {$('sg2').style.transform=`rotate(${Math.sin(t*3)*6+8*pop(t,11.76,5)*Math.sin(t*20)}deg)`;let z='';for(let i=0;i<5;i++){const p=((t-11.4)*.8+i/5)%1;z+=`<div style="position:absolute;left:${380+p*120+Math.sin(p*9)*10}px;top:${420-p*300}px;font:900 ${30+p*40}px Inter;color:#a59bff;opacity:${1-p}">Z</div>`}$('zz2').innerHTML=z;}
 {const q='её во снах';$('q3').textContent=q.slice(0,Math.round(q.length*seg(t,12.42,13.6)));const R=[[13.66,'🌙 сон №1 · пусто'],[13.92,'🌙 сон №2 · пусто'],[14.34,'🌙 сон №3 · кажется, она…'],[15.0,'💗 найдено: <b style="color:#fff">ты</b>']];$('rs3').innerHTML=R.filter(r=>t>=r[0]).map(r=>`<div>${r[1]}</div>`).join('');
  const x=300+Math.sin(t*1.5)*180;place('b',x,690,.9,Math.cos(t*1.5)<0);pose('b',{aL:8,aR:-90,hd:Math.sin(t*2)*8,lL:Math.sin(t*6)*18,lR:-Math.sin(t*6)*18});$('fl3').style.left=(x+(Math.cos(t*1.5)<0?-240:40))+'px';$('fl3').style.top='380px';}
 {const h=t<17.88?lerp(0,8,seg(t,16.18,17.6)):lerp(8,99,eo(seg(t,17.88,19.6)));$('hr4').textContent=Math.round(h)+' ч';$('br4').style.width=Math.min(100,h)+'%';$('rc4').style.opacity=seg(t,19.24,19.3);$('rc4').style.transform=`scale(${1+.3*pop(t,19.24,7)})`;
  place('c',300,690,.95,false);pose('c',{aL:8,aR:-8,hd:20+Math.sin(t*2)*5,bob:Math.sin(t*2)*4});}
 {const k=eo(seg(t,20.38,22.0));place('d',lerp(140,360,k),690,.95,false);pose('d',t>=21.96?{aL:150,aR:-150,open:1}:walk(t,7));$('ds5').textContent=t>=21.96?'рядом ❤️':(Math.round(lerp(5,0.1,k)*10)/10)+' км';
  $('pn5').style.boxShadow=`0 0 0 ${(t*40)%40}px rgba(255,45,120,${.5-((t*40)%40)/80})`;$('lk5').style.opacity=seg(t,22.7,22.8);$('lk5').style.transform=`scale(${1+.3*pop(t,22.7,7)})`;}
'''
