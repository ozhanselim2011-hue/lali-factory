exec(open("/home/user/lali-factory/jobs/_vo4/full.py").read())
FB=['#ffd6e8','#d6ecff','#fff3c4','#d9ffd6']
HTML='''<div class="card" id="c1" style="background:repeating-linear-gradient(90deg,#8a0a1a 0 50px,#6a0614 50px 100px)">
 <div id="bl10" class="ab" style="inset:0;background:radial-gradient(circle at 35% 55%,rgba(255,150,200,.6),transparent 60%);opacity:0"></div>
 <div class="ab" style="left:0;right:0;top:960px;bottom:0;background:#2a0006"></div>
 <div class="ch" data-p="a"></div><div class="ch" data-p="g" data-c="#8e8e93,#c8c8cc,#8e8e93"></div>
 <div id="strip" class="ab" style="left:770px;top:180px;width:260px;height:790px;background:#fff;box-shadow:0 20px 60px rgba(0,0,0,.6);transform-origin:50% 0;z-index:7">'''+''.join(f'<div id="fr{i}" class="ab" style="left:14px;top:{14+i*192}px;width:232px;height:178px;background:#555;overflow:hidden"><div class="ch" data-p="{"bcde"[i]}"></div></div>' for i in range(4))+'''
  <div id="stp" class="ab" style="left:20px;top:280px;width:220px;height:220px;border:12px solid #d0021b;border-radius:50%;font:900 170px Inter;color:#d0021b;display:flex;align-items:center;justify-content:center;opacity:0">4</div></div>
 <div id="cap10" class="ab ol" style="left:50px;top:200px;font:900 56px Inter;color:#fff;opacity:0;z-index:8"></div>
 <div id="fx10" class="ab" style="inset:0;background:#fff;opacity:0;z-index:9"></div></div>'''
FBJ=str(FB)
R='''
 const FB='''+FBJ+''';const T=[0.9,1.25,1.6,2.0];const PS=[{aL:150,aR:-8,hd:-10},{aL:8,aR:-150,hd:10},{aL:150,aR:-150,open:1},{aL:90,aR:-90,lL:-25,lR:25}];
 T.forEach((s,i)=>{const on=t>=s;$('fr'+i).style.background=on?FB[i]:'#555';$('ch_'+'bcde'[i]).style.opacity=on?1:0;place('bcde'[i],116,255,.78,false);pose('bcde'[i],PS[i]);});
 let fl=0;[...T,10.5].forEach(s=>fl=Math.max(fl,.9*pop(t,s,9)));fl=Math.max(fl,pop(t,7.0,4));$('fx10').style.opacity=fl;$('fx10').style.background=t>=7&&t<7.9?'#ffb347':'#fff';
 const sx=t<4.4?770:(t<13.25?lerp(770,1200,eo(seg(t,4.4,4.9))):410);const sy=t<13.25?180:lerp(-820,170,eb(seg(t,13.25,13.7)));$('strip').style.left=sx+'px';$('strip').style.top=sy+'px';$('strip').style.transform=t>=13.25?'rotate(-4deg) scale(1.02)':'none';
 $('stp').style.opacity=seg(t,13.75,13.8);$('stp').style.transform=`rotate(-15deg) scale(${lerp(2.2,1,eb(seg(t,13.75,14)))})`;
 const n=T.filter(x=>t>=x).length;let o;
 if(t<2.75)o=n?PS[n-1]:{aL:8,aR:-8};else if(t<4.5)o=dn(t);else if(t<7)o={aL:8,aR:-150+Math.sin(t*15)*40,hd:-6};else if(t<7.75)o={aL:160,aR:-160,open:1};
 else if(t<11)o={aL:t>=10.5?90:8,aR:-8,hd:t>=10.5?-18:0,open:t>=10.5};else o={aL:150,aR:-150,hd:-10,bob:Math.sin(t*2)*5};
 place('a',t<4.4?380:540,1000,2.2,false);pose('a',o);
 const rv=t>=7.75&&t<11;$('ch_g').style.display=rv?'block':'none';if(rv){place('g',lerp(-160,150,eo(seg(t,7.75,8.4))),1000,2.0,false,lerp(25,0,seg(t,7.75,8.4)));pose('g',t>=10.5?{aL:150,aR:-150,open:1}:dn(t,12.57,.6));}
 $('bl10').style.opacity=t>=11&&t<13.25?1:0;
 const cp=t>=10.5&&t<11?'ВОР В КАДРЕ!':(t>=12.25&&t<13.25?'ИДЕАЛЬНОЕ ФОТО':(t>=3.5&&t<4.4?'ВСЕ ЧЕТЫРЕ':''));$('cap10').textContent=cp;$('cap10').style.opacity=cp?1:0;
'''
FIN()
