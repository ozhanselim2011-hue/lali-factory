DUR=10.6
FADE=10.2
START=0
SONG='5UTRA — А ты мне докажи'
BG='linear-gradient(180deg,#160a14,#060306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["А",0.0],["ты",0.1],["мне",0.3],["докажи,",0.44]],
 [["что",1.28],["ты",1.6],["меня",1.8],["очень",2.12],["любишь,",2.64]],
 [["а",3.54],["то",4.12],["не",4.34],["верю",4.48],["я,",4.94]],
 [["не",5.12],["верят",5.22],["люди",5.62]],
 [["покажи",6.76],["мне",7.4],["чувства,",7.58]],
 [["и",8.14],["может",8.32],["будет",8.52],["переплетенье",8.96],["судеб",9.96]],
]
SC=[[-0.3,3.4],[3.4,5.05],[5.05,6.65],[6.65,8.05],[8.05,99]]
GLOW=['#5a1d4a','#7a0a0a','#3a3a5a','#1d3a7a','#7a0a2a']
PEMO=['📎','📈','👥','⏳','🧵']
END=[10.2,10.6]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:#ff2d55">Заявка · от неё</div>
 <div style="position:absolute;left:30px;right:30px;top:80px;background:#fff;border-radius:22px;padding:20px;box-shadow:0 6px 18px rgba(0,0,0,.08)"><div style="font:900 30px Inter">Докажи, что любишь</div>
  <div id="lv1" style="margin-top:14px;font:800 24px Inter;color:#888">любишь: ☐ да ☐ очень</div>
  <div id="at1" style="margin-top:14px;border:3px dashed #ff2d55;border-radius:16px;padding:14px;text-align:center;font:900 22px Inter;color:#ff2d55">📎 прикрепить доказательства</div></div>
 <div class="ch" data-p="a"></div><div class="ch" data-p="b"></div>
</div>
<div class="card" id="c2" style="background:#0e1a12">
 <div class="hdr" style="color:#30d158">Полиграф</div>
 <svg id="pg2" width="560" height="260" style="position:absolute;left:20px;top:90px"></svg>
 <div id="nv2" class="c" style="top:360px;font:900 70px Inter;color:#ff453a;opacity:0">НЕ ВЕРЮ</div>
 <div class="ch" data-p="b2"></div>
</div>
<div class="card" id="c3" style="background:#1c1c1e">
 <div class="hdr" style="color:#64d2ff">Опрос · вы верите, что он любит?</div>
 <div style="position:absolute;left:30px;right:30px;top:90px;font:900 26px Inter"><div style="display:flex;justify-content:space-between"><span>верим</span><span id="y3">0%</span></div><div style="height:22px;border-radius:11px;background:#2c2c2e;margin:6px 0 18px;overflow:hidden"><div id="yb3" style="height:100%;background:#30d158;width:0"></div></div>
  <div style="display:flex;justify-content:space-between"><span>не верим</span><span id="n3">0%</span></div><div style="height:22px;border-radius:11px;background:#2c2c2e;margin-top:6px;overflow:hidden"><div id="nb3" style="height:100%;background:#ff453a;width:0"></div></div></div>
 <div id="cr3" style="position:absolute;left:0;right:0;top:330px;height:360px"></div>
</div>
<div class="card" id="c4" style="background:#000">
 <div class="hdr" style="color:#ff375f">Его чувства · загрузка</div>
 <div style="position:absolute;left:40px;right:40px;top:110px;height:30px;border-radius:15px;background:#2c2c2e;overflow:hidden"><div id="ld4" style="height:100%;background:linear-gradient(90deg,#ff2d78,#ff8ac4);width:0"></div></div>
 <div id="pc4" class="c mono" style="top:160px;font-size:50px;font-weight:900">0%</div>
 <div id="ht4" class="c" style="top:230px;font-size:150px;opacity:0">❤️</div>
 <div class="ch" data-p="b3"></div>
