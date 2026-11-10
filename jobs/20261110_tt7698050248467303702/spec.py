DUR=21.2
FADE=20.8
START=0
SONG='Катрин Штоль — Пьяный'
BG='linear-gradient(180deg,#140a14,#050306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Красивый",0.0],["и",0.66],["пьяный,",0.7],["аромат",1.86],["этот",3.36],["пряный",3.6]],
 [["я",4.58],["запишу",5.52],["на",6.38],["диктофон,",6.6],["диктофон",8.1]],
 [["пьяный,",9.46],["такой",10.76],["красивый",11.68],["и",12.4],["пьяный",12.58]],
 [["аромат",13.52],["этот",15.22],["пряный",15.42]],
 [["и",16.46],["этот",17.56],["сладкий",17.82],["баритон,",18.52],["баритон",19.8]],
]
SC=[[-0.3,4.5],[4.5,9.4],[9.4,13.45],[13.45,16.4],[16.4,99]]
GLOW=['#7a1f4a','#1a4a7a','#5a1d7a','#7a5a1a','#7a1f4a']
PEMO=['✨','🎙️','🥴','🌶️','🍬']
END=[20.8,21.2]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#000">
 <div class="hdr">Камера · фильтр «Красивый»</div>
 <div style="position:absolute;left:30px;right:30px;top:70px;height:520px;border-radius:30px;background:linear-gradient(180deg,#3a1a3a,#1a0a1a);overflow:hidden" id="fr1"></div>
 <div class="ch" data-p="a"></div>
 <div id="tg1" style="position:absolute;left:60px;top:100px;background:#ff2d78;border-radius:14px;padding:6px 14px;font-size:24px;font-weight:900;opacity:0;z-index:7">✨ красивый 100%</div>
 <div id="ar1" style="position:absolute;inset:0;z-index:6"></div>
</div>
<div class="card" id="c2" style="background:#1c1c1e">
 <div class="hdr" style="color:#ff453a">● Диктофон</div><div class="ttl" style="font-size:34px">Новая запись: его голос 💖</div>
 <div id="wv2" style="position:absolute;left:30px;right:30px;top:200px;height:200px;display:flex;align-items:center;gap:4px"></div>
 <div class="c mono" id="tm2" style="top:430px;font-size:54px;font-weight:900">00:00</div>
 <div id="sv2" class="c" style="top:510px;font-size:24px;font-weight:800;color:#30d158;opacity:0">💾 сохранено ×2 (на всякий)</div>
</div>
<div class="card" id="c3" style="background:radial-gradient(circle at 50% 40%,#5a1a4a,#14020c)">
 <div style="position:absolute;left:24px;right:24px;top:24px;background:rgba(0,0,0,.4);border-radius:20px;padding:12px 16px;font-size:22px;font-weight:800;z-index:6">🧪 Анализ: алкоголь <span style="color:#30d158">0%</span> · любовь <span id="lv3" style="color:#ff2d78">0%</span></div>
 <div class="ch" data-p="b"></div>
 <div id="hr3" style="position:absolute;inset:0;z-index:6"></div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#3a2410,#140a04)">
 <div class="hdr" style="color:#ffb340">Парфюм</div>
 <div style="position:absolute;left:80px;top:180px;width:160px;height:220px;border-radius:30px 30px 40px 40px;background:linear-gradient(180deg,#ffb340,#a85a10);display:flex;align-items:center;justify-content:center;text-align:center;font-size:24px;font-weight:900;color:#3a1a00">Пряный<br>№5</div>
 <div style="position:absolute;left:135px;top:140px;width:50px;height:44px;background:#d4a017;border-radius:8px"></div>
 <div id="mt4" style="position:absolute;inset:0;z-index:4"></div>
 <div class="ch" data-p="c"></div>
 <div id="sn4" style="position:absolute;left:300px;top:110px;background:#fff;color:#111;border-radius:18px;padding:8px 14px;font-size:24px;font-weight:900;opacity:0;z-index:7">🌶️ корица · 🍂 гвоздика · 💖 он</div>
