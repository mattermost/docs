Announcing Deprecated Features
===============================

This document outlines the process for announcing deprecated features to the community. The guiding principle is `no surprises <https://docs.mattermost.com/developer/manifesto.html#no-surprises>`_ where users should never run into anything unexpected with Mattermost.

Once the decision to deprecate a feature or functionality is made, the acting release manager carries out the following actions:

1 - Adds the scheduled deprecation to the `webpage <https://about.mattermost.com/deprecated-features/>`_, which has a historical record of past and future deprecations. Link to the website is also included in the `changelog <https://docs.mattermost.com/administration/changelog.html>`_ and the `upgrade guide <https://docs.mattermost.com/administration/upgrade.html>`_.

2 - At `T-12 of the release process <https://docs.mattermost.com/process/release-process.html#c-t-minus-12-working-days-cut-off-for-merging-major-features>`_, includes a list of deprecated features to the compatibiltity section of the changelog. This list includes deprecated features scheduled for the upcoming release, as well as major deprecations (such as removal of an old CLI tool or discontinuing support for all APIv3 endpoints) in later releases.

3 - At `T-12 of the release process <https://docs.mattermost.com/process/release-process.html#c-t-minus-12-working-days-cut-off-for-merging-major-features>`_, communicates deprecated features to the marketing manager, who includes this information in the release announcement.

4 - At `T-2 of the release process <https://docs.mattermost.com/process/release-process.html#h-t-minus-2-working-days-release-build-cut>`_, updates the `deprecated feature list <https://about.mattermost.com/deprecated-features/>`_ with new and scheduled deprecations.
