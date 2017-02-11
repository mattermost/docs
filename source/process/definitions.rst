.. _definitions:

Levels of Feature Quality, Development, and Support Eligibility
===============================================================

This document defines the terminology that is used when communicating status of features to the Mattermost community. The terminology applies to all editions of Mattermost platform and to Mattermost apps.

.. contents::
  :local:
  :backlinks: top

Feature Quality Levels
----------------------

This list describes the quality levels of Mattermost features, and what can be expected at each level.

Production Level Quality
  - Recommended for use in production environments
  - Eligible for commercial support by `Mattermost, Inc. <https://about.mattermost.com/support/>`_
  - Documentation is complete
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
  - Unknown level of stability
  - Minimal feature set that is not yet complete
  - Little or no documentation available
  - Disabled by default and must be turned on with a run-time feature flag

Feature Development Levels
--------------------------

This list describes what can be expected at the various states of development of Mattermost products and features.

Initial Development
  - Experimental or Beta quality
  - Minimal feature set that is not yet complete
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

Support Eligibility Levels
----------------------------

The following list describes the support levels that are available. Not all features and configurations are eligible for paid support.

Eligible for official support
- Feature is production quality and in either Active Development or Maintenance Mode
- Commercial `Enterprise Edition support <https://about.mattermost.com/support/>`_ is able to cover this feature area
- Community pull requests for fixes are tested and merged

Eligible for Premier Support only
- Early or custom features developed for a specific enterprise (Experimental quality?)
- Beta Level Quality
- Not eligible for standard `Enterprise Edition support <https://about.mattermost.com/support/>`_, only supported via Premier Support agreement

Eligible for peer-to-peer support
- Configuration is unofficial, for example, deployment to an operating system that is not officially supported.
- `Enterprise Edition support <https://about.mattermost.com/support/>`_ will not support the configuration.
