'use strict';
// Únicamente selecciona la variante del mismo logo; no cambia el tema de la UI.
(() => {
  const root=document.documentElement;
  function sync(){
    const theme=root.getAttribute('data-theme')||'light';
    const dark=theme.includes('dark')||['cognitive','behavioral'].includes(theme);
    document.querySelectorAll('img[data-brand-dark]').forEach(img=>{
      if(!img.dataset.brandLight)img.dataset.brandLight=img.getAttribute('src');
      const src=dark?img.dataset.brandDark:img.dataset.brandLight;
      if(img.getAttribute('src')!==src)img.setAttribute('src',src);
      img.dataset.brandOnDark=String(dark);
    });
  }
  sync();
  new MutationObserver(sync).observe(root,{attributes:true,attributeFilter:['data-theme']});
})();
