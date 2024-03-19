Log out of Mattermost
=====================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

You can log out of Mattermost from your profile picture. Select **Log Out** to log out of all teams on the server.

.. tab:: Web/Desktop

  .. image:: ../images/profile-log-out.png
    :alt: Log out of Mattermost from your profile picture.

.. tab:: Mobile

  .. image:: ../images/profile-log-out-mobile.png
    :width: 300
    :alt: Log out of Mattermost from your profile picture.

Frequently asked questions
--------------------------

What happens when I log out of Mattermost?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you log out of Mattermost, all data related to your session is removed except a record in the app database of the server you accessed and general activity state information, such as the onboarding checklist. Your user data stored within the server database is deleted when you log out. If you were to delete the Mattermost desktop and the mobile app, the most recent server URL and state data would also be deleted.

When you log out, the following additional data is also deleted:
- All push notifications from that server.
- The websocket, network, and analytics clients stored locally in memory.
- All cookies for the server URL.
- The image cache for all servers (not just the server you've logged out of).
- All files saved in the cache directory for that server.
- All thumbnails and data saved to the clipboard for all servers (not just the server you've logged out of).
- The ``image_cache`` cache directory (Android mobile app)