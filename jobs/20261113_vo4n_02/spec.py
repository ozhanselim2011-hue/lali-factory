exec(open("/home/user/lali-factory/jobs/_vo4/full.py").read())
OUT='filter:drop-shadow(8px 0 0 #fff) drop-shadow(-8px 0 0 #fff) drop-shadow(0 8px 0 #fff) drop-shadow(0 -8px 0 #fff) drop-shadow(0 30px 30px rgba(0,0,0,.4))'
HTML=f'''<div class="card" id="c1"><div id="bg2" class="ab" style="inset:0"></div><div id="wd2" class="big" style="color:transparent;-webkit-text-stroke:7px rgba(255,255,255,.95)"></div>
<div class="ch" data-p="a" style="{OUT}"></div><div class="ch" data-p="b" data-c="#8e8e93,#c8c8cc,#8e8e93" style="{OUT}"></div></div>'''
R='''
 const W=LINES.flat();let i=-1;W.forEach((w,k)=>{if(t>=w[1])i=k});
 const P=['#ff2d55','#ffd60a','#30d158','#0a84ff','#bf5af2','#ff9f0a','#00c7be','#ff375f'];
 $('bg2').style.background=(t>=7&&t<7.6)?((Math.floor(t*14)%2)?'#fff':'#000'):(i<0?'#111':P[i%8]);
 const w=i<0?'':W[i][0].replace(/[,?«»]/g,'').toUpperCase();const fs=Math.min(330,Math.floor(1000/(Math.max(2,w.length)*.64)));
 const bt=i<0?0:pop(t,W[i][1],9);
 $('wd2').textContent=w;$('wd2').style.fontSize=fs+'px';$('wd2').style.top=(600-fs*.5)+'px';$('wd2').style.transform=`scale(${1+.25*bt}) rotate(${(i%3-1)*5}deg)`;
 const rv=t>=7.75&&t<11;let s=2.3+.12*bt,x=rv?lerp(540,330,eo(seg(t,7.75,8.3))):540,rot=(t>=7&&t<7.6)?Math.sin(t*60)*6:0;
 place('a',x,1070,rv?2.0:s,!rv&&(i%2==1),rot);
 pose('a',t<2.75?{aL:8+70*bt,aR:-8-70*bt,hd:(i%2?8:-8),open:bt>.5}:t<4.5?dn(t):(t<7?{aL:8,aR:-150+Math.sin(t*20)*30,hd:-5}:(t<7.75?{aL:160,aR:-160,open:1}:(t<11?{aL:8,aR:t>=10.5?-90:-8,hd:t>=9?18:0,open:t>=10.5}:(t<13.25?{aL:150,aR:-150,hd:-10,bob:Math.sin(t*3)*6}:{aL:8,aR:-8,hd:0,open:t>=13.75})))));
 $('ch_b').style.display=rv?'block':'none';if(rv){place('b',lerp(1300,800,eo(seg(t,7.75,8.3))),1070,2.0,true);pose('b',t>=10.5?{aL:8,aR:-8,hd:-15}:dn(t));}
'''
FIN()
