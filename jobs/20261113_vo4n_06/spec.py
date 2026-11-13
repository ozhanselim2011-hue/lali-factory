exec(open("/home/user/lali-factory/jobs/_vo4/full.py").read())
HTML='''<div class="card" id="c1" style="background:radial-gradient(ellipse at 50% 30%,#2a1a4a,#07050f 70%)">
 <div id="scr" class="ab" style="left:250px;top:180px;width:580px;height:190px;background:#0a0a14;border:8px solid #222;display:flex;align-items:center;justify-content:center;font:900 150px Inter;letter-spacing:-4px;color:#fff;overflow:hidden"></div>
 <div id="spt" class="ab" style="inset:0"></div>
 <div class="ab" style="left:0;right:0;top:760px;height:140px;background:linear-gradient(#2a1d3a,#120c1a)"></div>
 <div id="pyL" class="ab" style="left:50px;width:130px;top:760px;height:0;background:linear-gradient(0deg,#ff3b00,#ffd60a 55%,rgba(255,255,255,0));border-radius:65px 65px 0 0"></div>
 <div id="pyR" class="ab" style="right:50px;width:130px;top:760px;height:0;background:linear-gradient(0deg,#ff3b00,#ffd60a 55%,rgba(255,255,255,0));border-radius:65px 65px 0 0"></div>
 <div class="ch" data-p="a"></div><div class="ch" data-p="b" data-c="#8e8e93,#c8c8cc,#8e8e93"></div>
 <div id="crowd" class="ab" style="left:0;right:0;top:850px;height:230px;z-index:6"></div>
 <div id="fl6" class="ab" style="inset:0;background:#fff;opacity:0;z-index:8"></div></div>'''
R='''
 let lw=-9;LINES.flat().forEach(([w,s])=>{if(s<=t)lw=s});const b=pop(t,lw,8);
 const W=[[0,''],[0.9,'1'],[1.25,'2'],[1.6,'3'],[2.0,'4'],[2.75,'ВСЕ 4'],[4.5,'ВЖУХ'],[7.0,'C4'],[7.75,'MC?'],[10.0,'ТЫРЯТ?'],[11.0,'ХОРОШО'],[13.25,'САДИСЬ'],[13.75,'4']];
 let w='';let ws=0;W.forEach(x=>{if(t>=x[0]){w=x[1];ws=x[0]}});$('scr').textContent=w;$('scr').style.fontSize=Math.min(130,Math.floor(540/(Math.max(1,w.length)*.66)))+'px';
 $('scr').style.color=t>=7&&t<7.75?'#ff9f0a':(t>=10&&t<11?'#ff453a':'#fff');$('scr').firstChild&&($('scr').style.transform=`scale(${1+.08*pop(t,ws,8)})`);
 const SX=[110,380,700,970],ST=[0.9,1.25,1.6,2.0];let sp='';SX.forEach((x,i)=>{if(t>=ST[i]){const a=Math.sin(t*1.6+i*1.3)*25;const c=t>=11&&t<13.25?'255,120,200':(i%2?'120,200,255':'255,230,150');sp+=`<div class="ab" style="left:${x-170}px;top:170px;width:340px;height:900px;clip-path:polygon(45% 0,55% 0,100% 100%,0 100%);background:linear-gradient(rgba(${c},.55),rgba(${c},0) 85%);transform-origin:50% 0;transform:rotate(${a}deg)"></div>`}});$('spt').innerHTML=sp;
 const py=t>=7&&t<7.9?Math.sin(seg(t,7,7.9)*Math.PI)*620:0;$('pyL').style.height=$('pyR').style.height=py+'px';$('pyL').style.top=$('pyR').style.top=(760-py)+'px';
 $('fl6').style.opacity=.7*pop(t,7.0,8);
 let cr='';for(let i=0;i<20;i++){const x=i*56-10+(i%2)*20,j=(t>=2.75&&t<11)?Math.abs(Math.sin(t*12.57+i))*30*(.6+rnd(i)*.4):(b*12);const y=(i%2?40:0)-j;
  let ex='';if(t>=10.5&&t<11&&i%4==1)ex=`<div style="position:absolute;left:-40px;top:-120px;background:#fff;color:#d0021b;font:900 34px Inter;padding:4px 10px;border:3px solid #000">ВОР!</div>`;
  if(t>=11&&t<13.25&&i%3==0)ex=`<div style="position:absolute;left:${30+Math.sin(t*2+i)*14}px;top:-70px;width:14px;height:22px;border-radius:50% 50% 40% 40%;background:#ffd60a;box-shadow:0 0 20px #ffb000"></div>`;
  const arm=(t>=2.75&&t<11)&&i%3!=1?`<div style="position:absolute;left:${i%2?0:56}px;top:-70px;width:16px;height:90px;border-radius:8px;background:#000;transform:rotate(${i%2?-20:20}deg)"></div>`:'';
  cr+=`<div style="position:absolute;left:${x}px;top:${y}px">${arm}${ex}<div style="width:76px;height:76px;border-radius:50%;background:#000"></div><div style="width:110px;height:200px;margin-left:-17px;border-radius:50px 50px 0 0;background:#000"></div></div>`}$('crowd').innerHTML=cr;
 const rv=t>=7.75&&t<11;
 let o;if(t<2.75)o=[0.9,1.25,1.6,2.0].filter(x=>t>=x).length%2?{aL:150,aR:-8,open:1}:{aL:8,aR:-150,open:1};else if(t<4.5)o=dn(t);else if(t<7)o={aL:8,aR:-150+Math.sin(t*15)*40,hd:-6};else if(t<7.75)o={aL:160,aR:-160,open:1,bob:-60*Math.sin(seg(t,7,7.6)*Math.PI)};
 else if(t<11)o={aL:8,aR:t>=10.5?-90:-8,hd:t>=8.5?16:0,open:t>=10.5};else if(t<13.25)o={aL:150,aR:-150,hd:-8,bob:Math.sin(t*2)*4};else o={aL:30,aR:-30,hd:t>=13.6?30:0,bob:t>=13.6?20:0};
 place('a',rv?lerp(540,330,eo(seg(t,7.75,8.3))):540,800,1.5,false);pose('a',o);
 $('ch_b').style.display=rv?'block':'none';if(rv){place('b',t<10.5?lerp(1250,760,eo(seg(t,7.75,8.4))):lerp(760,1300,seg(t,10.5,10.95)),800,1.5,true);pose('b',{...dn(t,12.57,.7),open:Math.sin(t*20)>0});}
'''
FIN()
