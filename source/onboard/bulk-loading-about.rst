.. _about-bulk-loading-command:

About the bulk loading command
------------------------------

The bulk loading command is interruptible and idempotent
  If the import is interrupted for any reason, it continues from where it left off the next time you run it. You can run the command repeatedly with the same data file, and the data is imported only once. From v5.20, posts with matching timestamps to incoming posts will have their attachments replaced by the incoming data. Prior to v5.20 any updates to posts with matching timestamps were appended to older posts. 

You can run the bulk loading command on a live system
  Although you don't need to shut down Mattermost to run the command, changes made by users of the system between runs can be overwritten if the corresponding fields exist in the data file.

Some data fields are optional
  Not all fields are mandatory. If an optional field is missing from the object that is being imported, the field's current value in the database is not changed.

The bulk loading command is not a synchronization tool
  You cannot use the bulk loading command to remove any objects or their fields from the Mattermost database. The command only creates or overwrites fields.

.. important::
  The bulk loading command runs in the CLI and operates in the security context of the CLI. This means it has full permissions to access and alter everything in the Mattermost database.
