DUR=18.9
FADE=18.5
START=0
SONG='Люся Чеботина — ГОРГОНА'
BG='linear-gradient(180deg,#0a140a,#030503)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Я",0.0],["ГОРГОНА,",0.24],["я",1.08],["ГОРГОНА",1.3]],
 [["да",2.1],["ты",2.5],["не",2.72],["первый,",3.04],["знай",3.6]],
 [["не",3.98],["тот",4.54],["последний,",4.82],["кто",5.7],["готов",5.86],["был",6.92],["всё",7.22],["отдать",7.44]],
 [["и",8.32],["быть",8.62],["у",8.94],["моих",9.2],["ног",9.84]],
 [["да",10.1],["ты",10.7],["не",11.0],["первый,",11.26],["знай,",11.8],["не",12.38],["тот",12.8],["последний,",13.06],["кто",13.88]],
 [["рискует",15.04],["пострадать",15.68]],
 [["Я",16.32],["ГОРГОНА,",16.56],["я",17.48],["ГОРГОНА",17.7]],
]
SC=[[-0.3,2.05],[2.05,3.92],[3.92,8.26],[8.26,10.05],[10.05,14.98],[14.98,16.26],[16.26,99]]
GLOW=['#1a5c2e','#3a3a5a','#7a5a1a','#7a1f4a','#4a4a4a','#3a3a3a','#1a5c2e']
PEMO=['🐍','🎫','💸','👑','🗿','⚠️','🐍']
END=[18.5,18.9]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:radial-gradient(circle at 50% 40%,#1a5a2a,#051208)">
 <div id="sn1" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#1c1c1e">
 <div class="hdr">Электронная очередь · к ней</div>
 <div style="position:absolute;left:150px;top:120px;width:300px;height:200px;border-radius:20px;background:#fff;color:#111;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:24px;font-weight:800;color:#8e8e93">ваш номер</div><div id="nm2" class="mono" style="font-size:90px;font-weight:900">№1</div></div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Предложения ей</div>
 <div id="of3" style="position:absolute;left:24px;right:24px;top:80px"></div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#3a1a3a,#140814)">
 <div style="position:absolute;left:200px;top:330px;width:200px;height:90px;background:#c9a227;border-radius:10px 10px 0 0;z-index:3"></div>
 <div class="ch" data-p="q"></div>
 <div class="ch" data-p="c"></div><div class="ch" data-p="d"></div><div class="ch" data-p="e"></div>
 <div id="cr4" style="position:absolute;left:265px;top:30px;font-size:70px;z-index:6">👑</div>
</div>
<div class="card" id="c5" style="background:#e8e2d8;color:#2a1f10">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Её коллекция · зал славы</div>
 <div class="ch" data-p="f"></div><div class="ch" data-p="g"></div><div class="ch" data-p="h"></div>
 <div id="pl5" style="position:absolute;left:0;right:0;top:600px;display:flex;justify-content:space-around;font-size:18px;font-weight:900"><span>экс №1</span><span>экс №2</span><span>экс №3</span></div>
</div>
<div class="card" id="c6" style="background:#2a2a2e">
 <div id="wr6" style="position:absolute;left:24px;right:24px;top:24px;background:#ffd60a;color:#111;border-radius:16px;padding:10px 14px;font-size:24px;font-weight:900;z-index:7">⚠️ ОСТОРОЖНО: окаменение</div>
 <div class="ch" data-p="i"></div>
</div>
<div class="card" id="c7" style="background:radial-gradient(circle at 50% 40%,#2a8a3a,#051208)">
 <div id="fl7" style="position:absolute;inset:0;background:#c8ffd0;opacity:0;z-index:7"></div>
 <div id="sn7" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="j"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML='aqj'.includes(p)?CH(p,'#30d158','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 const S=(id)=>{let s='';for(let i=0;i<7;i++)s+=`<div id="${id}_${i}" style="position:absolute;font-size:46px">🐍</div>`;$(id).innerHTML=s;};S('sn1');S('sn7');
 $('of3').innerHTML=['🚗 машина','🏠 квартира','💍 кольцо','💖 сердце'].map((s,i)=>`<div id="o3_${i}" style="display:flex;justify-content:space-between;background:#fff;border-radius:16px;padding:12px 16px;margin-bottom:10px;font-size:26px;font-weight:800;opacity:0">${s}<span style="color:#ff453a">❌ мало</span></div>`).join('');})();
'''
RENDER='''
 {for(let i=0;i<7;i++){const a=-Math.PI*(.15+i*.12);const e=$('sn1_'+i);e.style.left=(275+Math.cos(a)*90)+'px';e.style.top=(380+Math.sin(a)*90+Math.sin(t*8+i)*8)+'px';e.style.transform=`rotate(${Math.sin(t*6+i)*20}deg)`;}
  place('a',300,700,1.1,false);pose('a',{aL:60,aR:-150,hd:-8,open:t>=1.3?1:0});}
 {$('nm2').textContent='№'+Math.max(1,Math.round(eo(seg(t,2.2,3.6))*47));place('b',300,700,.9,false);pose('b',{aL:8,aR:-8,hd:12});}
 {for(let i=0;i<4;i++)$('o3_'+i).style.opacity=seg(t,4.5+i*.8,4.6+i*.8);}
 {place('q',300,340,.9,true);pose('q',{aL:60,aR:-150,hd:-8});[['c',120],['d',300],['e',480]].forEach(([p,x],i)=>{place(p,x,700,.75,i==2);pose(p,{aL:150,aR:-150,hd:-14,bob:12});});}
 {[['f',110],['g',300],['h',490]].forEach(([p,x],i)=>{place(p,x,580,.85,false);pose(p,{aL:[60,8,150][i],aR:[-60,-150,-150][i],open:1});$('ch_'+p).style.filter=t>=10.1+i*.6?'grayscale(1) brightness(.9) contrast(.8)':'none';});}
 {const k=seg(t,15.04,16.0);place('i',300,700,1.1,false);pose('i',{aL:60,aR:-60,open:1,hd:k*8});$('ch_i').style.filter=`grayscale(${k}) brightness(${1-k*.15})`;$('wr6').style.transform=`scale(${1+.1*Math.abs(Math.sin(t*10))})`;}
 {for(let i=0;i<7;i++){const a=-Math.PI*(.15+i*.12);const e=$('sn7_'+i);e.style.left=(275+Math.cos(a)*100)+'px';e.style.top=(360+Math.sin(a)*100+Math.sin(t*8+i)*10)+'px';e.style.transform=`rotate(${Math.sin(t*6+i)*25}deg)`;}
  $('fl7').style.opacity=.7*pop(t,16.56,8)+.7*pop(t,17.7,8);place('j',300,700,1.15,false);pose('j',{aL:150,aR:-150,open:1});}
'''
