DUR=25.4
FADE=25.0
START=0
SONG='Женя Трофимов & Комната культуры — Нравится'
BG='linear-gradient(180deg,#0e1220,#04050a)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Нравится",0.0],["видеть",0.58],["тебя",1.78],["любой,",2.36]],
 [["молчать",3.24],["о",5.24],["тебе",5.4],["с",5.6],["тобой,",5.98]],
 [["и",6.64],["тихо",8.18],["упасть",8.6],["слезой",9.12]],
 [["сквозь",9.8],["улыбку",11.18],["внезапно",11.98]],
 [["нравится",12.88],["писать,",13.64],["что",14.98],["ещё",15.18],["не",15.36],["сплю,",15.72]],
 [["доеду",17.68],["и",18.4],["позвоню,",18.52]],
 [["не",19.5],["знать,",21.1],["как",21.44],["сказать",21.68],["«люблю»",22.0]],
 [["и",22.92],["крикнуть",23.52],["«до",24.14],["завтра»",24.4]],
]
SC=[[-0.3,3.1],[3.1,6.5],[6.5,12.75],[12.75,17.5],[17.5,19.4],[19.4,22.8],[22.8,99]]
GLOW=['#5a1d4a','#1d3a5a','#1d3a7a','#3a1d5a','#1d5a3a','#5a1d4a','#7a1f4a']
PEMO=['📸','🤍','🥲','🌙','🚕','⌨️','📣']
END=[25.0,25.4]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}.bb{position:absolute;max-width:380px;padding:14px 20px;border-radius:24px;font:800 26px Inter;opacity:0}'
PH=[('#ffd6e8','сонная'),('#ffe0b0','злая'),('#d6ecff','в капюшоне'),('#e0ffd6','без макияжа')]
HTML='''
<div class="card" id="c1" style="background:#000">
 <div class="hdr">Галерея · она</div>
 <div style="position:absolute;left:20px;right:20px;top:80px;display:grid;grid-template-columns:1fr 1fr;gap:12px">'''+''.join(f'<div id="ph{i}" style="height:270px;border-radius:16px;background:{c};position:relative;overflow:hidden;opacity:0"><div class="ch" data-p="p{i}"></div><div style="position:absolute;left:10px;bottom:8px;font:900 20px Inter;color:#111">{t}</div><div id="lk{i}" style="position:absolute;right:10px;top:8px;font-size:34px;opacity:0">❤️</div></div>' for i,(c,t) in enumerate(PH))+'''</div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#1a2a4a,#0a1020 60%,#1a1a1a 60%)">
 <div style="position:absolute;left:80px;top:470px;width:440px;height:40px;background:#6a4a2a;border-radius:8px"></div>
 <div class="ch" data-p="a"></div><div class="ch" data-p="g"></div>
 <div id="dt2a" class="bb" style="left:60px;top:140px;background:#3a3a3c">…</div><div id="dt2b" class="bb" style="right:60px;top:140px;background:#0a84ff">…</div>
 <div id="tx2" class="c" style="top:60px;font:900 32px Inter;color:#fff;opacity:0">молчим вместе 🤍</div>
</div>
<div class="card" id="c3" style="background:radial-gradient(circle at 50% 40%,#2a3a6a,#0a0e1a)">
 <div class="ch" data-p="b"></div>
 <div id="tr3" style="position:absolute;width:22px;height:30px;border-radius:50% 50% 50% 50%/60% 60% 40% 40%;background:#64d2ff;box-shadow:0 0 10px #64d2ff;opacity:0;z-index:7"></div>
 <div id="tx3" class="c" style="top:60px;font:900 34px Inter;color:#fff;opacity:0">улыбаюсь и плачу 🥲</div>
</div>
<div class="card" id="c4" style="background:#000">
 <div class="hdr">Чат · она · <span style="color:#30d158">в сети</span></div>
 <div class="c mono" style="top:80px;font-size:70px;font-weight:300;color:#8e8e93">03:47</div>
 <div id="m4" class="bb" style="right:24px;top:220px;background:#0a84ff">ещё не сплю 🌙</div>
 <div id="m4b" class="bb" style="left:24px;top:310px;background:#3a3a3c">я тоже)</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c5" style="background:#e8eef4;color:#111">
 <div style="position:absolute;inset:0;background-image:linear-gradient(#d0d8e0 2px,transparent 2px),linear-gradient(90deg,#d0d8e0 2px,transparent 2px);background-size:80px 80px"></div>
 <svg width="600" height="690" style="position:absolute;inset:0"><path d="M80 560 Q200 300 300 380 T520 140" stroke="#0a84ff" stroke-width="10" fill="none" stroke-linecap="round"/></svg>
 <div id="car5" style="position:absolute;font-size:60px">🚕</div>
 <div style="position:absolute;left:470px;top:90px;font-size:50px">🏠</div>
 <div id="cl5" style="position:absolute;left:24px;right:24px;bottom:24px;background:#30d158;border-radius:22px;padding:16px;text-align:center;font:900 28px Inter;color:#fff;opacity:0">📞 звоню тебе…</div>
</div>
<div class="card" id="c6" style="background:#000">
 <div class="hdr">Чат · она</div>
 <div style="position:absolute;left:24px;right:24px;bottom:120px;background:#1c1c1e;border-radius:24px;padding:16px 20px;font:800 30px Inter;min-height:70px"><span id="ty6"></span><span style="opacity:.5">|</span></div>
 <div id="cnt6" style="position:absolute;left:24px;bottom:60px;font:700 20px Inter;color:#8e8e93"></div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c7" style="background:linear-gradient(180deg,#ff9f43,#ff6a8a)">
 <div id="sh7" class="c" style="top:90px;font:900 90px Inter;color:#fff;text-shadow:0 8px 0 rgba(0,0,0,.2);opacity:0;line-height:1">ДО<br>ЗАВТРА!</div>
 <div id="wv7" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="e"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...((p.startsWith('p')||p=='g')?['#ff2d78','#ff8ac4','#ff2d78']:['#111','#64d2ff','#0a84ff']));});})();'''
