Configuring Mattermost Server
-----------------------------

Create the System Admin user and set up Mattermost for general use.

1. Open a browser and navigate to your Mattermost instance. For example, if the IP address of the Mattermost server is ``10.10.10.2`` then go to http://10.10.10.2:8065.

2. Create the first team and user. The first user in the system has the ``system_admin`` role, which gives you access to the System Console.

3. To open the System Console, click your username at the top of the navigation panel and select **System Console**.

4. Set the Site URL:

  * Open **System Console > Environment > Web Server**.
  * In the **Site URL** field, set the URL that users point their browsers at. For example, *https://mattermost.example.com*. If you are using HTTPS, make sure that you set up TLS, either on Mattermost server or on a proxy.

5. Set up email notifications.

  * In **Site Configuration > Notifications** make the following changes:

    - Set **Enable Email Notifications** to **true**
    - Set **Notification Display Name** to **No-Reply**
    - Set **Notification From Address** to *{your-domain-name}* For example, *example.com*
  
  * In **System Console > Environment > SMTP** make the following changes:

    - Set **SMTP Server Username** to *{SMTP-username}* For example, *admin@example.com*
    - Set **SMTP Server Password** to *{SMTP-password}*
    - Set **SMTP Server** to *{SMTP-server}* For example, *mail.example.com*
    - Set **SMTP Server Port** to *465*
    - Set **Connection Security** to *TLS* or *STARTTLS*, depending on what the SMTP server accepts

  * Select **Save**
  * Select **Test Connection**.
  
6. Open **System Console > Environment > File Storage** to set up the file and image storage location.

  * If you store the files locally, set **File Storage System** to *Local File System*, and then either accept the default for the **Local Storage Directory** or enter a location. The location must be a directory that exists and has write permissions for the Mattermost server. It can be an absolute path or a relative path. Relative paths are relative to the ``mattermost`` directory.
  * If you store the files on Amazon S3, set **File Storage System** to *Amazon S3* and enter the appropriate values for your Amazon account.
 
.. note::

    * Files and images that users attach to their messages are not stored in the database. Instead, they're stored in a location that you specify. You can keep the files on the local file system or in Amazon S3.
    * Make sure that the location has enough free space. The amount of storage required depends on the number of users and the number and size of files that users attach to messages.
 
7. Select **Save** to apply the configuration.

8. Review and configure any other settings that may be applicable.

9. Restart Mattermost.

  ``sudo systemctl restart mattermost``
