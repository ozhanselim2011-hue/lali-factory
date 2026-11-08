BG='linear-gradient(180deg,#0c1222,#04060c)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["а",0.0],["снег",0.1],["идёт,",0.9],["а",1.4],["снег",1.6],["идёт",2.5]],
 [["по",3.3],["щекам",4.4],["мне",5.2],["бьёт-",5.6],["бьёт",7.0]],
 [["болею",7.7],["очень,",8.6],["температура",9.3]],
 [["стою",11.3],["и",12.7],["жду",12.8],["тебя,",13.0],["как",13.6],["дура",14.0]],
 [["снежинки",14.8],["ртом",17.3],["ловила",17.8]],
 [["очень",19.0],["мило",20.7]],
 [["клёвый",21.6],["вечер,",22.6],["делать",23.4],["нечего",24.1]],
 [["там,",25.0],["где",25.6],["нет",26.0],["тебя",26.3]],
]
SC=[[-0.3,3.2],[3.2,7.6],[7.6,11.2],[11.2,14.7],[14.7,21.4],[21.4,24.9],[24.9,99]]
GLOW=['#1d3a6a','#2a4a6a','#6a1a1a','#2a2a4a','#1d4a6a','#3a2a4a','#1a1a2a']
PEMO=['❄️','🌬️','🤒','⏳','❄️','🌙','📍']
END=[26.9,27.4]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}.sn{position:absolute;color:#fff;font-size:22px}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#3a4a6a,#141a2a)">
 <div style="padding:30px 36px 0"><div style="font-size:28px;font-weight:600">Мой город</div><div style="font-size:96px;font-weight:200;line-height:1">−7°</div><div id="w1" style="font-size:24px;font-weight:600">Облачно</div></div>
 <div class="ch" data-p="a"></div>
 <div id="drift1" style="position:absolute;left:0;right:0;bottom:0;height:0;background:#e8eef8;border-radius:50% 50% 0 0/30px 30px 0 0"></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#24344e,#0c121e)">
 <div class="hdr">Погода · Ветер</div>
 <div class="c" style="top:80px"><div id="wd2" class="mono" style="font-size:80px;font-weight:800">0 м/с</div><div style="font-size:24px;font-weight:700;color:#9ad8ff">порывы · прямо в щёки</div></div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#1c1c1e">
 <div class="hdr" style="color:#ff375f">❤ Здоровье</div><div class="ttl">Температура</div>
 <div id="tp3" class="mono" style="position:absolute;right:40px;top:80px;font-size:64px;font-weight:800">36.6°</div>
 <div class="ch" data-p="c"></div>
 <div id="sk3" style="position:absolute;left:30px;right:30px;bottom:30px;background:#3a0d12;border-radius:22px;padding:16px 22px;font-size:24px;font-weight:900;color:#ff453a;opacity:0">🤒 болею очень</div>
</div>
<div class="card" id="c4" style="background:linear-gradient(180deg,#1a2238,#080a12)">
 <div style="position:absolute;left:24px;right:24px;top:24px;background:rgba(30,30,32,.94);border-radius:24px;padding:16px 22px;display:flex;gap:16px;align-items:center">
  <div style="width:60px;height:60px;border-radius:50%;background:linear-gradient(135deg,#ff8ac4,#ff2d78);display:flex;align-items:center;justify-content:center;font-size:30px">😎</div>
  <div><div style="font-size:26px;font-weight:900">Он</div><div style="font-size:20px;color:#8e8e93;font-weight:600">не в пути · 2,3 км</div></div><div id="wt4" class="mono" style="margin-left:auto;font-size:30px;font-weight:800;color:#ff9f0a">0:00</div></div>
 <div class="ch" data-p="d"></div>
 <div id="cap4" style="position:absolute;width:0;height:0;border-radius:50% 50% 30% 30%;background:#f2f6ff;z-index:7;box-shadow:0 4px 10px rgba(0,0,0,.3)"></div>
 <div id="dr4" class="c" style="top:140px;font-size:26px;font-weight:900;color:#ff9ac1;opacity:0">стою как дура 🙃</div>
</div>
<div class="card" id="c5" style="background:radial-gradient(circle at 50% 30%,#2a3a5a,#0a0e18)">
 <div class="hdr">Счётчик</div>
 <div id="ct5" class="c mono" style="top:70px;font-size:60px;font-weight:800">❄️ 0</div>
 <div class="ch" data-p="e"></div>
 <div id="mi5" class="c" style="bottom:28px;font-size:32px;font-weight:900;color:#ff9ac1;opacity:0">очень мило 🥹</div>
</div>
<div class="card" id="c6" style="background:#1c1c1e">
 <div class="hdr" style="color:#ff9f0a">Напоминания</div><div class="ttl">Планы на вечер</div>
 <div class="c" style="top:170px;font-size:28px;font-weight:700;color:#636366">нет напоминаний</div>
 <div class="ch" data-p="f"></div>
</div>
<div class="card" id="c7" style="background:#dfe4ea;color:#111">
 <div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 45%,#eef2f6,#c8d0da)"></div>
 <div class="ch" data-p="g"></div>
 <div id="gh7" style="position:absolute;left:390px;top:300px;width:110px;height:110px;border-radius:50%;border:5px dashed #8e8e93;display:flex;align-items:center;justify-content:center;font-size:30px;color:#8e8e93;font-weight:900">?</div>
 <div style="position:absolute;left:24px;right:24px;bottom:24px;background:#fff;border-radius:26px;padding:18px 24px"><div style="font-size:28px;font-weight:900">Он</div><div id="nl7" style="font-size:22px;color:#8e8e93;font-weight:700">поиск…</div></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
const GIRL=['#ff9ac1','#f3e8ff','#b38cff'];
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...GIRL);});
 document.querySelectorAll('.card').forEach((c,ci)=>{let s='';for(let i=0;i<26;i++)s+=`<div class="sn" data-i="${i}">❄</div>`;const d=document.createElement('div');d.className='snw';d.style.cssText='position:absolute;inset:0;pointer-events:none;z-index:6';d.innerHTML=s;c.appendChild(d);});})();
