Email Templates
===============

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Mattermost has a few email templates that are sent out when a specific event occurs.
Most of the time these templates do not need to be modified.
In case additional modifications are necessary, all available props in each email are listed below.
The 'Content'-Field is just to give a quick description of the prop. Please check the i18n strings for the exact wording.

The email templates are located in the Mattermost server directory in the ``templates`` folder.
The corresponding strings for each prop can be found in the ``i18n`` folder. 

.. note::
  The props between different email templates are not interchangeable without additional server code changes.  

.. warning::
  Changes made inside of the ``templates`` or ``i18n`` folder might get overwritten during a server update. 
  Please make sure to backup them accordingly.


Available templates
-------------------

Email Footer
~~~~~~~~~~~~

**Purpose**:
This is appended to all outgoing emails sent by Mattermost.

**Props**:

+--------------+------------------------------+-----------------------------------+
| Prop         | Content                      | i18n String                       |
+==============+==============================+===================================+
| Footer       | Message intro                | api.templates.email_footer        |
+--------------+------------------------------+-----------------------------------+
| Organization | Name of Organization         | api.templates.email_organization  |
+--------------+------------------------------+-----------------------------------+
| EmailInfo1   | First line of footer         | api.templates.email_info1         |
+--------------+------------------------------+-----------------------------------+
| EmailInfo2   | Second line of footer        | api.templates.email_info2         |
+--------------+------------------------------+-----------------------------------+
| EmailInfo3   | Third line of footer         | api.templates.email_info3         |
+--------------+------------------------------+-----------------------------------+
| SupportEmail | Email for Mattermost support | --                                |
+--------------+------------------------------+-----------------------------------+


SendChangeUsernameEmail
~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when username has been changed.

**Body Props**:

+---------+------------------------------+--------------------------------------------+
| Prop    | Content                      | i18n String                                |
+=========+==============================+============================================+
| SiteURL | URL of the Mattermost server | --                                         |
+---------+------------------------------+--------------------------------------------+
| Title   | Message heading              | api.templates.username_change_body.title   |
+---------+------------------------------+--------------------------------------------+
| Info    | Message body                 | api.templates.username_change_body.info    |
+---------+------------------------------+--------------------------------------------+
| Warning | Warning text                 | api.templates.email_warning                |
+---------+------------------------------+--------------------------------------------+


SendEmailChangeVerifyEmail
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when an email change has been requested. Contains verification link and button.

**Body Props**:

+--------------+-------------------------------+--------------------------------------------------+
| Prop         | Content                       | i18n String                                      |
+==============+===============================+==================================================+
| SiteURL      | URL of the Mattermost server  | --                                               |
+--------------+-------------------------------+--------------------------------------------------+
| Title        | Message heading               | api.templates.email_change_verify_body.title     |
+--------------+-------------------------------+--------------------------------------------------+
| Info         | Message body                  | api.templates.email_change_verify_body.info      |
+--------------+-------------------------------+--------------------------------------------------+
| VerifyUrl    | URL for email verification    | --                                               |
+--------------+-------------------------------+--------------------------------------------------+
| VerifyButton | Button for email verification | api.templates.email_change_verify_body.button    |
+--------------+-------------------------------+--------------------------------------------------+


SendEmailChangeEmail
~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when the email has been changed successfully.

**Body Props**:

+---------+------------------------------+-----------------------------------------+
| Prop    | Content                      | i18n String                             |
+=========+==============================+=========================================+
| SiteURL | URL of the Mattermost server | --                                      |
+---------+------------------------------+-----------------------------------------+
| Title   | Message heading              | api.templates.email_change_body.title   |
+---------+------------------------------+-----------------------------------------+
| Info    | Message body                 | api.templates.email_change_body.info    |
+---------+------------------------------+-----------------------------------------+
| Warning | Warning text                 | api.templates.email_warning             |
+---------+------------------------------+-----------------------------------------+


SendVerifyEmail
~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user upon account creation to verify email address.

**Body Props**:

