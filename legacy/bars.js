const { chromium } = require('playwright');const path=require('path');
(async()=>{const [,,song,out]=process.argv;const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:300}});
await p.goto('file://'+path.resolve('ava/bars.html'));
if(song==='__vpn'){await (await p.$('#vpn')).screenshot({path:out,omitBackground:true});}
else{await p.evaluate(s=>{const [a,t]=s.split(' — ');document.getElementById('sn').innerHTML=t?`${a} <span>— ${t}</span>`:a},song);await (await p.$('#np')).screenshot({path:out,omitBackground:true});}
await b.close();})();
