exec(open("/home/user/lali-factory/jobs/_vo4/full.py").read())
CHF='filter:drop-shadow(6px 0 0 rgba(255,0,0,.55)) drop-shadow(-6px 0 0 rgba(0,255,255,.55))'
MONO="font-family:'JetBrains Mono';color:#fff;text-shadow:3px 3px 0 #000;z-index:13"
HTML=f'''<div class="card" id="c1" style="background:#5a4636">
 <div class="ab" style="inset:0;background:repeating-linear-gradient(90deg,#6b5442 0 60px,#5e4a3a 60px 120px)"></div>
 <div class="ab" style="left:660px;top:260px;width:300px;height:240px;background:linear-gradient(#9fd3ff,#cfe9ff);border:14px solid #3a2a1e"></div>
 <div class="ab" style="left:0;right:0;top:770px;bottom:0;background:#4a3a2a"></div>
 <div class="ab" style="left:110px;top:600px;width:860px;height:240px;background:#7a2a2a;border-radius:50px 50px 20px 20px;box-shadow:inset 0 -30px 0 #5a1a1a"></div>
 <div class="ch" data-p="a" style="{CHF}"></div><div class="ch" data-p="b" data-c="#8e8e93,#c8c8cc,#8e8e93" style="{CHF}"></div>
 <div id="bsod" class="ab" style="inset:0;background:#0018a8;opacity:0;z-index:7"></div>
 <div id="v4" class="big" style="top:300px;font:400 460px 'JetBrains Mono';color:#fff;opacity:0;z-index:8">4</div>
 <div class="ab" style="inset:0;background:repeating-linear-gradient(0deg,rgba(0,0,0,.22) 0 2px,transparent 2px 5px);z-index:10"></div>
 <div id="trk" class="ab" style="left:0;right:0;height:60px;background:linear-gradient(rgba(255,255,255,0),rgba(255,255,255,.3),rgba(255,255,255,0));z-index:11"></div>
 <div id="nz" class="ab" style="inset:0;z-index:12"></div>
 <div id="osd" class="ab" style="left:60px;top:190px;font-size:56px;{MONO}">PLAY</div>
 <div id="tc" class="ab" style="right:60px;top:196px;font-size:40px;{MONO}"></div>
 <div class="ab" style="left:60px;top:890px;font-size:40px;{MONO}">13 НОЯ 2006</div>
 <div id="cnt" class="big" style="top:330px;font:400 260px 'JetBrains Mono';color:#fff;text-shadow:6px 6px 0 #000;z-index:9"></div></div>'''
R='''
 let T=t;const ps=t>=10.0&&t<10.95;if(ps)T=10.0;
 $('osd').textContent=t>=13.25?'STOP':ps?'PAUSE':(t>=11?'SLOW':'PLAY');$('tc').textContent='SP 0:00:'+String(Math.floor(t)).padStart(2,'0');
 $('trk').style.top=((t*260)%1200-100)+'px';
 const gl=(t>=7&&t<7.7)||(t>=13.25&&t<13.6);let n='';if(gl)for(let i=0;i<16;i++)n+=`<div class="ab" style="left:0;right:0;top:${rnd(i+Math.floor(t*30))*1080}px;height:${10+rnd(i+3)*50}px;background:rgba(255,255,255,${.2+rnd(i)*.5});transform:translateX(${(rnd(i+9)-.5)*120}px)"></div>`;$('nz').innerHTML=n;
 if(gl)$('c1').style.transform+=` translateX(${Math.sin(t*80)*24}px) skewX(${Math.sin(t*50)*5}deg)`;if(ps)$('c1').style.transform+=` translateY(${Math.floor(t*30)%2*5}px)`;
 $('bsod').style.opacity=t>=13.6?1:0;$('v4').style.opacity=t>=13.75?1:0;
 const C=[0.9,1.25,1.6,2.0].filter(x=>T>=x).length;$('cnt').textContent=T<2.75&&C?String(C):'';
 let o,x=540;if(T<2.75)o=[{aL:8,aR:-8},{aL:150,aR:-8},{aL:150,aR:-150},{aL:90,aR:-150,hd:10},{aL:150,aR:-150,open:1,bob:-20}][C];
 else if(T<4.5)o=dn(T);else if(T<7.75)o=T<7?{aL:8,aR:-150+Math.sin(T*15)*40,hd:-6}:{aL:160,aR:-160,open:1};
 else if(T<11){x=lerp(540,360,eo(seg(T,7.75,8.3)));o={aL:8,aR:T>=10?-90:-8,hd:T>=8.5?16:0,open:T>=10}}else o={aL:120,aR:-120,hd:-10,bob:Math.sin(T*2)*4};
 place('a',x,900,1.9,false);pose('a',o);
 const rv=T>=7.75&&T<11;$('ch_b').style.display=rv?'block':'none';if(rv){place('b',lerp(1250,760,eo(seg(T,7.75,8.4))),900,1.9,true);pose('b',dn(T,12.57,.6));}
'''
FIN()
