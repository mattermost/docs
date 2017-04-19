Video and Audio Calling (Beta)
=====================================

Mattermost supports an early preview of video and audio calling option using a self-hosted proxy. The implementation is based on WebRTC integration enabling one-on-one video and audio calling within a browser without needing additional software to be installed.

The feature is a working prototype for community development and not recommended for production. It has been tested on Chrome and Firefox running on Mac and Windows and the Mattermost Mac and Windows Apps using a Mattermost server running in SSL mode.

.. note:: This feature will be replaced by a plug-in architecture allowing multiple video and audio calling providers to connect into Mattermost, and features described in this section will be re-written as a plug-in. 

Configuring video and audio calls
------------------------------------------

This option can be enabled by the System Administrator in the System Console under **Integrations > WebRTC (Beta)** - `see configuration settings documentation to learn more <https://docs.mattermost.com/administration/config-settings.html#webrtc-beta>`_.

To set up the WebRTC server, you may either

 - use a `Mattermost docker container created for testing WebRTC <https://hub.docker.com/r/mattermost/webrtc/>`_
 - set up a `Janus server <https://github.com/meetecho/janus-gateway>`_ to act as the WebRTC gateway and `Coturn <https://github.com/coturn/coturn/wiki>`_ for STUN and TURN servers for your Mattermost installation.

Starting a video call
--------------------------

After enabling the feature in the System Console by a System Administrator:

1. Go to **Account Settings > Advanced > Preview pre-release features** and select **Enable the ability to make and receive one-on-one WebRTC calls**.

2. Initiate a call with another user by either:

    Clicking the video icon on a user's profile popover, which appears after clicking their profile picture or name on the center channel or right hand sidebar

    .. image:: ../images/webrtc-popover.png

    Clicking the video icon on the channel header of a direct message channel with that user

    .. image:: ../images/webrtc-header.png

Troubleshooting
--------------------------

As noted previously, video and audio calls are intended as a working prototype for community development and not recommended for production.

To review a list of open video and audio call issues, refer to our `existing Jira ticket queue for WebRTC <https://mattermost.atlassian.net/browse/PLT-4735?jql=issuetype%20in%20(Bug%2C%20Improvement%2C%20%22New%20Feature%22%2C%20Story%2C%20Task)%20AND%20status%20in%20(Open%2C%20%22In%20Progress%22%2C%20Reopened%2C%20Submitted)%20AND%20text%20~%20webrtc>`_. If the issue is not on the list, try the following troubleshooting steps.

If you are still experiencing problems, post your issue in our `Troubleshooting forum <https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150>`_ or `file a bug <https://www.mattermost.org/filing-issues/>`_ if it's a product defect.

There was a problem connecting the video call
..........................

Confirm video and audio calls were `configured successfully <https://docs.mattermost.com/deployment/webrtc.html#configuring-video-and-audio-calls>`_ and that both users have a good Internet connection.

Unable to access camera or microphone
..........................

Confirm you have allowed Mattermost to access your camera and microphone. See instructions on how to give permissions on `Chrome <https://support.google.com/chrome/answer/2693767?hl=en>`_ and `Firefox <http://blog.speaklikethem.com/how-to-allow-camera-and-mic-access-in-firefox/>`_.

User has WebRTC disabled, and cannot receive calls.
..........................

Confirm that both users have enabled the feature in **Account Settings > Advanced > Preview pre-release features**
