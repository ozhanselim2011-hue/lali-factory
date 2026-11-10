DUR=11.4
FADE=11.0
START=2.8
SONG='МИЛЕНА MIBREOO & Давид Туров — Ненавидеть'
BG='linear-gradient(180deg,#140a10,#050304)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Ты",2.98],["теряешься,",3.44],["звонишь —",4.26],["который",4.94],["час?",5.26]],
 [["я",6.02],["больше",6.16],["не",6.54],["хочу",6.84],["тебя",7.3],["видеть",8.06]],
 [["я",8.66],["давала",8.92],["шансы",9.58],["даже",10.22],["два",10.42],["и",10.9],["даже",11.24],["три",11.54]],
 [["хочу",12.02],["тебя",12.5],["ненавидеть",12.92]],
]
SC=[[2.5,5.9],[5.9,8.6],[8.6,11.95],[11.95,99]]
GLOW=['#1a2a5a','#3a3a3a','#7a1f1f','#7a1f4a']
PEMO=['📞','🙈','💔','😤']
END=[13.8,14.2]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#1a1a2e,#05050a)">
 <div class="c mono" id="ck1" style="top:40px;font-size:70px;font-weight:900">03:47</div>
 <div class="c" style="top:130px;font-size:24px;color:#8e8e93;font-weight:700">входящий вызов</div>
 <div class="c" style="top:170px;font-size:46px;font-weight:900">🤡 Он</div>
 <div id="ms1" class="c" style="top:240px;font-size:24px;font-weight:800;color:#ff453a">пропущенных: <span id="n1">1</span></div>
 <div class="ch" data-p="a"></div>
 <div id="ph1" style="position:absolute;left:380px;top:380px;font-size:70px;z-index:6">📱</div>
</div>
<div class="card" id="c2" style="background:#1c1c1e">
 <div class="hdr">Его профиль</div>
 <div style="position:absolute;left:150px;top:80px;width:300px;height:300px;border-radius:50%;background:linear-gradient(135deg,#64d2ff,#5e2cff);overflow:hidden"><div id="pf2" class="c" style="top:40px;font-size:200px">🧢</div></div>
 <div id="bt2" style="position:absolute;left:60px;right:60px;top:410px;height:64px;border-radius:32px;background:#ff453a;font-size:26px;font-weight:900;display:flex;align-items:center;justify-content:center;z-index:6">🙈 скрыть навсегда</div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#000">
 <div class="hdr" style="color:#ff453a">Шансы</div>
 <div id="lv3" class="c" style="top:120px;font-size:100px;letter-spacing:10px">❤️❤️❤️</div>
 <div id="go3" class="c" style="top:300px;font-size:64px;font-weight:900;color:#ff453a;opacity:0;font-family:'JetBrains Mono'">GAME OVER</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div class="hdr">Чувства к нему</div>
 <div style="position:absolute;left:30px;right:30px;top:90px;font-size:26px;font-weight:800;line-height:1.7">
  <div>😤 ненависть <span id="h4" class="mono" style="float:right;color:#ff453a">0%</span></div>
  <div style="height:22px;border-radius:11px;background:#2c2c2e;overflow:hidden"><div id="hb4" style="height:22px;background:#ff453a;width:0"></div></div>
  <div style="margin-top:12px">💖 всё ещё любовь <span id="l4" class="mono" style="float:right;color:#ff2d78">100%</span></div>
  <div style="height:22px;border-radius:11px;background:#2c2c2e;overflow:hidden"><div id="lb4" style="height:22px;background:#ff2d78;width:100%"></div></div></div>
 <div id="er4" class="c" style="top:330px;font-size:24px;font-weight:900;color:#ffd60a;opacity:0">⚠️ ошибка: не получается</div>
 <div class="ch" data-p="d"></div>
</div>
'''
BUILD=open(HELPERS).read()+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,'#ff8ac4','#ffffff','#ffd6e8');});})();
'''
RENDER='''
 {const n=1+Math.floor(seg(t,3.0,5.3)*11);$('n1').textContent=n;$('ph1').style.transform=`rotate(${Math.sin(t*40)*12}deg)`;place('a',220,700,1.0,false);pose('a',t>=5.26?{aL:60,aR:-60,hd:10,open:1}:{aL:8,aR:-8,hd:8});}
 {$('pf2').style.filter=`blur(${seg(t,7.3,8.0)*25}px)`;$('bt2').style.transform=`scale(${1-.08*pop(t,8.06,10)})`;place('b',470,700,.8,true);pose('b',t>=6.54?{aL:8,aR:-150,hd:-10}:{aL:8,aR:-8});}
 {const l=t<10.42?3:(t<11.54?2:(t<12.0?1:0));$('lv3').textContent='❤️'.repeat(l)+'🖤'.repeat(3-l);$('lv3').style.transform=`scale(${1+.15*(pop(t,10.42,8)+pop(t,11.54,8))})`;
  $('go3').style.opacity=seg(t,11.6,11.7);place('c',300,700,1.0,false);pose('c',t>=11.54?{aL:8,aR:-8,hd:14}:{aL:8,aR:-60});}
 {const h=Math.round(eo(seg(t,12.9,13.4))*3);$('h4').textContent=h+'%';$('hb4').style.width=h+'%';$('l4').textContent=(100-h)+'%';$('lb4').style.width=(100-h)+'%';$('er4').style.opacity=seg(t,13.4,13.5);
  place('d',300,700,1.0,false);pose('d',t>=12.92?{aL:40,aR:-40,hd:Math.sin(t*14)*8,open:1}:{aL:8,aR:-8});}
'''
