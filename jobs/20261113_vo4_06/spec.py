exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
BG='#0d0518'
SC=[[-0.3,4.4],[4.4,9.95],[9.95,13.15],[13.15,99]];GLOW=['#5a1d7a','#7a1d4a','#5a1d7a','#1d5a2a'];PEMO=['🛒','📦','⭐','📒']
P='position:absolute;left:24px;right:24px;'
HTML=f'''
<div class="card" id="c1" style="background:#f6f4f9;color:#111">
 <div style="{P}top:20px;font-size:28px;font-weight:900;color:#a73afd">Корзина</div>
 <div id="ct" style="{P}top:80px"></div>
 <div id="bt1" style="{P}bottom:24px;height:80px;border-radius:20px;background:#a73afd;color:#fff;font-size:28px;font-weight:900;display:flex;align-items:center;justify-content:center">Оформить</div>
</div>
<div class="card" id="c2" style="background:#f6f4f9;color:#111">
 <div style="{P}top:20px;font-size:28px;font-weight:900;color:#a73afd">Отслеживание заказа</div>
 <div id="tr2" style="{P}top:90px"></div>
 <div id="bx2" class="c" style="top:470px;font-size:140px">📦</div>
</div>
<div class="card" id="c3" style="background:#fff;color:#111">
 <div style="{P}top:20px;font-size:28px;font-weight:900">Отзывы · <span style="color:#f5a623">★★★★☆</span></div>
 <div id="rv" style="{P}top:84px;display:flex;flex-direction:column;gap:14px"></div>
</div>
<div class="card" id="c4" style="background:#f6f4f9;color:#111">
 <div style="{P}top:30px;font-size:30px;font-weight:900;text-align:center">Оцените покупку</div>
 <div id="st4" style="{P}top:180px;text-align:center;font-size:90px;letter-spacing:4px"></div>
 <div id="cm4" class="c" style="top:340px;font-size:34px;font-weight:900;color:#a73afd;opacity:0">садись, четыре.</div>
</div>'''
BUILD=''
RENDER='''
 {const I=[[0.9,'📦','Набор «Первое»'],[1.25,'📦','Набор «Второе»'],[1.6,'📦','Набор «Третье»'],[2.0,'📦','Набор «Четвёртое»']];
  $('ct').innerHTML=I.filter(x=>t>=x[0]).map(x=>`<div style="display:flex;align-items:center;gap:16px;background:#fff;border-radius:18px;padding:12px;margin-bottom:12px;transform:translateX(${(1-eb(seg(t,x[0],x[0]+.25)))*300}px)"><div style="width:64px;height:64px;border-radius:12px;background:#eee;display:flex;align-items:center;justify-content:center;font-size:20px;font-size:34px">${x[1]}</div><div style="font-size:24px;font-weight:800">${x[2]}<div style="font-size:16px;color:#888">товар скрыт 18+</div></div></div>`).join('');
  $('bt1').textContent=t>=3.5?'В корзине все 4 ✓':'Оформить';$('bt1').style.transform=`scale(${1+.1*pop(t,3.5,6)})`;}
 {const S=[[4.5,'Заказ собран'],[5.75,'Закрутили в упаковку'],[7.0,'💥 Посылка взорвалась'],[7.75,'Курьер слушает ваш трек'],[9.4,'…и выдаёт за свой']];
  $('tr2').innerHTML=S.map(s=>`<div style="display:flex;align-items:center;gap:14px;font-size:24px;font-weight:800;margin-bottom:12px;color:${t>=s[0]?'#111':'#bbb'}"><div style="width:26px;height:26px;border-radius:50%;background:${t>=s[0]?'#a73afd':'#ddd'}"></div>${s[1]}</div>`).join('');
  $('bx2').textContent=t>=7.0&&t<7.75?'💥':(t>=7.75?'🎧':'📦');$('bx2').style.transform=`scale(${1+.4*pop(t,7.0,6)})`;}
 {const R=[[10.0,'Аноним','★☆☆☆☆','Они чё, тырят? Мои строчки в описании товара 🤨'],[11.0,'Покупатель','★★★★★','Делает хорошо мне 😌'],[12.25,'Мама','★★★★★','Сынок, это что за набор?']];
  $('rv').innerHTML=R.filter(r=>t>=r[0]).map(r=>`<div style="background:#f6f4f9;border-radius:18px;padding:14px;opacity:${seg(t,r[0],r[0]+.15)}"><div style="font-size:20px;font-weight:900">${r[0]>=12?'👩':'👤'} ${r[1]} <span style="color:#f5a623">${r[2]}</span></div><div style="font-size:23px;font-weight:600;margin-top:4px">${r[3]}</div></div>`).join('');}
 {const n=t>=13.75?4:0;$('st4').innerHTML='<span style="color:#f5a623">'+'★'.repeat(n)+'</span><span style="color:#ddd">'+'★'.repeat(5-n)+'</span>';$('st4').style.transform=`scale(${1+.2*pop(t,13.75,6)})`;$('cm4').style.opacity=seg(t,13.75,13.9);}
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
