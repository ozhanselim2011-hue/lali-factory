DUR=19.1
FADE=18.7
START=0
SONG='HOLLYFLAME — Нежность'
BG='linear-gradient(180deg,#0a0a1a,#030306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Что",0.0],["же",0.22],["ты",0.38],["хочешь,",0.58],["скажи,",1.24],["а",2.06],["хочешь?",2.56]],
 [["я",3.62],["украду",4.04],["луну,",5.12],["подарю",5.68],["солнце",6.6]],
 [["буду",7.5],["тебя",8.5],["любить,",8.7],["как",9.58],["никто",9.84],["прежде",10.3]],
 [["прыгну",11.16],["или",12.32],["нырну",12.62],["в",13.3],["весну",13.52]],
 [["и,",14.12],["может,",14.52],["выучу",15.48],["наизусть",16.46],["всю",17.22],["твою",17.52],["нежность",18.26]],
]
SC=[[-0.3,3.56],[3.56,7.44],[7.44,11.1],[11.1,14.06],[14.06,99]]
GLOW=['#5a1d7a','#1a2a6a','#7a1f4a','#1a5c2e','#7a5a1a']
PEMO=['🎁','🌙','💖','🌸','📖']
END=[18.7,19.1]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Её вишлист</div>
 <div id="wl1" style="position:absolute;left:24px;right:24px;top:80px"></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#05082a,#3a2a6a 60%,#ff9a3d)">
 <div id="mn2" style="position:absolute;font-size:110px;z-index:3">🌙</div>
 <div id="sn2" style="position:absolute;font-size:120px;z-index:3;opacity:0">☀️</div>
 <div class="ch" data-p="b"></div><div class="ch" data-p="c"></div>
</div>
<div class="card" id="c3" style="background:#1c1c1e">
 <div class="hdr">Рейтинг любви</div>
 <div style="position:absolute;left:30px;right:30px;top:90px;font-size:26px;font-weight:800;line-height:2.1">
  <div>🤡 бывший №1 <span style="float:right;color:#8e8e93">12%</span></div>
  <div>🤡 бывший №2 <span style="float:right;color:#8e8e93">7%</span></div>
  <div style="color:#ff2d78">🧢 Лали <span id="lv3" class="mono" style="float:right">0%</span></div></div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#bfefff,#ffd6e8 60%,#7acb6a 61%,#4a9a3a)">
 <div id="fl4" style="position:absolute;inset:0;z-index:4"></div>
 <div class="ch" data-p="e"></div>
</div>
<div class="card" id="c5" style="background:#f4ecd8;color:#2a1f10">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Учебник «Её нежность» · 1000 стр.</div>
 <div style="position:absolute;left:60px;top:90px;width:480px;height:280px;background:#fff;border-radius:10px 24px 24px 10px;box-shadow:inset 18px 0 0 #e8dcc0;padding:20px 30px;font-size:22px;font-weight:700;line-height:1.7">§1 как она улыбается<br>§2 любимый чай 🍵<br>§3 когда ей грустно<br>§47 её смех 💖</div>
 <div class="c mono" id="pg5" style="top:390px;font-size:34px;font-weight:900;color:#ff2d78">выучено: 0%</div>
 <div class="ch" data-p="f"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=p=='c'?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 $('wl1').innerHTML=['🌙 луна','☀️ солнце','💖 вечная любовь'].map((s,i)=>`<div id="w1_${i}" style="background:#fff;border-radius:16px;padding:12px 16px;margin-bottom:10px;font-size:28px;font-weight:800;opacity:0">${s} <span style="float:right;color:#ff2d78">хочу</span></div>`).join('');
 let f='';for(let i=0;i<14;i++)f+=`<div id="f4_${i}" style="position:absolute;font-size:${30+rnd(i)*24}px;opacity:0">${i%2?'🌸':'🌷'}</div>`;$('fl4').innerHTML=f;})();
'''
RENDER='''
 {for(let i=0;i<3;i++)$('w1_'+i).style.opacity=seg(t,0.6+i*.7,0.7+i*.7);place('a',300,700,1.0,false);pose('a',t>=2.56?{aL:8,aR:-100,hd:12,open:1}:{aL:8,aR:-8,hd:-6});}
 {const k=eo(seg(t,4.04,5.1));$('mn2').style.left=lerp(420,170,k)+'px';$('mn2').style.top=lerp(60,330,k)+'px';$('sn2').style.opacity=seg(t,6.6,6.75);$('sn2').style.left='240px';$('sn2').style.top=lerp(600,140,eo(seg(t,5.7,6.8)))+'px';
  place('b',150,700,.9,false);place('c',450,700,.9,true);pose('b',{aL:8,aR:-120,hd:-8});pose('c',t>=6.6?{aL:120,aR:-120,open:1}:{aL:8,aR:-8});}
 {$('lv3').textContent=Math.round(eo(seg(t,8.7,10.3))*999)+'%';place('d',300,700,1.0,false);pose('d',t>=10.3?{aL:150,aR:-150,open:1}:{aL:8,aR:-60});}
 {const j=seg(t,11.16,12.4),d=seg(t,12.62,13.3);place('e',300,lerp(700,500,Math.sin(j*Math.PI))+d*120,1.0,false,d*170);pose('e',{aL:150,aR:-150,open:1});
  for(let i=0;i<14;i++){const e=$('f4_'+i);e.style.opacity=seg(t,13.52+i*.03,13.7+i*.03);e.style.left=(rnd(i)*560)+'px';e.style.top=(420+rnd(i+5)*230)+'px';e.style.transform=`scale(${eb(seg(t,13.52+i*.03,13.9+i*.03))})`;}}
 {$('pg5').textContent='выучено: '+Math.round(eo(seg(t,15.48,18.4))*100)+'%';place('f',470,700,.8,true);pose('f',{aL:8,aR:-110,hd:-10,open:t>=18.26?1:0});}
'''
