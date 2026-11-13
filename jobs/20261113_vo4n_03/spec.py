exec(open("/home/user/lali-factory/jobs/_vo4/full.py").read())
BGQ=['#ff2d55','#ffd60a','#30d158','#0a84ff'];CQ=['#111,#fff,#ff2d55','#111,#ff2d55,#ff9f0a','#111,#0a84ff,#30d158','#111,#ffd60a,#0a84ff']
HTML='<div class="card" id="c1" style="background:#000">'+''.join(f'<div id="q{i}" class="ab" style="left:{(i%2)*540}px;top:{(i//2)*540}px;width:540px;height:540px;overflow:hidden;background:{BGQ[i]};outline:4px solid #000"><div class="big ol" style="top:{190 if i<2 else 30}px;left:auto;right:30px;font-size:170px;color:rgba(255,255,255,.9)">{i+1}</div><div class="ch" data-p="{"abcd"[i]}" data-c="{CQ[i]}"></div></div>' for i in range(4))+'''
 <div id="vr3" class="big ol" style="top:600px;left:540px;font-size:150px;color:#ff453a;opacity:0;z-index:9">ВОР?</div>
 <div id="big3" class="big" style="top:250px;font-size:640px;color:#fff;-webkit-text-stroke:16px #000;paint-order:stroke fill;opacity:0;z-index:9">4</div></div>'''
R='''
 const T=[0.9,1.25,1.6,2.0],ids='abcd';
 for(let i=0;i<4;i++){const q=$('q'+i),p=ids[i];
  const lit=t>=2.75||(t>=T[i]&&(i==3||t<T[i+1]));q.style.filter=lit?'none':'brightness(.3) saturate(.3)';
  let qx=(i%2)*540,qy=Math.floor(i/2)*540;if(t>=7&&t<7.75){const k=eo(seg(t,7,7.15))*(1-seg(t,7.4,7.75));qx+=(i%2?1:-1)*90*k;qy+=(i<2?-1:1)*90*k;}
  q.style.left=qx+'px';q.style.top=qy+'px';q.style.zIndex=t>=T[i]&&t<T[i]+.3?2:1;q.style.transform=`scale(${1+.1*pop(t,T[i],8)})`;
  let o;
  if(t<2.75)o=t>=T[i]?{aL:150,aR:-150,open:1,bob:-10*pop(t,T[i],6)}:{aL:8,aR:-8};
  else if(t<4.5)o=dn(t);
  else if(t<7)o={aL:8,aR:-150+Math.sin(t*15+i)*35,hd:-5};
  else if(t<7.75)o={aL:160,aR:-160,open:1,hd:(i%2?10:-10)};
  else if(t<11)o=i==3?dn(t):{aL:8,aR:t>=10.5?-90:-8,hd:t>=8.5?(i%2?-14:14):0,open:t>=10.5};
  else if(t<13.25)o={aL:8,aR:-8,hd:Math.sin(t*2+i)*10,bob:Math.sin(t*2+i)*5};
  else o={aL:8,aR:-8,hd:0};
  pose(p,o);place(p,270,i<2?520:530,1.45,i%2==1,0);}
 const rv=t>=7.75&&t<11;$('q3').style.background=rv?'#3a3a3c':'#0a84ff';$('ch_d').style.filter=rv?'grayscale(1)':'none';
 $('vr3').style.opacity=t>=10.5&&t<11?1:0;$('vr3').style.transform=`scale(${1+.4*pop(t,10.5,8)}) rotate(-8deg)`;
 $('big3').style.opacity=seg(t,13.75,13.85);$('big3').style.transform=`scale(${lerp(1.6,1,eb(seg(t,13.75,14.0)))})`;
'''
FIN()
