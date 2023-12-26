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
 * @property {function(string[]): number} [score]
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
    // Implement the following function to further tweak the score for each result
    // The function takes a result array [filename, title, anchor, descr, score]
    // and returns the new score.
    /*
    score: function(result) {
      return result[4];
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
 * @property {Record<string,number>} envversion A map of version information (e.g., domains)
 * @property {Array<string>} filenames An ordered array of document filenames
 * @property {Record<string,Array<Array<(string|number)>>>} objects A map of object type to an array of ...?
 * @property {Record<string,Array<string>>} objnames
 * @property {Record<string,string>} objtypes
 * @property {Record<string,Array<number>>} terms A map of search terms to an array of matching document IDs
 * @property {Array<string>} titles A list of document titles
 * @property {Record<string,Array<number>>} titleterms A map of title search terms to an array of matching document IDs
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

const _removeChildren = (element) => {
    while (element && element.lastChild) element.removeChild(element.lastChild);
};

/**
 * See https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#escaping
 */
const _escapeRegExp = (string) =>
    string.replace(/[.*+\-?^${}()|[\]\\]/g, "\\$&"); // $& means the whole matched string

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

    init() {
        const query = new URLSearchParams(window.location.search).get("q");
        document
            .querySelectorAll('input[name="q"]')
            .forEach((el) => (el.value = query));
        if (query) this.performSearch(query);
    }

    /**
     * Convert the supplied HTML string into text
     * @param {string} htmlString
     * @returns {string|any}
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
            builder.field("configjson");
            builder.field("environment");
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
            Search.dots.text(dotString);
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
        this.title = document.getElementById("search-title"); //$('#search-title');
        this.dots = document.getElementById("search-dots"); //$('#search-dots');
        this.status = document.getElementById("search-summary"); //$('#search-summary');
        this.output = document.getElementById("search-results-list"); //$('#search-results-list');

        this.status.text(_('Preparing search...'));
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
        console.log(`query(${query})`);
        /** @type {number} */
        let i;

        // stem the searchterms and add them to the correct list
        const stemmer = new Stemmer();
        /** @type {Array<string>} */
        const searchterms = [];
        /** @type {Array<string>} */
        const excluded = [];
        /** @type {Array<string>} */
        const hlterms = [];
        const tmp = splitQuery(query);
        /** @type {Array<string>} */
        const objectterms = [];
        for (i = 0; i < tmp.length; i++) {
            if (tmp[i] !== "") {
                objectterms.push(tmp[i].toLowerCase());
            }

            if ($u.indexOf(stopwords, tmp[i].toLowerCase()) !== -1 || tmp[i] === "") {
                // skip this "word"
                continue;
            }
            // stem the word
            /** @type {string} */
            let word = stemmer.stemWord(tmp[i].toLowerCase());
            // prevent stemmer from cutting word smaller than two chars
            if (word.length < 3 && tmp[i].length >= 3) {
                word = tmp[i];
            }
            /** @type {Array<string>} */
            let toAppend;
            // select the correct list
            if (word[0] === '-') {
                toAppend = excluded;
                // word = word.substr(1);
                word = word.substring(1);
            } else {
                toAppend = searchterms;
                // Effectively disable highlighting by not collecting any highlight terms
                // Comment the line below to disable highlighting
                hlterms.push(tmp[i].toLowerCase());
            }
            // only add if not already in the list
            if (!$u.contains(toAppend, word))
                toAppend.push(word);
        }

        // Uncomment the line below to enable highlighting
        // var highlightstring = '?highlight=' + $.urlencode(hlterms.join(" "));

        // console.debug('SEARCH: searching for:');
        // console.info('required: ', searchterms);
        // console.info('excluded: ', excluded);

        // prepare search
        const terms = this._index.terms;
        const titleterms = this._index.titleterms;

        /** @type {Array<SearchResult>} */
        let results = [];
        $('#search-summary').empty();

        // Perform a config settings search
        const configSettingSearchResults = this.queryConfigSettings(query);

        // Perform an object search
        /** @type {Record<string, SearchResult>} */
        const uniqueObjectDocs = {}; // A map of the unique document anchors encountered when processing object results
        for (i = 0; i < objectterms.length; i++) {
            /** @type {Array<string>} A list of the search terms not including the current term being searched */
            const others = [].concat(
                objectterms.slice(0, i),
                objectterms.slice(i + 1, objectterms.length)
            );
            const objectResults = this.performObjectSearch(objectterms[i], others);
            // If there were any object results, remove duplicates by favouring the result with the highest score
            if (objectResults.length > 0) {
                /** @type {Record<string, SearchResult>} */
                const filteredObjectResults = {}; // A map of unique object results
                for (const objectResult of objectResults) {
                    const anchor = `${objectResult.docname}#${objectResult.anchor}`;
                    if (anchor in uniqueObjectDocs) {
                        const existingDoc = uniqueObjectDocs[anchor];
                        if (objectResult.score <= existingDoc.score) {
                            // The score of the result we're evaluating is less or equal to the existing result; skip this result
                            continue;
                        }
                        // We've got a result a higher score; remove the existing result with the lower score
                        delete (uniqueObjectDocs[anchor]);
                        delete (filteredObjectResults[anchor]);
                    }
                    // Add this result to the map of unique anchors and the map of filtered results
                    uniqueObjectDocs[anchor] = objectResult;
                    filteredObjectResults[anchor] = objectResult;
                }
                results = results.concat(Object.values(filteredObjectResults));
            }
        }

        // lookup as search terms in fulltext
        results = results.concat(this.performTermsSearch(searchterms, excluded, terms, titleterms));

        // let the scorer override scores with a custom scoring function
        if (Scorer.score) {
            for (i = 0; i < results.length; i++)
                results[i].score = Scorer.score(['', '', '', '', results[i].score]);
        }

        // Remove results that have a duplicate anchor by favouring the result with the higher score.
        // This is fixed differently from Sphinx 5.0.0 onward.
        /** @type {Record<string, SearchResult>} */
        const anchorMap = {};
        /** @type {Array<SearchResult>} */
        const filteredResults = [];
        for (const result of results) {
            // If the anchor is empty, include the result as-is.
            if (result.anchor === "") {
                filteredResults.push(result);
                continue;
            }
            // If we have seen this anchor before, skip this result if it has the same or lower score.
            if (result.anchor in anchorMap) {
                const existingResult = anchorMap[result.anchor];
                if (result.score <= existingResult.score) {
                    continue;
                }
                delete (anchorMap[result.anchor]);
            }
            anchorMap[result.anchor] = result;
        }
        results = filteredResults.concat(Object.values(anchorMap));

        // Sort the results
        results = this.sortSearchResults(results);

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
            this.displayConfigSettingResultItem(configSettingSearchResults[x - 1], hlterms);
        }
        // print the additional information results
        for (let x = results.length; x > 0; x--) {
            this.displayResultItem(results[x - 1], searchterms, hlterms);
        }

        // we're finished searching; stop the visual indicator and display the results summary
        Search.stopPulse();
        Search.title.text(_('Search Results'));
        this.setPostSearchStatus(results.length, configSettingSearchResults.length);
    }

    /**
     * Update the search status field with the results of the search
     * @param {number} numberOfResults
     * @param {number} numberOfConfigSettingResults
     */
    setPostSearchStatus(numberOfResults, numberOfConfigSettingResults) {
        // empty the current status
        Search.status.empty();
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
     * @param {Array<string>} searchterms The terms used in the search
     */
    displayConfigSettingResultItem(item, searchterms) {
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
        for (const searchterm of searchterms) {
            // Only highlight search terms longer than one character
            if (searchterm.length > 1) {
                mark.mark(searchterm);
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
     * @param searchterms {Array<string>}
     * @param hlterms {Array<string>}
     */
    displayResultItem(item, searchterms, hlterms) {
        /** @type {String} */
        let requestUrl;
        /** @type {String} */
        let linkUrl;
        // The result info is displayed as a list item
        const listItem = $('<li/>');
        if (DOCUMENTATION_OPTIONS.BUILDER === 'dirhtml') {
            // dirhtml builder
            let dirname = item.docname + '/';
            if (dirname.match(/\/index\/$/)) {
                dirname = dirname.substring(0, dirname.length - 6);
            } else if (dirname === 'index/') {
                dirname = '';
            }
            requestUrl = DOCUMENTATION_OPTIONS.URL_ROOT + dirname;
            linkUrl = requestUrl;
        } else {
            // normal html builders
            requestUrl = DOCUMENTATION_OPTIONS.URL_ROOT + item.docname + DOCUMENTATION_OPTIONS.FILE_SUFFIX;
            linkUrl = item.docname + DOCUMENTATION_OPTIONS.LINK_SUFFIX;
        }
        // Write the result's link
        // Note: Uncomment the 'highlightstring +' text below to enable highlighting on the linked page
        listItem.append(
            $('<a/>')
                .attr('href', linkUrl + /* highlightstring + */ item.anchor)
                .html(item.title)
        );
        // Write the result's description
        if (item.description !== "") {
            // If the result already includes a description, use it
            listItem.append($('<span> (' + item.description + ')</span>'));
        } else if (DOCUMENTATION_OPTIONS.HAS_SOURCE) {
            // If we're configured to read the source HTML page for a description, do that
            $.ajax({
                url: requestUrl,
                dataType: "text",
                complete: function (jqxhr, textstatus) {
                    const data = jqxhr.responseText;
                    if (data !== '' && data !== undefined) {
                        const summary = Search.makeSearchSummary(data, searchterms, hlterms);
                        if (summary) {
                            listItem.append(summary);
                        }
                    }
                }
            });
        }
        setTimeout(() => {
            $('#search-results-list').append(listItem);
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
     * @param otherterms {Array<string>}
     * @returns {Array<SearchResult>}
     */
    performObjectSearch(object, otherterms) {
        const filenames = this._index.filenames;
        const docnames = this._index.docnames;
        const objects = this._index.objects;
        const objnames = this._index.objnames;
        const titles = this._index.titles;

        /** @type {Array<SearchResult>} */
        const results = [];

        for (const prefix in objects) {
            for (let iMatch = 0; iMatch !== objects[prefix].length; ++iMatch) {
                const match = objects[prefix][iMatch];
                const name = match[4];
                const fullname = (prefix && prefix !== "" ? prefix + '.' : '') + name;
                const fullnameLower = fullname.toLowerCase()
                if (fullnameLower.indexOf(object) > -1) {
                    let score = 0;
                    const parts = fullnameLower.split('.');
                    // check for different match types: exact matches of full name or
                    // "last name" (i.e. last dotted part)
                    if (fullnameLower === object || parts[parts.length - 1] === object) {
                        score += Scorer.objNameMatch;
                        // matches in last name
                    } else if (parts[parts.length - 1].indexOf(object) > -1) {
                        score += Scorer.objPartialMatch;
                    }
                    const objname = objnames[match[1]][2];
                    const title = titles[match[0]];
                    if (title === "") {
                        // If there is no title, it is probably an included doc, and we don't want to show those results
                        continue;
                    }
                    // If more than one term searched for, we require other words to be
                    // found in the name/title/description
                    if (otherterms.length > 0) {
                        const haystack = (prefix + ' ' + name + ' ' + objname + ' ' + title).toLowerCase();
                        let allfound = true;
                        for (let i = 0; i < otherterms.length; i++) {
                            if (haystack.indexOf(otherterms[i]) === -1) {
                                allfound = false;
                                break;
                            }
                        }
                        if (!allfound) {
                            continue;
                        }
                    }
                    // If the object name is 'setting', remove the "setting, " part of the description
                    let descr = objname + _(', in ') + title;
                    if (objname === "setting") {
                        descr = _('in ') + title;
                    }

                    let anchor = match[3];
                    if (anchor === '')
                        anchor = fullname;
                    else if (anchor === '-')
                        anchor = objnames[match[1]][1] + '-' + fullname;
                    // add custom score for some objects according to scorer
                    if (Scorer.objPrio.hasOwnProperty(match[2])) {
                        score += Scorer.objPrio[match[2]];
                    } else {
                        score += Scorer.objPrioDefault;
                    }
                    results.push({
                        docname: docnames[match[0]],
                        title: fullname,
                        anchor: '#' + anchor,
                        description: descr,
                        score,
                        filename: filenames[match[0]],
                        isObject: true,
                    });
                }
            }
        }
        return results;
    }

    /**
     * See https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
     * @param {string} str
     */
    escapeRegExp(str) {
        return str.replace(/[.*+\-?^${}()|[\]\\]/g, '\\$&'); // $& means the whole matched string
    }

    /**
     * search for full-text terms in the index
     * @param {Array<string>} searchterms
     * @param {Array<string>} excluded
     * @param {Record<string,Array<number>>} terms
     * @param {Record<string,Array<number>>} titleterms
     * @returns {Array<SearchResult>}
     */
    performTermsSearch(searchterms, excluded, terms, titleterms) {
        const docnames = this._index.docnames;
        const filenames = this._index.filenames;
        const titles = this._index.titles;

        /** @type {number} */
        let i, j;
        /** @type {(string|Array<string>)} */
        let file;
        /** @type {Record<string,Array<string>>} */
        const fileMap = {};
        /** @type {Record<string,Record<string,number>>} */
        const scoreMap = {};
        /** @type {Array<SearchResult>} */
        const results = [];

        // perform the search on the required terms
        for (i = 0; i < searchterms.length; i++) {
            const word = searchterms[i];
            /** @type {Array<Array<string>>} */
            let files = [];
            /** @type {Array<{files: Array<number>, score: number}>} */
            const _o = [
                {files: terms[word], score: Scorer.term},
                {files: titleterms[word], score: Scorer.title}
            ];
            // add support for partial matches
            if (word.length > 2) {
                const word_regex = this.escapeRegExp(word);
                for (const w in terms) {
                    if (w.match(word_regex) && !terms[word]) {
                        _o.push({files: terms[w], score: Scorer.partialTerm})
                    }
                }
                for (const w in titleterms) {
                    if (w.match(word_regex) && !titleterms[word]) {
                        _o.push({files: titleterms[w], score: Scorer.partialTitle})
                    }
                }
            }

            // no match but word was a required one
            if ($u.every(_o, (o) => {
                return o.files === undefined;
            })) {
                break;
            }
            // found search word in contents
            $u.each(_o, (o) => {
                /** @type {Array<(string|Array<string>)>} */
                let _files = o.files;
                if (_files === undefined)
                    return

                if (_files.length === undefined)
                    _files = [_files];
                files = files.concat(_files);

                // set score for the word in each file to Scorer.term
                for (j = 0; j < _files.length; j++) {
                    file = _files[j];
                    if (!(file in scoreMap))
                        scoreMap[file] = {};
                    scoreMap[file][word] = o.score;
                }
            });

            // create the mapping
            for (j = 0; j < files.length; j++) {
                file = files[j];
                if (file in fileMap && fileMap[file].indexOf(word) === -1)
                    fileMap[file].push(word);
                else
                    fileMap[file] = [word];
            }
        }

        // now check if the files don't contain excluded terms
        for (file in fileMap) {
            let valid = true;

            // check if all requirements are matched
            const filteredTermCount = // as search terms with length < 3 are discarded: ignore
                searchterms.filter((term) => {
                    return term.length > 2;
                }).length;
            if (
                fileMap[file].length !== searchterms.length &&
                fileMap[file].length !== filteredTermCount
            ) continue;

            // ensure that none of the excluded terms is in the search result
            for (i = 0; i < excluded.length; i++) {
                if (terms[excluded[i]] === file ||
                    titleterms[excluded[i]] === file ||
                    $u.contains(terms[excluded[i]] || [], file) ||
                    $u.contains(titleterms[excluded[i]] || [], file)) {
                    valid = false;
                    break;
                }
            }

            // if we have still a valid result we can add it to the result list
            if (valid) {
                // select one (max) score for the file.
                // for better ranking, we should calculate ranking by using words statistics like basic tf-idf...
                /** @type {number} */
                const score = $u.max($u.map(fileMap[file], (w) => {
                    return scoreMap[file][w];
                }));
                results.push({
                    docname: docnames[file],
                    title: titles[file],
                    anchor: '',
                    description: '',
                    score,
                    filename: filenames[file],
                    isObject: false,
                });
            }
        }
        return results;
    }

    /**
     * helper function to return a node containing the search summary for a given text.
     *
     * @param {string} htmlText The text to summarize
     * @param {Array<string>} keywords a list of stemmed words; used to find occurrence of the word in the summary
     * @param {Array<string>} hlwords the list of normal, unstemmed words; used to highlight the stemmed word
     * @returns {(jQuery|null)}
     */
    makeSearchSummary(htmlText, keywords, hlwords) {
        const text = this.htmlToText(htmlText);
        if (text === "") {
            return null;
        }
        /** @type {string} */
        let excerpt;
        if (this._useDefaultSearchSummary) {
            /*
             * Default Sphinx search result summary
             */
            const textLower = text.toLowerCase();
            let start = 0;
            $.each(keywords, () => {
                const i = textLower.indexOf(this.toLowerCase());
                if (i > -1)
                    start = i;
            });
            const halfLength = this._summaryTextLength / 2;
            start = Math.max(start - halfLength, 0);
            excerpt = ((start > 0) ? '...' : '') +
                $.trim(text.substr(start, this._summaryTextLength)) +
                ((start + this._summaryTextLength - text.length) ? '...' : '');
        } else {
            /*
             * Search result summary using the first x number of characters
             */
            excerpt = $.trim(text.substr(0, this._summaryTextLength)) +
                (text.length > this._summaryTextLength ? '...' : '');
        }
        // build the search summary node
        let rv = $('<p class="context"></p>').text(excerpt);
        for (const hlword of hlwords) {
            // Only highlight words longer than one character
            if (hlword.length > 1) {
                rv = rv.highlightText(hlword, 'highlighted');
            }
        }
        return rv;
    }

}

const Search = new SearchClass();

_ready(Search.init);
