BG='linear-gradient(180deg,#0c0c10,#040406)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["если",0.0],["это",0.2],["мечта,",0.4],["почему",0.8],["ты",1.0],["её",1.3],["не",1.5],["выбрал?",1.7]],
 [["они",2.1],["ноют",2.3],["в",2.6],["телеграммах,",2.7],["что",3.2],["культура",3.3],["их",3.8],["не",3.9],["приняла",4.0]],
 [["надо",4.3],["работать",4.6],["так,",5.1],["как",5.4],["будто",5.5],["до*уя",5.8],["кредитов",6.2]],
 [["и",6.7],["у",6.8],["тебя",6.9],["пару",7.2],["месяцев,",7.4],["чтобы",7.9],["закрыть",8.4]],
 [["а",8.9],["пока",8.95],["мелкие",9.1],["огни",9.6],["моего",10.0],["big",10.3],["city",10.5],["life",10.8]],
 [["падают",11.1],["ракетами",11.9],["на",12.5],["мокрый",12.6],["асфальт",12.9]],
 [["в",13.8],["окно",13.85],["на",14.1],["Арбате",14.2],["я",14.6],["буду",14.8],["это",15.0],["кричать",15.2]],
 [["я",15.7],["не",15.8],["могу",15.9],["проиграть,",16.1],["не",17.0],["могу",17.1],["проиграть",17.3]],
]
SC=[[-0.3,2.05],[2.05,4.25],[4.25,8.85],[8.85,13.75],[13.75,15.65],[15.65,99]]
GLOW=['#3a3a5a','#1d3a6a','#5a3a0a','#1d2a6a','#5a1a1a','#1a5c2e']
PEMO=['💭','😭','💳','🌃','📢','🏆']
END=[18.45,18.93]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr">Выбор</div><div class="ttl">Что выбрать?</div>
 <div style="position:absolute;left:30px;right:30px;top:170px">
  <div class="row" style="background:#2c2c2e">🛋 <span>Стабильность</span><span id="k1a" style="margin-left:auto;color:#0a84ff;font-weight:900">✓</span></div>
  <div class="row" id="dr1" style="background:#2c2c2e">✨ <span>Мечта</span><span id="k1b" style="margin-left:auto;color:#0a84ff;font-weight:900"></span></div></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#0e1621">
 <div style="padding:24px 30px 14px;border-bottom:1px solid #1d2733;font-size:26px;font-weight:900">📣 Каналы · нытьё</div>
 <div id="wh2" style="position:absolute;left:24px;right:24px;top:90px"></div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#000">
 <div class="hdr">Банк · Кредиты</div>
 <div id="cr3" style="position:absolute;left:30px;right:30px;top:80px"></div>
 <div style="position:absolute;left:30px;right:30px;top:350px;display:flex;justify-content:space-between;font-size:24px;font-weight:800"><span>⏳ осталось</span><span id="dd3" class="mono" style="color:#ff9f0a">— дн.</span></div>
 <div style="position:absolute;left:30px;right:30px;top:390px;height:18px;border-radius:9px;background:#2c2c2e;overflow:hidden"><div id="db3" style="height:18px;background:#30d158;width:0"></div></div>
 <div class="ch" data-p="c"></div><div id="lp3" style="position:absolute;font-size:60px;z-index:6">💻</div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#0a0f2a,#05060f 60%,#0a0a12)">
 <div id="city" style="position:absolute;left:0;right:0;top:120px;height:300px"></div>
 <div style="position:absolute;left:0;right:0;top:420px;bottom:0;background:linear-gradient(180deg,#14161e,#0a0b10)"></div>
 <div id="rk4" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="d"></div>
 <div class="c" style="top:30px;font-size:30px;font-weight:900;letter-spacing:4px;color:#ffd60a">BIG CITY LIFE</div>
</div>
<div class="card" id="c5" style="background:#2a1d14">
 <div style="position:absolute;inset:0;background:repeating-linear-gradient(0deg,#3a2a1e 0 60px,#33251a 60px 62px)"></div>
 <div style="position:absolute;left:150px;top:180px;width:300px;height:360px;background:#ffe9a8;border:16px solid #f5f0e6;box-shadow:inset 0 0 60px rgba(255,160,0,.6)"></div>
 <div class="ch" data-p="e"></div>
 <div style="position:absolute;left:24px;top:24px;background:rgba(0,0,0,.6);border-radius:16px;padding:10px 16px;font-size:22px;font-weight:800">📍 Арбат</div>
 <div id="yl5" style="position:absolute;inset:0"></div>
