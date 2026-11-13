exec(open("/home/user/lali-factory/jobs/_vo4/full.py").read())
PX=[[30,175],[550,175],[30,445],[550,445],[30,715],[550,715]];PB=['#ffd60a','#64d2ff','#d1d1d6','#ff453a','#ff8ac4','#30d158']
SFX=['1·2·3·4!','ВЖУХ','','ЧЁ?!','ХОРОШО…','']
BUB=['ВО МНЕ ВСЕ ЧЕТЫРЕ!','','…МОИ СТРОЧКИ…','ОНИ ЧЁ, ТЫРЯТ?!','','САДИСЬ…']
def pn(i):
  x,y=PX[i];c=' data-c="#8e8e93,#c8c8cc,#8e8e93"' if i==2 else ''
  return f'''<div id="pn{i}" class="ab" style="left:{x}px;top:{y}px;width:500px;height:250px;background:{PB[i]};border:8px solid #111;overflow:hidden;opacity:0;background-image:radial-gradient(rgba(0,0,0,.15) 3px,transparent 3px);background-size:16px 16px">
 <div id="bs{i}" class="ab" style="right:20px;top:30px;width:260px;height:170px;background:#fff;clip-path:polygon(50% 0,61% 30%,98% 18%,72% 48%,100% 70%,64% 68%,58% 100%,45% 72%,10% 92%,30% 60%,0 40%,36% 34%);opacity:0"></div>
 <div class="ch" data-p="{'abcdef'[i]}"{c}></div>
 <div id="sx{i}" class="ab" style="right:24px;top:70px;width:250px;text-align:center;font:italic 900 52px Inter;color:#ffd60a;-webkit-text-stroke:4px #111;paint-order:stroke fill;opacity:0;z-index:6">{SFX[i]}</div>
 <div id="bb{i}" class="ab" style="left:200px;top:16px;max-width:280px;background:#fff;border:4px solid #111;border-radius:24px;padding:8px 14px;font:900 24px Inter;color:#111;opacity:0;z-index:6">{BUB[i]}</div></div>'''
HTML='<div class="card" id="c1" style="background:#fff7d6;background-image:radial-gradient(#e8c96a 3px,transparent 3px);background-size:18px 18px">'+''.join(pn(i) for i in range(6))+'<div id="st5" class="ab" style="left:700px;top:735px;width:210px;height:210px;border:12px solid #d0021b;border-radius:50%;font:900 160px Inter;color:#d0021b;display:flex;align-items:center;justify-content:center;opacity:0;z-index:9">4</div></div>'
R='''
 const S=[0.9,4.5,7.75,10.0,11.0,13.25];
 S.forEach((s,i)=>{const e=$('pn'+i);const k=eb(seg(t,s,s+.3));e.style.opacity=seg(t,s,s+.08);e.style.transform=`scale(${lerp(.6,1,k)}) rotate(${(1-k)*(i%2?6:-6)}deg)`;e.style.zIndex=t>=s?2:1;});
 const sh=(id,s)=>{if(t>=s)$(id).style.transform+=` translate(${Math.sin(t*90)*10*pop(t,s,5)}px,0)`};sh('pn1',7.0);sh('pn3',10.5);
 const sx=(i,s,txt)=>{$('sx'+i).style.opacity=seg(t,s,s+.05);$('sx'+i).style.transform=`scale(${lerp(2,1,eb(seg(t,s,s+.25)))}) rotate(-8deg)`;if(txt)$('sx'+i).textContent=txt;$('bs'+i).style.opacity=seg(t,s,s+.05);};
 sx(0,3.5);sx(1,5.75,t>=7?'БАБАХ!':'ВЖУХ');if(t>=7){$('pn1').style.background='#ff9f0a'}sx(3,10.5);sx(4,12.25);
 [[0,2.75],[2,9.0],[3,10.0],[5,13.25]].forEach(([i,s])=>{$('bb'+i).style.opacity=seg(t,s,s+.1)});
 const nw=[0.9,1.25,1.6,2.0].filter(x=>t>=x).length;
 place('a',120,250,.82,false);pose('a',t<3.5?[{aL:8,aR:-8},{aL:150,aR:-8},{aL:150,aR:-150},{aL:90,aR:-150},{aL:150,aR:-150,open:1}][nw]:{aL:150,aR:-150,open:1,bob:-Math.abs(Math.sin(t*10))*10});
 place('b',120,250,.82,false);pose('b',t<7?{aL:8,aR:-150+Math.sin(t*18)*35}:{aL:160,aR:-160,open:1});
 place('c',120,250,.82,false);pose('c',{...dn(t,12.57,.6),open:Math.sin(t*20)>0});
 place('d',140,470,1.75,false);pose('d',{aL:8,aR:-8,hd:t>=10.5?-12:0,open:t>=10.5});
 place('e',120,250,.82,false);pose('e',{aL:150,aR:-150,hd:-10,bob:Math.sin(t*3)*5});
 place('f',120,250,.82,false);pose('f',{aL:8,aR:-8,hd:t>=13.75?20:0});
 $('st5').style.opacity=seg(t,13.75,13.8);$('st5').style.transform=`rotate(-14deg) scale(${lerp(2.2,1,eb(seg(t,13.75,14)))})`;
'''
FIN()
