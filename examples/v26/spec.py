BG='linear-gradient(180deg,#0a1410,#030604)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["я",0.75],["подбираюсь",1.0],["осторожно,",2.0],["детка,",2.75],["будто",3.0],["следопыт",3.25]],
 [["ты",4.0],["слышишь",4.25],["ох*енный",5.0],["голос",5.5]],
 [["и",6.0],["танцуешь",6.25],["в",6.75],["этот",6.85],["ритм",7.25]],
 [["и",7.5],["я",7.75],["добавлю",8.0],["тебе",8.5],["звука,",8.75],["чтобы",9.0],["ты",9.5],["могла",9.75],["идти",10.25]],
 [["и",10.75],["я",11.0],["качусь",11.25],["по",11.5],["веб-сетям,",11.75],["таким,",12.75],["как",13.0],["я,",13.25],["те",13.5],["не",13.75],["найти",14.25]],
]
SC=[[-0.3,3.9],[3.9,5.95],[5.95,7.4],[7.4,10.6],[10.6,99]]
GLOW=['#1a4a2a','#3a1d6a','#5a1d4a','#1d3a6a','#0a4a5a']
PEMO=['👣','🎤','💃','🔊','🌐']
END=[14.6,14.95]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#e3e8e0;color:#111">
 <div id="ft1" style="position:absolute;inset:0"></div>
 <div style="position:absolute;left:470px;top:230px;width:80px;height:80px;margin:-40px;border-radius:50%;background:#fff;box-shadow:0 6px 20px rgba(0,0,0,.2);display:flex;align-items:center;justify-content:center;font-size:44px">👩</div>
 <div class="ch" data-p="a"></div>
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 6px 20px rgba(0,0,0,.1)"><div style="font-size:24px;font-weight:900">Локатор · Она</div><div id="d1" class="mono" style="font-size:22px;color:#30a14e;font-weight:700">120 м</div></div>
</div>
<div class="card" id="c2" style="background:#000">
 <div class="hdr" style="color:#ff453a">Диктофон</div>
 <div id="wf2" style="position:absolute;left:30px;right:30px;top:90px;height:150px;display:flex;align-items:center;gap:4px"></div>
 <div class="ch" data-p="b"></div><div class="ch" data-p="c"></div>
 <div id="t2" class="c" style="top:260px;font-size:30px;font-weight:900;color:#ff9f0a;opacity:0">качество голоса: ох*енное 🔥</div>
</div>
<div class="card" id="c3" style="background:linear-gradient(180deg,#2a0a2a,#0a020a)">
 <div class="hdr" style="color:#ff2d78">Метроном</div>
 <div id="mt3" style="position:absolute;left:298px;top:90px;width:6px;height:200px;background:#fff;border-radius:3px;transform-origin:3px 200px"></div>
 <div class="ch" data-p="d"></div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div class="hdr">Громкость</div>
 <div style="position:absolute;left:60px;top:80px;width:120px;height:440px;border-radius:40px;background:#3a3a3c;overflow:hidden"><div id="vl4" style="position:absolute;left:0;right:0;bottom:0;background:#fff;height:20%"></div><div style="position:absolute;left:0;right:0;bottom:20px;text-align:center;font-size:48px">🔊</div></div>
 <div id="vp4" class="mono" style="position:absolute;left:60px;top:540px;width:120px;text-align:center;font-size:30px;font-weight:800">20%</div>
 <div class="ch" data-p="e"></div><div class="ch" data-p="f"></div>
</div>
<div class="card" id="c5" style="background:#05141a">
 <svg width="600" height="690" style="position:absolute;inset:0" id="net5"></svg>
 <div class="ch" data-p="g"></div>
 <div style="position:absolute;left:24px;right:24px;top:24px;background:#1c1c1e;border-radius:22px;padding:14px 20px;font-size:24px;font-weight:700">🔍 <span id="q5"></span></div>
 <div id="r5" class="c" style="bottom:30px;font-size:30px;font-weight:900;color:#64d2ff;opacity:0">0 результатов · таких не найти</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
