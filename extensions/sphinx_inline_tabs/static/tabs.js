"use strict";
/** @type {Record<String, Element[]>} */
const labelsByText = {};
/** @type {Record<String, Element[]>} */
const labelsByName = {};
/** @type {Record<String, Element[]>} */
const labelsById = {};

// Tab ID pattern: "itab--{tab_name}--{level}_{tab_count}-{node_id}"
const inlinetabRE = new RegExp('itab--([a-zA-Z0-9- ]+)--([0-9]+)_([0-9]+)-(.*)');
const SCROLL_CURRENT = "scroll-current";

class TabId {
  tabName = "";
  level = 0;
  tabCount = 0;
  nodeId = "";

  static isTabId = (tabId) => inlinetabRE.test(tabId);

  static fromString = (idString) => {
    const idMatch = inlinetabRE.exec(idString);
    if (idMatch) {
      const tabId = new TabId();
      tabId.tabName = idMatch[1];
      tabId.level = idMatch[2];
      tabId.tabCount = idMatch[3];
      tabId.nodeId = idMatch[4];
      return tabId;
    }
    return null;
  };

  toString = () => {
    return `itab--${this.tabName}--${this.level}_${this.tabCount}-${this.nodeId}`;
  };
}

function ready() {
  const li = document.getElementsByClassName("tab-label");
  const urlParams = new URLSearchParams(window.location.search);
  const tabs = urlParams.getAll("tabs");

  for (const label of li) {
    console.log(`process tab label ${label} (${label.textContent})`);
    label.onclick = onLabelClick;
    const text = label.textContent;
    if (!labelsByText[text]) {
      console.debug(`create new labelsByText entry for ${text}`);
      labelsByText[text] = [];
    }
    console.debug(`sphinx_inline_tabs: labelsByText[${text}].push(${label})`);
    labelsByText[text].push(label);

    const childSpans = label.getElementsByTagName("span");
    console.debug(`${childSpans.length} child spans`);
    if (childSpans.length > 0) {
      const spanId = childSpans[0].getAttribute("id")
      console.debug(`child span ${spanId}`);
      if (!labelsByName[spanId]) {
        console.debug(`create new labelsByName entry for ${spanId}`);
        labelsByName[spanId] = [];
      }
      console.debug(`sphinx_inline_tabs: labelsByName[${spanId}].push(${label})`);
      labelsByName[spanId].push(label);
      const tabId = TabId.fromString(spanId);
      console.debug(`sphinx_inline_tabs: tabId=${tabId ? tabId.toString() : 'null'}`);
      if (tabId !== null) {
        if (!labelsById[tabId.tabName]) {
          console.debug(`create new labelsById entry for ${tabId.tabName}`);
          labelsById[tabId.tabName] = [];
        }
        console.debug(`sphinx_inline_tabs: labelsById[${tabId.tabName}].push(${label})`);
        labelsById[tabId.tabName].push(label);
      }
    }
  }

  for (const tab of tabs) {
    for (const label of labelsByText[tab]) {
      label.previousSibling.checked = true;
    }
  }

  if (li.length > 0) {
    // Ensure theme toggle is displayed
    document.body.parentNode.classList.remove("no-js");

    // Attach event handlers for toggling themes
    const buttons = document.getElementsByClassName("theme-toggle");
    for (const button of buttons) {
      button.addEventListener("click", cycleThemeOnce);
    }

    // Reset the active section in the ToC
    updateScrollCurrentForHash("");

    // Register the hashchange handler
    window.addEventListener("hashchange", onHashchange);
  }
}

function onLabelClick() {
  // Activate other labels with the same text.
  console.debug(`sphinx_inline_tabs: onLabelClick(); textContent=${this.textContent}`);
  for (const label of labelsByText[this.textContent]) {
    label.previousSibling.checked = true;
  }
}

