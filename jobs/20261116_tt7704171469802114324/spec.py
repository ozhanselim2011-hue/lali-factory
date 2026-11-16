DUR=16.0
FADE=15.6
START=7.0
SONG='DJ ZUP RAIii — губам'
BG='linear-gradient(180deg,#1a0612,#060205)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Сохни",7.42],["по",8.38],["моим",8.66],["губам",9.2]],
 [["Сохни",11.88],["по",12.84],["моим",13.08],["губам",13.48]],
 [["Сохни",14.94],["по",16.2],["моим",16.52],["губам",16.9]],
 [["Сохни",19.62],["по",20.58],["моим",20.86],["губам",21.24]],
]
SC=[[6.7,11.7],[11.7,14.8],[14.8,19.5],[19.5,99]]
GLOW=['#7a0a2a','#7a1f4a','#5a1d7a','#7a0a2a']
PEMO=['💄','💋','🥵','💘']
END=[22.6,23.0]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:#fff0f4;color:#111">
 <div class="hdr" style="color:#ff2d55">Макияж · губы</div>
 <div id="lp1" style="position:absolute;left:330px;top:120px;width:60px;height:180px;transform-origin:30px 180px"><div style="position:absolute;left:0;bottom:0;width:60px;height:100px;background:linear-gradient(90deg,#c8a24a,#f0d080,#c8a24a);border-radius:6px"></div><div style="position:absolute;left:8px;bottom:100px;width:44px;height:70px;background:#d0021b;border-radius:22px 22px 4px 4px"></div></div>
 <div id="ls1" class="c" style="top:360px;font:900 30px Inter;color:#d0021b;opacity:0">оттенок: «сохни»</div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#000">
 <div class="hdr">Пост · губы 💋</div>
 <div style="position:absolute;left:30px;right:30px;top:80px;height:340px;border-radius:24px;background:linear-gradient(135deg,#ff8ac4,#d0021b);display:flex;align-items:center;justify-content:center;font-size:200px">💋</div>
 <div style="position:absolute;left:30px;top:440px;font:900 30px Inter">❤️ <span id="lk2" class="mono">0</span> · 💬 «сохну»</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:linear-gradient(180deg,#ffb347,#ff6a3a)">
 <div class="hdr" style="color:#fff">Влажность · ты</div>
 <div id="hm3" class="c mono" style="top:100px;font-size:120px;font-weight:900;color:#fff">80%</div>
 <div id="sn3" style="position:absolute;left:400px;top:30px;font-size:110px">☀️</div>
 <div id="dr3" class="c" style="top:280px;font:900 30px Inter;color:#fff;opacity:0">🥵 высыхаешь</div>
 <div class="ch" data-p="c"></div><div class="ch" data-p="g"></div>
</div>
<div class="card" id="c4" style="background:radial-gradient(circle at 50% 40%,#5a0a2a,#14040a)">
 <div id="kk4" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="d"></div><div class="ch" data-p="g2"></div>
 <div id="tx4" class="c" style="top:60px;font:900 44px Inter;color:#ff2d78;opacity:0">засох окончательно 💘</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...(p.startsWith('g')?['#8e8e93','#c8c8cc','#8e8e93']:['#d0021b','#ff8ac4','#ff2d78']));});})();'''
RENDER='''
 {const k=seg(t,7.42,9.2);$('lp1').style.transform=`rotate(${-30+k*30}deg) translate(${-k*120}px,${k*60}px)`;$('ls1').style.opacity=seg(t,9.2,9.3);place('a',200,690,1.1,false);pose('a',{aL:8,aR:t<9.2?-150:-8,hd:-8,open:t>=9.2});
  const m=$('a_mouth');if(m){m.setAttribute('stroke',t>=9.2?'#d0021b':'#7a3a2a');m.setAttribute('stroke-width',t>=9.2?8:4);}}
 {const n=t<11.88?0:Math.round(1e6*eo(seg(t,11.88,13.48)));$('lk2').textContent=fmt(n);place('b',470,690,.75,true);pose('b',{aL:150,aR:-8,open:1});}
 {const k=eo(seg(t,14.94,16.9));$('hm3').textContent=Math.round(lerp(80,2,k))+'%';$('sn3').style.transform=`scale(${1+k*.6}) rotate(${t*30}deg)`;$('dr3').style.opacity=seg(t,16.9,17.0);
  place('c',150,690,.9,false);pose('c',{aL:150,aR:-8,hd:-6});place('g',440,690,lerp(1,.85,k),true);pose('g',{aL:30,aR:-30,hd:20*k,bob:k*20,open:1});$('ch_g').style.filter=`sepia(${k}) saturate(${1+k}) brightness(${1-k*.2})`;}
 {place('d',230,690,1.0,false);pose('d',{aL:8,aR:-8,hd:-10,open:t>=21.24});place('g2',lerp(560,400,eo(seg(t,19.62,20.6))),690,1.0,true);pose('g2',{aL:120,aR:-120,open:1,lL:Math.sin(t*12)*20,lR:-Math.sin(t*12)*20});
  let h='';for(let i=0;i<14;i++){const s=19.8+i*.14;if(t>=s){const p=(t-s)/1.4;h+=`<div style="position:absolute;left:${300+rnd(i)*240}px;top:${420-p*360}px;font-size:${28+rnd(i+2)*24}px;opacity:${1-p}">💋</div>`}}$('kk4').innerHTML=h;$('tx4').style.opacity=seg(t,21.24,21.3);$('tx4').style.transform=`scale(${1+.3*pop(t,21.24,7)})`;}
'''
