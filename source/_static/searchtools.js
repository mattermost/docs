/*
 * searchtools.js
 * ~~~~~~~~~~~~~~~~
 *
 * Sphinx JavaScript utilities for the full-text search.
 *
 * :copyright: Copyright 2007-2022 by the Sphinx team, see AUTHORS.
 * :license: BSD, see LICENSE for details.
 *
 */

/*
NOTE:
This file is specific to Sphinx v4.4.0. If the version of Sphinx used to build
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
 * @property {Array<string>} docnames
 * @property {Record<string,number>} envversion
 * @property {Array<string>} filenames
 * @property {Record<string, Array<Array<string>>>} objects
 * @property {Record<string,Array<string>>} objnames
 * @property {Record<string,Array<string>>} objtypes
 * @property {Record<string,Array<number>>} terms
 * @property {Array<string>} titles
 * @property {Record<string,Array<number>>} titleterms
 */

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
    /** @type {(SearchIndex|null)} */
    _index = null;
    /** @type {(string|null)} */
    _queued_query = null;
    /** @type {number} */
    _pulse_status = -1;

    constructor() {
    }

    init() {
        const params = $.getQueryParameters();
        if (params.q) {
            const query = params.q[0];
            $('input[name="q"]')[0].value = query;
            this.performSearch(query);
        }
    }

    /**
     * Convert the supplied HTML string into text
     * @param {string} htmlString
     * @returns {string|any}
     */
    htmlToText(htmlString) {
        /** @type {Document} */
        const virtualDocument = document.implementation.createHTMLDocument('virtual');
        /** @type {jQuery} */
        const htmlElement = $(htmlString, virtualDocument);
        htmlElement.find('.headerlink').remove();
        const docContent = htmlElement.find('[role=main]')[0];
        if (docContent === undefined) {
            console.warn("Content block not found. Sphinx search tries to obtain it " +
                "via '[role=main]'. Could you check your theme or template.");
            return "";
        }
        return docContent.textContent || docContent.innerText;
    }

    /**
     * Load the search index data from the specified URL
     * @param url {string} The URL to load search index data from
     */
    loadIndex(url) {
        $.ajax({
            type: "GET", url: url, data: null,
            dataType: "script", cache: true,
            complete: function (jqxhr, textstatus) {
                if (textstatus !== "success") {
                    document.getElementById("searchindexloader").src = url;
                }
            }
        });
    }

    /**
     * Set search index data and perform a search if a queued query exists
     * @param index {SearchIndex}
     */
    setIndex(index) {
        /** @type {string} */
        let q;
        this._index = index;
        if ((q = this._queued_query) !== null) {
            this._queued_query = null;
            this.query(q);
        }
    }

    hasIndex() {
        return this._index !== null;
    }

    /**
     * Queue a query to run at a later time
     * @param query {string} The query to queue
     */
    deferQuery(query) {
        this._queued_query = query;
    }

    stopPulse() {
        console.log("*** stopping pulse")
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
        console.log("*** starting pulse");
        pulse();
    }

    /**
     * perform a search for something (or wait until index is loaded)
     * @param query {string} The search query to perform
     */
    performSearch(query) {
        // create the required interface elements
        this.out = $('#search-results');
        this.title = $('#search-title');
        this.dots = $('#search-dots');
        this.status = $('#search-summary');
        this.output = $('#search-results-list');

        // $('#search-progress').text(_('Preparing search...'));
        this.status.text(_('Preparing search...'));
        this.startPulse();

        // index already loaded, the browser was quick!
        if (this.hasIndex())
            this.query(query);
        else
            this.deferQuery(query);
    }

    /**
     * execute search (requires search index to be loaded)
     * @param query {string} The search query to perform
     */
    query(query) {
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

        // array of [filename, title, anchor, descr, score]
        /** @type {Array<Array<string|number>>} */
        let results = [];
        $('#search-summary').empty();

        // lookup as object
        let foundObjectResults = false;
        for (i = 0; i < objectterms.length; i++) {
            /** @type {Array<string>} */
            const others = [].concat(objectterms.slice(0, i),
                objectterms.slice(i + 1, objectterms.length));
            const objectResults = this.performObjectSearch(objectterms[i], others);
            // console.log(`+++ objectResults=${JSON.stringify(objectResults)}`);
            if (objectResults.length > 0) {
                foundObjectResults = true;
            }
            results = results.concat(objectResults);
        }
        // console.log(`+++ foundObjectResults=${foundObjectResults}`);

        // lookup as search terms in fulltext
        results = results.concat(this.performTermsSearch(searchterms, excluded, terms, titleterms));

        // let the scorer override scores with a custom scoring function
        if (Scorer.score) {
            for (i = 0; i < results.length; i++)
                results[i][4] = Scorer.score(results[i]);
        }

        // Remove results that have a duplicate anchor. This is fixed differently from Sphinx 5.0.0 onward.
        /** @type {Record<string, boolean>} */
        const anchorMap = {};
        /** @type {Array<Array<(string|number)>>} */
        const filteredResults = [];
        for (const result of results) {
            // If the anchor is empty, include the result as-is.
            if (result[2] === "") {
                filteredResults.push(result);
                continue;
            }
            // If we have seen this anchor before, skip this result.
            if (result[2] in anchorMap) {
                continue;
            }
            anchorMap[result[2]] = true
            filteredResults.push(result)
        }
        results = filteredResults;

        // sort results into buckets by score
        /** @type {Record<number, Array<Array<(string|number)>>>} */
        const resultsByScore = {}
        for (const result of results) {
            if (result[4] in resultsByScore) {
                resultsByScore[Number(result[4])].push(result);
            } else {
                resultsByScore[Number(result[4])] = [result];
            }
        }
        // sort the bucket keys numerically, highest to lowest
        const rbsKeys = Object.keys(resultsByScore).sort((a, b) => {
            const left = Number(a);
            const right = Number(b);
            return (left > right) ? 1 : ((left < right) ? -1 : 0);
        });
        // add each bucket of results to the final array of results
        /** @type {Array<Array<(string|number)>>} */
        const sortedResults = [];
        for (const rbsKey of rbsKeys) {
            // sort the results in each bucket alphabetically by title
            const sorted = resultsByScore[rbsKey].sort((a, b) => {
                const left = String(a[1]).toLowerCase();
                const right = String(b[1]).toLowerCase();
                return (left > right) ? -1 : ((left < right) ? 1 : 0);
            });
            sortedResults.push(...sorted);
        }
        results = sortedResults;
        // debug
        // for (let x = 0; x < results.length; x++) {
        //     const result = results[x];
        //     // array of [filename, title, anchor, descr, score]
        //     console.log(
        //         `results[${x}]: doc=${result[0]}, title=${result[1]}, anchor=${result[2]}, score=${result[4]}, desc=${result[3]}`
        //     );
        // }

        // If we found object results, show the config settings div; otherwise hide it
        const displaySetting = foundObjectResults ? "contents" : "none";
        const configSettingsDiv = document.getElementById("config-setting-results-section");
        if (configSettingsDiv != null) {
            configSettingsDiv.setAttribute("style", "display: " + displaySetting + ";");
        }
        const additionalInfoDiv = document.getElementById("search-additional-information-header");
        if (additionalInfoDiv != null) {
            additionalInfoDiv.setAttribute("style", "display: " + displaySetting + ";");
        }

        // print the results
        for (let x = results.length; x > 0; x--) {
            const item = results[x-1];
            this.displayResultItem(item, searchterms, hlterms);
        }
        // we're finished searching; stop the visual indicator and display the results summary
        Search.stopPulse();
        Search.title.text(_('Search Results'));
        if (results.length === 0)
            Search.status.text(_('Your search did not match any documents. Please make sure that all words are spelled correctly and that you\'ve selected enough categories.'));
        else
            Search.status.text(_('Search finished, found %s page(s) matching the search query.').replace('%s', results.length));
    }

    /**
     * Display a single search result
     * @param item {Array<(string|number)>}
     * @param searchterms {Array<string>}
     * @param hlterms {Array<string>}
     */
    displayResultItem(item, searchterms, hlterms) {
        // Destructure each result into its fields; array of [0 - filename, 1 - title, 2 - anchor, 3 - descr, 4 - score]
        const [iFilename, iTitle, iAnchor, iDescr, iScore] = item;
        const isObject = (iScore === 26 || iScore === 21);
        const listItem = $('<li/>'); // The result info is displayed as a list item
        // Append the result's score
        listItem.append($("<span/>").html("[" + iScore + "]&nbsp;"));
        /** @type {String} */
        let requestUrl;
        /** @type {String} */
        let linkUrl;
        if (DOCUMENTATION_OPTIONS.BUILDER === 'dirhtml') {
            // dirhtml builder
            let dirname = iFilename + '/';
            if (dirname.match(/\/index\/$/)) {
                dirname = dirname.substring(0, dirname.length - 6);
            } else if (dirname === 'index/') {
                dirname = '';
            }
            requestUrl = DOCUMENTATION_OPTIONS.URL_ROOT + dirname;
            linkUrl = requestUrl;
        } else {
            // normal html builders
            requestUrl = DOCUMENTATION_OPTIONS.URL_ROOT + iFilename + DOCUMENTATION_OPTIONS.FILE_SUFFIX;
            linkUrl = iFilename + DOCUMENTATION_OPTIONS.LINK_SUFFIX;
        }
        // Write the result's link
        // Note: Uncomment the 'highlightstring +' text below to enable highlighting on the linked page
        listItem.append(
            $('<a/>')
                .attr('href', linkUrl + /* highlightstring + */ iAnchor)
                .html(iTitle)
        );
        // Write the result's description
        if (iDescr) {
            // If the result already includes a description, use it
            listItem.append($('<span> (' + iDescr + ')</span>'));
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
        const appendList = isObject ? $('#config-setting-results-list') : $('#search-results-list');
        setTimeout(() => {
           appendList.append(listItem);
        }, 5);
    }

    /**
     * search for object names
     * @param object {string}
     * @param otherterms {Array<string>}
     * @returns {Array<Array<string|number>>}
     */
    performObjectSearch(object, otherterms) {
        const filenames = this._index.filenames;
        const docnames = this._index.docnames;
        const objects = this._index.objects;
        const objnames = this._index.objnames;
        const titles = this._index.titles;

        /** @type {number} */
        let i;
        /** @type {Array<Array<string|number>>} */
        const results = [];

        for (const prefix in objects) {
            for (let iMatch = 0; iMatch !== objects[prefix].length; ++iMatch) {
                const match = objects[prefix][iMatch];
                const name = match[4];
                const fullname = (prefix ? prefix + '.' : '') + name;
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
                        for (i = 0; i < otherterms.length; i++) {
                            if (haystack.indexOf(otherterms[i]) === -1) {
                                allfound = false;
                                break;
                            }
                        }
                        if (!allfound) {
                            continue;
                        }
                    }
                    const descr = objname + _(', in ') + title;

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
                    results.push([
                        docnames[match[0]],
                        fullname,
                        '#' + anchor,
                        descr,
                        score,
                        filenames[match[0]]
                    ]);
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
     * @returns {Array<Array<(string|number|null)>>}
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
        /** @type {Array<Array<(string|number|null)>>} */
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
                results.push([docnames[file], titles[file], '', null, score, filenames[file]]);
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
        $.each(hlwords, () => {
            rv = rv.highlightText(this, 'highlighted');
        });
        return rv;
    }

}

/**
 * Search module
 * @type {SearchClass}
 */
const Search = new SearchClass();

$(document).ready(() => {
    Search.init();
});
