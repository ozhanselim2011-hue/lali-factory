exec(open("/home/user/lali-factory/jobs/_vo4/full.py").read())
HTML='''<div class="card" id="c1" style="background:#000"><div id="bg4" class="ab" style="inset:0"></div><div id="lz" class="ab" style="inset:0"></div>
<div id="n4" class="big" style="top:200px;font-size:700px;color:transparent;-webkit-text-stroke:10px #fff;opacity:0">4</div>
<div class="ch" data-p="a"></div><div class="ch" data-p="b"></div></div>'''
R='''
 let lw=-9;LINES.flat().forEach(([w,s])=>{if(s<=t)lw=s});const b=pop(t,lw,8);const h=(t*50)%360;const st=t>=7&&t<7.6;
 let bg=`radial-gradient(circle at 50% 62%,hsl(${h},100%,${55+25*b}%) 0%,hsl(${(h+70)%360},100%,28%) 38%,#000 78%)`;
 if(t>=11&&t<13.25)bg='radial-gradient(circle at 50% 62%,#ff6ac1,#7a1d6a 42%,#000 80%)';if(st)bg=(Math.floor(t*16)%2)?'#fff':'#000';
 $('bg4').style.background=bg;
 let L='';if(!st)for(let i=0;i<8;i++){const a=22+(i%4)*13+Math.sin(t*2+i)*14,c=`hsl(${(h+i*45)%360},100%,60%)`;L+=`<div class="ab" style="left:${i<4?0:1080}px;top:1080px;width:1700px;height:6px;background:${c};box-shadow:0 0 24px ${c};transform-origin:0 50%;transform:rotate(${i<4?-a:180+a}deg);opacity:${.45+.55*b}"></div>`}$('lz').innerHTML=L;
 const glow=`brightness(0) drop-shadow(0 0 ${18+30*b}px hsl(${h},100%,70%))`;$('ch_a').style.filter=glow;$('ch_b').style.filter=glow;
 const PS=[{aL:150,aR:-8,hd:-8},{aL:8,aR:-150,hd:8},{aL:150,aR:-150,open:1},{aL:90,aR:-90,lL:-25,lR:25}];const nw=[0.9,1.25,1.6,2.0].filter(x=>t>=x).length;
 let o;if(t<2.75)o=nw?PS[nw-1]:{aL:8,aR:-8};else if(t<4.5)o=dn(t);else if(t<7)o={aL:8,aR:-150+Math.sin(t*15)*40,hd:-6};else if(t<7.75)o={aL:160,aR:-160,bob:-30};
 else if(t<11)o=t>=10.5?{aL:8,aR:-90,hd:15}:dn(t);else if(t<13.25)o=dn(t,4,.7);else o={aL:8,aR:-8,hd:t>=13.75?-10:0};
 const rv=t>=7.75&&t<11;place('a',rv?lerp(540,350,eo(seg(t,7.75,8.3))):540,1090,rv?2.3:2.7,false);pose('a',o);
 $('ch_b').style.display=rv?'block':'none';if(rv){place('b',lerp(1300,760,eo(seg(t,7.75,8.3))),1090,2.3,true);pose('b',dn(t));}
 $('n4').style.opacity=seg(t,13.75,13.85);$('n4').style.filter=`drop-shadow(0 0 30px hsl(${h},100%,60%))`;$('n4').style.transform=`scale(${1+.15*pop(t,13.75,6)})`;
'''
FIN()
