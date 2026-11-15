DUR=21.0
FADE=20.6
START=2.2
SONG='Kai Angel — andy warhol'
BG='linear-gradient(180deg,#0e0a12,#050306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["у",2.2],["тебя",2.44],["в",2.84],["апартах,",3.3]],
 [["улыбнусь,",3.9],["как",4.5],["Энди",4.74],["Уорхол,",5.2]],
 [["с",5.9],["фотоаппаратом",6.12]],
 [["ты",7.68],["выглядишь",8.06],["пиз*ато",8.84]],
 [["на",9.6],["больших",10.08],["показах",10.8]],
 [["Prada,",11.62],["Prada,",12.32],["Prada,",12.94]],
 [["Devil",13.36],["носит",14.34],["Prada",14.84]],
 [["хочу",15.28],["быть",16.02],["твоим",16.16],["фанатом",16.66]],
 [["хочу",17.26],["быть",17.94],["твоим",18.14],["фанатом",18.56]],
 [["хочу",19.2],["быть",19.92],["твоим",20.04],["фанатом",20.46]],
 [["хочу",21.14],["быть",21.72],["твоим",21.94],["фанатом",22.34]],
]
SC=[[1.9,3.8],[3.8,6.0],[6.0,7.6],[7.6,9.5],[9.5,11.5],[11.5,13.25],[13.25,15.2],[15.2,99]]
GLOW=['#3a2a5a','#7a1f4a','#3a3a3a','#5a1d4a','#5a5a7a','#2a2a2a','#7a0a0a','#5a1d7a']
PEMO=['🏙️','🎨','📸','🔥','💃','🛍️','😈','⭐']
END=[22.8,23.2]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
FANC='#8e8e93,#c8c8cc,#8e8e93'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#0b1a3a,#2a3a6a 55%,#1c1c1e 55%)">
 <div id="ct1" style="position:absolute;left:0;right:0;top:0;height:380px"></div>
 <div style="position:absolute;left:24px;right:24px;top:24px;background:rgba(0,0,0,.6);border-radius:20px;padding:12px 18px;font-size:22px;font-weight:800">🏙️ Апартаменты · 86 этаж · <span style="color:#30d158">свободно</span></div>
 <div style="position:absolute;left:60px;top:470px;width:480px;height:110px;border-radius:40px 40px 16px 16px;background:#3a3a3c"></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#000">
 <div id="wh2" style="position:absolute;inset:20px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:12px">
  <div id="w2_0" style="background:#ff2d78;position:relative;overflow:hidden;border-radius:12px"><div class="ch" data-p="b0"></div></div>
  <div id="w2_1" style="background:#ffd60a;position:relative;overflow:hidden;border-radius:12px"><div class="ch" data-p="b1"></div></div>
  <div id="w2_2" style="background:#30d158;position:relative;overflow:hidden;border-radius:12px"><div class="ch" data-p="b2"></div></div>
  <div id="w2_3" style="background:#0a84ff;position:relative;overflow:hidden;border-radius:12px"><div class="ch" data-p="b3"></div></div></div>
</div>
<div class="card" id="c3" style="background:#111">
 <div style="position:absolute;inset:30px;border:3px solid rgba(255,255,255,.5);border-radius:20px"></div>
 <div style="position:absolute;left:30px;top:30px;font:800 22px 'JetBrains Mono';color:#ff453a">● REC</div><div style="position:absolute;right:40px;top:34px;font:800 20px 'JetBrains Mono'">ISO 400 · 1/250</div>
 <div style="position:absolute;left:270px;top:315px;width:60px;height:60px;border:3px solid #ffd60a"></div>
 <div class="ch" data-p="c"></div>
 <div id="fl3" style="position:absolute;inset:0;background:#fff;opacity:0;z-index:8"></div>
 <div id="pl3" style="position:absolute;left:170px;top:120px;width:260px;height:310px;background:#fff;padding:14px 14px 60px;transform:rotate(-6deg);opacity:0;z-index:9;box-shadow:0 20px 40px rgba(0,0,0,.6)"><div style="width:100%;height:100%;background:linear-gradient(135deg,#ff8ac4,#5e2cff);position:relative;overflow:hidden"><div class="ch" data-p="c2"></div></div><div style="position:absolute;left:0;right:0;bottom:14px;text-align:center;font:700 22px 'Comic Sans MS',cursive;color:#111">я 📸</div></div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div class="hdr" style="color:#ff375f">Оценка образа</div>
 <div style="position:absolute;left:330px;top:90px;width:230px;height:500px;border-radius:120px 120px 20px 20px;background:linear-gradient(135deg,#d9e6f2,#8aa0b8);border:10px solid #c8a24a"></div>
 <div class="ch" data-p="d"></div>
 <div id="sc4" style="position:absolute;left:30px;top:110px;font-size:100px;font-weight:900;color:#30d158">0/10</div>
 <div id="sb4" style="position:absolute;left:30px;top:240px;width:260px;font-size:24px;font-weight:800;color:#aeaeb2;line-height:1.5">кепка ✓<br>очки ✓<br>цепь ✓<br>вайб ✓</div>
