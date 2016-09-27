Zapier Integration
===================

`Zapier <https://zapier.com/>`_ is a service that automates tasks between web apps. You can create zaps that contains a trigger and an action for a task that you want to perform repeatedly. Zapier regularly checks your trigger for new data and automatically performs the action for you.

Integrate Mattermost with over 500 supported apps on Zapier, including `GitHub <https://zapier.com/zapbook/github/>`_, `Jira <https://zapier.com/zapbook/jira/>`_, `Wufoo <https://zapier.com/zapbook/wufoo/>`_, `Salesforce <https://zapier.com/zapbook/salesforce/>`_, `Twitter <https://zapier.com/zapbook/twitter/>`_, `Gmail <https://zapier.com/zapbook/gmail/>`_ and `many more <https://zapier.com/zapbook/>`_. Zapier integrations trigger new Mattermost messages for events in other apps. This documentation includes:

- `Zapier Setup Guide <https://docs.mattermost.com/integrations/zapier.html#id1>`_ - **Instructions on registering the Zapier app on your server and creating a zap**
- `Message Formatting Tips <https://docs.mattermost.com/integrations/zapier.html#id4>`_ - **Tips from the Mattermost team on formatting Zapier integration messages**
- `Troubleshooting Guide <https://docs.mattermost.com/integrations/zapier.html#id6>`_ - **Advice on troubleshooting common setup issues**


Zapier Setup Guide
--------------------------------
Zapier is authorized using OAuth2.0. The setup guide requires that a System Admin register the Zapier app on their Mattermost server and can then optionally allow any users with a Zapier account to create integrations.

Enable Zapier on your Mattermost Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The first time you set up Zapier on your Mattermost instance you will be required to enable an OAuth 2.0 application which can be used by everyone on your server. Your System Admin must execute these steps.

Enable OAuth 2.0
```````````````````````````
1. Go to the **Main Menu** > **System Console**
2. Under **Integrations** > **Custom Integrations**
  a. Set `Enable OAuth 2.0 Service Provider <https://docs.mattermost.com/administration/config-settings.html#enable-oauth-2-0-service-provider>`_ to **True**.
  b. If you’d like to allow Zapier integrations to post with customizable usernames and profile pictures, then set `Enable integrations to override usernames <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-usernames>`_ and `Enable integrations to override profile picture icons <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-profile-picture-iconss>`_ to **True**.

Register Zapier as an OAuth 2.0 Application
````````````````````````````````````````````````````````````````
1. Go to **Main Menu** > **Integrations**
2. Click **OAuth 2.0 Applications**, then click **Add OAuth 2.0 Application** and enter the following fields:
  a. **Is Trusted**: No
  b. **Display Name**: ``Zapier``
  c. **Description**: ``Application for Zapier integrations``
  d. **Homepage**: ``https://zapier.com/``
  e. **Icon URL**: ``http://bit.ly/2bxrzv0``
  f. **Callback URLs**: ``https://zapier.com/dashboard/auth/oauth/return/MattermostDevAPI/``
3. Click **Save** to create the application. You will be provided with a **Client ID** and **Client Secret**. Save these values, or share them with your team to connect Zapier in the steps below.

.. image:: ../images/zapier-oauth.png


Create a Zap
~~~~~~~~~~~~~~~~~~~~~~~~~
1. `Sign up <https://zapier.com/sign-up/>`_ for a free Zapier account or `login <https://zapier.com/app/login>`_ if you already have one.
2. On your `Zapier dashboard <https://zapier.com/app/dashboard>`_ click **Make a Zap!**.
3. **Trigger App**: Events in this app will trigger new messages in Mattermost.
  a. **Select a Trigger App** that will trigger new messages in Mattermost. If the app you’re looking to connect isn’t supported on Zapier, consider firing in-app events to a Gmail account and then connecting Gmail to Mattermost using Zapier.
  b. **Select the Trigger Event**. New messages in Mattermost will fire depending on these selected events in conjunction with any filters you apply.
  c. **Connect the Trigger Account**. Connect the account from which you’d like to trigger events and **Test** it to ensure Zapier can connect successfully.
4. **Filtering** (Optional): Exclude certain events from triggering new messages. Learn more about using `Zapier custom filtering <https://zapier.com/learn/how-to-use-zapier/custom-filters/>`_.
  a. Add a filter by clicking the small **+** icon before the **Action** step.
  b. Zapier supports **AND** and **OR** filters. Use the dropdown selectors to choose what events will allow the trigger to send a Mattermost message.
