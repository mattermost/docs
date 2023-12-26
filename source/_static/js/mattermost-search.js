/*
 * searchtools.js
 * ~~~~~~~~~~~~~~~~
 *
 * Sphinx JavaScript utilities for the full-text search.
 *
 * :copyright: Copyright 2007-2023 by the Sphinx team, see AUTHORS.
 * :license: BSD, see LICENSE for details.
 *
 */
"use strict";

/*
NOTE:
This file is specific to Sphinx v7.2.6. If the version of Sphinx used to build
these docs changes, this file will need to be re-written based on that version.
Search may not work correctly if this is not done.
 */

/**
 * @typedef ScorerObject
 * @type {object}
 * @property {function(SearchResult): number} [score]
 * @property {number} objNameMatch
 * @property {number} objPartialMatch
 * @property {Record<string, number>} objPrio
 * @property {number} objPrioDefault
 * @property {number} title
 * @property {number} partialTitle
 * @property {number} term
 * @property {number} partialTerm
 */

/**
 * Search scorer
 * @type {ScorerObject}
 */
const Scorer = {
    // Implement the following function to further tweak the score for each result.
    // The function takes a SearchResult object and returns the new score.
    /*
    score: function(searchResult) {
        return searchResult.score;
    },
    */

    // query matches the full name of an object
    objNameMatch: 11,
    // or matches in the last dotted part of the object name
    objPartialMatch: 6,
    // Additive scores depending on the priority of the object
    objPrio: {
        0: 15,   // used to be importantResults
        1: 5,   // used to be objectResults
        2: -5
    },  // used to be unimportantResults
    //  Used when the priority is not in the mapping.
    objPrioDefault: 0,

    // query found in title
    title: 15,
    partialTitle: 7,
    // query found in terms
    term: 5,
    partialTerm: 2
};

/* JSDoc type definition for search index */
/**
 * @typedef SearchIndex
 * @type {(object|null)}
 * @property {Array<string>} docnames An ordered array of document names
 * @property {Array<string>} filenames An ordered array of document filenames
 * @property {Array<string>} titles A list of document titles
 * @property {Record<string,Array<number>>} terms A map of search terms to an array of matching document IDs
 * @property {Record<string,Array<Array<(string|number)>>>} objects A map of object type to an array of ...?
 * @property {Record<string,string>} objtypes
 * @property {Record<string,Array<string>>} objnames
 * @property {Record<string,Array<number>>} titleterms A map of title search terms to an array of matching document IDs
 * @property {Record<string,number>} envversion A map of version information (e.g., domains)
 * @property {Record<string,Array<Array<(string|number)>>>} alltitles
 * @property {Record<string,any>} indexentries
 */

/* JSDoc type definition for a config setting search index record */
/**
 * @typedef ConfigSettingRecord
 * @type {object}
 * @property {string} id
 * @property {string} docname
 * @property {string} anchor
 * @property {string} displayname
 * @property {string} systemconsole
 * @property {string} configjson
 * @property {string} environment
 * @property {string} description
 */

/* JSDoc type definition for the config setting search result */
/**
 * @typedef ConfigSettingSearchResult
 * @type {object}
 * @property {number} score
 * @property {ConfigSettingRecord} page
 * @property {Record<string,any>} matchData
 */

/* JSDoc type definition for a search result */
/**
 * @typedef SearchResult
 * @type {object}
 * @property {string} docname The docname of the result
 * @property {string} title The title of the document
 * @property {string} anchor The anchor to the content, if any
 * @property {string} description The description of the document
 * @property {number} score The score of the result
 * @property {string} filename The filename of the result document
 * @property {boolean} isObject Indicates the result was found by an object search
 */

/**
 * Default splitQuery function. Can be overridden in ``sphinx.search`` with a
 * custom function per language.
 *
 * The regular expression works by splitting the string on consecutive characters
 * that are not Unicode letters, numbers, underscores, or emoji characters.
 * This is the same as ``\W+`` in Python, preserving the surrogate pair area.
 *
 * @param {string} query
 * @returns {Array<string>}
 */
const splitQuery = (query) => query
    .split(/[^\p{Letter}\p{Number}_\p{Emoji_Presentation}]+/gu)
    .filter(term => term);  // remove remaining empty strings

/**
 * Remove all children of the specified element
 *
 * @param {HTMLElement} element
 * @private
 */
const _removeChildren = (element) => {
    while (element && element.lastChild) element.removeChild(element.lastChild);
};

/**
 * See https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#escaping
 * @param {string} str
 * @returns {string}
 */
