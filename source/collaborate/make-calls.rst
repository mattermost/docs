Make calls 
============

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Using a web browser, the desktop app, or the mobile app, you can `join a call <#join-a-call>`__ or `start a call <#start-a-call>`__, `share your screen <#share-screen>`__, raise your hand, `react using emojis <#react-using-emojis>`__ during a call, `chat in a thread <#chat-in-a-call>`__, and continue working in Mattermost during a call.

.. note::

  - All Mattermost customers can start, join, and participate in 1:1 audio calls with optional screen sharing.
  - For group calls up to 50 concurrent users, Mattermost Enterprise, Professional, or Mattermost Cloud is required.
  - Enterprise customers can also `record calls <#record-a-call>`__, enable :ref:`live text captions <collaborate/make-calls:live captions during calls (beta)>` during calls, and `transcribe recorded calls <#transcribe-recorded-calls>`__. We recommend that Enterprise self-hosted customers looking for group calls beyond 50 concurrent users consider using the :ref:`dedicated rtcd service <configure/calls-deployment:rtcd>`.
  - Mattermost Cloud users can start calling right out of the box. For Mattermost self-hosted deployments, System admins need to enable and configure the plugin :ref:`using the System Console <configure/plugins-configuration-settings:calls>`.

.. include:: ../_static/badges/academy-calls.rst
  :start-after: :nosearch:

Join a call
-----------

To join a call, select **Join call** in a channel, group message, or direct message. Any active team member in a channel or message can join a call, whether it's a public or private channel, or a group or direct message. 

.. tip::

  - You can share a call's link to use in a meeting request or share with other people. The link is unique to each channel, and contains the channel's ID, so it doesn't change between calls. Use the ``/call link`` slash command to generate a shareable link. The call link is valid for long as the channel is active. When a channel is archived or deleted, the share link becomes invalid.
  - If someone from outside of the organization wants to join a call, you need to provide them with a guest account, and add them to the channel. Users who are archived or not registered can't join a call.

From Mattermost v9.4:

- You can join the same call using a web browser, the desktop app, and the mobile app. You can mute, unmute, react, share your screen, and configure voice settings independently for each Mattermost client you're using. You'll appear multiple times as a call participant in the call widget when you join one call on multiple clients.
- You'll see incoming call notifications for direct and group messages when a new call is started. Multiple calls will result in multiple incoming call notifications. If you're already in a call, and you receive a new incoming call notification, Mattermost prompts you to **Join** the incoming call, or dismiss the notification.

Start a call
------------

.. tab:: Web/Desktop

  To start a call, select **Start call** in the channel header. When you start a call, you become the call host by default. See the `host controls <#host-controls>`__ section below for details on host controls available to ensure calls run smoothly.
  
    
  .. tip::
      
    - When you start a call in a channel, you're muted by default. In a direct or group message you're unmuted by default.
    - You can move the call widget to a different area of your screen.
    - Alternatively, you can start a call using the ``/call start`` slash command.

.. tab:: Mobile
    
  To start a call, go the channel info menu. Then tap **Start Call**.
     
  After starting the call, audio will come through the device's speaker or a Bluetooth device, if connected. On Android, audio output will automatically switch to a Bluetooth device if one is connected during a call. You can tap the **Speaker** icon to manually select the output device.

  On iOS, audio will automatically come through a connected device. You can override this behavior by tapping the **Speaker** button. Audio will then come through the speaker. However, you cannot manually select an output device on iOS at this time.

Host controls
-------------

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

From Mattermost v9.9, and Mattermost mobile v2.17, call host controls are available and include the ability to `transfer host duties <#transfer-host-duties>`__, `remove call participants <#remove-call-participants>`__, `stop a screen share <#stop-a-screen-share>`__, `mute or unmute participants <#mute-or-nmute-participants>`__, `lower raised hands <#lower-raised-hands>`__, and `end the call for everyone <#end-the-call-for-everyone>`__.

