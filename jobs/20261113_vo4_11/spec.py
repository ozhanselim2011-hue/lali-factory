exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#6a3a0a'];PEMO=['👨‍🍳']
HTML='''
<div class="card" id="c1" style="background:linear-gradient(180deg,#f5e6d0,#d9b98a);color:#3a2410">
 <div style="position:absolute;left:0;right:0;top:20px;text-align:center;font-size:30px;font-weight:900">👨‍🍳 Готовим «Во мне все 4»</div>
 <div id="ig" style="position:absolute;left:24px;top:80px;width:250px;font-size:22px;font-weight:800;line-height:1.7"></div>
 <div style="position:absolute;left:260px;top:280px;width:300px;height:170px;border-radius:0 0 150px 150px;background:#555;border-top:14px solid #333"></div>
 <div id="pot" style="position:absolute;left:330px;top:150px;font-size:110px"></div>
 <div id="st" style="position:absolute;left:24px;right:24px;bottom:24px;background:#fff8ee;border-radius:18px;padding:14px;font-size:24px;font-weight:900;text-align:center"></div>
</div>'''
BUILD=''
RENDER='''
 const I=[[0.9,'ингредиент №1'],[1.25,'ингредиент №2'],[1.6,'ингредиент №3'],[2.0,'ингредиент №4']];
 $('ig').innerHTML='<div style="font-size:20px;opacity:.6">ИНГРЕДИЕНТЫ:</div>'+I.map(x=>`<div style="opacity:${t>=x[0]?1:.25}">${t>=x[0]?'✅':'⬜'} ${x[1]}</div>`).join('');
 const S=[[0,'Шаг 1: добавляем всё'],[2.75,'Шаг 2: все четыре в одну кастрюлю'],[4.5,'Шаг 3: закручиваем венчиком'],[7.0,'Шаг 4: 💥 взрывная подача'],[7.75,'Шаг 5: дегустация от соседнего МС'],[10.0,'Шаг 6: он ворует рецепт?!'],[11.0,'Шаг 7: пробуем… хорошо 😌'],[13.25,'Оценка жюри: 4. Садись.']];
 let c='';for(const s of S)if(t>=s[0])c=s[1];$('st').textContent=c;
 $('pot').textContent=t>=7&&t<7.75?'💥':(t>=4.5&&t<7?'🌀':(t>=11?'😋':'🍲'));$('pot').style.transform=`rotate(${t>=4.5&&t<7?t*600:0}deg) scale(${1+.3*pop(t,7,6)})`;
'''
