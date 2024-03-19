:orphan:
:nosearch:

Common issues
-------------

Run the bulk import command as the *mattermost* user. Running it as *root* or any other user will cause issues with file permissions on imported attachments.

Ensure that :ref:`file attachments are enabled <configure/site-configuration-settings:allow file sharing>`, that you have enough free space in your :ref:`file storage system <configure/environment-configuration-settings:file storage system>` to support the incoming attachments, and that your :ref:`maximum file size <configure/environment-configuration-settings:maximum file size>` is appropriate.

Make sure you have enough free space for logs on the Mattermost server as well as free space on the database server for both the database itself and transaction logs.

Disable anti-virus or any other plugins that might interfere with attachment uploading. They could potentially block uploading of attachments and cause the import to fail if configured incorrectly. If you need anti-virus scanning, scan the attachment folder before the import.
