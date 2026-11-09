DUR=13.9
FADE=13.5
START=1.5
SONG='NEMIGA & Дорогой Дневник — Весь этот мир'
BG='linear-gradient(180deg,#070a18,#020306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Весь",1.76],["этот",2.16],["мир",2.46],["выключает",2.9],["фонари",3.9]],
 [["и",4.46],["включает",5.1],["их",6.12],["только",6.5],["для",7.08],["нас",7.44],["двоих",7.78]],
 [["весь",8.0],["этот",9.12],["мир",9.56],["отвернулся",9.98],["от",11.06],["любви",11.16]],
 [["милая",11.76],["мысль,",12.9],["чтобы",13.48],["это",13.9],["изменить",14.38]],
]
SC=[[1.2,4.4],[4.4,7.95],[7.95,11.7],[11.7,99]]
GLOW=['#1a2a7a','#7a6a1a','#3a3a4a','#7a1f4a']
PEMO=['🌃','💡','🙈','💖']
END=[15.0,15.4]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#0a1030,#1a2050)">
 <div class="hdr" style="color:#64d2ff">Умный город</div><div class="ttl" style="font-size:36px">Фонари: <span id="lc1" class="mono">6/6</span></div>
 <div id="lm1" style="position:absolute;left:0;right:0;top:200px;height:400px"></div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:90px;background:#111"></div>
</div>
<div class="card" id="c2" style="background:#05060f">
 <div id="lt2" style="position:absolute;left:150px;top:60px;width:300px;height:600px;background:radial-gradient(ellipse at 50% 0%,rgba(255,214,10,.55),transparent 70%);clip-path:polygon(40% 0,60% 0,100% 100%,0 100%);opacity:0"></div>
 <div style="position:absolute;left:290px;top:40px;width:20px;height:40px;background:#444;border-radius:6px"></div><div id="bu2" style="position:absolute;left:280px;top:75px;width:40px;height:24px;border-radius:12px;background:#333"></div>
 <div style="position:absolute;left:150px;top:560px;width:300px;height:24px;background:#5a3a1a;border-radius:8px"></div>
 <div class="ch" data-p="a"></div><div class="ch" data-p="b"></div>
 <div id="nt2" style="position:absolute;left:24px;right:24px;top:24px;background:rgba(60,60,64,.95);border-radius:22px;padding:12px 16px;font-size:22px;font-weight:800;opacity:0;z-index:8">💡 Фонарь №1 включён · доступ: только вы двое</div>
</div>
<div class="card" id="c3" style="background:linear-gradient(180deg,#2c2c2e,#111)">
 <div class="hdr">Любовь · статистика</div><div class="ttl" style="font-size:36px">Интерес: <span id="in3" class="mono" style="color:#ff453a">100%</span></div>
 <div class="ch" data-p="c"></div><div class="ch" data-p="d"></div><div class="ch" data-p="e"></div><div class="ch" data-p="f"></div>
 <div id="hr3" style="position:absolute;left:250px;top:200px;font-size:100px;z-index:6">💔</div>
</div>
<div class="card" id="c4" style="background:radial-gradient(circle at 50% 40%,#5a0b3a,#14020c)">
 <div id="id4" style="position:absolute;left:250px;top:140px;font-size:100px;opacity:0;z-index:6">💡</div>
 <div class="c" id="pl4" style="top:40px;font-size:32px;font-weight:900;opacity:0">План «Изменить мир» ✅</div>
 <div id="hs4" style="position:absolute;inset:0;z-index:7"></div>
 <div class="ch" data-p="g"></div><div class="ch" data-p="h"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML='cdef'.includes(p)?CH(p,'#8e8e93','#c8c8cc','#8e8e93'):(p=='b'||p=='h'?CH(p,'#ff8ac4','#ffffff','#ffd6e8'):CH(p,'#64d2ff','#ff8ac4','#ff2d78'));});
 let l='';for(let i=0;i<6;i++){const x=30+i*95;l+=`<div style="position:absolute;left:${x+30}px;top:60px;width:8px;height:340px;background:#444"></div><div id="g1_${i}" style="position:absolute;left:${x}px;top:-40px;width:70px;height:220px;background:radial-gradient(ellipse at 50% 20%,rgba(255,214,10,.8),transparent 70%)"></div><div id="b1_${i}" style="position:absolute;left:${x+18}px;top:50px;width:32px;height:20px;border-radius:10px;background:#ffd60a"></div>`;}$('lm1').innerHTML=l;
 let h='';for(let i=0;i<18;i++)h+=`<div id="h4_${i}" style="position:absolute;font-size:${30+rnd(i)*30}px;opacity:0">💖</div>`;$('hs4').innerHTML=h;})();
'''
RENDER='''
 {let on=0;for(let i=0;i<6;i++){const off=t>=2.9+i*.18;$('g1_'+i).style.opacity=off?0:1;$('b1_'+i).style.background=off?'#333':'#ffd60a';if(!off)on++;}$('lc1').textContent=on+'/6';}
 {const on=t>=5.1;$('lt2').style.opacity=on?1:0;$('bu2').style.background=on?'#ffd60a':'#333';$('bu2').style.boxShadow=on?'0 0 40px #ffd60a':'none';$('nt2').style.opacity=seg(t,6.12,6.3);
  place('a',240,690,.85,false);place('b',360,690,.85,true);const c=t>=7.44;pose('a',c?{aL:8,aR:-60,hd:10}:{aL:8,aR:-8,hd:-6});pose('b',c?{aL:8,aR:-60,hd:10}:{aL:8,aR:-8,hd:-6});}
 {const tr=t>=9.98;[['c',90],['d',230],['e',370],['f',510]].forEach(([p,x],i)=>{place(p,x,690,.8,tr&&seg(t,9.98+i*.12,10.1+i*.12)>.5);pose(p,{aL:8,aR:-8,hd:tr?-8:0});});
  $('in3').textContent=Math.round(lerp(100,0,eo(seg(t,9.98,11.3))))+'%';$('hr3').style.opacity=t>=11.06?1:.25;$('hr3').style.transform=`scale(${1+.3*pop(t,11.06,6)})`;}
 {$('id4').style.opacity=seg(t,12.9,13.0);$('id4').style.transform=`scale(${eb(seg(t,12.9,13.2))})`;$('pl4').style.opacity=seg(t,14.38,14.5);
  place('g',230,690,1.0,false);place('h',380,690,1.0,true);pose('g',t>=12.9?{aL:8,aR:-150,open:1}:{aL:8,aR:-30});pose('h',t>=14.38?{aL:120,aR:-120,open:1}:{aL:8,aR:-8});
  for(let i=0;i<18;i++){const k=seg(t,13.9+i*.03,15.4);const e=$('h4_'+i);e.style.opacity=k>0?1-k*.4:0;const a=i*.35;e.style.left=(290+Math.cos(a)*k*320)+'px';e.style.top=(260+Math.sin(a)*k*260)+'px';}}
'''
