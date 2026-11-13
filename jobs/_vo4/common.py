DUR=14.7
FADE=14.3
START=0
SONG=''
BG='#050507'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["алк*,",0.9],["тр*ва,",1.25],["з*ны,",1.6],["никот*н",2.0]],
 [["во",2.75],["мне",3.0],["все",3.25],["четыре",3.5]],
 [["в",4.5],["зубы",4.75],["палку",5.25],["закрутил",5.75]],
 [["взрыв,",6.25],["как",6.6],["C4",7.0]],
 [["слышу",7.75],["у",8.4],["эмси",8.5],["мои",9.0],["строчки",9.4]],
 [["они",10.0],["чё,",10.25],["тырят?",10.5]],
 [["с*ка",11.0],["делает",11.5],["хорошо",12.25],["мне",12.9]],
 [["садись,",13.25],["четыре",13.75]],
]
SC=[[-0.3,4.4],[4.4,7.6],[7.6,9.95],[9.95,10.95],[10.95,13.15],[13.15,99]]
GLOW=['#5a0a0a','#6a3a0a','#1d3a7a','#7a0a0a','#5a1d4a','#1d5a2a']
PEMO=['4️⃣','💥','🎧','©️','😌','📒']
END=[14.35,14.7]
CSS='''.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}
.row{display:flex;justify-content:space-between;align-items:center}'''

# ---- слой эмоций (отзыв владельца: «более эмоциональные») ----
EMO_CSS='''#emo{position:absolute;inset:0;z-index:45;pointer-events:none}
#fcam{position:absolute;left:800px;top:610px;width:210px;height:210px;border-radius:50%;background:radial-gradient(circle at 50% 40%,#3a3a44,#111);border:6px solid #ff375f;box-shadow:0 0 40px rgba(255,55,95,.6);display:flex;align-items:center;justify-content:center;font-size:150px;overflow:hidden}
#fcl{position:absolute;left:836px;top:578px;z-index:2;background:#ff375f;color:#fff;font:900 20px Inter;padding:3px 10px;border-radius:8px}
#rtx{position:absolute;left:0;right:0;top:470px;text-align:center;font:900 130px Inter;letter-spacing:-4px;-webkit-text-stroke:6px #000;paint-order:stroke fill;text-shadow:0 12px 0 #000}
#fl{position:absolute;inset:0}'''
EMO_BUILD=''';(function(){const d=document.createElement('div');d.id='emo';d.innerHTML='<div id="fl"></div><div id="rtx"></div><div id="fcl">🔴 РЕАКЦИЯ</div><div id="fcam"></div>';$('stage').appendChild(d);})();'''
EMO_RENDER='''
 {const R=[[-9,'😐','','#fff',0],[0.9,'😮','','#fff',0],[3.5,'😳','ВСЕ ЧЕТЫРЕ?!','#ffd60a',14],[4.5,'🤔','','#fff',0],[5.75,'😏','','#fff',0],[7.0,'🤯','БА-БАХ','#ff9f0a',30],[7.75,'🧐','','#fff',0],[9.4,'🤨','МОИ?!','#64d2ff',12],[10.5,'😡','ЭЙ!!','#ff453a',22],[11.0,'😏','','#fff',0],[12.25,'🥵','КАЙФ','#ff375f',14],[13.25,'😤','','#fff',0],[13.75,'😤','САДИСЬ. 4','#30d158',18]];
  let r=R[0];for(const x of R)if(t>=x[0])r=x;
  let lw=-9;LINES.flat().forEach(([w,s])=>{if(s<=t)lw=s});const beat=pop(t,lw,9);
  const hit=r[4]?pop(t,r[0],5):0;const sh=r[4]*hit;
  $('stage').style.transform=`scale(${1.02+.03*beat+.04*hit}) translate(${Math.sin(t*97)*sh}px,${Math.cos(t*83)*sh}px) rotate(${Math.sin(t*61)*sh*.04}deg)`;
  const ce=$('c'+(si+1));ce.style.transform+=` rotate(${Math.sin(t*2.3)*1.5+Math.sin(t*70)*sh*.08}deg) scale(${1+.03*beat})`;
  $('fcam').textContent=r[1];$('fcam').style.transform=`scale(${1+.25*pop(t,r[0],7)+.05*beat}) rotate(${Math.sin(t*5)*6}deg)`;$('fcam').style.borderColor=r[4]&&t-r[0]<.8?r[3]:'#ff375f';
  const on=r[2]&&t-r[0]<.9;$('rtx').textContent=on?r[2]:'';$('rtx').style.color=r[3];
  $('rtx').style.transform=`scale(${on?lerp(2.4,1,eb(seg(t,r[0],r[0]+.25))):1}) rotate(${(r[0]*7%2?-6:6)}deg)`;$('rtx').style.opacity=on?1-seg(t,r[0]+.7,r[0]+.9):0;
  $('fl').style.background=r[3];$('fl').style.opacity=r[4]?.55*pop(t,r[0],10):0;
  $('stage').style.filter=r[4]&&t-r[0]<.12?'saturate(2) contrast(1.3)':'none';}
'''
