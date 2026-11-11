DUR=20.2
FADE=19.8
START=0
SONG='Antoha MC — Лишь тень (из сериала «Айда!»)'
BG='linear-gradient(180deg,#0a0a14,#030306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["И",0.0],["ушли",0.1],["ко",1.74],["дну",2.18],["все",2.62],["детские",3.24],["мечты",4.1]],
 [["и",6.86],["всё-таки",8.06],["я",9.22],["верю,",9.78]],
 [["настанет",10.94],["новый",12.32],["день",12.84]],
 [["найдутся",13.38],["к",15.66],["свету",15.74],["двери,",16.54]],
 [["а",17.56],["прошлое",18.36],["лишь",19.3],["тень",19.64]],
]
SC=[[-0.3,6.8],[6.8,10.88],[10.88,13.32],[13.32,17.5],[17.5,99]]
GLOW=['#1a2a5a','#7a5a1a','#7a6a1a','#5a5a3a','#3a3a3a']
PEMO=['⛵','🕯️','🌅','🚪','👤']
END=[19.8,20.2]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#5aa8e8 0,#5aa8e8 40%,#1a4a8a 40%,#05142a)">
 <div id="bt1" style="position:absolute;left:0;right:0;top:0;height:690px"></div>
 <div id="bb1" style="position:absolute;inset:0"></div>
</div>
<div class="card" id="c2" style="background:radial-gradient(circle at 50% 45%,#5a3a10,#0a0602)">
 <div id="cd2" class="c" style="top:120px;font-size:120px">🕯️</div>
 <div class="c" style="top:300px;font-size:28px;font-weight:900;color:#ffd60a">вера: <span id="vr2" class="mono">0%</span></div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c3" style="background:#f2f2f7;color:#111">
 <div style="position:absolute;left:150px;top:80px;width:300px;height:300px;border-radius:24px;background:#fff;box-shadow:0 10px 30px rgba(0,0,0,.15);overflow:hidden">
  <div style="height:70px;background:#ff453a;color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:900">НОВЫЙ ДЕНЬ</div>
  <div id="dn3" class="c mono" style="top:100px;font-size:120px;font-weight:900">1</div></div>
 <div id="sn3" style="position:absolute;left:230px;top:620px;font-size:140px">🌅</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c4" style="background:#050505">
 <div id="dr4" style="position:absolute;left:220px;top:150px;width:160px;height:320px;background:#fff7c2;box-shadow:0 0 0 #fff7c2;transform-origin:left center"></div>
 <div id="lt4" style="position:absolute;left:100px;top:470px;width:400px;height:220px;background:linear-gradient(180deg,rgba(255,247,194,.6),transparent);clip-path:polygon(30% 0,70% 0,100% 100%,0 100%);opacity:0"></div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c5" style="background:linear-gradient(180deg,#fff7c2,#ffd36b)">
 <div id="sh5" style="position:absolute;left:130px;top:560px;width:300px;height:60px;border-radius:50%;background:rgba(0,0,0,.6);filter:blur(6px);transform-origin:left center"></div>
 <div class="ch" data-p="d"></div>
 <div id="tx5" class="c" style="top:60px;font-size:30px;font-weight:900;color:#3a2a00;opacity:0">прошлое → 👤 лишь тень</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 $('bt1').innerHTML=['🚀 космонавт','⚽ футболист','🦸 супергерой'].map((s,i)=>`<div id="p1_${i}" style="position:absolute;left:${40+i*180}px;top:200px;text-align:center"><div style="font-size:90px">⛵</div><div style="background:#fff;color:#111;border-radius:10px;padding:4px 8px;font-size:18px;font-weight:900">${s}</div></div>`).join('');
 let b='';for(let i=0;i<14;i++)b+=`<div id="q1_${i}" style="position:absolute;width:${10+i%3*8}px;height:${10+i%3*8}px;border-radius:50%;border:2px solid rgba(255,255,255,.7)"></div>`;$('bb1').innerHTML=b;})();
'''
RENDER='''
 {for(let i=0;i<3;i++){const s=1.74+i*.6;const k=eo(seg(t,s,s+2.2));$('p1_'+i).style.top=lerp(200,600,k)+'px';$('p1_'+i).style.opacity=1-seg(t,s+1.8,s+2.6);$('p1_'+i).style.transform=`rotate(${k*30*(i%2?1:-1)}deg)`;}
  for(let i=0;i<14;i++){const ph=(t*.7+i/14)%1;$('q1_'+i).style.left=(60+rnd(i)*480)+'px';$('q1_'+i).style.top=(680-ph*400)+'px';$('q1_'+i).style.opacity=t>2?(1-ph):0;}}
 {const v=Math.round(eo(seg(t,8.0,9.8))*100);$('vr2').textContent=v+'%';$('cd2').style.transform=`scale(${1+v/200+.05*Math.sin(t*14)})`;$('cd2').style.filter=`drop-shadow(0 0 ${v/2}px #ffd60a)`;
  place('a',300,700,1.0,false);pose('a',t>=9.78?{aL:8,aR:-110,hd:-8}:{aL:8,aR:-8,hd:-10});}
 {const k=eo(seg(t,11.0,12.9));$('sn3').style.top=lerp(620,400,k)+'px';$('dn3').textContent=t>=12.84?'✨':'1';place('b',120,700,.8,false);pose('b',t>=12.84?{aL:150,aR:-150,open:1}:{aL:8,aR:-8});}
 {const o=eo(seg(t,15.74,16.6));$('dr4').style.transform=`perspective(500px) rotateY(${-o*70}deg)`;$('dr4').style.background=o>0?'#fff7c2':'#3a2410';$('dr4').style.boxShadow=`0 0 ${o*120}px #fff7c2`;$('lt4').style.opacity=o;
  const w=eo(seg(t,16.54,17.5));place('c',lerp(120,280,w),690,.9,false);pose('c',w>0&&w<1?walk(t,10):{aL:8,aR:-8,hd:-6});}
 {const f=seg(t,18.36,19.9);$('sh5').style.opacity=1-f;$('sh5').style.transform=`scaleX(${1-f*.6})`;$('tx5').style.opacity=seg(t,19.64,19.74);place('d',lerp(240,330,seg(t,17.6,19.6)),690,1.0,false);pose('d',walk(t,8));}
'''
