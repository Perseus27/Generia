/* ChatGPT code, probably trash, but seems to work for now */

(function () {
  function mount() {
    const tpl = document.querySelector('#sidebar-extra');
    const target = document.querySelector('.md-sidebar--secondary .md-sidebar__scrollwrap');
    if (!tpl || !target) return;

    target.querySelectorAll('.sidebar-extra').forEach(n => n.remove());

    const frag = tpl.content ? tpl.content.cloneNode(true) : null;
    if (!frag) return;
    let wrapper = frag.querySelector('.sidebar-extra');
    if (!wrapper) {
      wrapper = document.createElement('div');
      wrapper.className = 'sidebar-extra';
      wrapper.append(...frag.childNodes);
    }
    target.appendChild(wrapper);
  }
  window.document$.subscribe(mount);
})();
