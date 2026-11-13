exec(open('/home/user/lali-factory/jobs/_vo4/common.py').read())
# Новый формат: на весь кадр 1080×1080, без карточки/фона/частиц/смайликов, с Лали
SUBX='text-transform:uppercase;font-size:64px;-webkit-text-stroke:5px #000;paint-order:stroke fill;letter-spacing:-1px'
CSS='''.card{left:0!important;top:0!important;width:1080px!important;height:1080px!important;margin:0!important;border-radius:0!important;box-shadow:none!important}
#glow,#pts,#vign,#grain{display:none!important}
.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}
.ab{position:absolute}.big{position:absolute;left:0;right:0;text-align:center;font-weight:900;letter-spacing:-4px;line-height:.9}
.ol{-webkit-text-stroke:6px #000;paint-order:stroke fill}'''
LBUILD=open(HELPERS).read()+'''
const dn=(t,k=12.57,a=1)=>{const q=Math.sin(t*k);return {aL:(110+q*40)*a,aR:(-110+q*40)*a,lL:q*14*a,lR:-q*14*a,hd:q*8*a,bob:-Math.abs(q)*14*a}};
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;const c=e.dataset.c?e.dataset.c.split(','):['#64d2ff','#ff8ac4','#ff2d78'];e.innerHTML=CH(p,...c);});})();
'''
CUT='''
 {const ce=$('c'+(si+1));let lw=-9;LINES.flat().forEach(([w,s])=>{if(s<=t)lw=s});const b=pop(t,lw,10);
  ce.style.opacity=1;ce.style.filter='none';ce.style.transform=`scale(${1+.025*b+.05*pop(t,SC[si][0],7)})`;}
'''
SC=[[-0.3,99]]
def FIN():
  g=globals();n=len(g['SC']);g['PEMO']=['']*n;g['GLOW']=['#000']*n
  g['BUILD']=LBUILD+g.get('B2','');g['RENDER']=CUT+g['R']
