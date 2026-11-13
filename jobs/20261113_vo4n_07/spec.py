exec(open("/home/user/lali-factory/jobs/_vo4/full.py").read())
BAR='position:absolute;top:185px;width:440px;height:44px;background:#3a0d12;border:4px solid #fff'
HTML=f'''<div class="card" id="c1" style="background:linear-gradient(90deg,#0a3a8a,#1a0a2a 50%,#4a4a4e)">
 <div class="ab" style="left:0;right:0;top:850px;height:230px;background:#111;border-top:8px solid #ffd60a"></div>
 <div style="{BAR};left:40px"><div id="hpA" style="height:100%;background:#30d158;width:100%"></div></div><div class="ab" style="left:40px;top:236px;font:900 30px Inter;color:#fff">ЛАЛИ</div>
 <div style="{BAR};right:40px"><div id="hpB" style="height:100%;background:#30d158;width:100%;margin-left:auto"></div></div><div class="ab" style="right:40px;top:236px;font:900 30px Inter;color:#fff">МС КТО-ТО</div>
 <div id="rd" class="big ol" style="top:300px;font-size:64px;color:#ffd60a"></div>
 <div class="ch" data-p="a"></div><div class="ch" data-p="b" data-c="#8e8e93,#c8c8cc,#8e8e93"></div>
 <div id="dmg" class="ab ol" style="font:italic 900 96px Inter;color:#ff453a;opacity:0;z-index:9;white-space:nowrap"></div>
 <div id="ko" class="big" style="top:330px;font-size:320px;font-style:italic;color:#ff453a;-webkit-text-stroke:12px #000;paint-order:stroke fill;opacity:0;z-index:9">K.O.</div>
 <div id="jd" class="ab" style="left:0;right:0;top:690px;display:flex;justify-content:center;gap:26px;z-index:9;opacity:0">{''.join('<div style="width:120px;height:150px;background:#fff;border:6px solid #000;border-radius:12px;font:900 120px Inter;color:#111;text-align:center;line-height:140px">4</div>' for _ in range(4))}</div></div>'''
R='''
 const H=[[3.5,'B',30,'-30'],[7.0,'B',35,'C4!'],[9.4,'A',30,'КОПИРКА!'],[10.5,'B',20,'-20'],[12.25,'B',15,'ДОБИВ']];
 let hA=100,hB=100,last=null;H.forEach(h=>{if(t>=h[0]){const k=eo(seg(t,h[0],h[0]+.3));if(h[1]=='A')hA-=h[2]*k;else hB-=h[2]*k;last=h;}});
 $('hpA').style.width=hA+'%';$('hpB').style.width=hB+'%';$('hpA').style.background=hA<50?'#ff9f0a':'#30d158';$('hpB').style.background=hB<35?'#ff453a':(hB<70?'#ff9f0a':'#30d158');
 const dm=$('dmg');if(last&&t<last[0]+.9){const tg=last[1];dm.textContent=last[3];dm.style.opacity=1-seg(t,last[0]+.6,last[0]+.9);dm.style.left=(tg=='B'?620:120)+'px';dm.style.top=(420-seg(t,last[0],last[0]+.9)*120)+'px';dm.style.transform=`scale(${lerp(1.8,1,eb(seg(t,last[0],last[0]+.2)))}) rotate(-8deg)`;}else dm.style.opacity=0;
 $('rd').textContent=t<4.5?'РАУНД 1':t<7.75?'РАУНД 2':t<10?'ХОД СОПЕРНИКА':t<11?'КОНТРАТАКА':t<13.25?'ФИНАЛ':'';
 const hit=(s)=>t>=s-.25&&t<s+.25;const rec=(s)=>pop(t,s,5);
 let ax=330,bx=750,aO=dn(t,6,.5),bO={aL:8,aR:-8,hd:0},bR=0,aR=0;
 [3.5,7.0,10.5,12.25].forEach(s=>{if(hit(s)){aO={aL:8,aR:-90,open:1,hd:-5};ax=330+90*Math.sin(seg(t,s-.25,s+.25)*Math.PI)}bR+=-14*rec(s)});
 if(t>=7.75&&t<10){bO={...dn(t,12.57,.7),open:Math.sin(t*20)>0};aO={aL:8,aR:-8,hd:t>=8.5?10:0}}
 if(hit(9.4)){bO={aL:8,aR:-90,open:1};bx=750-90*Math.sin(seg(t,9.15,9.65)*Math.PI)}aR+=12*rec(9.4);
 if(t>=12.25){bR=-lerp(0,75,eo(seg(t,12.25,12.7)));bx=700;bO={aL:150,aR:-150,open:1}}
 if(t>=13.25)aO={aL:150,aR:-150,open:1,bob:-Math.abs(Math.sin(t*10))*15};
 place('a',ax,880,1.9,false,aR);pose('a',aO);place('b',bx,880,1.9,true,bR);pose('b',bO);
 if(t>=7&&t<7.5)$('c1').style.transform+=` translate(${Math.sin(t*90)*14}px,0)`;
 $('ko').style.opacity=seg(t,13.25,13.35)*(1-seg(t,13.7,13.75));$('ko').style.transform=`scale(${lerp(2,1,eb(seg(t,13.25,13.5)))}) rotate(-6deg)`;
 $('jd').style.opacity=seg(t,13.75,13.85);$('jd').style.transform=`translateY(${(1-eb(seg(t,13.75,14.05)))*200}px)`;
'''
FIN()
