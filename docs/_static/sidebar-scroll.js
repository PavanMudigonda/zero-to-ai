/**
 * Preserve the left sidebar scroll position across page navigations.
 *
 * Furo's own JS calls scrollIntoView on the current toctree item after
 * DOMContentLoaded, which resets any scrollTop we set earlier.  We fight
 * back by:
 *   1. Saving scrollTop on every sidebar link click (before navigation).
 *   2. Restoring it *after* Furo has finished (requestAnimationFrame loop
 *      that re-applies the position until the browser has settled).
 *   3. Then locking the position for a short window by temporarily
 *      suppressing the scroll via CSS overflow:hidden.
 */
(function () {
  "use strict";

  var STORAGE_KEY = "ztai-sidebar-scroll";
  var LOCK_MS = 400;            // ms to hold scroll position after restore

  function getSidebar() {
    return document.querySelector(".sidebar-scroll");
  }

  /* ---- Restore ---- */
  function restore() {
    var sidebar = getSidebar();
    if (!sidebar) return;

    var raw = sessionStorage.getItem(STORAGE_KEY);
    if (raw === null) return;          // first visit — let Furo do its thing
    sessionStorage.removeItem(STORAGE_KEY);

    var target = parseInt(raw, 10);
    if (isNaN(target)) return;

    // Apply position repeatedly to beat Furo's own scrollIntoView
    var attempts = 0;
    function apply() {
      sidebar.scrollTop = target;
      if (++attempts < 6) {
        requestAnimationFrame(apply);
      } else {
        // After settling, briefly lock so no late scripts can override
        sidebar.style.overflow = "hidden";
        setTimeout(function () { sidebar.style.overflow = ""; }, LOCK_MS);
      }
    }
    apply();
  }

  /* ---- Save on click ---- */
  function listen() {
    var sidebar = getSidebar();
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
