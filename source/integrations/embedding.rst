================================================
Embedding Mattermost in other applications 
================================================

This guide discusses how to embed Mattermost into other applications in different ways. 

.. contents::
    :backlinks: top

Launching Mattermost from a button click 
-------------------------------------------------------

The most common way of integrating Mattermost into another application is via a link or a button that brings up Mattermost in a new browser window or tab, with a link to a specific Mattermost channel to begin discussion. 

Optionally, single-sign-on can be added to make the experience seamless. 

Mattermost Launch Button Example in HTML 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Save the below HTML code in a file called ``mattermost-button-example.html`` then open the file in a browser as an example. 

  <script>

      var myWindow = null;

      function openMMWindow() {
          myWindow = window.open("https://pre-release.mattermost.com/core/channels/developer", "Mattermost", "top=0,left=0,width=400,height=600,status=no,toolbar=no,location=no,menubar=no,titlebar=no");
      }


      function closeMMWindow() {
          if (myWindow) {
              myWindow.close();
          }
      }


  </script>


  <html>
      <br/>
      <br/>
      <button onclick="openMMWindow()">Open Developer Channel</button>
      <br/>
      <br/>
      <button onclick="closeMMWindow()">Close Developer Channel</button>
      <br/>
      <br/>
  </html>


Embedding Mattermost in web applications using an iframe  
----------------------------------------------------------

.. warning:: Any web application embedded into another using an iframe is at risk of security exploits, since the outer application intercepts all user input into the embedded application, an exploit known as `Click-Jacking <https://en.wikipedia.org/wiki/Clickjacking>`_. By default, Mattermost disables embedding. If you choose to embed Mattermost using the following instructions we highly recommend it is done only on a private network that you control. 

To embed Mattermost in an iframe by overriding Mattermost security features: 

1. On your Mattermost server, change the HTML template to remove the anti-Clickjacking security feature 

    a. Find the file ``/mattermost/mattermost/web/templates/head.html``
    b. Comment out the security feature by changing ``<style id="antiClickjack">body{display:none !important;}</style>`` to ``<!-- <style id="antiClickjack">body{display:none !important;}</style> -->`` 

2. Update your NGINX configuration to strip out the security policy settings in the HTTP header.

    - See `community example <https://forum.mattermost.org/t/how-can-we-load-mattermost-in-iframe/165/6>`_ for details.

Embedding Mattermost in mobile applications 
-------------------------------------------------------

The open source mobile applications can serve as a guide or started code to embed Mattermost in mobile applications. The Mattermost Javascript Driver is used to connect with the Mattermost server and product the interactivity for these applications. 

The mobile applications also provide full source code for push notifications. 

Mobile applications offering Mattermost as a web view: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- https://github.com/mattermost/ios
- https://github.com/mattermost/android


Mobile applications offering Mattermost with React Native components: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- https://github.com/mattermost/mattermost-mobile 



