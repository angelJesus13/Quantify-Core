/* Fuente para use_figma: syncStyleGuide(figma, modelo.json).
 * La evidencia de sincronización y revisión se registra en identidad/README.md.
 * Usa la primera página existente y añade una sección; no elimina los lienzos previos.
 * Cargar mediante use_figma con figma-use,figma-generate-design,figma-generate-library.
 */
async function syncStyleGuide(figma, model) {
  if (figma.fileKey && figma.fileKey !== model.fileKey) throw Error('Archivo Figma distinto del proyecto');
  const page = figma.root.children[0];
  await figma.setCurrentPageAsync(page);
  const prior = page.children.find(n => n.name === model.section);
  if (prior) throw Error('La sección ya existe: inspeccionarla antes de actualizar; no duplicar ni borrar');
  if (page.children.length === 0) page.name='01 · Guía de Estilos';
  const fonts = await figma.listAvailableFontsAsync();
  const weightNames = {400:'Regular',500:'Medium',600:'Semi Bold',700:'Bold'};
  for (const name of Object.values(weightNames)) {
    if (!fonts.some(f => f.fontName.family === 'Inter' && f.fontName.style === name)) throw Error('Falta Inter '+name);
  }
  await Promise.all(Object.values(weightNames).map(style => figma.loadFontAsync({family:'Inter',style})));
  const rgb = hex => ({r:parseInt(hex.slice(1,3),16)/255,g:parseInt(hex.slice(3,5),16)/255,b:parseInt(hex.slice(5,7),16)/255});
  const created = [];
  const record = n => {created.push(n.id); return n;};
  const collections = await figma.variables.getLocalVariableCollectionsAsync();
  const existingVars = await figma.variables.getLocalVariablesAsync();
  const collection = name => collections.find(c => c.name === name) || (()=>{
    const c = figma.variables.createVariableCollection(name); collections.push(c); return c;
  })();
  const primitiveCollection = collection('QC / Primitivos');
  const lightCollection = collection('QC / Claro');
  const darkCollection = collection('QC / Oscuro');
  const variables = {};
  function variable(name, coll, type, value, scopes, css) {
    let v = existingVars.find(v => v.name === name && v.variableCollectionId === coll.id);
    if (!v) {v = figma.variables.createVariable(name,coll,type); existingVars.push(v);}
    v.setValueForMode(coll.modes[0].modeId,value);v.scopes=scopes;
    v.setVariableCodeSyntax('WEB',`var(--qc-${css})`);
    variables[name]=v; return v;
  }
  for (const [key,hex] of Object.entries(model.tokens.colors)) {
    variable('qc/color/'+key,primitiveCollection,'COLOR',{...rgb(hex),a:1},[],key);
  }
  // Starter permite una modalidad: una colección por tema evita requerir una segunda modalidad.
  for (const [theme,roles] of Object.entries(model.tokens.themes)) {
    for (const [role,key] of Object.entries(roles)) {
      const css={icon:'icon-active',iconMuted:'icon-muted',statusInk:'status-ink'}[role] || role.replace(/[A-Z]/g,c=>'-'+c.toLowerCase());
      const scopes = /text|muted|onAction|statusInk/.test(role) ? ['TEXT_FILL','SHAPE_FILL','STROKE_COLOR'] : ['FRAME_FILL','SHAPE_FILL','STROKE_COLOR'];
      variable(`qc/${theme}/${role}`,theme==='light'?lightCollection:darkCollection,'COLOR',
        {type:'VARIABLE_ALIAS',id:variables['qc/color/'+key].id},scopes,css);
    }
  }
  const sizes = new Set([0,8,12,16,24,32,48]);
  for (const num of sizes) variable('qc/space/'+num,primitiveCollection,'FLOAT',num,['GAP'],'space-'+num);
  variable('qc/radius/card',primitiveCollection,'FLOAT',16,['CORNER_RADIUS'],'radius-card');
  const paint = key => figma.variables.setBoundVariableForPaint({type:'SOLID',color:rgb(model.tokens.colors[key])},'color',variables['qc/color/'+key]);
  const textStyles = await figma.getLocalTextStylesAsync();
  const styles = {};
  for (const [key,spec] of Object.entries(model.tokens.typography)) {
    const name = 'qc/type/'+key;
    const style = textStyles.find(s => s.name===name) || figma.createTextStyle();
    style.name=name;style.fontName={family:spec.family,style:weightNames[spec.weight]};style.fontSize=spec.size;
    style.lineHeight={unit:'PIXELS',value:spec.lineHeight};style.letterSpacing={unit:'PIXELS',value:0};
    styles[key]=style;
  }
  const extent=page.children.reduce((m,n)=>Math.max(m,n.x+n.width),0);
  const section = record(figma.createSection());section.name=model.section;section.x=extent+240;section.y=0;
  const assets = record(figma.createAutoLayout('VERTICAL'));assets.name='QC / Componentes Tarea 03';assets.resize(1440,100);
  assets.layoutSizingVertical='HUG';assets.itemSpacing=32;assets.x=section.x;assets.y=-2040;assets.fills=[];
  const components = {};
  function placeAsset(c) {assets.appendChild(c);return c;}
  for (const [key,path] of Object.entries(model.icons)) {
    const name='qc/icon/'+key;
    // Reutilizar el componente local compatible por nombre y tamaño antes de crear.
    let c=page.findAllWithCriteria({types:['COMPONENT']}).find(n=>n.name===name && n.width===24 && n.height===24);
    if (!c) {
      c=record(figma.createComponent());c.name=name;c.resize(24,24);c.fills=[];
      const svg=record(figma.createNodeFromSvg(`<svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="${path}" fill="none" stroke="#275BC0" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>`));
      c.appendChild(svg);svg.x=0;svg.y=0;placeAsset(c);
      c.description='Icono lineal original. Retícula 24, trazo 1.8. Instanciar con etiqueta o nombre accesible.';
    }
    components['icon/'+key]=c;
  }
  function recolor(node,key) {
    const nodes=[node,...('findAll' in node?node.findAll(()=>true):[])];
    for (const n of nodes) {
      if ('strokes' in n && Array.isArray(n.strokes) && n.strokes.length) n.strokes=n.strokes.map(p=>p.type==='SOLID'?paint(key):p);
    }
  }
  async function build(spec,parent,width) {
    if (spec.type==='text') {
      const n=record(figma.createText());parent.appendChild(n);n.name=spec.text.slice(0,72);
      n.fontName={family:'Inter',style:weightNames[model.tokens.typography[spec.style].weight]};
      await n.setTextStyleIdAsync(styles[spec.style].id);n.characters=spec.text;n.fills=[paint(spec.color)];
      n.resize(width,model.tokens.typography[spec.style].lineHeight);n.textAutoResize='HEIGHT';
      n.layoutSizingHorizontal='FIXED';return n;
    }
    if (spec.type==='icon') {
      const n=record(components['icon/'+spec.key].createInstance());parent.appendChild(n);n.rescale(spec.size/24);recolor(n,spec.color);return n;
    }
    if (spec.type==='brand') {
      const key='brand/'+spec.variant+'/'+spec.symbolOnly;
      let component=components[key];
      if (!component) {
        component=record(figma.createComponent());component.name='qc/'+key;component.layoutMode='HORIZONTAL';
        component.primaryAxisSizingMode='AUTO';component.counterAxisSizingMode='AUTO';component.itemSpacing=24;
        component.counterAxisAlignItems='CENTER';component.fills=[];
        const dark=spec.variant==='oscura',mono=spec.variant==='monocromatica';
        const ink=dark?'white':'obsidian';const color=mono?ink:dark?'skyLaser':'laserBlue';
        const svg=record(figma.createNodeFromSvg(`<svg width="72" height="72" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><path d="${model.symbol}" fill="none" stroke="${model.tokens.colors[color]}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg>`));
        component.appendChild(svg);recolor(svg,color);
        if (!spec.symbolOnly) await build({type:'text',text:'Quantify\nCore',style:'title',color:ink},component,220);
        component.description='Imagotipo/isotipo Q de Tarea 03. Mantener proporciones y área libre de 1/4. Originales heredados intactos.';
        placeAsset(component);components[key]=component;
      }
      const n=record(component.createInstance());parent.appendChild(n);return n;
    }
    if (spec.component && components[spec.component]) {
      const n=record(components[spec.component].createInstance());parent.appendChild(n);return n;
    }
    const n=record(figma.createAutoLayout(spec.direction==='horizontal'?'HORIZONTAL':'VERTICAL'));parent.appendChild(n);
    n.name=spec.name;n.resize(spec.width||width,100);n.layoutSizingHorizontal='FIXED';n.layoutSizingVertical='HUG';
    n.itemSpacing=spec.gap;n.paddingTop=n.paddingRight=n.paddingBottom=n.paddingLeft=spec.padding;
    n.fills=spec.background?[paint(spec.background)]:[];
    n.setBoundVariable('cornerRadius',variables['qc/radius/card']);
    for (const prop of ['paddingTop','paddingRight','paddingBottom','paddingLeft']) {
      if(sizes.has(spec.padding))n.setBoundVariable(prop,variables['qc/space/'+spec.padding]);
    }
    if(sizes.has(spec.gap))n.setBoundVariable('itemSpacing',variables['qc/space/'+spec.gap]);
    const inner=(spec.width||width)-2*spec.padding;
    const natural=s=>s.width || (s.type==='icon'?s.size:s.type==='brand'?(s.symbolOnly?72:316):null);
    const fixed=spec.children.reduce((s,c)=>s+(natural(c)||0),0);
    const count=spec.children.filter(c=>!natural(c)).length;
    const share=(inner-fixed-spec.gap*Math.max(0,spec.children.length-1))/Math.max(1,count);
    for(const c of spec.children)await build(c,n,c.width || (spec.direction==='horizontal'?(natural(c)||share):inner));
    if(spec.component) {
      const c=record(figma.createComponentFromNode(n));c.name='qc/'+spec.component;
      c.description='Elemento reutilizable de la pantalla de aplicación. Texto, colores e iconos editables.';
      components[spec.component]=c;
      const instance=record(c.createInstance());parent.appendChild(instance);placeAsset(c);return instance;
    }
    return n;
  }
  const frames=[];
  for (let i=0;i<model.frames.length;i++) {
    const n=await build(model.frames[i],section,1440);n.x=48+(i%3)*1504;n.y=48+Math.floor(i/3)*6400;
    frames.push({id:n.id,name:n.name,width:n.width,height:n.height});
  }
  const secondRowY=48+Math.max(...frames.slice(0,3).map(f=>f.height))+96;
  for(const f of frames.slice(3)){
    const node=await figma.getNodeByIdAsync(f.id);node.y=secondRowY;
  }
  const descendants=section.findAll(()=>true),counts={};
  for(const n of descendants)counts[n.type]=(counts[n.type]||0)+1;
  const badFonts=descendants.filter(n=>n.type==='TEXT' && (n.fontName===figma.mixed || n.fontName.family!=='Inter')).map(n=>n.id);
  const imageNodes=descendants.filter(n=>'fills' in n && Array.isArray(n.fills) && n.fills.some(p=>p.type==='IMAGE')).map(n=>n.id);
  section.resizeWithoutConstraints(3*1504+48,secondRowY+Math.max(...frames.slice(3).map(f=>f.height))+48);
  assets.y=-assets.height-240;
  return {sectionId:section.id,assetsId:assets.id,frames,counts,createdNodeIds:created,
    textStyles:Object.values(styles).map(s=>({id:s.id,name:s.name})),variableIds:Object.values(variables).map(v=>v.id),
    badFonts,imageNodes,componentIds:Object.values(components).map(c=>c.id),
    pending:['Revisar screenshot de composición y overflow','Verificar acceso por enlace con sesión sin autenticar']};
}
if(typeof module!=='undefined')module.exports={syncStyleGuide};
