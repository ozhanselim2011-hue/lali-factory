(function(){
const Q=id=>document.getElementById(id);const st=Q('stage');
const css=document.createElement('style');css.textContent=`
#np{position:absolute;left:50%;top:10px;transform:translateX(-50%);height:58px;display:flex;align-items:center;gap:12px;padding:0 22px 0 8px;border-radius:30px;background:rgba(18,18,22,.86);box-shadow:0 0 0 1.5px rgba(255,255,255,.12) inset,0 8px 24px rgba(0,0,0,.5);z-index:60;max-width:900px;overflow:hidden;font-family:Inter,'Apple Color Emoji',sans-serif}
#np .a{width:42px;height:42px;border-radius:11px;background:linear-gradient(135deg,#ff2d78,#7a2cff);display:flex;align-items:center;justify-content:center;font-size:24px;color:#fff;flex:none}
#np .eq{display:flex;gap:3px;align-items:flex-end;height:24px;flex:none}#np .eq i{display:block;width:4px;border-radius:2px;background:#ff2d78}
#np .w{position:relative;overflow:hidden;max-width:700px;height:30px}
#np .s{white-space:nowrap;font-weight:800;font-size:23px;line-height:30px;color:#fff;display:inline-block}
#np .s span{color:#aeaeb2;font-weight:600}
#np .pr{position:absolute;left:0;bottom:0;height:3px;background:linear-gradient(90deg,#ff2d78,#bf5af2)}
#vp{position:absolute;left:50%;bottom:16px;transform:translateX(-50%);height:68px;display:flex;align-items:center;gap:14px;padding:0 26px 0 10px;border-radius:34px;background:#141418;box-shadow:0 0 0 2px rgba(255,255,255,.14) inset,0 8px 24px rgba(0,0,0,.5);z-index:60;overflow:hidden;white-space:nowrap;font-family:Inter,'Apple Color Emoji',sans-serif}
#vp .i{width:48px;height:48px;border-radius:14px;background:linear-gradient(135deg,#30d158,#0a84ff);display:flex;align-items:center;justify-content:center;font-size:28px;flex:none}
#vp .t{color:#fff;font-weight:800;font-size:27px}#vp .t b{color:#64d2ff}#vp .t span{color:#8e8e93;font-weight:600;font-size:22px}
#vp .sh{position:absolute;top:0;bottom:0;width:120px;background:linear-gradient(100deg,transparent,rgba(255,255,255,.22),transparent);pointer-events:none}`;
document.head.appendChild(css);
const song=window.SONG||'';
if(song){const [a,t]=song.split(' — ');const np=document.createElement('div');np.id='np';
 np.innerHTML=`<div class="a" id="npa">♫</div><div class="eq">${[0,1,2,3,4].map(i=>`<i id="nq${i}"></i>`).join('')}</div><div class="w" id="npw"><div class="s" id="nps">${t?`${a} <span>— ${t}</span>`:a}</div></div><div class="pr" id="npr"></div>`;st.appendChild(np);}
const vp=document.createElement('div');vp.id='vp';vp.innerHTML=`<div class="i" id="vpi">🔒</div><div class="t">VPN в тг: <b id="vpb">@PluggerVpnBot</b> <span>· лучший впн в тг</span></div><div class="sh" id="vps"></div>`;st.appendChild(vp);
const DUR=window.DUR||15;
window.barsRender=function(t){
 if(song){for(let i=0;i<5;i++)Q('nq'+i).style.height=(5+Math.abs(Math.sin(t*(7+i*1.7)+i*1.3))*19)+'px';
  Q('npa').style.transform=`rotate(${Math.sin(t*3)*8}deg) scale(${1+.06*Math.abs(Math.sin(t*6))})`;
  const w=Q('npw'),s=Q('nps');const over=s.scrollWidth-w.clientWidth;
  if(over>4){const cyc=6+over/60;const ph=(t%cyc)/cyc;const x=ph<.2?0:(ph<.7?-over*((ph-.2)/.5):-over);s.style.transform=`translateX(${x}px)`;}
  s.style.textShadow=`0 0 ${8+6*Math.sin(t*2)}px rgba(255,45,120,${.35+.25*Math.sin(t*2)})`;
  Q('npr').style.width=(Math.min(1,t/DUR)*100)+'%';
  Q('np').style.opacity=Math.min(1,Math.max(0,t*4+1));}
 const sh=Q('vps');const W=Q('vp').clientWidth;const ph=(t*.45)%1;sh.style.left=(-140+ph*(W+280))+'px';
 Q('vpi').style.transform=`scale(${1+.1*Math.max(0,Math.sin(t*4))}) rotate(${Math.sin(t*4)*6}deg)`;
 Q('vpb').style.textShadow=`0 0 ${6+8*Math.abs(Math.sin(t*2))}px rgba(100,210,255,.6)`;
};
const _r=window.render;window.render=function(t){_r(t);window.barsRender(t);};
})();
