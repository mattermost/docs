General Mattermost questions
============================

.. contents:: On this page
    :backlinks: top
    :depth: 2

Why was Mattermost created?
---------------------------

Mattermost was created to offer an alternative to proprietary SaaS services. For more information, please see the article `Why we built Mattermost <https://mattermost.com/about-us/>`__.

Why does the open source repository contain code specific to the commercial version of Mattermost?
---------------------------------------------------------------------------------------------------

The commercial version of Mattermost is designed to never lock-in your data. Portions of the commercial version are shared with the open source version to ensure upgrade and downgrade across editions happens without data loss.

Does Mattermost support 508 Compliance?
---------------------------------------

Yes, please see our `VPAT </about/vpat.html>`__ form for details. Mattermost Enterprise Edition has been purchased by multiple US public sector organizations, including US federal agencies and the Department of Defense.

What's the largest Mattermost deployment you have?
--------------------------------------------------

Our largest contractual obligation is for over a quarter of a million registered users. Our most typical large enterprise deployment size is between 10,000 and 40,000 users in Dev and Ops organizations who use Mattermost for DevOps workflows, remote work, mission-critical and rapid response, and to address email overload.

We have done performance testing of 60,000 concurrent users and 60 million posts in the database, with a peak concurrent utilization safety factor of between 10 to 1 and 3 to 1, depending on the distribution of an organization across time zones. Peak concurrent usage in a single timezone is generally around the start of the day, probably 9am, and lunchtime when people are messaging to meet for a meal. Our monthly releases are tested at 20 million posts in the database.

Mattermost provides an open source, well-documented `load test simulator <https://github.com/mattermost/mattermost-load-test>`_ to verify that your Mattermost deployment can achieve the stated scale benchmarks ahead of production deployment.

How do I deploy the open source Mattermost Team Edition under an MIT license?
-----------------------------------------------------------------------------

The open source Mattermost Team Edition is functionally identical to the commercial Mattermost Enterprise Edition in its free “team mode”, but there is no ability to unlock enterprise features. It deploys as a single Linux binary with PostgreSQL under an MIT license.

We generally recommend installing Enterprise Edition, even if you don't currently need a license. This provides the flexibility to unlock Enterprise features seamlessly should you need them. However, if you only want to install software with a fully open source code base, then Team Edition is the best choice for you.

To deploy the Team Edition, download the `Mattermost Team Edition binary </upgrade/version-archive.html#mattermost-team-edition>`_, and follow our standard install guides. The same applies to server upgrades.

What are the limitations for embargoed countries?
-------------------------------------------------

We greatly appreciate your interest in Mattermost. Due to recent sanctions from the United States government, we must pause interactions with your organization until the sanctions are lifted.

This includes:

- We must pause on selling, issuing, or renewing a Mattermost license key to your organization. If you have a Mattermost license key, or a trial key, we ask that you do not use it.
- We are not permitted to provide you technical support for our software. Moreover, we cannot answer questions about our software.
- We are not permitted to provide our software, including any updates, upgrades or cloud-hosted versions to your organization. We must ask that you do not use any software or online services provided by Mattermost, Inc., including any versions that have been provided online to the general public.

We deeply apologize for the inconvenience. We must abide by United States laws. We hope after sanctions are lifted that we can support your interest once again. Please reach out to compliance@mattermost.com for any questions around current export limitations.
