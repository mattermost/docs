Announcing Deprecated Features
===============================

This document outlines the process for announcing deprecated features to the community. The guiding principle is `no surprises <https://docs.mattermost.com/developer/manifesto.html#no-surprises>`_, where users should never run into anything unexpected with Mattermost.

When the decision to deprecate a feature or function is made, the release manager carries out the following actions:

1. Adds the scheduled deprecation to the `deprecated features page <https://about.mattermost.com/deprecated-features/>`_, which has a record of past and future deprecations. Note: A link to the deprecated features page is currently in the `changelog <https://docs.mattermost.com/administration/changelog.html>`_ and the `upgrade guide <https://docs.mattermost.com/administration/upgrade.html>`_.

2. At `T-minus 12 working days <https://docs.mattermost.com/process/release-process.html#c-t-minus-12-working-days-cut-off-for-merging-major-features>`_, adds a list of the deprecated features to the compatibiltity section of the changelog. The list also includes major deprecations that are coming in later releases, such as removing an old CLI tool or ending support for all APIv3 endpoints.

3. At `T-minus 12 working days <https://docs.mattermost.com/process/release-process.html#c-t-minus-12-working-days-cut-off-for-merging-major-features>`_, sends the list of deprecated features to the marketing manager, who includes this information in the release announcement.

4. At `T-minus 2 working days <https://docs.mattermost.com/process/release-process.html#h-t-minus-2-working-days-release-build-cut>`_, updates the `deprecated feature list <https://about.mattermost.com/deprecated-features/>`_ with new and scheduled deprecations.
