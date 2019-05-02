Email Templates
====================

Mattermost has a few email templates that are sent out when a specific event occurs.
Most of the time these templates do not need to be modified.
In case additional modifications are necessary, all available props in each email are listed below.  

The email templates are located in the Mattermost server directory in the ``templates`` folder.

.. note::
  The props between different email templates are not interchangable without additional server code changes.


Available templates
------------------------


SendChangeUsernameEmail
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when username has been changed.

**Body Props**:
 - SiteURL: URL of the Mattermost server
 - Title: Message heading
 - Info: Message body
 - Warning: Warning Text


SendEmailChangeVerifyEmail
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when email change has been requested. Contains verification link and button.

**Body Props**:
 - SiteURL: URL of the Mattermost server
 - Title: Message heading
 - Info: Message body
 - VerifyUrl: Link for Verification
 - VerifyButton: Button for Verification


SendEmailChangeEmail
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when email has been changed succesfully.

**Body Props**:
 - SiteURL: URL of the Mattermost server
 - Title: Message heading
 - Info: Message body
 - Warning: Warning Text


SendVerifyEmail
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user upon account creation to verify email address.

**Body Props**:
 - SiteURL: URL of the Mattermost server
 - Title: Message heading
 - Info: Message body
 - VerifyUrl: Link for Verification
 - Button: Button for confirmation


SendSignInChangeEmail
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when sign-in method has been changed (i.e. from email to LDAP, etc.)

**Body Props**:
 - SiteURL: URL of the Mattermost server
 - Title: Message heading
 - Info: Message body
 - Warning: Warning Text


SendWelcomeEmail
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when account has been created. May also contain download links to Apps as well as email verification links.

**Body Props**:
 - SiteURL: URL of the Mattermost server
 - Title: Message heading
 - Info: Message body
 - Button: Button for confirmation
 - Info2: Continuation of message body
 - Info3: Continuation of message body

Optional Props:
 - AppDownloadInfo
 - AppDownloadLink
 - VerifyUrl: Link for Verification


SendPasswordChangeEmail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when password has been changed.

**Body Props**:
 - SiteURL: URL of the Mattermost server
 - Title: Message heading
 - Info: Message body
 - Warning: Warning Text


SendAccessTokenEmail
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when an access token has been added to the account.

**Body Props**:
 - SiteURL: URL of the Mattermost server
 - Title: Message heading
 - Info: Message body
 - Warning: Warning Text


SendPasswordResetEmail
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when password request has been initiated.

**Body Props**:
 - SiteURL: URL of the Mattermost server
 - Title: Message heading
 - Info1: Message body
 - Info2: Continuation of message body
 - ResetUrl: Url to reset password
 - Button: Button for confirmation


SendMfaChangeEmail
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when multi-factor authentication method has been changed.

**Body Props**:
 - SiteURL: URL of the Mattermost server
 - Info: Message body
 - Title: Message heading
 - Warning: Warning Text


SendDeactivateAccountEmail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when account has been deactivated.

**Body Props**:
 - SiteURL: URL of the Mattermost server
 - ServerURL: 
 - Title: Message heading
 - Info: Message body
 - Warning: Warning Text


SendInviteEmails
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Purpose**:
Sent to the user when team invite via email has been used.

**Body Props**:
 - SiteURL: URL of the Mattermost server
 - Title: Message heading
 - Info: Message body
 - Button: Button for confirmation
 - ExtraInfo: Additional info about Mattermost
 - TeamURL: URL to the team the user has been invited to
 - Link: URL for team invite confirmation (not to be confused with TeamURL)
