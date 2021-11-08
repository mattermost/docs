General Mattermost Questions
============================

Why was Mattermost created?
---------------------------

Mattermost was created to offer an alternative to proprietary SaaS services. For more information, please see the article `Why we built Mattermost <https://mattermost.com/about-us/>`__.

Why does the open source repository contain code specific to the commercial version of Mattermost?
---------------------------------------------------------------------------------------------------

The commercial version of Mattermost is designed to never lock-in your data. Portions of the commercial version are shared with the open source version to ensure upgrade and downgrade across editions happens without data loss.

Does Mattermost support 508 Compliance?
---------------------------------------

Yes, please see our `VPAT <https://docs.mattermost.com/about/vpat.html>`__ form for details. Mattermost Enterprise Edition has been purchased by multiple US public sector organizations, including US federal agencies and the Department of Defense.

What's the largest Mattermost deployment you have?
--------------------------------------------------

Our largest contractual obligation is for over a quarter of a million registered users. Our most typical large enterprise deployment size is between 10,000 and 40,000 users in Dev and Ops organizations who use Mattermost for DevOps workflows, remote work, mission-critical and rapid response, and to address email overload.

We have done performance testing of 60,000 concurrent users and 60 million posts in the database, with a peak concurrent utilization safety factor of between 10 to 1 and 3 to 1, depending on the distribution of an organization across time zones. Peak concurrent usage in a single timezone is generally around the start of the day, probably 9am, and lunchtime when people are messaging to meet for a meal. Our monthly releases are tested at 20 million posts in the database.

Mattermost provides an open source, well-documented `load test simulator <https://github.com/mattermost/mattermost-load-test>`_ to verify that your Mattermost deployment can achieve the stated scale benchmarks ahead of production deployment.

How do I deploy the open source Mattermost Team Edition under an MIT license?
-----------------------------------------------------------------------------

The open source Mattermost Team Edition is functionally identical to the commercial Mattermost Enterprise Edition in its free “team mode”, but there is no ability to unlock enterprise features. It deploys as a single Linux binary with MySQL or PostgreSQL under an MIT license.

We generally recommend installing Enterprise Edition, even if you don't currently need a license. This provides the flexibility to unlock Enterprise features seamlessly should you need them. However, if you only want to install software with a fully open source code base, then Team Edition is the best choice for you.

To deploy the Team Edition, download the `Mattermost Team Edition binary <https://docs.mattermost.com/upgrade/version-archive.html#mattermost-team-edition>`_, and follow our standard install guides. The same applies to server upgrades.