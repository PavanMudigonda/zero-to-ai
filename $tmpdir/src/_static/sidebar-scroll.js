/**
 * Preserve only the left sidebar scroll position across sidebar-driven
 * navigations without touching the main page scroll behavior.
 */
(function () {
  "use strict";

  var STORAGE_KEY = "ztai-sidebar-scroll";
  var NAV_KEY = "ztai-sidebar-nav";

  function getSidebar() {
    return document.querySelector(".sidebar-scroll");
  }

  function save(sidebar) {
    if (!sidebar) return;
    sessionStorage.setItem(STORAGE_KEY, String(sidebar.scrollTop));
  }

  function restore() {
    var sidebar = getSidebar();
    var raw = sessionStorage.getItem(STORAGE_KEY);
    var fromSidebarNav = sessionStorage.getItem(NAV_KEY) === "1";

    if (!sidebar || raw === null || !fromSidebarNav) {
      sessionStorage.removeItem(NAV_KEY);
      return;
    }

    sessionStorage.removeItem(NAV_KEY);

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
      });
    });
  }

  function listen() {
    var sidebar = getSidebar();
    if (!sidebar) return;

    sidebar.addEventListener("click", function (e) {
      var link = e.target.closest("a");
      if (!link) return;
      sessionStorage.setItem(NAV_KEY, "1");
      save(sidebar);
    }, true);

    window.addEventListener("pagehide", function () {
      save(sidebar);
    });
  }

  function boot() {
    restore();
    listen();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }

  window.addEventListener("pageshow", restore);
  window.addEventListener("load", restore);
})();
