exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#1d3a7a'];PEMO=['✏️']
HTML='''<div class="card" id="c1" style="background:#fdfdf8;background-image:linear-gradient(#cfe0f5 1px,transparent 1px),linear-gradient(90deg,#cfe0f5 1px,transparent 1px);background-size:30px 30px;color:#1a3a9a">
 <div style="position:absolute;left:70px;top:0;bottom:0;width:3px;background:#f08080"></div>
 <div id="nb" style="position:absolute;left:90px;right:20px;top:24px;font:italic 700 30px 'Comic Sans MS','Segoe Print',cursive;line-height:60px"></div>
 <div id="gr" style="position:absolute;right:40px;bottom:40px;font:900 170px 'Comic Sans MS',cursive;color:#d0021b;opacity:0;transform:rotate(-14deg)">4</div></div>'''
BUILD=''
RENDER='''
 const L=[[0.9,'Дз: что во мне?'],[2.75,'Ответ: все четыре ✔'],[4.5,'Задача: палка + зубы ='],[6.25,'= взрыв (C4) 💥'],[7.75,'Слышу у МС мои строчки:'],[10.0,'он чё, списал?!  ✗✗✗'],[11.0,'Вывод: мне хорошо 😌'],[13.25,'Учитель: садись,']];
 $('nb').innerHTML=L.filter(l=>t>=l[0]).map(l=>{const k=seg(t,l[0],l[0]+.5);return `<div>${l[1].slice(0,Math.ceil(l[1].length*k))}${k<1?'✏️':''}</div>`}).join('');
 $('gr').style.opacity=seg(t,13.75,13.8);$('gr').style.transform=`rotate(-14deg) scale(${lerp(2.5,1,eb(seg(t,13.75,14)))})`;
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
