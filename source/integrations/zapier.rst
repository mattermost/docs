Zapier and Mattermost
===================



Integrate Mattermost with over 500 supported apps on Zapier, including `GitHub <https://zapier.com/zapbook/github/>`_, `Jira <https://zapier.com/zapbook/jira/>`_, `Wufoo <https://zapier.com/zapbook/wufoo/>`_, `Salesforce <https://zapier.com/zapbook/salesforce/>`_, `Twitter <https://zapier.com/zapbook/twitter/>`_, `Gmail <https://zapier.com/zapbook/gmail/>`_ and `many more <https://zapier.com/zapbook/>`_. Zapier integration triggers new Mattermost messages for events in other apps. This documentation includes:

- `Zapier Setup Guide <https://docs.mattermost.com/integrations/zapier.html#zapier-setup-guide>`_ - **Instructions on registering the Zapier app on your server and creating a zap**
- `Message Formatting Tips <https://docs.mattermost.com/integrations/zapier.html#message-formatting-tips>`_ - **Tips from the Mattermost team on formatting Zapier integration messages**
- `Troubleshooting Guide <https://docs.mattermost.com/integrations/zapier.html#troubleshooting-guide>`_ - **Advice on troubleshooting common setup issues**


Zapier Setup Guide
--------------------------------
Zapier is authorized using OAuth2.0. The setup guide requires that a System Admin register the Zapier app on their Mattermost server and can then optionally allow any users on the system to create Zapier integrations.

Enable Zapier on your Mattermost Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The first time you set up Zapier on your Mattermost instance you will be required to enable an OAuth 2.0 application which can be accessible by everyone on your server. Your System Admin must execute these steps.

Enable OAuth 2.0
```````````````````````````
1. Go to the **Main Menu** > **System Console**
2. Under **Integrations** > **Custom Integrations**
  a. Set `Enable OAuth 2.0 Service Provider <https://docs.mattermost.com/administration/config-settings.html#enable-oauth-2-0-service-provider>`_ to **True**.
  b. If you’d like to allow Zapier integrations to post with customizable usernames and profile pictures, then set `Enable webhooks and slash commands to override usernames <https://docs.mattermost.com/administration/config-settings.html#enable-webhooks-and-slash-commands-to-override-usernames>`_ and `Enable webhooks and slash commands to override profile picture icons <https://docs.mattermost.com/administration/config-settings.html#enable-webhooks-and-slash-commands-to-override-profile-picture-iconss>`_ to **True**.
  c. If you’d like to allow users on your system who are not Team or System Admins to create Zapier integrations, then set `Restrict creating integrations to Team and System Admins <https://docs.mattermost.com/administration/config-settings.html#restrict-creating-integrations-to-team-and-system-admins>`_ to **False**.

Register Zapier as an OAuth 2.0 Application
````````````````````````````````````````````````````````````````
1. Go to **Main Menu** > **Integrations**
2. Click **OAuth 2.0 Applications**, then click **Add OAuth 2.0 Application** and enter the following fields:
  a. **Is Trusted**: Yes
  b. **Display Name**: ``Zapier``
  c. **Description**: ``Application for Zapier integrations``
  d. **Homepage**: ``https://zapier.com/``
  e. **Icon URL**: ``http://bit.ly/2bxrzv0``
  f. **Callback URLs**: ``https://zapier.com/dashboard/auth/oauth/return/App27274API/``
3. Click **Save** to create the application. You will be provided with a **Client ID** and **Client Secret**. Save these values to connect Zapier in the steps below.

.. image:: ../images/zapier-oauth.png


Create your First Zap
~~~~~~~~~~~~~~~~~~~~~~~~~
1. XXXXXX how does this step work with the link to an "Invite only" app? Need to test.
2. **Trigger App**: Events in this app will trigger new messages in Mattermost.
  a. **Select a Trigger App** or choose from one of Zapier’s built-in apps that will trigger new messages in Mattermost. If the app you’re looking to connect isn’t supported on Zapier, consider firing in-app events to a Gmail account and then connecting Gmail to Mattermost using Zapier.
  b. **Select the Trigger Event**. New messages in Mattermost will fire depending on these selected events in conjunction with any filters you apply.
  c. **Connect the Trigger Account**. Connect the account from which you’d like to trigger events and **Test** it to ensure Zapier can connect successfully.
3. **Filtering** (Optional): Exclude certain events from triggering new messages. Learn more about using `Zapier custom filtering <https://zapier.com/learn/how-to-use-zapier/custom-filters/>`_.
  a. Add a filter by clicking the small **+** icon before the **Action** step.
  b. Zapier supports **AND** and **OR** filters. Use the dropdown selectors to choose what events will allow the trigger to send a Mattermost message.
