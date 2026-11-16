DUR=19.4
FADE=19.0
START=3.9
SONG='SHAQINA — Действуешь на нервы'
BG='linear-gradient(180deg,#160a14,#060306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Ты",4.16],["мне",5.14],["действуешь",5.34],["на",5.84],["нервы,",5.98]],
 [["и",6.62],["я",7.78],["тебе",7.96],["тоже",8.24]],
 [["то",8.76],["готовы",10.0],["убить,",10.64]],
 [["то",11.38],["друг",12.28],["без",12.46],["друга",12.62],["не",12.92],["можем",13.2]],
 [["то",13.64],["доводим",14.8],["до",15.36],["психа,",15.46]],
 [["то",16.22],["снова",17.22],["скучаем",17.64]],
 [["каждый",18.56],["раз",19.8],["ставим",19.98],["точку,",20.52]],
 [["но",21.22],["опять",22.02],["начинаем",22.32]],
]
SC=[[3.6,6.5],[6.5,8.6],[8.6,11.3],[11.3,13.55],[13.55,16.1],[16.1,18.45],[18.45,21.1],[21.1,99]]
GLOW=['#7a1f2a','#7a1f2a','#7a0a0a','#7a1f4a','#7a2a0a','#3a1d5a','#2a2a2a','#1d5a2a']
PEMO=['😤','😤','🔪','🫂','🤯','📞','🚫','♻️']
END=[22.9,23.3]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}.bar{position:absolute;height:34px;border-radius:17px;background:#2c2c2e;overflow:hidden}.bar div{height:100%;background:linear-gradient(90deg,#ff453a,#30d158)}'
BUB='position:absolute;max-width:360px;padding:14px 20px;border-radius:24px;font:800 26px Inter;opacity:0'
HTML=f'''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr" style="color:#ff453a">Нервы · Лали</div>
 <div class="bar" style="left:40px;right:40px;top:90px"><div id="n1"></div></div><div id="v1" class="c mono" style="top:140px;font-size:60px;font-weight:900">100%</div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#1c1c1e">
 <div style="position:absolute;left:30px;top:40px;font:800 22px Inter;color:#64d2ff">нервы · Лали</div><div class="bar" style="left:30px;width:250px;top:80px"><div style="width:3%"></div></div>
 <div style="position:absolute;right:30px;top:40px;font:800 22px Inter;color:#bf5af2">нервы · она</div><div class="bar" style="right:30px;width:250px;top:80px"><div id="n2" style="width:100%"></div></div>
 <div id="t2" class="c" style="top:150px;font:900 40px Inter;color:#ff453a;opacity:0">оба на нуле</div>
 <div class="ch" data-p="b"></div><div class="ch" data-p="g1"></div>
</div>
<div class="card" id="c3" style="background:#000">
 <div class="hdr">Чат · она 💜</div>
 <div id="m3" style="{BUB};left:24px;top:110px;background:#3a3a3c">я тебя убью 😡</div>
 <div id="m3b" style="{BUB};right:24px;top:210px;background:#0a84ff">сначала я тебя 😤</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#ffd6e8,#ff8ac4)">
 <div class="ch" data-p="d"></div><div class="ch" data-p="g2"></div>
 <div id="hh4" style="position:absolute;inset:0;z-index:6"></div>
</div>
<div class="card" id="c5" style="background:#1c1c1e">
 <div class="hdr" style="color:#ff9f0a">Уровень бешенства</div>
 <svg width="440" height="240" style="position:absolute;left:80px;top:80px"><path d="M30 220 A190 190 0 0 1 410 220" fill="none" stroke="url(#gg5)" stroke-width="40"/><defs><linearGradient id="gg5"><stop offset="0" stop-color="#30d158"/><stop offset=".5" stop-color="#ffd60a"/><stop offset="1" stop-color="#ff453a"/></linearGradient></defs></svg>
 <div id="nd5" style="position:absolute;left:296px;top:120px;width:8px;height:180px;background:#fff;border-radius:4px;transform-origin:4px 180px"></div>
 <div id="ps5" class="c" style="top:330px;font:900 54px Inter;color:#ff453a;opacity:0">ПСИХ</div>
 <div id="st5" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="e"></div>
</div>
<div class="card" id="c6" style="background:linear-gradient(180deg,#1a1440,#0a0820)">
 <div class="c" style="top:60px;font:800 26px Inter;color:#aeaeb2">вызов…</div>
 <div class="c" style="top:100px;font:900 50px Inter">она 💜</div>
 <div id="mc6" class="c mono" style="top:180px;font-size:30px;font-weight:900;color:#ff453a">пропущенных: 0</div>
 <div class="ch" data-p="f"></div>
</div>
<div class="card" id="c7" style="background:#000">
 <div class="hdr">Чат · она 💜</div>
 <div id="m7" style="{BUB};right:24px;top:110px;background:#0a84ff">всё. это конец</div>
 <div id="dt7" style="position:absolute;left:250px;top:240px;width:100px;height:100px;border-radius:50%;background:#fff;opacity:0"></div>
 <div id="bl7" class="c" style="top:400px;font:900 34px Inter;color:#ff453a;opacity:0">🚫 заблокирована</div>
</div>
<div class="card" id="c8" style="background:#000">
 <div class="hdr">Чат · она 💜</div>
 <div id="ub8" style="position:absolute;left:60px;right:60px;top:110px;background:#2c2c2e;border-radius:22px;padding:18px;text-align:center;font:800 26px Inter">Разблокировать?<div id="ok8" style="margin-top:12px;background:#3a3a3c;border-radius:14px;padding:10px">Да</div></div>
 <div id="m8" style="{BUB};right:24px;top:300px;background:#0a84ff">привет 🙂</div>
 <div id="sr8" class="c" style="top:400px;font:900 30px Inter;color:#30d158;opacity:0">♻️ серия №148</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...(p.startsWith('g')?['#bf5af2','#e0b0ff','#bf5af2']:['#111','#64d2ff','#0a84ff']));});})();'''
RENDER='''
 {const v=lerp(100,3,eo(seg(t,4.16,6.0)));$('n1').style.width=v+'%';$('v1').textContent=Math.round(v)+'%';$('v1').style.color=v<30?'#ff453a':'#fff';
  place('a',300,690,1.15,false,t>=5.98?Math.sin(t*50)*3:0);pose('a',{aL:8,aR:-8,hd:t>=5.34?Math.sin(t*40)*6:0,open:t>=5.98});}
 {const v=lerp(100,0,eo(seg(t,7.78,8.24)));$('n2').style.width=v+'%';$('t2').style.opacity=seg(t,8.24,8.3);place('b',160,690,.9,false);pose('b',{aL:8,aR:-8,hd:15});place('g1',440,690,.9,true);pose('g1',{aL:60,aR:-60,hd:15,open:t>=7.78});}
 {$('m3').style.opacity=seg(t,9.0,9.1);$('m3b').style.opacity=seg(t,10.64,10.7);$('m3b').style.transform=`scale(${1+.2*pop(t,10.64,7)})`;place('c',300,690,.95,false);pose('c',{aL:8,aR:-8,hd:t>=10.64?-12:0,open:t>=10.64});if(si==2&&t>=10.64)$('c3').style.transform+=` translateX(${Math.sin(t*90)*8*pop(t,10.64,6)}px)`;}
 {const k=eo(seg(t,11.38,12.3));place('d',lerp(100,250,k),690,1.0,false);place('g2',lerp(500,350,k),690,1.0,true);const hug={aL:lerp(8,110,k),aR:-lerp(8,110,k),open:t>=13.2};pose('d',hug);pose('g2',hug);
  let h='';for(let i=0;i<10;i++){const s=12.3+i*.12;if(t>=s){const p=(t-s)/1.2;h+=`<div style="position:absolute;left:${200+rnd(i)*200}px;top:${300-p*260}px;font-size:${30+rnd(i+2)*24}px;opacity:${1-p}">💗</div>`}}$('hh4').innerHTML=h;}
 {const a=lerp(-80,85,eo(seg(t,13.64,15.46)));$('nd5').style.transform=`rotate(${a+(t>=15.46?Math.sin(t*40)*4:0)}deg)`;$('ps5').style.opacity=seg(t,15.46,15.55);$('ps5').style.transform=`scale(${1+.4*pop(t,15.46,7)})`;
  let s='';if(t>=14.8)for(let i=0;i<6;i++){const p=((t-14.8)*1.5+i/6)%1;s+=`<div style="position:absolute;left:${250+(i%2?-40:40)+p*(i%2?-30:30)}px;top:${430-p*120}px;width:${30+p*30}px;height:${30+p*30}px;border-radius:50%;background:rgba(255,255,255,${.5*(1-p)})"></div>`}$('st5').innerHTML=s;
  place('e',300,690,.9,false);pose('e',{aL:t>=15.46?150:8,aR:t>=15.46?-150:-8,open:t>=15.46});$('ch_e').style.filter=`hue-rotate(${-seg(t,13.64,15.46)*40}deg) saturate(${1+seg(t,13.64,15.46)})`;}
 {const n=t<16.22?0:Math.round(47*eo(seg(t,16.22,17.8)));$('mc6').textContent='пропущенных: '+n;$('mc6').style.transform=`scale(${1+.04*Math.sin(t*20)})`;place('f',300,690,1.0,false);pose('f',{aL:8,aR:-140,hd:-14,bob:Math.sin(t*2)*4});}
 {$('m7').style.opacity=seg(t,18.7,18.8);$('dt7').style.opacity=seg(t,20.52,20.55);$('dt7').style.transform=`scale(${lerp(3,1,eb(seg(t,20.52,20.75)))})`;$('bl7').style.opacity=seg(t,20.8,20.9);}
 {const y=t>=21.22;$('ok8').style.background=y?'#30d158':'#3a3a3c';$('ok8').textContent=y?'Да ✓':'Да';$('m8').style.opacity=seg(t,22.02,22.1);$('m8').style.transform=`scale(${1+.2*pop(t,22.02,7)})`;$('sr8').style.opacity=seg(t,22.32,22.4);}
'''