5. **Mattermost Action**: Connect your Mattermost Account and then specify posting details.
  a. **Select the Action App**. Search for “Mattermost”.
  b. **Select the Action Event**. Select **Post a Message**. The Mattermost team plans to expand the actions available here.
  c. **Connect the Action Account**. Click **Connect a New Account** and enter the following fields:
    1. **Mattermost URL**: This is the URL you use to access your Mattermost site. Do not include a slash at the end of the URL and do not append a team to the end of the server URL. For example, ``https://pre-release.mattermost.com/core`` is the entire URL to the Contributors team on our pre-release server. The **Mattermost URL** entered here would be ``https://pre-release.mattermost.com``.
    2. **Client ID/Secret**: If Zapier has been enabled as an OAuth application as per the steps above, then these values can be found by navigating to one of your Mattermost teams, then **Main Menu** > **Integrations** > **OAuth 2.0 Applications**. Click **Show Secret** next to the Zapier app, then obtain the Client ID and Client Secret. 
    3. **Login to Mattermost**. After completing the above fields you will be prompted to login to your Mattermost account if you are not logged in already. If you’re having trouble connecting then please read our `troubleshooting guide <https://docs.mattermost.com/integrations/zapier.html#id6>`_. 
    4. You'll then be prompted to allow Zapier to access your Mattermost account. Click **Allow**.
  d. **Message Post Details**: Specify the formatting of the messages and the team/channel where messages will post.
    1. **Team**: Choose the team where new messages will post. The dropdown should contain all teams you have access to on Mattermost.
    2. **Channel**: Choose the channel where new messages will post. The dropdown will contain all Public Channels and Private Groups that you belong to. Zapier cannot post into Direct Message channels.
    3. **Message Text**: Enter the message text that will post to Mattermost. This text can be formatted using `Markdown <https://docs.mattermost.com/help/messaging/formatting-text.html>`_ and include the dynamic fields offered by your selected trigger app. Read our `message formatting tips <https://docs.mattermost.com/integrations/zapier.html#id4>`_ below.
    
      .. image:: ../images/zapier-dynamic-fields.png    
    
    4. **Username**: This is the username that Zapier will post as. Zapier integrations will always appear with a ``BOT`` tag next to the username. In order for bots to override the username of the authorized user, your System Admin must set `Enable integrations to override usernames <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-usernames>`_ to **True**.
    5. **Icon URL**: This is the profile picture of the bot that Zapier will post as. In order for bots to override the profile picture of the authorized user, your System Admin must set `Enable integrations to override profile picture icons <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-profile-picture-iconss>`_ to **True**.
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

**GitHub Issues and Comments, UserVoice Suggestions and Comments, GitLab MM Issues, GitLab Omnibus MM Issues:**
 
.. code::

    #### [Title of issue]  

    #[searchable-hashtag] in [external service](link to service) by [author](link to author profile) on [time-stamp](link to specific issue or comment) 

    [Body of issue or comment]

.. image:: ../images/zapier-ch1.png


**Forum Posts, Jira Comments, Hacker News Mentions, Tweets:**

.. code::

     > [forum post, media mention, or tweet]  

     #[searchable-hashtag] in [external service](link to service) by [author](link to author profile) on [time-stamp](link to specific forum post, media mention or tweet)

.. image:: ../images/zapier-ch2.png

-----------

Troubleshooting Guide
--------------------------------
Possible solutions to common issues encountered during setup.

Cannot connect a Mattermost account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **"Token named access_token was not found in oauth response!"**
  a. Possible Solution: Try removing any trailing ``/``'s on the end of your **Mattermost URL**.
    - Correct: ``https://pre-release.mattermost.com``
    - Incorrect: ``https://pre-release.mattermost.com/``
  
    .. image:: ../images/zapier-error1.png
  
2. **"[Server URL] returned (404)"**
  a. Possible Solution: The **Mattermost URL** cannot have a team appended to the end of the server URL.
    - Correct: ``https://pre-release.mattermost.com``
    - Incorrect: ``https://pre-release.mattermost.com/core``

  .. image:: ../images/zapier-error2.png

3. **"[Server URL] returned (500) Internal Server Error"**
  a. Possible Solution: The **Client Secret** might be incorrect. Verify this value in **Main Menu** > **Integrations** > **OAuth 2.0 Applications**, or check with your System Admin.
  
  .. image:: ../images/zapier-error4.png

4. **"Mattermost needs your help: We couldn't find the requested app"**
  a. Possible Solution: The **Client ID** might be incorrect. Verify this value in **Main Menu** > **Integrations** > **OAuth 2.0 Applications**, or check with your System Admin.

  .. image:: ../images/zapier-error3.png

Post Error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **"We hit an error creating a post message."**
  a. Possible Solution: Ensure your **Message Text** is less than 4000 characters, since that is the maximum character limit for any single message in Mattermost.
  
  .. image:: ../images/zapier-error5.png

Deauthorize the Zapier App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. If you'd like to deauthorize Zapier so it can no longer post through your connected account, go to **Account Settings** > **Security** > **OAuth 2.0 Applications**, then click **Deauthorize** on the Zapier app.

.. image:: ../images/zapier-deauthorize.png
