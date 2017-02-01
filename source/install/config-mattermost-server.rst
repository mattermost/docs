Configuring Mattermost Server
=============================

1. Navigate to ``https://mattermost.example.com`` and create a team and user.

  The first user in the system is automatically granted the ``system_admin`` role, which gives you access to the System Console.

2. Open the System Console. Click your username at the top left of navigation panel. In the menu that opens, click **System Console**.

3. Setup an SMTP email service. Click **Notifications > Email** and make the following changes. The example below assumes AmazonSES.

    a. Set **Enable Email Notifications** to ``true``
    b. Set **Notification Display Name** to ``No-Reply``
    c. Set **Notification From Address** to ``mattermost@example.com``
    d. Set **SMTP Server Username** to ``[YOUR_SMTP_USERNAME]``
    e. Set **SMTP Server Password** to ``[YOUR_SMTP_PASSWORD]``
    f. Set **SMTP Server** to ``email-smtp.us-east-1.amazonaws.com``
    g. Set **SMTP Server Port** to ``465``
    h. Set **Connection Security** to ``TLS``
    i. Save the Settings

4. Click **Files > Storage** and change **Local Storage Directory** from ``./data/`` to ``/mattermost/data``

5. Click **General > Logging** and set **Output logs to console** to ``false``

6. Feel free to modify other settings.
7. Restart the Mattermost Service.
  
  ``sudo restart mattermost``
