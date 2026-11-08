DUR=14.0
FADE=13.6
START=0
SONG=''
BG='linear-gradient(180deg,#0c0a14,#040306)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Гадкие",0.4],["мальчишки,",1.28],["они",2.44],["не",2.9],["понимают",3.14]],
 [["они",4.26],["все",4.68],["как",4.94],["глупышки",5.18]],
 [["готовы",6.22],["дать",6.7],["всё,",7.18],["чтобы",7.56],["с",7.86],["тобой",8.06]],
 [["да",8.52],["ты",8.68],["со",8.9],["мною",9.1]],
 [["порублю",10.04],["кабину",10.86]],
 [["я",11.52],["потом",11.74],["всё",12.12],["это",12.48],["смою",12.98]],
]
SC=[[-0.3,4.15],[4.15,6.1],[6.1,8.4],[8.4,9.9],[9.9,11.4],[11.4,99]]
GLOW=['#2a4a7a','#7a6a1a','#1a5c2e','#7a1f4a','#7a3a1a','#1a5a7a']
PEMO=['🙄','🤪','💸','💘','🪓','🧽']
END=[13.6,14.0]
CSS='''.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}
.bub{position:absolute;max-width:380px;border-radius:24px;padding:12px 18px;font-size:26px;font-weight:700;opacity:0}
.me{right:24px;background:#0a84ff}.th{left:24px;background:#2c2c2e}'''
HTML='''
<div class="card" id="c1" style="background:#000">
 <div class="hdr">Чат · «мальчишки 🙄»</div><div class="ttl" style="font-size:38px">3 участника</div>
 <div class="bub me" id="b1a" style="top:150px">я обиделась.</div>
 <div class="bub th" id="b1b" style="top:225px">ок 👍</div>
 <div class="bub th" id="b1c" style="top:295px">а на что? 🤨</div>
 <div class="bub th" id="b1d" style="top:365px">го в доту</div>
 <div class="ch" data-p="a"></div>
 <div id="q1" style="position:absolute;left:330px;top:420px;font-size:80px;opacity:0;z-index:6">🤦</div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#fff7c2,#ffd84d);color:#111">
 <div class="hdr" style="color:rgba(0,0,0,.5)">Тест «Понимает намёки»</div><div class="ttl">Результаты</div>
 <div id="rw2" style="position:absolute;left:30px;right:30px;top:150px"></div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#0d1a12">
 <div class="hdr" style="color:#30d158">Банк · Перевод</div>
 <div class="c mono" id="bal3" style="top:100px;font-size:64px;font-weight:800">250 000 ₽</div>
 <div class="c" style="top:185px;font-size:22px;color:#8e8e93;font-weight:700">получатель: она 💖 · «чтобы с тобой»</div>
 <div id="bt3" style="position:absolute;left:60px;right:60px;top:240px;height:76px;border-radius:38px;background:#30d158;color:#000;font-size:30px;font-weight:900;display:flex;align-items:center;justify-content:center">Перевести ВСЁ</div>
 <div id="ok3" class="c" style="top:340px;font-size:30px;font-weight:900;color:#30d158;opacity:0">✅ отправлено</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:radial-gradient(circle at 50% 40%,#ff4f8b,#5a0b2a)">
 <div class="c" id="m4" style="top:60px;font-size:64px;font-weight:900;font-style:italic;opacity:0">It’s a match!</div>
 <div class="c" id="s4" style="top:150px;font-size:24px;font-weight:700;opacity:0">статус: ты со мною 💍</div>
 <div class="ch" data-p="d"></div><div class="ch" data-p="e"></div>
 <div id="h4" style="position:absolute;left:250px;top:260px;font-size:100px;opacity:0;z-index:6">💘</div>
</div>
<div class="card" id="c5" style="background:linear-gradient(180deg,#2b1a10,#120a05)">
 <div class="hdr" style="color:#ffb340">Кабина · прочность</div>
 <div style="position:absolute;left:40px;right:40px;top:76px;height:20px;border-radius:10px;background:#3a2412;overflow:hidden"><div id="hp5" style="height:20px;background:#ff453a;width:100%"></div></div>
 <div id="cb5" style="position:absolute;left:300px;top:200px;width:220px;height:300px;background:#8a5a32;border:8px solid #5a3a1a;border-radius:14px 14px 0 0;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:900;color:#ffe2b8;z-index:4">КАБИНА</div>
 <div id="pc5" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="f"></div>
 <div id="ax5" style="position:absolute;font-size:90px;z-index:7">🪓</div>
</div>
<div class="card" id="c6" style="background:linear-gradient(180deg,#bfefff,#5ac8fa);color:#06243a">
 <div class="hdr" style="color:rgba(0,0,0,.5)">Уборка улик</div><div class="ttl">Очистка <span id="pr6" class="mono">0%</span></div>
 <div style="position:absolute;left:40px;right:40px;top:150px;height:20px;border-radius:10px;background:rgba(255,255,255,.5);overflow:hidden"><div id="pb6" style="height:20px;background:#0a84ff;width:0"></div></div>
 <div id="dt6" style="position:absolute;inset:0"></div>
 <div id="bb6" style="position:absolute;inset:0;z-index:6"></div>
 <div class="ch" data-p="g"></div>
 <div id="mp6" style="position:absolute;font-size:80px;z-index:7">🧽</div>
 <div id="dn6" class="c" style="top:200px;font-size:34px;font-weight:900;opacity:0;z-index:8">✨ как будто ничего не было</div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#64d2ff','#ff8ac4','#ff2d78');});
 const R=[['Петя','#ff453a'],['Ваня','#ff9f0a'],['Саша','#ff453a']];
 $('rw2').innerHTML=R.map((r,i)=>`<div style="display:flex;align-items:center;gap:12px;margin-bottom:22px;font-size:28px;font-weight:900"><span style="width:150px;white-space:nowrap">🧢 ${r[0]}</span><div style="flex:1;height:26px;border-radius:13px;background:rgba(0,0,0,.12);overflow:hidden"><div id="r2_${i}" style="height:26px;background:${r[1]};width:100%"></div></div><span id="v2_${i}" class="mono" style="width:90px;text-align:right">100</span></div>`).join('');
 let p='';for(let i=0;i<8;i++)p+=`<div id="p5_${i}" style="position:absolute;width:40px;height:22px;background:#8a5a32;border:3px solid #5a3a1a;opacity:0"></div>`;$('pc5').innerHTML=p;
 let d='';for(let i=0;i<10;i++)d+=`<div id="d6_${i}" style="position:absolute;left:${40+rnd(i)*500}px;top:${260+rnd(i+3)*360}px;width:${40+rnd(i+1)*40}px;height:${26+rnd(i+2)*20}px;border-radius:50%;background:#6b4a2a"></div>`;$('dt6').innerHTML=d;
 let b='';for(let i=0;i<14;i++)b+=`<div id="o6_${i}" style="position:absolute;width:${16+i%3*10}px;height:${16+i%3*10}px;border-radius:50%;border:3px solid #fff;opacity:0"></div>`;$('bb6').innerHTML=b;})();
'''
RENDER='''
 {['b1a','b1b','b1c','b1d'].forEach((id,i)=>{const s=[0.3,1.3,2.4,3.1][i];$(id).style.opacity=seg(t,s,s+.12);$(id).style.transform=`scale(${eb(seg(t,s,s+.25))})`;});
  place('a',190,680,.95,false);const fp=t>=3.14;pose('a',fp?{aL:8,aR:-150,hd:14}:{aL:8,aR:-8,hd:-6});$('q1').style.opacity=seg(t,3.14,3.3);$('q1').style.transform=`scale(${1+.3*pop(t,3.14,6)})`;}
 {for(let i=0;i<3;i++){const s=4.3+i*.35,v=eo(seg(t,s,s+.5));const val=Math.round(lerp(100,[2,0,1][i],v));$('r2_'+i).style.width=val+'%';$('v2_'+i).textContent=val;}
  place('b',300,690,1.15,false);pose('b',t>=5.18?{aL:60,aR:-60,hd:Math.sin(t*14)*12,open:1}:{aL:8,aR:-8});}
 {const pr=t>=7.18;const v=eo(seg(t,7.2,7.9));$('bal3').textContent=fmt(250000*(1-v))+' ₽';$('bal3').style.color=v>.9?'#ff453a':'#fff';
  $('bt3').style.transform=`scale(${1-.08*pop(t,7.18,10)})`;$('ok3').style.opacity=seg(t,7.9,8.0);
  place('c',300,690,1.1,false);pose('c',pr?{aL:8,aR:-150,hd:-8,open:t>7.9?1:0}:{aL:8,aR:-60});}
 {const m=eo(seg(t,8.5,8.9));place('d',lerp(60,230,m),680,1.0,false);place('e',lerp(540,370,m),680,1.0,true);
  pose('d',t>=9.1?{aL:8,aR:-80,open:1}:{aL:8,aR:-30});pose('e',t>=9.1?{aL:8,aR:-80,open:1}:{aL:8,aR:-30});
  $('m4').style.opacity=seg(t,8.52,8.65);$('m4').style.transform=`scale(${eb(seg(t,8.52,8.8))})`;$('s4').style.opacity=seg(t,9.1,9.25);
  $('h4').style.opacity=seg(t,8.9,9.0);$('h4').style.transform=`scale(${1+.15*Math.sin(t*12)})`;}
 {const hits=[10.04,10.5,10.86];let h=0;hits.forEach(s=>{if(t>=s)h++;});$('hp5').style.width=Math.max(0,100-h*34)+'%';
  const sw=hits.reduce((a,s)=>a+pop(t,s,9),0);const up=Math.min(1,sw);
  place('f',170,690,1.1,false);pose('f',{aL:8,aR:lerp(-160,-40,up),hd:-6,open:h>0?1:0});
  $('ax5').style.left=(lerp(150,250,up))+'px';$('ax5').style.top=(lerp(240,380,up))+'px';$('ax5').style.transform=`rotate(${lerp(-60,40,up)}deg)`;
  const br=t>=10.86;$('cb5').style.transform=`rotate(${Math.sin(t*40)*3*sw}deg) translateY(${br?eo(seg(t,10.86,11.2))*120:0}px) scaleY(${br?1-.6*eo(seg(t,10.86,11.2)):1})`;
  for(let i=0;i<8;i++){const e=$('p5_'+i);const k=seg(t,10.86,11.4);e.style.opacity=br?1-k*.3:0;const a=i*.8-1.2;e.style.left=(400+Math.cos(a)*k*260)+'px';e.style.top=(330-Math.sin(a)*k*220+k*k*200)+'px';e.style.transform=`rotate(${k*400+i*40}deg)`;}}
 {const c=eo(seg(t,11.6,13.1));$('pr6').textContent=Math.round(c*100)+'%';$('pb6').style.width=(c*100)+'%';
  for(let i=0;i<10;i++)$('d6_'+i).style.opacity=1-seg(t,11.6+i*.14,11.9+i*.14);
  const mx=300+Math.sin(t*9)*180,my=470+Math.cos(t*5)*120;$('mp6').style.left=mx+'px';$('mp6').style.top=my+'px';
  for(let i=0;i<14;i++){const e=$('o6_'+i);const ph=(t*1.5+i*.37)%1;e.style.opacity=t>11.6&&t<13.3?1-ph:0;e.style.left=(60+rnd(i+9)*480)+'px';e.style.top=(620-ph*400)+'px';}
  place('g',150,690,1.0,false);pose('g',{aL:8,aR:-110+Math.sin(t*9)*25,hd:-6,open:t>=12.98?1:0});$('dn6').style.opacity=seg(t,12.98,13.15);}
'''
