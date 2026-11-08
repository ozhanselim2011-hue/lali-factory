# Татьяна Буланова — Я больше не любовь (TikTok-тренд): контакт переименован, нужность 0%, перекрёсток, звонок покинул
DUR=15.8; FADE=15.4; START=43.9
SONG='Татьяна Буланова — Я больше не любовь'
BG='linear-gradient(180deg,#160a12,#050205)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[[["я", 44.28],
 ["больше", 46.2],
 ["не", 46.68],
 ["любовь,", 47.1]],
 [["я", 48.8],
 ["больше", 50.16],
 ["не", 50.66],
 ["нужна.", 51.04]],
 [["на", 52.58],
 ["перекрёстке", 54.1],
 ["двух", 55.16],
 ["дорог", 55.38]],
 [["осталась", 56.28],
 ["я", 57.78],
 ["одна.", 58.48]]]
SC=[[43.6, 48.6], [48.6, 52.4], [52.4, 56.1], [56.1, 99]]
GLOW=['#7a1f4a','#5a2a2a','#3a3a5a','#2a2a3a']
PEMO=['💔','🔋','🛣️','😔']
END=[59.3, 59.7]
CSS='''.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'''
HTML='''
<div class="card" id="c1" style="background:#0e1621">
 <div style="position:absolute;left:0;right:0;top:0;height:86px;background:#17212b;display:flex;align-items:center;gap:16px;padding:0 26px;font-size:28px;font-weight:800"><span style="color:#64b5ef">‹</span><div style="width:54px;height:54px;border-radius:50%;background:#ff2d78;display:flex;align-items:center;justify-content:center;font-size:30px">❤️</div><span id="nm1">Любовь ❤️</span></div>
 <div style="position:absolute;left:24px;top:130px;background:#182533;border-radius:22px;padding:14px 20px;font-size:26px;font-weight:600">привет, любимая 😘</div>
 <div id="nt1" style="position:absolute;left:24px;right:24px;top:240px;background:rgba(255,45,120,.15);border:3px solid #ff2d78;border-radius:20px;padding:14px 18px;font-size:26px;font-weight:900;opacity:0">✏️ контакт переименован</div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#1c1c1e">
 <div class="hdr">Батарея · нужность</div><div class="ttl" id="pc2">100%</div>
 <div style="position:absolute;left:60px;top:170px;width:480px;height:130px;border-radius:30px;border:8px solid #fff;padding:8px"><div id="bt2" style="height:100%;border-radius:18px;background:#30d158;width:100%"></div></div>
 <div id="al2" style="position:absolute;left:40px;right:40px;top:330px;background:#3a0d12;border-radius:20px;padding:14px 18px;font-size:26px;font-weight:900;color:#ff453a;opacity:0">🪫 «нужна» разряжено</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:linear-gradient(180deg,#8ec5ff,#cfe8ff 50%,#6a6a6a 50%)">
 <div style="position:absolute;left:290px;top:210px;width:20px;height:320px;background:#555"></div>
 <div style="position:absolute;left:60px;top:230px;background:#2e7d32;color:#fff;border-radius:12px;padding:8px 16px;font-size:26px;font-weight:900;transform:rotate(-6deg)">← к нему</div>
 <div style="position:absolute;left:340px;top:300px;background:#0a84ff;color:#fff;border-radius:12px;padding:8px 16px;font-size:26px;font-weight:900;transform:rotate(6deg)">к себе →</div>
 <div class="c" style="top:40px;font-size:34px;font-weight:900;color:#111">🛣️ перекрёсток</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:#101018">
 <div class="hdr">Видеозвонок · 2 участника</div>
 <div style="position:absolute;left:30px;top:100px;width:250px;height:300px;border-radius:24px;background:#26262e;display:flex;align-items:center;justify-content:center;font-size:100px" id="pe4">🧑</div>
 <div style="position:absolute;left:320px;top:100px;width:250px;height:300px;border-radius:24px;background:#26262e;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:800">Лали</div>
 <div id="lv4" style="position:absolute;left:30px;right:30px;top:412px;background:#3a0d12;border-radius:20px;padding:14px 18px;font-size:26px;font-weight:900;color:#ff453a;opacity:0">он покинул звонок · остался 1</div>
 <div class="ch" data-p="d"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#ff2d78','#ff8ac4','#c2185b');});})();
'''
RENDER='''
 {const T=t;{const t=T-43.9; // анимация карточек написана от начала куска
 {const on=t>=3.2;$('nm1').textContent=on?'не любовь 💔':'Любовь ❤️';$('nt1').style.opacity=seg(t,3.2,3.35);$('nt1').style.transform=`scale(${1+.1*pop(t,3.2,6)})`;
  place('a',300,690,1.0,false);pose('a',on?{aL:8,aR:-8,hd:14,rot:-3}:{aL:8,aR:-8});}
 {const k=eo(seg(t,6.76,7.4));$('bt2').style.width=(100-k*97)+'%';$('bt2').style.background=k<.5?'#30d158':'#ff453a';$('pc2').textContent=Math.round(100-k*100)+'%';$('al2').style.opacity=seg(t,7.2,7.4);
  place('b',300,690,1.0,false);pose('b',t>=7.2?{aL:8,aR:-8,hd:14,rot:-3}:{aL:8,aR:-8});}
 {place('c',300,690,1.0,false);pose('c',{aL:8,aR:-8,hd:Math.sin(t*2)*10});$('ch_c').style.zIndex=7;}
 {const gone=t>=12.38;$('pe4').style.opacity=gone?.15:1;$('lv4').style.opacity=seg(t,12.4,12.6);
  place("d",300,695,0.72,false);pose('d',t>=13.88?{aL:8,aR:-8,hd:14,rot:-3}:{aL:8,aR:-8});}
 }}
'''