const _escapeRegExp = (str) =>
    str.replace(/[.*+\-?^${}()|[\]\\]/g, "\\$&"); // $& means the whole matched string

/**
 * The main search module
 */
class SearchClass {
    /**
     * The length of text to use for the summary of each search result. If the summary text
     * is longer than this length, an ellipsis (...) will be appended.
     * The Sphinx default value is 240.
     * @type {number}
     */
    _summaryTextLength = 300;
    /**
     * Use the default Sphinx search summary generator instead of using the first x characters
     * of the summary text.
     * @type {boolean}
     */
    _useDefaultSearchSummary = false;
    /**
     * The search index
     * @type {(SearchIndex|null)}
     */
    _index = null;
    /**
     * The config settings search index
     * @type {(Array<ConfigSettingRecord>|null)}
     */
    _configSettingIndex = null;
    /** @type {(lunr.Index|null)} */
    _lunrConfigSettingIndex = null;
    /** @type {(string|null)} */
    _queued_query = null;
    /** @type {number} */
    _pulse_status = -1;
    /** @type {HTMLDivElement} */
    out = null;
    /** @type {HTMLHeadingElement} */
    title = null
    /** @type {HTMLHeadingElement} */
    dots = null;
    /** @type {HTMLParagraphElement} */
    status = null;
    /** @type {HTMLUListElement} */
    output = null;

    init() {
        const query = new URLSearchParams(window.location.search).get("q");
        document.querySelectorAll('input[name="q"]')
            .forEach((el) => (el.value = query));
        if (query !== null && query !== "") {
            this.performSearch(query);
        }
    }

    /**
     * Convert the supplied HTML string into text
     * @param {string} htmlString
     * @returns {string}
     */
    htmlToText(htmlString) {
        const htmlElement = new DOMParser().parseFromString(htmlString, 'text/html');
        htmlElement.querySelectorAll(".headerlink").forEach((el) => { el.remove() });
        const docContent = htmlElement.querySelector('[role="main"]');
        if (docContent !== undefined) return docContent.textContent;
        console.warn(
            "Content block not found. Sphinx search tries to obtain it via '[role=main]'. Could you check your theme or template."
        );
        return "";
    }

    /**
     * Strips all HTML tags from the source string and returns it
     * @param {string} htmlString The source HTML string
     * @returns {string} The source string stripped of all HTML tags
     */
    stripHtml(htmlString) {
        const doc = new DOMParser().parseFromString(htmlString, 'text/html');
        return doc.body.textContent || '';
    }

    /**
     * Load the search index data from the specified URL
     * @param url {string} The URL to load search index data from
     */
    loadIndex(url) {
        document.body.appendChild(document.createElement("script")).src = url;
    }

    /**
     * Set search index data and perform a search if a queued query exists
     * @param index {SearchIndex}
     */
    setIndex(index) {
        this._index = index;
        if (this.hasIndex() && this.hasConfigSettingsIndex() && this._queued_query !== null) {
            const query = this._queued_query;
            this._queued_query = null;
            console.log(`setIndex(): running query; query=${query}`);
            this.query(query);
        }
    }

    hasIndex() {
        return this._index !== null;
    }

    loadConfigSettingsIndex(url) {
        console.log(`loadConfigSettingsIndex(): loading index from ${url}`);
        fetch(url)
            .catch((e) => {
                console.error(e);
            })
            .then((response) => response.text())
            .then((data) => {
                // console.log(`loadConfigSettingsIndex(): data=${data}`);
                /** @type {Array<ConfigSettingRecord>} */
                const decoded = JSON.parse(data);
                this.setConfigSettingsIndex(decoded);
            });
    }

    /**
     * Split configjson field data differently
     * @param {lunr.Token} token
     * @returns {(undefined|null|string|lunr.Token|Array<lunr.Token>)}
     */
    configjsonFilter(token) {
        if (token.metadata["fields"] && token.metadata["fields"].indexOf("configjson") === -1) {
            return token;
        }
        /** @type {Array<lunr.Token>} */
        const replaced = []
        const toks = token.toString().split(".");
        for (const tok of toks) {
            if (tok === "") {
                continue;
            }
            replaced.push(new lunr.Token(tok));
        }
        return replaced;
    }

    /**
     * Split environment variable field data differently
     * @param {lunr.Token} token
     * @returns {(undefined|null|string|lunr.Token|Array<lunr.Token>)}
     */
    environmentVarFilter(token) {
        if (token.metadata["fields"] && token.metadata["fields"].indexOf("environment") === -1) {
            return token;
        }
        const tokenString = token.toString().replaceAll("MM_", "");
        /** @type {Array<lunr.Token>} */
        const replaced = []
        const toks = tokenString.split("_");
        for (const tok of toks) {
            if (tok === "") {
                continue;
            }
            replaced.push(new lunr.Token(tok));
        }
        return replaced;
    }