</div>
<div class="card" id="c5" style="background:radial-gradient(circle at 50% 40%,#3a0a1a,#120408)">
 <svg id="th5" width="600" height="690" style="position:absolute;inset:0;z-index:6"></svg>
 <div class="ch" data-p="a2"></div><div class="ch" data-p="b4"></div>
 <div id="ok5" class="c" style="top:60px;font:900 36px Inter;color:#ff2d78;opacity:0">переплетение судеб ✓</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...(p.startsWith('b')?['#111','#64d2ff','#0a84ff']:['#ff2d78','#ff8ac4','#ff2d78']));});})();'''
RENDER='''
 {place('a',140,690,.9,false);pose('a',{aL:8,aR:t>=0.44?-90:-8,open:t>=0.44,hd:-6});place('b',470,690,.9,true);pose('b',{aL:8,aR:-8,hd:t>=2.64?Math.sin(t*20)*8:0});$('ch_b').style.transform+=` translateX(${t>=2.64?Math.sin(t*50)*3:0}px)`;
  $('at1').style.transform=`scale(${1+.08*Math.sin(t*6)})`;$('lv1').style.color=t>=2.64?'#ff2d55':'#888';}
 {let p='';for(let x=0;x<=560;x+=6){const amp=t<4.48?10:lerp(10,110,seg(t,4.48,4.9));p+=`${x},${130+Math.sin(x*.09+t*14)*amp*(rnd(Math.floor(x/30)+Math.floor(t*10))*.6+.4)} `;}$('pg2').innerHTML=`<polyline points="${p}" fill="none" stroke="#30d158" stroke-width="4"/>`;
  $('nv2').style.opacity=seg(t,4.48,4.55);$('nv2').style.transform=`scale(${1+.4*pop(t,4.48,8)}) rotate(-5deg)`;place('b2',300,690,.7,false);pose('b2',{aL:8,aR:-8,hd:Math.sin(t*25)*6,open:1});}
 {const k=eo(seg(t,5.22,5.9));$('y3').textContent=Math.round(2*k)+'%';$('n3').textContent=Math.round(98*k)+'%';$('yb3').style.width=2*k+'%';$('nb3').style.width=98*k+'%';
  let c='';for(let i=0;i<9;i++){const x=20+(i%5)*115+(i>4?55:0),y=i>4?130:30;c+=`<div style="position:absolute;left:${x}px;top:${y}px;transform:rotate(${t>=5.62?Math.sin(t*10+i)*14:0}deg)"><div style="width:70px;height:70px;border-radius:50%;background:#8e8e93"></div><div style="width:100px;height:120px;margin-left:-15px;border-radius:50px 50px 0 0;background:#8e8e93"></div></div>`}$('cr3').innerHTML=c;}
 {const v=t<7.58?lerp(0,12,seg(t,6.76,7.5)):lerp(12,100,eo(seg(t,7.58,8.0)));$('ld4').style.width=v+'%';$('pc4').textContent=Math.round(v)+'%';$('ht4').style.opacity=seg(t,7.9,8.0);place('b3',300,690,.75,false);pose('b3',{aL:8,aR:-8,hd:-10});}
 {const k=eo(seg(t,8.14,9.96));place('a2',lerp(120,230,k),690,1.0,false);place('b4',lerp(480,370,k),690,1.0,true);pose('a2',{aL:8,aR:-60*k,open:t>=9.96});pose('b4',{aL:8,aR:-60*k,open:t>=9.96});
  const ax=lerp(120,230,k)+50,bx=lerp(480,370,k)-50;let d='';for(let s=0;s<2;s++){let p=`M${ax} 500 `;for(let i=1;i<=10;i++){const x=lerp(ax,bx,i/10),y=500+Math.sin(i*1.2+s*Math.PI+t*4)*40*k;p+=`L${x} ${y} `}d+=`<path d="${p}" stroke="#ff2d55" stroke-width="6" fill="none" stroke-dasharray="1000" stroke-dashoffset="${1000*(1-seg(t,8.14,9.0))}"/>`}
  if(t>=9.96)d+=`<circle cx="${(ax+bx)/2}" cy="500" r="${18+6*pop(t,9.96,6)}" fill="#ff2d55"/>`;$('th5').innerHTML=d;$('ok5').style.opacity=seg(t,9.96,10.05);}
'''
