// Collapsible TOC functionality
document.addEventListener('DOMContentLoaded', function() {
  const toc = document.querySelector('.toc');
  const navTitle = document.querySelector('.toc .nav__title');

  if (navTitle && toc) {
    // Start collapsed on review page (many items)
    const tocMenu = toc.querySelector('.toc__menu');
    if (tocMenu && tocMenu.querySelectorAll('li').length > 10) {
      toc.classList.add('collapsed');
    }

    // Toggle on click
    navTitle.addEventListener('click', function() {
      toc.classList.toggle('collapsed');
    });
  }
});
