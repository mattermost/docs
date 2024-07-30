..  _smtp-email-setup:

SMTP email setup
================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

In a production environment, Mattermost requires SMTP email enabled for email notifications and password resets when using :ref:`email-based authentication <configure/authentication-configuration-settings:enable sign-in with email>`.

Set up an SMTP email service
-----------------------------

Any SMTP email service can be used. You need a copy of the following information: ``Server Name``, ``Port``, ``SMTP Username``, and ``SMTP Password``.

.. tip::

    If you don't have an SMTP service you can set one up with `Amazon Simple Email Service (SES) <https://aws.amazon.com/ses/>`_:

    1. Go to `Amazon SES console <https://console.aws.amazon.com/ses>`__ then **SMTP Settings > Create My SMTP Credentials**.
    2. Copy the ``Server Name``, ``Port``, ``SMTP Username``, and ``SMTP Password`` values. You'll need these values to configure Mattermost.
    3. From the ``Domains`` menu, set up and verify a new domain, then enable ``Generate DKIM Settings`` for the domain. We recommend you set up `Sender Policy Framework <https://en.wikipedia.org/wiki/Sender_Policy_Framework>`__ (SPF) and/or `Domain Keys Identified Mail <https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail>`__ (DKIM) for your email domain.

    4. Choose a sender address like ``mattermost@domain.com`` and select ``Send a Test Email`` to verify setup is working correctly.
	    
    Alternatively, you can use one of the `services listed below <#sample-smtp-settings>`__, or can set up local ``sendmail`` by setting **Server Name** ``127.0.0.1`` with **Port** ``25``.

    If deploying Mattermost using :doc:`Docker </install/install-docker>`, the standard docker ``172.16.0.0/12`` IP range isn't used. Specify the IP range ``192.168.0.0/24`` to the email service to avoid relay access errors. If using postfix, under ``/etc/postfix/main.cf``, specify ``mynetworks = 192.168.0.0/24``. This may vary depending on how Mattermost is deployed. Ensure that **Port 25** is open if a firewall is present.

Configure SMTP settings
------------------------

1. In Mattermost go to **System Console > Authentication > Email**, and set **Allow Sign Up With Email**  to **true**.
      
2. In the System Console, go to **Notifications > Email** and configure Mattermost for your SMTP service. See the :ref:`SMTP configuration <configure/environment-configuration-settings:smtp>` documentation for details.

  - Set **Send Email Notifications** to **true**.
  - Set the **Notification Display Name** for the account sending notifications.
  - Set **Notification Email Address** for the email address used to send notifications.
  - Enter the **SMTP Username**, **SMTP Password**, **SMTP Server**, and **SMTP Port** you copied from initial setup.
  - We recommend setting **Connection Security**: to **TLS (Recommended)** to encrypt communication between Mattermost and your SMTP service.

3. Select **Save**.
4. Under **Connection Security**, select **Test Connection**. Mattermost will confirm whether a connection to the SMTP service is successful by sending you an email. If the test fails, Mattermost will provide details about why it failed in the System Console. See the `check Mattermost logs <#troubleshooting-using-logs>`__ section below for details.

Sample SMTP settings
--------------------

.. tab:: Amazon SES

  - Set **SMTP Username** to **[YOUR_SMTP_USERNAME]**
  - Set **SMTP Password** to **[YOUR_SMTP_PASSWORD]**
  - Set **SMTP Server** to **email-smtp.us-east-1.amazonaws.com**
  - Set **SMTP Port** to **465**
  - Set **Connection Security** to **TLS**

.. tab:: Postfix

  Make sure Postfix is installed on the same machine as Mattermost.

  - Set **SMTP Username** to **(empty)**
  - Set **SMTP Password** to **(empty)**
  - Set **SMTP Server** to **localhost**
  - Set **SMTP Port** to **25**
  - Set **Connection Security** to **(empty)**

.. tab:: Gmail

  - Set **SMTP Username** to **your\_email@gmail.com**
  - Set **SMTP Password** to **your\_password**
  - Set **SMTP Server** to **smtp.gmail.com**
  - Set **SMTP Port** to **587**
  - Set **Connection Security** to **STARTTLS**

  .. warning::

   Additional configuration is required in Google to allow SMTP email to relay through their servers. See `SMTP relay: Route outgoing non-Gmail messages through Google <https://support.google.com/a/answer/2956491?hl=en>`_ for the required steps.

.. tab:: Hotmail

  - Set **SMTP Username** to **your\_email@hotmail.com**
  - Set **SMTP Password** to **your\_password**
  - Set **SMTP Server** to **smtp-mail.outlook.com**
  - Set **SMTP Port** to **587**
  - Set **Connection Security** to **STARTTLS**

.. tab:: Office365/Outlook	

  - Set **SMTP Username** to **your\_email@hotmail.com**	
  - Set **SMTP Password** to **your\_password**	
  - Set **SMTP Server Name** to **smtp.office365.com**	
  - Set **SMTP Port** to **587**	
  - Set **Connection Security** to **STARTTLS**

Troubleshooting SMTP
--------------------

TLS/STARTTLS requirements 
~~~~~~~~~~~~~~~~~~~~~~~~~

If you fill in **SMTP Username** and **SMTP Password** then you must set **Connection Security** to **TLS** or to **STARTTLS**

Troubleshooting using logs
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have issues with your SMTP install, from your Mattermost team site go to **System Console > Logs** to look for error messages related to your setup. You can do a search for the error code to narrow down the issue. Sometimes ISPs require nuanced setups for SMTP and error codes can hint at how to make the proper adjustments.

For example, if **System Console > Logs** displays the following error, search for ``554 5.7.1 error`` and ``Client host rejected: Access denied``.

.. code-block:: none

  Connection unsuccessful: Failed to add to email address - 554 5.7.1 <unknown[IP-ADDRESS]>: Client host rejected: Access denied

Checking your SMTP server is reachable 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Attempt to Telnet to the email service to make sure the server is reachable. For additional information, visit https://docs.microsoft.com/en-us/exchange/mail-flow/test-smtp-with-telnet?view=exchserver-2019. If you're using an earlier version than Exchange Server 2019, select your version from the left-hand navigation menu.
- You must run the following commands from the same machine or virtual instance where ``mattermost/bin/mattermost`` is located.
- Telnet to the email server with ``telnet mail.example.com 25``. If the command works you should see something like:

  .. code-block:: none

    Trying 24.121.12.143...
    Connected to mail.example.com.
    220 mail.example.com NO UCE ESMTP

  Then type something like ``HELO <your mail server domain>``. If the command works you should see something like:

  .. code-block:: none

    250-mail.example.com NO UCE
    250-STARTTLS
    250-PIPELINING
    250 8BITMIME

.. note:: 

  - Telnet isn't included in official Mattermost Docker images, so you either need to use ``ping`` on those, or install Telnet yourself either directly or by modifying the Dockerfile.
  - For further assistance, review the `Troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot>`_ for previously reported errors, or `join the Mattermost user community for troubleshooting help <https://mattermost.com/community/>`_.