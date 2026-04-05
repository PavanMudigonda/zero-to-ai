/**
 * Preserve the left sidebar scroll position across page navigations.
 *
 * Furo's sidebar lives inside `.sidebar-scroll` (the scrollable container).
 * On every click we stash its scrollTop into sessionStorage, and on the next
 * page load we restore it — so the toctree stays where the reader left it.
 *
 * As a fallback (first visit / cleared storage) we scroll the active item
 * into view so the reader always sees where they are in the tree.
 */
(function () {
  "use strict";

  var STORAGE_KEY = "ztai-sidebar-scroll";

  function getSidebarContainer() {
    // Furo uses .sidebar-scroll as the scrollable wrapper
    return document.querySelector(".sidebar-scroll");
  }

  function restoreOrReveal() {
    var container = getSidebarContainer();
    if (!container) return;

    var saved = sessionStorage.getItem(STORAGE_KEY);
    if (saved !== null) {
      container.scrollTop = parseInt(saved, 10);
      sessionStorage.removeItem(STORAGE_KEY);
    } else {
      // No saved position — scroll the current page's link into view
      var active = container.querySelector(".current");
      if (active) {
        active.scrollIntoView({ block: "center" });
      }
    }
  }

  function saveOnNavigate() {
    var container = getSidebarContainer();
    if (!container) return;

    // Capture scroll position on every link click inside the sidebar
    container.addEventListener("click", function (e) {
      var link = e.target.closest("a");
      if (link) {
        sessionStorage.setItem(STORAGE_KEY, container.scrollTop);
      }
    });
  }

  // Run after the DOM is ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      restoreOrReveal();
      saveOnNavigate();
    });
  } else {
    restoreOrReveal();
    saveOnNavigate();
  }
})();
