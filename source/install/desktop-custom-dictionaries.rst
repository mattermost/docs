Desktop Custom dictionaries
===========================

Mattermost Desktop allows users to download their dictionary definitions from a custom URL. If the user doesn't want to provide
such a service, dictionaries definitions will be automatically obtained from Chromium's CDNs.

This feature enables users to skip using Chromium's CDNs as well as to provide customized dictionaries definitions.

This feature is available since v4.7.1 on Windows and Linux.

Setting up the dictionaries
---------------------------

The desktop app uses [Hunspell Dinctionary definitions](https://hunspell.github.io/) for Windows and Linux (for macOS definitions 
are provided by the OS itself). A quick way to get them is to obtain a copy of `hunspell_dictionaries.zip` from the [latest 
electron release](https://github.com/electron/electron/releases/latest).

Once obtained it needs to be extracted and converted to lowercase, as chromium won't try to access `en-US...` but `en-us...`.

Serve the files from a webserver and copy the URL to the root folder of the dictionaries.

Configuring the desktop app
---------------------------

Open the desktop app and go to the settings tab and ensure that check spelling is turned on. Below this setting there is a link 
named `Use and alternative dictionary URL`, clicking on it will reveal an input box. Fill it with the URL to the root folder of 
the dictionaries and click `Save`.

Removing the customized dictionaries
------------------------------------

Open the preferences of the desktop app and below the input box there is a link `Revert to default`, clicking on it will disable 
the feature and revert to using Chromium's CDN