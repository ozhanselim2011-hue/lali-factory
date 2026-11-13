exec(open("/home/user/lali-factory/jobs/_vo4/full.py").read())
HTML='''<div class="card" id="c1" style="background:#000">
 <div id="bg1" class="ab" style="inset:0"></div><div id="city" class="ab" style="left:0;right:0;top:250px;height:400px"></div>
 <div id="ex1" class="ab" style="border-radius:50%;background:radial-gradient(circle,#fff,#ffd60a 18%,#ff6a00 40%,rgba(255,40,0,0) 68%);opacity:0"></div>
 <div class="ch" data-p="a"></div><div class="ch" data-p="b" data-c="#8e8e93,#c8c8cc,#8e8e93"></div>
 <div id="ttl1" class="big" style="top:400px;font-size:170px;color:#ffd27a;text-shadow:0 0 50px #ff9f0a;opacity:0;font-style:italic;z-index:8">ВО МНЕ<br>ВСЕ 4</div>
 <div id="fz1" class="ab" style="left:60px;right:60px;top:190px;font:italic 800 40px Inter;color:#fff;text-shadow:0 3px 8px #000;opacity:0;z-index:21">Да, это я. Наверное, вам интересно, как я здесь оказался…</div>
 <div id="cr1" class="ab" style="left:0;right:0;top:1080px;text-align:center;font:800 50px Inter;color:#fff;line-height:1.5;z-index:8"><div style="font-size:30px;opacity:.6">в главной роли</div>ЛАЛИ<div style="font-size:30px;opacity:.6;margin-top:24px">в роли всех четырёх</div>ТОЖЕ ЛАЛИ<div style="font-size:30px;opacity:.6;margin-top:24px">оценка критиков</div><span style="color:#ffd60a;font-size:110px">4/5</span></div>
 <div class="ab" style="left:0;right:0;top:0;height:170px;background:#000;z-index:20"></div><div class="ab" style="left:0;right:0;bottom:0;height:130px;background:#000;z-index:20"></div>
</div>'''
B2='''(function(){let s='';for(let i=0;i<14;i++){const w=60+rnd(i)*90,h=150+rnd(i+20)*250,x=i*80-20;let win='';for(let k=0;k<12;k++)win+=`<div style="position:absolute;left:${10+(k%3)*((w-20)/3)}px;top:${15+Math.floor(k/3)*35}px;width:12px;height:16px;background:${rnd(i*7+k)>.5?'#ffd27a':'#1a2335'}"></div>`;s+=`<div style="position:absolute;left:${x}px;bottom:0;width:${w}px;height:${h}px;background:#0f1726">${win}</div>`;}$('city').innerHTML=s;})();'''
R='''
 let T=t;const fr=t>=10.0&&t<10.95;if(fr)T=10.0;const ce=$('c1');const sun=T>=10.95&&T<13.15;
 $('bg1').style.background=T>=13.15?'#000':(sun?'linear-gradient(180deg,#ff7e5f,#feb47b 58%,#3a2a3a 60%)':'linear-gradient(180deg,#0b1a2e,#1d2b45 60%,#0b0b12 60%)');
 $('city').style.opacity=T>=13.15?0:1;
 {const k=seg(T,7.0,7.5),w=2400*eo(k);const E=$('ex1');E.style.width=E.style.height=w+'px';E.style.left=(540-w/2)+'px';E.style.top=(600-w/2)+'px';E.style.opacity=T>=7.0?1-seg(T,7.35,7.7):0;}
 $('ch_a').style.display=T>=13.15?'none':'block';
 if(T<4.4){place('a',lerp(-120,540,seg(T,0.3,3.3)),900,1.9,false);pose('a',T<3.3?walk(T,7):{aL:8,aR:-8});}
 else if(T<7.6){const k=seg(T,4.4,7.6);place('a',540,lerp(900,1150,k),lerp(1.9,3.2,k),false);pose('a',walk(T,5));}
 else if(T<10.95){place('a',lerp(540,360,eo(seg(T,7.75,8.4))),900,1.9,false);pose('a',{aL:8,aR:-8,hd:T>=9.0?16:0});}
 else{place('a',540,900,2.0,false);pose('a',{aL:150+Math.sin(T*2)*8,aR:-150-Math.sin(T*2)*8,hd:-8,bob:Math.sin(T*2.5)*5});}
 const rv=T>=7.75&&T<10.95;$('ch_b').style.display=rv?'block':'none';if(rv){place('b',lerp(1250,760,eo(seg(T,7.75,8.4))),900,1.9,true);pose('b',dn(T,12.57,.6));}
 $('ttl1').style.opacity=seg(T,3.5,3.7)*(1-seg(T,4.3,4.5));$('ttl1').style.transform=`scale(${lerp(1.4,1,eo(seg(T,3.5,4.0)))})`;
 $('fz1').style.opacity=fr?1:0;if(fr)ce.style.filter='sepia(.9) contrast(1.1)';
 $('cr1').style.top=lerp(1080,200,seg(t,13.2,14.4))+'px';
 if(T>=7&&T<7.6)ce.style.transform+=` translate(${Math.sin(t*90)*14}px,${Math.cos(t*70)*10}px)`;
'''
FIN()
