/**
 * Preserve the sidebar scroll position across sidebar-driven navigations.
 */
(function () {
  "use strict";

  var STORAGE_KEY = "ztai-sidebar-scroll";
  var NAV_KEY = "ztai-sidebar-nav";

  function getSidebar() {
    return document.querySelector(".sidebar-scroll");
  }

  function save() {
    var sidebar = getSidebar();
    if (!sidebar) return;
    sessionStorage.setItem(STORAGE_KEY, String(sidebar.scrollTop));
  }

  function restore() {
    var sidebar = getSidebar();
    if (!sidebar) return;
    
    var raw = sessionStorage.getItem(STORAGE_KEY);
    var fromSidebarNav = sessionStorage.getItem(NAV_KEY) === "1";

    if (raw === null || !fromSidebarNav) {
      return; 
    }

    var target = parseInt(raw, 10);
    if (isNaN(target)) return;

    var previousBehavior = sidebar.style.scrollBehavior;
    sidebar.style.scrollBehavior = "auto";

    function apply() {
      sidebar.scrollTop = target;
    }

    apply();
    requestAnimationFrame(function () {
      apply();
      requestAnimationFrame(function () {
        apply();
        sidebar.style.scrollBehavior = previousBehavior;
        // Clean up only after we applied the final frame
        sessionStorage.removeItem(NAV_KEY);
      });
    });
  }

  function init() {
    var sidebar = getSidebar();
    if (!sidebar) return;

    restore();

    sidebar.addEventListener("click", function (e) {
      var link = e.target.closest("a");
      if (!link || !link.href) return;
      sessionStorage.setItem(NAV_KEY, "1");
      save();
    }, true);

    sidebar.addEventListener("scroll", function () {
      save();
    }, { passive: true });

    window.addEventListener("beforeunload", save);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
