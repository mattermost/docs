.. _bulk-loading-data:

Running the bulk loading command
--------------------------------

Before running the bulk loading command, you must first create a `JSONL
<https://jsonlines.org>`__ file that contains the data that you want to import. After you create the file, run the bulk load command in validation mode. In this mode, the data is checked for correctness, but is not written to the database. After validating, run the command in apply mode, which saves the data to the database.

**To bulk load data**:

1. Create the `JSONL
<https://jsonlines.org>`__ data file in your Mattermost directory. The file can have any name, but in this procedure it's called ``data.jsonl``. The format of the file is described in the :ref:`data-format` section.

2. Validate that the file is correct:

  a. Change to the Mattermost directory.

    ``cd /opt/mattermost`` (the location might be different on your system)

  b. Run the following command:

    ``sudo -u mattermost bin/mattermost import bulk data.jsonl --validate``

3. Resolve any errors that are reported, and validate the file again. Do not go to the next step until you can run the validate command without errors.

4. Run the bulk load command in apply mode:

  ``sudo -u mattermost bin/mattermost import bulk data.jsonl --apply``

5. When the bulk load command completes, clear all caches by going to **System Console > Environment > Web Server**.

.. important::

After the import tool has run, all files created in the ``data`` directory are owned by *root* as the tool was run as *sudo*. The owner of the ``data`` directory and all its content has to change to *mattermost* user, otherwise, Mattermost can't fetch the files created in the ``data`` directory after the import tool has run.