    /**
     * Set the configuration settings search index
     * @param {Array<ConfigSettingRecord>} index
     */
    setConfigSettingsIndex(index) {
        this._configSettingIndex = index;
        // console.log("setConfigSettingsIndex(): start building lunr index");
        lunr.Pipeline.registerFunction(this.configjsonFilter, 'configjsonFilter');
        lunr.Pipeline.registerFunction(this.environmentVarFilter, 'environmentVarFilter');
        this._lunrConfigSettingIndex = lunr((builder) => {
            builder.pipeline.before(lunr.stemmer, this.configjsonFilter);
            builder.pipeline.before(lunr.stemmer, this.environmentVarFilter);
            builder.field("displayname", { boost: 1 });
            builder.field("systemconsole", { boost: 0.5 });
            builder.field("configjson", {});
            builder.field("environment", {});
            builder.field("description", { boost: 2 });
            builder.ref("anchor");
            for (const record of index) {
                // console.log(`lunr(): record=${JSON.stringify(record)}`);
                // Strip HTML tags from the description field before adding it to the Lunr index
                const strippedDescriptionRecord = { ...record };
                strippedDescriptionRecord.description = this.stripHtml(record.description);
                builder.add(strippedDescriptionRecord);
            }
        });
        // console.log("setConfigSettingsIndex(): finished building lunr index");
        if (this.hasIndex() && this.hasConfigSettingsIndex() && this._queued_query !== null) {
            const query = this._queued_query;
            this._queued_query = null;
            // console.log(`setConfigSettingsIndex(): running query; query=${q}`);
            this.query(query);
        }
    }

    hasConfigSettingsIndex() {
        return this._configSettingIndex !== null && this._lunrConfigSettingIndex !== null;
    }

    /**
     * Queue a query to run at a later time
     * @param query {string} The query to queue
     */
    deferQuery(query) {
        this._queued_query = query;
    }

    stopPulse() {
        this._pulse_status = 0;
    }

    startPulse() {
        if (this._pulse_status >= 0)
            return;
        const pulse = () => {
            if (this._pulse_status < 0)
                return;
            this._pulse_status = (this._pulse_status + 1) % 4;
            let dotString = '';
            for (let i = 0; i < this._pulse_status; i++)
                dotString += '.';
            this.dots.innerText = dotString;
            if (this._pulse_status > -1)
                setTimeout(pulse, 500);
        };
        pulse();
    }

    /**
     * perform a search for something (or wait until index is loaded)
     * @param query {string} The search query to perform
     */
    performSearch(query) {
        // create the required interface elements
        this.out = document.getElementById("search-results");
        this.title = document.getElementById("search-title");
        this.dots = document.getElementById("search-dots");
        this.status = document.getElementById("search-summary");
        this.output = document.getElementById("search-results-list");

        this.status.innerText = _('Preparing search...');
        this.startPulse();

        // index already loaded, the browser was quick!
        if (this.hasIndex() && this.hasConfigSettingsIndex()) {
            this.query(query);
            return;
        }
        this.deferQuery(query);
    }

    /**
     * Search through configuration settings for matches on the query terms
     * @param {string} query The search query
     * @returns {Array<ConfigSettingSearchResult>} The config setting search results
     */
    queryConfigSettings(query) {
        /** @type {Array<ConfigSettingSearchResult>} */
        let configSettingSearchResults = [];
        if (this.hasConfigSettingsIndex()) {
            console.log("query(): searching lunr");
            /** @type {Array<{score: number, ref: string, matchData: Record<string,any>}>} */
            const lunrResults = this._lunrConfigSettingIndex.search(query);
            console.log(`query(): lunr search returned ${lunrResults.length} results`);
            configSettingSearchResults = lunrResults.map((result) => {
                /** @type {Array<ConfigSettingRecord>} */
                const configSetting = this._configSettingIndex.filter((setting) => setting["anchor"] === result.ref);
                return {
                    score: result.score,
                    page: configSetting[0],
                    matchData: result.matchData,
                };
            });
            // sort the results by descending score
            configSettingSearchResults = configSettingSearchResults.sort((a, b) => {
                return (a.score > b.score) ? 1 : ((a.score < b.score) ? -1 : 0);
            });
        }
        return configSettingSearchResults;
    }

