DUR=19.4
FADE=19.0
START=9.0
SONG='Weeka — Международная'
BG='linear-gradient(180deg,#0a0e18,#040508)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Колумбийка,",9.0],["африканка,",10.06]],
 [["русская",11.62],["или",13.48],["британка",13.98]],
 [["шампанское,",14.98],["шампанское",16.82]],
 [["***",17.38],["всю",17.82],["ночь",18.18]],
 [["сделай",18.9],["по",19.78],["залёту",19.96],["мне",20.56],["сына",20.74],["и",21.44],["дочь",21.62]],
 [["аргентинка,",22.22],["пуэрториканка",23.22]],
 [["белорусская",24.94],["или",26.58],["испанка",27.24]],
]
SC=[[8.7,11.5],[11.5,14.9],[14.9,17.3],[17.3,18.8],[18.8,22.1],[22.1,24.8],[24.8,99]]
GLOW=['#5a3a0a','#5a1d4a','#6a5a0a','#1d1d5a','#7a1f4a','#1d3a5a','#7a3a0a']
PEMO=['🛂','💘','🍾','🌙','👶','✈️','🍽️']
END=[28.0,28.4]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
STAMP='position:absolute;border:7px solid;border-radius:14px;padding:6px 14px;font:900 34px Inter;opacity:0'
HTML=f'''
<div class="card" id="c1" style="background:#1c1c1e">
 <div style="position:absolute;left:60px;top:50px;width:480px;height:420px;background:#7a1f2a;border-radius:18px;box-shadow:0 20px 40px rgba(0,0,0,.5)"><div style="position:absolute;inset:16px;background:#f4ecd8;border-radius:8px"></div>
  <div style="position:absolute;left:40px;top:34px;font:900 20px Inter;color:#8a6a3a;letter-spacing:4px">ПАСПОРТ · ВИЗЫ</div>
  <div id="s1a" style="{STAMP};left:50px;top:110px;color:#e0a800;border-color:#e0a800;transform:rotate(-12deg)">КОЛУМБИЯ ✈</div>
  <div id="s1b" style="{STAMP};left:200px;top:240px;color:#1a8a3a;border-color:#1a8a3a;transform:rotate(9deg)">АФРИКА ✈</div></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#fff;color:#111">
 <div class="hdr" style="color:#ff2d55">Знакомства · международные</div>
 <div id="p2a" style="position:absolute;left:30px;top:90px;width:255px;height:330px;border-radius:24px;background:linear-gradient(160deg,#ffd6e8,#ff8ac4);display:flex;flex-direction:column;align-items:center;justify-content:center;font:900 28px Inter"><div style="font-size:110px">🇷🇺</div>Русская</div>
 <div id="p2b" style="position:absolute;right:30px;top:90px;width:255px;height:330px;border-radius:24px;background:linear-gradient(160deg,#d6e4ff,#7a9cff);display:flex;flex-direction:column;align-items:center;justify-content:center;font:900 28px Inter"><div style="font-size:110px">🇬🇧</div>Британка</div>
 <div id="or2" class="c" style="top:220px;font:900 30px Inter;color:#fff;z-index:6"><span style="background:#111;border-radius:30px;padding:10px 16px">или?</span></div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:radial-gradient(circle at 50% 30%,#4a3a0a,#120e04)">
 <div id="b3a" style="position:absolute;left:110px;top:200px;font-size:170px;transform:rotate(-20deg)">🍾</div><div id="b3b" style="position:absolute;left:330px;top:200px;font-size:170px;transform:scaleX(-1) rotate(-20deg)">🍾</div>
 <div id="fm3" style="position:absolute;inset:0;z-index:4"></div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#0a0a2a,#1a1a4a)">
 <div id="sk4" style="position:absolute;inset:0"></div>
 <div id="cl4" class="c mono" style="top:120px;font-size:110px;font-weight:900">23:00</div>
 <div id="mn4" style="position:absolute;left:420px;top:40px;font-size:70px">🌙</div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c5" style="background:#f2f2f7;color:#111">
 <div style="position:absolute;left:60px;top:60px;width:110px;height:330px;border-radius:20px;background:#fff;border:4px solid #ddd"><div style="position:absolute;left:30px;top:120px;width:50px;height:80px;background:#eee;border-radius:6px"></div>
  <div id="ln5a" style="position:absolute;left:38px;top:135px;width:34px;height:8px;background:#ff2d78;opacity:0"></div><div id="ln5b" style="position:absolute;left:38px;top:170px;width:34px;height:8px;background:#ff2d78;opacity:0"></div></div>
 <div id="ts5" style="position:absolute;left:200px;top:90px;font:900 36px Inter;color:#ff2d78;opacity:0">2 полоски!</div>
 <div id="bb5" style="position:absolute;left:200px;top:160px;font:900 30px Inter"></div>
 <div class="ch" data-p="e"></div>
</div>
<div class="card" id="c6" style="background:#0a0a0a">
 <div style="position:absolute;left:24px;right:24px;top:30px;font:900 28px 'JetBrains Mono';color:#ffd60a">✈ ВЫЛЕТ · ЛАЛИ</div>
 <div id="bd6" style="position:absolute;left:24px;right:24px;top:90px;font:900 26px 'JetBrains Mono';color:#ffd60a"></div>
 <div class="ch" data-p="f"></div>
</div>
<div class="card" id="c7" style="background:#fff8ee;color:#2a1a0a">
 <div class="hdr" style="color:#c45a10">Меню · что выбрать?</div>
 <div id="m7a" style="position:absolute;left:30px;top:90px;width:255px;padding:18px;border-radius:24px;background:#fff;box-shadow:0 8px 20px rgba(0,0,0,.08);text-align:center;font:900 26px Inter;opacity:0"><div style="font-size:90px">🥔</div>Беларусь<br><span style="color:#888;font-size:22px">драники</span></div>
 <div id="m7b" style="position:absolute;right:30px;top:90px;width:255px;padding:18px;border-radius:24px;background:#fff;box-shadow:0 8px 20px rgba(0,0,0,.08);text-align:center;font:900 26px Inter;opacity:0"><div style="font-size:90px">🥘</div>Испания<br><span style="color:#888;font-size:22px">паэлья</span></div>
 <div id="bt7" class="c" style="top:380px;font:900 34px Inter;color:#30d158;opacity:0">беру обе ✓</div>
 <div class="ch" data-p="g"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#111','#64d2ff','#0a84ff');});
 let s='';for(let i=0;i<30;i++)s+=`<div style="position:absolute;left:${rnd(i)*600}px;top:${rnd(i+5)*400}px;width:4px;height:4px;border-radius:50%;background:#fff"></div>`;$('sk4').innerHTML=s;})();'''
