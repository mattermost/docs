.. _bulk-loading-data:

Running the bulk loading command
================================

Before running the bulk loading command, you must first create a JSON file that contains the data that you want to import. After you create the file, run the bulk load command in validation mode. In this mode, the data is checked for correctness, but is not written to the database. After validating, run the command in apply mode, which saves the data to the database.

**To bulk load data**:

1. Create the JSON data file in your Mattermost ``bin`` directory. The file can have any name, but in this procedure it's called ``data.json``. The format of the file is described in the :ref:`data-format` section.
2. Validate that the file is correct:

  a. Change to the Mattermost ``bin`` directory.

    ``cd /opt/mattermost/bin`` (the location might be different on your system)

  b. Run the following command:

    ``sudo ./platform import bulk data.json --validate``

3. Resolve any errors that are reported, and validate the file again. Do not go to the next step until you can run the validate command without errors.

4. Run the bulk load command in apply mode:

  ``sudo ./platform import bulk data.json --apply``

5. When the bulk load command completes, clear all caches. Open the System Console, and click **General > Configuration > Purge All Caches**.