    /**
     * Sort the search results by score
     * @param {Array<SearchResult>} results The search results to sort
     * @returns {Array<SearchResult>} The sorted search results
     */
    sortSearchResults(results) {
        // sort results into buckets by score
        /** @type {Record<number, Array<SearchResult>>} */
        const resultsByScore = {}
        for (const result of results) {
            if (result.score in resultsByScore) {
                resultsByScore[Number(result.score)].push(result);
            } else {
                resultsByScore[Number(result.score)] = [result];
            }
        }
        // sort the bucket keys numerically, highest to lowest
        const rbsKeys = Object.keys(resultsByScore).sort((a, b) => {
            const left = Number(a);
            const right = Number(b);
            return (left > right) ? 1 : ((left < right) ? -1 : 0);
        });
        // add each bucket of results to the final array of results
        /** @type {Array<SearchResult>} */
        const sortedResults = [];
        for (const rbsKey of rbsKeys) {
            // sort the results in each bucket alphabetically by title
            const sorted = resultsByScore[rbsKey].sort((a, b) => {
                const left = String(a.title).toLowerCase();
                const right = String(b.title).toLowerCase();
                return (left > right) ? -1 : ((left < right) ? 1 : 0);
            });
            sortedResults.push(...sorted);
        }
        return sortedResults;
    }

    /**
     * execute search (requires search index to be loaded)
     * @param query {string} The search query to perform
     */
    query(query) {
        const filenames = Search._index.filenames;
        const docNames = Search._index.docnames;
        const titles = Search._index.titles;
        const allTitles = Search._index.alltitles;
        const indexEntries = Search._index.indexentries;

        // stem the searchterms and add them to the correct list
        const stemmer = new Stemmer();
        /** @type {Set<string>} */
        const searchTerms = new Set();
        /** @type {Set<string>} */
        const excludedTerms = new Set();
        /** @type {Set<string>} */
        const highlightTerms = new Set();
        //const tmp = splitQuery(query);
        const objectTerms = new Set(splitQuery(query.toLowerCase().trim()));

        splitQuery(query.trim()).forEach((queryTerm) => {
            const queryTermLower = queryTerm.toLowerCase();

            // maybe skip this "word"
            // stopwords array is from language_data.js
            if (
                stopwords.indexOf(queryTermLower) !== -1 ||
                queryTerm.match(/^\d+$/)
            )
                return;

            // stem the word
            /** @type {string} */
            const word = stemmer.stemWord(queryTermLower);
            // select the correct list
            if (word[0] === "-") excludedTerms.add(word.substring(1));
            else {
                searchTerms.add(word);
                highlightTerms.add(queryTermLower);
            }
        });

        if (SPHINX_HIGHLIGHT_ENABLED) {  // set in sphinx_highlight.js
            localStorage.setItem("sphinx_highlight_terms", [...highlightTerms].join(" "))
        }

        // console.debug("SEARCH: searching for:");
        // console.info("required: ", [...searchTerms]);
        // console.info("excluded: ", [...excludedTerms]);

        /** @type {Array<SearchResult>} */
        let results = [];
        _removeChildren(document.getElementById("search-search-summary"));

        // Perform a config settings search
        const configSettingSearchResults = this.queryConfigSettings(query);

        const queryLower = query.toLowerCase();
        for (const [title, foundTitles] of Object.entries(allTitles)) {
            if (title.toLowerCase().includes(queryLower) && (queryLower.length >= title.length/2)) {
                for (const [file, id] of foundTitles) {
                    let score = Math.round(100 * queryLower.length / title.length)
                    results.push({
                        docname: docNames[file],
                        title: titles[file] !== title ? `${titles[file]} > ${title}` : title,
                        anchor: id !== null ? "#" + id : "",
                        description: '',
                        score,
                        filename: filenames[file],
                        isObject: false,
                    });
                }
            }
        }

        // search for explicit entries in index directives
        for (const [entry, foundEntries] of Object.entries(indexEntries)) {
            if (entry.includes(queryLower) && (queryLower.length >= entry.length/2)) {
                for (const [file, id] of foundEntries) {
                    let score = Math.round(100 * queryLower.length / entry.length)
                    results.push({
                        docname: docNames[file],
                        title: titles[file],
                        anchor: id ? "#" + id : "",
                        description: '',
                        score,
                        filename: filenames[file],
                        isObject: false,
                    });
                }
            }
        }

        // Perform an object search
        objectTerms.forEach((term) =>
            results.push(...this.performObjectSearch(term, objectTerms))
        );

        // lookup as search terms in fulltext
        results.push(...this.performTermsSearch(searchTerms, excludedTerms));

        // let the scorer override scores with a custom scoring function
        if (Scorer.score) results.forEach(
            (item) => (item.score = Scorer.score(item))
        );

        // Sort the results
        results = this.sortSearchResults(results);

        // remove duplicate search results
        // note the reversing of results, so that in the case of duplicates, the highest-scoring entry is kept
        const seen = new Set();
        results = results.reverse()
            .reduce((acc, result) => {
                const resultStr =
                    [result.docname, result.title, result.anchor, result.description, result.score, [result.filename]]
                        .map(v => String(v))
                        .join(',');
                if (!seen.has(resultStr)) {
                    acc.push(result);
                    seen.add(resultStr);
                }
                return acc;
            }, []);
        results = results.reverse();

        // If we found config setting results, show the config settings div; otherwise hide it
        const displaySetting = configSettingSearchResults.length > 0 ? "contents" : "none";
        const configSettingsDiv = document.getElementById("config-setting-results-section");
        if (configSettingsDiv) {
            configSettingsDiv.setAttribute("style", "display: " + displaySetting + ";");
        }
        const additionalInfoHeader = document.getElementById("search-additional-information-header");
        if (additionalInfoHeader) {
            additionalInfoHeader.setAttribute("style", "display: " + displaySetting + ";");
        }

        // print the config setting results
        for (let x = configSettingSearchResults.length; x > 0; x--) {
            this.displayConfigSettingResultItem(configSettingSearchResults[x - 1], highlightTerms);
        }
        // print the additional information results
        for (let x = results.length; x > 0; x--) {
            this.displayResultItem(results[x - 1], searchTerms, highlightTerms);
        }

        // we're finished searching; stop the visual indicator and display the results summary
        this.stopPulse();
        this.title.innerText = _('Search Results');
        this.setPostSearchStatus(results.length, configSettingSearchResults.length);
    }

