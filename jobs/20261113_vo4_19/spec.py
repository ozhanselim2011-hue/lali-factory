exec(open("/home/user/lali-factory/jobs/_vo4/common.py").read())
SC=[[-0.3,99]];GLOW=['#3a1a6a'];PEMO=['👾']
CSS='.px{image-rendering:pixelated;font-family:"JetBrains Mono";font-weight:900}'
HTML='''
<div class="card px" id="c1" style="background:#000;border:8px solid #fff">
 <div id="sky" style="position:absolute;inset:0;background:#1a0a3a"></div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:120px;background:repeating-linear-gradient(90deg,#b05a1a 0 48px,#8a4410 48px 52px),#b05a1a;border-top:12px solid #3ac43a"></div>
 <div id="hero" style="position:absolute;bottom:120px;width:72px;height:96px;background:linear-gradient(#e33 0 25%,#fc9 25% 50%,#33e 50%)"></div>
 <div id="blk" style="position:absolute;left:0;top:0"></div>
 <div style="position:absolute;left:16px;top:16px;color:#fff;font-size:22px">SCORE <span id="sc">0000</span>   ×<span id="cn">0</span></div>
 <div id="big" class="c" style="top:230px;font-size:52px;color:#ffd60a;text-shadow:5px 5px 0 #e33;opacity:0"></div>
</div>'''
BUILD='''(function(){let s='';for(let i=0;i<4;i++)s+=`<div id="q${i}" style="position:absolute;left:${110+i*100}px;top:330px;width:72px;height:72px;background:#f5a623;border:5px solid #000;color:#000;font:900 46px 'JetBrains Mono';display:flex;align-items:center;justify-content:center">?</div>`;document.getElementById('blk').innerHTML=s;})();'''
RENDER='''
 const T=[0.9,1.25,1.6,2.0];let n=0;T.forEach((s,i)=>{const on=t>=s;if(on)n++;const q=$('q'+i);q.textContent=on?String(i+1):'?';q.style.background=on?'#8a5a2a':'#f5a623';q.style.transform=`translateY(${-20*pop(t,s,12)}px)`});
 const x=t<2.2?lerp(90,420,seg(t,0.8,2.1)):(t<10?420:lerp(420,240,seg(t,10,10.6)));const hb=T.some(s=>t>=s-.15&&t<s+.1)?-70:0;
 $('hero').style.left=Math.round(x/8)*8+'px';$('hero').style.bottom=(120+(t<2.2?Math.max(0,-hb):0))+'px';
 $('sc').textContent=String(Math.min(9999,Math.floor(t*680))).padStart(4,'0');$('cn').textContent=n;
 $('sky').style.background=t>=7&&t<7.5?'#fff':(t>=11&&t<13.2?'#5a1a4a':'#1a0a3a');
 const B=t>=3.5&&t<4.4?'4 UP!':t>=7&&t<7.75?'BOOM!':t>=10.5&&t<11?'STOLEN!':t>=12.25&&t<13.2?'FEELS GOOD':t>=13.75?'GAME OVER · 4':'';$('big').textContent=B;$('big').style.opacity=B?1:0;
'''

CSS=CSS+EMO_CSS
BUILD=BUILD+EMO_BUILD
RENDER=RENDER+EMO_RENDER
