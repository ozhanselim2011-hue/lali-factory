DUR=21.8
FADE=21.4
START=0
SONG='тима ищет свет — волна'
BG='linear-gradient(180deg,#06101a,#020306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Прошу,",0.0],["моя",0.8],["маленькая,",1.2],["не",2.36],["беги",2.7],["так",3.18],["далече",3.46]],
 [["ты",4.34],["знаешь,",4.54],["место",5.16],["не",5.6],["сыщешь",5.86],["себе",6.66]],
 [["среди",6.96],["всех",7.58],["этих",7.78],["пьяных",8.2],["встреч",9.18]],
 [["я",9.52],["буду",9.86],["беречь",10.18],["тебя,",11.14],["чаще",11.56],["буду",12.12],["беречь",12.52],["тебя",13.52]],
 [["дольше",13.72],["думай",14.5],["лишь",15.14],["о",15.42],["настоящем",15.78]],
 [["и",17.08],["не",17.22],["пытайся",17.42],["о",18.5],["прошлом",18.64]],
 [["а",19.3],["за",19.34],["городом",19.44],["море",20.32],["и",21.0],["камни",21.0]],
]
SC=[[-0.3,4.28],[4.28,6.9],[6.9,9.46],[9.46,13.66],[13.66,17.0],[17.0,19.24],[19.24,99]]
GLOW=['#1a4a7a','#3a3a5a','#5a1d7a','#7a1f4a','#1a5c4e','#3a3a3a','#1a5a7a']
PEMO=['🏃','🗺️','🥂','🫶','⏳','🗑️','🌊']
END=[21.4,21.8]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#d8e6d0">
 <svg width="600" height="690" style="position:absolute"><path d="M0 220 L600 280 M0 480 L600 400 M170 0 L230 690 M430 0 L390 690" stroke="#fff" stroke-width="18"/></svg>
 <div id="hp1" style="position:absolute;font-size:56px;z-index:6">📍</div>
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#fff;color:#111;border-radius:22px;padding:12px 18px;font-size:24px;font-weight:800;z-index:7">📍 Она удаляется: <span id="km1" class="mono" style="color:#ff453a">0 км</span></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#1c1c1e">
 <div class="hdr">Поиск места</div>
 <div style="position:absolute;left:24px;right:24px;top:70px;background:#2c2c2e;border-radius:16px;padding:14px 18px;font-size:24px;font-weight:700">🔍 где мне хорошо?</div>
 <div id="nr2" class="c" style="top:190px;font-size:28px;font-weight:900;color:#8e8e93;opacity:0">ничего не найдено 🤷</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:linear-gradient(180deg,#2a0a3a,#0a0214)">
 <div id="ps3" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="c"></div>
 <div class="c" style="top:60px;font-size:28px;font-weight:900;color:#bf5af2">вечеринка №47 😵‍💫</div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#ffd6e8,#ff9ac1)">
 <div id="sh4" style="position:absolute;left:150px;top:180px;width:300px;height:420px;border-radius:150px 150px 40px 40px;border:10px solid #64d2ff;opacity:0;z-index:6"></div>
 <div class="ch" data-p="d"></div><div class="ch" data-p="e"></div>
 <div class="c" id="tx4" style="top:60px;font-size:30px;font-weight:900;color:#ff2d78;opacity:0">🛡️ режим «беречь»: ВКЛ</div>
</div>
<div class="card" id="c5" style="background:#111214">
 <div class="hdr">Мысли</div>
 <div style="position:absolute;left:40px;right:40px;top:100px;height:26px;border-radius:13px;background:#2c2c2e;overflow:hidden"><div id="nw5" style="height:26px;background:#30d158;width:0"></div></div>
 <div class="c" style="top:140px;font-size:26px;font-weight:900;color:#30d158">о настоящем</div>
 <div class="ch" data-p="f"></div><div id="cl5" style="position:absolute;left:380px;top:350px;font-size:80px">⏳</div>
</div>
<div class="card" id="c6" style="background:#e8e8ec;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Корзина</div>
 <div id="pf6" style="position:absolute;left:80px;top:120px;width:160px;height:120px;border-radius:12px;background:#8e8e93;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:900;color:#fff">📁 прошлое</div>
 <div style="position:absolute;left:360px;top:300px;font-size:150px">🗑️</div>
 <div class="ch" data-p="g"></div>
</div>
<div class="card" id="c7" style="background:linear-gradient(180deg,#87ceeb,#bfe3ff 45%,#1a6aa8 46%,#0a3a68)">
 <div id="wv7" style="position:absolute;left:0;right:0;top:300px;height:80px"></div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:140px;background:#8a8a8a;border-radius:40% 60% 0 0"></div>
 <div class="ch" data-p="h"></div><div class="ch" data-p="i"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML='ei'.includes(p)?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 let p='';for(let i=0;i<12;i++)p+=`<div id="p3_${i}" style="position:absolute;font-size:${40+rnd(i)*30}px">${['🥂','🍾','🪩','🎉'][i%4]}</div>`;$('ps3').innerHTML=p;
 let w='';for(let i=0;i<8;i++)w+=`<div id="w7_${i}" style="position:absolute;font-size:50px">🌊</div>`;$('wv7').innerHTML=w;})();
'''
RENDER='''
 {const k=eo(seg(t,2.4,4.2));$('hp1').style.left=lerp(330,520,k)+'px';$('hp1').style.top=lerp(300,80,k)+'px';$('km1').textContent=Math.round(k*900)+' км';place('a',180,700,.9,false);pose('a',{aL:8,aR:-150+Math.sin(t*10)*20,open:1});}
 {$('nr2').style.opacity=seg(t,6.66,6.76);place('b',300,700,1.0,false);pose('b',{aL:8,aR:-8,hd:Math.sin(t*4)*14});}
 {for(let i=0;i<12;i++){const e=$('p3_'+i);e.style.left=(rnd(i)*540)+'px';e.style.top=(120+rnd(i+3)*380+Math.sin(t*4+i)*20)+'px';}place('c',300,700,1.0,false,Math.sin(t*3)*10);pose('c',{aL:40,aR:-40,hd:Math.sin(t*3)*14});}
 {const on=t>=10.18;$('sh4').style.opacity=on?.6+.3*Math.sin(t*6):0;$('tx4').style.opacity=seg(t,10.18,10.3);place('d',250,690,1.0,false);place('e',350,690,1.0,true);pose('d',{aL:8,aR:-100,hd:-8});pose('e',{aL:8,aR:-60,hd:-8});}
 {const k=eo(seg(t,14.5,16.5));$('nw5').style.width=(k*100)+'%';$('cl5').style.transform=`rotate(${t*180}deg)`;place('f',200,700,1.0,false);pose('f',{aL:8,aR:-150,hd:-6});}
 {const k=eo(seg(t,17.42,18.9));$('pf6').style.left=lerp(80,400,k)+'px';$('pf6').style.top=lerp(120,330,k)+'px';$('pf6').style.transform=`scale(${1-k*.6}) rotate(${k*40}deg)`;$('pf6').style.opacity=1-seg(t,18.7,19.0);
  place('g',180,700,1.0,false);pose('g',{aL:8,aR:-100,hd:-6});}
 {for(let i=0;i<8;i++){$('w7_'+i).style.left=(((i*90+t*60)%720)-60)+'px';$('w7_'+i).style.top=(Math.sin(t*2+i)*14)+'px';}place('h',250,640,.8,false);place('i',350,640,.8,true);pose('h',{aL:8,aR:-60,hd:-6});pose('i',{aL:8,aR:-60,hd:-6});}
'''