    /**
     * Update the search status field with the results of the search
     * @param {number} numberOfResults
     * @param {number} numberOfConfigSettingResults
     */
    setPostSearchStatus(numberOfResults, numberOfConfigSettingResults) {
        // empty the current status
        this.status.innerText = '';
        // If there were no results, then display an appropriate message and return
        if (!numberOfResults && !numberOfConfigSettingResults) {
            const searchStatusEl = document.getElementById("search-summary");
            if (searchStatusEl) {
                searchStatusEl.innerText = "Your search did not match any documents. Please make sure that all words are spelled correctly.";
            }
            return;
        }
        const prefixSpan = document.createElement('span');
        prefixSpan.innerText = "Search finished, found ";
        const postfixSpan = document.createElement('span');
        postfixSpan.innerText = " matching your search query. Results are sorted by relevance.";
        let configSettingSpan;
        let resultSpan;
        if (numberOfConfigSettingResults) {
            configSettingSpan = document.createElement('span');
            configSettingSpan.innerText = String(numberOfConfigSettingResults) + " ";
            const configSettingLink = document.createElement('a');
            configSettingLink.text = "configuration setting";
            if (numberOfConfigSettingResults > 1) {
                configSettingLink.text += "s";
            }
            configSettingLink.href = "#config-setting-results-anchor";
            configSettingSpan.appendChild(configSettingLink);
        }
        if (numberOfResults) {
            resultSpan = document.createElement('span');
            if (numberOfConfigSettingResults) {
                resultSpan.innerText = String(numberOfResults) + " page";
                resultSpan.innerText += numberOfResults > 1 ? "s of " : " of ";
                const resultSpanLink = document.createElement('a');
                resultSpanLink.text = "additional information";
                resultSpanLink.href = "#search-results-anchor";
                resultSpan.appendChild(resultSpanLink);
            } else {
                resultSpan.innerText = String(numberOfResults) + " document";
                resultSpan.innerText += numberOfResults > 1 ? "s " : " ";
            }
        }
        const searchStatusEl = document.getElementById("search-summary");
        if (searchStatusEl) {
            // prefixSpan + configSettingSpan? + " and "? + resultSpan? + postfixSpan
            searchStatusEl.appendChild(prefixSpan);
            if (configSettingSpan) {
                searchStatusEl.appendChild(configSettingSpan);
                if (resultSpan) {
                    const andSpan = document.createElement('span');
                    andSpan.innerText = " and ";
                    searchStatusEl.appendChild(andSpan);
                }
            }
            if (resultSpan) {
                searchStatusEl.appendChild(resultSpan);
            }
            searchStatusEl.appendChild(postfixSpan);
        }
    }

