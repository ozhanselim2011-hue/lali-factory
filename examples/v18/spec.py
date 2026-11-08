BG='radial-gradient(circle at 50% 40%,#3a3f4a,#101216 75%)'
SUBW='700'
LINES=[
 [["моей",0.0],["юной",0.2],["и",0.9],["страстной,",1.0]],
 [["странной,",1.6],["бесстрашно",2.0],["важной",2.8]],
 [["утончённой",3.5],["и",4.5],["влажной",4.7]],
 [["моей",5.3],["лояльной",5.6]],
 [["испорченной,",7.2],["но",8.0],["не",8.2],["каждой",8.3]],
 [["дорогой,",9.1],["но",9.9],["не",10.1],["жадной",10.2]],
 [["мы",10.8],["снова",11.0],["на",11.3],["расстоянии,",11.7]],
 [["теряем",12.7],["самосознание",13.3]],
]
SC=[[-0.3,3.4],[3.4,5.2],[5.2,7.1],[7.1,9.0],[9.0,10.7],[10.7,99]]
GLOW=['#8a7a9a','#5a7a9a','#9a8a6a','#7a6a8a','#9a7a5a','#7a8a9a']
PEMO=['🤍','💧','💳','🕊️','💎','🌫️']
END=[14.2,14.88]
CSS='.card.lt{background:rgba(245,245,247,.96);color:#111}.lt .hdr{color:rgba(0,0,0,.45)}.chip{display:inline-block;padding:12px 20px;border-radius:22px;background:#fff;box-shadow:0 4px 14px rgba(0,0,0,.08);font-size:26px;font-weight:800;margin:0 8px 12px 0;opacity:0}'
HTML='''
<div class="card lt" id="c1">
 <div style="position:absolute;top:44px;left:50%;margin-left:-80px;width:160px;height:160px;border-radius:50%;background:linear-gradient(135deg,#ffe0ec,#e0d4ff);display:flex;align-items:center;justify-content:center;font-size:90px">👼</div>
 <div class="c" style="top:220px;font-size:42px;font-weight:900">Моя 🤍</div>
 <div class="c" style="top:280px;font-size:20px;color:#8e8e93;font-weight:700">заметки о контакте</div>
 <div id="chips" style="position:absolute;left:34px;right:34px;top:330px"></div>
</div>
<div class="card" id="c2" style="background:linear-gradient(180deg,#9fb6cf,#5a7290)">
 <div style="text-align:center;padding-top:34px"><div style="font-size:32px;font-weight:600">Она</div><div style="font-size:130px;font-weight:200;line-height:1">22°</div><div id="w2" style="font-size:28px;font-weight:600">Туман</div></div>
 <div style="position:absolute;left:30px;right:30px;bottom:30px;display:flex;gap:14px">
  <div style="flex:1;background:rgba(255,255,255,.18);border-radius:24px;padding:20px"><div style="font-size:19px;font-weight:700;opacity:.7">✨ СТИЛЬ</div><div id="ut" style="font-size:30px;font-weight:800;margin-top:6px">—</div></div>
  <div style="flex:1;background:rgba(255,255,255,.18);border-radius:24px;padding:20px"><div style="font-size:19px;font-weight:700;opacity:.7">💧 ВЛАЖНОСТЬ</div><div id="hm" class="mono" style="font-size:40px;font-weight:800;margin-top:6px">0%</div></div></div>
 <div id="drops" style="position:absolute;left:0;right:0;top:240px;height:200px;overflow:hidden"></div>
</div>
<div class="card lt" id="c3">
 <div class="hdr">Wallet</div><div class="ttl" style="color:#111">Карта лояльности</div>
 <div id="lc" style="position:absolute;left:40px;right:40px;top:180px;height:280px;border-radius:30px;background:linear-gradient(135deg,#f5d0e0,#d4c8ff 60%,#c8e8ff);box-shadow:0 20px 50px rgba(0,0,0,.15);padding:28px;overflow:hidden">
  <div style="position:absolute;inset:0;background:linear-gradient(115deg,transparent 30%,rgba(255,255,255,.5) 45%,transparent 60%)" id="sh3"></div>
  <div style="font-size:34px;font-weight:900">МОЯ 🤍</div><div style="font-size:22px;font-weight:700;opacity:.6;margin-top:6px">участник с 2024</div>
  <div style="position:absolute;left:28px;bottom:26px;font-size:22px;font-weight:700;opacity:.6">уровень</div><div id="lv" style="position:absolute;right:28px;bottom:20px;font-size:36px;font-weight:900">—</div></div>
</div>
<div class="card lt" id="c4">
 <div class="hdr">Фото</div><div class="ttl" style="color:#111">Она · 10 фото</div>
 <div id="pg" style="position:absolute;left:30px;right:30px;top:170px;display:grid;grid-template-columns:repeat(4,1fr);gap:8px"></div>
 <div id="t4" class="c" style="bottom:40px;font-size:26px;font-weight:800;color:#ff453a;opacity:0">повреждено: 1 из 10 · но не каждая</div>
</div>
<div class="card lt" id="c5">
 <div class="hdr">App Store</div>
 <div style="display:flex;gap:24px;padding:20px 40px 0;align-items:center"><div style="width:150px;height:150px;border-radius:36px;background:linear-gradient(135deg,#ffd6e8,#cfc4ff);display:flex;align-items:center;justify-content:center;font-size:80px">💎</div>
  <div><div style="font-size:36px;font-weight:900">Она</div><div style="font-size:20px;color:#8e8e93;font-weight:600">эксклюзив</div><div id="pr5" style="margin-top:12px;display:inline-block;padding:8px 22px;border-radius:20px;background:#0a84ff;color:#fff;font-size:24px;font-weight:900">—</div></div></div>
 <div style="position:absolute;left:30px;right:30px;top:300px;background:#fff;border-radius:24px;padding:0 24px;box-shadow:0 4px 14px rgba(0,0,0,.06)">
  <div style="display:flex;justify-content:space-between;padding:22px 0;border-bottom:1px solid #eee;font-size:24px;font-weight:700"><span>Цена</span><span id="pc5" style="color:#8e8e93">—</span></div>
  <div style="display:flex;justify-content:space-between;align-items:center;padding:18px 0;font-size:24px;font-weight:700"><span>Семейный доступ</span><div class="tg" id="tg5"><b></b></div></div></div>
 <div id="ng" class="c" style="bottom:40px;font-size:28px;font-weight:900;color:#30d158;opacity:0">дорогая, но не жадная 🤍</div>
</div>
<div class="card" id="c6" style="background:#e9ecf1;color:#111">
 <div id="map6" style="position:absolute;left:0;right:0;top:0;height:420px;background:#dfe4ea;overflow:hidden">
  <svg width="600" height="420" style="position:absolute;inset:0"><path id="ln6" stroke="#5e5ce6" stroke-width="5" stroke-dasharray="10 10" fill="none"/></svg>
  <div id="pa6" style="position:absolute;width:80px;height:80px;margin:-40px;border-radius:50%;background:#fff;box-shadow:0 6px 20px rgba(0,0,0,.2);display:flex;align-items:center;justify-content:center;font-size:44px">👼</div>
  <div id="pb6" style="position:absolute;width:80px;height:80px;margin:-40px;border-radius:50%;background:#fff;box-shadow:0 6px 20px rgba(0,0,0,.2);display:flex;align-items:center;justify-content:center;font-size:44px">🧍</div></div>
 <div style="position:absolute;left:0;right:0;top:440px;padding:0 34px"><div style="font-size:32px;font-weight:900">Моя</div><div id="ds6" class="mono" style="font-size:26px;font-weight:700;color:#5e5ce6;margin-top:6px">рядом</div>
  <div style="margin-top:18px;font-size:20px;font-weight:700;color:#8e8e93">самосознание</div><div style="height:14px;border-radius:7px;background:#d1d1d6;margin-top:8px;overflow:hidden"><div id="sc6" style="height:14px;background:#5e5ce6;width:100%"></div></div></div>
 <div id="fog" style="position:absolute;inset:0;background:radial-gradient(circle,rgba(255,255,255,.2),rgba(255,255,255,.95));opacity:0"></div>
</div>
'''
BUILD='''(function(){const C=['юная','страстная 🔥','странная 🌀','бесстрашная','важная ⭐'];$('chips').innerHTML=C.map((c,i)=>`<span class="chip" id="ch${i}">${c}</span>`).join('');
 let d='';for(let i=0;i<16;i++)d+=`<div id="dr${i}" style="position:absolute;left:${20+rnd(i)*540}px;font-size:${22+rnd(i+3)*20}px">💧</div>`;$('drops').innerHTML=d;
 let g='';for(let i=0;i<10;i++)g+=`<div id="pg${i}" style="aspect-ratio:1;border-radius:12px;background:linear-gradient(135deg,hsl(${300+i*12},40%,85%),hsl(${220+i*9},40%,80%));display:flex;align-items:center;justify-content:center;font-size:48px">${['🤍','🕊️','🌸','✨','🤍','🌫️','💐','🕊️','🌸','✨'][i]}</div>`;$('pg').innerHTML=g;})();'''
