var labels_by_text = {};
const labels_by_name = {};
const labels_by_id = {};

// Tab ID pattern: "inlinetab--{tab_name}--{level}-{node_id}"
const inlinetabRE = new RegExp('inlinetab--([a-zA-Z0-9- ]+)--([0-9]+)-(.*)');

function ready() {
  const li = document.getElementsByClassName("tab-label");
  const urlParams = new URLSearchParams(window.location.search);
  const tabs = urlParams.getAll("tabs");

  for (const label of li) {
    label.onclick = onLabelClick;
    const text = label.textContent;
    if (!labels_by_text[text]) {
      labels_by_text[text] = [];
    }
    console.log(`sphinx_inline_tabs: labels_by_text[${text}].push(${label})`);
    labels_by_text[text].push(label);

    const childSpans = label.getElementsByTagName("span");
    if (childSpans.length) {
      const spanId = childSpans[0].getAttribute("id")
      if (!labels_by_name[spanId]) {
        labels_by_name[spanId] = [];
      }
      console.log(`sphinx_inline_tabs: labels_by_name[${spanId}].push(${label})`);
      labels_by_name[spanId].push(label);
      if (inlinetabRE.test(spanId)) {
        const reExecArray = inlinetabRE.exec(spanId);
        const tabId = reExecArray[1];
        if (!labels_by_id[tabId]) {
          labels_by_id[tabId] = [];
        }
        console.log(`sphinx_inline_tabs: labels_by_id[${tabId}].push(${label})`);
        labels_by_id[tabId].push(label);
      }
    }
  }

  for (const tab of tabs) {
    for (const label of labels_by_text[tab]) {
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

    updateScrollCurrentForHash("");

    window.addEventListener("hashchange", onHashchange);
  }
}

function onLabelClick() {
  // Activate other labels with the same text.
  for (const label of labels_by_text[this.textContent]) {
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
  if (hash in labels_by_name && labels_by_name[hash].length > 0) {
    const labelElement = labels_by_name[hash][0];
    if (labelElement) {
      console.log(`sphinx_inline_tabs: labels_by_name[${hash}][0].click()`);
      labelElement.click();
      updateScrollCurrentForHash(hash);
      return;
    }
  }
  // extract tab id and check labels_by_id
  const reExecArray = inlinetabRE.exec(hash);
  const tabName = reExecArray[1];
  if (tabName in labels_by_id && labels_by_id[tabName].length > 0) {
    const labelElement = labels_by_id[tabName][0];
    if (labelElement) {
      console.log(`sphinx_inline_tabs: labels_by_id[${tabName}][0].click()`);
      labelElement.click();
      window.location.hash = `${window.location.hash}`;
    }
  }
  updateScrollCurrentForHash(hash);
}

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
          if (!listitemElement.classList.contains("scroll-current")) {
            console.log(`sphinx_inline_tabs: [${anchorId}] add scroll-current`);
            listitemElement.classList.add("scroll-current");
          }
        } else {
          if (listitemElement.classList.contains("scroll-current")) {
            console.log(`sphinx_inline_tabs: [${anchorId}] remove scroll-current`);
            listitemElement.classList.remove("scroll-current");
          }
        }
      }
    }
  }
}

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