+-----------+------------------------------+-----------------------------------+
| Prop      | Content                      | i18n String                       |
+===========+==============================+===================================+
| SiteURL   | URL of the Mattermost server | --                                |
+-----------+------------------------------+-----------------------------------+
| Title     | Message heading              | api.templates.verify_body.title   |
+-----------+------------------------------+-----------------------------------+
| Info      | Message body                 | api.templates.verify_body.info    |
+-----------+------------------------------+-----------------------------------+
| VerifyUrl | URL for email verification   | --                                |
+-----------+------------------------------+-----------------------------------+
| Button    | Button for email verfication | api.templates.verify_body.button  |
+-----------+------------------------------+-----------------------------------+


SendSignInChangeEmail
~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when sign-in method has been changed (i.e. from email to LDAP, etc.)

**Body Props**:

+---------+------------------------------+------------------------------------------------+
| Prop    | Content                      | i18n String                                    |
+=========+==============================+================================================+
| SiteURL | URL of the Mattermost server | --                                             |
+---------+------------------------------+------------------------------------------------+
| Title   | Message heading              | api.templates.signin_change_email.body.title   |
+---------+------------------------------+------------------------------------------------+
| Info    | Message body                 | api.templates.signin_change_email.body.info    |
+---------+------------------------------+------------------------------------------------+
| Warning | Warning text                 | api.templates.email_warning                    |
+---------+------------------------------+------------------------------------------------+


SendWelcomeEmail
~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when the account has been created. May also contain download links to Apps as well as email verification links.

**Body Props**:

+-----------------+------------------------------+-------------------------------------------------+
| Prop            | Content                      | i18n String                                     |
+=================+==============================+=================================================+
| SiteURL         | URL of the Mattermost server | --                                              |
+-----------------+------------------------------+-------------------------------------------------+
| Title           | Message heading              | api.templates.welcome_body.title                |
+-----------------+------------------------------+-------------------------------------------------+
| Info            | Message body                 | api.templates.welcome_body.info                 |
+-----------------+------------------------------+-------------------------------------------------+
| Button          | Button for confirmation      | api.templates.welcome_body.button               |
+-----------------+------------------------------+-------------------------------------------------+
| Info2           | Continuation of message body | api.templates.welcome_body.info2                |
+-----------------+------------------------------+-------------------------------------------------+
| Info3           | Continuation of message body | api.templates.welcome_body.info3                |
+-----------------+------------------------------+-------------------------------------------------+


**Optional Props**:

+-----------------+------------------------------+-------------------------------------------------+
| Prop            | Content                      | i18n String                                     |
+=================+==============================+=================================================+
| AppDownloadInfo | Info for App Downloads       | api.templates.welcome_body.app_download_info    |
+-----------------+------------------------------+-------------------------------------------------+
| AppDownloadLink | Download link for Apps       | --                                              |
+-----------------+------------------------------+-------------------------------------------------+
| VerifyUrl       | Link for verification        | --                                              |
+-----------------+------------------------------+-------------------------------------------------+


SendPasswordChangeEmail
~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when password has been changed.

**Body Props**:

+---------+------------------------------+--------------------------------------------+
| Prop    | Content                      | i18n String                                |
+=========+==============================+============================================+
| SiteURL | URL of the Mattermost server | --                                         |
+---------+------------------------------+--------------------------------------------+
| Title   | Message heading              | api.templates.password_change_body.title   |
+---------+------------------------------+--------------------------------------------+
| Info    | Message body                 | api.templates.password_change_body.info    |
+---------+------------------------------+--------------------------------------------+
| Warning | Warning text                 | api.templates.email_warning                |
+---------+------------------------------+--------------------------------------------+


SendAccessTokenEmail
~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when an access token has been added to the account.

**Body Props**:

+---------+------------------------------+-----------------------------------------------+
| Prop    | Content                      | i18n String                                   |
+=========+==============================+===============================================+
| SiteURL | URL of the Mattermost server | --                                            |
+---------+------------------------------+-----------------------------------------------+
| Title   | Message heading              | api.templates.user_access_token_body.title    |
+---------+------------------------------+-----------------------------------------------+
| Info    | Message body                 | api.templates.user_access_token_body.info     |
+---------+------------------------------+-----------------------------------------------+
| Warning | Warning text                 | api.templates.email_warning                   |
+---------+------------------------------+-----------------------------------------------+


