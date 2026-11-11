DUR=18.6
FADE=18.2
START=0
SONG='Егор Крид — Мало 2.0'
BG='linear-gradient(180deg,#140a14,#050306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Да",0.0],["мне",0.24],["так",0.4],["мало,",0.6],["мяу",0.94]],
 [["мне",2.1],["тебя",2.78],["мало",3.1]],
 [["ты",3.78],["мои",4.62],["деньги,",4.96],["деньги,",5.66],["деньги —",6.1],["всегда",6.36],["мало",6.74]],
 [["ты",7.32],["бы",8.34],["убил",8.54],["того,",9.18],["кого",9.52],["я",9.88],["целовала",10.24]],
 [["надел",11.4],["против",12.38],["меня",12.52],["жилет —",12.76],["я",13.34],["сквозь",13.44],["него",13.8],["попала",13.98]],
 [["мне",15.0],["тебя",15.72],["мало,",16.1],["мало,",16.7],["мало,",17.14],["мало,",17.62],["мало",18.06]],
]
SC=[[-0.3,2.05],[2.05,3.72],[3.72,7.26],[7.26,11.35],[11.35,14.95],[14.95,99]]
GLOW=['#7a1f4a','#5a1d7a','#1a5c2e','#7a1f1f','#7a5a1a','#7a1f4a']
PEMO=['😼','🔋','💸','😡','💘','🔁']
END=[18.2,18.6]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#000">
 <div class="hdr">Чат · она 😼</div>
 <div id="m1" style="position:absolute;left:24px;top:90px;background:#2c2c2e;border-radius:22px;padding:12px 18px;font-size:32px;font-weight:800;opacity:0">мне мало 🥺</div>
 <div id="m2" style="position:absolute;left:24px;top:170px;background:#2c2c2e;border-radius:22px;padding:12px 18px;font-size:44px;font-weight:900;opacity:0">мяу 😼</div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#1c1c1e">
 <div class="hdr">Тебя · уровень</div>
 <div style="position:absolute;left:150px;top:120px;width:280px;height:130px;border:8px solid #fff;border-radius:22px;padding:8px"><div id="bt2" style="height:100%;border-radius:12px;background:#ff453a;width:12%"></div></div>
 <div style="position:absolute;left:438px;top:160px;width:20px;height:50px;background:#fff;border-radius:6px"></div>
 <div class="c" style="top:280px;font-size:36px;font-weight:900;color:#ff453a">МАЛО ⚠️</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#0d1a12">
 <div class="hdr" style="color:#30d158">Её запросы</div><div class="ttl mono" id="bl3">1 000 000 ₽</div>
 <div id="cs3" style="position:absolute;inset:0;z-index:6"></div>
 <div id="ml3" class="c" style="top:200px;font-size:34px;font-weight:900;color:#ff453a;opacity:0">«всегда мало» 💅</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div class="hdr">Ревность</div>
 <div style="position:absolute;left:330px;top:90px;width:200px;height:240px;background:#fff;padding:10px 10px 40px;transform:rotate(6deg)"><div style="width:100%;height:100%;background:linear-gradient(135deg,#aaa,#666);display:flex;align-items:center;justify-content:center;font-size:110px">🤡</div></div>
 <div id="xx4" style="position:absolute;left:330px;top:90px;font-size:220px;color:#ff453a;opacity:0;line-height:1">✖</div>
 <div style="position:absolute;left:40px;top:120px;width:250px;height:24px;border-radius:12px;background:#2c2c2e;overflow:hidden"><div id="jl4" style="height:24px;background:#ff453a;width:0"></div></div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c5" style="background:radial-gradient(circle at 50% 40%,#5a3a1a,#140a02)">
 <div class="ch" data-p="e"></div>
 <div id="vs5" style="position:absolute;left:225px;top:400px;width:150px;height:170px;border-radius:30px 30px 20px 20px;background:#556b2f;border:6px solid #2e3b17;z-index:6;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:900;color:#e8e8c8">ЖИЛЕТ</div>
 <div id="ar5" style="position:absolute;top:430px;font-size:90px;z-index:7">💘</div>
</div>
<div class="card" id="c6" style="background:linear-gradient(180deg,#ff8ac4,#5e2cff)">
 <div class="c mono" id="ct6" style="top:60px;font-size:60px;font-weight:900">обнимашек: 0</div>
 <div class="c" style="top:140px;font-size:30px;font-weight:900">ещё! ещё! 🥺</div>
 <div class="ch" data-p="f"></div><div class="ch" data-p="g"></div>
 <div id="hs6" style="position:absolute;inset:0;z-index:6"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML='acdeg'.includes(p)?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 let c='';for(let i=0;i<12;i++)c+=`<div id="k3_${i}" style="position:absolute;font-size:44px">💸</div>`;$('cs3').innerHTML=c;
 let h='';for(let i=0;i<14;i++)h+=`<div id="h6_${i}" style="position:absolute;font-size:34px;opacity:0">💖</div>`;$('hs6').innerHTML=h;})();
