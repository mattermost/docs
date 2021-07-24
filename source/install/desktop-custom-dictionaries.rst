Desktop App Custom Dictionaries
=====================================

Mattermost Desktop App users running Windows or Linux can download dictionary definitions from a custom URL. If custom dictionaries aren't specified, default dictionary definitions are obtained automatically from Chromium's CDNs.
such a service, dictionaries definitions will be automatically obtained from Chromium's CDNs.

This feature is available in the Mattermost Desktop App from v4.7.1 on Windows and Linux. Custom dictionaries are not supported in the Mattermost Desktop App on macOS.

Setting up the dictionaries
---------------------------

The Mattermost Desktop App uses [Hunspell Dictionary definitions](https://hunspell.github.io/) for Windows and Linux. For macOS, dictionary definitions 
are provided by Apple within the operating system itself. A quick way to access default dictionary definitions is to obtain a copy of `hunspell_dictionaries.zip` from the [latest 
electron release](https://github.com/electron/electron/releases/latest).

Once downloaded, the dictionary definitions need to be extracted and converted to lowercase because chromium expects `en-us` rather than `en-US...`.
These defitions are ready to use and would match the usage of using Chromium's CDN ones without accesing it, but they could also be modified to fit specific needs.

Serve the files from a web server, and write down the URL to the root folder of the dictionaries for using it in the Desktop App.

Configuring the Desktop App
---------------------------

Open the Mattermost Desktop App, go to **… > File > Settings**. Under **App Options**, and ensure that the **Check Spelling** option is enabled. Below this setting there is a link 
named **Use and alternative dictionary URL**. Use this option to specify the URL to the root folder of the dictionaries, then select `Save`.

Removing customized dictionaries
------------------------------------

To stop using the specified dictionary definitions, select the **Revert to default** preference option under the input box in the **App Options** to 
use Chromium's CDNs instead.