    /**
     * Display a single config setting search result item
     * @param {ConfigSettingSearchResult} item The result item to display
     * @param {Set<string>} searchTerms The terms used in the search
     */
    displayConfigSettingResultItem(item, searchTerms) {
        // The result info is displayed in a div
        const div = document.createElement("div");
        div.classList.add("config-setting-result-item");

        // Append the link
        const itemLink = document.createElement("a");
        itemLink.classList.add("config-setting-result-item_link");
        itemLink.innerText = item.page.displayname;
        itemLink.href = item.page.anchor;
        div.appendChild(itemLink);

        // Create a table to hold the description and the config setting metadata
        const table = document.createElement("table");
        table.classList.add("docutils", "align-default");
        // Table has 2 columns, each taking 50% of the table width
        const tableColGroup = document.createElement("colgroup");
        const tableColDesc = document.createElement("col");
        tableColDesc.style.width = "50%";
        const tableColDetail = document.createElement("col");
        tableColDetail.style.width = "50%";
        tableColGroup.append(tableColDesc, tableColDetail);
        // Add the column group to the table
        table.appendChild(tableColGroup);
        // Table body contains one row
        const tableBody = document.createElement("tbody");
        const tableRow = document.createElement("tr");
        tableRow.classList.add("row-odd");
        // The first cell contains the description of the config setting
        const itemDescCell = document.createElement("td");
        itemDescCell.innerHTML = item.page.description;
        // The second cell contains metadata about the config setting
        const itemDetailCell = document.createElement("td");
        const itemDetailCellList = document.createElement("ul");
        itemDetailCellList.style.listStyleType = "disc";
        // System console path
        const systemconsoleDetail = document.createElement("li");
        const systemconsoleDetailLabel = document.createElement("span");
        systemconsoleDetailLabel.innerText = "System Config path: ";
        const systemconsoleDetailValue = document.createElement("b");
        systemconsoleDetailValue.innerText = item.page.systemconsole;
        systemconsoleDetail.append(systemconsoleDetailLabel, systemconsoleDetailValue);
        // config.json setting
        const configjsonDetail = document.createElement("li");
        const configjsonCode = document.createElement("code");
        configjsonCode.classList.add("docutils", "literal", "notranslate");
        configjsonCode.innerText = "config.json";
        const configjsonDetailLabel = document.createElement("span");
        configjsonDetailLabel.innerText = " setting: ";
        const configjsonDetailValue = document.createElement("code");
        configjsonDetailValue.innerText = item.page.configjson;
        configjsonDetailValue.classList.add("docutils", "literal", "notranslate");
        configjsonDetail.append(configjsonCode, configjsonDetailLabel, configjsonDetailValue);
        // Environment variable
        const environmentDetail = document.createElement("li");
        const environmentDetailLabel = document.createElement("span");
        environmentDetailLabel.innerText = "Environment variable: ";
        const environmentDetailValue = document.createElement("code");
        environmentDetailValue.innerText = item.page.environment;
        environmentDetailValue.classList.add("docutils", "literal", "notranslate");
        environmentDetail.append(environmentDetailLabel, environmentDetailValue);
        itemDetailCellList.append(systemconsoleDetail, configjsonDetail, environmentDetail);
        itemDetailCell.append(itemDetailCellList);
        // Add the two cells to the table row
        tableRow.append(itemDescCell, itemDetailCell);
        // Add the table row to the table body
        tableBody.appendChild(tableRow);
        // Add the table body to the table
        table.appendChild(tableBody);

        // Append the description table
        div.appendChild(table);

        // DEBUG: display score and match data
        // const debugPara = document.createElement('p');
        // debugPara.innerText = `score=${item.score}, matchData=${JSON.stringify(item.matchData)}`;
        // div.appendChild(debugPara);

        // Highlight search terms in the description cell
        const mark = new Mark(itemDescCell);
        for (const searchTerm of searchTerms) {
            // Only highlight search terms longer than one character
            if (searchTerm.length > 1) {
                mark.mark(searchTerm);
            }
        }

        // Find the results div and add this result to it
        const resultsListEl = document.getElementById("config-setting-results-list");
        if (resultsListEl) {
            resultsListEl.appendChild(div);
        }
    }

