DUR=19.8
FADE=19.4
START=0
SONG='bigpluggssd & YouRunPlugg — Пойдём со мною'
BG='linear-gradient(180deg,#120a16,#050306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Гадкие",0.0],["мальчишки,",0.84],["они",1.92],["не",2.36],["понимают",2.56]],
 [["они",3.72],["всегда",4.08],["глупышки",4.46]],
 [["они",5.4],["готовы",5.82],["дать",6.4],["всё,",6.62],["чтобы",6.8],["с",7.08],["тобой",7.28]],
 [["но",7.68],["ты",7.86],["со",8.04],["мною",8.26]],
 [["порубят",9.12],["кабину,",9.88],["я",10.52],["потом",10.74],["всё",11.06],["это",11.4],["смою",11.74]],
 [["в",12.5],["горизонт",12.82],["на",13.48],["8",13.58],["я",13.9],["твоё",14.12],["лицо",14.72],["закрою",15.16]],
 [["ты",15.86],["всегда",16.38],["со",16.74],["мной,",17.02],["ты",17.4],["станешь",17.52],["для",18.06],["меня",18.18],["женой",18.5]],
]
SC=[[-0.3,3.6],[3.6,5.3],[5.3,7.6],[7.6,9.0],[9.0,12.4],[12.4,15.8],[15.8,99]]
GLOW=['#7a1f4a','#7a6a1a','#7a1f2a','#1a5c4e','#1a4a7a','#5a1d7a','#7a5a1a']
PEMO=['❌','🧠','🎁','📍','🚿','🙈','💍']
END=[19.4,19.8]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr">Знакомства · анкеты</div>
 <div class="c" style="top:250px;font-size:30px;font-weight:900;color:#8e8e93">Анкеты закончились 🤷<br>все не понимают</div>
 <div id="pf1" style="position:absolute;left:0;right:0;top:70px;height:420px"></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#fff7c2,#ffd84d);color:#111">
 <div class="c" style="top:60px;font-size:130px">🧠</div>
 <div class="c" style="top:230px;font-size:30px;font-weight:900">Загрузка мозга…</div>
 <div style="position:absolute;left:60px;right:60px;top:290px;height:30px;border-radius:15px;background:rgba(0,0,0,.12);overflow:hidden"><div id="lb2" style="height:30px;background:#ff453a;width:0"></div></div>
 <div class="c mono" id="lp2" style="top:330px;font-size:40px;font-weight:900">0%</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#000">
 <div class="hdr">Её директ</div><div class="ttl">Подарков: <span id="gc3" class="mono" style="color:#ff2d55">0</span></div>
 <div id="gf3" style="position:absolute;inset:0;z-index:4"></div>
 <div id="rd3" style="position:absolute;left:24px;right:24px;top:540px;background:#2c2c2e;border-radius:20px;padding:12px 16px;font-size:24px;font-weight:800;color:#8e8e93;opacity:0;z-index:7">👀 Прочитано. Без ответа.</div>
</div>
<div class="card" id="c4" style="background:#d8e6d0">
 <svg width="600" height="690" style="position:absolute"><path d="M0 220 L600 280 M0 480 L600 400 M170 0 L230 690 M430 0 L390 690" stroke="#fff" stroke-width="18"/></svg>
 <div id="hp4" style="position:absolute;font-size:60px;z-index:6">📍</div>
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#fff;color:#111;border-radius:22px;padding:14px 20px;font-size:26px;font-weight:800;z-index:7">📍 Она: <span id="st4" style="color:#0a84ff">где-то там</span></div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c5" style="background:linear-gradient(180deg,#1a2a3a,#0a1018)">
 <div class="hdr" style="color:#64d2ff">Автомойка 🚿</div><div class="ttl">Чистота <span id="cl5" class="mono">0%</span></div>
 <div id="tk5" style="position:absolute;left:300px;top:250px;font-size:170px;filter:sepia(1) brightness(.5);z-index:3">🚚</div>
 <div id="dr5" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c6" style="background:#111214">
 <div class="hdr">Редактор фото</div>
 <div style="position:absolute;left:100px;top:80px;width:400px;height:400px;border-radius:30px;background:linear-gradient(135deg,#ff8ac4,#5e2cff);overflow:hidden"><div class="c" style="top:90px;font-size:200px">👩</div><div id="sk6" style="position:absolute;left:110px;top:70px;font-size:190px;opacity:0">❤️</div></div>
 <div id="bt6" style="position:absolute;left:40px;right:200px;top:500px;height:60px;border-radius:30px;background:#ff2d55;font-size:24px;font-weight:900;display:flex;align-items:center;justify-content:center;z-index:7">🙈 скрыть от всех</div>
 <div class="ch" data-p="e"></div>
