=================================
Mattermost Software Requirements
=================================

This document provides guidelines for determining which software versions Mattermost requires. For past discussion on why these guidelines were chosen, see `this conversation <https://community.mattermost.com/core/pl/sb4fq6qhyfbb5xjdp7x3ud146e>`__.

Current software requirements are `documented here <https://docs.mattermost.com/install/requirements.html#software-requirements>`__.

Before submitting software requirement updates to the documentation, the following has to be taken into consideration:

1. Check with Chen in `the Analytics channel <https://community.mattermost.com/private-core/pl/qy675c87zbfn7dmzkh919ppmor>`_ to see what % of users and what % of posts are made by the versions we’re considering to drop support for, to review potential impact to users.
2. For versions we are considering dropping support for, ask the customer support team what the impact is for customers (e.g. if there are known customers on those versions and if we get customer support tickets specific to those versions).
3. Ask developers what the impact is for us internally if we consider dropping or continuing support for a version.
4. If we decide to drop support for a version, work with product managers and developers to plan for updating the version information in all relevant place, including but not limited to: in the product itself (such as the mobile app), Changelogs and README GitHub pages.

Desktop Apps
---------------------------------

.. csv-table::
    :header: "Operating System", "Guideline"

    "Windows", "Supported versions by Microsoft - `reference <https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions>`__"
    "Mac", "Supported versions by Apple - `reference <https://en.wikipedia.org/wiki/MacOS_version_history>`__"
    "Linux", "Fixed to Ubuntu LTS releases 16.04 or later"

PC Web
---------------------------------

.. csv-table::
    :header: "Browser", "Guideline"

    "Chrome", "Chromium version of latest Mattermost Desktop App"
    "Firefox", "Supported versions by Mozilla - `reference <https://www.mozilla.org/en-US/firefox/organizations/>`__"
    "Safari", "Safari version available in the minimum supported iOS version - `reference <https://en.wikipedia.org/wiki/Safari_version_history>`__"
    "Edge", "Latest release"
    
Mobile Apps
---------------------------------

.. csv-table::
    :header: "Operating System", "Guideline"

    "iOS", "Latest and next-to-latest versions - `reference <https://en.wikipedia.org/wiki/IOS_version_history>`__"
    "Android", "Supported versions by Google - `reference <https://en.wikipedia.org/wiki/Android_version_history>`__"
