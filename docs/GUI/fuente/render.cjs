/* Exportación de las escenas de generar.py con la misma fuente Inter local.
   Requiere Playwright disponible en el entorno de autoría; no lo instala. */
const fs = require('node:fs');
const path = require('node:path');
const {pathToFileURL} = require('node:url');
const {chromium} = require('playwright');
const root = path.resolve(__dirname,'..');
const scenes = JSON.parse(fs.readFileSync(path.join(root,'.build/escenas.json'),'utf8'));
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.QC_CHROME?{executablePath:process.env.QC_CHROME}:{})});
 try {
  const page=await browser.newPage({deviceScaleFactor:1});
  const font=fs.readFileSync(path.join(root,'assets/inter.woff2')).toString('base64');
  const failures=[];
  for(const [filename,svg] of Object.entries(scenes)){
   if(process.env.QC_IDENTITY_ONLY==='1'&&!filename.startsWith('identidad/imagenes/'))continue;
   if(process.env.QC_MOBILE_ONLY==='1'&&!filename.startsWith('prototipos/movil/'))continue;
   const width=Number(svg.match(/width="(\d+)"/)[1]),height=Number(svg.match(/height="(\d+)"/)[1]);
   const html=`<!doctype html><meta charset="utf-8"><style>@font-face{font-family:Inter;src:url(data:font/woff2;base64,${font});font-weight:100 900}*{box-sizing:border-box}body{margin:0}svg{display:block}svg[data-fidelity="sketch"],svg[data-fidelity="wireframe"]{filter:grayscale(1)}</style>${svg}`;
   const temp=path.join(root,'.build/current.html');fs.writeFileSync(temp,html);
   await page.setViewportSize({width,height});await page.goto(pathToFileURL(temp).href);
   await page.evaluate(async()=>{await document.fonts.load('16px Inter');await document.fonts.ready;});
   if(!(await page.evaluate(()=>document.fonts.check('16px Inter'))))throw Error('Inter no cargó');
   const overflow=await page.evaluate(()=>{const s=document.querySelector('svg'),v=s.viewBox.baseVal;return [...s.querySelectorAll('text')].filter(t=>{const b=t.getBBox();return b.x<0||b.y<0||b.x+b.width>v.width||b.y+b.height>v.height}).map(t=>t.textContent);});
   const blockOverflow=await page.evaluate(()=>[...document.querySelectorAll('g[data-block]')].flatMap(g=>{
    const [x,y,w,h]=g.dataset.box.split(',').map(Number);
    return [...g.querySelectorAll('text')].filter(t=>{const b=t.getBBox();return b.x<x-1||b.y<y-1||b.x+b.width>x+w+1||b.y+b.height>y+h+1;}).map(t=>g.dataset.block+': '+t.textContent);
   }));
   if(overflow.length||blockOverflow.length){failures.push({filename,canvas:overflow,blocks:blockOverflow});continue;}
   const out=path.join(root,filename);fs.mkdirSync(path.dirname(out),{recursive:true});
   await page.locator('body > svg').screenshot({path:out,timeout:20000});
   console.log(filename);
  }
  if(failures.length)throw Error('Desbordamientos: '+JSON.stringify(failures));
 } finally {await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
