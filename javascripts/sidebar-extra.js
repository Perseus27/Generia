/* Move page-defined #sidebar-extra into the right sidebar */
(function () {
  function mount() {
    const tpl = document.querySelector('#sidebar-extra');
    const target = document.querySelector('.md-sidebar--secondary .md-sidebar__scrollwrap');
    if (!tpl || !target) return;

    // clear previous injection (SPA navigation)
    target.querySelectorAll('.sidebar-extra').forEach(n => n.remove());

    // clone template content and ensure a wrapper class
    const frag = tpl.content ? tpl.content.cloneNode(true) : null;
    if (!frag) return;
    // if the author forgot a wrapper, create one
    let wrapper = frag.querySelector('.sidebar-extra');
    if (!wrapper) {
      wrapper = document.createElement('div');
      wrapper.className = 'sidebar-extra';
      wrapper.append(...frag.childNodes);
    }
    target.appendChild(wrapper);
  }
  // Material SPA hook
  window.document$.subscribe(mount);
})();
