/* Scroll progress bar - shows reading progress at the top of the page */
(function () {
  "use strict";

  var bar = document.createElement("div");
  bar.id = "scroll-progress";
  document.body.prepend(bar);

  function updateProgress() {
    var scrollTop = window.scrollY || document.documentElement.scrollTop;
    var docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    bar.style.width = progress + "%";
  }

  window.addEventListener("scroll", updateProgress, { passive: true });
  window.addEventListener("resize", updateProgress, { passive: true });
  updateProgress();
})();
