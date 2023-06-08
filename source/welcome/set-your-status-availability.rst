Set your status and availability
=================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Let your team know whether you're available by setting a custom status and your availability in Mattermost. 

Set a custom status
--------------------

Set a custom status to display a descriptive status message and optional emoji next to your name in Mattermost. Other members can see your status anywhere they can see your name, such as the channel sidebar and in conversations. 

To set a custom status in Mattermost:

.. tabs::

  .. tab:: Desktop

    1. Select your profile picture, then select **Set a custom status**.
    2. Choose from a list of suggested statuses, or enter a new emoji and status. The Speech bubble emoji 💬  is used by default if you don't specify an emoji. A custom status can be a maximum of 100 characters in length.
    3. Specify when to clear your custom status.
    4. Select **Set Status**.

  .. tab:: Mobile

    1. Select your profile picture, then selecting **Set a status**.
    2. Choose from a list of suggested statuses, reuse a recent status, or tap to enter a status and select an emoji. The Speech bubble emoji 💬  is used by default if you don't specify an emoji. A custom status can be a maximum of 100 characters in length.
    3. Specify when to clear your custom status.
    4. Tap **Done**. 

.. tip::

  - Custom statuses are enabled by default in Mattermost. System admins can disable this feature by going to **System Console > Site Configuration > Users and Teams > Enable Custom Statuses**. Disabling this feature also removes the "Update your status" prompts in Mattermost.

Clear a custom status
------------------------

To clear a custom status, select your profile picture, then select **Clear Status**, or select the **Clear** option next to your current status.

.. image:: ../images/clear-custom-status.png
  :alt: Clear your custom status.

Set your availability
---------------------

To set your availability, select your profile picture, then specify your availability as  **Online**, **Away**, **Do Not Disturb**, or **Offline**.

.. image:: ../images/set-your-availability.png
  :alt: Set your availability to online, away, do not disturb, or offline.

Other members can see your availability anywhere they can see your name, such as the channel sidebar, within conversations, and within Direct Messages.

Set your availability as Do Not Disturb
---------------------------------------

Set your availability to **Do Not Disturb** to disable all desktop, email, and push notifications when you are unavailable or need to concentrate. 

You can specify how long to disable notifications by selecting a preset expiration or setting a custom expiration. Your availability setting automatically reverts to its previous setting once the expiration is reached (this may take up to five minutes).

How Mattermost determines your availability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "Client", "**Online**", "**Away**", "**Offline**"

    "**Desktop App**", "You're interacting with your computer", "You've been inactive on your computer for five minutes", "You close Mattermost, sleep, or lock your computer"
    "**Web Browser**", "You're interacting with Mattermost in a browser", "
    - You have not typed or navigated between channels for five minutes
    - The tab is unfocused for five minutes
    - The browser is in the background or minimized for five minutes", "You close the Mattermost browser window"
    "**Mobile App**", "Mattermost is open", "Mattermost is open with five minutes of inactivity", "You change apps, close Mattermost, or lock your screen" 