SendPasswordResetEmail
~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when password request has been initiated.

**Body Props**:

+----------+------------------------------+----------------------------------+
| Prop     | Content                      | i18n String                      |
+==========+==============================+==================================+
| SiteURL  | URL of the Mattermost server | --                               |
+----------+------------------------------+----------------------------------+
| Title    | Message heading              | api.templates.reset_body.title   |
+----------+------------------------------+----------------------------------+
| Info1    | Message body                 | api.templates.reset_body.info1   |
+----------+------------------------------+----------------------------------+
| Info2    | Continuation of message body | api.templates.reset_body.info2   |
+----------+------------------------------+----------------------------------+
| ResetUrl | URL to reset password        | --                               |
+----------+------------------------------+----------------------------------+
| Button   | Button for confirmation      | api.templates.reset_body.button  |
+----------+------------------------------+----------------------------------+


SendMfaChangeEmail
~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when multi-factor authentication method has been changed.

**Body Props when MFA is activated**:

+---------+------------------------------+------------------------------------------+
| Prop    | Content                      | i18n String                              |
+=========+==============================+==========================================+
| SiteURL | URL of the Mattermost server | --                                       |
+---------+------------------------------+------------------------------------------+
| Title   | Message heading              | api.templates.mfa_activated_body.title   |
+---------+------------------------------+------------------------------------------+
| Info    | Message body                 | api.templates.mfa_activated_body.info    |
+---------+------------------------------+------------------------------------------+
| Warning | Warning text                 | api.templates.email_warning              |
+---------+------------------------------+------------------------------------------+


**Body Props when MFA is deactivated**:

+---------+------------------------------+--------------------------------------------+
| Prop    | Content                      | i18n String                                |
+=========+==============================+============================================+
| SiteURL | URL of the Mattermost server | --                                         |
+---------+------------------------------+--------------------------------------------+
| Title   | Message heading              | api.templates.mfa_deactivated_body.title   |
+---------+------------------------------+--------------------------------------------+
| Info    | Message body                 | api.templates.mfa_deactivated_body.info    |
+---------+------------------------------+--------------------------------------------+
| Warning | Warning text                 | api.templates.email_warning                |
+---------+------------------------------+--------------------------------------------+


SendDeactivateAccountEmail
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when account has been deactivated.

**Body Props**:

+---------+------------------------------+----------------------------------------+
| Prop    | Content                      | i18n String                            |
+=========+==============================+========================================+
| SiteURL | URL of the Mattermost server | --                                     |
+---------+------------------------------+----------------------------------------+
| Title   | Message heading              | api.templates.deactivate_body.title    |
+---------+------------------------------+----------------------------------------+
| Info    | Message body                 | api.templates.deactivate_body.info     |
+---------+------------------------------+----------------------------------------+
| Warning | Warning text                 | api.templates.deactivate_body.warning  |
+---------+------------------------------+----------------------------------------+


SendInviteEmails
~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when team invite via email has been used.

**Body Props**:

+-----------+--------------------------------------------------------------------+----------------------------------------+
| Prop      | Content                                                            | i18n String                            |
+===========+====================================================================+========================================+
| SiteURL   | URL of the Mattermost server                                       | --                                     |
+-----------+--------------------------------------------------------------------+----------------------------------------+
| Title     | Message heading                                                    | api.templates.invite_body.title        |
+-----------+--------------------------------------------------------------------+----------------------------------------+
| Info1     | Message body                                                       | api.templates.invite_body.info         |
+-----------+--------------------------------------------------------------------+----------------------------------------+
| Button    | Button for confirmation                                            | api.templates.invite_body.button       |
+-----------+--------------------------------------------------------------------+----------------------------------------+
| ExtraInfo | Additional info about Mattermost                                   | api.templates.invite_body.extra_info   |
+-----------+--------------------------------------------------------------------+----------------------------------------+
| TeamURL   | URL to the team the user has been invited to                       | --                                     |
+-----------+--------------------------------------------------------------------+----------------------------------------+
| Link      | URL for team invite confirmation (not to be confused with TeamURL) | --                                     |
+-----------+--------------------------------------------------------------------+----------------------------------------+


