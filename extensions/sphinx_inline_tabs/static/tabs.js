"use strict";
/**
 * A list of label elements keyed by a text string, usually the name of a Tab
 * @type {Record<String, Element[]>}
 */
const labelsByText = {};
/**
 * A list of label elements keyed by Tab name
 * @type {Record<String, Element[]>}
 */
const labelsByName = {};
/**
 * A list of label elements keyed by TabId
 * @type {Record<String, Element[]>}
 */
const labelsById = {};

// Tab ID pattern: "itab--{tab_name}--{level}_{tab_count}-{node_id}"
const inlinetabRE = new RegExp('itab--([a-zA-Z0-9-.:,\'\(\) ]+)--([0-9]+)_([0-9]+)-(.*)');
const SCROLL_CURRENT = "scroll-current";

/**
 * A JavaScript implementation of the TabId Python class in `tab_id.py`
 */
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

/**
 * Prepares the tab elements and theme toggling functionality on the page.
 * This method initializes event listeners for tab interactions and theme toggling,
 * associates tabs with their respective labels, and ensures proper functionality
 * based on the current URL parameters and state of the document.
 *
 * @return {void} This function does not return a value.
 */
function ready() {
  const li = document.getElementsByClassName("tab-label");
  const urlParams = new URLSearchParams(window.location.search);
  const tabs = urlParams.getAll("tabs");

  for (const label of li) {
    console.log(`sphinx_inline_tabs: process tab label ${label} (${label.textContent})`);
    label.onclick = onLabelClick;
    const text = label.textContent;
    if (!labelsByText[text]) {
      console.debug(`sphinx_inline_tabs: create new labelsByText entry for ${text}`);
      labelsByText[text] = [];
    }
    console.debug(`sphinx_inline_tabs: labelsByText[${text}].push(${label})`);
    labelsByText[text].push(label);

    const childSpans = label.getElementsByTagName("span");
    console.debug(`sphinx_inline_tabs: ${childSpans.length} child spans`);
    if (childSpans.length > 0) {
      const spanId = childSpans[0].getAttribute("id")
      console.debug(`sphinx_inline_tabs: child span ${spanId}`);
      if (!labelsByName[spanId]) {
        console.debug(`sphinx_inline_tabs: create new labelsByName entry for ${spanId}`);
        labelsByName[spanId] = [];
      }
      console.debug(`sphinx_inline_tabs: labelsByName[${spanId}].push(${label})`);
      labelsByName[spanId].push(label);
      const tabId = TabId.fromString(spanId);
      console.debug(`sphinx_inline_tabs: tabId=${tabId ? tabId.toString() : 'null'}`);
      if (tabId !== null) {
        if (!labelsById[tabId.tabName]) {
          console.debug(`sphinx_inline_tabs: create new labelsById entry for ${tabId.tabName}`);
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
    
    // If there's a hash in the URL, handle it now
    if (window.location.hash !== "") {
        onHashchange();
    }

    // Register the hashchange handler
    window.addEventListener("hashchange", onHashchange);
  }
}

/**
 * Handles the click event on a label. Activates all labels sharing the
 * same text by checking their corresponding input element.
 *
 * @return {void} This function does not return a value.
 */
function onLabelClick() {
  // Activate other labels with the same text.
  console.debug(`sphinx_inline_tabs: onLabelClick(); textContent=${this.textContent}`);
  for (const label of labelsByText[this.textContent]) {
    label.previousSibling.checked = true;
  }
}

/**
 * Handles the `hashchange` event triggered when the URL's hash changes.
 * This function decodes the current hash, checks if it corresponds to a valid tab identifier,
 * and updates the UI by activating the appropriate tab and scrolling to its associated content.
 *
 * If the hash corresponds to a valid tab identifier (`TabId`), it activates the tab and its
 * possible parent tab. If the hash is not a `TabId`, it updates the scroll position for the
 * current hash without interacting with tabs.
 *
 * @return {void} No value is returned by this function. The function only performs
 * side effects such as updating the UI and modifying the scroll position.
 */
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
      // If the TabId contains the name of a parent tab, extract it and click its label
      let maybeParentId = tabId.tabName.replace(`-${tabId.nodeId}`, "");
      console.debug(`sphinx_inline_tabs: maybeParentId=${maybeParentId}`);
      if (maybeParentId !== "" && maybeParentId in labelsById && labelsById[maybeParentId].length > 0) {
        const parentLabelElement = labelsById[maybeParentId][0];
        if (parentLabelElement) {
          console.debug(`sphinx_inline_tabs: labelsById[${maybeParentId}][0].click()`);
          parentLabelElement.click();
        }
      }
      // Click the desired tab
      console.debug(`sphinx_inline_tabs: labelsByName[${hash}][0].click()`);
      labelElement.click();
      // Update the scroll position for the current hash
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
      // If the TabId contains the name of a parent tab, extract it and click its label
      let maybeParentId = tabId.tabName.replace(`-${tabId.nodeId}`, "");
      console.debug(`sphinx_inline_tabs: maybeParentId=${maybeParentId}`);
      if (maybeParentId !== "" && maybeParentId in labelsById && labelsById[maybeParentId].length > 0) {
        const parentLabelElement = labelsById[maybeParentId][0];
        if (parentLabelElement) {
          console.debug(`sphinx_inline_tabs: labelsById[${maybeParentId}][0].click()`);
          parentLabelElement.click();
        }
      }
      // Click the desired tab
      console.debug(`sphinx_inline_tabs: labelsById[${tabId.tabName}][0].click()`);
      labelElement.click();
      // Re-run the current window hash
      console.debug(`sphinx_inline_tabs: re-run current window hash`);
      window.location.hash = `${window.location.hash}`;
    }
  }
  console.debug(`sphinx_inline_tabs: update scroll-current for hash ${hash}`);
  updateScrollCurrentForHash(hash);
}

/**
 * Set the SCROLL_CURRENT CSS class on the label element in the ToC that has a given ID
 * @param hash {String} The ID of the label element to set the SCROLL_CURRENT CSS class
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

/**
 * Cycles through the available theme modes (auto, light, dark) once, depending on the current theme mode
 * and the user's system preference for dark mode.
 *
 * The cycling order is:
 * - Auto (dark) -> Light -> Dark if the system prefers dark mode.
 * - Auto (light) -> Dark -> Light if the system prefers light mode.
 *
 * This method updates the theme preference in the localStorage and applies the chosen theme.
 *
 * @return {void} Does not return a value.
 */
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
