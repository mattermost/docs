Import your data
================

Import from Asana
-----------------

This node app converts an Asana json archive into a Focalboard archive. To use:

    From the Asana Board Menu, select Export / Print, and JSON
    Save it locally, e.g. to asana.json
    Run npm install from within focalboard/webapp
    Run npm install from within focalboard/import/asana
    Run npx ts-node importAsana.ts -i <asana.json> -o archive.focalboard
    In Focalboard, click Settings, then Import archive and select archive.focalboard

Import scope
^^^^^^^^^^^^

Currently, the script imports all cards from a single board, including their section (column) membership, names, and notes. Contribute code to expand this.

Import from Notion
------------------

This node app converts a Notion CSV and markdown export into a Focalboard archive. To use:

1. From a Notion Board, open the ... menu at the top right
2. Select `Export` and pick `Markdown & CSV` as the export format
3. Save it locally, and unzip the folder e.g. to `notion-export`
4. Run `npm install` from within `focalboard/webapp`
5. Run `npm install` from within `focalboard/import/notion`
6. Run `npx ts-node importNotion.ts -i <path to the notion-export folder> -o archive.focalboard`
7. In Focalboard, click `Settings`, then `Import archive` and select `archive.focalboard`

Import scope
^^^^^^^^^^^^

Currently, the script imports all cards from a single board, including their properties and markdown content.

The Notion export format does not preserve property types, so the script currently imports all card properties as a Select type. You can change the type after importing into Focalboard.

[Contribute code](https://www.focalboard.com/contribute/getting-started/) to expand this.


Import from Jira
----------------

This node app converts a Jira xml export into a Focalboard archive. To use:
1. Open Jira advanced search, and search for all the items to export
2. Select ``Export``, then ``Export XML``
3. Save it locally, e.g. to ``jira_export.xml``
4. Run ``npm install`` from within ``focalboard/webapp``
5. Run ``npm install`` from within ``focalboard/import/jira``
6. Run ``npx ts-node importJira.ts -i <path-to-jira.xml> -o archive.focalboard`` (also from within `focalboard/import/jira`)
7. In Focalboard, click ``Settings``, then `Import archive` and select ``archive.focalboard``

Import scope and known limitations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently, the script imports each item as a card into a single board. Note that Jira XML export is limited to 1000 issues at a time.

Users are imported as Select properties, with the name of the user.

The following aren't currently imported:
* Custom properties
* Comments
* Embedded files

Import from Trello
------------------

This node app converts a Trello json archive into a Focalboard archive. To use:
1. From the Trello Board Menu, ``...Show Menu`` on right
2. Select ``More``, then ``Print and Export``, and ``Export to JSON``
3. Save it locally, e.g. to ``trello.json``
4. Run ``npm install`` from within `focalboard/webapp`
5. Run ``npm install`` from within `focalboard/import/trello`
6. Run ``npx ts-node importTrello.ts -i <path-to-trello.json> -o archive.focalboard`` (also from within ``focalboard/import/trello``)
7. In Focalboard, click ``Settings``, then ``Import archive`` and select ``archive.focalboard``

Import scope
^^^^^^^^^^^^

Currently, the script imports all cards from a single board, including their list (column) membership, names, and descriptions.

Import from Todoist
-------------------

This node app converts a Todoist json archive into a Focalboard archive. To use:
1. Visit the open source Todoist data export service at https://darekkay.com/todoist-export/.
1. Select ``JSON (all data)`` in **Export As** option.
1. Uncheck the **Archived** option if checked.
1. Click on **Authorize and Backup**. This wil take you to your Todoist account. Follow the instructions on screen.
1. Note the name and location of the downloaded *json* file.
3. Run ``npm install`` from within ``focalboard/webapp``
4. Run ``npm install`` from within ``focalboard/import/todoist``
5. Run ``npx ts-node importTodoist.ts -i <path-to-todoist.json> -o archive.focalboard`` (also from within ``focalboard/import/todoist``)
6. In Focalboard, click `Settings`, then ``Import archive`` and select ``archive.focalboard``

