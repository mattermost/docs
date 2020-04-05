..  _smtp-email-setup:

SMTP email set up
================

To run in production, Mattermost requires SMTP email to be enabled for email notifications and password reset for systems using email-based authentication.

How to enable email
-------------------

To enable email, configure an SMTP email service as follows:

1. **Set up an SMTP email sending service** (if you don't yet have an
   SMTP service with credentials).

   * Any SMTP email service can be used, you just need the following
      information: ``Server Name``, ``Port``, ``SMTP Username``, and
      ``SMTP Password``.

      * If you don't have an SMTP service, here are simple instructions
         to set one up with `Amazon Simple Email Service
         (SES) <https://aws.amazon.com/ses/>`__:

         1. Go to `Amazon SES
            console <https://console.aws.amazon.com/ses>`__ then
            ``SMTP Settings > Create My SMTP Credentials``
         2. Copy the ``Server Name``, ``Port``, ``SMTP Username``, and
            ``SMTP Password`` for Step 2 below.
         3. From the ``Domains`` menu set up and verify a new domain,
            then enable ``Generate DKIM Settings`` for the domain.

            1. We recommend you set up `Sender Policy
               Framework <https://en.wikipedia.org/wiki/Sender_Policy_Framework>`__
               (SPF) and/or `Domain Keys Identified
               Mail <https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail>`__
               (DKIM) for your email domain.

         4. Choose a sender address such as ``mattermost@example.com`` and
            click ``Send a Test Email`` to verify setup is working
            correctly.

2. **Configure SMTP settings**

   1. Log into an existing team and open the **System Console**.

      * Alternatively, if a team doesn't yet exist, go to
         ``http://dockerhost:8065/`` in your browser, create a team,
         then select **System Console** from the main menu.

   2. Go to **Authentication > Email** and configure the following:

      1.  **Allow account creation with email:** ``true``

   3. Go to **Site Configuration > Notifications > Email** and configure the following:

      1.  **Enable Email Notifications:** ``true``
      2.  **Notification Display Name:** Display name on email account
          sending notifications
      3.  **Notification From Address:** Email address displayed on
          email account used to send notifications
  4. Go to **Environment > SMTP** and configure the following:

      1. **SMTP Server**: ``SMTP Server`` from Step 1
      2. **SMTP Server Username**: ``SMTP Username`` from Step 1
      3. **SMTP Server Password**: ``SMTP Password`` from Step 1
      4. **SMTP Server Port**: ``SMTP Port`` from Step 1
      8. **Connection Security**: ``TLS (Recommended)``
      9. Select **Save**
      10. Choose **Test Connection**
      11. If the test failed please look in **Reporting > Server Logs** for any
          errors that look like ``[EROR] /api/v4/email/test ...``

   4. (Optional) Go to **Authentication** > **Signup** and configure the following:

      1.  **Enable Email Invitations:** ``true``

Sample SMTP settings
--------------------

Amazon SES
^^^^^^^^^^

-  Set **SMTP Server Username** to **[YOUR_SMTP_USERNAME]**
-  Set **SMTP Server Password** to **[YOUR_SMTP_PASSWORD]**
-  Set **SMTP Server** to **email-smtp.us-east-1.amazonaws.com**
-  Set **SMTP Server Port** to **465**
-  Set **Connection Security** to **TLS**

Postfix
^^^^^^^

-  Make sure Postfix is installed on the machine where Mattermost is
   installed
-  Set **SMTP Server Username** to **(empty)**
-  Set **SMTP Server Password** to **(empty)**
-  Set **SMTP Server** to **localhost**
-  Set **SMTP Server Port** to **25**
-  Set **Connection Security** to **(empty)**

Gmail
^^^^^^

-  Set **SMTP Server Username** to **your\_email@gmail.com**
-  Set **SMTP Server Password** to **your\_password**
-  Set **SMTP Server** to **smtp.gmail.com**
-  Set **SMTP Server Port** to **587**
-  Set **Connection Security** to **STARTTLS**

.. warning::

  Additional configuration is required in Google to allow SMTP email to relay through their servers.
  See `SMTP relay: Route outgoing non-Gmail messages through Google <https://support.google.com/a/answer/2956491?hl=en>`_ for the required steps.

Hotmail
^^^^^^^

-  Set **SMTP Server Username** to **your\_email@hotmail.com**
-  Set **SMTP Server Password** to **your\_password**
-  Set **SMTP Server** to **smtp-mail.outlook.com**
-  Set **SMTP Server Port** to **587**
-  Set **Connection Security** to **STARTTLS**

Office365 / Outlook
^^^^^^^^^^^^^^^^^^^^^

- Set **SMTP Server Username** to **your\_email@hotmail.com**
- Set **SMTP Server Password** to **your\_password**
- Set **SMTP Server** to **smtp.office365.com**
- Set **SMTP Server Port** to **587**
- Set **Connection Security** to **STARTTLS**

Troubleshooting SMTP
--------------------

TLS/STARTTLS requirements
^^^^^^^^^^^^^^^^^^^^^^^^^

If you fill in **SMTP Server Username** and **SMTP Server Password** then you must set
**Connection Security** to **TLS** or to **STARTTLS**.

Troubleshooting using logs
^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have issues with your SMTP install, from your Mattermost team
site go to the main menu and open **System Console > Reporting > Server Logs** to look for
error messages related to your setup. You can do a search for the error
code to narrow down the issue. Sometimes ISPs require nuanced setups for
SMTP and error codes can hint at how to make the proper adjustments.

For example, if **System Console > Reporting > Server Logs** has an error code reading:

::

    Connection unsuccessful: Failed to add to email address - 554 5.7.1 <unknown[IP-ADDRESS]>: Client host rejected: Access denied

Search for ``554 5.7.1 error`` and
``Client host rejected: Access denied``.

Checking your SMTP server is reachable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Attempt to telnet to the email service to make sure the server is
   reachable.
-  You must run the following commands from the same machine or virtual
   instance where ``mattermost/bin/mattermost`` is located.
-  Telnet to the email server with ``telnet mail.example.com 25``. If
   the command works you should see something like

   ::

       Trying 24.121.12.143...
       Connected to mail.example.com.
       220 mail.example.com NO UCE ESMTP

-  Then type something like ``HELO <your mail server domain>``. If the
   command works you should see something like

   ::

       250-mail.example.com NO UCE
       250-STARTTLS
       250-PIPELINING
       250 8BITMIME


.. note::
  As we're not installing telnet by default on the official docker images you either need to use ``ping`` on those or install telnet yourself either directly or by modifying the Dockerfile.

.. note::
  For additional troubleshooting tips, see
  the `troubleshooting guide <https://www.mattermost.org/troubleshoot/>`__. To submit an improvement or correction, click  **Edit** at the top of this page.
