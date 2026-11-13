exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#0a4a2a'];PEMO=['📊']
HTML='''
<div class="card" id="c1" style="background:#fff;color:#111">
 <div style="position:absolute;left:0;right:0;top:0;height:60px;background:#107c41;color:#fff;display:flex;align-items:center;padding:0 20px;font-size:22px;font-weight:800">📊 KPI_во_мне.xlsx</div>
 <div style="position:absolute;left:0;right:0;top:60px;height:36px;background:#f3f3f3;border-bottom:1px solid #ccc;display:flex;align-items:center;padding:0 12px;font-family:'JetBrains Mono';font-size:16px;color:#555">fx&nbsp;<span id="fx">=СЧЁТ(во_мне)</span></div>
 <div id="tb" style="position:absolute;left:0;right:0;top:96px"></div>
 <svg id="ch" width="560" height="190" style="position:absolute;left:20px;top:470px"></svg>
</div>'''
BUILD=''
RENDER='''
 const R=[[0.9,'Во мне','4 / 4','#1d6f42'],[4.5,'Мощность','C4 💥','#c00'],[7.75,'Мои строчки у МС','100%','#c55a11'],[10.0,'Украдено','ДА ⚠️','#c00'],[11.0,'Самочувствие','хорошо 😌','#1d6f42'],[13.25,'Итог','4','#2f5597']];
 let h=`<div style="display:flex;background:#f3f3f3;font-size:15px;color:#666;font-weight:700;border-bottom:1px solid #ccc"><span style="width:40px"></span><span style="flex:1;padding:6px">A</span><span style="width:200px;padding:6px">B</span></div>`;
 R.forEach((r,i)=>{const on=t>=r[0];const cur=on&&(i==5||t<R[i+1][0]);h+=`<div style="display:flex;height:56px;align-items:center;border-bottom:1px solid #e1e1e1;font-size:24px;font-weight:700;${cur?'outline:3px solid #107c41;outline-offset:-3px':''}"><span style="width:40px;text-align:center;font-size:15px;color:#888;background:#f3f3f3;height:100%;line-height:56px">${i+1}</span><span style="flex:1;padding:0 10px">${on?r[1]:''}</span><span style="width:200px;padding:0 10px;color:${r[3]};font-weight:900;transform:scale(${1+.2*pop(t,r[0],8)});display:inline-block">${on?r[2]:''}</span></div>`});
 $('tb').innerHTML=h;
 const k=t<4.5?seg(t,0.9,2.0):1;const v=[4,9,14,3,18,4].map((x,i)=>t>=R[i][0]?x:0);
 $('ch').innerHTML=v.map((x,i)=>`<rect x="${i*92+10}" y="${180-x*9*eo(seg(t,R[i][0],R[i][0]+.4))}" width="70" height="${x*9*eo(seg(t,R[i][0],R[i][0]+.4))}" fill="${R[i][3]}"/>`).join('')+'<line x1="0" y1="180" x2="560" y2="180" stroke="#999"/>';
 $('fx').textContent=t<4.5?'=СЧЁТ(во_мне)':t<7.75?'=ВЗРЫВ(C4)':t<11?'=ПОИСКПОЗ("мои строчки";МС)':t<13.25?'=ХОРОШО()':'=ОЦЕНКА()';
'''
