var labels_by_text = {};
const labels_by_id = {};

function ready() {
  var li = document.getElementsByClassName("tab-label");
  const urlParams = new URLSearchParams(window.location.search);
  const tabs = urlParams.getAll("tabs");

  for (const label of li) {
    label.onclick = onLabelClick;
    const text = label.textContent;
    if (!labels_by_text[text]) {
      labels_by_text[text] = [];
    }
    labels_by_text[text].push(label);
    const id = label.getAttribute("id");
    console.log(`id=${id}`);
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

// "inlinetab--{tab_name}--{level}-{node_id}"
const inlinetabRE = new RegExp('inlinetab--([a-zA-Z0-9- ]+)--([0-9]+)-(.*)');

function addHashchangeListener() {
  window.addEventListener("hashchange", function() {
    const hash = window.location.hash;
    if (inlinetabRE.test(hash)) {
      console.log(`sphinx_inline_tabs: hash change to inlinetab; ${hash}`);
      const reExecArray = inlinetabRE.exec(hash);
      const tabName = reExecArray[1];
      const nodeId = reExecArray[3];
      console.log(`sphinx_inline_tabs: tabName=${tabName}, nodeId=${nodeId}`);
      if (tabName in labels_by_text && labels_by_text[tabName].length > 0) {
        const labelElement = labels_by_text[tabName][0];
        if (labelElement) {
          console.log(`sphinx_inline_tabs: labels_by_test[${tabName}][0].click()`);
          labelElement.click();
        }
      }
    }
  });
}

document.addEventListener("DOMContentLoaded", ready, false);