RENDER='''
 {[0.2,1.0,1.6,2.0,2.8].forEach((s,i)=>{const e=$('ch'+i);e.style.opacity=seg(t,s,s+.1);e.style.transform=`scale(${eb(seg(t,s,s+.25))})`;e.style.background=i==4&&t>=2.8?'#ffd60a':'#fff';});}
 {$('ut').textContent=t>=3.5?'утончённо':'—';$('ut').style.transform=`scale(${1+.15*pop(t,3.5,6)})`;const h=t<4.7?seg(t,3.6,4.7)*60:lerp(60,100,eo(seg(t,4.7,5.0)));$('hm').textContent=Math.round(h)+'%';
  for(let i=0;i<16;i++){const ph=((t-4.5)*.8+rnd(i+9))%1;$('dr'+i).style.top=(-30+ph*230)+'px';$('dr'+i).style.opacity=t>=4.7?.8:0;}$('w2').textContent=t>=4.7?'Влажно':'Туман';}
 {$('sh3').style.transform=`translateX(${lerp(-500,500,(t*.7)%1)}px)`;const l=t>=5.6;$('lv').textContent=l?'лояльная ✓':'—';$('lc').style.transform=`rotate(${Math.sin(t*2)*3}deg) scale(${1+.05*pop(t,5.6,5)})`;}
 {const b=t>=7.2;const e=$('pg6');e.textContent=b?'⚠️':'🌫️';e.style.filter=b?`hue-rotate(${Math.sin(t*30)*90}deg) contrast(2)`:'none';e.style.transform=`translateX(${b?Math.sin(t*60)*4:0}px)`;
  for(let i=0;i<10;i++)if(i!=6)$('pg'+i).style.boxShadow=t>=8.3?'0 0 0 4px #30d158':'none';$('t4').style.opacity=seg(t,8.3,8.45);}
 {const d=t>=9.1;$('pr5').textContent=d?'∞ ₽':'—';$('pc5').textContent=d?'дорогая 💎':'—';$('pc5').style.color=d?'#111':'#8e8e93';$('pr5').style.transform=`scale(${1+.25*pop(t,9.1,6)})`;tog('tg5',t>=10.2);$('ng').style.opacity=seg(t,10.2,10.35);}
 {const p=eo(seg(t,11.0,12.5));const ax=lerp(260,90,p),ay=lerp(200,90,p),bx=lerp(340,510,p),by=lerp(220,330,p);$('pa6').style.left=ax+'px';$('pa6').style.top=ay+'px';$('pb6').style.left=bx+'px';$('pb6').style.top=by+'px';
  $('ln6').setAttribute('d',`M${ax} ${ay} L${bx} ${by}`);$('ds6').textContent=t<11.0?'рядом':fmt(lerp(0,2340,p))+' км · снова';
  const c=t<12.7?100:lerp(100,0,eo(seg(t,12.7,14.0)));$('sc6').style.width=c+'%';$('fog').style.opacity=seg(t,13.0,14.4)*.95;if(si==5)$('c6').style.filter+=` blur(${seg(t,13.3,14.4)*6}px)`;}
'''
