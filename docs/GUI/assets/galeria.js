'use strict';
(() => {
  const screens=JSON.parse(document.getElementById('screen-data').textContent);
  const grid=document.getElementById('prototype-grid'),format=document.getElementById('format');
  const dialog=document.getElementById('viewer'),full=document.getElementById('full-image');
  let fidelity='mockup',theme='light',activeCards=[],current=0,opener;
  const notes={sketch:'Baja fidelidad: únicamente formas y trazos, sin letras ni contenido. La descripción de cada pantalla queda fuera de la imagen.',wireframe:'Fidelidad media: estructura funcional en grises, con etiquetas y contenido de referencia. Sin fotografía ni identidad gráfica.',mockup:'Alta fidelidad: Inter, firma Quantify Core, color, iconos, fotografía y componentes consistentes. Diseños estáticos con datos sintéticos.'};
  function showImage(index){
    current=(index+activeCards.length)%activeCards.length;
    const card=activeCards[current];full.src=card.dataset.image;full.alt=card.dataset.title;
    full.classList.remove('zoomed');document.getElementById('zoom').setAttribute('aria-pressed','false');document.getElementById('zoom').textContent='Ampliar';
    document.getElementById('viewer-title').textContent=card.dataset.title;
    document.getElementById('viewer-description').textContent=card.dataset.description;
    document.getElementById('download').href=card.dataset.image;
    document.querySelector('.image-viewport').scrollTo(0,0);
  }
  function bindCards(){
    document.querySelectorAll('.image-card').forEach(card=>{
      card.onclick=()=>{
        const container=card.closest('.identity-grid,.prototype-grid');activeCards=[...container.querySelectorAll('.image-card')];opener=card;
        showImage(activeCards.indexOf(card));dialog.showModal();document.body.classList.add('modal-open');
      };
    });
  }
  function render(){
    grid.replaceChildren();
    const desktop=format.value==='desktop';grid.classList.toggle('desktop',desktop);
    document.getElementById('fidelity-note').textContent=notes[fidelity];
    document.querySelectorAll('[data-theme]').forEach(b=>b.disabled=fidelity!=='mockup');
    if(fidelity!=='mockup'&&desktop){format.value='mobile';return render();}
    format.disabled=fidelity!=='mockup';
    const visible=desktop?screens.filter(s=>['hoy','administracion'].includes(s.id)):screens;
    for(const s of visible){
      const folder={sketch:'sketches',wireframe:'wireframes',mockup:'mockups'}[fidelity];
      const name=s.id==='hoy'&&desktop?'hoy-escritorio':s.id;
      const file=`prototipos/${folder}/${name}-${fidelity==='mockup'?theme:'light'}.png`;
      const card=document.createElement('button');card.className='image-card';card.dataset.image=file;card.dataset.title=s.title;card.dataset.description=`${s.rf} · ${s.note}`;
      const img=document.createElement('img');img.src=file;img.alt=`${fidelity}: ${s.title}, ${fidelity==='mockup'?theme:'grises'}`;img.width=s.id==='administracion'||desktop?1440:390;img.height=s.id==='administracion'||desktop?900:844;
      const caption=document.createElement('span'),title=document.createElement('b'),sub=document.createElement('small');title.textContent=s.title;sub.textContent=`${s.rf} · ${s.id==='administracion'||desktop?'Escritorio':'Móvil'}`;
      caption.append(title,sub);card.append(img,caption);grid.append(card);
    }
    bindCards();
  }
  document.querySelectorAll('[data-fidelity]').forEach(b=>b.addEventListener('click',()=>{fidelity=b.dataset.fidelity;document.querySelectorAll('[data-fidelity]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));render();}));
  document.querySelectorAll('[data-theme]').forEach(b=>b.addEventListener('click',()=>{theme=b.dataset.theme;document.querySelectorAll('[data-theme]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));render();}));
  format.addEventListener('change',render);
  document.getElementById('previous').addEventListener('click',()=>showImage(current-1));document.getElementById('next').addEventListener('click',()=>showImage(current+1));
  document.getElementById('zoom').addEventListener('click',e=>{const on=full.classList.toggle('zoomed');e.currentTarget.setAttribute('aria-pressed',String(on));e.currentTarget.textContent=on?'Ajustar':'Ampliar';});
  document.getElementById('close').addEventListener('click',()=>dialog.close());
  dialog.addEventListener('close',()=>{document.body.classList.remove('modal-open');opener?.focus();});
  dialog.addEventListener('keydown',e=>{if(e.key==='ArrowRight'){e.preventDefault();showImage(current+1);}if(e.key==='ArrowLeft'){e.preventDefault();showImage(current-1);}});
  render();
})();
