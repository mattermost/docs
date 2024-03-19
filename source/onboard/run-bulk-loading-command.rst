:nosearch:
.. _bulk-loading-data:

Bulk load data
---------------

Before running the bulk loading command, you must first create a `JSONL <https://jsonlines.org>`__ file that contains the data that you want to import in your Mattermost directory. The file can have any name, but in this example it's called ``data.jsonl``. The format of the file is described in the :ref:`data-format <onboard/bulk-loading-data:data format>` section.

Next, zip it by running the ``zip -r data.zip data.jsonl`` command.

Using mmctl local mode
~~~~~~~~~~~~~~~~~~~~~~

From Mattermost v9.5, the mmctl bulk import process command in :ref:`local mode <manage/mmctl-command-line-tool:local mode>` supports processing an import file without uploading it to the server. 

Run ``mmctl import process --bypass-upload <file>.zip`` to start your import and enable the Mattermost server to read from the file directly.

Not using mmctl local mode
~~~~~~~~~~~~~~~~~~~~~~~~~~
If you're not running mmctl commands in local mode:

1. Upload the ZIP file to the database by running the :ref:`mmctl import upload <manage/mmctl-command-line-tool:mmctl import upload>` command. For example: ``mmctl import upload data.zip``. 
2. Confirm that the file is uploaded and ready for use by running the :ref:`mmctl import list available <manage/mmctl-command-line-tool:mmctl import list available>` command. 
3. Import your uploaded file by running the :ref:`mmctl import process <manage/mmctl-command-line-tool:mmctl import process>` command. For example: ``mmctl import process <importedid>_data.zip`` (use the name of the uploaded file from :ref:`mmctl import list available <manage/mmctl-command-line-tool:mmctl import list available>` command).