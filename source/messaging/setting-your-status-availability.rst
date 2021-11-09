Setting Your Status and Availability
====================================

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Let your team know whether you're available by setting a custom status and your availability in Mattermost.

Setting a custom status
-----------------------

.. tabs::

  .. tab:: Mattermost v6.0 onwards

      From Mattermost v6.0, set status and availability from your Avatar in the top-right corner of the Global Header.
      
  .. tab:: Mattermost v5.39 and earlier

      In Mattermost versions up to 5.39, set status and availability from your avatar at the top of the channel sidebar.
  
Set a custom status to add an optional emoji to a descriptive status message. Other members can see your status anywhere they can see your name, such as the channel sidebar and in conversations. 

.. tabs::

  .. tab:: Mattermost v6.0 onwards

     1. To set a custom status, select your Avatar in the top-right corner of the global header, then select **Set a Custom Status**.
     2. Choose from a list of suggested statuses, reuse a recent status, or enter a new emoji and status, then select **Set Status**. The Speech bubble emoji 💬  is used by default if you don't specify an emoji. A custom status can be a maximum of 100 characters in length.

  .. tab:: v5.39 and earlier

     1. To set a custom status, select your avatar at the top of the channel sidebar, then select **Set a Custom Status**.
     2. Choose from a list of suggested statuses, reuse a recent status, or enter a new emoji and status, then select **Set Status**. The Speech bubble emoji 💬  is used by default if you don't specify an emoji. A custom status can be a maximum of 100 characters in length.
 
.. note::

  - If custom statuses aren't available, you can request your System Admin to enable this feature in **System Console > Site Configuration > Users and Teams > Enable Custom Statuses**.
  - Custom statuses will be available in the Mattermost Mobile App in a future release. 

Clearing a custom status
------------------------

To clear a custom status, select your Avatar, then select **Clear Status**, or select the **Clear** option next to your current status.

.. image:: ../images/clear-custom-status.png
  :alt: Clear your custom status.

Setting your availability
-------------------------

To set your availability, select your Avatar, then specify your availability as  **Online**, **Away**, **Do Not Disturb**, or **Offline**.

.. image:: ../images/set-your-availability.png
  :alt: Set your availability to online, away, do not disturb, or offline.

Other members can see your availability anywhere they can see your name, such as the channel sidebar, within conversations, and within Direct Messages. 

Setting Do Not Disturb
----------------------

From Mattermost v6.1, set your availability to **Do Not Disturb** to disable all desktop, email, and push notifications when you are unavailable or need to concentrate. 

You can specify how long to disable notifications by selecting a preset expiration or setting a custom expiration. Your availability setting automatically reverts to its previous setting once the expiration is reached. It may take up to five minutes for your availability to revert to its previous setting.

How Mattermost determines your availability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
    :header: "Client", "**Online**", "**Away**", "**Offline**"

    "**Desktop App**", "You're interacting with your computer", "You're inactive on your computer for five minutes", "You close Mattermost, sleep, or lock your computer"
    "**Web Browser**", "You're interacting with Mattermost in a browser", "
    - You have not typed or switched channels for five minutes
    - The tab is unfocused for five minutes
    - The browser is in the background or minimized for five minutes", "You close the Mattermost browser window"
    "**Mobile App**", "Mattermost is open", "Mattermost is open with five minutes of inactivity", "You switch apps, close Mattermost, or lock your screen" 
    
