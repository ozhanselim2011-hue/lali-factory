DUR=22.8
FADE=22.4
START=0
SONG='Баста & Моя Мишель — Если я буду танцевать'
BG='linear-gradient(180deg,#0a0a1a,#030306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Если",0.0],["я",0.38],["буду",0.68],["танцевать,",1.1]],
 [["то",1.88],["только",2.1],["с",2.24],["тобой,",2.42],["моя",2.78],["любовь",3.42]],
 [["если",7.68],["я",8.02],["буду",8.42],["танцевать,",8.76]],
 [["то",9.76],["только",9.8],["с",9.88],["тобой,",10.08],["моя",10.46],["любовь",11.14]],
 [["я",14.96],["хотела",15.28],["бы",15.9],["остаться",16.2],["на",16.8],["окраине",17.34],["вселенной",18.0]],
 [["в",18.78],["этом",19.1],["одиноком",19.4],["танце,",20.22],["ты",20.88],["течёшь",21.04],["по",21.5],["моим",21.78],["венам",22.2]],
]
SC=[[-0.3,1.8],[1.8,7.6],[7.6,9.7],[9.7,14.9],[14.9,18.7],[18.7,99]]
GLOW=['#3a3a5a','#7a1f4a','#5a1d7a','#7a1f4a','#1a2a7a','#7a1f1f']
PEMO=['💃','💖','📝','🔒','🪐','🩸']
END=[22.4,22.8]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#1c1c1e">
 <div class="hdr">Приглашения на танец</div>
 <div id="iv1" style="position:absolute;left:24px;right:24px;top:70px"></div>
 <div class="ch" data-p="z"></div>
</div>
<div class="card" id="c2" style="background:radial-gradient(circle at 50% 20%,#5a1a4a,#0a0410)">
 <div id="sp2" style="position:absolute;left:150px;top:0;width:300px;height:690px;background:radial-gradient(ellipse at 50% 0%,rgba(255,180,230,.45),transparent 70%);clip-path:polygon(40% 0,60% 0,100% 100%,0 100%)"></div>
 <div id="db2" style="position:absolute;left:255px;top:30px;font-size:80px">🪩</div>
 <div class="ch" data-p="a"></div><div class="ch" data-p="b"></div>
 <div id="hs2" style="position:absolute;inset:0;z-index:6"></div>
</div>
<div class="card" id="c3" style="background:#f4ecd8;color:#2a1f10">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Запись на танцы</div><div class="ttl">Анкета</div>
 <div style="position:absolute;left:30px;right:30px;top:150px;font-size:28px;font-weight:800;line-height:2">Имя: <u>Лали</u><br>Стиль: <u>медляк</u><br>Партнёр: <span id="pt3" style="border-bottom:3px solid #2a1f10;padding:0 40px">&nbsp;</span></div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:#f4ecd8;color:#2a1f10">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Запись на танцы</div><div class="ttl">Анкета</div>
 <div style="position:absolute;left:30px;right:30px;top:150px;font-size:28px;font-weight:800;line-height:2">Имя: <u>Лали</u><br>Стиль: <u>медляк</u><br>Партнёр: <span id="pt4" style="color:#ff2d78"></span></div>
 <div id="lk4" style="position:absolute;left:230px;top:380px;font-size:130px;opacity:0;z-index:6">🔒</div>
 <div id="ot4" class="c" style="top:560px;font-size:24px;font-weight:900;color:#d0021b;opacity:0;z-index:6">другие варианты: недоступны</div>
</div>
<div class="card" id="c5" style="background:radial-gradient(circle at 30% 70%,#1a1a4a,#020210)">
 <div id="st5" style="position:absolute;inset:0"></div>
 <div style="position:absolute;left:40px;top:420px;font-size:120px">🌍</div><div style="position:absolute;left:200px;top:300px;font-size:60px">🪐</div><div style="position:absolute;left:330px;top:200px;font-size:40px">🌑</div>
 <div id="pl5" style="position:absolute;left:470px;top:70px;width:70px;height:70px;border-radius:50%;background:#bf5af2;box-shadow:0 0 30px #bf5af2"></div>
 <div id="lb5" style="position:absolute;left:330px;top:150px;background:#fff;color:#111;border-radius:14px;padding:6px 12px;font-size:20px;font-weight:900;opacity:0">📍 окраина вселенной</div>
 <div class="ch" data-p="d"></div><div class="ch" data-p="e"></div>
