Mattermost desktop app requirements
===================================

all plans, cloud & sh



.. csv-table::
    :header: "Operating System", "Self-Hosted Technical Requirement", "Cloud Technical Requirement"

    "Windows", "Windows 8.1+", "Windows 8.1+"
    "Mac", "macOS 11+", "macOS 11+"
    "Linux", "Ubuntu LTS releases 18.04 or later", "Ubuntu LTS releases 18.04 or later"

Though not officially supported, the Linux desktop app also runs on RHEL/CentOS 7+.

`*` Integrated Windows Authentication is not supported by Mattermost desktop apps. If you use ADFS we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.


Email client
~~~~~~~~~~~~

Receive emails on desktop and mobile from the Mattermost server.

-  *Desktop clients:* Outlook 2010+, Apple Mail version 7+, Thunderbird 38.2+
