/* Render y QA de la guía: necesita Playwright en el entorno de autoría. */
const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
const {chromium}=require('playwright');
const out=path.resolve(__dirname,'../identidad/guia');
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.QC_CHROME?{executablePath:process.env.QC_CHROME}:{})});
 try{
  const page=await browser.newPage({viewport:{width:1520,height:1000},deviceScaleFactor:1});
  await page.goto(pathToFileURL(path.join(out,'index.html')).href);
  await page.evaluate(async()=>{await document.fonts.load('16px Inter');await document.fonts.ready;});
  const errors=await page.evaluate(()=>{
   const failures=[];
   if(!document.fonts.check('16px Inter'))failures.push('Inter no cargó');
   for(const f of document.querySelectorAll('[data-artboard]')){
    const bounds=f.getBoundingClientRect();
    for(const el of f.querySelectorAll('.text,.brand-sample,svg')){
     const r=el.getBoundingClientRect();
     if(r.left<bounds.left-1||r.right>bounds.right+1||r.bottom>bounds.bottom+1)failures.push(f.getAttribute('aria-label')+': '+el.textContent);
     if(el.classList.contains('text')&&el.scrollWidth>el.clientWidth+1)failures.push('Texto desbordado: '+el.textContent);
     if(el.classList.contains('text')&&getComputedStyle(el).fontFamily.split(',')[0]!=='Inter')failures.push('Fuente incorrecta');
    }
   }
   return failures;
  });
  if(errors.length)throw Error(JSON.stringify(errors));
  const boards=page.locator('[data-artboard]');
  const evidence=[];
  for(let i=0;i<await boards.count();i++){
   const node=boards.nth(i),file=`0${i+1}.png`;
   await node.screenshot({path:path.join(out,file),timeout:30000});
   const {width,height}=await node.boundingBox();
   evidence.push({frame:await node.getAttribute('aria-label'),file,width,height});
  }
  // Contacto para revisión visual; los PNG nunca se importan como UI de Figma.
  fs.writeFileSync(path.join(out,'validacion.json'),JSON.stringify({font:'Inter',overflow:errors,frames:evidence},null,2)+'\n');
  console.log(JSON.stringify(evidence));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
