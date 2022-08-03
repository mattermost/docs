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
 * @property {Record<String,Number>} objPrio
 * @property {number} objPrioDefault
 * @property {number} title
 * @property {number} partialTitle
 * @property {number} term
 * @property {number} partialTerm
 */

if (!Scorer) {
    /**
     * Simple result scoring code.
     * @type {ScorerObject}
     */
    var Scorer = {
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
        objPrio: {0:  15,   // used to be importantResults
            1:  5,   // used to be objectResults
            2: -5},  // used to be unimportantResults
        //  Used when the priority is not in the mapping.
        objPrioDefault: 0,

        // query found in title
        title: 15,
        partialTitle: 7,
        // query found in terms
        term: 5,
        partialTerm: 2
    };
}

/* Define the splitQuery function if it has not been defined */
if (!splitQuery) {
    /**
     * Splits a query string into words
     * @param query {String} The query string to split
     * @returns {String[]} The array of split query tokens
     */
    function splitQuery(query) {
        return query.split(/\s+/);
    }
}

/* JSDoc type definition for search index */
/**
 * @typedef SearchIndex
 * @type {object|null}
 * @property {Array<String>} docnames
 * @property {Record<String,Number>} envversion
 * @property {Array<String>} filenames
 * @property {Record<String, Array<Array<String>>>} objects
 * @property {Record<String,Array<String>>} objnames
 * @property {Record<String,Array<String>>} objtypes
 * @property {Record<String,Array<Number>>} terms
 * @property {Array<String>} titles
 * @property {Record<String,Array<Number>>} titleterms
 */

/**
 * Search Module
 */
