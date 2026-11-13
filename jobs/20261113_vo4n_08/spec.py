exec(open("/home/user/lali-factory/jobs/_vo4/full.py").read())
HTML='''<div class="card" id="c1" style="background:#0a0614">
 <div id="nb8" class="big" style="top:170px;font-size:520px;color:rgba(255,255,255,.14)"></div>
 <div class="ab" style="left:-300px;right:-300px;top:640px;height:700px;transform:perspective(700px) rotateX(58deg);transform-origin:50% 0"><div id="fl8" style="display:grid;grid-template-columns:repeat(10,1fr);grid-template-rows:repeat(6,1fr);height:100%;gap:8px"></div></div>
 <div id="mb" class="ab" style="left:475px;top:175px;width:130px;height:130px;border-radius:50%;background:repeating-conic-gradient(#eee 0 12deg,#777 12deg 24deg);box-shadow:0 0 60px rgba(255,255,255,.7)"></div>
 <div id="sp8" class="ab" style="inset:0"></div>
 <div class="ch" data-p="a"></div><div class="ch" data-p="b" data-c="#8e8e93,#c8c8cc,#8e8e93"></div>
 <div id="f8" class="big" style="top:260px;font-size:560px;color:#ffd60a;-webkit-text-stroke:14px #000;paint-order:stroke fill;opacity:0;z-index:9">4</div></div>'''
R='''
 const C=[0.9,1.25,1.6,2.0].filter(x=>t>=x).length;$('nb8').textContent=t<2.75&&C?String(C):'';$('nb8').style.transform=`scale(${1+.2*pop(t,[0,0.9,1.25,1.6,2.0][C],8)})`;
 const wh=t>=7&&t<7.6,pk=t>=11&&t<13.25;let f='';for(let i=0;i<60;i++){const on=rnd(i*3+Math.floor(t*(pk?1.5:4)))>.55;const c=wh?'#fff':(pk?(on?'#ff6ac1':'#2a0a20'):(on?`hsl(${(i*37+Math.floor(t*4)*60)%360},100%,60%)`:'#15101f'));f+=`<div style="background:${c};box-shadow:${on||wh?'0 0 30px '+c:'none'}"></div>`}$('fl8').innerHTML=f;
 $('mb').style.transform=`rotate(${t*90}deg)`;let s='';for(let i=0;i<26;i++){const a=i*0.9+t*1.4;s+=`<div class="ab" style="left:${540+Math.cos(a)*(250+rnd(i)*300)}px;top:${400+Math.sin(a*1.3)*(150+rnd(i+5)*120)}px;width:8px;height:8px;border-radius:50%;background:#fff;box-shadow:0 0 12px #fff;opacity:${.4+.6*Math.abs(Math.sin(t*5+i))}"></div>`}$('sp8').innerHTML=s;
 const rv=t>=7.75&&t<11;let o,flip=false,by=0;
 if(t<2.75)o=C?[{aL:150,aR:-8},{aL:8,aR:-150},{aL:150,aR:-150,open:1},{aL:90,aR:-90,lL:-25,lR:25}][C-1]:{aL:8,aR:-8};
 else if(t<4.5)o=dn(t);else if(t<7){o={aL:90,aR:-90,lL:Math.sin(t*12.57)*25,lR:-Math.sin(t*12.57)*25,hd:Math.sin(t*12.57)*10};flip=Math.floor(t*4)%2==1}
 else if(t<7.75){o={aL:160,aR:-160,open:1};by=-120*Math.sin(seg(t,7,7.6)*Math.PI)}
 else if(t<11)o=t>=10.5?{aL:8,aR:-90,hd:15,open:1}:dn(t);else if(t<13.25)o=dn(t,4,.8);else o={aL:8,aR:-8,hd:t>=13.75?-10:0};
 place('a',rv?lerp(540,350,eo(seg(t,7.75,8.3))):540,960+by,2.2,flip);pose('a',o);
 $('ch_b').style.display=rv?'block':'none';if(rv){place('b',lerp(1300,750,eo(seg(t,7.75,8.3))),960,2.2,true);pose('b',t>=10.5?{aL:8,aR:-8,hd:-12}:dn(t));}
 $('f8').style.opacity=seg(t,13.75,13.85);$('f8').style.transform=`scale(${lerp(1.7,1,eb(seg(t,13.75,14)))})`;
'''
FIN()