RENDER='''
 {const T=[0.0,0.58,1.78,2.36];const P=[{aL:8,aR:-8,hd:20},{aL:60,aR:-60,open:1,hd:-10},{aL:8,aR:-8,hd:0},{aL:150,aR:-8,open:1}];for(let i=0;i<4;i++){$('ph'+i).style.opacity=seg(t,T[i],T[i]+.15);$('ph'+i).style.transform=`scale(${lerp(.7,1,eb(seg(t,T[i],T[i]+.3)))})`;
   place('p'+i,130,300,.85,i%2==1);pose('p'+i,P[i]);$('lk'+i).style.opacity=seg(t,T[i]+.4,T[i]+.5);$('lk'+i).style.transform=`scale(${1+.5*pop(t,T[i]+.4,8)})`;}
  $('ch_p2').style.filter='brightness(.4)';}
 {place('a',220,480,.85,false);pose('a',{aL:8,aR:-8,lL:-80,lR:-80,bob:40,hd:-6});place('g',380,480,.85,true);pose('g',{aL:8,aR:-8,lL:-80,lR:-80,bob:40,hd:-6});
  const d='.'.repeat(1+Math.floor(t*3)%3);$('dt2a').textContent=d;$('dt2b').textContent=d;$('dt2a').style.opacity=seg(t,3.24,3.4);$('dt2b').style.opacity=seg(t,5.24,5.4);$('tx2').style.opacity=seg(t,5.98,6.1);}
 {place('b',300,690,1.4,false);pose('b',{aL:8,aR:-8,hd:-4,open:t>=11.18});const k=seg(t,8.6,10.6);$('tr3').style.opacity=t>=8.6?1-seg(t,10.6,11):0;$('tr3').style.left=(300-22)+'px';$('tr3').style.top=(690-290*1.4+110+k*90)+'px';$('tx3').style.opacity=seg(t,11.18,11.3);}
 {$('m4').style.opacity=seg(t,13.64,13.75);$('m4b').style.opacity=seg(t,15.72,15.85);place('c',150,690,.8,false);pose('c',{aL:8,aR:-140,hd:-12});}
 {const k=eo(seg(t,17.68,18.5));const x=lerp(80,500,k),y=k<.5?lerp(560,370,k*2):lerp(370,150,(k-.5)*2);$('car5').style.left=(x-30)+'px';$('car5').style.top=(y-40)+'px';$('cl5').style.opacity=seg(t,18.52,18.62);$('cl5').style.transform=`scale(${1+.05*Math.sin(t*12)})`;}
 {const W=['л','лю','люб','любл','люблю','любл','люб','лю','л','',' ','с','сп','спо','спок','споки 🙂'];const i=Math.max(0,Math.min(W.length-1,Math.floor((t-19.5)*5)));$('ty6').textContent=t<19.5?'':W[i];$('cnt6').textContent=t>=19.5?'стёрто: '+Math.min(9,Math.floor((t-19.5)*2))+' раз':'';
  place('d',300,400,.75,false);pose('d',{aL:8,aR:-8,hd:Math.sin(t*3)*10});}
 {$('sh7').style.opacity=seg(t,23.52,23.6);$('sh7').style.transform=`scale(${lerp(.5,1,eb(seg(t,23.52,23.9)))+.08*pop(t,24.4,7)})`;let w='';if(t>=23.52)for(let i=0;i<4;i++){const p=((t-23.52)*1.2+i/4)%1;w+=`<div style="position:absolute;left:${300-p*260}px;top:${360-p*260}px;width:${p*520}px;height:${p*520}px;border-radius:50%;border:6px solid rgba(255,255,255,${1-p})"></div>`}$('wv7').innerHTML=w;
  place('e',300,690,1.15,false);pose('e',t>=23.52?{aL:150,aR:-150,open:1,bob:-Math.abs(Math.sin(t*10))*10}:{aL:8,aR:-8});}
'''
