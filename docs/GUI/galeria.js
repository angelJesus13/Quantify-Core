'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const screens = window.QC_SCREENS;
  const states = {
    base: ['Vista base', 'Lámina estática de composición; datos de ejemplo.'],
    loading: ['Cargando información', 'Conservar el contexto. Anunciar la carga; no dibujar una tendencia ni permitir otro envío mientras el primero está pendiente.'],
    empty: ['Todavía no hay datos', 'En Hoy, ofrecer crear un hábito; en Análisis, elegir periodo. Sin oportunidades significa «sin datos», no 0 % de fracaso.'],
    validation: ['Revisa el nombre del hábito', 'Campo requerido. Mantener el borrador, asociar la ayuda al campo y mover el foco al primer dato inválido en la implementación.'],
    error: ['No pudimos obtener la información', 'Conservar el contexto y ofrecer reintentar. Si se perdió la respuesta de una escritura, no afirmar que falló: consultar o reintentar con la misma clave.'],
    pending: ['Avance pendiente de sincronizar', 'Variante futura, condicionada a soporte offline aprobado. Separar valor local y confirmado; hasta implementar cola segura, exigir conexión para guardar.'],
    conflict: ['Este hábito cambió en otro dispositivo', 'Revisar la versión actual y comparar el borrador antes de volver a enviar. No sobrescribir automáticamente ni elegir por el reloj del cliente.'],
    expired: ['Tu sesión terminó', 'Iniciar sesión con Keycloak y retornar a una ruta autorizada. No revelar datos privados tras cerrar la sesión.'],
    denied: ['Tu cuenta no tiene acceso a esta acción', 'Volver a una sección permitida. La API comprueba permisos y pertenencia; una lámina administrativa no concede acceso.']
  };
  const flows = {acceso:['hoy'],hoy:['habito','registro','analisis','sugerencias','ajustes'],habito:['registro','hoy'],registro:['habito','analisis','hoy'],analisis:['registro','hoy'],sugerencias:['habito','ajustes','hoy'],ajustes:['hoy'],administracion:['administracion']};
  for (const s of screens) $('screen').add(new Option(s.title,s.id));
  $('screen').value='hoy';
  function render() {
    const s=screens.find(s=>s.id===$('screen').value);
    const fidelity=$('fidelity').value;
    const theme=$('theme').value;
    $('theme').disabled=fidelity!=='mockup';
    $('format').disabled=s.id!=='hoy'||fidelity!=='mockup';
    const desktop=s.id==='administracion'||(s.id==='hoy'&&fidelity==='mockup'&&$('format').value==='desktop');
    const filename=s.id==='hoy'&&desktop?`mockups/hoy-escritorio-${theme}.svg`:s.variants[`${fidelity}-${fidelity==='mockup'?theme:'light'}`];
    document.documentElement.dataset.theme=theme;
    $('preview').src=filename;
    $('preview').alt=`${fidelity}: ${s.title}; ${desktop?'escritorio':'móvil'}; ${fidelity==='mockup'?theme:'escala de grises'}. ${s.note}`;
    $('preview').className=desktop?'desktop':'mobile';
    $('preview').width=desktop?1440:390;
    $('preview').height=desktop?900:844;
    $('download').href=filename;
    $('caption').textContent=`${s.id.toUpperCase()} / ${fidelity.toUpperCase()}`;
    $('dimensions').textContent=desktop?'1440 × 900':'390 × 844';
    $('screen-title').textContent=s.title;
    $('reference').textContent=`${s.rf} · Referencia académica: ${s.reference}`;
    $('note').textContent=s.note;
    const state=states[$('state').value];
    $('state-title').textContent=state[0];$('state-body').textContent=state[1];
    $('recover').hidden=$('state').value==='base';
    $('flow').replaceChildren(...flows[s.id].map(id=>{
      const b=document.createElement('button');
      b.textContent=screens.find(x=>x.id===id).title;
      b.addEventListener('click',()=>{$('screen').value=id;$('state').value='base';render();$('screen-title').setAttribute('tabindex','-1');$('screen-title').focus();});
      return b;
    }));
  }
  for(const id of ['screen','theme','fidelity','format','state']) $(id).addEventListener('change',render);
  $('recover').addEventListener('click',()=>{$('state').value='base';render();$('state').focus();});
  render();
})();
