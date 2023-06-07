:nosearch:
.. _bulk-loading-common-issues:

Common issues
-------------

Run the bulk import command as the *mattermost* user. Running it as *root* or any other user will cause issues with file permissions on imported attachments.

Ensure that `file attachments are enabled </configure/configuration-settings.html#allow-file-sharing>`__, that you have enough free space in your `file storage system </configure/configuration-settings.html#file-storage-system>`__ to support the incoming attachments, and that your `maximum file size </configure/configuration-settings.html#maximum-file-size>`__ is appropriate.

Make sure you have enough free space for logs on the Mattermost server as well as free space on the database server for both the database itself and transaction logs.

Disable anti-virus or any other plugins that might interfere with attachment uploading. They could potentially block uploading of attachments and cause the import to fail if configured incorrectly. If you need anti-virus scanning, scan the attachment folder before the import.
