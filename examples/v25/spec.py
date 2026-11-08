BG='linear-gradient(180deg,#120812,#050206)'
SUBW='900'
SUBX='text-transform:uppercase'
RED='любви'
REDC='#ff2d55'
LINES=[
 [["и",0.25],["посмотри,",0.75],["как",1.25],["сердце",1.75],["бьётся",2.5]],
 [["пули",4.25]],
 [["пули",6.0],["летят,",6.25],["летят",8.25],["в",9.5],["сторону",11.0],["мою",12.25]],
 [["пули",13.25]],
 [["пули",15.0],["твоей",15.75],["любви",16.25],["раздели",16.75]],
]
SC=[[-0.3,4.15],[4.15,5.95],[5.95,13.15],[13.15,14.95],[14.95,99]]
GLOW=['#6a0a2a','#3a1d5a','#5a0a1a','#7a0a2a','#7a1f5a']
PEMO=['💓','💘','💘','💥','💞']
END=[17.45,17.88]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}.bl{position:absolute;font-size:56px;z-index:6}'
HTML='''
<div class="card" id="c1" style="background:#000">
 <div class="hdr" style="color:#ff375f">❤ Пульс</div>
 <div id="bpm1" class="mono" style="position:absolute;right:40px;top:30px;font-size:48px;font-weight:800">72</div>
 <svg width="600" height="160" style="position:absolute;top:110px;left:0"><path id="ecg1" fill="none" stroke="#ff375f" stroke-width="5"/></svg>
 <div id="hb1" style="position:absolute;left:300px;top:420px;font-size:90px;z-index:7;margin:-45px 0 0 -45px">❤️</div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#1a1430,#07050e)">
 <div id="n2" style="position:absolute;left:24px;right:24px;top:40px;background:rgba(60,60,64,.9);border-radius:24px;padding:16px 20px;display:flex;gap:14px;align-items:center;opacity:0">
  <div style="width:56px;height:56px;border-radius:14px;background:#ff2d55;display:flex;align-items:center;justify-content:center;font-size:30px">💘</div><div><div style="font-size:24px;font-weight:900">Входящие</div><div style="font-size:20px;color:#d1d1d6;font-weight:600">пули · летят к вам</div></div></div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:radial-gradient(circle at 50% 70%,#0e2a16,#020804)">
 <svg width="600" height="690" style="position:absolute;inset:0" id="rad3"></svg>
 <div id="bul3"></div>
 <div class="ch" data-p="c"></div>
 <div style="position:absolute;left:24px;right:24px;top:24px;background:rgba(0,0,0,.5);border-radius:22px;padding:14px 20px;display:flex;justify-content:space-between;font-size:24px;font-weight:800;color:#30d158"><span>📡 Радар · пули</span><span id="cn3" class="mono">0</span></div>
</div>
<div class="card" id="c4" style="background:#1c0a10">
 <div id="hit4" class="bl" style="font-size:80px">💘</div>
 <div id="bm4" style="position:absolute;left:250px;top:330px;font-size:160px;opacity:0;z-index:7">💥</div>
 <div class="ch" data-p="d"></div>
 <div id="t4" class="c" style="top:60px;font-size:40px;font-weight:900;color:#ff2d55;opacity:0">ПОПАДАНИЕ 💘</div>
</div>
<div class="card" id="c5" style="background:#1c1c1e">
 <div class="hdr">Поделиться</div><div class="ttl">Раздели</div>
 <div id="hL" style="position:absolute;left:300px;top:200px;width:80px;height:160px;overflow:hidden;margin-left:-80px"><div style="width:160px;font-size:140px;line-height:160px;text-align:center">❤️</div></div>
 <div id="hR" style="position:absolute;left:300px;top:200px;width:80px;height:160px;overflow:hidden"><div style="width:160px;margin-left:-80px;font-size:140px;line-height:160px;text-align:center">❤️</div></div>
 <div class="ch" data-p="e"></div><div class="ch" data-p="f"></div>
 <div id="t5" class="c" style="bottom:30px;font-size:30px;font-weight:900;color:#ff2d55;opacity:0">50 / 50 💞</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
const GIRL=['#ff9ac1','#f3e8ff','#b38cff'];
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...(p=='f'?GIRL:['#64d2ff','#ff8ac4','#ff2d78']));});
 let b='';for(let i=0;i<8;i++)b+=`<div class="bl" id="b3_${i}">💘</div>`;$('bul3').innerHTML=b;
 let r='';for(let k=1;k<5;k++)r+=`<circle cx="300" cy="500" r="${k*90}" fill="none" stroke="rgba(48,209,88,.25)" stroke-width="2"/>`;$('rad3').innerHTML=r+'<line id="sw3" x1="300" y1="500" x2="300" y2="140" stroke="rgba(48,209,88,.6)" stroke-width="4"/>';})();
'''
RENDER='''
 {const b=Math.round(lerp(72,140,seg(t,1.75,3.0)));$('bpm1').textContent=b;let d='M0 80';for(let x=0;x<=600;x+=4){const ph=((x/600*3+t*b/60)%1);let v=0;if(ph>.4&&ph<.44)v=-60;else if(ph>.44&&ph<.47)v=40;d+=` L${x} ${80+v}`}$('ecg1').setAttribute('d',d);
  const beat=Math.pow(Math.abs(Math.sin(t*b/60*Math.PI)),8);$('hb1').style.transform=`scale(${1+beat*.35})`;$('hb1').style.left=(300+20)+'px';$('hb1').style.top=(460)+'px';
  place('a',300,660,1.2,false);pose('a',t>=0.75?{aL:-58,aR:58,hd:6}:{aL:8,aR:-8});}
 {$('n2').style.opacity=seg(t,4.25,4.4);$('n2').style.transform=`translateY(${(1-eb(seg(t,4.25,4.5)))*-40}px)`;place('b',300,660,1.25,false);
  pose('b',t>=4.25?{aL:55,aR:-55,hd:-14,open:1,bob:-pop(t,4.25,6)*40}:{aL:8,aR:-8});}
 {$('sw3').setAttribute('transform',`rotate(${t*180} 300 500)`);let n=0;const T=[6.0,6.25,7.2,8.25,9.0,9.5,11.0,12.25];
  T.forEach((s,i)=>{const e=$('b3_'+i);const p=seg(t,s,s+.9);const from=i%2?[-60,150+i*40]:[620,120+i*40];e.style.left=lerp(from[0],300,p)+'px';e.style.top=lerp(from[1],470,p)+'px';e.style.opacity=p>0&&p<1?1:0;e.style.transform=`scaleX(${i%2?1:-1})`;if(t>=s)n++;});
  $('cn3').textContent=n;const dodge=Math.sin(t*6);place('c',300+dodge*30,640,1.0,false,dodge*20);pose('c',{aL:120+Math.sin(t*14)*30,aR:-120-Math.sin(t*14)*30,open:1,hd:-dodge*10,lL:dodge*15,lR:-dodge*15});}
 {const p=seg(t,13.25,13.6);$('hit4').style.left=lerp(620,300,p)+'px';$('hit4').style.top='380px';$('hit4').style.opacity=p<1&&t>=13.25?1:0;$('bm4').style.opacity=t>=13.6?1-seg(t,13.9,14.3):0;
  $('t4').style.opacity=seg(t,13.6,13.7);const h=t>=13.6;place('d',300,660,1.2,false,h?-eo(seg(t,13.6,14.0))*25:0);pose('d',h?{aL:-58,aR:58,hd:-20,open:1}:{aL:8,aR:-8});if(si==3)shake('c4',t,13.6,12);}
 {const s=t>=16.75?eo(seg(t,16.75,17.1)):0;$('hL').style.transform=`translateX(${-s*150}px) rotate(${-s*10}deg)`;$('hR').style.transform=`translateX(${s*150}px) rotate(${s*10}deg)`;$('t5').style.opacity=seg(t,16.9,17.0);
  place('e',150,660,1.0,false);place('f',450,660,1.0,true);const o=t>=16.75?{aL:8,aR:-150,open:1}:{aL:8,aR:-95};pose('e',o);pose('f',o);}
'''