const GIRL=['#ff9ac1','#f3e8ff','#b38cff'];
(function(){const G={c:1,d:1,f:1};document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...(G[p]?GIRL:['#64d2ff','#ff8ac4','#ff2d78']));});
 let f='';for(let i=0;i<10;i++)f+=`<div id="f1_${i}" style="position:absolute;font-size:32px;opacity:0;left:${80+i*36}px;top:${600-i*36+(i%2)*14}px;transform:rotate(-40deg)">👣</div>`;$('ft1').innerHTML=f;
 let w='';for(let i=0;i<50;i++)w+=`<div id="w2_${i}" style="flex:1;border-radius:3px;background:#ff453a"></div>`;$('wf2').innerHTML=w;
 const N=[[80,200],[220,140],[380,210],[520,150],[140,350],[300,320],[460,380],[90,520],[260,500],[430,540],[560,470]];let s='';
 N.forEach((a,i)=>N.forEach((b,j)=>{if(j>i&&Math.hypot(a[0]-b[0],a[1]-b[1])<220)s+=`<line x1="${a[0]}" y1="${a[1]}" x2="${b[0]}" y2="${b[1]}" stroke="rgba(100,210,255,.35)" stroke-width="3"/>`}));
 N.forEach(a=>s+=`<circle cx="${a[0]}" cy="${a[1]}" r="9" fill="#64d2ff"/>`);$('net5').innerHTML=s;})();
'''
RENDER='''
 {const p=seg(t,0.75,3.8);for(let i=0;i<10;i++)$('f1_'+i).style.opacity=p*10>i?.8:0;const x=lerp(100,400,p),y=lerp(640,330,p);
  const w=walk(t,6);w.bob=(w.bob||0)+14;w.aL=-30;w.aR=30;w.hd=10;place('a',x,y,lerp(.75,.45,p),false);pose('a',t>=0.75?w:{aL:8,aR:-8});$('d1').textContent=Math.round(lerp(120,3,p))+' м · крадусь 🤫';}
 {const s=t>=4.25;for(let i=0;i<50;i++)$('w2_'+i).style.height=(4+(s?Math.abs(Math.sin(i*1.7+t*9))*130:0))+'px';
  place('b',190,660,1.05,false);pose('b',s?{aL:70,aR:-150+Math.sin(t*6)*10,open:Math.sin(t*16)>0}:{aL:8,aR:-8});
  place('c',430,660,1.0,true);pose('c',t>=5.0?{aL:-58,aR:58,hd:10,open:1}:{aL:8,aR:-8,hd:-6});$('t2').style.opacity=seg(t,5.0,5.15);}
 {const q=Math.sin(t*Math.PI*2.2);$('mt3').style.transform=`rotate(${q*30}deg)`;place('d',300,670,1.25,false);
  pose('d',t>=6.25?{aL:lerp(20,150,(q+1)/2),aR:-lerp(20,150,(1-q)/2),lL:q*14,lR:-q*14,bob:-Math.abs(q)*12,open:1,hd:q*8}:{aL:8,aR:-8});}
 {const v=t<8.75?20:lerp(20,100,eo(seg(t,8.75,9.5)));$('vl4').style.height=v+'%';$('vp4').textContent=Math.round(v)+'%';
  place('e',300,660,.95,false);pose('e',t>=8.0?{aL:8,aR:-95+(t<9.5?Math.sin(t*10)*8:0)}:{aL:8,aR:-8});
  const g=seg(t,10.25,10.6);place('f',lerp(460,560,g),660,.95,true);pose('f',t>=9.75?walk(t,12):{aL:8,aR:-8,hd:-6});}
 {const p=seg(t,11.25,14.0);const x=lerp(60,520,p),y=lerp(560,300,p)+Math.sin(p*12)*30;place('g',x,y,.55,false,t>=11.25&&t<14.0?t*600:0);pose('g',t>=14.25?{aL:8,aR:-8,hd:-6,rot:-5}:{aL:-58,aR:58,lL:-40,lR:40});
  const q='таких как я';$('q5').textContent=t<12.75?'':q.slice(0,Math.floor(seg(t,12.75,13.4)*q.length));$('r5').style.opacity=seg(t,14.25,14.35);}
'''