NotificationEmailBody
~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user as a notification for new messages or mentions.

**Body Props**:

+----------+------------------------------+---------------------------------+
| Prop     | Content                      | i18n String                     |
+==========+==============================+=================================+
| SiteURL  | URL of the Mattermost server | --                              |
+----------+------------------------------+---------------------------------+
| Button   | Button to post               | api.templates.post_body.button  |
+----------+------------------------------+---------------------------------+
| TeamLink | URL to Team                  | --                              |
+----------+------------------------------+---------------------------------+


This email can change depending on the settings and type of channel the notification is sent for.

**For group channels**:

**With full notification contents enabled**: 

+------------+------------------+-------------------------------------------------+
| Prop       | Content          | i18n String                                     |
+============+==================+=================================================+
| BodyText   | Message intro    | app.notification.body.intro.group_message.full  |
+------------+------------------+-------------------------------------------------+
| Info1      | Channel name     | app.notification.body.text.group_message.full   |
+------------+------------------+-------------------------------------------------+
| Info2      | Message contents | app.notification.body.text.group_message.full2  |
+------------+------------------+-------------------------------------------------+
| SenderName | Name of sender   | --                                              |
+------------+------------------+-------------------------------------------------+


**Without**:

+----------+---------------+----------------------------------------------------+
| Prop     | Content       | i18n String                                        |
+==========+===============+====================================================+
| BodyText | Message intro | app.notification.body.intro.group_message.generic  |
+----------+---------------+----------------------------------------------------+
| Info     | Timestamp     | app.notification.body.text.group_message.generic   |
+----------+---------------+----------------------------------------------------+


**For direct messages**:

**With full notification contents enabled**: 

+------------+---------------------------+-----------------------------------------+
| Prop       | Content                   | i18n String                             |
+============+===========================+=========================================+
| BodyText   | Message intro             | app.notification.body.intro.direct.full |
+------------+---------------------------+-----------------------------------------+
| Info1      | Empty for direct messages | --                                      |
+------------+---------------------------+-----------------------------------------+
| Info2      | Message contents          | app.notification.body.text.direct.full  |
+------------+---------------------------+-----------------------------------------+
| SenderName | Name of sender            | --                                      |
+------------+---------------------------+-----------------------------------------+


**Without**:

+----------+---------------+--------------------------------------------+
| Prop     | Content       | i18n String                                |
+==========+===============+============================================+
| BodyText | Message intro | app.notification.body.intro.direct.generic |
+----------+---------------+--------------------------------------------+
| Info     | Timestamp     | app.notification.body.text.direct.generic  |
+----------+---------------+--------------------------------------------+


**Notifications**:

**With full notification contents enabled**: 

+------------+------------------+-----------------------------------------------+
| Prop       | Content          | i18n String                                   |
+============+==================+===============================================+
| BodyText   | Message intro    | app.notification.body.intro.notification.full |
+------------+------------------+-----------------------------------------------+
| Info1      | Channel name     | app.notification.body.text.notification.full  |
+------------+------------------+-----------------------------------------------+
| Info2      | Message contents | app.notification.body.text.notification.full2 |
+------------+------------------+-----------------------------------------------+
| SenderName | Name of sender   | --                                            |
+------------+------------------+-----------------------------------------------+


**Without**:

+----------+------------------------------+--------------------------------------------------+
| Prop     | Content                      | i18n String                                      |
+==========+==============================+==================================================+
| BodyText | URL of the Mattermost server | app.notification.body.intro.notification.generic |
+----------+------------------------------+--------------------------------------------------+
| Info     | Message heading              | app.notification.body.text.notification.generic  |
+----------+------------------------------+--------------------------------------------------+
