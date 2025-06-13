Display channel headers
=======================

.. include:: ../_static/badges/ent-adv-cloud-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v10.9, users with admin permissions can enable channel banners to remind channel members about being diligent to avoid data spillage in channels that aren't intended for classified or sensitive information. These non-dismissible banners are visible across all Mattermost clients, including web browsers, the desktop app, and the mobile app.

Mattermost :ref:`channel admins <collaborate/learn-about-roles:channel admin>`, :ref:`team admins <collaborate/learn-about-roles:team admin>`, and :ref:`system admins <collaborate/learn-about-roles:system admin>` can enable a banner with custom text at the top of Mattermost public or private channels. Banner text can also include :ref:`Markdown formatting <collaborate/format-messages:use markdown>`. 

Create a channel banner:

1. Open a channel where you have administrative permissions.
2. Select the channel name at the top of the center pane to access the drop-down menu, then select **Channel Settings**.
3. Select **Configuration** and enable the **Channel Banner** option.
4. Specify the banner text you want to display at the top of the channel, and the banner color preferred.
5. Select **Save** to apply the changes. The banner displays immediate.

Change a channel banner
------------------------

You can change the banner text or banner color at any time by following the same steps as above. The new banner text or color displays immediately.

Remove a channel banner
-------------------------

Disable the **Channel Banner** option in the channel settings to remove the banner from the channel.

.. tip::

  System admins can grant any user the ability to create and manage channel banners by assigning the **Manage Channel Banners** permission in the System Console. See the :doc:`advanced permissions </onboard/advanced-permissions>` documentation for details.