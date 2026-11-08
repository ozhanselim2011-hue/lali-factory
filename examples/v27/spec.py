BG='linear-gradient(180deg,#14100a,#050403)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["выход",1.0],["один,",1.5],["братан,",1.75],["мой",2.5],["гениальный",3.25],["план",4.5]],
 [["это",5.5],["наш",5.75],["тайный",6.0],["клан",6.5]],
 [["будем",7.5],["как",8.0],["Гунн",8.75],["и",9.0],["Алан",9.25]],
 [["хочешь",10.5],["не",10.75],["пить?",11.0],["не",11.75],["пей",12.0]],
 [["хочешь",12.75],["побить?",13.25],["не",14.0],["бей",14.25]],
 [["хочешь",15.0],["кричать?",15.5],["нехай,",16.25],["хай-",16.75],["хай",17.25]],
]
SC=[[-0.3,5.4],[5.4,7.4],[7.4,10.4],[10.4,12.65],[12.65,14.9],[14.9,99]]
GLOW=['#5a4a1a','#2a2a2a','#5a2a0a','#1a3a5a','#5a1a1a','#7a0a3a']
PEMO=['💡','🕶️','⚔️','🙅','🥊','📢']
END=[17.3,17.65]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr" style="color:#ffd60a">Заметки</div><div class="ttl">План 🧠</div>
 <div id="pl1" style="position:absolute;left:36px;right:36px;top:170px;font-size:26px;font-weight:700;line-height:1.8"></div>
 <div id="ex1" style="position:absolute;right:30px;top:40px;background:#30d158;color:#000;border-radius:12px;padding:6px 14px;font-size:22px;font-weight:900;opacity:0">🚪 ВЫХОД: 1</div>
 <div class="ch" data-p="a"></div>
 <div id="bulb" style="position:absolute;font-size:70px;opacity:0;z-index:7">💡</div>
</div>
<div class="card" id="c2" style="background:#0c0c0e">
 <div style="padding:26px 30px 16px;border-bottom:1px solid #222;display:flex;gap:14px;align-items:center"><div style="width:58px;height:58px;border-radius:50%;background:#2c2c2e;display:flex;align-items:center;justify-content:center;font-size:30px">🕶️</div><div><div style="font-size:26px;font-weight:900">Тайный клан</div><div id="m2" style="font-size:20px;color:#8e8e93;font-weight:600">1 участник</div></div></div>
 <div class="ch" data-p="b"></div><div class="ch" data-p="c"></div><div class="ch" data-p="d"></div>
</div>
<div class="card" id="c3" style="background:linear-gradient(180deg,#3a1a0a,#0a0402)">
 <div id="n3a" style="position:absolute;left:30px;top:60px;font-size:60px;font-weight:900;color:#ff9f0a;opacity:0">ГУНН</div>
 <div id="n3b" style="position:absolute;right:30px;top:60px;font-size:60px;font-weight:900;color:#64d2ff;opacity:0">АЛАН</div>
 <div class="ch" data-p="e"></div><div class="ch" data-p="f"></div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div class="hdr" style="color:#0a84ff">‹ Настройки</div><div class="ttl">Свобода</div>
 <div style="padding:26px 30px 0"><div class="row" style="background:#2c2c2e">🍺 <span>Пить</span><div class="tg" id="tg4"><b></b></div></div></div>
 <div class="ch" data-p="g"></div>
 <div id="t4" class="c" style="top:200px;font-size:30px;font-weight:900;color:#30d158;opacity:0">не пей ✓ твой выбор</div>
</div>
<div class="card" id="c5" style="background:#1c1c1e">
 <div class="hdr" style="color:#0a84ff">‹ Настройки</div><div class="ttl">Свобода</div>
 <div style="padding:26px 30px 0"><div class="row" style="background:#2c2c2e">🥊 <span>Бить</span><div class="tg" id="tg5"><b></b></div></div></div>
 <div class="ch" data-p="h"></div>
 <div id="t5" class="c" style="top:200px;font-size:30px;font-weight:900;color:#30d158;opacity:0">не бей ✓</div>
</div>
<div class="card" id="c6" style="background:radial-gradient(circle at 50% 60%,#5a0a2a,#0a0206)">
 <div style="position:absolute;left:40px;right:40px;top:40px;height:40px;border-radius:20px;background:#2c2c2e;overflow:hidden"><div id="lv6" style="height:100%;width:0;background:linear-gradient(90deg,#30d158,#ffd60a,#ff453a)"></div></div>
 <div id="hy" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="i"></div><div class="ch" data-p="j"></div><div class="ch" data-p="k"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
