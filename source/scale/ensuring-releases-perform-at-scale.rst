Ensuring Releases Perform at Scale
==================================

To ensure each release of Mattermost upholds our high standards for performance at scale, the Mattermost Engineering team performs thorough load testing, develops features with scale in mind, and follows strict guidelines for database schema migrations.

Monthly release load tests
--------------------------

Each month, before being approved for distribution, a release candidate of Mattermost is load tested via a comprehensive and mature set of `load test tooling <https://github.com/mattermost/mattermost-load-test-ng>`__ using simulated data that matches real-world, high-scale usage patterns.

Multiple tests covering different configurations are run against highly-available deployments of Mattermost with thousands of users and millions of posts. Both PostgreSQL and MySQL are tested, although MySQL tests will be dropped when :ref:`MySQL goes out of support with Mattermost v11 <about/deprecated-features:mattermost server v10.0.0>`.

The load tests generate a report detailing average API request times, database I/O, memory usage, concurrency, requests per second, and more. This performance report on the release candidate is then compared to the report of the latest previous stable version. Any deviations are investigated and remedied before the release candidate is promoted to the final release.

Each report, along with analysis, is posted into the public `Developers: Performance <https://community.mattermost.com/core/channels/developers-performance>`__ channel.


Developing scalable features and systems
----------------------------------------

Scale is a major consideration during the development of new features and systems, and it's included in technical specifications from the beginning of the software design process.

As a part of implementation, the load test agent is updated to include coverage for the feature or system. A load test is then run with results being compared to baselines.

The code changes are then reviewed by at least two developers and a SDET/QA analyst before being merged.

Once merged, a new build is created and deployed the next day to the `Mattermost Community Server <https://community.mattermost.com>`__ where any impacts on performance are monitored for 3-4 weeks before the changes are included in a release candidate.


Database schema changes
-----------------------

Database schema changes are kept to a minimum to reduce risk on upgrades and impact on performance. When a change in schema is required, Mattermost follows `strict migration guidelines <https://developers.mattermost.com/contribute/more-info/server/schema-migration-guide/>`__ that minimize risk and prevents performance impact during and after migrations.

If a more involved migration is required, detailed analysis is performed and published with guidance. An example analysis is the `Mattermost v6.0 schema migration <https://gist.github.com/streamer45/59b3582118913d4fc5e8ff81ea78b055>`__.

Additionally, all database schema changes are load tested as a part of our monthly release process.


Monitoring post-release
-----------------------

After a new version of Mattermost is released, it is rolled out to Mattermost Cloud customers over a multi-week period. During roll out, performance and error rate metrics are monitored for any unexpected changes. If any user-impacting changes are observed, the release is reverted and the deviations are investigated with any fixes being delivered as a part of patch release.

In addition, Mattermost channels, user forums, and support tickets are closely monitored for reports of any issues. Any reports are investigated and resolved appropriately.
