# Account Settings
___
Account Settings is accessible from the **Main Menu** by clicking the three dots at the top of the channels pane. From here, you can configure your profile settings, notification preferences, integrations, theme settings, and display options.

## General
Settings to configure name, username, nickname, email and profile picture.

#### Full Name
Full names appear in the Direct Messages member list and team management modal. By default, you will receive mention notifications when someone types your first name. Entering a full name is optional.

#### Username
Usernames appear next to all posts. Pick something easy for teammates to recognize and recall. By default, you will receive mention notifications when someone types your username. In order to maintain message integrity, changing your username does not update @mentions in messages already posted.  

#### Nickname
Nicknames appear in the Direct Messages member list and team management modal. You will not receive mention notifications when someone types your nickname unless you add it to the *Words That Trigger Mentions* in **Account Settings > Notifications**.

#### Email
Email is used for sign-in, notifications, and password reset. Email requires verification if changed. If you are signing in using a single sign-on service, the email field is not editable and you will receive email notifications to the email you used to sign up to your SSO service.

#### Profile Picture
Profile pictures appear next to all posts and in the top of the channels pane next to your name. All users have a generic profile picture when they sign up for an account. Edit your profile picture by clicking **Select** and then choosing a picture in either JPG or PNG format that’s at least 128px wide and 128px high. For best results, choose an image that is square with the subject of interest centered. If you edit your profile picture, all past posts will appear with the new picture.

## Security
Settings to configure your password, view access history, and view or logout of active sessions.

#### Password
You may change your password if you’ve logged in by email. If you are signing in using a single sign-on service, the password field is not editable, and you must access your SSO service’s account settings to update your password.

#### Sign-in Method 

Allows user to switch between single-sign-on option, such as GitLab authentication, and email authentication. 

#### View Access History
Access History displays a chronological list of the last 20 login and logout attempts, channel creations and deletions, account settings changes, or channel setting modifications made on your account. The details of the Session ID (unique identifier for each Mattermost browser session) and IP Address of the action is recorded for audit log purposes.

#### View and Logout of Active Sessions
Sessions are created when you log in with your email and password to a new browser on a device. Sessions let you use Mattermost for up to 30 days without having to log in again. Click **Logout** on an active session if you want to revoke automatic login privileges for a specific browser or device. Click **More Info** to view details on browser and operating system.

## Notifications
Settings to configure desktop notifications, desktop notification sounds, email notifications, and words that trigger mentions.

#### Send Desktop Notifications
Desktop notifications appear at the bottom right corner of your main monitor. The desktop notification preference you choose in *Account Settings* applies globally, but this preference is customizable for each channel from the channel name drop-down menu. Desktop notifications are available on Firefox, Safari, and Chrome.

#### Desktop Notification Sounds
A notification sound plays for all Mattermost posts that would fire a desktop notification, unless *Desktop Notification Sound* is turned off. Desktop notification sounds are available on Firefox, Safari, Chrome, Internet Explorer, and Edge.

#### Email Notifications
Email notifications are sent for mentions and direct messages after you’ve been offline for more than 60 seconds or away from Mattermost for more than 5 minutes. Change the email where notifications are sent from **Account Settings > General > Email**.

#### Words That Trigger Mentions
By default, you will receive mention notifications from your non-case sensitive username, mentioned @username and @channel. Customize the words that trigger mentions by typing them in the input box. This is useful if you want to be notified of all posts on a certain topic, for example, “marketing”.

## Integrations
Settings to configure incoming and outgoing webhooks for your team.

#### Incoming Webhooks
Incoming webhooks from external integrations can post messages to Mattermost in public channels or private groups. Learn more about setting up incoming webhooks on our [documentation page](http://docs.mattermost.com/developer/webhooks-incoming.html).


#### Outgoing Webhooks
Outgoing webhooks use trigger words to fire new message events to external integrations. For security reasons, outgoing webhooks are only available in public channels. Learn more about setting up outgoing webhooks on our [documentation page](http://docs.mattermost.com/developer/webhooks-outgoing.html).

## Display
Settings to configure clock and teammate name display preferences.

#### Theme 

Select **Theme Colors** to select from four standard themes designed by the Mattermost team. To make custom adjustments on the four standard theme colours, click a standard theme and then select **Custom Theme** to load the standard theme into the custom theme color selectors.

Select **Custom Theme** to customize your theme colors and share them with others by copying and pasting theme vectors into the input box. Observe a live preview as you customize theme colors and then click **Save** to confirm your changes. Discard your changes by clicking **Cancel** or by exiting the settings modal and clicking **Yes, Discard**.

Learn more about the custom theme color selectors [here](http://docs.mattermost.com/help/settings/theme-colors.html#custom-themes).

Select **Import theme colors from Slack** to import a Slack theme. In Slack, go to **Preferences > Sidebar Theme** and open the custom theme option. From there, copy the theme color vector and then paste it into the *Input Slack Theme* input box in Mattermost. Any theme settings that are not customizable in Slack will default to the “Mattermost” standard theme settings.

#### Display Font
Select what font is used.

#### Clock Display
Choose a 12-hour or 24-hour time preference that appears on the time stamp for all posts. 

#### Teammate Name Display
Configure how names are displayed in Mattermost: nickname, username or full name.

#### Language
Select what language Mattermost uses.  

## Advanced
Setting to configure when messages are sent.

#### Send Messages on Ctrl+Enter
If enabled, press **Enter** to insert a new line and **Ctrl + Enter** posts the message. If disabled, **Shift + Enter** inserts a new line and **Enter** posts the message.

#### Preview pre-release features
Turn on preview features to view them early, ahead of their official release:
- **Show markdown preview option in message input box:** Turning this on will show a "Preview" option when typing in the text input box. Pressing "Preview" shows what the Markdown formatting in the message looks like before the message is sent.
- **Show preview snippet of links below message:** Turning this on will show a preview snippet posted below links from select websites. 
