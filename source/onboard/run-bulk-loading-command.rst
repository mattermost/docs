:nosearch:
.. _bulk-loading-data:

Bulk load data
---------------

Before running the bulk loading command, you must first create a `JSONL <https://jsonlines.org>`__ file that contains the data that you want to import in your Mattermost directory. The file can have any name, but in this example it's called ``data.jsonl``. The format of the file is described in the :ref:`data-format` section.

Next, zip it by running the ``zip -r data.zip data.jsonl`` command.

Using mmctl local mode
~~~~~~~~~~~~~~~~~~~~~~

From Mattermost v9.5, the mmctl bulk import process command in `local mode </manage/mmctl-command-line-tool.html#local-mode>`__ supports processing an import file without uploading it to the server. 

Run ``mmctl import process --bypass-upload <file>.zip`` to start your import and enable the Mattermost server to read from the file directly.

Not using mmctl local mode
~~~~~~~~~~~~~~~~~~~~~~~~~~
If you're not running mmctl commands in local mode:

1. Upload the ZIP file to the database by running the `mmctl import upload </manage/mmctl-command-line-tool.html#mmctl-import-upload>`__ command. For example: ``mmctl import upload data.zip``. 
2. Confirm that the file is uploaded and ready for use by running the `mmctl import list available </manage/mmctl-command-line-tool.html#mmctl-import-list-available>`__ command. 
3. Import your uploaded file by running the `mmctl import process </manage/mmctl-command-line-tool.html#mmctl-import-process>`__ command. For example: ``mmctl import process <importedid>_data.zip`` (use the name of the uploaded file from `mmctl import list available </manage/mmctl-command-line-tool.html#mmctl-import-list-available>`__ command).