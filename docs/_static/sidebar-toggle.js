/**
 * Datadog-style draggable sidebar resize handles.
 *
 * Adds a thin drag handle on the right edge of the left sidebar and the
 * left edge of the right (TOC) sidebar.  Users can:
 *   • Drag the handle to resize the panel in real time.
 *   • Double-click the handle to collapse / restore the panel.
 *
 * Widths are persisted in localStorage so they survive page navigations.
 * Works only at desktop widths (≥ 63em); on mobile Furo's built-in
 * overlay sidebars take over.
 */
(function () {
  "use strict";

  /* --- Constants -------------------------------------------------- */
  var LEFT_W_KEY   = "ztai-left-sidebar-width";
  var RIGHT_W_KEY  = "ztai-right-sidebar-width";
  var LEFT_COL_KEY = "ztai-sidebar-left-collapsed";
  var RIGHT_COL_KEY = "ztai-sidebar-right-collapsed";
  var MIN_W        = 60;   // px – minimum before auto-collapse
  var DEFAULT_LEFT = 15;   // em – Furo default
  var DEFAULT_RIGHT = 15;  // em
  var SNAP_THRESHOLD = 80; // px – drag below this → collapse

  /* --- Helpers ---------------------------------------------------- */
  function emToPx(em) {
    return em * parseFloat(getComputedStyle(document.documentElement).fontSize);
  }

  function getLeftDrawer()  { return document.querySelector(".sidebar-drawer"); }
  function getRightDrawer() { return document.querySelector(".toc-drawer"); }

  /* --- Restore persisted widths (runs before DOM ready) ----------- */
  function applyStored() {
    var lw = localStorage.getItem(LEFT_W_KEY);
    var rw = localStorage.getItem(RIGHT_W_KEY);
    var lc = localStorage.getItem(LEFT_COL_KEY) === "1";
    var rc = localStorage.getItem(RIGHT_COL_KEY) === "1";

    if (lc) document.body.classList.add("sidebar-left-collapsed");
    if (rc) document.body.classList.add("sidebar-right-collapsed");

    // Inject a <style> so the widths apply before paint
    var css = "";
    if (lw && !lc) {
      css += ".sidebar-drawer{min-width:" + lw + "px!important;width:" + lw + "px!important}";
      css += ".sidebar-container{width:" + lw + "px!important}";
    }
    if (rw && !rc) {
      css += ".toc-drawer{width:" + rw + "px!important}";
    }
    if (css) {
      var s = document.createElement("style");
      s.id = "ztai-sidebar-sizes";
      s.textContent = css;
      document.head.appendChild(s);
    }
  }

  function removeStoredStyle() {
    var el = document.getElementById("ztai-sidebar-sizes");
    if (el) el.remove();
  }

  /* --- Apply width live ------------------------------------------- */
  function setLeftWidth(px) {
    var d = getLeftDrawer();
    if (!d) return;
    d.style.minWidth = px + "px";
    d.style.width = px + "px";
    var c = d.querySelector(".sidebar-container");
    if (c) c.style.width = px + "px";
  }

  function setRightWidth(px) {
    var d = getRightDrawer();
    if (!d) return;
    d.style.width = px + "px";
  }

  function clearLeftWidth() {
    var d = getLeftDrawer();
    if (!d) return;
    d.style.minWidth = "";
    d.style.width = "";
    var c = d.querySelector(".sidebar-container");
    if (c) c.style.width = "";
  }

  function clearRightWidth() {
    var d = getRightDrawer();
    if (!d) return;
    d.style.width = "";
  }

  /* --- Collapse / expand helpers ---------------------------------- */
  function collapseLeft() {
    document.body.classList.add("sidebar-left-collapsed");
    localStorage.setItem(LEFT_COL_KEY, "1");
  }
  function expandLeft(px) {
    document.body.classList.remove("sidebar-left-collapsed");
    localStorage.setItem(LEFT_COL_KEY, "0");
    if (px) { setLeftWidth(px); localStorage.setItem(LEFT_W_KEY, px); }
  }
  function collapseRight() {
    document.body.classList.add("sidebar-right-collapsed");
    localStorage.setItem(RIGHT_COL_KEY, "1");
  }
  function expandRight(px) {
    document.body.classList.remove("sidebar-right-collapsed");
    localStorage.setItem(RIGHT_COL_KEY, "0");
    if (px) { setRightWidth(px); localStorage.setItem(RIGHT_W_KEY, px); }
  }

  /* --- Create drag handle element --------------------------------- */
  function makeHandle(side) {
    var h = document.createElement("div");
    h.className = "sidebar-resize-handle sidebar-resize-handle--" + side;
    h.setAttribute("role", "separator");
    h.setAttribute("aria-orientation", "vertical");
    h.setAttribute("aria-label", "Resize " + side + " sidebar");
    h.setAttribute("tabindex", "0");
    return h;
  }

  /* --- Main init -------------------------------------------------- */
  function init() {
    var leftDrawer  = getLeftDrawer();
    var rightDrawer = getRightDrawer();

    /* Left handle */
    if (leftDrawer) {
      var lh = makeHandle("left");
      leftDrawer.appendChild(lh);

      var lastLeftW = parseInt(localStorage.getItem(LEFT_W_KEY), 10) || emToPx(DEFAULT_LEFT);

      lh.addEventListener("mousedown", function (e) {
        e.preventDefault();
        document.body.classList.add("sidebar-resizing");
        var startX = e.clientX;
        var startW = leftDrawer.getBoundingClientRect().width;
        var wasCollapsed = document.body.classList.contains("sidebar-left-collapsed");
        if (wasCollapsed) {
          expandLeft(0);
          startW = 0;
        }

        function onMove(ev) {
          var newW = Math.max(0, startW + (ev.clientX - startX));
          if (newW < SNAP_THRESHOLD) {
            document.body.classList.add("sidebar-left-collapsed");
            setLeftWidth(0);
          } else {
            document.body.classList.remove("sidebar-left-collapsed");
            setLeftWidth(newW);
          }
        }

        function onUp(ev) {
          document.removeEventListener("mousemove", onMove);
          document.removeEventListener("mouseup", onUp);
          document.body.classList.remove("sidebar-resizing");

          var finalW = leftDrawer.getBoundingClientRect().width;
          if (finalW < SNAP_THRESHOLD) {
            collapseLeft();
            lastLeftW = startW > MIN_W ? startW : emToPx(DEFAULT_LEFT);
          } else {
            localStorage.setItem(LEFT_COL_KEY, "0");
            localStorage.setItem(LEFT_W_KEY, Math.round(finalW));
            lastLeftW = Math.round(finalW);
          }
          removeStoredStyle();
        }

        document.addEventListener("mousemove", onMove);
        document.addEventListener("mouseup", onUp);
      });

      /* Double-click to toggle collapse */
      lh.addEventListener("dblclick", function () {
        if (document.body.classList.contains("sidebar-left-collapsed")) {
          expandLeft(lastLeftW || emToPx(DEFAULT_LEFT));
        } else {
          lastLeftW = leftDrawer.getBoundingClientRect().width;
          collapseLeft();
        }
        removeStoredStyle();
      });
    }

    /* Right handle */
    if (rightDrawer) {
      var rh = makeHandle("right");
      rightDrawer.insertBefore(rh, rightDrawer.firstChild);

      var lastRightW = parseInt(localStorage.getItem(RIGHT_W_KEY), 10) || emToPx(DEFAULT_RIGHT);

      rh.addEventListener("mousedown", function (e) {
        e.preventDefault();
        document.body.classList.add("sidebar-resizing");
        var startX = e.clientX;
        var startW = rightDrawer.getBoundingClientRect().width;
        var wasCollapsed = document.body.classList.contains("sidebar-right-collapsed");
        if (wasCollapsed) {
          expandRight(0);
          startW = 0;
        }

        function onMove(ev) {
          var newW = Math.max(0, startW - (ev.clientX - startX));
          if (newW < SNAP_THRESHOLD) {
            document.body.classList.add("sidebar-right-collapsed");
            setRightWidth(0);
          } else {
            document.body.classList.remove("sidebar-right-collapsed");
            setRightWidth(newW);
          }
        }

        function onUp(ev) {
          document.removeEventListener("mousemove", onMove);
          document.removeEventListener("mouseup", onUp);
          document.body.classList.remove("sidebar-resizing");

          var finalW = rightDrawer.getBoundingClientRect().width;
          if (finalW < SNAP_THRESHOLD) {
            collapseRight();
            lastRightW = startW > MIN_W ? startW : emToPx(DEFAULT_RIGHT);
          } else {
            localStorage.setItem(RIGHT_COL_KEY, "0");
            localStorage.setItem(RIGHT_W_KEY, Math.round(finalW));
            lastRightW = Math.round(finalW);
          }
          removeStoredStyle();
        }

        document.addEventListener("mousemove", onMove);
        document.addEventListener("mouseup", onUp);
      });

      rh.addEventListener("dblclick", function () {
        if (document.body.classList.contains("sidebar-right-collapsed")) {
          expandRight(lastRightW || emToPx(DEFAULT_RIGHT));
        } else {
          lastRightW = rightDrawer.getBoundingClientRect().width;
          collapseRight();
        }
        removeStoredStyle();
      });
    }
  }

  /* --- Boot --- */
  applyStored();
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
