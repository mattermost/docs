Import your data
================

You can import data from other tools to use with Boards. [Contribute code](https://www.focalboard.com/contribute/getting-started/) to expand this.

Import from Asana
-----------------

This node app converts an Asana JSON archive into a ``.focalboard`` archive.

1. Log into your Asana account.
2. Select the drop-down menu next to the Asana board's name. Then select **Export/Print > JSON**. This will create an archive file which you'll use in Boards.
3. Save the file locally, e.g. to ``asana.json``.
4. Open a terminal window on your local machine and navigate to ``focalboard/webapp``.
5. Run ``npm install``.
6. Change directory to ``focalboard/import/asana``.
7. Run ``npm install``.
8. From within the same folder, run ``npx ts-node importAsana.ts -i <asana.json> -o archive.focalboard``. This generates the following data:

.. code-block::
   
    My-MacbookPro:asana macbook$ npx ts-node importAsana.ts -i ~/Downloads/asana.json -o archive.focalboard
    Board: 1:1 Meeting Agenda Test
    Card: [READ ME] Instructions for using this project
    Card: [EXAMPLE TASK] Feedback on design team presentation
    Card: [EXAMPLE TASK] Finalize monthly staffing plan
    Card: [EXAMPLE TASK] Review Q2 launch video outline
    Card: [EXAMPLE TASK] Mentor a peer
    
    Found 5 card(s).
    Exported to archive.focalboard

9. In Boards, open the board you want to use for the export.
10. Select **Settings > Import archive** and select ``archive.focalboard``.
11. Select **Upload**.
12. Return to your board and confirm that your Asana data is now displaying.

If you don't see your Asana data, an the error should be displayed. You can also check log files for errors.

Import scope
^^^^^^^^^^^^

Currently, the script imports all cards from a single board, including their section (column) membership, names, and notes.

Import from Notion
------------------

This node app converts a Notion CSV and markdown export into a ``.focalboard`` archive.

1. From a Notion Board, open the **...** menu at the top right corner of the board.
2. Select `Export` and pick `Markdown & CSV` as the export format.
3. Save the generated file locally, and unzip the folder.
4. Open a terminal window on your local machine and navigate to ``focalboard/webapp``.
5. Run ``npm install``.
6. Change directory to `focalboard/import/notion`.
5. Run ``npm install``.
6. From within the same folder, run ``npx ts-node importNotion.ts -i <path to the notion-export folder> -o archive.focalboard``.
7. In Boards, open the board you want to use for the export.
8. Select **Settings > Import archive** and select ``archive.focalboard``.
9. Select **Upload**.
10. Return to your board and confirm that your Notion data is now displaying.

Import scope
^^^^^^^^^^^^

Currently, the script imports all cards from a single board, including their properties and markdown content.

The Notion export format does not preserve property types, so the script currently imports all card properties as a Select type. You can change the type after importing into Focalboard.

Import from Jira
----------------

This node app converts a Jira ``.XML`` export into a ``.focalboard`` archive.

1. Open Jira advanced search, and search for all the items to export.
2. Select **Export > Export XML.
3. Save the generated file locally, e.g. to ``jira_export.xml``.
4. Open a terminal window on your local machine and navigate to ``focalboard/webapp``.
5. Run ``npm install``.
6. Change directory to ``focalboard/import/jira`.
7. Run ``npm install``.
8. From within the same folder, run ``npx ts-node importJira.ts -i <path-to-jira.xml> -o archive.focalboard``.
9. In Boards, open the board you want to use for the export.
10. Select **Settings > Import archive** and select ``archive.focalboard``.
11. Select **Upload**.
12. Return to your board and confirm that your Jira data is now displaying.

Import scope and known limitations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently, the script imports each item as a card into a single board. Note that Jira ``.XML`` export is limited to 1000 issues at a time.

Users are imported as Select properties, with the name of the user.

The following aren't currently imported:

* Custom properties
* Comments
* Embedded files

Import from Trello
------------------

This node app converts a Trello ``.json`` archive into a ``.focalboard`` archive.

1. From the Trello Board Menu, select **...Show Menu**.
2. Select **More > Print and Export > Export to JSON**.
3. Save the generated file locally, e.g. to ``trello.json``.
4. Open a terminal window on your local machine and navigate to ``focalboard/webapp``.
5. Run ``npm install``.
6. Change directory to ``focalboard/import/trello``.
7. Run ``npm install``.
8. From within the same folder, run ``npx ts-node importTrello.ts -i <path-to-trello.json> -o archive.focalboard``.
9. In Boards, open the board you want to use for the export.
10. Select **Settings > Import archive** and select ``archive.focalboard``.
11. Select **Upload**.
12. Return to your board and confirm that your Trello data is now displaying.

Import scope
^^^^^^^^^^^^

Currently, the script imports all cards from a single board, including their list (column) membership, names, and descriptions.

Import from Todoist
-------------------

This node app converts a Todoist ``.json`` archive into a ``.focalboard`` archive.

1. Visit the open source Todoist data export service at https://darekkay.com/todoist-export/.
2. From the **Options** menu, select **Export As > JSON (all data)**.
3. Uncheck the **Archived** option if checked.
4. Select **Authorize and Backup**. This will take you to your Todoist account. Follow the instructions on screen.
5. Note the name and location of the downloaded ``.json`` file.
6. Open a terminal window on your local machine and navigate to ``focalboard/webapp``.
7. Run ``npm install``.
8. Change directory to ``focalboard/import/todoist``.
9. Run ``npm install``.
10. From within the same folder, run ``npx ts-node importTodoist.ts -i <path-to-todoist.json> -o archive.focalboard``.
11. In Boards, open the board you want to use for the export.
12. Select **Settings > Import archive** and select ``archive.focalboard``.
13. Select **Upload**.
14. Return to your board and confirm that your Todoist data is now displaying.
