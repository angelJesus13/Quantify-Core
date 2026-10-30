/* Importa un lote del catálogo anterior. No importa PNG de interfaces. */
async function importPrototypeBatch(figma, pageId, stage, screens, assets) {
  const page=await figma.getNodeByIdAsync(pageId);await figma.setCurrentPageAsync(page);
  const sketch=stage.startsWith('sketch'),wire=stage.startsWith('wireframe');
  // Arial no está disponible en el motor remoto; Arimo es la alternativa neutra.
  const family=wire?'Arimo':'Inter';
  const fontStyles=wire?{400:'Regular',600:'Bold',700:'Bold'}:{400:'Regular',600:'Semi Bold',700:'Bold'};
  await Promise.all([...new Set(Object.values(fontStyles))].map(style=>figma.loadFontAsync({family,style})));
  const rgb=hex=>({r:parseInt(hex.slice(1,3),16)/255,g:parseInt(hex.slice(3,5),16)/255,b:parseInt(hex.slice(5,7),16)/255});
  const created=[],frames=[];
  for(const spec of screens){
    const name=`${String(spec.number).padStart(2,'0')} ${spec.title} / ${stage}`;
    if(page.children.some(n=>n.name===name))throw Error('Vista ya existente: '+name);
    const f=figma.createFrame();created.push(f.id);page.appendChild(f);f.name=name;f.resize(390,844);
    f.x=((spec.number-1)%5)*454;f.y=160+Math.floor((spec.number-1)/5)*984+(stage==='mockup/dark'?4200:0);f.clipsContent=true;
    const svg=figma.createNodeFromSvg(spec.vector);created.push(svg.id);f.appendChild(svg);svg.x=0;svg.y=0;
    for(const [x,y,value,size,weight,hex] of spec.texts){
      const t=figma.createText();created.push(t.id);f.appendChild(t);t.name=value.slice(0,64);
      t.fontName={family,style:fontStyles[weight]||fontStyles[400]};t.fontSize=size;t.lineHeight={unit:'PIXELS',value:size};
      t.characters=value;t.fills=[{type:'SOLID',color:rgb(hex)}];t.x=x;t.y=y-size*.82;
    }
    for(const item of spec.images){
      const [key,x,y,w,h,iw,ih,ix,iy]=item;
      const wrap=figma.createFrame();created.push(wrap.id);f.appendChild(wrap);wrap.name='Activo / '+key;
      wrap.resize(w,h);wrap.x=x;wrap.y=y;wrap.clipsContent=true;wrap.fills=[];
      const img=figma.createRectangle();created.push(img.id);wrap.appendChild(img);img.name=key;
      img.resize(iw||w,ih||h);img.x=ix||0;img.y=iy||0;
      img.fills=[{type:'IMAGE',imageHash:assets[key],scaleMode:key==='photo'?'FILL':'FIT'}];
      if(key==='photo')wrap.cornerRadius=14;
    }
    if(!sketch){
      for(const [x,y,w,h,target]of spec.targets){
        const hot=figma.createRectangle();created.push(hot.id);f.appendChild(hot);hot.name='Destino / '+target;
        hot.resize(w,h);hot.x=x;hot.y=y;hot.fills=[{type:'SOLID',color:{r:1,g:1,b:1},opacity:0}];
      }
      for(let i=0;i<4;i++){
        const target=['hoy','habitos','analisis','ajustes'][i];const hot=figma.createRectangle();created.push(hot.id);
        f.appendChild(hot);hot.name='Destino / '+target;hot.resize(94,70);hot.x=i*94;hot.y=774;
        hot.fills=[{type:'SOLID',color:{r:1,g:1,b:1},opacity:0}];
      }
    }
    frames.push({id:f.id,key:spec.id,stage,name:f.name,width:f.width,height:f.height,
      textCount:f.findAllWithCriteria({types:['TEXT']}).length,imageCount:spec.images.length});
  }
  return {frames,createdNodeIds:created};
}
if(typeof module!=='undefined')module.exports={importPrototypeBatch};
