..  _smtp-email-setup:

SMTP Email Setup
================

In product evaluation setups with single-container Docker instances,
email is intentionally disabled. This allows account creation and system
operation without having to set up email, but it also means email
notification and password reset functionality aren't available.

How to Enable Email
~~~~~~

To enable email, configure an SMTP email service as follows:

1. **Set up an SMTP email sending service** (if you don't yet have an
   SMTP service with credentials)

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

         4. Choose an sender address like ``mattermost@example.com`` and
            click ``Send a Test Email`` to verify setup is working
            correctly.

2. **Configure SMTP settings**

   1. Open the **System Console** by logging into an existing team and
      accessing "System Console" from the main menu.

      * Alternatively, if a team doesn't yet exist, go to
         ``http://dockerhost:8065/`` in your browser, create a team,
         then from the main menu click **System Console**

   2. Go to the **Email Settings** tab and configure the following:

      1.  **Allow Sign Up With Email:** ``true``
      2.  **Send Email Notifications:** ``true``
      3.  **Require Email Verification:** ``true``
      4.  **Notification Display Name:** Display name on email account
          sending notifications
      5.  **Notification Email Address:** Email address displayed on
          email account used to send notifications
      6.  **SMTP Username**: ``SMTP Username`` from Step 1
      7.  **SMTP Password**: ``SMTP Password`` from Step 1
      8.  **SMTP Server**: ``SMTP Server`` from Step 1
      9.  **SMTP Port**: ``SMTP Port`` from Step 1
      10. **Connection Security**: ``TLS (Recommended)``
      11. Then click **Save**
      12. Then click **Test Connection**
      13. If the test failed please look in **OTHER** > **Logs** for any
          errors that look like ``[EROR] /api/v3/admin/test_email ...``

Sample SMTP Settings
~~~~~~

Amazon SES
^^^^^^

-  Set **SMTP Username** to **SMTP_USERNAME**
-  Set **SMTP Password** to
   **SMTP_PASSWORD**
-  Set **SMTP Server** to **SMTP_SERVER**
-  Set **SMTP Port** to **SMTP_PORT**
-  Set **Connection Security** to **TLS**

Postfix
^^^^^^

-  Make sure Postfix is installed on the machine where Mattermost is
   installed
-  Set **SMTP Username** to **(empty)**
-  Set **SMTP Password** to **(empty)**
-  Set **SMTP Server** to **localhost**
-  Set **SMTP Port** to **25**
-  Set **Connection Security** to **(empty)**

Gmail
^^^^^^

-  Set **SMTP Username** to **your\_email@gmail.com**
-  Set **SMTP Password** to **your\_password**
-  Set **SMTP Server** to **smtp.gmail.com**
-  Set **SMTP Port** to **587**
-  Set **Connection Security** to **TLS**

Hotmail
^^^^^^

-  Set **SMTP Username** to **your\_email@hotmail.com**
-  Set **SMTP Password** to **your\_password**
-  Set **SMTP Server** to **smtp-mail.outlook.com**
-  Set **SMTP Port** to **587**
-  Set **Connection Security** to **STARTTLS**

Troubleshooting SMTP
~~~~~~~

Tip 1
^^^^^

If you fill in **SMTP Username** and **SMTP Password** then you must set
**Connection Security** to **TLS** or to **STARTTLS**

Tip 2
^^^^^

If you have issues with your SMTP install, from your Mattermost team
site go to the main menu and open **System Console -> Logs** to look for
error messages related to your setup. You can do a search for the error
code to narrow down the issue. Sometimes ISPs require nuanced setups for
SMTP and error codes can hint at how to make the proper adjustments.

For example, if **System Console -> Logs** has an error code reading:

::

    Connection unsuccessful: Failed to add to email address - 554 5.7.1 <unknown[IP-ADDRESS]>: Client host rejected: Access denied

Search for ``554 5.7.1 error`` and
``Client host rejected: Access denied``.

Tip 3
^^^^^

-  Attempt to telnet to the email service to make sure the server is
   reachable.
-  You must run the following commands from the same machine or virtual
   instance where ``mattermost/bin/platform`` is located. So if you're
   running Mattermost from docker you need to
   ``docker exec -ti mattermost-dev /bin/bash``
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