Host controls are available to call hosts and admins in both the call widget by selecting the **More** |more-icon| icon next to a participant's name, and in the expanded the call window as hosts hover over a call participant in the list.

Transfer host duties
~~~~~~~~~~~~~~~~~~~~

Transfer host duties to another call participant by accessing the host controls and selecting **Make host**. Once host duties are transferred to someone else, you can't access host controls unless they're transferred back to you. System admins can change the host at any time.

Remove call participants
~~~~~~~~~~~~~~~~~~~~~~~~

Remove a call participant from an active call by accessing the host controls and selecting **Remove from call**, then confirm by selecting **Yes, remove**. The call participant is notified that they've been removed from the call by the host.

Stop a screen share
~~~~~~~~~~~~~~~~~~~~

Stop a call participant's screen share by accessing the host controls and selecting **Stop screen share**.

Mute participants
~~~~~~~~~~~~~~~~~~

Invite muted participants to unmute their microphone by accessing the host controls and selecting **Ask to unmute**.  The call particpant is prompted to decide whether unmute or stay muted.

You can mute the microphone of specific particpants by accessing the host controls and toggling the particpant's mute icon. Mute all call particpants by selecting **Mute all**.

Lower raised hands
~~~~~~~~~~~~~~~~~~~

Lower a raised hand by accessing the host controls and selecting **Lower hand**. The participant is notified that their hand was lowered by the host.

End the call for everyone
~~~~~~~~~~~~~~~~~~~~~~~~~

From Mattermost v9.10 and mobile v2.19, call hosts who choose to leave a call are prompted to confirm whether they want to leave or end the call for all participants.

Share your screen
-----------------

During a call, call participants can share their screen with other call participants, unless your system admin has :ref:`disabled your ability to do so <configure/plugins-configuration-settings:allow screen sharing>`. 

.. note::
  
  Screensharing is available in the Mattermost desktop app or a web browser. The ability to screenshare using the mobile app isn't supported.

To share your screen:

1. In the call widget, select **Start presenting**.
2. Select the screen you want to share.
3. To stop sharing, select the **Stop presenting** icon or the **Stop sharing** option.

React using emojis
------------------

All call participants can use emojis to react during a call.

.. tab:: Web/Desktop

  Expand the call window using the arrows in the top-right of the call widget. From there, select the emoji icon to access frequently-used emojis or select additional emojis from the emoji picker.

.. tab:: Mobile
  
  Expand the call window using the arrows in the top-right of the active call banner. From there, select **React**.

Chat in a call
--------------

A chat thread is created automatically for every new call.

.. tab:: Web/Desktop

  Expand the call window using the arrows in the top-right of the call widget. From there, select the emoji icon to access frequently-used emojis or select additional emojis from the emoji picker.

.. tab:: Mobile
  
  Expand the call window using the arrows in the top-right of the active call banner. Then select **More > Call Thread**.

Record a call
-------------

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

