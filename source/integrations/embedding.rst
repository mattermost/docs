
Embedding Mattermost in Other Applications
==========================================

This guide discusses how to embed Mattermost into other applications in different ways.

.. contents::
    :backlinks: top

Launching Mattermost From a Button Click
-----------------------------------------

The most common way of integrating Mattermost into another application is via a link or a button that brings up Mattermost in a new browser window or tab, with a link to a specific Mattermost channel to begin discussion.

Optionally, single-sign-on can be added to make the experience seamless.

Mattermost Launch Button Example in HTML 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Save the below HTML code in a file called ``mattermost-button-example.html`` then open the file in a browser as an example.

  <script>

      var myWindow = null;

      function openMMWindow() {
          myWindow = window.open("https://community.mattermost.com/core/channels/developer", "Mattermost", "top=0,left=0,width=400,height=600,status=no,toolbar=no,location=no,menubar=no,titlebar=no");
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

Embedding Mattermost in Web Applications Using an iframe
----------------------------------------------------------

Any web application embedded into another using an iframe is at risk of security exploits, since the outer application intercepts all user input into the embedded application, an exploit known as `Click-Jacking <https://en.wikipedia.org/wiki/Clickjacking>`__. By default, Mattermost disables embedding. If you choose to embed Mattermost we highly recommend it is done only on a private network that you control.

See `this recipe <https://forum.mattermost.org/t/recipe-embedding-mattermost-in-web-applications-using-an-iframe-unsupported-recipe/10233>`__ for details.

Embedding Mattermost in Mobile Applications
--------------------------------------------

The open source mobile applications can serve as a guide or starter code to embed Mattermost in mobile applications. The Mattermost Javascript Driver is used to connect with the Mattermost server and product the interactivity for these applications.

The mobile applications also provide full source code for push notifications.

Mobile Applications Offering Mattermost as a Web View 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- https://github.com/mattermost/ios
- https://github.com/mattermost/android

Mobile Applications Offering Mattermost with React Native Components 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

https://github.com/mattermost/mattermost-mobile
