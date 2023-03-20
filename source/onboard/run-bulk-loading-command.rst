:nosearch:
.. _bulk-loading-data:

Bulk load data
---------------

Before running the bulk loading command, you must first create a `JSONL <https://jsonlines.org>`__ file that contains the data that you want to import in your Mattermost directory. The file can have any name, but in this example it's called ``data.jsonl``. The format of the file is described in the :ref:`data-format` section.

.. tabs::

  .. tab:: Use mmctl

    1. After you created the JSONL file, you need to zip it (`zip -r data.zip data.jsonl`) and upload the ZIP file to the database by running the `mmctl import upload </manage/mmctl-command-line-tool.html#mmctl-import-upload>`__ command. For example: ``mmctl import upload data.zip``.

    2. Confirm that the file is uploaded and ready for use by running the `mmctl import list available </manage/mmctl-command-line-tool.html#mmctl-import-list-available>`__ command. 

    3. Import your uploaded file by running the `mmctl import process </manage/mmctl-command-line-tool.html#mmctl-import-process>`__ command. For example: ``mmctl import process <importedid>_data.zip`` (use the name of the uploaded file from `mmctl import list available </manage/mmctl-command-line-tool.html#mmctl-import-list-available>`__ command).

  .. tab:: Use CLI

    After you create the file, validate that the file is correct by running the bulk load command in validation mode. In this mode, the data is checked for correctness, but is not written to the database. After validating, run the command in apply mode, which saves the data to the database.

    1. Change to the Mattermost directory.

       ``cd /opt/mattermost`` (the location might be different on your system)

    2. Run the following command:

       ``sudo -u mattermost bin/mattermost import bulk data.jsonl --validate``

    3. Resolve any errors that are reported, and validate the file again. Do not go to the next step until you can run the validate command without errors.

    4. Run the bulk load command in apply mode:

       ``sudo -u mattermost bin/mattermost import bulk data.jsonl --apply``

    5. When the bulk load command completes, clear all caches in the System Console by going to **System Console > Environment > Web Server**.

    .. important::

      After the import tool has run, all files created in the ``data`` directory are owned by *root* as the tool was run as *sudo*. The owner of the ``data`` directory and all its content has to change to *mattermost* user, otherwise, Mattermost can't fetch the files created in the ``data`` directory after the import tool has run.