From Mattermost v7.7, if you're the host of a meeting, you can record the call, unless your system admin has :ref:`disabled the host's ability to do so <configure/plugins-configuration-settings:enable call recordings>`.

Call recordings include audio, any screen sharing during the call, and text transcriptions, when :ref:`enabled <configure/plugins-configuration-settings:enable call transcriptions (beta)>`. 

The default setting for a recording is 60 minutes, but your system admin may :ref:`change the recording duration <configure/plugins-configuration-settings:maximum call recording duration>` as needed. You'll receive a reminder 10 minutes before the recording limit is reached. If your call is going to continue beyond the recording limit, allow the first recording to complete, then start a new recording immediately after.

When you stop recording, the recording file is posted in the call thread as an MP4 file attachment. It's available to all users in the channel both during the call, and after the call has ended.

To record a call:

.. tab:: Web/Desktop

  1. Select **Start call** in the header of the channel, group message, or direct message.
  2. Select the pop-out icon.
  3. In the call widget, select the **Record** button.
  4. To stop recording, select the **Record** button again.

.. tab:: Mobile
  
  To start recording, use the ``/call recording start`` slash command. When you're finished recording, use the ``/call recording stop`` slash command. Alternatively, expand the call window using the arrows in the top-right of the active call banner. Then select the **Record** button. To finish, select the **Record** button again.

Live captions during calls (Beta)
---------------------------------

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

From Mattermost v9.7, and Mattermost mobile app v.2.16, all call participants can display real-time text captions by selecting the **More** |more-icon| icon and **Show live captions** when the call is being recorded, and when :ref:`live captions are enabled <configure/plugins-configuration-settings:enable live captions (beta)>`. Live captions can be helpful in cases where noise is preventing you from hearing the audio of participants clearly.

By default, live captions display in English. Your Mattermost system admin can :ref:`specify a different language for live captions <configure/plugins-configuration-settings:live captions language>` in the System Console.

.. note::

  :ref:`Call recording must be enabled <configure/plugins-configuration-settings:enable call recordings>` to enable live captions.

Transcribe recorded calls (Beta)
--------------------------------

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

From Mattermost v9.4, and Mattermost mobile app v.2.13, call recordings can include text captions, and a transcription text file can be generated, unless your system admin has :ref:`disabled the ability to transcribe call recordings <configure/plugins-configuration-settings:enable call transcriptions (beta)>`.

.. note::

  :ref:`Call recording must be enabled <configure/plugins-configuration-settings:enable call recordings>` to enable recorded call transcriptions.

When call recording stops, the transcription file is posted in the call thread as a TXT file attachment. It's available to all users in the channel both during the call, and after the call has ended. Additionally, users viewing the call recording can show or hide text captions using the Closed Captioning option in the video player.

Frequently asked questions
--------------------------

Can I set a ring tone for incoming calls?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes! From Mattermost v8.0 and Calls v0.17.0, desktop app and web users can go to **Settings > Notifications > Desktop Notifications** to enable Mattermost to alert you to incoming calls through direct or group messages with a specific ring tone and a desktop notification, unless the system admin has :ref:`disabled your ability to do so <configure/plugins-configuration-settings:enable call ringing>`.

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

If you can hear the other participants in the call but they can't hear you, select the Gear icon |gear| next to the call end button in the widget. From there, you can check and change your audio output and microphone settings. Select |gear| again to close the menu. Alternatively, you can :doc:`manage your audio and microphone preferences </preferences/manage-your-calls-preferences>` in **Settings**.

My call is disconnected after a few seconds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is usually a sign that the underlying UDP channel has not been established and the connection times out after ~10 seconds. When the connection has been established correctly an ``rtc connected`` line should appear in the client-side logs (JS console). There isn't a single solution as it depends on your infrastructure/deployment specifics. However, if you're a system or network admin, you may need to open up the UDP port or configure the network accordingly.

I can't screen share using Mattermost desktop on macOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There's a known bug on macOS with some versions of Chrome (which is used by Mattermost desktop). If you've given screen sharing permissions to Mattermost desktop, and are still unable to screen share, do the following:

1. Quit Mattermost.
2. Open Terminal.
3. In the terminal, run: ``tccutil reset ScreenCapture Mattermost.Desktop``
4. Restart Mattermost and start a call.
5. Select **Screen share** and give it permissions again.
6. Restart Mattermost again.

If the issue persists please post on the Mattermost Community Server in the `Developer: Calls <https://community.mattermost.com/core/channels/developers-channel-call>`_ channel to troubleshoot further.

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

In the top menu bar of the app, select **View > Developer Tools > Developer Tools for Current Tab**. In the logs that are generated, right-click and select **Save as** to download the logs.

Mobile app
^^^^^^^^^^

You can access and share debug logs from **Account screen > Settings > Report a problem**.

Call stats dump
~~~~~~~~~~~~~~~

In cases where there are audio/video issues, difficulty in hearing other participants, and/or stuttering video and/or choppy audio, run the ``/call stats`` slash command in the channel where the call is currently active. This returns a JSON object via an ephemeral message. Additionally, run the ``/call logs`` command to review the client logs for the last call session.

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
