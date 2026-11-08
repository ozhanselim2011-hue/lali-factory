DUR=13.2
FADE=12.8
START=0
SONG='Koss & ПЛУТТО — Земляк'
BG='linear-gradient(180deg,#0a0e14,#030406)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Ещё,",0.0],["пока",0.54],["в",1.02],["душе",1.26],["неразобранный",1.54],["бардак",2.32]],
 [["пока-пока,",2.86],["уезжаю,",3.86],["земляк",4.56]],
 [["всё,",5.04],["что",5.34],["с",5.58],["собой,",5.62],["зажму",6.02],["в",6.44],["кулак",6.58]],
 [["за",7.04],["спину",7.12],["флаг,",7.7],["вперёд,",8.0],["казак!",8.52]],
 [["как",9.26],["стекло",9.5],["плавится",10.12],["любовь",11.12]],
]
SC=[[-0.3,2.8],[2.8,5.0],[5.0,7.0],[7.0,9.15],[9.15,99]]
GLOW=['#5a3a1a','#1a4a7a','#5a5a1a','#7a1f1f','#7a3a1a']
PEMO=['🧳','🚆','✊','🚩','🫠']
END=[12.8,13.2]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#3a2a4a,#1a1222)">
 <div class="hdr">Душа · состояние</div><div class="ttl">Разобрано <span id="pr1" class="mono">0%</span></div>
 <div id="it1" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#0b1a2e">
 <div style="position:absolute;left:24px;right:24px;top:30px;background:#000;border-radius:18px;padding:16px 20px;font-family:'JetBrains Mono';color:#ffd60a">
  <div style="font-size:20px;color:#8e8e93">ОТПРАВЛЕНИЕ</div>
  <div style="display:flex;justify-content:space-between;font-size:30px;font-weight:800"><span>Москва → Ростов</span><span id="tm2">23:59</span></div>
  <div id="st2" style="font-size:24px;color:#30d158">посадка</div></div>
 <div id="tr2" style="position:absolute;top:300px;font-size:150px;z-index:4">🚆</div>
 <div class="ch" data-p="b"></div><div class="ch" data-p="c"></div>
</div>
<div class="card" id="c3" style="background:#1c1c1e">
 <div class="hdr">Ручная кладь</div><div class="ttl">Вес: <span id="kg3" class="mono">23 кг</span></div>
 <div id="sk3" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="d"></div>
 <div id="ok3" class="c" style="top:150px;font-size:28px;font-weight:900;color:#30d158;opacity:0">✅ всё в кулаке</div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#5aa8e8,#bfe3ff 55%,#d9b36a 56%,#a8823a)">
 <div class="ch" data-p="e"></div>
 <div id="fl4" style="position:absolute;font-size:90px;z-index:4">🚩</div>
 <div id="sp4" style="position:absolute;left:60px;top:80px;background:#fff;color:#111;border-radius:22px;padding:10px 20px;font-size:34px;font-weight:900;opacity:0">вперёд! 🐎</div>
</div>
<div class="card" id="c5" style="background:radial-gradient(circle at 50% 40%,#3a1a0a,#0a0402)">
 <div class="hdr" style="color:#ffb340">Температура чувств</div>
 <div class="c mono" id="tp5" style="top:70px;font-size:58px;font-weight:800;color:#ffb340">20°C</div>
 <div id="hr5" style="position:absolute;left:220px;top:180px;font-size:160px;transform-origin:50% 100%">❤️</div>
 <div class="ch" data-p="f"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=p=='c'?CH(p,'#ff9f0a','#8e8e93','#5a5a5e'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 const E=['👕','🧦','📦','💔','🎧','📱','🧸','📸','🧦','🗝️','💌','🥫'];let s='';E.forEach((e,i)=>s+=`<div id="i1_${i}" style="position:absolute;left:${30+rnd(i)*500}px;top:${160+rnd(i+5)*430}px;font-size:${44+rnd(i+2)*24}px;transform:rotate(${rnd(i+7)*80-40}deg)">${e}</div>`);$('it1').innerHTML=s;
 const K=['🧳','🎒','📦','👟','🎸','🛏️'];let k='';K.forEach((e,i)=>k+=`<div id="k3_${i}" style="position:absolute;font-size:60px">${e}</div>`);$('sk3').innerHTML=k;})();
'''
RENDER='''
 {$('pr1').textContent=Math.round(eo(seg(t,0.5,2.6))*3)+'%';for(let i=0;i<12;i++){$('i1_'+i).style.marginTop=(Math.sin(t*3+i)*6)+'px';}
  place('a',300,690,1.0,false);pose('a',t>=2.32?{aL:60,aR:-60,hd:Math.sin(t*10)*8,open:1}:{aL:8,aR:-30,hd:-8});}
 {place('b',140,690,.9,false);pose('b',{aL:8,aR:-150+Math.sin(t*14)*25,open:1});place('c',460,690,.9,true);pose('c',t>=4.56?{aL:8,aR:-150+Math.sin(t*14)*25,hd:-6}:{aL:8,aR:-8});
  const d=eo(seg(t,3.9,5.0));$('tr2').style.left=lerp(380,700,d)+'px';$('ch_b').style.opacity=1-seg(t,3.86,4.0);$('st2').textContent=t<3.86?'посадка':'🚆 отправился';$('st2').style.color=t<3.86?'#30d158':'#ff9f0a';}
 {place('d',300,690,1.15,false);const g=t>=6.58;pose('d',g?{aL:8,aR:-100,hd:-6,open:0}:{aL:8,aR:-60});
  for(let i=0;i<6;i++){const k=eo(seg(t,6.0+i*.06,6.55+i*.06));const a=i*1.05;const x0=300+Math.cos(a)*220,y0=420+Math.sin(a)*170;$('k3_'+i).style.left=lerp(x0,400,k)+'px';$('k3_'+i).style.top=lerp(y0,330,k)+'px';$('k3_'+i).style.transform=`scale(${1-k*.95})`;}
  $('kg3').textContent=(t<6.58?23:0)+' кг';$('ok3').style.opacity=seg(t,6.6,6.7);}
 {const r=eo(seg(t,7.0,9.1));place('e',lerp(140,420,r),690,1.0,false);pose('e',t>=8.0?run(t,14):{aL:8,aR:-8});
  $('fl4').style.left=(lerp(140,420,r)-110)+'px';$('fl4').style.top=(t>=7.7?370:500)+'px';$('fl4').style.opacity=seg(t,7.04,7.2);$('sp4').style.opacity=seg(t,8.0,8.1);}
 {const m=eo(seg(t,10.1,12.2));$('tp5').textContent=Math.round(lerp(20,1400,m))+'°C';$('hr5').style.transform=`scaleY(${1-m*.6}) scaleX(${1+m*.4})`;$('hr5').style.filter=`drop-shadow(0 0 ${m*40}px #ff6a00)`;
  place('f',150,690,1.0,false);pose('f',t>=11.12?{aL:60,aR:-60,hd:12,open:1}:{aL:8,aR:-8});}
'''
