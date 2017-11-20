End-to-end Testing
==================

This page describes how to run End-to-End (E2E) testing and build tests to a section or page of Mattermost web application.

Under the Hood
--------------

The E2E testing usually run against `Selenium <http://www.seleniumhq.org/>`__ and for ease of use, we are writing a test based on `Nightwatch.js <http://nightwatchjs.org/>`__ which is an easy to use Node.js based E2E testing solution for browser based apps and websites. It uses the powerful W3C WebDriver API to perform commands and assertions on DOM elements. To get started in writing an E2E tests, checkout Nightwatch.js documentation, specifically:

- `Developer Guide <http://nightwatchjs.org/guide//>`__, and
- `API Reference <http://nightwatchjs.org/api//>`__.

Quick Overview of Running E2E Testing
-------------------------------------

1. Run a local Mattermost instance by initiating ``make run`` to `mattermost-server` folder. Confirm that the instance has successfully started.
2. Change directory to `mattermost-webapp` and run ``yarn run test:e2e``. This will start full E2E testing. To run partial testing, select specific tag and initiate ``yarn run test:e2e tagname`` (e.g. ``yarn run test:e2e login``).
3. Full testing will control both Chrome and Firefox browsers, while partial testing will be in Chrome only.
4. Observe that the tests are executed accordingly and will have final outcome either pass or with failing results.

Folder Structures
----------------------

E2E tests files are located at `mattermost-webapp/tests/e2e`. It includes utility and actual tests. Usually, you will be writing in the following folders:

- `/pages`: 
    a. Files are named with a prefix of `Page.js` which contains `Page Objects <https://martinfowler.com/bliki/PageObject.html/>`__.
    b. Each file typically consists of `commands`, `url`, `section`, `elements` and `selector`.
    c. Selector can be CSS or XPath locate strategies but for convenience and readability, the default CSS selector is used with corresponding elements IDs.

- `/tests`: 
    a. Files are named with a prefix of `.element.js` (which contains assertions to elements' presence) and `.action.js` (which contains assertions to element/s given an action).
    b. Files are group into separate folders depending on their purpose or similarity.

Writing an E2E testing
----------------------

1. After you've written a feature, plugin or a bug fix, assess whether it requires E2E testing.
2. Identify its DOM structure by inspecting elements.
3. See to it that all relevant elements for assertion are assigned with element IDs.
4. Under `/pages` folder, review existing files whether the DOM structure has already an existing Page Object.
    - If none yet, add a new file containing the Page Object.
    - If exists, then update the corresponding page file accordingly.
5. Under `tests` folder, review existing files whether there exists related tag or test.
    - If none yet, add a new test file both for elements and actions assertions.
    - If exists, then update the corresponding test file accordingly.
6. Initiate E2E test commands, preferably with tags or partial testing for quick iteration and then full testing for final observation.
