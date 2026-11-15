DUR=12.4
FADE=12.0
START=0
SONG='Miyagi & Эндшпиль — No contest'
BG='linear-gradient(180deg,#0e0e10,#050506)'
SUBW='900'
SUBX='text-transform:uppercase'
LINES=[
 [["Это",0.0],["жирный",0.2],["юг,",0.8],["мы",1.26],["не",1.36],["East",1.52],["и",1.86],["не",2.12],["West",2.28]],
 [["Среди",2.64],["бетонных",3.36],["плит",3.96],["тут",4.28],["виниловый",4.52],["треск",5.3]],
 [["Следи",6.1],["за",6.56],["правилами",6.9],["здешних",7.8],["мест",8.62]],
 [["Твоя",9.0],["бравада",9.74],["неуместна,",10.28],["no",11.18],["contest",11.42]],
]
SC=[[-0.3,2.55],[2.55,6.0],[6.0,8.9],[8.9,99]]
GLOW=['#6a4a0a','#3a3a3a','#1d3a7a','#7a0a0a']
PEMO=['🧭','💿','📜','🥊']
END=[12.0,12.4]
CSS='.ch{position:absolute;width:200px;height:300px;transform-origin:100px 290px;z-index:5}'
HTML='''
<div class="card" id="c1" style="background:radial-gradient(circle at 50% 40%,#2a2410,#0a0904)">
 <div class="hdr" style="color:#ffd60a">Компас</div>
 <div style="position:absolute;left:150px;top:90px;width:300px;height:300px;border-radius:50%;border:10px solid #ffd60a;background:#14120a"></div>
 <div id="e1" style="position:absolute;left:400px;top:215px;font-size:40px;font-weight:900;color:#8e8e93">E</div><div id="w1" style="position:absolute;left:175px;top:215px;font-size:40px;font-weight:900;color:#8e8e93">W</div>
 <div style="position:absolute;left:287px;top:105px;font-size:40px;font-weight:900;color:#8e8e93">N</div>
 <div id="nd1" style="position:absolute;left:290px;top:115px;width:20px;height:250px;transform-origin:10px 125px;background:linear-gradient(#8e8e93 50%,#ff453a 50%);clip-path:polygon(50% 0,100% 50%,50% 100%,0 50%)"></div>
 <div id="s1" class="c" style="top:405px;font-size:90px;color:#ffd60a;font-weight:300">ЮГ</div>
 <div class="ch" data-p="a"></div>
</div>
<div class="card" id="c2" style="background:#6e6e70;background-image:linear-gradient(#58585a 4px,transparent 4px),linear-gradient(90deg,#58585a 4px,transparent 4px);background-size:200px 160px">
 <div id="vn2" style="position:absolute;left:150px;top:80px;width:300px;height:300px;border-radius:50%;background:repeating-radial-gradient(circle,#111 0 3px,#222 3px 6px);box-shadow:0 20px 40px rgba(0,0,0,.5)"><div style="position:absolute;left:105px;top:105px;width:90px;height:90px;border-radius:50%;background:#ff453a;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:18px">ЮГ</div></div>
 <div id="cr2" style="position:absolute;inset:0"></div>
 <div class="ch" data-p="b"></div>
</div>
<div class="card" id="c3" style="background:#f4ecd8;color:#2a1f10">
 <div class="hdr" style="color:rgba(0,0,0,.5)">Доска объявлений</div><div class="ttl" style="color:#2a1f10">Правила района</div>
 <div id="rl3" style="position:absolute;left:40px;right:40px;top:170px;font-size:30px;font-weight:800;line-height:1.9"></div>
 <div id="st3" style="position:absolute;left:300px;top:400px;border:8px solid #d0021b;border-radius:16px;padding:6px 16px;font-size:40px;font-weight:900;color:#d0021b;transform:rotate(-10deg);opacity:0">СОБЛЮДАТЬ</div>
 <div class="ch" data-p="c"></div>
</div>
<div class="card" id="c4" style="background:#1c1c1e">
 <div style="position:absolute;left:30px;right:30px;top:420px;height:20px;background:#ff453a;border-radius:4px"></div>
 <div id="bg4" style="position:absolute;left:30px;right:30px;top:40px;background:#111;border:4px solid #ffd60a;border-radius:16px;padding:12px;text-align:center;font-size:24px;font-weight:900;color:#ffd60a">ВЫЗОВ ПРИНЯТ?</div>
 <div id="nc4" class="c" style="top:150px;font-size:76px;font-weight:900;color:#fff;opacity:0;text-shadow:0 6px 0 #ff453a">NO CONTEST</div>
 <div id="un4" style="position:absolute;left:330px;top:240px;background:#ff453a;border-radius:12px;padding:6px 14px;font-size:26px;font-weight:900;opacity:0">❌ неуместно</div>
 <div class="ch" data-p="d"></div><div class="ch" data-p="e"></div>
</div>
'''
BUILD=open(HELPERS).read()+"const dn=(t,k=12.57,a=1)=>{const q=Math.sin(t*k);return {aL:(110+q*40)*a,aR:(-110+q*40)*a,lL:q*14*a,lR:-q*14*a,hd:q*8*a,bob:-Math.abs(q)*14*a}};"+'''
(function(){document.querySelectorAll('.ch').forEach(e=>{const p=e.dataset.p;e.id='ch_'+p;e.innerHTML=CH(p,...(p=='e'?['#8e8e93','#c8c8cc','#8e8e93']:['#111','#ffd60a','#ff9f0a']));});})();'''
RENDER='''
 {const a=t<0.8?t*900:(t<1.5?180+Math.sin(t*30)*8:180+Math.sin(t*30)*8);$('nd1').style.transform=`rotate(${a}deg)`;$('s1').style.fontWeight=t>=0.2?900:300;$('s1').style.transform=`scale(${1+.3*pop(t,0.2,6)})`;
  $('e1').style.textDecoration=t>=1.52?'line-through':'none';$('e1').style.color=t>=1.52?'#ff453a':'#8e8e93';$('w1').style.textDecoration=t>=2.28?'line-through':'none';$('w1').style.color=t>=2.28?'#ff453a':'#8e8e93';
  place('a',480,690,.85,true);pose('a',t>=0.8?{aL:8,aR:30,hd:10}:{aL:8,aR:-8});}
 {$('vn2').style.transform=`rotate(${t*200+(t>=4.52?Math.sin(t*25)*25:0)}deg)`;let c='';if(t>=5.3)for(let i=0;i<8;i++){const p=((t-5.3)*2+rnd(i))%1;c+=`<div style="position:absolute;left:${120+rnd(i+1)*360}px;top:${80+rnd(i+4)*300}px;font-size:28px;font-weight:900;color:#ffd60a;opacity:${1-p}">трр</div>`}$('cr2').innerHTML=c;
  place('b',300,690,1.0,false);pose('b',t>=4.52?{aL:8,aR:-150+Math.sin(t*25)*25,hd:Math.sin(t*12.57)*8,bob:-Math.abs(Math.sin(t*12.57))*6}:dn(t,6,.4));}
 {const R=[[6.1,'1. не East'],[6.9,'2. не West'],[7.8,'3. только юг'],[8.62,'4. см. п. 3']];$('rl3').innerHTML=R.filter(r=>t>=r[0]).map(r=>`<div style="opacity:${seg(t,r[0],r[0]+.1)}">${r[1]}</div>`).join('');
  $('st3').style.opacity=seg(t,8.62,8.7);$('st3').style.transform=`rotate(-10deg) scale(${lerp(2,1,eb(seg(t,8.62,8.85)))})`;
  place('c',480,690,.85,true);pose('c',{aL:8,aR:t>=6.1?-90:-8,hd:-5});}
 {const fl=t<10.28;place('e',430,690,1.0,true);pose('e',fl?{aL:150,aR:-150,open:1,bob:-Math.abs(Math.sin(t*8))*8}:{aL:8,aR:-8,hd:-15});$('ch_e').style.transform+=` scale(${t>=11.18?lerp(1,.6,seg(t,11.18,11.6)):1})`;
  place('d',160,690,1.0,false);pose('d',t>=11.18?{aL:60,aR:-60,hd:10,open:1}:{aL:8,aR:-8,hd:t>=9.74?10:0});
  $('un4').style.opacity=seg(t,10.28,10.35);$('nc4').style.opacity=seg(t,11.18,11.25);$('nc4').style.transform=`scale(${lerp(2,1,eb(seg(t,11.18,11.45)))}) rotate(-4deg)`;$('bg4').textContent=t>=11.18?'БОЙ ОТМЕНЁН':'ВЫЗОВ ПРИНЯТ?';}
'''
