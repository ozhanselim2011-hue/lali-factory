const { chromium } = require('playwright');const path=require('path');
(async()=>{const [,,html,out,dur,times]=process.argv;
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1080},deviceScaleFactor:1});
 await p.goto('file://'+path.resolve(html));await p.waitForTimeout(500);
 if(times){for(const t of times.split(',').map(Number)){await p.evaluate(t=>render(t),t);await p.screenshot({path:`${out}/t_${String(Math.round(t*100)).padStart(5,'0')}.png`});}}
 else{const N=Math.round(+dur*30);for(let i=0;i<N;i++){await p.evaluate(t=>render(t),i/30);await p.screenshot({path:`${out}/f_${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:92});}}
 await b.close();})();
