// Paso posterior a syncStyleGuide y al traslado de los prototipos.
// Recibe los IDs devueltos por esas operaciones; conserva los nodos editables.
async function organizarLienzos(figma, { sectionId, assetsId, frames, originalsId, prototypePageIds }) {
  for (const style of ['Regular', 'Medium', 'Semi Bold', 'Bold']) {
    await figma.loadFontAsync({ family: 'Inter', style });
  }

  const titles = [
    '01 · Guía de Estilos · Identidad Gráfica',
    '02 · Guía de Estilos · Paleta de Colores',
    '03 · Guía de Estilos · Tipografía',
    '04 · Guía de Estilos · Iconografía de Navegación',
    '05 · Guía de Estilos · Acciones y Estados',
    '06 · Guía de Estilos · Aplicación de Estilos',
  ];
  if (frames.length !== titles.length) throw new Error('La guía requiere seis frames');
  const createdNodeIds = [];
  const mutatedNodeIds = [];
  const firstPage = figma.root.children[0];
  firstPage.name = titles[0];
  mutatedNodeIds.push(firstPage.id);

  for (let index = 1; index < frames.length; index++) {
    const board = await figma.getNodeByIdAsync(frames[index].id);
    if (!board || board.name !== frames[index].name) throw new Error(`Falta el frame ${index + 1}`);
    let page = figma.root.children.find(node => node.name === titles[index]);
    if (!page) {
      page = figma.createPage();
      page.name = titles[index];
      createdNodeIds.push(page.id);
    }
    if (board.parent !== page) {
      page.appendChild(board);
      board.x = 80;
      board.y = 80;
      mutatedNodeIds.push(board.id);
    }
    figma.root.insertChild(index, page);
    mutatedNodeIds.push(page.id);
  }

  const section = await figma.getNodeByIdAsync(sectionId);
  const identity = await figma.getNodeByIdAsync(frames[0].id);
  if (!section || section.type !== 'SECTION' || !identity || section.children.length !== 1 || section.children[0] !== identity) {
    throw new Error('La primera sección debe contener solo Identidad Gráfica');
  }
  section.x = 80;
  section.y = 80;
  section.resizeWithoutConstraints(identity.width + 96, identity.height + 96);
  mutatedNodeIds.push(section.id);

  const stages = ['07 · Sketches', '08 · Wireframes', '09 · Mockups'];
  if (prototypePageIds.length !== stages.length) throw new Error('Faltan páginas de prototipos');
  for (let index = 0; index < stages.length; index++) {
    const page = figma.root.children.find(node => node.id === prototypePageIds[index]);
    if (!page) throw new Error(`Falta la página ${stages[index]}`);
    page.name = stages[index];
    figma.root.insertChild(index + 6, page);
    mutatedNodeIds.push(page.id);
  }

  let resources = figma.root.children.find(node => node.name === '10 · Recursos y componentes');
  if (!resources) {
    resources = figma.createPage();
    resources.name = '10 · Recursos y componentes';
    createdNodeIds.push(resources.id);
  }
  const components = await figma.getNodeByIdAsync(assetsId);
  const originals = await figma.getNodeByIdAsync(originalsId);
  if (!components || !originals) throw new Error('Faltan recursos originales o componentes');
  if (components.parent !== resources) resources.appendChild(components);
  if (originals.parent !== resources) resources.appendChild(originals);
  components.x = 80;
  components.y = 80;
  originals.x = 1600;
  originals.y = 80;
  figma.root.insertChild(9, resources);
  mutatedNodeIds.push(components.id, originals.id, resources.id);

  return {
    createdNodeIds,
    mutatedNodeIds: [...new Set(mutatedNodeIds)],
    pages: figma.root.children.map(page => ({ id: page.id, name: page.name })),
  };
}

if (typeof module !== 'undefined') module.exports = { organizarLienzos };
