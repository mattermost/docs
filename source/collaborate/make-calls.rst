Make calls 
============

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v7.0, you can make voice calls and share your screen in channels, group messages, and direct messages in both Mattermost Cloud and Mattermost self-hosted deployments.

On this page:

- `Start a call <#start-a-call>`__
- `Emojis <#emojis>`__
- `Chat in a call <#chat-in-a-call>`__
- `Record a call <#record-a-call>`__
- `Frequently asked questions <#frequently-asked-questions>`__
- `Troubleshooting <#troubleshooting>`__
- `Debugging <#debugging>`__

From Mattermost v7.0, you can:

- Start or join a call from desktop and mobile apps in addition to web browsers.
- Share screen (not available on mobile), raise hands, chat in a thread, and continue working in Mattermost while on a call.
- Start a call using the ``/call start`` slash command or **Start call** in the channel header.

Starting from Mattermost v7.7 you can:

- Record calls (Mattermost Enterprise only).
- React using emojis.

Mattermost Cloud users can start calling right out of the box. For Mattermost self-hosted deployments, System Admins need to enable the plugin and adjust configurations `in the System Console </configure/plugins-configuration-settings.html#calls>`_.

Start a call
------------

.. tabs::

  .. tab:: Web/Desktop

    To start a call, select **Start call** in the channel or message header. When you start a call in a channel, you're muted by default. In a direct or group message you're unmuted by default.
    
    .. tip::
      
      Select the call widget to move it to a different area of your screen.

  .. tab:: Mobile
    
    To start a call, select the channel info menu. Then select **Start Call**.
     
    After starting the call, audio will come through the device's speaker or a Bluetooth device, if connected. On Android, audio output will automatically switch to a Bluetooth device if one is connected during a call. You can tap the **Speaker** icon to manually select the output device.

    On iOS, audio will automatically come through a connected device. You can override this behavior by tapping the **Speaker** button. Audio will then come through the speaker. However, you cannot manually select an output device on iOS at this time.
    
Any active team member in the channel can join a call, whether it's a public or private channel. If someone from outside of the organization wants to join a call, you'll need to provide them with a guest account, and add them to the channel. Users who are archived or not registered can't join a call.

You can share a call's link to use in a meeting request or share with other team mates. The link is unique to each channel, and contains the channel's ID, so it doesn't change between calls. Use the ``/call link`` slash command to generate a shareable link.

The call link is valid for long as the channel is active. When a channel is archived or deleted the link will become invalid.

Emojis
------

You can use emojis to react during a call.

.. tabs::

  .. tab:: Web/Desktop

    Expand the call window using the arrows in the top-right of the call widget. From there, select the emoji icon to access frequently-used emojis or select additional emojis from the emoji picker.

  .. tab:: Mobile
  
    Expand the call window using the arrows in the top-right of the active call banner. From there, select **React**.
      
Chat in a call
--------------

A chat thread is created automatically for every new call.

.. tabs::

  .. tab:: Web/Desktop

    To do this, expand the call window using the arrows in the top-right of the call widget. From there, select the emoji icon to access frequently-used emojis or select additional emojis from the emoji picker.

  .. tab:: Mobile
  
    To do this, expand the call window using the arrows in the top-right of the active call banner. Then select **More > Call Thread**.
    
Record a call
-------------

From Mattermost v7.7 if you're the host of a meeting, you can record the call.

The recording includes audio as well as any screen sharing during the call. The default setting for a recording is 60 minutes, but your system admin may adjust that as needed. Ten minutes before the time limit is reached, you'll receive a reminder that the recording limit will be reached soon.

If your call is going to continue and you still want to record, once the first recording is complete you can start a new one immediately after.

When you stop recording, the recording is posted in the call thread as a file attachment. It's available to all users in the channel both during the call, and when the call has ended.

To record a call:

.. tabs::

  .. tab:: Web/Desktop

    1. Select **Start call** in the header of the channel, group message, or direct message.
    2. Select the pop-out icon.
    3. In the pop-out screen, select the record button.
    4. To stop recording, select the record button again.

  .. tab:: Mobile
  
    To start recording, use the ``/call recording start`` slash command. When you're finished recording, use the ``/call recording stop`` slash command. Alternatively, expand the call window using the arrows in the top-right of the active call banner. Then select the record button. To finish, select the button again.
    
Frequently asked questions
--------------------------

Can I set a ring tone for incoming calls?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes! From Mattermost v8.0 and Calls v0.17.0, desktop app and webapp users can go to **Settings > Notifications > Desktop Notifications** to enable Mattermost to alert you to incoming calls through direct or group messages with a specific ring tone and a desktop notification, unless the system admin has `disabled your ability to do so </plugins-configuration-settings.html#enable-call-ringing-beta>`__.

