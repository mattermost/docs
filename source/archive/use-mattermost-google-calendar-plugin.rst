Use the Mattermost Google Calendar plugin
=========================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

:doc:`The Mattermost Google Calendar plugin </about/mattermost-google-calendar-integration>` enables you to manage events using a two-way integration between Mattermost and Google Calendar without leaving Mattermost.

.. note..

  Your system admin needs to :doc:`set up this plugin </about/setup-mattermost-google-calendar-plugin>` before you can use it to manage your Google Calendar in Mattermost.

Connect your Google Calendar account to Mattermost
---------------------------------------------------

To use the Mattermost Google Calendar plugin, you must connect your Google Calendar account to Mattermost. You only need to complete this step once.

1. Log into Mattermost using your credentials.
2. Enter the Mattermost slash command ``/gcal connect`` in the message text field, and select **Send**.
3. When prompted, select the link to open a new browser window and connect your Google Calendar account to Mattermost.
4. Choose your Google account and enter your Google credentials if you're not already logged in.
5. Select **Allow**.

Mattermost will tell you when you’ve successfully connected your account. You can close the browser window and return to Mattermost.

Customize your Google Calendar plugin
---------------------------------------

Mattermost prompts you to configure the plugin based on your personal preferences with the following options. You only need to complete this step once.

- **Update status**: The plugin can update :ref:`your Mattermost availability <preferences/set-your-status-availability:set your availability>` when you have an event scheduled.
- **Get Confirmation**: You can manually confirm every availability change, or the plugin can update your availability automatically.

  - If you select **Yes**, Mattermost confirms your availability update 5 minutes before each event starts. You'll also be prompted to change your availability back to **Online** once an event ends.
  - Select **No** to enable the plugin to update your availability automatically.

- **Receive notifications during meetings**: During an event, your availability can be set to **Away** or **No Not Disturb** when you’re in a meeting. 

  - Set your availability to **Away** to clearly communicate to others in Mattermost that you're unavailable. You'll continue to receive desktop, email, and push notifications based on your Mattermost notification preferences.
  - Set your availability to :ref:`Do Not Disturb <preferences/set-your-status-availability:set your availability as do not disturb>`  to disable all desktop, email, and push notifications.

- **Receive reminders**: You can choose to receive an event reminder 5 minutes before a meeting in a direct message.

- **Daily summary**: You can get a daily summary of your events delivered in a direct message.

Create a calendar event
-----------------------

1. Using a web browser or the desktop app, select a channel name to access additional channel options.
2. Select **Create calendar event**.
3. Specify a subject, date, start time, and end time for the event. You can optionally specify additional event details, including location, guest invitations, description, and a channel where event reminders will be posted.

4. Select **Create**.

  .. note:: 

    - You can invite guests to the event by username if they’ve already connected their Google Calendar account to the Mattermost server, or alternatively by their email address. 
    - Once you’ve invited guests to an event, guests must accept the event invitation to receive event reminders based on how they’ve customized their Google Calendar plugin preferences.
    - When you create an event, it's based on your timezone. Guests see event details based on their timezone in direct message reminders, but channel reminders display using the event creator's timezone. 

Review your upcoming events
---------------------------

You can use the following Mattermost slash commands to review your upcoming Google Calendar events without leaving Mattermost.

- See a summary of today's events by entering the slash command ``/gcal today`` in the message text field.
- See a summary of tomorrow's events by entering the slash command ``/gcal tomorrow`` in the message text field.
- See a summary of the week's events by entering the slash command ``/gcal viewcal`` in the message text field.
- Update your plugin preferences any time by entering the Mattermost slash command ``/gcal settings`` in the message text field.
