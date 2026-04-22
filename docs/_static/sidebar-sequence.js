/**
 * Prefix left-sidebar curriculum links with a user-facing sequence number.
 *
 * We number only document links in the left sidebar and intentionally skip
 * in-page hash links so section headings do not look like standalone
 * curriculum steps.
 *
 * To keep the navigation readable, numbering stops after one nested level.
 */
(function () {
  "use strict";

  var EXISTING_PREFIX_PATTERN = /^(?:part\s+\d+|\d+(?:\.\d+)*[.)-]?|\d+[:\-])\s+/i;

  function matchesSelector(element, selector) {
    var matcher = element.matches || element.webkitMatchesSelector || element.msMatchesSelector;
    return matcher ? matcher.call(element, selector) : false;
  }

  function getSidebarTree() {
    return document.querySelector(".sidebar-scroll .sidebar-tree");
  }

  function getDirectLink(listItem) {
    return listItem.querySelector(":scope > a.reference.internal, :scope > a.reference.external, :scope > a.reference");
  }

  function getDirectChildList(listItem) {
    return listItem.querySelector(":scope > ul");
  }

  function isDocumentLink(link) {
    if (!link || !link.getAttribute("href")) return false;
    return link.getAttribute("href").indexOf("#") === -1;
  }

  function needsSequencePrefix(text) {
    return !EXISTING_PREFIX_PATTERN.test(text);
  }

  function setLinkLabel(link, prefix) {
    if (!link.dataset.sequenceOriginalText) {
      link.dataset.sequenceOriginalText = link.textContent.trim();
    }

    if (!needsSequencePrefix(link.dataset.sequenceOriginalText)) {
      link.dataset.sequencePrefix = "";
      link.textContent = link.dataset.sequenceOriginalText;
      return;
    }

    if (link.dataset.sequencePrefix === prefix) {
      return;
    }

    link.dataset.sequencePrefix = prefix;
    link.textContent = prefix + " " + link.dataset.sequenceOriginalText;
  }

  function numberChildren(listElement, parentPrefix) {
    if (!listElement) return;

    var items = Array.prototype.slice.call(listElement.children);
    var childIndex = 0;

    items.forEach(function (item) {
      if (!matchesSelector(item, "li")) return;

      var link = getDirectLink(item);
      if (!isDocumentLink(link)) {
        return;
      }

      childIndex += 1;
      var prefix = parentPrefix.concat(childIndex).join(".");
      setLinkLabel(link, prefix + ".");
    });
  }

  function applySidebarSequence() {
    var sidebarTree = getSidebarTree();
    if (!sidebarTree) return;

    var rootLists = sidebarTree.querySelectorAll(":scope > ul");

    rootLists.forEach(function (listElement) {
      var topLevelIndex = 0;

      Array.prototype.forEach.call(listElement.children, function (item) {
        if (!matchesSelector(item, "li")) return;

        var link = getDirectLink(item);
        var childList = getDirectChildList(item);

        if (!isDocumentLink(link)) {
          return;
        }

        topLevelIndex += 1;
        setLinkLabel(link, String(topLevelIndex) + ".");
        numberChildren(childList, [topLevelIndex]);
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", applySidebarSequence);
  } else {
    applySidebarSequence();
  }
})();