    /**
     * Display a single search result
     * @param item {SearchResult}
     * @param searchTerms {Set<string>}
     * @param highlightTerms {Set<string>}
     */
    displayResultItem(item, searchTerms, highlightTerms) {
        /** @type {String} */
        let requestUrl;
        /** @type {String} */
        let linkUrl;
        const contentRoot = document.documentElement.dataset.content_root;
        const docFileSuffix = DOCUMENTATION_OPTIONS.FILE_SUFFIX;
        const docLinkSuffix = DOCUMENTATION_OPTIONS.LINK_SUFFIX;
        const showSearchSummary = DOCUMENTATION_OPTIONS.SHOW_SEARCH_SUMMARY;
        // The result info is displayed as a list item
        const listItem = document.createElement("li");
        if (DOCUMENTATION_OPTIONS.BUILDER === 'dirhtml') {
            // dirhtml builder
            let dirname = item.docname + "/";
            if (dirname.match(/\/index\/$/))
                dirname = dirname.substring(0, dirname.length - 6);
            else if (dirname === "index/") dirname = "";
            requestUrl = contentRoot + dirname;
            linkUrl = requestUrl;
        } else {
            // normal html builders
            requestUrl = contentRoot + item.docname + docFileSuffix;
            linkUrl = item.docname + docLinkSuffix;
        }
        // Write the result's link
        const linkEl = listItem.appendChild(document.createElement("a"));
        linkEl.href = linkUrl + item.anchor;
        linkEl.dataset.score = String(item.score);
        linkEl.innerHTML = item.title;
        // Write the result's description
        if (item.description !== "") {
            // If the result already includes a description, use it
            const descSpan = listItem.appendChild(document.createElement('span'));
            descSpan.innerText = `(${item.description})`
        } else if (showSearchSummary) {
            // If we're configured to read the source HTML page for a description, do that
            fetch(requestUrl)
                .then((responseData) => responseData.text())
                .then((data) => {
                    if (data) {
                        const summaryEl = this.makeSearchSummary(data, searchTerms);
                        if (summaryEl) {
                            listItem.appendChild(summaryEl);
                        }
                    }
                    // highlight search terms in the summary
                    if (SPHINX_HIGHLIGHT_ENABLED)  // set in sphinx_highlight.js
                        highlightTerms.forEach((term) => _highlightText(listItem, term, "highlighted"));
                });
        }
        setTimeout(() => {
            const resultsListEl = document.getElementById('search-results-list');
            if (resultsListEl) {
                resultsListEl.appendChild(listItem);
            }
        }, 5);
    }

    /* JSDoc type definition for an object in the objects list */
    /**
     * @typedef ObjectDef
     * @type {object}
     * @property {number} docnameIndex The index into docnames for the document this object lives in
     * @property {number} objectTypeIndex The index into objtypes for the type of this object
     * @property {number} priority The priority of this result
     * @property {string} anchor The section anchor, if any
     * @property {string} name The object name
     */

    /**
     * search for object names
     * @param object {string}
     * @param objectTerms {Set<string>}
     * @returns {Array<SearchResult>}
     */
    performObjectSearch(object, objectTerms) {
        const filenames = this._index.filenames;
        const docNames = this._index.docnames;
        const objects = this._index.objects;
        const objNames = this._index.objnames;
        const titles = this._index.titles;

        /** @type {Array<SearchResult>} */
        const results = [];

        /**
         * Object search callback function
         * @param {string} prefix
         * @param {Array<String | Number>} match
         */
        const objectSearchCallback = (prefix, match) => {
            /** @type {string} */
            const name = match[4]
            const fullname = (prefix ? prefix + "." : "") + name;
            const fullnameLower = fullname.toLowerCase();
            if (fullnameLower.indexOf(object) < 0) return;

            let score = 0;
            const parts = fullnameLower.split(".");

            // check for different match types: exact matches of full name or
            // "last name" (i.e. last dotted part)
            if (fullnameLower === object || parts.slice(-1)[0] === object)
                score += Scorer.objNameMatch;
            else if (parts.slice(-1)[0].indexOf(object) > -1)
                score += Scorer.objPartialMatch; // matches in last name

            const objName = objNames[match[1]][2];
            const title = titles[match[0]];

            // If more than one term searched for, we require other words to be
            // found in the name/title/description
            const otherTerms = new Set(objectTerms);
            otherTerms.delete(object);
            if (otherTerms.size > 0) {
                const haystack = `${prefix} ${name} ${objName} ${title}`.toLowerCase();
                if (
                    [...otherTerms].some((otherTerm) => haystack.indexOf(otherTerm) < 0)
                )
                    return;
            }

            /** @type {string} */
            let anchor = match[3];
            if (anchor === "") anchor = fullname;
            else if (anchor === "-") anchor = objNames[match[1]][1] + "-" + fullname;

            const descr = objName + _(", in ") + title;

            // add custom score for some objects according to scorer
            if (Scorer.objPrio.hasOwnProperty(match[2]))
                score += Scorer.objPrio[match[2]];
            else score += Scorer.objPrioDefault;

            results.push({
                docname: docNames[match[0]],
                title: fullname,
                anchor: "#" + anchor,
                description: descr,
                score,
                filename: filenames[match[0]],
                isObject: true,
            })
        };
        Object.keys(objects).forEach((prefix) =>
            objects[prefix].forEach((array) =>
                objectSearchCallback(prefix, array)
            )
        );
        return results;
    }

