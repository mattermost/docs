Desktop App custom dictionaries
===============================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. |vertical-3-dots| image:: ../images/dots-vertical_F01D9.svg
  :alt: Navigate Desktop App options on Windows or Linux.

On Windows or Linux, Mattermost desktop app v4.7.1 and later supports custom dictionary definitions served through a URL. If custom dictionaries aren't specified, default dictionary definitions are obtained automatically from Chromium's CDNs (content delivery networks).

.. note::
  
  On macOS, the Mattermost desktop app uses dictionary definitions provided by Apple that can't be customized.

Prepare custom dictionaries
---------------------------

On Windows and Linux, the Mattermost desktop app uses `Hunspell Dictionary definitions <https://hunspell.github.io/>`_ by default. You can download a copy of these dictionary definitions and modify them to fit specific needs. 

To access a copy of these dictionary definitions:

1. Download a copy of ``hunspell_dictionaries.zip`` from the `latest electron release <https://github.com/electron/electron/releases/latest>`__. 

2. Extract the dictionary definitions from the ZIP file.

3. Convert the filenames to lowercase. (Chromium expects ``en-us`` rather than ``en-US``). Once renamed, these definition files match the usage of using Chromium's CDN ones, and you can modify the definitions as needed.

4. Serve the extracted and converted files from a web server, and note the URL to the root folder of the dictionaries. Specify this URL as the **alternate dictionary URL** in the desktop app.

Configure the Desktop App
-------------------------

1. In the Mattermost Desktop App, go to Settings by selecting |vertical-3-dots| **> File > Settings**. 

2. Under **App Options**, ensure that the **Check spelling** option is enabled. 

3. Select **Use an alternative dictionary URL** to specify the URL to the root folder of your custom dictionaries, then select **Save**.

Remove custom dictionaries
--------------------------

Select **Revert to default** to stop using the specified dictionary definitions, and revert to default dictionary definitions.