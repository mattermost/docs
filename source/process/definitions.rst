.. _definitions:

Definitions
===========


Feature Quality Levels
----------------------

Production Level Quality
  - Recommended for use in production environments
  - Supported in Mattermost, Inc. SLA
  - Documented
  - Included in security reviews
  - Tested on several platforms
Beta Level Quality
  - Is a work in progress
  - Not recommended in production without `Premier Support <https://about.mattermost.com/support/>`_ engagement with Mattermost, Inc.
  - Minimal documentation
  - Disabled by default and must be turned on with a run-time feature flag
  - Tested thoroughly on a small set of platforms, with tickets and work items drafted, and made available for testing and feedback on additional platforms
Experimental Level Quality
  - Not recommended for use in production
  - Unknown level of stability, and might cause data loss
  - Minimal feature that is not yet complete
  - Little or no documentation available
  - Disabled by default and must be turned on with a run-time feature flag

Feature Development Levels
--------------------------

Initial Development
  - Experimental or Beta quality
  - Improved, minimal features not yet complete
Active Development
  - Production Level quality
  - Tested and released in one or more Mattermost products
  - Improvements and maintenance changes accepted
Maintenance Mode
  - Feature complete, with no updates planned
  - Production Level quality
  - Maintenance changes accepted (bug fixes, security fixes)
Deprecated Feature
  - Will be discontinued
  - Exists only for backwards compatibility with released and supported features

Feature Support Levels
----------------------

Not to be confused with paid product support available for Enterprise Editions.

Official Support
  - Production level quality
  - In Active Development or in Maintenance Mode
  - GitHub Pull Requests are accepted for bug fixes and security fixes
Casual Support
  - Peer-to-peer support on forum.mattermost.org and at pre-release.mattermost.org
  -