    /**
     * search for full-text terms in the index
     * @param {Set<string>} searchTerms
     * @param {Set<string>} excludedTerms
     * @returns {Array<SearchResult>}
     */
    performTermsSearch(searchTerms, excludedTerms) {
        // prepare search
        const terms = Search._index.terms;
        const titleTerms = Search._index.titleterms;
        const filenames = Search._index.filenames;
        const docNames = Search._index.docnames;
        const titles = Search._index.titles;

        const scoreMap = new Map();
        const fileMap = new Map();

        // perform the search on the required terms
        searchTerms.forEach((word) => {
            const files = [];
            const arr = [
                { files: terms[word], score: Scorer.term },
                { files: titleTerms[word], score: Scorer.title },
            ];
            // add support for partial matches
            if (word.length > 2) {
                const escapedWord = _escapeRegExp(word);
                Object.keys(terms).forEach((term) => {
                    if (term.match(escapedWord) && !terms[word])
                        arr.push({ files: terms[term], score: Scorer.partialTerm });
                });
                Object.keys(titleTerms).forEach((term) => {
                    if (term.match(escapedWord) && !titleTerms[word])
                        arr.push({ files: titleTerms[word], score: Scorer.partialTitle });
                });
            }

            // no match but word was a required one
            if (arr.every((record) => record.files === undefined)) return;

            // found search word in contents
            arr.forEach((record) => {
                if (record.files === undefined) return;

                let recordFiles = record.files;
                if (recordFiles.length === undefined) recordFiles = [recordFiles];
                files.push(...recordFiles);

                // set score for the word in each file
                recordFiles.forEach((file) => {
                    if (!scoreMap.has(file)) scoreMap.set(file, {});
                    scoreMap.get(file)[word] = record.score;
                });
            });

            // create the mapping
            files.forEach((file) => {
                if (fileMap.has(file) && fileMap.get(file).indexOf(word) === -1)
                    fileMap.get(file).push(word);
                else fileMap.set(file, [word]);
            });
        });

        // now check if the files don't contain excluded terms
        const results = [];
        for (const [file, wordList] of fileMap) {
            // check if all requirements are matched

            // as search terms with length < 3 are discarded
            const filteredTermCount = [...searchTerms].filter(
                (term) => term.length > 2
            ).length;
            if (
                wordList.length !== searchTerms.size &&
                wordList.length !== filteredTermCount
            )
                continue;

            // ensure that none of the excluded terms is in the search result
            if (
                [...excludedTerms].some(
                    (term) =>
                        terms[term] === file ||
                        titleTerms[term] === file ||
                        (terms[term] || []).includes(file) ||
                        (titleTerms[term] || []).includes(file)
                )
            )
                break;

            // select one (max) score for the file.
            const score = Math.max(...wordList.map((w) => scoreMap.get(file)[w]));
            // add result to the result list
            results.push({
                docname: docNames[file],
                title: titles[file],
                anchor: '',
                description: '',
                score,
                filename: filenames[file],
                isObject: false,
            });
        }
        return results;
    }

    /**
     * helper function to return a node containing the search summary for a given text.
     *
     * @param {string} htmlText The text to summarize
     * @param {Set<string>} keywords a list of stemmed words; used to find occurrence of the word in the summary
     * @returns {(HTMLParagraphElement|null)}
     */
    makeSearchSummary(htmlText, keywords) {
        const text = this.htmlToText(htmlText);
        if (text === "") {
            return null;
        }

        let summary = document.createElement("p");
        summary.classList.add("context");

        if (this._useDefaultSearchSummary) {
            const textLower = text.toLowerCase();
            const actualStartPosition = [...keywords]
                .map((k) => textLower.indexOf(k.toLowerCase()))
                .filter((i) => i > -1)
                .slice(-1)[0];
            const startWithContext = Math.max(actualStartPosition - 120, 0);

            const top = startWithContext === 0 ? "" : "...";
            const tail = startWithContext + 240 < text.length ? "..." : "";

            summary.textContent = top + text.substring(startWithContext, 240).trim() + tail;
        } else {
            const excerpt = text.substring(0, this._summaryTextLength) + (text.length > this._summaryTextLength ? '...' : '');
            summary.textContent = excerpt.trim();
        }

        return summary;
    }
}

const Search = new SearchClass();
_ready(() => {
    Search.init();
});