</div>
<div class="card" id="c6" style="background:#f2f2f7;color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.45)">Анализ крови</div><div class="ttl">Результаты</div>
 <div style="position:absolute;left:30px;right:30px;top:150px;font-size:24px;font-weight:800;line-height:1.9">
  <div style="display:flex;justify-content:space-between"><span>эритроциты</span><span class="mono" id="r6a">4.5</span></div>
  <div style="display:flex;justify-content:space-between"><span>гемоглобин</span><span class="mono" id="r6b">140</span></div>
  <div style="display:flex;justify-content:space-between;color:#ff2d78"><span>💖 она</span><span class="mono" id="r6c">0%</span></div></div>
 <svg width="600" height="260" style="position:absolute;left:0;top:400px"><path d="M0 120 C150 40 250 200 400 110 S560 60 600 120" stroke="#d0021b" stroke-width="26" fill="none" stroke-linecap="round"/></svg>
 <div id="vn6" style="position:absolute;inset:0;z-index:4"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=(p=='b'||p=='e')?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 $('iv1').innerHTML=['Маша · потанцуем?','Катя · го на медляк','Лена · танец?','Аня · 💃?'].map((s,i)=>`<div style="display:flex;justify-content:space-between;align-items:center;background:#2c2c2e;border-radius:18px;padding:12px 16px;margin-bottom:12px;font-size:24px;font-weight:800">${s}<span id="d1_${i}" style="color:#ff453a;opacity:0">❌ отклонено</span></div>`).join('');
 let h='';for(let i=0;i<10;i++)h+=`<div id="h2_${i}" style="position:absolute;font-size:${24+i%3*10}px;opacity:0">💖</div>`;$('hs2').innerHTML=h;
 let s='';for(let i=0;i<40;i++)s+=`<div style="position:absolute;left:${rnd(i)*590}px;top:${rnd(i+9)*680}px;width:3px;height:3px;border-radius:50%;background:#fff;opacity:${.3+rnd(i+2)*.7}"></div>`;$('st5').innerHTML=s;
 let v='';for(let i=0;i<8;i++)v+=`<div id="v6_${i}" style="position:absolute;font-size:30px">💖</div>`;$('vn6').innerHTML=v;})();
'''
RENDER='''
 {place('z',300,700,.95,false);pose('z',{aL:8,aR:-150+Math.sin(t*10)*20,hd:8});for(let i=0;i<4;i++){$('d1_'+i).style.opacity=seg(t,0.3+i*.25,0.4+i*.25);}}
 {$('db2').style.transform=`rotate(${t*60}deg)`;const k=eo(seg(t,2.0,3.2));place('a',lerp(120,250,k),690,1.0,false);place('b',lerp(480,350,k),690,1.0,true);
  const sw=Math.sin(t*2)*8;pose('a',t>=2.42?{aL:8,aR:-100,hd:-8,bob:sw/3}:{aL:8,aR:-8});pose('b',t>=2.42?{aL:8,aR:-100,hd:-8,bob:-sw/3}:{aL:8,aR:-8});
  $('ch_a').style.transform+=` rotate(${t>=3?sw/2:0}deg)`;
  for(let i=0;i<10;i++){const ph=(t*.5+i/10)%1;const e=$('h2_'+i);e.style.opacity=t>=3.42?1-ph:0;e.style.left=(150+rnd(i)*300)+'px';e.style.top=(420-ph*300)+'px';}}
 {place('c',470,700,.8,true);pose('c',{aL:8,aR:-100,hd:Math.sin(t*2)*8});}
 {const nm='она 💖 (и только она)';$('pt4').textContent=nm.slice(0,Math.round(nm.length*seg(t,10.0,11.1)));$('lk4').style.opacity=seg(t,11.14,11.25);$('lk4').style.transform=`scale(${1+.3*pop(t,11.14,6)})`;$('ot4').style.opacity=seg(t,11.8,11.9);}
 {$('lb5').style.opacity=seg(t,17.34,17.5);const k=eo(seg(t,15.3,17.3));place('d',lerp(100,480,k),lerp(690,100,k),lerp(.8,.25,k),false);place('e',lerp(170,520,k),lerp(690,100,k),lerp(.8,.25,k),true);pose('d',{aL:8,aR:-90});pose('e',{aL:8,aR:-90});}
 {const p=Math.round(eo(seg(t,20.9,22.2))*98);$('r6c').textContent=p+'%';
  for(let i=0;i<8;i++){const ph=(t*.35+i/8)%1;const x=ph*600;const y=400+120-((Math.sin(ph*Math.PI*2.2))*45)-15;const e=$('v6_'+i);e.style.left=x+'px';e.style.top=(y-20)+'px';e.style.opacity=t>=20.74?1:0;}}
'''