</div>
<div class="card" id="c5" style="background:#111214">
 <div class="hdr">Анализ голоса</div>
 <div id="eq5" style="position:absolute;left:30px;right:30px;top:90px;height:180px;display:flex;align-items:flex-end;gap:6px"></div>
 <div style="position:absolute;left:30px;right:30px;top:300px;font-size:26px;font-weight:800;line-height:1.8"><div>тембр: <span style="color:#64d2ff">баритон</span></div><div>сладость: <span id="sw5" class="mono" style="color:#ff2d78">0%</span> 🍬</div></div>
 <div class="ch" data-p="d"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=p=='c'?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 let a='';for(let i=0;i<6;i++)a+=`<div id="a1_${i}" style="position:absolute;font-size:34px;opacity:0">${['〰️','🌶️','🍂'][i%3]}</div>`;$('ar1').innerHTML=a;
 let w='';for(let i=0;i<36;i++)w+=`<div id="w2_${i}" style="flex:1;border-radius:3px;background:#ff453a;height:6px"></div>`;$('wv2').innerHTML=w;
 let h='';for(let i=0;i<8;i++)h+=`<div id="h3_${i}" style="position:absolute;font-size:34px">💖</div>`;$('hr3').innerHTML=h;
 let m='';for(let i=0;i<10;i++)m+=`<div id="m4_${i}" style="position:absolute;width:40px;height:40px;border-radius:50%;background:rgba(255,200,120,.35);opacity:0"></div>`;$('mt4').innerHTML=m;
 let e='';for(let i=0;i<20;i++)e+=`<div id="e5_${i}" style="flex:1;border-radius:4px 4px 0 0;background:linear-gradient(0deg,#64d2ff,#ff2d78);height:10px"></div>`;$('eq5').innerHTML=e;})();
'''
RENDER='''
 {place('a',300,620,1.15,false);pose('a',t>=0.7?{aL:8,aR:-60,hd:-8}:{aL:8,aR:-8});$('tg1').style.opacity=seg(t,0.0,0.15);$('ch_a').style.filter=`drop-shadow(0 0 ${20+10*Math.sin(t*4)}px #ff8ac4)`;
  for(let i=0;i<6;i++){const ph=(t*.6+i/6)%1;const e=$('a1_'+i);e.style.opacity=t>=1.86?Math.sin(ph*Math.PI):0;e.style.left=(420+Math.sin(ph*6+i)*30)+'px';e.style.top=(450-ph*300)+'px';}}
 {const rec=t>=5.52;for(let i=0;i<36;i++){$('w2_'+i).style.height=(rec?10+Math.abs(Math.sin(t*9+i*.7))*150*(.4+.6*rnd(i)):6)+'px';}
  const s=rec?Math.floor(t-5.52):0;$('tm2').textContent='00:0'+Math.min(9,s);$('sv2').style.opacity=seg(t,8.1,8.2);}
 {const l=Math.round(eo(seg(t,10.76,12.6))*100);$('lv3').textContent=l+'%';place('b',300,690,1.1,false,Math.sin(t*3)*10);pose('b',{aL:30+Math.sin(t*3)*20,aR:-30+Math.sin(t*3)*20,hd:Math.sin(t*3)*12,open:1});
  for(let i=0;i<8;i++){const a=t*2+i*Math.PI/4;$('h3_'+i).style.left=(285+Math.cos(a)*90)+'px';$('h3_'+i).style.top=(330+Math.sin(a)*30)+'px';}}
 {const sp=t>=13.52;for(let i=0;i<10;i++){const ph=(t*.7+i/10)%1;const e=$('m4_'+i);e.style.opacity=sp?(1-ph):0;e.style.left=(240+ph*200)+'px';e.style.top=(220+Math.sin(ph*6+i)*30-ph*40)+'px';e.style.transform=`scale(${1+ph*2})`;}
  place('c',460,690,1.0,true);pose('c',t>=15.22?{aL:8,aR:-8,hd:-14,open:1}:{aL:8,aR:-8});$('sn4').style.opacity=seg(t,15.42,15.55);}
 {const on=t>=17.56;for(let i=0;i<20;i++){$('e5_'+i).style.height=(on?20+Math.abs(Math.sin(t*6+i*.5))*150*(i<8?1:.5):10)+'px';}$('sw5').textContent=Math.round(eo(seg(t,17.82,19.8))*200)+'%';
  place('d',300,700,.9,false);pose('d',t>=18.52?{aL:60,aR:-60,hd:-10,open:1}:{aL:8,aR:-8});}
'''