function snow(t,wind,speed){document.querySelectorAll('.snw .sn').forEach(e=>{const i=+e.dataset.i;const ph=(t*speed*(.2+rnd(i)*.2)+rnd(i+30))%1;e.style.top=(-20+ph*720)+'px';e.style.left=(((rnd(i+3)*640+ph*wind*400)%640)-20)+'px';e.style.opacity=.5+rnd(i)*.5;e.style.fontSize=(14+rnd(i+8)*20)+'px';});}
'''
RENDER='''
 snow(t,si==1?1.4:.15,si==1?2.4:1);
 {$('w1').textContent=t>=0.9?'Снег идёт ❄️':'Облачно';$('drift1').style.height=(seg(t,0,3.2)*60)+'px';place('a',300,650,1.2,false);pose('a',t>=0.9?{aL:80,aR:-80,hd:-14,open:1}:{aL:8,aR:-8,hd:-6});}
 {const w=Math.round(lerp(0,25,seg(t,3.3,5.6)));$('wd2').textContent=w+' м/с';const h=Math.max(pop(t,5.6,8),pop(t,7.0,8));place('b',300+Math.sin(t*30)*4*(t>=4.4?1:0),660,1.2,false,-6*(t>=4.4?1:0));
  pose('b',t>=4.4?{aL:-150,aR:150,hd:12+h*10}:{aL:8,aR:-8});}
 {const tp=t<9.3?lerp(36.6,38.2,seg(t,7.7,9.3)):lerp(38.2,39.4,eo(seg(t,9.3,10.2)));$('tp3').textContent=tp.toFixed(1)+'°';$('tp3').style.color=tp>37.5?'#ff453a':'#fff';
  place('c',300,660,1.2,false);pose('c',{aL:-40,aR:40,hd:16,bob:4+Math.sin(t*30)*2});$('sk3').style.opacity=seg(t,8.6,8.75);}
 {const m=Math.floor(seg(t,11.3,14.6)*107);$('wt4').textContent=Math.floor(m/60)+':'+String(m%60).padStart(2,'0');place('d',300,660,1.2,false);pose('d',t>=14.0?{aL:55,aR:-55,hd:14,open:1}:{aL:8,aR:-8,hd:6});
  const c=seg(t,11.3,14.6);const cw=lerp(0,96,c),ch=lerp(0,40,c);$('cap4').style.width=cw+'px';$('cap4').style.height=ch+'px';$('cap4').style.left=(300-cw/2)+'px';$('cap4').style.top=(352-ch)+'px';$('dr4').style.opacity=seg(t,14.0,14.15);}
 {const n=t<17.3?0:Math.floor(seg(t,17.3,20.7)*27);$('ct5').textContent='❄️ поймано: '+n;place('e',300,660,1.25,false);
  pose('e',t>=20.7?{aL:-58,aR:58,hd:6}:{aL:20,aR:-20,hd:-22+Math.sin(t*4)*6,open:t>=17.3&&Math.sin(t*8)>-0.3,bob:-Math.abs(Math.sin(t*3))*8*(t>=17.3?1:0)});$('mi5').style.opacity=seg(t,20.7,20.85);}
 {const q=Math.sin(t*3);place('f',300,660,1.2,false);pose('f',t>=24.1?{aL:55,aR:-55,hd:12,open:1}:{aL:q*20,aR:q*20,lL:q*8,lR:-q*8,hd:q*6,bob:-Math.abs(q)*4});}
 {place('g',220,560,1.0,false);pose('g',t>=26.0?{aL:2,aR:-2,hd:20,bob:6}:{aL:8,aR:-95});$('nl7').textContent=t>=26.0?'нет геопозиции · там, где нет тебя':'поиск…';$('gh7').style.opacity=t>=26.0?.4:1;}
'''