var Search = {
    /**
     * The length of text to use for the summary of each search result. If the summary text
     * is longer than this length, an ellipsis (...) will be appended.
     * The Sphinx default value is 240.
     */
    _summaryTextLength : 300,
    /**
     * Use the default Sphinx search summary generator instead of using the first x characters
     * of the summary text.
     */
    _useDefaultSearchSummary : false,

    /** @type {SearchIndex|null} */
    _index : null,
    /** @type {String|null} */
    _queued_query : null,
    /** @type {Number} */
    _pulse_status : -1,

    /**
     * Convert the supplied HTML string into text
     * @param {String} htmlString
     * @returns {string|*}
     */
    htmlToText : function(htmlString) {
        /** @type {Document} */
        var virtualDocument = document.implementation.createHTMLDocument('virtual');
        /** @type {jQuery} */
        var htmlElement = $(htmlString, virtualDocument);
        htmlElement.find('.headerlink').remove();
        const docContent = htmlElement.find('[role=main]')[0];
        if (docContent === undefined) {
            console.warn("Content block not found. Sphinx search tries to obtain it " +
                "via '[role=main]'. Could you check your theme or template.");
            return "";
        }
        return docContent.textContent || docContent.innerText;
    },

    init : function() {
        var params = $.getQueryParameters();
        if (params.q) {
            var query = params.q[0];
            $('input[name="q"]')[0].value = query;
            this.performSearch(query);
        }
    },

    /**
     * Load the search index data from the specified URL
     * @param url {String} The URL to load search index data from
     */
    loadIndex : function(url) {
        $.ajax({type: "GET", url: url, data: null,
            dataType: "script", cache: true,
            complete: function(jqxhr, textstatus) {
                if (textstatus !== "success") {
                    document.getElementById("searchindexloader").src = url;
                }
            }});
    },

    /**
     * Set search index data and perform a search if a queued query exists
     * @param index {SearchIndex}
     */
    setIndex : function(index) {
        /** @type {String} */
        var q;
        this._index = index;
        if ((q = this._queued_query) !== null) {
            this._queued_query = null;
            Search.query(q);
        }
    },

    hasIndex : function() {
        return this._index !== null;
    },

    /**
     * Queue a query to run at a later time
     * @param query {String} The query to queue
     */
    deferQuery : function(query) {
        this._queued_query = query;
    },

    stopPulse : function() {
        this._pulse_status = 0;
    },

    startPulse : function() {
        if (this._pulse_status >= 0)
            return;
        function pulse() {
            var i;
            Search._pulse_status = (Search._pulse_status + 1) % 4;
            var dotString = '';
            for (i = 0; i < Search._pulse_status; i++)
                dotString += '.';
            Search.dots.text(dotString);
            if (Search._pulse_status > -1)
                window.setTimeout(pulse, 500);
        }
        pulse();
    },

    /**
     * perform a search for something (or wait until index is loaded)
     * @param query {String} The search query to perform
     */
    performSearch : function(query) {
        // create the required interface elements
        this.out = $('#search-results');
        this.title = $('<h2>' + _('Searching') + '</h2>').appendTo(this.out);
        this.dots = $('<span></span>').appendTo(this.title);
        this.status = $('<p class="search-summary">&nbsp;</p>').appendTo(this.out);
        this.output = $('<ul class="search"/>').appendTo(this.out);

        $('#search-progress').text(_('Preparing search...'));
        this.startPulse();

        // index already loaded, the browser was quick!
        if (this.hasIndex())
            this.query(query);
        else
            this.deferQuery(query);
    },

    /**
     * execute search (requires search index to be loaded)
     * @param query {String} The search query to perform
     */
    query : function(query) {
        /** @type {Number} */
        var i;

        // stem the searchterms and add them to the correct list
        var stemmer = new Stemmer();
        /** @type {String[]} */
        var searchterms = [];
        /** @type {String[]} */
        var excluded = [];
        /** @type {String[]} */
        var hlterms = [];
        var tmp = splitQuery(query);
        /** @type {String[]} */
        var objectterms = [];
        for (i = 0; i < tmp.length; i++) {
            if (tmp[i] !== "") {
                objectterms.push(tmp[i].toLowerCase());
            }

            if ($u.indexOf(stopwords, tmp[i].toLowerCase()) !== -1 || tmp[i] === "") {
                // skip this "word"
                continue;
            }
            // stem the word
            /** @type {String} */
            var word = stemmer.stemWord(tmp[i].toLowerCase());
            // prevent stemmer from cutting word smaller than two chars
            if (word.length < 3 && tmp[i].length >= 3) {
                word = tmp[i];
            }
            /** @type {String[]} */
            var toAppend;
            // select the correct list
            if (word[0] === '-') {
                toAppend = excluded;
                word = word.substr(1);
            }
            else {
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
        var terms = this._index.terms;
        var titleterms = this._index.titleterms;

        // array of [filename, title, anchor, descr, score]
        /** @type {Array<Array<String|Number>>} */
        var results = [];
        $('#search-progress').empty();

        // lookup as object
        for (i = 0; i < objectterms.length; i++) {
            /** @type {String[]} */
            var others = [].concat(objectterms.slice(0, i),
                objectterms.slice(i+1, objectterms.length));
            results = results.concat(this.performObjectSearch(objectterms[i], others));
        }

        // lookup as search terms in fulltext
        results = results.concat(this.performTermsSearch(searchterms, excluded, terms, titleterms));

        // let the scorer override scores with a custom scoring function
        if (Scorer.score) {
            for (i = 0; i < results.length; i++)
                results[i][4] = Scorer.score(results[i]);
        }

        // now sort the results by score (in opposite order of appearance, since the
        // display function below uses pop() to retrieve items) and then
        // alphabetically
        results.sort(function(a, b) {
            /** @type {String|Number} */
            var left = a[4];
            /** @type {String|Number} */
            var right = b[4];
            if (left > right) {
                return 1;
            } else if (left < right) {
                return -1;
            } else {
                // same score: sort alphabetically
                left = a[1].toLowerCase();
                right = b[1].toLowerCase();
                return (left > right) ? -1 : ((left < right) ? 1 : 0);
            }
        });

        // for debugging
        //Search.lastresults = results.slice();  // a copy
        //console.info('search results:', Search.lastresults);

        // print the results
        var resultCount = results.length;
        function displayNextItem() {
            // results left, load the summary and display it
            if (results.length) {
                var item = results.pop();
                var listItem = $('<li></li>');
                /** @type {String} */
                var requestUrl;
                /** @type {String} */
                var linkUrl;
                if (DOCUMENTATION_OPTIONS.BUILDER === 'dirhtml') {
                    // dirhtml builder
                    var dirname = item[0] + '/';
                    if (dirname.match(/\/index\/$/)) {
                        dirname = dirname.substring(0, dirname.length-6);
                    } else if (dirname === 'index/') {
                        dirname = '';
                    }
                    requestUrl = DOCUMENTATION_OPTIONS.URL_ROOT + dirname;
                    linkUrl = requestUrl;
                } else {
                    // normal html builders
                    requestUrl = DOCUMENTATION_OPTIONS.URL_ROOT + item[0] + DOCUMENTATION_OPTIONS.FILE_SUFFIX;
                    linkUrl = item[0] + DOCUMENTATION_OPTIONS.LINK_SUFFIX;
                }

                // Uncomment the 'highlightstring' text below to enable highlighting on the linked page
                listItem.append($('<a/>').attr('href',
                    linkUrl +
                    /* highlightstring + */ item[2]).html(item[1]));

                if (item[3]) {
                    listItem.append($('<span> (' + item[3] + ')</span>'));
                    Search.output.append(listItem);
                    setTimeout(function() {
                        displayNextItem();
                    }, 5);
                } else if (DOCUMENTATION_OPTIONS.HAS_SOURCE) {
                    $.ajax({url: requestUrl,
                        dataType: "text",
                        complete: function(jqxhr, textstatus) {
                            var data = jqxhr.responseText;
                            if (data !== '' && data !== undefined) {
                                var summary = Search.makeSearchSummary(data, searchterms, hlterms);
                                if (summary) {
                                    listItem.append(summary);
                                }
                            }
                            Search.output.append(listItem);
                            setTimeout(function() {
                                displayNextItem();
                            }, 5);
                        }});
                } else {
                    // no source available, just display title
                    Search.output.append(listItem);
                    setTimeout(function() {
                        displayNextItem();
                    }, 5);
                }
            }
            // search finished, update title and status message
            else {
                Search.stopPulse();
                Search.title.text(_('Search Results'));
                if (!resultCount)
                    Search.status.text(_('Your search did not match any documents. Please make sure that all words are spelled correctly and that you\'ve selected enough categories.'));
                else
                    Search.status.text(_('Search finished, found %s page(s) matching the search query.').replace('%s', resultCount));
                Search.status.fadeIn(500);
            }
        }
        displayNextItem();
    },

    /**
     * search for object names
     * @param object {String}
     * @param otherterms {String[]}
     * @returns {Array<Array<String|Number>>}
     */
    performObjectSearch : function(object, otherterms) {
        var filenames = this._index.filenames;
        var docnames = this._index.docnames;
        var objects = this._index.objects;
        var objnames = this._index.objnames;
        var titles = this._index.titles;

        /** @type {Number} */
        var i;
        /** @type {Array<Array<String|Number>>} */
        var results = [];

        for (var prefix in objects) {
            for (var iMatch = 0; iMatch !== objects[prefix].length; ++iMatch) {
                var match = objects[prefix][iMatch];
                var name = match[4];
                var fullname = (prefix ? prefix + '.' : '') + name;
                var fullnameLower = fullname.toLowerCase()
                if (fullnameLower.indexOf(object) > -1) {
                    var score = 0;
                    var parts = fullnameLower.split('.');
                    // check for different match types: exact matches of full name or
                    // "last name" (i.e. last dotted part)
                    if (fullnameLower === object || parts[parts.length - 1] === object) {
                        score += Scorer.objNameMatch;
                        // matches in last name
                    } else if (parts[parts.length - 1].indexOf(object) > -1) {
                        score += Scorer.objPartialMatch;
                    }
                    var objname = objnames[match[1]][2];
                    var title = titles[match[0]];
                    // If more than one term searched for, we require other words to be
                    // found in the name/title/description
                    if (otherterms.length > 0) {
                        var haystack = (prefix + ' ' + name + ' ' +
                            objname + ' ' + title).toLowerCase();
                        var allfound = true;
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
                    var descr = objname + _(', in ') + title;

                    var anchor = match[3];
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
                        '#'+anchor,
                        descr,
                        score,
                        filenames[match[0]]
                    ]);
                }
            }
        }

        return results;
    },

    /**
     * See https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions
     * @param {String} string
     */
    escapeRegExp : function(string) {
        return string.replace(/[.*+\-?^${}()|[\]\\]/g, '\\$&'); // $& means the whole matched string
    },

    /**
     * search for full-text terms in the index
     * @param {Array<String>} searchterms
     * @param {Array<String>} excluded
     * @param {Record<String,Array<Number>>} terms
     * @param {Record<String,Array<Number>>} titleterms
     * @returns {Array<Array<(String|Number|null)>>}
     */
    performTermsSearch : function(searchterms, excluded, terms, titleterms) {
        var docnames = this._index.docnames;
        var filenames = this._index.filenames;
        var titles = this._index.titles;

        /** @type {Number} */
        var i, j;
        /** @type {(String|Array<String>)} */
        var file;
        /** @type {Record<String,Array<String>>} */
        var fileMap = {};
        /** @type {Record<String,Record<String,Number>>} */
        var scoreMap = {};
        /** @type {Array<Array<(String|Number|null)>>} */
        var results = [];

        // perform the search on the required terms
        for (i = 0; i < searchterms.length; i++) {
            var word = searchterms[i];
            /** @type {Array<Array<String>>} */
            var files = [];
            /** @type {Array<{files: Array<Number>, score: Number}>} */
            var _o = [
                {files: terms[word], score: Scorer.term},
                {files: titleterms[word], score: Scorer.title}
            ];
            // add support for partial matches
            if (word.length > 2) {
                var word_regex = this.escapeRegExp(word);
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
            if ($u.every(_o, function(o){return o.files === undefined;})) {
                break;
            }
            // found search word in contents
            $u.each(_o, function(o) {
                /** @type {Array<(String|Array<String>)>} */
                var _files = o.files;
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
            var valid = true;

            // check if all requirements are matched
            var filteredTermCount = // as search terms with length < 3 are discarded: ignore
                searchterms.filter(function(term){return term.length > 2}).length
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
                /** @type {Number} */
                var score = $u.max($u.map(fileMap[file], function(w){return scoreMap[file][w]}));
                results.push([docnames[file], titles[file], '', null, score, filenames[file]]);
            }
        }
        return results;
    },

    /**
     * helper function to return a node containing the search summary for a given text.
     *
     * @param {String} htmlText The text to summarize
     * @param {Array<String>} keywords a list of stemmed words; used to find occurrence of the word in the summary
     * @param {Array<String>} hlwords the list of normal, unstemmed words; used to highlight the stemmed word
     * @returns {(jQuery|null)}
     */
    makeSearchSummary : function(htmlText, keywords, hlwords) {
        var text = Search.htmlToText(htmlText);
        if (text === "") {
            return null;
        }
        /** @type {String} */
        var excerpt;
        if (this._useDefaultSearchSummary) {
            /*
             * Default Sphinx search result summary
             */
            var textLower = text.toLowerCase();
            var start = 0;
            $.each(keywords, function() {
                var i = textLower.indexOf(this.toLowerCase());
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
        var rv = $('<p class="context"></p>').text(excerpt);
        $.each(hlwords, function() {
            rv = rv.highlightText(this, 'highlighted');
        });
        return rv;
    }
};

$(document).ready(function() {
    Search.init();
});
