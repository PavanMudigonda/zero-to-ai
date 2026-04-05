/**
 * Preserve the left sidebar scroll position across page navigations.
 *
 * Strategy: if a saved position exists, we immediately inject CSS that
 * hides the sidebar (visibility:hidden keeps layout stable). Then on
 * DOMContentLoaded we set scrollTop, intercept Furo's scrollIntoView,
 * and reveal — all before the user sees anything.
 */
(function () {
  "use strict";

  var STORAGE_KEY = "ztai-sidebar-scroll";
  var hasSaved = sessionStorage.getItem(STORAGE_KEY) !== null;

  /* ---- Phase 1: run immediately at parse time ---- */
  // If we have a saved position, hide sidebar content to prevent flash
  if (hasSaved) {
    var hideStyle = document.createElement("style");
    hideStyle.id = "ztai-sidebar-hide";
    hideStyle.textContent = ".sidebar-scroll{visibility:hidden!important}";
    document.head.appendChild(hideStyle);
  }

  /* ---- Phase 2: intercept scrollIntoView at parse time ---- */
  var nativeScrollIntoView = Element.prototype.scrollIntoView;

  if (hasSaved) {
    Element.prototype.scrollIntoView = function () {
      // Skip calls targeting sidebar children
      var sidebar = document.querySelector(".sidebar-scroll");
      if (sidebar && sidebar.contains(this)) return;
      return nativeScrollIntoView.apply(this, arguments);
    };
  }

  /* ---- Phase 3: restore position on DOMContentLoaded ---- */
  function restore() {
    var sidebar = document.querySelector(".sidebar-scroll");
    if (!sidebar) { cleanup(); return; }

    var raw = sessionStorage.getItem(STORAGE_KEY);
    sessionStorage.removeItem(STORAGE_KEY);

    if (raw !== null) {
      var target = parseInt(raw, 10);
      if (!isNaN(target)) {
        sidebar.scrollTop = target;
      }
    }

    // Reveal: remove the hide style and restore native scrollIntoView
    cleanup();
  }

  function cleanup() {
    var s = document.getElementById("ztai-sidebar-hide");
    if (s) s.remove();
    Element.prototype.scrollIntoView = nativeScrollIntoView;
  }

  /* ---- Save on click ---- */
  function listen() {
    var sidebar = document.querySelector(".sidebar-scroll");
    if (!sidebar) return;
    sidebar.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        sessionStorage.setItem(STORAGE_KEY, sidebar.scrollTop);
      }
    });
  }

  /* ---- Boot ---- */
  function boot() { restore(); listen(); }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
