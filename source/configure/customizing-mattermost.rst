Customizing Mattermost
======================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

There are several ways to customize your Mattermost server. 

If customizing Mattermost, please avoid branding that could be confused with the Mattermost brand. For example, it's okay to brand as "Healthcare Central" because it's a completely different brand. "Mattermost Healthcare Central" is not okay, because it can potentially be confused with the Mattermost brand. Please see the `Mattermost trademark guidelines <https://mattermost.com/trademark-standards-of-use/>`__ for details.

While you're welcome to add your own copyright notice in the user interface if you feel it is warranted by your changes, we ask that you do not remove the Mattermost, Inc. copyright notice from the login footer or from the About dialog.

Mattermost Web App
------------------

The Mattermost webapp is licensed under the Apache 2.0 license. To modify and use with the Mattermost server, you can:

1. Install the Mattermost server by following one of our installation guides
2. Fork the `mattermost <https://github.com/mattermost/mattermost>`__ repository
3. Go to the web app code located in the ``webapp`` directory and make your changes
4. Run ``make package`` to create ``mattermost-webapp.tar.gz``
5. Copy ``mattermost-webapp-tar.gz`` to the location Mattermost was installed in Step 1
6. Rename the existing ``client`` folder to ``client-original``
7. Run ``tar -xvf mattermost-webapp.tar.gz`` to extract your new customized ``client`` folder
8. If you're installing Mattermost 7.5 - 7.10, copy the ``products`` folder from ``client-original`` into ``client``
9. Restart your Mattermost server

It is possible to customize certain parts of the webapp without forking by using our :doc:`Custom Branding <../configure/custom-branding-tools>` settings. 

To replace the logo in email notifications, change the file located in the ``/images`` directory. To change the app icon, modify the ``/app/components/app_icon.js`` file.

Mattermost Server
-----------------

There are a few things you can customize in the Mattermost server without forking:

1. Modify text in the Mattermost interface by modifying the ``en.json`` file.
2. Customize or hide help and support links by modifying your `configuration settings </configure/configuration-settings.html#customization>`__.
3. Customize the email notifications by editing the HTML files in ``/templates``.

Mattermost mobile apps
----------------------

The Mattermost mobile apps can be customized if you choose to build the apps yourself. 

To brand the mobile apps: 

1. Fork the `mattermost-mobile <https://github.com/mattermost/mattermost-mobile>`__ repository
2. Replace the name, images, and any key text strings
3. :doc:`Compile the apps <../deploy/build-custom-mobile-apps>`
4. Deploy the apps to an app store

While most organizations deploy to internal enterprise app stores, you are welcome to deploy to iTunes and Google Play as long as the branding is not confusable with official Mattermost products.

Mattermost desktop apps
-----------------------

The Mattermost desktop apps can be customized if you choose to build the apps yourself. 

To brand the desktop apps: 

1. Fork the `mattermost/desktop <https://github.com/mattermost/desktop>`__ repository
2. Replace the name, images, and any key text strings
3. Refer to `this documentation <https://github.com/mattermost/desktop/blob/master/docs/development.md>`__ for help with compiling the apps
4. Share the desktop application with your users 
