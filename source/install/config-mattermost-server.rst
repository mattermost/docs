Configuring Mattermost Server
=============================

Create the System Admin user and set up Mattermost for general use.

1. Open a browser and navigate to your Mattermost instance. For example, if the IP address of the Mattermost server is ``10.10.10.2`` then go to http://10.10.10.2:8065.

2. Create the first team and user. The first user in the system has the ``system_admin`` role, which gives you access to the System Console.

3. Open the System Console. To open the System Console, click your username at the top of the navigation panel, and in the menu that opens, click **System Console**.

4. Set the Site URL:
  a. In the GENERAL section of the System Console, click **Configuration** in prior versions or **System Console** > **Environment** > **Web Server** in versions after 5.12.
  b. In the **Site URL** field, set the URL that users point their browsers at. For example, *https://mattermost.example.com*. If you are using HTTPS, make sure that you set up TLS, either on Mattermost Server or on a proxy.

5. Set up email notifications.

  a. In the NOTIFICATIONS section of the System Console, make the following changes:

    - Set **Enable Email Notifications** to *true*
    - Set **Notification Display Name** to *No-Reply*
    - Set **Notification From Address** to *{your-domain-name}* For example, *example.com*
  
    B. In the NOTIFICATIONS section of the System Console in prior versions or **System Console** > **Environment** > **SMTP** in versions after 5.12, also make the following changes:

    - Set **SMTP Server Username** to *{SMTP-username}* For example, *admin@example.com*
    - Set **SMTP Server Password** to *{SMTP-password}*
    - Set **SMTP Server** to *{SMTP-server}* For example, *mail.example.com*
    - Set **SMTP Server Port** to *465*
    - Set **Connection Security** to *TLS* or *STARTTLS*, depending on what the SMTP server accepts.

  b. Click **Test Connection**.

  c. After your connection is working, click **Save**.

6. Set up the file and image storage location.

  .. note::
    1. Files and images that users attach to their messages are not stored in the database. Instead, they are stored in a location that you specify. You can store the files on the local file system or in Amazon S3.
    2. Make sure that the location has enough free space. The amount of storage that's required depends on the number of users and on the number and size of files that users attach to messages.

  a. In the FILES section of the System Console, click **Storage** in prior versions or **System Console** > **Environment** > **File Storage** in versions after 5.12.
  b. If you store the files locally, set **File Storage System** to *Local File System*, and then either accept the default for the **Local Storage Directory** or enter a location. The location must be a directory that exists and has write permissions for the Mattermost server. It can be an absolute path or a relative path. Relative paths are relative to the ``mattermost`` directory.
  c. If you store the files on Amazon S3, set **File Storage System** to *Amazon S3* and enter the appropriate values for your Amazon account.
  d. Click **Save**.

7. Review the other settings in the System Console to make sure everything is as you want it.

8. Restart the Mattermost Service.

  On Ubuntu 14.04 and RHEL 6:

  ``sudo restart mattermost``

  On Ubuntu 16.04, 18.04, Debian Stretch, and RHEL 7:

  ``sudo systemctl restart mattermost``
