"use strict";
/** @type {Record<String, Element[]>} */
const labelsByText = {};
/** @type {Record<String, Element[]>} */
const labelsByName = {};
/** @type {Record<String, Element[]>} */
const labelsById = {};

// Tab ID pattern: "inlinetab--{tab_name}--{level}-{node_id}"
const inlinetabRE = new RegExp('inlinetab--([a-zA-Z0-9- ]+)--([0-9]+)-(.*)');
const SCROLL_CURRENT = "scroll-current";

function ready() {
  const li = document.getElementsByClassName("tab-label");
  const urlParams = new URLSearchParams(window.location.search);
  const tabs = urlParams.getAll("tabs");

  for (const label of li) {
    label.onclick = onLabelClick;
    const text = label.textContent;
    if (!labelsByText[text]) {
      labelsByText[text] = [];
    }
    console.log(`sphinx_inline_tabs: labelsByText[${text}].push(${label})`);
    labelsByText[text].push(label);

    const childSpans = label.getElementsByTagName("span");
    if (childSpans.length > 0) {
      const spanId = childSpans[0].getAttribute("id")
      if (!labelsByName[spanId]) {
        labelsByName[spanId] = [];
      }
      console.log(`sphinx_inline_tabs: labelsByName[${spanId}].push(${label})`);
      labelsByName[spanId].push(label);
      if (inlinetabRE.test(spanId)) {
        const reExecArray = inlinetabRE.exec(spanId);
        if (reExecArray !== null) {
          const tabId = reExecArray[1];
          if (!labelsById[tabId]) {
            labelsById[tabId] = [];
          }
          console.log(`sphinx_inline_tabs: labelsById[${tabId}].push(${label})`);
          labelsById[tabId].push(label);
        }
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
  for (const label of labelsByText[this.textContent]) {
    label.previousSibling.checked = true;
  }
}

function onHashchange() {
  const hash = decodeURIComponent(window.location.hash.substring(1));
  console.log(`sphinx_inline_tabs: hash change to inlinetab; ${hash}`);
  if (!inlinetabRE.test(hash)) {
    updateScrollCurrentForHash(hash);
    return;
  }
  // check full hash
  if (hash in labelsByName && labelsByName[hash].length > 0) {
    const labelElement = labelsByName[hash][0];
    if (labelElement) {
      console.log(`sphinx_inline_tabs: labelsByName[${hash}][0].click()`);
      labelElement.click();
      updateScrollCurrentForHash(hash);
      return;
    }
  }
  // extract tab id and check labels_by_id
  const reExecArray = inlinetabRE.exec(hash);
  const tabName = reExecArray[1];
  if (tabName in labelsById && labelsById[tabName].length > 0) {
    const labelElement = labelsById[tabName][0];
    if (labelElement) {
      console.log(`sphinx_inline_tabs: labelsById[${tabName}][0].click()`);
      labelElement.click();
      window.location.hash = `${window.location.hash}`;
    }
  }
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
          console.log('sphinx_inline_tabs: skip anchorElem since anchorHref is falsy');
          continue;
        }
        const anchorId = anchorHref.length > 1 ? anchorHref.substring(1) : "";
        if (anchorId !== "" && anchorId === hash) {
          if (!listitemElement.classList.contains(SCROLL_CURRENT)) {
            console.log(`sphinx_inline_tabs: [${anchorId}] add scroll-current`);
            listitemElement.classList.add(SCROLL_CURRENT);
          }
        } else {
          if (listitemElement.classList.contains(SCROLL_CURRENT)) {
            console.log(`sphinx_inline_tabs: [${anchorId}] remove scroll-current`);
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
  console.log(`Changed to ${mode} mode.`);
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