</div>
<div class="card" id="c5" style="background:#0a0a0a">
 <div style="position:absolute;left:200px;top:0;width:200px;height:690px;background:linear-gradient(90deg,#222,#3a3a3c 50%,#222);transform:perspective(500px) rotateX(40deg);transform-origin:50% 100%"></div>
 <div id="fl5" style="position:absolute;inset:0"></div>
 <div class="hdr" style="color:#fff">FASHION WEEK · ПОКАЗ</div>
 <div class="ch" data-p="e"></div>
</div>
<div class="card" id="c6" style="background:#f2f2f2;color:#111">
 <div class="hdr" style="color:#111">Корзина · бутик</div>
 <div id="bg6" style="position:absolute;left:20px;right:20px;top:120px;display:flex;justify-content:center;gap:16px"></div>
 <div id="tt6" class="c mono" style="top:360px;font-size:34px;font-weight:900">итого: 0 ₽</div>
 <div class="ch" data-p="f"></div>
</div>
<div class="card" id="c7" style="background:linear-gradient(180deg,#e8e0d0,#c8b8a0);color:#111">
 <div style="position:absolute;left:0;right:0;top:30px;text-align:center;font:900 italic 48px Georgia,serif;letter-spacing:-1px">Дьявол <span style="font-size:30px">носит</span> PRADA</div>
 <div style="position:absolute;left:0;right:0;top:92px;text-align:center;font:700 18px Inter;letter-spacing:6px;color:#555">В ГЛАВНОЙ РОЛИ — ЛАЛИ</div>
 <div class="ch" data-p="g"></div>
 <div id="hn7" style="position:absolute;z-index:6;opacity:0"><div style="position:absolute;left:0;top:0;width:0;height:0;border-left:16px solid transparent;border-right:16px solid transparent;border-bottom:44px solid #d0021b"></div><div style="position:absolute;left:92px;top:0;width:0;height:0;border-left:16px solid transparent;border-right:16px solid transparent;border-bottom:44px solid #d0021b"></div></div>
 <div id="bg7" style="position:absolute;left:390px;top:470px;width:110px;height:120px;background:#111;border-radius:10px;color:#fff;font:900 22px Inter;display:flex;align-items:center;justify-content:center;opacity:0">PRADA</div>
