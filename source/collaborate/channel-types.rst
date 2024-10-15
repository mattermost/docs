Channel types
=============

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Channels are used to organize conversations across different topics. Find available channels in the left-hand panel. There are four types of channels: public channels, private channels, direct messages, and group messages. Enterprise system administrators can also configure channels as :ref:`read-only <onboard/advanced-permissions:read only channels>`.

Sending messages, replying to messages, and participating in conversation threads are important ways to keep conversations active with your team. See the following topics to learn more about working with channels.

Public channels
---------------

Public channels are open to everyone on a team and are identified with a **Globe** |globe| icon. New team members are automatically added to two public channels when they sign up: **Town Square** and **Off-Topic**.

See the :doc:`Join and leave channels </collaborate/join-leave-channels>` documentation for details on discovering and joining other channels.

Private channels
----------------

Private channels are for sensitive topics and are only visible to selected team members. Private channels are identified with a **Lock** |lock| icon. In Team Edition, any member of a private channel can add or remove other members from private channels, but in other Mattermost versions these permissions can be restricted to the channel admins and system admins.

Channel members can choose to leave private channels at any time.

Direct messages
---------------

Direct messages conversations between 2 people. You can start a direct message with people on other teams :ref:`unless the system admin has disabled your ability to do so <configure/site-configuration-settings:enable users to open direct message channels with>`. Only members of the conversation can see direct messages and channel heading information, including the last active status of the other user. 

Direct messages increment the numbered badge and trigger a notification unless the direct message is muted, or your notifications are disabled. See the :doc:`notification documentation </preferences/manage-your-notifications>` for details on customizing notifications based on your preferences.

.. note::

  - From Mattermost v10, when sending a direct message, Mattermost warns you that the recipient's availability is set to :ref:`Do Not Disturb <preferences/set-your-status-availability:set your availability>`, and when the recipient's local time is outside of regular business hours (between 10PM and 6AM). This warning displays directly above the message text field.
  
  - Any message history you have with a deactivated user remains available :ref:`unless your system admin disables your ability to do so <configure/site-configuration-settings:allow users to view archived channels>`.

Group messages
--------------

Group messages are conversations between 3 to 7 people. You can also start a group message with people on other teams when :ref:`unless the system admin has disabled your ability to do so <configure/site-configuration-settings:enable users to open direct message channels with>`. Only members of the conversation can see group messages. Group messages always display a new message badge.

From Mattermost v9.1, group messages increment the numbered badge and trigger a notification unless the direct message is muted, or your notifications are disabled. You can control how you're notified about group message conversations by going to **Settings > Notifications**. See the :doc:`notification documentation </preferences/manage-your-notifications>` to learn more.

.. note::

   - Want to have a group conversation with more than 7 people? You can :doc:`create a private channel </collaborate/create-channels>`. Alternatively, from Mattermost v9.1, you can :doc:`convert the group message to a private channel </collaborate/convert-group-messages>`.
  
   - Any group message history you have with a deactivated user remains available :ref:`unless your system admin disables your ability to do so <configure/site-configuration-settings:allow users to view archived channels>`.