'''
RENDER='''
 {$('m1').style.opacity=seg(t,0.4,0.5);$('m2').style.opacity=seg(t,0.94,1.04);$('m2').style.transform=`scale(${1+.3*pop(t,0.94,6)})`;place('a',300,700,1.0,false);pose('a',{aL:8,aR:-150,hd:-8,open:t>=0.94?1:0});}
 {$('bt2').style.width=(12+Math.sin(t*6)*2)+'%';place('b',300,700,1.0,false);pose('b',t>=3.1?{aL:40,aR:-40,hd:12,open:1}:{aL:8,aR:-8});}
 {const k=eo(seg(t,4.8,6.6));$('bl3').textContent=fmt(1000000*(1-k))+' ₽';$('bl3').style.color=k>.9?'#ff453a':'#fff';$('ml3').style.opacity=seg(t,6.74,6.84);
  for(let i=0;i<12;i++){const ph=(t*1.2+i/12)%1;const e=$('k3_'+i);e.style.opacity=t>=4.96?1-ph:0;e.style.left=(300+Math.cos(i)*ph*280)+'px';e.style.top=(450-ph*300)+'px';}
  place('c',300,700,1.0,false);pose('c',{aL:60,aR:-60,open:1});}
 {const j=eo(seg(t,8.5,10.5));$('jl4').style.width=(j*100)+'%';$('xx4').style.opacity=seg(t,10.24,10.34);place('d',150,700,1.0,false);pose('d',t>=8.54?{aL:30,aR:-30,hd:Math.sin(t*20)*6,open:1}:{aL:8,aR:-8});
  $('ch_d').style.filter=`drop-shadow(0 0 ${j*30}px #ff453a)`;}
 {const k=seg(t,13.3,14.4);$('ar5').style.left=lerp(-80,620,k)+'px';$('ar5').style.opacity=t>=13.3&&t<14.5?1:0;$('vs5').style.transform=`scale(${1+.15*pop(t,13.98,8)})`;
  place('e',300,700,1.0,false);pose('e',t>=13.98?{aL:60,aR:-60,open:1,hd:10}:{aL:8,aR:-8});}
 {const n=[16.1,16.7,17.14,17.62,18.06].filter(s=>t>=s).length;$('ct6').textContent='обнимашек: '+n*100;
  const k=eo(seg(t,15.0,15.7));place('f',lerp(150,250,k),700,1.0,false);place('g',lerp(450,350,k),700,1.0,true);pose('f',{aL:8,aR:-100,hd:-6});pose('g',{aL:8,aR:-100,hd:-6});
  for(let i=0;i<14;i++){const ph=(t*.8+i/14)%1;const e=$('h6_'+i);e.style.opacity=n?1-ph:0;e.style.left=(150+rnd(i)*300)+'px';e.style.top=(440-ph*300)+'px';}}
'''
