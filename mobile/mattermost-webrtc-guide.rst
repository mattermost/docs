Mattermost WebRTC Guide
----------------------------------------------

This guide is aimed to set up Mattermost WebRTC with a docker container if you need support for a full `Janus Gateway <https://janus.conf.meetecho.com/>`_ please visit their `Github repo <https://github.com/meetecho/janus-gateway>`_ for detail instructions.

Assertions about using the Mattermost `WebRTC docker image <https://hub.docker.com/r/mattermost/webrtc/>`_
 - You need docker to install this image (docker installation, configuration and management is out of the scope of this guide)
 - You need a working Mattermost server (installation, configuration and management of the Mattermost server is out of the scope of this guide)
 - Janus version is 0.2.2
 - No TURN or STUN service included
 - SSL Certificate valid for host **dockerhost** and until 2 January 2018
 - Ability to connect using SSL or plain WebSocket and HTTP

Deploying Mattermost WebRTC Docker Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assuming you have docker installed and running you'll need to execute in a terminal the following command to install the Mattermost WebRTC docker image

`docker run --name mattermost-webrtc -p 7088:7088 -p 7089:7089 -p 8188:8188 -p 8189:8189 -d mattermost/webrtc:latest`

This will download, install and run your mattermost-webrtc container with the Janus Gateway pre-configured to use WebRTC within the Mattermost WebApp and Desktop Apps.

Note: Make sure your Mattermost server can reach the running docker Mattermost WebRTC container.

Configuring Mattermost to Enable WebRTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first thing you need to decide is whether your are going to establish the connections to the Mattermost WebRTC container running the Janus Gateway with or without SSL, this is particularly important in this case because the SSL certificate used to run the Janus Gateway is not being signed by a trusted CA, that means that you will need to make some additional configuration changes in your Mattermost Server.

In case you decide to go ahead with SSL then you need to go to **System Console** -> **Security** -> **Connections and Enable Insecure Outgoing Connections**

.. image:: connections_true_apps.png

The reason for this is that Mattermost will make a http request to the Janus Gateway service to get a Token that is used to identify the user and so on and if you configure Mattermost to make requests to that service with SSL then the certificate won't be valid thus returns a status code of 500.

Next we need to configure the WebRTC service on our Mattermost Server for that go to **System Console** -> **Integrations** -> **WebRTC (Beta)**

.. image:: webrtc_apps.png

Once you enable WebRTC you'll need to input a few values
 - **Gateway WebSocket URL**: This is the WebSocket route for the Janus Gateway service inside the Mattermost WebRTC container used to connect the peers on a Video Call. If you want to establish the connection using SSL then you need to set the protocol to **wss://**  and the port to **8189**, for non-SSL use protocol **ws://** and port **8188**.
 - **Gateway Admin URL**: This is the admin route for the Janus Gateway service inside the Mattermost WebRTC container use to fetch a valid Token. If you want to establish the connection using SSL then you need to set the protocol to **https://**  and the port to **7089**, for non-SSL use protocol **http://** and port **7088**.
 - **Gateway Admin Secret**: This is the admin's secret to validate the request being made to fetch the token, for any Janus  Gateway installation the default is **janusoverlord**, you can change it by editing the janus.cfg under /opt/janus/etc/janus and modify the value for admin_secret
 - **STUN URI**: This is the Stun server to use, you need to have one so either deploy one or use the public google one. The google public stun server is **stun:stun.l.google.com:19302**
 - **TURN URI**: In case you need NAT Traversal you'll need to configure a TURN server, you can use Coturn to accomplish that but is out of the scope of this guide
 - **TURN Username**: The username of your TURN server if you have one.
 - **TURN Shared Key**: The password of your TURN server if you have one.
 
.. image:: webrtc_values_apps.png

Don't forget to **Save** your configuration Changes

Finally, because this feature is in Beta every user has to enable WebRTC in order to establish a video call with other users on the server. Go to  **Main Menu** -> **Account Settings** -> **Advanced** -> **Preview pre-release features and select Enable the ability to make and receive one-on-one WebRTC calls**.

.. image:: enable_web_rtc_calls_apps.png
