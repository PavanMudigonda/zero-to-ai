document.addEventListener("DOMContentLoaded", function () {
  var storageKey = "zero-to-ai:selected-track";
  var checklistProgressStorageKey = "zero-to-ai:checklist-progress";
  var lastChecklistItemStorageKey = "zero-to-ai:last-checklist-item";
  var recentChecklistItemsStorageKey = "zero-to-ai:recent-checklist-items";
  var checklistTotalStorageKey = "zero-to-ai:checklist-total";
  var trackMeta = {
    "ai-engineer": {
      name: "AI Engineer",
      guideHash: "#track-ai-engineer",
      homeCopy:
        "Resume with setup, then move through Embeddings, RAG, Prompt Engineering, and Agents before hardening projects with MLOps.",
      checklistCopy:
        "Prioritize the application-building path: embeddings, retrieval, prompting, agents, and deployment. Keep math depth selective unless a concept blocks you.",
      corePhases: [
        "Phase 1: Python & Machine Learning (278 notebooks)",
        "Phase 3: Tokenization (8 notebooks)",
        "Phase 4: Embeddings (10 notebooks)",
        "Phase 5: Neural Networks",
        "Phase 6: Vector Databases (7 notebooks)",
        "Phase 7: RAG Systems",
        "Phase 8: MLOps",
        "Phase 10: Prompt Engineering (6 notebooks) 🔥",
        "Phase 11: LLM Fine-tuning (12 notebooks) 🔥",
        "Phase 13: Local LLMs (6 notebooks) 🔥",
        "Phase 14: AI Agents (9 notebooks) 🔥 HOT TOPIC",
        "Phase 15: Real-Time Streaming AI (4 notebooks) 🔥"
      ],
      optionalPhases: [
        {
          title: "Model Evaluation",
          headingKey: "Model Evaluation - 16-model-evaluation/"
        },
        {
          title: "AI Safety & Red Teaming",
          headingKey: "AI Safety & Red Teaming - 19-ai-safety-redteaming/"
        }
      ]
    },
    "ml-engineer": {
      name: "ML Engineer",
      guideHash: "#track-ml-engineer",
      homeCopy:
        "Resume with setup, then build sequential depth through Python, Data Science, Math, Neural Networks, and production systems.",
      checklistCopy:
        "Prioritize foundations and systems depth first: math, neural networks, evaluation, debugging, and production tooling before optional specialization breadth.",
      corePhases: [
        "Phase 1: Python & Machine Learning (278 notebooks)",
        "Phase 2: Mathematics for ML",
        "Phase 5: Neural Networks",
        "Phase 8: MLOps",
        {
          title: "Model Evaluation",
          headingKey: "Model Evaluation - 16-model-evaluation/"
        },
        {
          title: "Debugging & Troubleshooting",
          headingKey: "Debugging & Troubleshooting - 17-debugging-troubleshooting/"
        },
        "Phase 11: LLM Fine-tuning (12 notebooks) 🔥",
        "Phase 24: Advanced Deep Learning (RESEARCH LEVEL) 🔬",
        "Phase 25: Reinforcement Learning (7 notebooks)",
        "Phase 26: Time Series Analysis & Forecasting (7 notebooks)"
      ],
      optionalPhases: [
        "Phase 27: Causal Inference & Experimental Design (7 notebooks)"
      ]
    },
    "data-scientist": {
      name: "Data Scientist",
      guideHash: "#track-data-scientist",
      homeCopy:
        "Resume with setup, then focus on Data Science, Math, Evaluation, Time Series, and Causal Inference.",
      checklistCopy:
        "Prioritize analytical depth and experimental rigor: data science, statistics, evaluation, time series, and causal reasoning before heavier systems work.",
      corePhases: [
        "Phase 1: Python & Machine Learning (278 notebooks)",
        "Phase 2: Mathematics for ML",
        {
          title: "Low-Code AI Tools",
          headingKey: "Low-Code AI Tools - 18-low-code-ai-tools/"
        },
        "Phase 5: Neural Networks",
        {
          title: "Model Evaluation",
          headingKey: "Model Evaluation - 16-model-evaluation/"
        },
        "Phase 7: RAG Systems",
        "Phase 10: Prompt Engineering (6 notebooks) 🔥",
        "Phase 26: Time Series Analysis & Forecasting (7 notebooks)",
        "Phase 27: Causal Inference & Experimental Design (7 notebooks)"
      ],
      optionalPhases: [
        "Phase 4: Embeddings (10 notebooks)",
        "Phase 6: Vector Databases (7 notebooks)",
        "Phase 11: LLM Fine-tuning (12 notebooks) 🔥"
      ]
    }
  };

  function textKey(value) {
    return value.replace(/\s+/g, " ").trim();
  }

  function normalizePhaseEntry(entry) {
    if (typeof entry === "string") {
      return {
        title: entry,
        headingKey: entry
      };
    }

    return entry;
  }

  function readStoredTrack() {
    try {
      return window.localStorage.getItem(storageKey);
    } catch (error) {
      return null;
    }
  }

  function writeStoredTrack(track) {
    try {
      window.localStorage.setItem(storageKey, track);
    } catch (error) {
      return;
    }
  }

  function clearStoredTrack() {
    try {
      window.localStorage.removeItem(storageKey);
    } catch (error) {
      return;
    }
  }

  function readChecklistProgress() {
    try {
      var raw = window.localStorage.getItem(checklistProgressStorageKey);
      return raw ? JSON.parse(raw) : {};
    } catch (error) {
      return {};
    }
  }

  function writeChecklistProgress(progress) {
    try {
      window.localStorage.setItem(checklistProgressStorageKey, JSON.stringify(progress));
    } catch (error) {
      return;
    }
  }

  function clearChecklistProgress() {
    try {
      window.localStorage.removeItem(checklistProgressStorageKey);
    } catch (error) {
      return;
    }
  }

  function readLastChecklistItem() {
    try {
      var raw = window.localStorage.getItem(lastChecklistItemStorageKey);
      return raw ? JSON.parse(raw) : null;
    } catch (error) {
      return null;
    }
  }

  function writeLastChecklistItem(item) {
    try {
      window.localStorage.setItem(lastChecklistItemStorageKey, JSON.stringify(item));
    } catch (error) {
      return;
    }
  }

  function clearLastChecklistItem() {
    try {
      window.localStorage.removeItem(lastChecklistItemStorageKey);
    } catch (error) {
      return;
    }
  }

  function readRecentChecklistItems() {
    try {
      var raw = window.localStorage.getItem(recentChecklistItemsStorageKey);
      if (raw) {
        var parsed = JSON.parse(raw);
        return Array.isArray(parsed) ? parsed : [];
      }

      var legacyItem = readLastChecklistItem();
      return legacyItem ? [legacyItem] : [];
    } catch (error) {
      return [];
    }
  }

  function writeRecentChecklistItems(items) {
    try {
      window.localStorage.setItem(
        recentChecklistItemsStorageKey,
        JSON.stringify(items.slice(0, 3))
      );
    } catch (error) {
      return;
    }
  }

  function clearRecentChecklistItems() {
    try {
      window.localStorage.removeItem(recentChecklistItemsStorageKey);
    } catch (error) {
      return;
    }
  }

  function readChecklistTotal() {
    try {
      var raw = window.localStorage.getItem(checklistTotalStorageKey);
      return raw ? Number(raw) : 0;
    } catch (error) {
      return 0;
    }
  }

  function writeChecklistTotal(total) {
    try {
      window.localStorage.setItem(checklistTotalStorageKey, String(total));
    } catch (error) {
      return;
    }
  }

  function clearChecklistTotal() {
    try {
      window.localStorage.removeItem(checklistTotalStorageKey);
    } catch (error) {
      return;
    }
  }

  function clearAllLearningData() {
    clearStoredTrack();
    clearChecklistProgress();
    clearLastChecklistItem();
    clearRecentChecklistItems();
    clearChecklistTotal();
  }

  function createProgressSnapshot() {
    return {
      version: 1,
      exportedAt: new Date().toISOString(),
      selectedTrack: readStoredTrack(),
      checklistProgress: readChecklistProgress(),
      recentChecklistItems: readRecentChecklistItems(),
      lastChecklistItem: readLastChecklistItem(),
      checklistTotal: readChecklistTotal()
    };
  }

  function downloadProgressSnapshot() {
    var snapshot = createProgressSnapshot();
    var blob = new Blob([JSON.stringify(snapshot, null, 2)], {
      type: "application/json"
    });
    var url = window.URL.createObjectURL(blob);
    var link = document.createElement("a");
    var dateStamp = snapshot.exportedAt.slice(0, 10);

    link.href = url;
    link.download = "zero-to-ai-progress-" + dateStamp + ".json";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(url);
  }

  function applyImportedProgress(snapshot) {
    if (!snapshot || typeof snapshot !== "object") {
      throw new Error("Invalid progress file.");
    }

    if (snapshot.selectedTrack && trackMeta[snapshot.selectedTrack]) {
      writeStoredTrack(snapshot.selectedTrack);
    } else if (!snapshot.selectedTrack) {
      clearStoredTrack();
    }

    if (snapshot.checklistProgress && typeof snapshot.checklistProgress === "object") {
      writeChecklistProgress(snapshot.checklistProgress);
    } else {
      clearChecklistProgress();
    }

    if (snapshot.lastChecklistItem && typeof snapshot.lastChecklistItem === "object") {
      writeLastChecklistItem(snapshot.lastChecklistItem);
    } else {
      clearLastChecklistItem();
    }

    if (Array.isArray(snapshot.recentChecklistItems)) {
      writeRecentChecklistItems(snapshot.recentChecklistItems);
    } else if (snapshot.lastChecklistItem && typeof snapshot.lastChecklistItem === "object") {
      writeRecentChecklistItems([snapshot.lastChecklistItem]);
    } else {
      clearRecentChecklistItems();
    }

    if (typeof snapshot.checklistTotal === "number" && snapshot.checklistTotal >= 0) {
      writeChecklistTotal(snapshot.checklistTotal);
    }
  }

  function updateStudyGuideLinks(track) {
    var links = Array.prototype.slice.call(
      document.querySelectorAll("[data-study-guide-link]")
    );
    var meta = trackMeta[track];

    links.forEach(function (link) {
      var baseHref = link.getAttribute("data-base-href");
      if (!baseHref) {
        baseHref = (link.getAttribute("href") || "MASTER_STUDY_GUIDE.html").split("#")[0];
        link.setAttribute("data-base-href", baseHref);
      }
      link.setAttribute(
        "href",
        meta ? baseHref + meta.guideHash : baseHref
      );
    });
  }

  function updateResumeLearningWidget(track) {
    var widget = document.querySelector("[data-resume-learning]");
    if (!widget) {
      return;
    }

    var copy = widget.querySelector("[data-resume-learning-copy]");
    var checklistLink = widget.querySelector("[data-resume-checklist-link]");
    var studyGuideLink = widget.querySelector("[data-study-guide-link]");
    var baseChecklistUrl = widget.getAttribute("data-checklist-url") || "checklist.html";
    var meta = trackMeta[track];
    var lastItem = readLastChecklistItem();
    var recentItems = readRecentChecklistItems();
    var completedCount = Object.keys(readChecklistProgress()).length;
    var totalCount = readChecklistTotal();
    var progressRoot = widget.querySelector("[data-resume-progress]");
    var progressFill = widget.querySelector("[data-resume-progress-fill]");
    var progressLabel = widget.querySelector("[data-resume-progress-label]");
    var recentRoot = widget.querySelector("[data-resume-recent]");
    var recentList = widget.querySelector("[data-resume-recent-list]");
    var parts = [];

    if (meta) {
      parts.push("Saved track: " + meta.name + ".");
    }

    if (lastItem && lastItem.text) {
      parts.push("Last completed item: " + lastItem.text + ".");
      if (checklistLink) {
        checklistLink.setAttribute(
          "href",
          baseChecklistUrl + (lastItem.anchor ? "#" + lastItem.anchor : "")
        );
      }
    } else if (checklistLink) {
      checklistLink.setAttribute("href", baseChecklistUrl);
    }

    if (studyGuideLink) {
      var studyGuideBaseHref = studyGuideLink.getAttribute("data-base-href");
      if (!studyGuideBaseHref) {
        studyGuideBaseHref = (studyGuideLink.getAttribute("href") || widget.getAttribute("data-study-guide-url") || "MASTER_STUDY_GUIDE.html").split("#")[0];
        studyGuideLink.setAttribute("data-base-href", studyGuideBaseHref);
      }
      studyGuideLink.setAttribute(
        "href",
        meta ? studyGuideBaseHref + meta.guideHash : studyGuideBaseHref
      );
    }

    if (!parts.length) {
      widget.hidden = true;
      if (copy) {
        copy.textContent = "";
      }
      if (progressRoot) {
        progressRoot.hidden = true;
      }
      if (recentRoot) {
        recentRoot.hidden = true;
      }
      return;
    }

    widget.hidden = false;
    if (copy) {
      copy.textContent = parts.join(" ");
    }

    if (progressRoot && progressFill && progressLabel && totalCount > 0) {
      var percentage = Math.max(0, Math.min(100, Math.round((completedCount / totalCount) * 100)));
      progressRoot.hidden = false;
      progressFill.style.width = percentage + "%";
      progressLabel.textContent = completedCount + " / " + totalCount + " complete";
    } else if (progressRoot) {
      progressRoot.hidden = true;
    }

    if (recentRoot && recentList && recentItems.length) {
      recentRoot.hidden = false;
      recentList.innerHTML = "";
      recentItems.slice(0, 3).forEach(function (item) {
        var listItem = document.createElement("li");
        var link = document.createElement("a");
        link.href = baseChecklistUrl + (item.anchor ? "#" + item.anchor : "");
        link.textContent = item.text;
        listItem.appendChild(link);
        recentList.appendChild(listItem);
      });
    } else if (recentRoot) {
      recentRoot.hidden = true;
    }
  }

  function updateChecklistProgressSummary(completedCount, totalCount) {
    var summary = document.querySelector("[data-checklist-progress-summary]");
    if (!summary) {
      return;
    }

    if (!totalCount) {
      summary.textContent = "Progress is stored only on this device.";
      return;
    }

    var percentage = Math.round((completedCount / totalCount) * 100);
    summary.textContent =
      completedCount +
      " of " +
      totalCount +
      " checklist items completed on this device (" +
      percentage +
      "%).";
  }

  function createChecklistItemKey(checkbox, index) {
    var container = checkbox.closest("li") || checkbox.parentElement;
    var labelText = textKey(container ? container.textContent || "" : "");
    return "checklist:" + index + ":" + labelText.slice(0, 160);
  }

  function setupChecklistProgress() {
    var resetButton = document.querySelector("[data-reset-checklist-progress]");
    var exportButton = document.querySelector("[data-export-checklist-progress]");
    var importButton = document.querySelector("[data-import-checklist-progress]");
    var clearAllButton = document.querySelector("[data-clear-learning-data]");
    var importFileInput = document.querySelector("[data-import-checklist-file]");
    var checkboxes = Array.prototype.slice.call(
      document.querySelectorAll("main li.task-list-item input[type='checkbox']")
    );

    if (!checkboxes.length) {
      updateChecklistProgressSummary(0, 0);
      return;
    }

    var progress = readChecklistProgress();
    writeChecklistTotal(checkboxes.length);

    function refreshSummary() {
      var completedCount = checkboxes.filter(function (checkbox) {
        return checkbox.checked;
      }).length;
      updateChecklistProgressSummary(completedCount, checkboxes.length);
    }

    function syncCheckboxesFromStorage() {
      var currentProgress = readChecklistProgress();

      checkboxes.forEach(function (checkbox, index) {
        var itemKey = createChecklistItemKey(checkbox, index);
        var listItem = checkbox.closest("li");
        checkbox.checked = Boolean(currentProgress[itemKey]);
        if (listItem) {
          listItem.classList.toggle("checklist-item-completed", checkbox.checked);
        }
      });

      refreshSummary();
      renderChecklistRecommendations(readStoredTrack());
      updateStudyGuideLinks(readStoredTrack());
      updateResumeLearningWidget(readStoredTrack());
    }

    checkboxes.forEach(function (checkbox, index) {
      var itemKey = createChecklistItemKey(checkbox, index);
      var listItem = checkbox.closest("li");
      var anchorId = listItem && listItem.id ? listItem.id : "checklist-item-" + (index + 1);

      if (listItem && !listItem.id) {
        listItem.id = anchorId;
      }

      checkbox.disabled = false;
      checkbox.checked = Boolean(progress[itemKey]);
      if (listItem) {
        listItem.classList.toggle("checklist-item-completed", checkbox.checked);
      }

      checkbox.addEventListener("change", function () {
        var nextProgress = readChecklistProgress();
        nextProgress[itemKey] = checkbox.checked;
        if (!checkbox.checked) {
          delete nextProgress[itemKey];
        }
        writeChecklistProgress(nextProgress);

        if (checkbox.checked && listItem) {
          var recentItems = readRecentChecklistItems().filter(function (item) {
            return item.anchor !== anchorId;
          });
          recentItems.unshift({
            text: textKey(listItem.textContent || ""),
            anchor: anchorId
          });
          writeRecentChecklistItems(recentItems);
          writeLastChecklistItem({
            text: textKey(listItem.textContent || ""),
            anchor: anchorId
          });
        } else {
          var lastItem = readLastChecklistItem();
          if (lastItem && lastItem.anchor === anchorId) {
            clearLastChecklistItem();
          }
          writeRecentChecklistItems(
            readRecentChecklistItems().filter(function (item) {
              return item.anchor !== anchorId;
            })
          );
        }

        if (listItem) {
          listItem.classList.toggle("checklist-item-completed", checkbox.checked);
        }
        refreshSummary();
        updateResumeLearningWidget(readStoredTrack());
      });
    });

    if (resetButton) {
      resetButton.addEventListener("click", function () {
        clearChecklistProgress();
        clearLastChecklistItem();
        clearRecentChecklistItems();
        checkboxes.forEach(function (checkbox) {
          checkbox.checked = false;
          var listItem = checkbox.closest("li");
          if (listItem) {
            listItem.classList.remove("checklist-item-completed");
          }
        });
        refreshSummary();
        updateResumeLearningWidget(readStoredTrack());
      });
    }

    if (clearAllButton) {
      clearAllButton.addEventListener("click", function () {
        clearAllLearningData();
        checkboxes.forEach(function (checkbox) {
          checkbox.checked = false;
          var listItem = checkbox.closest("li");
          if (listItem) {
            listItem.classList.remove("checklist-item-completed");
          }
        });
        refreshSummary();
        renderChecklistRecommendations(null);
        updateStudyGuideLinks(null);
        updateResumeLearningWidget(null);
      });
    }

    if (exportButton) {
      exportButton.addEventListener("click", function () {
        downloadProgressSnapshot();
      });
    }

    if (importButton && importFileInput) {
      importButton.addEventListener("click", function () {
        importFileInput.click();
      });

      importFileInput.addEventListener("change", function () {
        var file = importFileInput.files && importFileInput.files[0];
        if (!file) {
          return;
        }

        var reader = new FileReader();
        reader.onload = function () {
          try {
            var snapshot = JSON.parse(String(reader.result || "{}"));
            applyImportedProgress(snapshot);
            syncCheckboxesFromStorage();
          } catch (error) {
            window.alert("Could not import progress from that file.");
          } finally {
            importFileInput.value = "";
          }
        };
        reader.onerror = function () {
          window.alert("Could not read the selected progress file.");
          importFileInput.value = "";
        };
        reader.readAsText(file);
      });
    }

    refreshSummary();
    updateResumeLearningWidget(readStoredTrack());
  }

  function findChecklistHeadings() {
    return Array.prototype.slice
      .call(document.querySelectorAll("main h2, main h3"))
      .reduce(function (map, heading) {
        var key = textKey(heading.textContent || "");
        if (key) {
          map[key] = heading;
        }
        return map;
      }, {});
  }

  function ensureLabel(heading, labelText, modifierClass) {
    if (!heading) {
      return;
    }

    var existing = heading.querySelector(".track-highlight-label");
    if (existing) {
      existing.remove();
    }

    var label = document.createElement("span");
    label.className = "track-highlight-label" + (modifierClass ? " " + modifierClass : "");
    label.textContent = labelText;
    heading.appendChild(document.createTextNode(" "));
    heading.appendChild(label);
  }

  function clearChecklistHighlights(headingsMap) {
    Object.keys(headingsMap).forEach(function (key) {
      var heading = headingsMap[key];
      heading.classList.remove("track-highlight-core", "track-highlight-optional");
      var label = heading.querySelector(".track-highlight-label");
      if (label) {
        label.remove();
      }
    });
  }

  function createChecklistListItem(text, heading) {
    var item = document.createElement("li");
    if (heading && heading.id) {
      var link = document.createElement("a");
      link.href = "#" + heading.id;
      link.textContent = text;
      item.appendChild(link);
    } else {
      item.textContent = text;
    }
    return item;
  }

  function renderChecklistRecommendations(track) {
    var focusRoot = document.querySelector("[data-checklist-track-focus]");
    if (!focusRoot) {
      return;
    }

    var title = focusRoot.querySelector(".checklist-track-focus__title");
    var copy = focusRoot.querySelector("[data-checklist-track-copy]");
    var coreList = focusRoot.querySelector("[data-track-core-list]");
    var optionalList = focusRoot.querySelector("[data-track-optional-list]");
    var headingsMap = findChecklistHeadings();
    var meta = trackMeta[track];

    if (!title || !copy || !coreList || !optionalList) {
      return;
    }

    clearChecklistHighlights(headingsMap);
    coreList.innerHTML = "";
    optionalList.innerHTML = "";

    if (!meta) {
      updateStudyGuideLinks(null);
      title.textContent = "No saved learning path found yet.";
      copy.textContent = "Pick a path on the homepage and this checklist will prioritize the phases that matter most for that track.";
      coreList.appendChild(
        createChecklistListItem("Saved path recommendations will appear here.")
      );
      optionalList.appendChild(
        createChecklistListItem("Stretch topics will appear here after you choose a path.")
      );
      return;
    }

    updateStudyGuideLinks(track);
    title.textContent = meta.name + " priorities";
    copy.textContent = meta.checklistCopy;

    meta.corePhases.forEach(function (phaseEntry) {
      var normalized = normalizePhaseEntry(phaseEntry);
      var key = textKey(normalized.headingKey);
      var heading = headingsMap[key];
      if (heading) {
        heading.classList.add("track-highlight-core");
        ensureLabel(heading, "Core for this track");
      }
      coreList.appendChild(createChecklistListItem(normalized.title, heading));
    });

    meta.optionalPhases.forEach(function (phaseEntry) {
      var normalized = normalizePhaseEntry(phaseEntry);
      var key = textKey(normalized.headingKey);
      var heading = headingsMap[key];
      if (heading) {
        heading.classList.add("track-highlight-optional");
        ensureLabel(heading, "Optional depth", "track-highlight-label--optional");
      }
      optionalList.appendChild(createChecklistListItem(normalized.title, heading));
    });
  }

  function setupHomepagePlanner() {
    var banner = document.querySelector("[data-saved-track]");
    var trackCards = Array.prototype.slice.call(
      document.querySelectorAll("[data-track-card]")
    );
    var selectButtons = Array.prototype.slice.call(
      document.querySelectorAll("[data-select-track]")
    );
    var clearButton = document.querySelector("[data-clear-track]");
    var bannerCopy = document.querySelector("[data-saved-track-copy]");

    if (!banner || !trackCards.length || !selectButtons.length || !bannerCopy) {
      return;
    }

    function applySelectedTrack(track) {
      var meta = trackMeta[track];
      var hasSelection = Boolean(meta);

      banner.hidden = !hasSelection;
      if (hasSelection) {
        bannerCopy.textContent = meta.homeCopy;
        banner.querySelector(".saved-path-banner__title").textContent =
          meta.name + " is your saved learning path.";
      }

      updateStudyGuideLinks(track);
      updateResumeLearningWidget(track);

      trackCards.forEach(function (card) {
        var isActive = card.getAttribute("data-track-card") === track;
        card.classList.toggle("is-active", isActive);
      });

      selectButtons.forEach(function (button) {
        var isSelected = button.getAttribute("data-select-track") === track;
        button.classList.toggle("is-selected", isSelected);
        button.setAttribute("aria-pressed", String(isSelected));
        button.textContent = isSelected ? "Saved on this device" : "Save this path";
      });

      renderChecklistRecommendations(track);
    }

    selectButtons.forEach(function (button) {
      button.addEventListener("click", function () {
        var track = button.getAttribute("data-select-track");
        if (!trackMeta[track]) {
          return;
        }
        writeStoredTrack(track);
        setTimeout(function() {
          applySelectedTrack(track);
        }, 0);
      });
    });

    if (clearButton) {
      clearButton.addEventListener("click", function () {
        clearStoredTrack();
        setTimeout(function() {
          applySelectedTrack(null);
        }, 0);
      });
    }

    applySelectedTrack(readStoredTrack());
  }

  setupHomepagePlanner();
  updateStudyGuideLinks(readStoredTrack());
  renderChecklistRecommendations(readStoredTrack());
  setupChecklistProgress();
  updateResumeLearningWidget(readStoredTrack());
});