Video and Audio Calling (Beta)
=====================================

Mattermost supports an early preview of video and audio calling option using a self-hosted proxy. The implementation is based on WebRTC integration enabling one-on-one video and audio calling within a browser without needing additional software to be installed.

The feature is a working prototype for community development and not recommended for production. It has been tested on Chrome and Firefox running on Mac and Windows and the Mattermost Mac and Windows Apps using a Mattermost server running in SSL mode.

.. note:: This feature will be replaced by a plug-in architecture allowing multiple video and audio calling providers to connect into Mattermost, and features described in this section will be re-written as a plug-in.

Configuring video and audio calls with WebRTC
----------------------------------------------

This guide is aimed to set up Mattermost WebRTC with a Docker image, `available here <https://hub.docker.com/r/mattermost/webrtc/>`_  and a Janus server to act as the WebRTC gateway. 

If you want to use a full `Janus Gateway <https://janus.conf.meetecho.com/>`_, please visit their `GitHub repo <https://github.com/meetecho/janus-gateway>`_ for detailed instructions. You may also optionally set up `Coturn <https://github.com/coturn/coturn/wiki>`_ for STUN and TURN servers for your Mattermost installation.

Pre-requisites
~~~~~~~~~~~~~~~

- Install Docker using the `Ubuntu online guide <https://docs.docker.com/installation/ubuntulinux/`_. Docker installation, configuration and management are out of scope for this guide.
- Install a Mattermost server using the `official install guides <https://docs.mattermost.com/guides/administrator.html#installing-mattermost>`_. Mattermost server installation, configuration and management are out of scope for this guide.
- Install Janus server version 0.2.2.
- Add an SSL certificate for host **dockerhost**, valid until January 2, 2018.
- Ability to connect using SSL or plain WebSocket and HTTP // XXX Is this for WebRTC connection?

STUN and TURN servers are not required for this setup.

Deploy Mattermost WebRTC Docker container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After installing Docker, run the following command in a terminal to install the Mattermost WebRTC Docker image.

   .. code:: bash

       docker run --name mattermost-webrtc -p 7088:7088 -p 7089:7089 -p 8188:8188 -p 8189:8189 -d mattermost/webrtc:latest

The command downloads, installs and runs your ``mattermost-webrtc`` container with the Janus Gateway pre-configured to use WebRTC on Chrome, Firefox or the Mattermost Destkop Apps.

.. note::
  Make sure your Mattermost server can reach the running Mattermost WebRTC Docker container. // XXX How can they verify this?

Configure Mattermost to enable WebRTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1 - (Optional) If you want to establish the connection to the Mattermost WebRTC Docker container running the Janus Gateway

First you need to decide whether to establish the connections to the Mattermost WebRTC Docker container running the Janus Gateway with or without SSL.  this is particularly important in this case because the SSL certificate used to run the Janus Gateway is not being signed by a trusted CA, that means that you will need to make some additional configuration changes in your Mattermost Server.

In case you decide to go ahead with SSL then you need to go to System Console -> Security -> Connections and Enable Insecure Outgoing Connections

The reason for this is that Mattermost will make a http request to the Janus Gateway service to get a Token that is used to identify the user and so on and if you configure Mattermost to make requests to that service with SSL then the certificate won't be valid thus returns a status code of 500.

// XXX

2 - Go to **System Console > Integrations > WebRTC (Beta)** and set the following values:

.. image:: ../images/webrtc_full_settings.png

- **Enable Mattermost WebRTC** - ``true``.
- **Gateway WebSocket URL** - example: ``wss://dockerhost:8189``. This is the WebSocket route for the Janus Gateway service, inside the Mattermost WebRTC container, used to connect peers on a video call. For SSL connections, set the protocol to ``wss://`` and the port to ``8189``. For non-SSL connections, set the protocol to ``ws://`` and port to ``8188``.
- **Gateway Admin URL** - example: ``
- **Gateway Admin Secret** - example: ``https://
- **STUN URI**
- **TURN URI**
- **TURN Username**
- **TURN Shared Key**


Starting a video call
--------------------------

After enabling the feature in the System Console by a System Administrator:

1. Go to **Account Settings > Advanced > Preview pre-release features** and select **Enable the ability to make and receive one-on-one WebRTC calls**.

2. Initiate a call with another user by either:

    Clicking **Start Video Call** on a user's profile popover, which appears after clicking their profile picture or name on the center channel or right hand sidebar.

    .. image:: ../images/webrtc-popover.png

    Clicking the video icon on the channel header of a direct message channel with that user.

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