4. **Mattermost Action**: Connect your Mattermost Account and then specify posting details.
  a. **Select the Action App**. Search for “Mattermost” XXXXXX how does this work with invite only?
  b. **Select the Action Event**. Select **Post a Message**. The Mattermost team plans to expand the actions available here.
  c. **Connect the Action Account**. Click **Connect a New Account** and enter the following fields:
    1. **Mattermost URL**: This is the URL you use to access your Mattermost site. Do not include a slash at the end of the URL and do not append a team to the end of the server URL. For example, ``https://pre-release.mattermost.com/core`` is the entire URL to the Contributors team on our pre-release server. The **Mattermost URL** entered here would be ``https://pre-release.mattermost.com``.
    2. **Client ID/Secret**: These values were obtained in Step 4 in the section above. If Zapier has been enabled as an OAuth applications as per the steps above, then these values can also be found by navigating to one of your Mattermost teams, then **Main Menu** > **Integrations** > **OAuth 2.0 Applications**. Click **Show Secret** next to the Zapier app, then obtain the Client ID and Client Secret. 
    3. **Login to Mattermost**. After completing the above fields you will be prompted to login to your Mattermost account if you are not logged in already. If you’re having trouble connecting then please read our `troubleshooting guide <https://docs.mattermost.com/integrations/zapier.html#troubleshooting-guide>`_. 
  d. **Message Post Details**: Specify the formatting of the messages and the team/channel where messages will post.
    1. **Team**: Choose the team where new messages will post. The dropdown should contain all teams you have access to on Mattermost.
    2. **Channel**: Choose the channel where new messages will post. Zapier cannot post into Direct Message channels, but all other Channels and Private Groups should appear in the dropdown.
    3. **Message Text**: Enter the message text that will post to Mattermost. This text can be formatted using `Markdown <https://docs.mattermost.com/help/messaging/formatting-text.html>`_ and include the dynamic fields offered by your selected trigger app. Read our `message formatting tips <https://docs.mattermost.com/integrations/zapier.html#message-formatting-tips>`_ below.
    
      .. image:: ../images/zapier-dynamic-fields.png    
    
    4. **Username**: This is the username that Zapier will post as. Zapier integrations will always appear with a ``BOT`` tag next to the username.
    5. **Icon URL**: This is the profile picture of the bot that Zapier will post as.
  e. **Test the Zap**: You may want to test your zap formatting in a Private Group before posting in a channel that is visible to your entire team.
 
-----------

Message Formatting Tips
--------------------------------------

Here are some useful tips we recommend to get the most out of Zapier integration:

- **Markdown**: Mattermost supports the use of `Markdown. <https://docs.mattermost.com/help/messaging/formatting-text.html>`_ in Zapier integrations. For example, use `heading markdown <https://docs.mattermost.com/help/messaging/formatting-text.html#headings>`_ for JIRA issue titles. 
- **Custom Icons**: Use different icons for different services and Zapier integrations.
- **Hashtags**: Use hashtags to make your Zapier posts searchable. Use different hashtags for different services and Zapier integrations. For example, use the dynamic fields available in Zapier to include ticket a JIRA ticket number in hashtags. This makes all conversation on a specific ticket instantly searchable by clicking the hashtag.
- **Quick Links**: Link back to the service that fired the zap through the use of Markdown `embedded links <https://docs.mattermost.com/help/messaging/formatting-text.html#links>`_. For example, in our zaps we embed a link back to the service within the timestamp so it’s easy to take action on any zap.

Examples
~~~~~~~~~~~~~

The Mattermost team has over 50 zaps integrated on our `Pre-Release Contributors team <https://pre-release.mattermost.com/core/>`_ used for internal communication and interacting with contributors. The `Community Heartbeat channel <https://pre-release.mattermost.com/core/channels/community-heartbeat>`_ integrates all our community services in one accessible location. These zaps are formatted in two ways depending on the service:

**GitHub Issues & Comments, UserVoice Suggestions & Comments, GitLab MM Issues, GitLab Omnibus MM Issues:**
 
.. code:

#### [Title of issue]  

#[searchable-hashtag] in [external service](link to service) by [author](link to author profile) on [time-stamp](link to specific issue or comment) 

[Body of issue or comment]

.. image:: ../images/zapier-ch1.png


**Forum Posts, Jira Comments, Hacker News Mentions, Tweets:**

.. code:

> [forum post, media mention, or tweet]  

#[searchable-hashtag] in [external service](link to service) by [author](link to author profile) on [time-stamp](link to specific forum post, media mention or tweet)
```

.. image:: ../images/zapier-ch2.png

-----------
