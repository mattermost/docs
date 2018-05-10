End-to-end Testing
==================

This page describes how to run End-to-End (E2E) testing and build tests for a section or page of the Mattermost web application.

Under the Hood
--------------

The E2E testing is usually run against `Selenium <http://www.seleniumhq.org/>`__ and, for ease of use, tests are written in `Nightwatch.js <http://nightwatchjs.org/>`__ which is an easy to use Node.js based E2E testing solution for browser based apps and websites. It uses the powerful W3C WebDriver API to perform commands and assertions on DOM elements. To get started, see the Nightwatch.js documentation, specifically:

- `Developer Guide <http://nightwatchjs.org/guide//>`__, and
- `API Reference <http://nightwatchjs.org/api//>`__.

Quick Overview of Running E2E Testing
-------------------------------------

1. Run a local Mattermost instance by initiating ``make run`` to the `mattermost-server` folder. Confirm that the instance has started successfully.
2. Change directory to `mattermost-webapp` and run ``npm run test:e2e``. This will start full E2E testing. To run partial testing, select a specific tag and initiate ``npm run test:e2e tagname`` (e.g. ``npm run test:e2e login``).
3. Full testing makes use of both Chrome and Firefox browsers, while partial testing uses Chrome only.
4. Tests are executed according to your selection and will display whether the tests passed or failed.

Folder Structures
----------------------

E2E tests files are located at `mattermost-webapp/tests/e2e`. This folder includes utility and actual tests. Usually, you will be writing tests in the following folders:

- `/pages`: 
    a. Files are named with a prefix of `Page.js` which contain `Page Objects <https://martinfowler.com/bliki/PageObject.html/>`__.
    b. Each file typically consists of `commands`, `url`, `section`, `elements` and `selector`.
    c. Selector can be either CSS or XPath locate strategies but, for convenience and readability, the default CSS selector is used with corresponding element IDs.

- `/tests`: 
    a. Files are named with a prefix of `.element.js` (which contains assertions to the element's presence) and `.action.js` (which contains assertions to the element/s given an action).
    b. Files are group into separate folders depending on their purpose or similarity.

Writing an E2E test
-------------------

1. After you've written a feature, plugin or bug fix, assess whether it requires E2E testing.
2. Identify its DOM structure by inspecting elements.
3. Ensure that all relevant elements for assertion are assigned with element IDs.
4. Under `/pages` folder, review existing files to check whether the DOM structure already has an existing Page Object.

    - If no file exists, add a new one containing the Page Object.
    - If a file does exist, then update the corresponding page file accordingly.
5. Under `tests` folder, review existing files to check whether a related tag or test already exists.

    - If no file exists, add a new test file for both elements and action assertions.
    - If a file does exist, then update the corresponding test file accordingly.
6. Initiate E2E test commands, preferably with tags or partial testing for quick iteration and then full testing for final observation.