</div>
<div class="card" id="c7" style="background:radial-gradient(circle at 50% 35%,#5a3a0a,#140a02)">
 <div class="c" style="top:40px;font-size:24px;font-weight:800;color:#ffd60a">Семейное положение</div>
 <div class="c" id="ms7" style="top:76px;font-size:44px;font-weight:900">всегда со мной</div>
 <div id="rg7" style="position:absolute;left:245px;top:180px;font-size:110px;opacity:0;z-index:6">💍</div>
 <div class="ch" data-p="f"></div><div class="ch" data-p="g"></div>
 <div id="cf7" style="position:absolute;inset:0;z-index:7"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=p=='g'?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 $('pf1').innerHTML=['Петя, 17 · «а чё ты обиделась?»','Ваня, 18 · «к? норм»','Саша, 17 · «го в доту»'].map((s,i)=>`<div id="f1_${i}" style="position:absolute;left:60px;right:60px;top:${i*12}px;height:330px;border-radius:30px;background:linear-gradient(135deg,#3a3a5a,#1a1a2a);border:2px solid #444;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:24px;font-weight:800;text-align:center;padding:0 20px"><div style="font-size:110px">🧢</div>${s}<div id="x1_${i}" style="position:absolute;right:20px;top:20px;font-size:60px;opacity:0">❌</div></div>`).join('');
 const G=['🌹','🧸','💐','📱','🍫','💎','🎧','👟'];let g='';for(let i=0;i<16;i++)g+=`<div id="g3_${i}" style="position:absolute;font-size:56px;opacity:0">${G[i%8]}</div>`;$('gf3').innerHTML=g;
 let d='';for(let i=0;i<20;i++)d+=`<div id="w5_${i}" style="position:absolute;width:8px;height:22px;border-radius:4px;background:#64d2ff;opacity:0"></div>`;$('dr5').innerHTML=d;
 let c='';for(let i=0;i<24;i++)c+=`<div id="k7_${i}" style="position:absolute;width:12px;height:18px;background:${['#ffd60a','#ff2d78','#64d2ff','#30d158'][i%4]};opacity:0"></div>`;$('cf7').innerHTML=c;})();
'''
RENDER='''
 {for(let i=0;i<3;i++){const k=2-i,s=[0.84,1.92,2.56][k];const e=$('f1_'+k);const o=eo(seg(t,s+.15,s+.55));e.style.transform=`translateX(${-o*600}px) rotate(${-o*25}deg)`;$('x1_'+k).style.opacity=seg(t,s,s+.1);e.style.zIndex=3+k;}
  place('a',470,690,.8,true);pose('a',t>=2.56?{aL:8,aR:-150,hd:12}:{aL:8,aR:-8});}
 {const p=t<4.46?eo(seg(t,3.72,4.4))*3:3;$('lb2').style.width=p+'%';$('lp2').textContent=(t>=4.46?'1':Math.round(p))+'%';place('b',300,690,1.0,false);pose('b',t>=4.46?{aL:60,aR:-60,hd:Math.sin(t*14)*12,open:1}:{aL:8,aR:-8});}
 {let n=0;for(let i=0;i<16;i++){const s=5.5+i*.11,k=eo(seg(t,s,s+.35));const e=$('g3_'+i);e.style.opacity=k>0?1:0;if(k>0)n++;e.style.left=lerp(rnd(i)*500,40+(i%8)*65,k)+'px';e.style.top=lerp(-80,180+Math.floor(i/8)*80+rnd(i+2)*120,k)+'px';}
  $('gc3').textContent=n*3;$('rd3').style.opacity=seg(t,7.2,7.3);}
 {const k=eo(seg(t,7.7,8.4));$('hp4').style.left=lerp(470,330,k)+'px';$('hp4').style.top=lerp(120,420,k)+'px';$('st4').textContent=t<8.04?'где-то там':'рядом с тобой ❤️';
  place('c',260,690,1.0,false);pose('c',t>=8.26?{aL:8,aR:-120,open:1}:{aL:8,aR:-8});}
 {const c=eo(seg(t,10.5,12.0));$('cl5').textContent=Math.round(c*100)+'%';$('tk5').style.filter=`sepia(${1-c}) brightness(${.5+c*.6})`;
  $('tk5').style.transform=`rotate(${t>=9.12&&t<10.4?Math.sin(t*40)*4:0}deg)`;place('d',150,690,1.0,false);pose('d',t>=10.52?{aL:8,aR:-100,open:1}:{aL:8,aR:-8,hd:10});
  for(let i=0;i<20;i++){const e=$('w5_'+i);const ph=(t*2+i*.05)%1;e.style.opacity=t>10.52&&t<12.2?1:0;e.style.left=(230+ph*170+(i%3)*8)+'px';e.style.top=(450-ph*80+Math.sin(i)*20)+'px';e.style.transform='rotate(-60deg)';}}
 {$('sk6').style.opacity=seg(t,15.16,15.25);$('sk6').style.transform=`scale(${1+.3*pop(t,15.16,6)})`;$('bt6').style.transform=`scale(${1-.08*pop(t,15.1,10)})`;
  place('e',510,690,.8,true);pose('e',t>=14.72?{aL:8,aR:-140,hd:-6}:{aL:8,aR:-30});}
 {const r=t>=17.52;$('ms7').textContent=t<18.5?'всегда со мной':'женаты 💍';$('rg7').style.opacity=seg(t,17.4,17.55);$('rg7').style.transform=`scale(${eb(seg(t,17.4,17.8))})`;
  place('f',200,690,1.0,false);place('g',400,690,1.0,true);pose('f',r?{aL:8,aR:-90,lL:-25,bob:20}:{aL:8,aR:-30});pose('g',t>=18.5?{aL:120,aR:-120,open:1}:{aL:8,aR:-8,hd:-6});
  for(let i=0;i<24;i++){const k=seg(t,18.5,19.8);const e=$('k7_'+i);e.style.opacity=k>0?1:0;e.style.left=(rnd(i)*580)+'px';e.style.top=(-20+k*700*(.6+rnd(i+5)*.6))+'px';e.style.transform=`rotate(${k*600+i*30}deg)`;}}
'''
