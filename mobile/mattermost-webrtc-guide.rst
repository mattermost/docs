Mattermost WebRTC Guide
----------------------------------------------

This guide is aimed at setting up Mattermost WebRTC with a docker container. If you need support for a full `Janus Gateway <https://janus.conf.meetecho.com/>`_, please visit their `GitHub repo <https://github.com/meetecho/janus-gateway>`_ for detailed instructions.

Assertions about using the Mattermost `WebRTC docker image <https://hub.docker.com/r/mattermost/webrtc/>`_
 - You need docker to install this image (docker installation, configuration and management is outside the scope of this guide)
 - You need a working Mattermost server (installation, configuration and management of the Mattermost server is outside the scope of this guide)
 - Janus version is 0.2.2
 - No TURN or STUN service included
 - SSL Certificate valid for host **dockerhost** and until 2 January 2018
 - Ability to connect using SSL or plain WebSocket and HTTP

Deploying Mattermost WebRTC Docker Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assuming you have docker installed and running, you'll need to execute the following command in a terminal to install the Mattermost WebRTC docker image.

`docker run --name mattermost-webrtc -p 7088:7088 -p 7089:7089 -p 8188:8188 -p 8189:8189 -d mattermost/webrtc:latest`

This will download, install and run your mattermost-webrtc container with the Janus Gateway pre-configured to use WebRTC within the Mattermost Web and Desktop Apps.

Note: Make sure your Mattermost server can reach the running docker Mattermost WebRTC container.

Configuring Mattermost to Enable WebRTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first thing you need to decide is whether you are going to establish the connections to the Mattermost WebRTC container running the Janus Gateway with or without SSL. This is particularly important in this case because the SSL certificate used to run the Janus Gateway is not being signed by a trusted CA, which means that you will need to make some additional configuration changes in your Mattermost Server.

If you decide to go ahead with SSL, go to **System Console** -> **Security** -> **Connections and Enable Insecure Outgoing Connections**

.. image:: ../../source/images/connections_true_apps.png

The reason for this is that Mattermost will make an http request to the Janus Gateway service to get a token that is used to identify the user. If you configure Mattermost to make requests to that service with SSL, the certificate won't be valid and will return a status code of 500.

Next we need to configure the WebRTC service on our Mattermost Server. Go to **System Console** -> **Integrations** -> **WebRTC (Beta)**

.. image:: ../../source/images/webrtc_apps.png

Once you have enabled WebRTC, you'll need to input the following values:
 - **Gateway WebSocket URL**: This is the WebSocket route for the Janus Gateway service inside the Mattermost WebRTC container used to connect the peers on a Video Call. If you want to establish the connection using SSL, set the protocol to **wss://**  and the port to **8189**. For non-SSL, use protocol **ws://** and port **8188**.
 - **Gateway Admin URL**: This is the admin route for the Janus Gateway service inside the Mattermost WebRTC container used to fetch a valid Token. If you want to establish the connection using SSL, set the protocol to **https://** and the port to **7089**. For non-SSL, use protocol **http://** and port **7088**.
 - **Gateway Admin Secret**: This is the admin's secret to validate the request being made to fetch the token. For any Janus Gateway installation, the default is **janusoverlord**. To modify the value for the admin_secret, edit the janus.cfg under /opt/janus/etc/janus.
 - **STUN URI**: This is the Stun server to use. A Stun server is required so, either deploy one or use the public Google one. The public Google Stun server is **stun:stun.l.google.com:19302**.
 - **TURN URI**: If you require NAT Traversal, you'll need to configure a TURN server. You can make use of Coturn to accomplish this but this is outside the scope of this guide.
 - **TURN Username**: The username of your TURN server, if you have one.
 - **TURN Shared Key**: The password of your TURN server, if you have one.
 
.. image:: ../../source/images/webrtc_values_apps.png

Don't forget to **Save** your configuration changes.

Finally, because this feature is in Beta, every user has to enable WebRTC in order to establish a video call with other users on the server. Go to  **Main Menu** -> **Account Settings** -> **Advanced** -> **Preview pre-release features and select Enable the ability to make and receive one-on-one WebRTC calls**.

.. image:: ../../source/images/enable_web_rtc_calls_apps.png
