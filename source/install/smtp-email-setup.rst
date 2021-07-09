..  _smtp-email-setup:

SMTP Email Setup
================

To run in production, Mattermost requires SMTP email to be enabled for email notifications and password reset for systems using email-based authentication.

How to Enable Email
-------------------

To enable email, configure an SMTP email service as follows:

1. **Set up an SMTP email sending service** (if you don't yet have an
   SMTP service with credentials)

    * Any SMTP email service can be used, you just need the following
      information: ``Server Name``, ``Port``, ``SMTP Username``, and
      ``SMTP Password``.

    * If you don't have an SMTP service you can set one up with:

        - `Amazon Simple Email Service (SES) <https://aws.amazon.com/ses/>`__:

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

            4. Choose a sender address like ``mattermost@example.com`` and
                click ``Send a Test Email`` to verify setup is working
                correctly.
	    
        - By local ``sendmail`` can be used by using **Server Name** ``127.0.0.1`` with **Port** ``25``
	- Or by using one of the services listed below in the **Sample SMTP Settings**

2. **Configure SMTP settings**

   1. Open the **System Console** by logging into an existing team and
      accessing "System Console" from the main menu.

      * Alternatively, if a team doesn't yet exist navigate to your ``serverURL`` click **Go To System Console**.

   2. Go to the **Authentication** > **Email** tab and configure the following:

      1.  **Allow Sign Up With Email:** ``true``
      
   3. Go to the **Notifications** > **Email** tab and configure the following:
   
      1.  **Send Email Notifications:** ``true``
      2.  **Notification Display Name:** Display name on email account
          sending notifications
      3.  **Notification Email Address:** Email address displayed on
          email account used to send notifications
      4.  **SMTP Username**: ``SMTP Username`` from Step 1
      5.  **SMTP Password**: ``SMTP Password`` from Step 1
      6.  **SMTP Server**: ``SMTP Server`` from Step 1
      7.  **SMTP Port**: ``SMTP Port`` from Step 1
      8. **Connection Security**: ``TLS (Recommended)``
      9. Then click **Save**
      10. Then click **Test Connection**
      11. If the test failed please look in **OTHER** > **Logs** for any
          errors that look like ``[EROR] /api/v4/email/test ...``

   4. (Optional) Go to the **Security** > **Sign Up** tab and configure the following:

      1.  **Enable Email Invitations:** ``true``

Sample SMTP Settings
--------------------

Amazon SES
~~~~~~~~~~

-  Set **SMTP Username** to **[YOUR_SMTP_USERNAME]**
-  Set **SMTP Password** to **[YOUR_SMTP_PASSWORD]**
-  Set **SMTP Server** to **email-smtp.us-east-1.amazonaws.com**
-  Set **SMTP Port** to **465**
-  Set **Connection Security** to **TLS**

Postfix
~~~~~~~

-  Make sure Postfix is installed on the machine where Mattermost is
   installed
-  Set **SMTP Username** to **(empty)**
-  Set **SMTP Password** to **(empty)**
-  Set **SMTP Server** to **localhost**
-  Set **SMTP Port** to **25**
-  Set **Connection Security** to **(empty)**

Gmail
~~~~~

-  Set **SMTP Username** to **your\_email@gmail.com**
-  Set **SMTP Password** to **your\_password**
-  Set **SMTP Server** to **smtp.gmail.com**
-  Set **SMTP Port** to **587**
-  Set **Connection Security** to **STARTTLS**

.. warning::

  Additional configuration is required in Google to allow SMTP email to relay through their servers.
  See `SMTP relay: Route outgoing non-Gmail messages through Google <https://support.google.com/a/answer/2956491?hl=en>`_ for the required steps.

Hotmail
~~~~~~~

-  Set **SMTP Username** to **your\_email@hotmail.com**
-  Set **SMTP Password** to **your\_password**
-  Set **SMTP Server** to **smtp-mail.outlook.com**
-  Set **SMTP Port** to **587**
-  Set **Connection Security** to **STARTTLS**

Office365/Outlook	
~~~~~~~~~~~~~~~~~~~
	
- Set **SMTP Username** to **your\_email@hotmail.com**	
- Set **SMTP Password** to **your\_password**	
- Set **SMTP Server Name** to **smtp.office365.com**	
- Set **SMTP Port** to **587**	
- Set **Connection Security** to **STARTTLS**

Troubleshooting SMTP
--------------------

TLS/STARTTLS Requirements 
~~~~~~~~~~~~~~~~~~~~~~~~~

If you fill in **SMTP Username** and **SMTP Password** then you must set
**Connection Security** to **TLS** or to **STARTTLS**

Troubleshooting using Logs
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have issues with your SMTP install, from your Mattermost team site go to **System Console > Logs** to look for error messages related to your setup. You can do a search for the error code to narrow down the issue. Sometimes ISPs require nuanced setups for SMTP and error codes can hint at how to make the proper adjustments.

For example, if **System Console > Logs** has an error code reading:

::

    Connection unsuccessful: Failed to add to email address - 554 5.7.1 <unknown[IP-ADDRESS]>: Client host rejected: Access denied

Search for ``554 5.7.1 error`` and
``Client host rejected: Access denied``.

Checking your SMTP server is reachable 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Attempt to telnet to the email service to make sure the server is reachable.
-  You must run the following commands from the same machine or virtual instance where ``mattermost/bin/mattermost`` is located.
-  Telnet to the email server with ``telnet mail.example.com 25``. If the command works you should see something like:

   ::

       Trying 24.121.12.143...
       Connected to mail.example.com.
       220 mail.example.com NO UCE ESMTP

-  Then type something like ``HELO <your mail server domain>``. If the command works you should see something like:

   ::

       250-mail.example.com NO UCE
       250-STARTTLS
       250-PIPELINING
       250 8BITMIME
       

.. note:: 
   
   As we're not installing telnet by default on the official docker images you either need to use ``ping`` on those or install telnet yourself either directly or by modifying the Dockerfile.

.. note::
   
   For further assistance, review the `Troubleshooting forum <https://forum.mattermost.org/c/trouble-shoot>`__ for previously reported errors, or `join the Mattermost user community for troubleshooting help <https://mattermost.com/pl/default-ask-mattermost-community/>`_. To submit an improvement or correction to this page, click **Edit** in the top-right corner of the page.