const HOOD=['#2c2c2e','#4a4a52','#141418'];
(function(){const H={c:1,d:1,j:1,k:1};document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...(H[p]?HOOD:(p=='f'?['#ff9f0a','#64d2ff','#0a5ad8']:['#64d2ff','#ff8ac4','#ff2d78'])));});
 $('pl1').innerHTML=['1. найти выход','2. собрать своих','3. ???','4. гениально'].map((l,i)=>`<div id="p1_${i}" style="opacity:0">☐ ${l}</div>`).join('');
 let h='';for(let i=0;i<10;i++)h+=`<div id="hy${i}" style="position:absolute;font-size:${40+i%3*14}px;font-weight:900;color:#fff;opacity:0">ХАЙ</div>`;$('hy').innerHTML=h;})();
'''
RENDER='''
 {[1.0,1.75,2.5,3.25].forEach((s,i)=>{const e=$('p1_'+i);e.style.opacity=seg(t,s,s+.15);if(t>=4.5)e.textContent='☑ '+e.textContent.slice(2);});$('ex1').style.opacity=seg(t,1.5,1.65);
  place('a',430,660,1.0,true);pose('a',t>=4.5?{aL:8,aR:-150,open:1,bob:-pop(t,4.5,5)*40}:{aL:-40,aR:112,hd:-8+Math.sin(t*2)*4});
  $('bulb').style.opacity=t>=4.5?1:0;$('bulb').style.left='395px';$('bulb').style.top=(320-pop(t,4.5,5)*40)+'px';$('bulb').style.transform=`scale(${1+.4*pop(t,4.5,5)})`;}
 {const n=t<5.75?1:(t<6.0?2:3);$('m2').textContent=n+' участника'+(t>=6.5?' · 🔒 секретно':'');
  [['b',300,1.1],['c',150,.9],['d',450,.9]].forEach(([p,x,s],i)=>{const on=t>=[5.5,5.75,6.0][i];place(p,x,660,s,i==2);$('ch_'+p).style.opacity=on?1:0;
   pose(p,t>=6.5?{aL:8,aR:-8,hd:-6,rot:-4,bob:-pop(t,6.5,6)*20}:{aL:-58,aR:58,hd:6});});}
 {$('n3a').style.opacity=seg(t,8.75,8.9);$('n3b').style.opacity=seg(t,9.25,9.4);place('e',190,660,1.1,false);place('f',410,660,1.1,true);
  pose('e',t>=8.75?{aL:8,aR:-165+Math.sin(t*10)*10,open:1}:{aL:-40,aR:40});pose('f',t>=9.25?{aL:8,aR:-165+Math.sin(t*10)*10,open:1}:{aL:-40,aR:40});}
 {tog('tg4',t<12.0);$('t4').style.opacity=seg(t,12.0,12.15);place('g',300,670,1.15,false);pose('g',t<11.75?{aL:55,aR:-55,hd:12,open:1}:{aL:8,aR:-95});}
 {tog('tg5',t<14.25);$('t5').style.opacity=seg(t,14.25,14.4);place('h',300,670,1.15,false);pose('h',t<14.0?{aL:-30,aR:-120+Math.sin(t*20)*20}:{aL:8,aR:-8,hd:4});}
 {const l=t<15.5?0:eo(seg(t,15.5,16.5));$('lv6').style.width=(l*100)+'%';
  [['i',300,1.1],['j',140,.85],['k',460,.85]].forEach(([p,x,s],i)=>{place(p,x,670,s,i==2);pose(p,t>=16.25?{aL:150+Math.sin(t*12)*15,aR:-150-Math.sin(t*12)*15,open:1,bob:-Math.abs(Math.sin(t*8))*20}:{aL:8,aR:-8});});
  for(let i=0;i<10;i++){const st=16.25+i*.12;const ph=seg(t,st,st+.8);const e=$('hy'+i);e.style.opacity=ph>0&&ph<1?1-ph:0;e.style.left=(80+rnd(i)*400)+'px';e.style.top=(380-ph*300)+'px';e.style.transform=`rotate(${(rnd(i+3)-.5)*30}deg) scale(${.8+ph})`;}
  if(si==5)shake('c6',t,16.75,10),shake('c6',t,17.25,10);}
'''
