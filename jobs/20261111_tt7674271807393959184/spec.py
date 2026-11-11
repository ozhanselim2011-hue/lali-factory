DUR=15.0
FADE=14.6
START=0
SONG='VITA CHIKOVANI — Керосин'
BG='linear-gradient(180deg,#140806,#050202)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Я",0.0],["больше",0.14],["не",0.44],["плачу,",0.7],["а",1.36],["ты?",2.0]],
 [["не",2.58],["ищи",2.98],["огонь",3.46],["в",4.04],["глазах,",4.14]],
 [["который",5.12],["ты",5.8],["сам",6.16],["погасил",6.56]],
 [["пусть",7.84],["любовь",8.62],["горит",9.0],["дотла,",9.6]],
 [["я",10.6],["подливаю",11.18],["керосин",12.38]],
 [["не",13.12],["ищи",13.88],["огонь",14.38]],
]
SC=[[-0.3,2.5],[2.5,5.05],[5.05,7.78],[7.78,10.5],[10.5,13.05],[13.05,99]]
GLOW=['#1a2a5a','#7a3a0a','#3a3a3a','#7a2a0a','#7a5a0a','#7a1f0a']
PEMO=['😌','🔍','🧯','🔥','⛽','🚫']
END=[14.6,15.0]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#000">
 <div class="hdr">Чат · Он 🤡</div>
 <div id="m1a" style="position:absolute;right:24px;top:90px;background:#ff2d78;border-radius:22px;padding:12px 18px;font-size:30px;font-weight:800;opacity:0">я больше не плачу 💅</div>
 <div id="m1b" style="position:absolute;right:24px;top:170px;background:#ff2d78;border-radius:22px;padding:12px 18px;font-size:30px;font-weight:800;opacity:0">а ты? 😏</div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#1c1c1e">
 <div class="hdr">Поиск</div>
 <div style="position:absolute;left:24px;right:24px;top:70px;background:#2c2c2e;border-radius:16px;padding:14px 18px;font-size:26px;font-weight:700">🔍 <span id="q2"></span></div>
 <div id="nf2" class="c" style="top:200px;font-size:30px;font-weight:900;color:#8e8e93;opacity:0">огонь в её глазах: 0 результатов</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:linear-gradient(180deg,#2a2a2e,#111)">
 <div class="hdr">История</div>
 <div id="fi3" style="position:absolute;left:330px;top:200px;font-size:140px;z-index:3">🔥</div>
 <div id="sm3" style="position:absolute;inset:0;z-index:4"></div>
 <div class="ch" data-p="c"></div><div id="ex3" style="position:absolute;left:220px;top:420px;font-size:70px;z-index:6">🧯</div>
 <div id="lb3" class="c" style="top:60px;font-size:28px;font-weight:900;color:#ff453a;opacity:0;z-index:7">потушил сам 🤡</div>
</div>
<div class="card" id="c4" style="background:radial-gradient(circle at 50% 70%,#7a1a00,#140400)">
 <div class="c" style="top:200px;font-size:150px;z-index:3">💔</div>
 <div id="fl4" style="position:absolute;inset:0;z-index:4"></div>
 <div class="c mono" id="tp4" style="top:60px;font-size:50px;font-weight:900;color:#ff9f0a;z-index:6">100°</div>
</div>
<div class="card" id="c5" style="background:radial-gradient(circle at 50% 70%,#7a2a00,#140400)">
 <div class="c" style="top:150px;font-size:120px;z-index:3" id="fr5">🔥</div>
 <div id="dr5" style="position:absolute;inset:0;z-index:4"></div>
 <div class="ch" data-p="d"></div>
 <div id="cn5" style="position:absolute;left:380px;top:330px;font-size:80px;z-index:6;transform:rotate(-60deg)">⛽</div>
</div>
<div class="card" id="c6" style="background:#000">
 <div class="c" style="top:150px;font-size:160px">🔥</div>
 <div id="no6" style="position:absolute;left:150px;top:140px;width:300px;height:300px;border:24px solid #ff453a;border-radius:50%;opacity:0;z-index:6"><div style="position:absolute;left:-20px;top:126px;width:300px;height:24px;background:#ff453a;transform:rotate(-45deg)"></div></div>
 <div class="ch" data-p="e"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=p=='c'?CH(p,'#8e8e93','#c8c8cc','#8e8e93'):CH(p,'#ff8ac4','#ffffff','#ffd6e8');});
 let s='';for(let i=0;i<12;i++)s+=`<div id="k3_${i}" style="position:absolute;width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,.8);opacity:0"></div>`;$('sm3').innerHTML=s;
 let f='';for(let i=0;i<16;i++)f+=`<div id="f4_${i}" style="position:absolute;font-size:${40+rnd(i)*40}px">🔥</div>`;$('fl4').innerHTML=f;
 let d='';for(let i=0;i<10;i++)d+=`<div id="d5_${i}" style="position:absolute;width:10px;height:22px;border-radius:5px;background:#c9a227"></div>`;$('dr5').innerHTML=d;})();
'''
RENDER='''
 {$('m1a').style.opacity=seg(t,0.1,0.2);$('m1b').style.opacity=seg(t,1.36,1.46);$('m1b').style.transform=`scale(${1+.2*pop(t,2.0,6)})`;place('a',300,700,1.05,false);pose('a',t>=0.7?{aL:8,aR:-120,hd:-10}:{aL:8,aR:-8});}
 {const q='огонь в её глазах';$('q2').textContent=q.slice(0,Math.round(q.length*seg(t,2.6,4.1)));$('nf2').style.opacity=seg(t,4.14,4.25);place('b',300,700,1.0,false);pose('b',{aL:8,aR:-8,hd:-12});}
 {const k=seg(t,6.16,6.9);$('fi3').style.opacity=1-k;$('fi3').style.transform=`scale(${1-k*.6})`;$('lb3').style.opacity=seg(t,6.56,6.66);
  for(let i=0;i<12;i++){const ph=(t*2+i/12)%1;const e=$('k3_'+i);e.style.opacity=t>=5.8?(1-ph):0;e.style.left=(280+ph*130)+'px';e.style.top=(440-ph*160+Math.sin(i)*20)+'px';e.style.transform=`scale(${1+ph*2})`;}
  place('c',160,700,1.0,false);pose('c',{aL:8,aR:-90,hd:-6});}
 {const k=seg(t,8.6,10.4);$('tp4').textContent=Math.round(lerp(100,3000,k))+'°';for(let i=0;i<16;i++){const ph=(t*.9+rnd(i))%1;const e=$('f4_'+i);e.style.left=(rnd(i+5)*560)+'px';e.style.top=(620-ph*500*(.4+k))+'px';e.style.opacity=(1-ph)*(.4+k*.6);}}
 {const p=t>=11.18;$('cn5').style.transform=`rotate(${p?-110:-60}deg)`;$('fr5').style.transform=`scale(${1+seg(t,11.2,13.0)*1.2+.08*Math.sin(t*12)})`;
  for(let i=0;i<10;i++){const ph=(t*2.5+i/10)%1;const e=$('d5_'+i);e.style.opacity=p?1:0;e.style.left=(380-ph*90)+'px';e.style.top=(330+ph*60)+'px';}
  place('d',470,700,.95,true);pose('d',{aL:8,aR:-100,hd:-6,open:t>=12.38?1:0});}
 {$('no6').style.opacity=seg(t,13.88,13.98);$('no6').style.transform=`scale(${eb(seg(t,13.88,14.2))})`;place('e',300,700,1.0,false);pose('e',t>=13.12?{aL:8,aR:-150,hd:-6}:{aL:8,aR:-8});}
'''
