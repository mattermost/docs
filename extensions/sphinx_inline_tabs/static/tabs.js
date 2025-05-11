var labels_by_text = {};
const labels_by_name = {};
const labels_by_id = {};

// "inlinetab--{tab_name}--{level}-{node_id}"
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
    console.log(`labels_by_text[${text}].push(${label})`);
    labels_by_text[text].push(label);

    const childSpans = label.getElementsByTagName("span");
    if (childSpans.length) {
      const spanId = childSpans[0].getAttribute("id")
      if (!labels_by_name[spanId]) {
        labels_by_name[spanId] = [];
      }
      console.log(`labels_by_name[${spanId}].push(${label})`);
      labels_by_name[spanId].push(label);
      if (inlinetabRE.test(spanId)) {
        const reExecArray = inlinetabRE.exec(spanId);
        const tabId = reExecArray[1];
        if (!labels_by_id[tabId]) {
          labels_by_id[tabId] = [];
        }
        console.log(`labels_by_id[${tabId}].push(${label})`);
        labels_by_id[tabId].push(label);
      }
    }
  }

  for (const tab of tabs) {
    for (label of labels_by_text[tab]) {
      label.previousSibling.checked = true;
    }
  }

  addHashchangeListener();
}

function onLabelClick() {
  // Activate other labels with the same text.
  for (label of labels_by_text[this.textContent]) {
    label.previousSibling.checked = true;
  }
}

function addHashchangeListener() {
  window.addEventListener("hashchange", function() {
    const hash = decodeURIComponent(window.location.hash.substring(1));
    if (inlinetabRE.test(hash)) {
      console.log(`sphinx_inline_tabs: hash change to inlinetab; ${hash}`);
      // check full hash
      if (hash in labels_by_name && labels_by_name[hash].length > 0) {
        const labelElement = labels_by_name[hash][0];
        if (labelElement) {
          console.log(`sphinx_inline_tabs: labels_by_name[${hash}][0].click()`);
          labelElement.click();
        }
      } else {
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
      }
      // set class of <a href="#id"> to "scroll-current"; remove from others
      const toctreeDiv = document.getElementsByClassName("toc-tree");
      if (toctreeDiv && toctreeDiv.length) {
        const listitemElements = toctreeDiv[0].getElementsByTagName("li");
        for (const listitemElement of listitemElements) {
          const anchorElements = listitemElement.getElementsByTagName("a");
          if (anchorElements.length) {
            const anchorHref = anchorElements[0].getAttribute("href");
            if (!anchorHref) {
              console.log('+++ skip anchorElem since anchorHref is falsy');
              continue;
            }
            const anchorId = anchorHref.substring(1);
            if (anchorId === hash) {
              if (!listitemElement.classList.contains("scroll-current")) {
                console.log(`[${anchorId}] add scroll-current`);
                listitemElement.classList.add("scroll-current");
              }
            } else {
              if (listitemElement.classList.contains("scroll-current")) {
                console.log(`[${anchorId}] remove scroll-current`);
                listitemElement.classList.remove("scroll-current");
              }
            }
          }
        }
      }
    }
  });
}

document.addEventListener("DOMContentLoaded", ready, false);