</div>
<div class="card" id="c6" style="background:#000">
 <div id="go6" class="c" style="top:120px;font-size:84px;font-weight:900;color:#ff453a;font-family:'JetBrains Mono'">GAME OVER</div>
 <div id="lu6" class="c" style="top:120px;font-size:84px;font-weight:900;color:#30d158;font-family:'JetBrains Mono';opacity:0">LEVEL UP</div>
 <div id="no6" class="c" style="top:230px;font-size:26px;font-weight:800;color:#aeaeb2;opacity:0">проигрыш недоступен ✕</div>
 <div class="ch" data-p="f"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 $('wh2').innerHTML=['культура нас не приняла 😭','никто не слушает 😢','индустрия закрыта 🙄'].map((m,i)=>`<div id="w2_${i}" style="margin-bottom:12px;opacity:0"><div class="bub" style="background:#182533;font-size:24px">${m}</div></div>`).join('');
 $('cr3').innerHTML=[1,2,3,4,5].map(i=>`<div id="c3_${i}" style="display:flex;justify-content:space-between;background:#1c1c1e;border-radius:14px;padding:8px 16px;margin-bottom:6px;font-size:20px;font-weight:700;opacity:0"><span>💳 Кредит #${i}</span><span class="mono" style="color:#ff453a">−${i*120} 000 ₽</span></div>`).join('');
 let c='';for(let i=0;i<14;i++){const h=80+rnd(i)*200;c+=`<div style="position:absolute;left:${i*44}px;bottom:0;width:40px;height:${h}px;background:#111628">`;for(let j=0;j<12;j++)c+=`<div class="win" style="position:absolute;left:${6+(j%3)*11}px;top:${10+Math.floor(j/3)*22}px;width:6px;height:10px;background:#ffd60a;opacity:${rnd(i*12+j)>.5?.9:.1}"></div>`;c+='</div>';}$('city').innerHTML=c;
 let r='';for(let i=0;i<8;i++)r+=`<div id="r4_${i}" style="position:absolute;font-size:44px;opacity:0">🚀</div>`;$('rk4').innerHTML=r;
 let y='';for(let i=0;i<8;i++)y+=`<div id="y5_${i}" style="position:absolute;font-size:${30+i%3*12}px;font-weight:900;color:#fff;opacity:0">!!!</div>`;$('yl5').innerHTML=y;})();
'''
RENDER='''
 {const ch=t>=1.7;$('k1a').textContent=ch?'':'✓';$('k1b').textContent=ch?'✓':'';$('dr1').style.background=ch?'#3a1d6a':'#2c2c2e';
  place('a',300,670,1.15,false);pose('a',t<0.8?{aL:8,aR:-8}:(t<1.7?{aL:55,aR:-55,hd:12,open:1}:{aL:8,aR:-95,hd:-6}));}
 {[2.3,3.2,4.0].forEach((s,i)=>{$('w2_'+i).style.opacity=seg(t,s,s+.1);$('w2_'+i).style.transform=`scale(${eb(seg(t,s,s+.25))})`;$('w2_'+i).style.transformOrigin='left';});
  place('b',420,680,1.0,true);pose('b',t>=2.7?{aL:8,aR:145,hd:12}:{aL:8,aR:-8});}
 {[5.8,5.9,6.0,6.1,6.2].forEach((s,i)=>$('c3_'+(i+1)).style.opacity=seg(t,s,s+.05));const d=t<7.4?60:Math.round(lerp(60,0,seg(t,7.4,8.6)));$('dd3').textContent=(t<7.2?'—':d)+' дн.';
  $('db3').style.width=(seg(t,7.9,8.6)*100)+'%';const o=run(t,22);o.aR=-60;place('c',lerp(150,450,seg(t,4.6,8.6)),680,.9,false);pose('c',t>=4.6?o:{aL:8,aR:-8});
  const L=$('ch_c').getBoundingClientRect();$('lp3').style.left=(parseFloat($('ch_c').style.left)+150)+'px';$('lp3').style.top=(parseFloat($('ch_c').style.top)+180)+'px';$('lp3').style.opacity=t>=4.6?1:0;}
 {document.querySelectorAll('.win').forEach((w,i)=>{if(t>=9.6)w.style.opacity=Math.sin(t*3+i)>0.2?.95:.1;});
  for(let i=0;i<8;i++){const st=11.1+i*.25;const p=seg(t,st,st+.6);const e=$('r4_'+i);e.style.opacity=p>0&&p<1?1:0;e.style.left=(60+i*65)+'px';e.style.top=(80+p*380)+'px';e.style.transform='rotate(135deg)';}
  place('d',300,680,1.0,false);pose('d',t>=10.3?{aL:150,aR:-150,open:1,hd:-14}:{aL:8,aR:-8,hd:-12});}
 {place('e',300,560,1.0,false);const y=t>=15.2;pose('e',y?{aL:150+Math.sin(t*14)*10,aR:-150,open:1,hd:-10}:{aL:8,aR:-95});
  for(let i=0;i<8;i++){const ph=((t-15.2)*1.4+i/8)%1;const e=$('y5_'+i);e.style.opacity=y?1-ph:0;e.style.left=(300+Math.cos(i)*ph*260-20)+'px';e.style.top=(260-ph*200)+'px';}}
 {const u=t>=16.1;$('go6').style.opacity=u?0:1;$('go6').style.textDecoration=t>=15.9?'line-through':'none';$('lu6').style.opacity=seg(t,16.1,16.2);$('no6').style.opacity=seg(t,16.1,16.25);$('lu6').style.transform=`scale(${1+.3*pop(t,16.1,5)+.2*pop(t,17.3,5)})`;
  place('f',300,680,1.2,false);pose('f',u?{aL:8,aR:-165+Math.sin(t*16)*12,open:1,bob:-Math.max(pop(t,16.1,5),pop(t,17.3,5))*50}:{aL:-14,aR:14});
  if(t>=17.3){[1,2,3].forEach((n,ix)=>$('f_s'+n).setAttribute('stop-color',`hsl(${(t*240+ix*120)%360},100%,62%)`));$('ch_f').style.filter='drop-shadow(0 0 25px #30d158)';}}
'''
