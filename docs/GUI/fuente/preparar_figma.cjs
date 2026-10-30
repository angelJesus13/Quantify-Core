/* Empaqueta el modelo sin perder contenido para el límite de 50 000 caracteres. */
const fs=require('node:fs');
const path=require('node:path');
const gui=path.resolve(__dirname,'..');
const model=JSON.parse(fs.readFileSync(path.join(gui,'identidad/guia/modelo.json'),'utf8'));
const source=fs.readFileSync(path.join(__dirname,'figma_guia.js'),'utf8')
 .replace(/\/\*[\s\S]*?\*\//g,'').replace(/^\s*\/\/.*$/gm,'');
function pack(n){
 if(n.type==='text')return [0,n.text,n.style,n.color];
 if(n.type==='icon')return [1,n.key,n.color,n.size];
 if(n.type==='brand')return [2,n.variant,n.symbolOnly];
 return [3,n.children.map(pack),n.direction,n.width,n.background,n.padding,n.gap,n.name,!!n.artboard,n.component||null];
}
const decoder=`function unpack(n){if(n[0]===0)return {type:'text',text:n[1],style:n[2],color:n[3]};if(n[0]===1)return {type:'icon',key:n[1],color:n[2],size:n[3]};if(n[0]===2)return {type:'brand',variant:n[1],symbolOnly:n[2]};return {type:'box',children:n[1].map(unpack),direction:n[2],width:n[3],background:n[4],padding:n[5],gap:n[6],name:n[7],artboard:n[8],component:n[9]};}`;
const packed={...model,frames:model.frames.map(pack)};
const code=source+'\n'+decoder+'\nconst model='+JSON.stringify(packed)+';model.frames=model.frames.map(unpack);return await syncStyleGuide(figma,model);';
if(code.length>50000)throw Error('El código excede el límite de use_figma: '+code.length);
const target=path.join(gui,'.build/figma-guia-call.js');fs.mkdirSync(path.dirname(target),{recursive:true});
fs.writeFileSync(target,code);console.log(code.length+' caracteres; salida: docs/GUI/.build/figma-guia-call.js');