RENDER='''
 {[['s1a',9.0,-12],['s1b',10.06,9]].forEach(([id,s,r])=>{$(id).style.opacity=seg(t,s,s+.05);$(id).style.transform=`rotate(${r}deg) scale(${lerp(2.2,1,eb(seg(t,s,s+.25)))})`});
  place('a',470,690,.85,true);pose('a',t>=10.06?{aL:150,aR:-150,open:1}:{aL:8,aR:-90});}
 {const L=t>=11.62&&t<13.48,R=t>=13.98;$('p2a').style.transform=`scale(${L?1.06:1}) rotate(-3deg)`;$('p2b').style.transform=`scale(${R?1.06:1}) rotate(3deg)`;$('p2a').style.boxShadow=L?'0 0 0 6px #ff2d55':'none';$('p2b').style.boxShadow=R?'0 0 0 6px #0a84ff':'none';
  $('or2').style.transform=`scale(${1+.3*pop(t,13.48,8)})`;place('b',300,690,.9,false);pose('b',{aL:8,aR:-8,hd:L?-18:(R?18:Math.sin(t*6)*10),open:t>=13.48});}
 {const S=[14.98,16.82];let f='';S.forEach((s,k)=>{if(t>=s)for(let i=0;i<14;i++){const p=Math.min(1,(t-s)*1.3);const ang=-Math.PI/2+(k?.35:-.35)+(rnd(i+k*20)-.5)*.9;f+=`<div style="position:absolute;left:${(k?400:200)+Math.cos(ang)*p*260}px;top:${220+Math.sin(ang)*p*260+p*p*120}px;width:${14+rnd(i)*14}px;height:${14+rnd(i)*14}px;border-radius:50%;background:rgba(255,240,180,${1-p})"></div>`}});$('fm3').innerHTML=f;
  $('b3a').style.transform=`rotate(${-20-8*pop(t,14.98,6)}deg)`;$('b3b').style.transform=`scaleX(-1) rotate(${-20-8*pop(t,16.82,6)}deg)`;place('c',300,690,.95,false);pose('c',t>=14.98?{aL:150,aR:-150,open:1,bob:-Math.abs(Math.sin(t*10))*10}:{aL:8,aR:-8});}
 {const k=seg(t,17.38,18.7);const h=Math.floor(lerp(23,30,k));$('cl4').textContent=String(h%24).padStart(2,'0')+':'+String(Math.floor((k*7*60)%60)).padStart(2,'0');$('mn4').textContent=k>.85?'☀️':'🌙';
  $('c4').style.background=k>.85?'linear-gradient(180deg,#ff9f43,#ffd6a0)':'linear-gradient(180deg,#0a0a2a,#1a1a4a)';place('d',300,690,1.1,Math.floor(t*4)%2==1);pose('d',{aL:120+Math.sin(t*12.57)*40,aR:-120+Math.sin(t*12.57)*40,lL:Math.sin(t*12.57)*15,lR:-Math.sin(t*12.57)*15,bob:-Math.abs(Math.sin(t*12.57))*12});}
 {$('ln5a').style.opacity=seg(t,19.0,19.1);$('ln5b').style.opacity=seg(t,19.96,20.05);$('ts5').style.opacity=seg(t,19.96,20.05);$('ts5').style.transform=`scale(${1+.3*pop(t,19.96,7)})`;
  $('bb5').innerHTML=(t>=20.74?'<div>👶 сын ✓</div>':'')+(t>=21.62?'<div style="margin-top:10px">👶 дочь ✓</div>':'');place('e',420,690,1.0,true);pose('e',t>=20.74?{aL:150,aR:-150,open:1}:(t>=19.96?{aL:160,aR:-160,open:1,hd:10}:{aL:8,aR:-8}));}
 {const R=[[22.22,'BUE','БУЭНОС-АЙРЕС','АРГЕНТИНКА'],[23.22,'SJU','САН-ХУАН','ПУЭРТОРИКАНКА'],[99,'MSQ','МИНСК','...'],[99,'MAD','МАДРИД','...']];
  $('bd6').innerHTML=R.map(r=>{const on=t>=r[0],fl=on&&t<r[0]+.3;return `<div style="display:flex;justify-content:space-between;padding:16px 0;border-bottom:1px solid #222;color:${on?'#ffd60a':'#555'}"><span>${r[1]}</span><span>${fl?'▓▓▓▓▓▓':r[2]}</span><span style="color:${on?'#30d158':'#555'}">${on?'ПОСАДКА':'—'}</span></div>`}).join('');
  place('f',300,690,.9,false);pose('f',walk(t,7));$('ch_f').style.left=(lerp(-100,620,seg(t,22.1,24.8))-100)+'px';}
 {$('m7a').style.opacity=seg(t,24.94,25.05);$('m7b').style.opacity=seg(t,27.24,27.3);$('m7a').style.transform=`scale(${1+.15*pop(t,24.94,7)})`;$('m7b').style.transform=`scale(${1+.15*pop(t,27.24,7)})`;$('bt7').style.opacity=seg(t,27.6,27.7);
  place('g',300,690,.9,false);pose('g',t>=27.6?{aL:150,aR:-150,open:1}:{aL:8,aR:-8,hd:t>=26.58?Math.sin(t*8)*15:0});}
'''