function onHashchange() {
  const hash = decodeURIComponent(window.location.hash.substring(1));
  console.log(`sphinx_inline_tabs: hash change to inlinetab; ${hash}`);
  if (!TabId.isTabId(hash)) {
    console.debug(`sphinx_inline_tabs: ${hash} is not a TabId; update scroll-current for hash as-is`);
    updateScrollCurrentForHash(hash);
    return;
  }
  const tabId = TabId.fromString(hash);
  if (tabId === null) {
    console.error(`sphinx_inline_tabs: TabId of hash ${hash} was null; this is unexpected`);
    updateScrollCurrentForHash(hash);
    return;
  }
  // check full hash
  console.debug(`sphinx_inline_tabs: ${hash} in labelsByName = ${hash in labelsByName}`);
  if (hash in labelsByName && labelsByName[hash].length > 0) {
    const labelElement = labelsByName[hash][0];
    if (labelElement) {
      console.debug(`sphinx_inline_tabs: labelsByName[${hash}][0].click()`);
      labelElement.click();
      console.debug(`sphinx_inline_tabs: update scroll-current for hash ${hash}`);
      updateScrollCurrentForHash(hash);
      return;
    }
  }
  // extract tab id and check labels_by_id
  console.debug(`sphinx_inline_tabs: tabId=${tabId.toString()}`);
  console.debug(`sphinx_inline_tabs: ${tabId.tabName} in labelsById = ${tabId.tabName in labelsById}`);
  if (tabId.tabName in labelsById && labelsById[tabId.tabName].length > 0) {
    const labelElement = labelsById[tabId.tabName][0];
    if (labelElement) {
      console.debug(`sphinx_inline_tabs: labelsById[${tabId.tabName}][0].click()`);
      labelElement.click();
      console.debug(`sphinx_inline_tabs: re-run current window hash`);
      window.location.hash = `${window.location.hash}`;
    }
  }
  console.debug(`sphinx_inline_tabs: update scroll-current for hash ${hash}`);
  updateScrollCurrentForHash(hash);
}

/**
 *
 * @param hash {String}
 */
function updateScrollCurrentForHash(hash) {
  // set class of <a href="#id"> to "scroll-current"; remove from others
  const toctreeDiv = document.getElementsByClassName("toc-tree");
  if (toctreeDiv && toctreeDiv.length) {
    const listitemElements = toctreeDiv[0].getElementsByTagName("li");
    for (const listitemElement of listitemElements) {
      const anchorElements = listitemElement.getElementsByTagName("a");
      if (anchorElements.length) {
        const anchorHref = anchorElements[0].getAttribute("href");
        if (!anchorHref) {
          console.warn('sphinx_inline_tabs: skip anchorElem since anchorHref is falsy');
          continue;
        }
        const anchorId = anchorHref.length > 1 ? anchorHref.substring(1) : "";
        if (anchorId !== "" && anchorId === hash) {
          if (!listitemElement.classList.contains(SCROLL_CURRENT)) {
            console.debug(`sphinx_inline_tabs: [${anchorId}] add scroll-current`);
            listitemElement.classList.add(SCROLL_CURRENT);
          }
        } else {
          if (listitemElement.classList.contains(SCROLL_CURRENT)) {
            console.debug(`sphinx_inline_tabs: [${anchorId}] remove scroll-current`);
            listitemElement.classList.remove(SCROLL_CURRENT);
          }
        }
      }
    }
  }
}

/**
 * Set theme mode
 * @param mode {String} One of "light", "dark", or "auto".
 */
function setTheme(mode) {
  if (mode !== "light" && mode !== "dark" && mode !== "auto") {
    console.error(`Got invalid theme mode: ${mode}. Resetting to auto.`);
    mode = "auto";
  }
  document.body.dataset.theme = mode;
  localStorage.setItem("theme", mode);
  console.log(`sphinx_inline_tabs: Changed to ${mode} mode.`);
}

function cycleThemeOnce() {
  const currentTheme = localStorage.getItem("theme") || "auto";
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

  if (prefersDark) {
    // Auto (dark) -> Light -> Dark
    if (currentTheme === "auto") {
      setTheme("light");
    } else if (currentTheme === "light") {
      setTheme("dark");
    } else {
      setTheme("auto");
    }
  } else {
    // Auto (light) -> Dark -> Light
    if (currentTheme === "auto") {
      setTheme("dark");
    } else if (currentTheme === "dark") {
      setTheme("light");
    } else {
      setTheme("auto");
    }
  }
}

document.addEventListener("DOMContentLoaded", ready, false);
