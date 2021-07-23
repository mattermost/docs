Desktop App Custom Dictionaries
===========================

Mattermost Desktop App users running Windows or Linux can download dictionary definitions from a custom URL. If custom dictionaries aren't specified, default dictionary definitions are obtained automatically from Chromium's CDNs.
such a service, dictionaries definitions will be automatically obtained from Chromium's CDNs.

This feature allows users to provide customized dictionary definitions instead of using Chromium's CDNs.

This feature is available in the Mattermost Desktop App from v4.7.1 on Windows and Linux. Custom dictionaries are not supported in the Mattermost Desktop App on macOS.

Setting up the dictionaries
---------------------------

The Mattermost Desktop App uses [Hunspell Dictionary definitions](https://hunspell.github.io/) for Windows and Linux. For macOS, dictionary definitions 
are provided by Apple within the operating system itself. A quick way to access default dictionary definitions is to obtain a copy of `hunspell_dictionaries.zip` from the [latest 
electron release](https://github.com/electron/electron/releases/latest).

Once downloaded, the dictionary definitions need to be extracted and converted to lowercase because chromium expects `en-us` rather than `en-US...`.

Serve the files from a web server, and copy the URL to the root folder of the dictionaries.

Configuring the Desktop App
---------------------------

Access Mattermost Desktop App Preferences by opening the Desktop App, then going to **… > File > Settings**. Under **App Options**, ensure that the **Check Spelling** option is enabled. Below this setting there is a link 
named **Use and alternative dictionary URL**. Use this option to specify the URL to the root folder of 
the dictionaries, then select `Save`.

Removing customized dictionaries
------------------------------------

Open the preferences of the desktop app and below the input box there is a link `Revert to default`, clicking on it will disable 
the feature and revert to using Chromium's CDN
