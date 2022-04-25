Announcement banner
===================

|enterprise| |professional| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Mattermost Enterprise Edition E10 and E20*

System Admins can display a notice that's visible to all users on the system via an announcement banner.

.. image:: ../images/announcement-banner-1106x272.png
  :width: 1106
  :height: 272
  :alt: Shows the announcement banner at the top of the user's screen.

By default, users can dismiss the banner until they log in again or until you update the banner. You can update the banner by either changing the text of the banner or by re-enabling the banner after it has been disabled. You can also control the text color and the background color. A setting in the System Console allows you to prevent users from dismissing the banner.

**To enable the banner**

1. Go to **System Console > Site Configuration**, then select **Announcement Banner**.
2. Set **Enable Announcement Banner** to **true**.
3. In the **Banner Text** field, enter the text of the announcement that you want to make.
4. Specify the background and text colors for the banner.
5. To prevent users from dismissing the banner, select **false** for **Allow Banner Dismissal**.
6. Select **Save**.
