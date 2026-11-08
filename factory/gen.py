import sys,json
# usage: gen.py spec.py out.html
import os
spec={'HELPERS':os.path.join(os.path.dirname(os.path.abspath(__file__)),'helpers.js')};exec(open(sys.argv[1]).read(),spec)
HEAD='''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px;overflow:hidden;background:#000;font-family:Inter,"Apple Color Emoji",sans-serif}
#stage{position:absolute;inset:0;overflow:hidden;background:%(BG)s}
#glow{position:absolute;inset:-20%%;background:radial-gradient(circle at 50%% 58%%,var(--g,#333) 0%%,transparent 55%%)}
#vign{position:absolute;inset:0;background:radial-gradient(circle,transparent 45%%,rgba(0,0,0,.8) 100%%);z-index:50}
#grain{position:absolute;inset:0;z-index:51;opacity:.07;background-image:repeating-radial-gradient(circle at 17%% 32%%,#fff 0 1px,transparent 1px 4px);mix-blend-mode:overlay}
.pt{position:absolute;font-size:32px}
#sub{position:absolute;top:56px;left:0;right:0;text-align:center;font-weight:%(SUBW)s;font-size:50px;color:#fff;z-index:40;text-shadow:0 4px 24px rgba(0,0,0,.7);padding:0 50px;line-height:1.12;%(SUBX)s}
#sub span{display:inline-block;margin:0 10px}
.card{position:absolute;left:50%%;top:57%%;width:600px;height:690px;margin-left:-300px;margin-top:-345px;border-radius:52px;overflow:hidden;opacity:0;box-shadow:0 40px 120px rgba(0,0,0,.8),0 0 0 1.5px rgba(255,255,255,.08) inset;background:#111214;color:#fff}
.hdr{font-size:22px;font-weight:600;color:rgba(255,255,255,.55);padding:34px 40px 0}
.ttl{font-size:46px;font-weight:800;padding:6px 40px 0;letter-spacing:-1px}
.c{position:absolute;left:0;right:0;text-align:center}
.mono{font-family:'JetBrains Mono'}
.box{background:#2c2c2e;border-radius:24px;padding:20px 24px}
.bub{display:inline-block;padding:14px 22px;border-radius:28px;font-size:27px;font-weight:500}
.row{display:flex;align-items:center;gap:18px;background:#1c1c1e;border-radius:22px;padding:16px 22px;margin-bottom:12px;font-size:26px;font-weight:700}
.tg{width:84px;height:50px;border-radius:25px;background:#3a3a3c;position:relative;flex:none;margin-left:auto}.tg b{position:absolute;top:4px;left:4px;width:42px;height:42px;border-radius:50%%;background:#fff}
#fade{position:absolute;inset:0;background:#000;opacity:0;z-index:70}
%(CSS)s
</style></head><body><div id="stage"><div id="glow"></div><div id="pts"></div>
'''
TAIL='''<div id="sub"></div><div id="vign"></div><div id="grain"></div><div id="fade"></div></div>
<script>
const $=id=>document.getElementById(id);
const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const seg=(t,a,b)=>cl((t-a)/(b-a));
const eo=x=>1-Math.pow(1-x,3);
const eb=x=>{const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const lerp=(a,b,x)=>a+(b-a)*x;
const rnd=i=>{const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x)};
const pop=(t,s,k=8)=>t>=s?Math.exp(-(t-s)*k):0;
const fmt=n=>Math.round(n).toLocaleString('ru-RU');
const tog=(id,on)=>{const e=$(id);e.style.background=on?'#30d158':'#3a3a3c';e.firstElementChild.style.left=on?'38px':'4px'};
const LINES=%(LINES)s;const SC=%(SC)s;const GLOW=%(GLOW)s;const PEMO=%(PEMO)s;const END=%(END)s;const SUBFROM=%(SUBFROM)s;
%(BUILD)s
(function(){let p='';for(let i=0;i<20;i++)p+=`<div class="pt" id="p${i}"></div>`;$('pts').innerHTML=p;})();
function sceneIdx(t){for(let i=SC.length-1;i>=0;i--)if(t>=SC[i][0])return i;return 0}
function showCard(i,t){const [a,b]=SC[i];const el=$('c'+(i+1));
 const inP=eo(seg(t,a,a+.25)),outP=i<SC.length-1?seg(t,b-.1,b):0;const s=lerp(.86,1,eb(seg(t,a,a+.3)))*(1+outP*.06);
 el.style.opacity=inP*(1-outP);el.style.transform=`scale(${s}) translateY(${(1-inP)*40}px)`;el.style.filter=`blur(${(1-inP)*14+outP*10}px)`;}
const shake=(id,t,s,amp=10)=>{if(t>=s)$(id).style.transform+=` translateX(${Math.sin(t*90)*amp*pop(t,s,6)}px)`};
function render(t){
 for(let i=1;i<=SC.length;i++)$('c'+i).style.opacity=0;
 const si=sceneIdx(t);showCard(si,t);
 $('glow').style.setProperty('--g',GLOW[si]);
 let lastW=-9;LINES.flat().forEach(([w,s])=>{if(s<=t)lastW=s});const pulse=Math.exp(-(t-lastW)*7);
 $('glow').style.opacity=.5+.4*pulse;$('glow').style.transform=`scale(${1+.04*pulse})`;
 for(let i=0;i<20;i++){const e=$('p'+i);const y=1-((t*(.05+rnd(i)*.07)+rnd(i+50))%%1);e.textContent=PEMO[si];
  e.style.left=(rnd(i+9)*1040)+'px';e.style.top=(y*1180-80)+'px';e.style.opacity=.12+rnd(i+3)*.25;
  e.style.transform=`rotate(${Math.sin(t+i)*25}deg) scale(${.6+rnd(i+7)*.7})`;e.style.filter=`blur(${rnd(i+5)>.6?3:0}px)`;}
%(RENDER)s
 $('fade').style.opacity=seg(t,END[0],END[1]);
 let li=-1;LINES.forEach((L,i)=>{if(t>=L[0][1]-.15)li=i});
 $('sub').innerHTML=(li<0||t<SUBFROM)?'':LINES[li].map(([w,s])=>{const on=t>=s;const pp=on?Math.exp(-(t-s)*9):0;return `<span style="opacity:${on?1:.3};color:${on&&w.includes('%(RED)s')?'%(REDC)s':'#fff'};transform:scale(${1+.14*pp}) translateY(${-6*pp}px)">${w}</span>`}).join('');
}
window.render=render;render(0);
</script></body></html>'''
d=dict(BG=spec.get('BG','#07070a'),SUBW=spec.get('SUBW','800'),SUBX=spec.get('SUBX',''),CSS=spec.get('CSS',''),
 LINES=json.dumps(spec['LINES'],ensure_ascii=False),SC=json.dumps(spec['SC']),GLOW=json.dumps(spec['GLOW']),PEMO=json.dumps(spec['PEMO'],ensure_ascii=False),
 END=json.dumps(spec['END']),SUBFROM=spec.get('SUBFROM',-9),BUILD=spec.get('BUILD',''),RENDER=spec['RENDER'],RED=spec.get('RED','@@@'),REDC=spec.get('REDC','#ff453a'))
open(sys.argv[2],'w').write(HEAD%d+spec['HTML']+TAIL%d)