</div>
<div class="card" id="c8" style="background:radial-gradient(ellipse at 50% 20%,#3a1a5a,#0a0614 70%)">
 <div class="ch" data-p="h"></div>
 <div id="fn8" style="position:absolute;inset:0"></div>
 <div id="cn8" class="c" style="top:30px;font-size:30px;font-weight:900;color:#ffd60a">фан-клуб: <span id="n8">0</span></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...(p.startsWith('x')?['#8e8e93','#c8c8cc','#8e8e93']:['#111','#ff8ac4','#ff2d78']));});
 let s='';for(let i=0;i<12;i++){const w=30+rnd(i)*40,h=120+rnd(i+9)*240;s+=`<div style="position:absolute;left:${i*52-10}px;bottom:0;width:${w}px;height:${h}px;background:#0f1726;border-top:3px solid #64d2ff"></div>`}$('ct1').innerHTML=s;
 let f='';for(let i=0;i<8;i++)f+=`<div class="ch" data-p="x${i}" id="ch_x${i}">${CH('x'+i,'#8e8e93','#c8c8cc','#8e8e93')}</div><div id="sg${i}" style="position:absolute;background:#fff;color:#ff2d78;font:900 18px Inter;padding:4px 8px;border-radius:6px;z-index:6;white-space:nowrap">ЛАЛИ ❤</div>`;$('fn8').innerHTML=f;})();'''
RENDER='''
 {place('a',300,560,1.0,false);pose('a',t>=3.3?{aL:150,aR:-150,hd:-6,bob:Math.sin(t*3)*3}:{aL:8,aR:-8,hd:-5});}
 {const T=[3.9,4.5,4.74,5.2];const H=[0,120,200,280];for(let i=0;i<4;i++){const e=$('w2_'+i);e.style.opacity=t>=T[i]?1:.08;e.style.transform=`scale(${1+.08*pop(t,T[i],8)})`;
   place('b'+i,135,305,.95,i%2==1);pose('b'+i,[{aL:8,aR:-8},{aL:150,aR:-8},{aL:8,aR:-150},{aL:150,aR:-150,open:1}][i]);$('ch_b'+i).style.filter=`hue-rotate(${H[i]}deg) saturate(1.6)`;}}
 {place('c',300,640,1.4,false);pose('c',t>=6.12?{aL:90,aR:-90,open:1}:{aL:8,aR:-8});$('fl3').style.opacity=pop(t,6.12,9);$('pl3').style.opacity=seg(t,6.4,6.5);$('pl3').style.transform=`rotate(-6deg) translateY(${(1-eb(seg(t,6.4,6.7)))*300}px)`;
  place('c2',116,290,.8,false);pose('c2',{aL:90,aR:-90,open:1});}
 {place('d',445,600,1.2,true);pose('d',t>=8.84?{aL:150,aR:-150,open:1}:{aL:8,aR:-60,hd:-8});const v=t<8.84?Math.round(10*seg(t,7.68,8.6)):10;$('sc4').textContent=(t>=8.84?'11':v)+'/10';$('sc4').style.transform=`scale(${1+.3*pop(t,8.84,7)})`;}
 {const k=seg(t,9.6,11.4);place('e',300,lerp(450,700,k),lerp(.7,1.25,k),false);pose('e',walk(t,7));let f='';for(let i=0;i<10;i++){const s=9.6+i*.17;if(t>=s&&t<s+.12)f+=`<div style="position:absolute;left:${rnd(i)>.5?20+rnd(i+1)*120:440+rnd(i+2)*120}px;top:${200+rnd(i+3)*400}px;width:70px;height:70px;border-radius:50%;background:radial-gradient(circle,#fff,rgba(255,255,255,0) 70%)"></div>`}$('fl5').innerHTML=f;}
 {const T=[11.62,12.32,12.94];$('bg6').innerHTML=T.filter(s=>t>=s).map((s,i)=>`<div style="width:160px;height:200px;background:#111;border-radius:12px;color:#fff;font:900 30px Inter;display:flex;align-items:center;justify-content:center;transform:translateY(${(1-eb(seg(t,s,s+.25)))*-200}px) rotate(${(i-1)*6}deg)">PRADA</div>`).join('');
  const n=T.filter(s=>t>=s).length;$('tt6').textContent='итого: '+fmt(n*389000)+' ₽';place('f',470,690,.8,true);pose('f',n?{aL:150,aR:-150,open:1}:{aL:8,aR:-8});}
 {place('g',300,640,1.45,false);pose('g',{aL:8,aR:t>=14.84?-90:-8,hd:t>=14.34?-8:0});const hx=300-100*1.45+60,hy=640-290*1.45+30;$('hn7').style.left=(300-62)+'px';$('hn7').style.top=(640-290*1.45+28)+'px';$('hn7').style.opacity=seg(t,14.34,14.45);$('bg7').style.opacity=seg(t,14.84,14.95);
  $('ch_g').style.filter=t>=14.34?'drop-shadow(0 0 30px #ff2d2d)':'none';}
 {place('h',300,330,1.0,false);pose('h',{aL:150+Math.sin(t*8)*15,aR:-150+Math.sin(t*8)*15,open:1,bob:-Math.abs(Math.sin(t*8))*8});
  const S=[15.28,16.66,17.26,18.56,19.2,20.46,21.14,22.34];let n=0;for(let i=0;i<8;i++){const on=t>=S[i];if(on)n++;const x=40+(i%4)*140,y=i<4?690:560;place('x'+i,x+60,y,.7,i%2==1);pose('x'+i,{aL:150+Math.sin(t*10+i)*20,aR:-150+Math.sin(t*10+i)*20,bob:-Math.abs(Math.sin(t*10+i))*10});
   $('ch_x'+i).style.display=on?'block':'none';const sg=$('sg'+i);sg.style.display=on?'block':'none';sg.style.left=(x+10)+'px';sg.style.top=(y-260+Math.sin(t*10+i)*6)+'px';}
  $('n8').textContent=fmt(n*1250000);$('cn8').style.transform=`scale(${1+.15*pop(t,S[Math.max(0,n-1)],8)})`;}
'''
