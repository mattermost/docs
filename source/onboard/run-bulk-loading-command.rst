:nosearch:

Bulk load data
---------------

Before running the bulk loading command, you must first create a `JSONL <https://jsonlines.org>`__ file that contains the data that you want to import in your Mattermost directory. The file can have any name, but in this example it's called ``data.jsonl``. The format of the file is described in the `data-format </onboard/bulk-loading-data.html#data-format>`__ section.

After you create the JSONL file, you need to zip it by running the ``zip -r data.zip data.jsonl`` command, and upload the ZIP file to the database by running the `mmctl import upload </manage/mmctl-command-line-tool.html#mmctl-import-upload>`__ command. For example: ``mmctl import upload data.zip``.

Confirm that the file is uploaded and ready for use by running the `mmctl import list available </manage/mmctl-command-line-tool.html#mmctl-import-list-available>`__ command. 

Then import your uploaded file by running the `mmctl import process </manage/mmctl-command-line-tool.html#mmctl-import-process>`__ command. For example: ``mmctl import process <importedid>_data.zip`` (use the name of the uploaded file from `mmctl import list available </manage/mmctl-command-line-tool.html#mmctl-import-list-available>`__ command).