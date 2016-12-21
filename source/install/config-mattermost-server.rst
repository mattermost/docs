Configuring Mattermost Server
=============================

1. Navigate to ``https://mattermost.example.com`` and create a team and user.

  The first user in the system is automatically granted the
  ``system_admin`` role, which gives you access to the System Console.

3. Open the System Console. Click your username at the top left of navigation panel. In the menu that opens, click **System Console**.

4. Setup an SMTP email service. Click **Notification** > **Email** and make the following changes. The example below assumes AmazonSES.

    a. Set **Send Email Notifications** to ``true``
    b. Set **Require Email Verification** to ``true``
    c. Set **Feedback Name** to ``No-Reply``
    d. Set **Feedback Email** to ``mattermost@example.com``
    e. Set **SMTP Username** to ``[YOUR_SMTP_USERNAME]``
    f. Set **SMTP Password** to ``[YOUR_SMTP_PASSWORD]``
    g. Set **SMTP Server** to ``email-smtp.us-east-1.amazonaws.com``
    h. Set **SMTP Port** to ``465``
    i. Set **Connection Security** to ``TLS``
    j. Save the Settings

5. Click **FILES** > **Storage** and change **Local Directory Location** from ``./data/`` to ``/mattermost/data``

6. Update **General** > **Logging** settings:

   -  Set **Log to The Console** to ``false``

7. Feel free to modify other settings.
8. Restart the Mattermost Service.
  
  ``sudo restart mattermost``
