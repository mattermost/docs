Deprecation Policy
===============================

This document outlines the process for announcing deprecated features to the community. The guiding principle is `no surprises <https://docs.mattermost.com/developer/manifesto.html#no-surprises>`_ with guaranteed long-term stability, where admins or users should never run into anything unexpected with Mattermost.

Definition of Deprecated Feature
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A deprecated feature is considered one that breaks backwards compatibility with previous versions.

Examples include:

1) Removing an API endpoint, or one of its parameters.

 - APIv3 endpoints on January 16, 2018.
 - “permanent” parameter of the DELETE /teams/{team_id} APIv4 endpoint in Mattermost v5.0.0.

2) Removing a config.json setting

 - System Console settings in Files > Images in Mattermost v4.0.0.

3) Removing an end user setting or functionality.

 - Font setting in Account Settings > Display in Mattermost v4.0.0.

Notice
~~~~~~~

When the decision to deprecate a feature or function is made, the product manager responsible for the feature carries out the following actions:

1. Adds the scheduled deprecation to the `deprecated features page <https://about.mattermost.com/deprecated-features/>`_, which has a record of past and future deprecations.
2. Prepares a forum post describing the reasons for deprecating the feature, providing an opportunity for the community to share feedback. See a `sample forum post <https://forum.mattermost.org/t/switching-teammate-name-display-to-a-system-console-setting/3366>`_.
3. Creates a JIRA ticket for removing the feature, including a prefix “Deprecation:” and a fix version matching the removal target date.

Moreover, the acting release manager takes the following actions:

1. `12 working days before each release <https://docs.mattermost.com/process/release-process.html#c-t-minus-12-working-days-cut-off-for-merging-major-features>`_, adds a list of deprecated features to the compatibility section of the `changelog <https://docs.mattermost.com/administration/changelog.html>`_ and `important upgrade notes <https://docs.mattermost.com/administration/important-upgrade-notes.html>`_. The changelog should include deprecations scheduled for upcoming releases.
2. `12 working days before each release <https://docs.mattermost.com/process/release-process.html#c-t-minus-12-working-days-cut-off-for-merging-major-features>`_, sends the list of deprecated features to the marketing manager, who includes this information in the release announcement.
3. `2 working days before each release <https://docs.mattermost.com/process/release-process.html#h-t-minus-2-working-days-release-build-cut>`_, ensures the `deprecated features page <https://about.mattermost.com/deprecated-features/>`_ is up to date.

Removal target date
~~~~~~~~~~~~~~~~~~~~~

The removal target date should always be the date of the next major release, such as v4.0.0. If the date is not known, you can reference the next major version rather than the actual release date.

However, there should always be at least two months from the time the deprecation is announced to its removal. This number is chosen to match our security backport release policy.

See the table below for examples:

+-----------------------+---------------------+---------------------+
| Deprecation Announced | Final Minor Release | Removal Target Date |
+=======================+=====================+=====================+
| 3.9.0                 | 3.10.0              | 4.0.0               |
+-----------------------+---------------------+---------------------+
| 3.10.0                | 3.10.0              | 5.0.0               |
+-----------------------+---------------------+---------------------+

Exceptions for the removal target date may be made if it impacts security or performance of using Mattermost. In such cases, the target date for removing the feature may be made sooner.

On the other hand, if removing a feature is deemed significant, such as the removal of APIv3 endpoints, the target date for removing the feature may be extended to a later release.
