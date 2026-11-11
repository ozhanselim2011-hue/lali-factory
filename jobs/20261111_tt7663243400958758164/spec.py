DUR=19.6
FADE=19.2
START=0
SONG="Akmal' — Любовная"
BG='linear-gradient(180deg,#140a10,#050304)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Мы",0.0],["закрывали",0.18],["двери,",1.12],["чтобы",1.64],["вновь",2.08],["их",2.72],["открыть",2.78]],
 [["падай",3.62],["в",3.98],["мои",4.12],["объятья,",4.28],["нам",5.66],["так",6.12],["лучше",6.68]],
 [["…двоим",10.0],["не",10.5],["скучно",10.74]],
 [["и",11.78],["ты",12.2],["в",12.42],["своём",12.52],["платье",13.0],["мне",13.62],["голову",14.16],["кружишь",14.98]],
 [["я",15.84],["даже",16.2],["не",16.64],["знал,",16.86],["что",17.46],["стану",17.66],["твоим",18.26],["мужем",19.04]],
]
SC=[[-0.3,3.55],[3.55,9.9],[9.9,11.7],[11.7,15.78],[15.78,99]]
GLOW=['#5a3a1a','#7a1f4a','#7a6a1a','#5a1d7a','#7a5a1a']
PEMO=['🚪','🫂','🎲','👗','💍']
END=[19.2,19.6]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#2a2a2e">
 <div style="position:absolute;left:200px;top:120px;width:200px;height:420px;background:#fff7c2"></div>
 <div id="dr1" style="position:absolute;left:200px;top:120px;width:200px;height:420px;background:#5a3a1a;border:8px solid #3a2410;transform-origin:left center;z-index:3"><div style="position:absolute;right:16px;top:200px;width:18px;height:18px;border-radius:50%;background:#ffd60a"></div></div>
 <div id="hr1" class="c" style="top:260px;font-size:110px;opacity:0;z-index:2">💖</div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#ffd6e8,#ff9ac1)">
 <div class="ch" data-p="a"></div><div class="ch" data-p="b"></div>
 <div id="ok2" class="c" style="top:60px;font-size:34px;font-weight:900;color:#1f8a3a;opacity:0">✅ нам так лучше</div>
</div>
<div class="card" id="c3" style="background:#1c1c1e">
 <div class="hdr">Скука</div><div class="ttl mono" id="bd3" style="color:#30d158">100%</div>
 <div id="ic3" style="position:absolute;left:30px;right:30px;top:180px;display:grid;grid-template-columns:repeat(4,1fr);gap:10px"></div>
</div>
<div class="card" id="c4" style="background:radial-gradient(circle at 50% 40%,#5a1a4a,#14020c)">
 <div class="ch" data-p="c"></div><div class="ch" data-p="d"></div>
 <div id="sp4" style="position:absolute;left:150px;top:220px;font-size:50px;z-index:6">💫</div>
</div>
<div class="card" id="c5" style="background:#f4ecd8;color:#2a1f10">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Свидетельство о браке</div>
 <div style="position:absolute;left:40px;right:40px;top:80px;font-size:26px;font-weight:800;line-height:1.9">Муж: <u>Лали</u> 🧢<br>Жена: <u>она</u> 👰<br>Статус: <span id="st5" style="color:#d0021b"></span></div>
 <div id="sm5" style="position:absolute;left:300px;top:250px;border:6px solid #1f8a3a;color:#1f8a3a;border-radius:50%;width:150px;height:150px;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:900;transform:rotate(-12deg);opacity:0">ЗАГС ✓</div>
 <div class="ch" data-p="e"></div><div id="ex5" style="position:absolute;left:160px;top:340px;font-size:60px;opacity:0;z-index:6">😳</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML='bd'.includes(p)?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 $('ic3').innerHTML=['🎲','🎮','🍿','🎤','🛼','🎳','🎡','🃏'].map((e,i)=>`<div id="i3_${i}" style="height:110px;border-radius:16px;background:#2c2c2e;display:flex;align-items:center;justify-content:center;font-size:60px;opacity:.15">${e}</div>`).join('');})();
'''
RENDER='''
 {const cl=t<1.12?eo(seg(t,0.18,1.0)):1-eo(seg(t,2.2,2.9));$('dr1').style.transform=`perspective(600px) rotateY(${-(1-cl)*75}deg)`;$('hr1').style.opacity=seg(t,2.78,2.9);}
 {const f=seg(t,3.62,4.5);place('b',lerp(380,330,f),690,1.0,true,f*-35);pose('b',{aL:60,aR:-60,open:1});place('a',230,690,1.0,false);pose('a',t>=4.0?{aL:8,aR:-110,hd:6,open:1}:{aL:8,aR:-60});$('ok2').style.opacity=seg(t,6.68,6.8);}
 {const k=seg(t,10.0,10.9);$('bd3').textContent=Math.round(100*(1-k))+'%';$('bd3').style.color=k>.5?'#ff2d78':'#30d158';for(let i=0;i<8;i++){$('i3_'+i).style.opacity=t>=10.0+i*.08?1:.15;}}
 {place('d',380,690,1.0,true,Math.sin(t*6)*12);pose('d',{aL:120,aR:-120,open:1});place('c',200,690,1.0,false);pose('c',{aL:8,aR:-8,hd:Math.sin(t*10)*25,open:1});
  $('sp4').style.transform=`rotate(${t*400}deg)`;$('sp4').style.opacity=t>=14.16?1:0;}
 {const s='теперь МУЖ 😳';$('st5').textContent=s.slice(0,Math.round(s.length*seg(t,17.66,19.1)));$('sm5').style.opacity=seg(t,19.04,19.14);$('sm5').style.transform=`rotate(-12deg) scale(${1+.4*pop(t,19.04,8)})`;
  $('ex5').style.opacity=seg(t,16.86,16.96);place('e',190,700,1.0,false);pose('e',t>=16.86?{aL:60,aR:-60,open:1,hd:-6}:{aL:8,aR:-8});}
'''
