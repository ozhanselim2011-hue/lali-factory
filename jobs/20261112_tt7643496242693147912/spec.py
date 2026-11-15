DUR=10.4
FADE=10.0
START=3.2
SONG='MIA BOYKA — ЭКСПОНАТ'
BG='linear-gradient(180deg,#140a10,#050305)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Я",3.48],["экспонат,",4.04]],
 [["ты",4.98],["мой",5.16],["фанат,",5.42]],
 [["миллиард",6.1],["на",6.68],["тысячу",6.8],["карат",7.64]],
 [["носи",8.24],["меня",9.16],["на",9.52],["руках,",9.78]],
 [["я",10.72],["растаю",11.08],["в",11.68],["них,",11.76],["как",11.96],["шоколад",12.18]],
]
SC=[[2.9,4.9],[4.9,6.0],[6.0,8.1],[8.1,10.6],[10.6,99]]
GLOW=['#5a4a2a','#7a1f4a','#1d5a7a','#7a1f4a','#5a3a1a']
PEMO=['🖼️','📸','💎','🤲','🍫']
END=[13.2,13.6]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#e9e2d6,#cfc4b2);color:#2a1f10">
 <div class="hdr" style="color:#8a6a3a">Музей современного искусства</div>
 <div id="sp1" style="position:absolute;left:150px;top:0;width:300px;height:690px;background:linear-gradient(180deg,rgba(255,250,220,.9),rgba(255,250,220,0) 80%);clip-path:polygon(40% 0,60% 0,100% 100%,0 100%);opacity:0"></div>
 <div style="position:absolute;left:170px;top:480px;width:260px;height:160px;background:#fff;border:6px solid #ddd"></div>
 <div style="position:absolute;left:40px;right:40px;top:560px;height:8px;background:#b8001f;border-radius:4px"></div>
 <div class="ch" data-p="a"></div>
 <div id="pq1" style="position:absolute;left:40px;top:100px;background:#fff;border-radius:6px;padding:10px 14px;font-size:20px;font-weight:800;box-shadow:0 4px 10px rgba(0,0,0,.15);opacity:0">ЭКСПОНАТ №1<br><span style="color:#8a6a3a">«Лали». Бесценно.</span><br><span style="color:#d0021b">руками не трогать</span></div>
</div>
<div class="card" id="c2" style="background:#1c1c1e">
 <div class="ch" data-p="b"></div><div class="ch" data-p="x"></div>
 <div id="sg2" style="position:absolute;left:330px;top:150px;background:#fff;color:#ff2d78;font:900 32px Inter;padding:8px 14px;border-radius:10px;transform:rotate(6deg);opacity:0;z-index:6">ЛАЛИ, Я ТВОЙ ФАНАТ</div>
 <div id="fl2" style="position:absolute;inset:0;background:#fff;opacity:0;z-index:8"></div>
</div>
<div class="card" id="c3" style="background:radial-gradient(circle at 50% 40%,#0a3a5a,#020a14)">
 <div class="hdr" style="color:#64d2ff">Оценка экспоната</div>
 <div id="pr3" class="c mono" style="top:110px;font-size:58px;font-weight:900;color:#64d2ff">0 ₽</div>
 <div id="dm3" class="c" style="top:200px;font-size:170px;opacity:0">💎</div>
 <div id="ct3" class="c" style="top:420px;font-size:40px;font-weight:900;color:#fff;opacity:0">1000 карат</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#ffd6e8,#ff8ac4)">
 <div class="ch" data-p="y"></div><div class="ch" data-p="d"></div>
 <div id="hh4" style="position:absolute;inset:0;z-index:6"></div>
</div>
<div class="card" id="c5" style="background:linear-gradient(180deg,#f5e6d0,#d9b98a);color:#3a2410">
 <div id="wr5" style="position:absolute;left:60px;top:40px;background:#5a2e14;color:#f5e6d0;border-radius:14px;padding:10px 18px;font:900 26px Inter">ЛАЛИ · молочный 72%</div>
 <div id="pd5" style="position:absolute;left:150px;top:600px;width:300px;height:40px;border-radius:50%;background:#5a2e14;transform:scaleX(0)"></div>
 <div class="ch" data-p="e"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...((p=='x'||p=='y')?['#8e8e93','#c8c8cc','#8e8e93']:['#111','#ff8ac4','#ff2d78']));});})();'''
RENDER='''
 {place('a',300,490,1.05,false);pose('a',t>=4.04?{aL:150,aR:-30,hd:-8}:{aL:8,aR:-8});$('sp1').style.opacity=seg(t,3.48,3.6);$('pq1').style.opacity=seg(t,4.04,4.15);$('pq1').style.transform=`scale(${1+.15*pop(t,4.04,8)})`;}
 {place('b',150,690,.95,false);pose('b',t>=5.42?{aL:150,aR:-8,open:1}:{aL:8,aR:-8});place('x',430,690,1.1,true);pose('x',{aL:150+Math.sin(t*10)*10,aR:-150+Math.sin(t*10)*10,open:1,bob:-Math.abs(Math.sin(t*10))*8});
  $('sg2').style.opacity=seg(t,5.16,5.25);$('fl2').style.opacity=Math.max(pop(t,4.98,10),pop(t,5.42,10))*.7;}
 {const v=t<6.1?0:1e9*eo(seg(t,6.1,7.4));$('pr3').textContent=fmt(v)+' ₽';$('pr3').style.fontSize=(v>=1e8?44:58)+'px';$('dm3').style.opacity=seg(t,6.8,6.9);$('dm3').style.transform=`scale(${lerp(.3,1,eb(seg(t,6.8,7.1)))}) rotate(${Math.sin(t*3)*8}deg)`;
  $('ct3').style.opacity=seg(t,7.64,7.7);$('ct3').style.transform=`scale(${1+.3*pop(t,7.64,7)})`;place('c',120,690,.8,false);pose('c',{aL:8,aR:-8,hd:t>=7.64?-10:0});}
 {const up=eo(seg(t,9.16,9.78));place('y',300,690,1.2,false);pose('y',{aL:lerp(8,165,up),aR:-lerp(8,165,up),open:t>=9.78});place('d',300,lerp(690,330,up),.95,false,t>=9.78?Math.sin(t*3)*6:0);pose('d',t>=9.78?{aL:150,aR:-150,open:1,lL:-30,lR:30}:{aL:8,aR:-8});
  let h='';for(let i=0;i<8;i++){const s=9.8+i*.12;if(t>=s){const p=(t-s)/1.2;h+=`<div style="position:absolute;left:${120+rnd(i)*360}px;top:${450-p*400}px;font-size:${34+rnd(i+2)*20}px;opacity:${1-p}">💗</div>`}}$('hh4').innerHTML=h;}
 {const m=eo(seg(t,11.08,12.6));place('e',300,610,1.25,false);$('ch_e').style.transform=`scale(${1.25*(1+m*.35)},${1.25*(1-m*.4)})`;$('ch_e').style.filter=`sepia(${m}) saturate(${1+m*2}) hue-rotate(${-m*20}deg) brightness(${1-m*.35})`;pose('e',{aL:lerp(8,60,m),aR:-lerp(8,60,m),hd:m*15,open:t>=12.18});$('pd5').style.transform=`scaleX(${m})`;}
'''