Is video supported?
~~~~~~~~~~~~~~~~~~~

The integration currently supports only voice calling and screen sharing. We're considering video support in the future.

Can I password-protect a call?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Any member with sufficient permission to access the channel can join the call.

Is there encryption?
~~~~~~~~~~~~~~~~~~~~

Media (audio/video) is encrypted using security standards as part of WebRTC. It's mainly a combination of DTLS and SRTP. It's not e2e encrypted in the sense that in the current design all media needs to go through Mattermost which acts as a media router and has complete access to it. Media is then encrypted back to the clients so it's secured during transit. In short: only the participant clients and the Mattermost server have access to unencrypted call data.

Are there any third-party services involved?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The only external service used is Mattermost official STUN server (``stun.global.calls.mattermost.com``) which is configured as default. This is primarily used to find the public address of the Mattermost server. The only information sent to this service is the IP addresses of clients connecting as no other traffic goes through it. It can be removed in the System Console if you want to provide an ``ICE Host Override`` setting instead.

Troubleshooting
---------------

My audio doesn't work when I join a call
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you can hear the other participants in the call but they can't hear you, select the horizontal dots next to the call end button in the widget. From there, you can check and change your audio output and microphone settings. Select the horizontal dots again to close the menu.

My call is disconnected after a few seconds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is usually a sign that the underlying UDP channel has not been established and the connection times out after ~10 seconds. When the connection has been established correctly an ``rtc connected`` line should appear in the client-side logs (JS console). There isn't a single solution as it depends on your infrastructure/deployment specifics. However, if you're a system or network admin, you may need to open up the UDP port or configure the network accordingly.

I can't screen share using Mattermost desktop on macOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There's a known bug on macOS with some versions of Chrome (which is used by Mattermost desktop). If you've given screen sharing permissions to Mattermost desktop, and are still unable to screen share, do the following:

1. Quit Mattermost.
2. Open Terminal.
3. In terminal, run: ``tccutil reset ScreenCapture Mattermost.Desktop``
4. Restart Mattermost and start a call.
5. Select **Screen share** and give it permissions again.
6. Restart Mattermost again.

If the issue persists please post in the public calls channel.

Debugging
---------

If you experience issues with calls, collecting information is helpful as you can share it with us for debugging purposes.

As with any other issue, but more importantly with calls, it’s very useful to let us know the date and time that the problem occurred, with as much detail as possible so that information can be cross-checked with server logs. Also please include any reproduction steps if applicable. Other important information includes:

- Browser/app version
- Operating system type and version

JS console logs
~~~~~~~~~~~~~~~

Web app
^^^^^^^

+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Browser                         | Action                                                                                                                                                                                                                | 
+=================================+=======================================================================================================================================================================================================================+
| **Chrome**                      | CMD+OPTION+J (macOS)                                                                                                                                                                                                  |
|                                 | CTRL+SHIFT+J (Windows, Linux, ChromeOS)                                                                                                                                                                               | 
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Firefox**                     | CMD+SHIFT+J (macOS)/CTRL+SHIFT+J (Windows, Linux, ChromeOS)                                                                                                                                                           | 
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Safari**                      | Enable Developer Menu in **Safari > Preferences > Advanced > Show Develop Menu in Menu Bar**. Then **Develop > Show Javascript Console**. Right-click on the console and select **Save to file** to download the logs.|
+---------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Desktop app
^^^^^^^^^^^

In the top menu bar of the app, select **View > Developer Tools for Current Tab**. In the logs that are generated, right-click and select **Save as** to download the logs.

Call stats dump
~~~~~~~~~~~~~~~

In cases where there are audio/video issues, difficulty in hearing other participants, and/or stuttering video and/or choppy audio, run the ``/call stats`` slash command in the channel where the call is currently active. This returns a JSON object via an ephemeral message.

You can run this command in an active call or after leaving the call in question. However, we will only save data for the last joined call so joining again will delete the previous call's feedback.

WebRTC internals (Chrome and Firefox only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is an additional method for Chrome and Firefox users in cases where there are audio/video issues, difficulty in hearing other participants, and/or stuttering video and/or choppy audio.

Chrome browser (recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open ``chrome://webrtc-internals/`` in the browser that you're using for the active call.

Firefox browser
^^^^^^^^^^^^^^^

Open ``about://webrtc`` in the browser that you're using for the active call.

Share information
~~~~~~~~~~~~~~~~~

Debug information is helpful to our community as there may be other community members having the same issue as you. We recommend that debug information be shared in either of the two options below:

- Post in `Developers: Calls <https://community.mattermost.com/core/channels/developers-channel-call>`_ channel:  prefer this method when possible but keep in mind the channel is public.
- Post in `Team: Calls <https://community.mattermost.com/private-core/channels/calls-team>`_ channel: use this channel if posting sensitive information.
