General Mattermost
===================

Why was Mattermost created?
---------------------------

Mattermost was created to offer an alternative to proprietary SaaS services. For more information, please see the article `Why we built Mattermost <https://mattermost.com/about-us/>`_.

Why does the open source repository contain code specific to the commercial version of Mattermost?
---------------------------------------------------------------------------------------------------

The :ref:`commercial version of Mattermost <product-overview/editions-and-offerings:mattermost enterprise edition>` is designed to never lock-in your data. Portions of the commercial version are shared with the :ref:`open source version <product-overview/editions-and-offerings:mattermost team edition>` to ensure upgrade and downgrade across editions happens without data loss.

Does Mattermost support 508 Compliance?
---------------------------------------

Yes. See the :doc:`accessibility compliance policy </product-overview/accessibility-compliance-policy>` documentation for details. Mattermost Enterprise Edition has been purchased by multiple US public sector organizations, including US federal agencies and the Department of Defense.

What's the largest Mattermost deployment you have?
--------------------------------------------------

Our largest contractual obligation is for over a quarter of a million registered users. Our most typical large enterprise deployment size is between 10,000 and 40,000 users in Dev and Ops organizations who use Mattermost for DevOps workflows, remote work, mission-critical and rapid response, and to address email overload.

We have done performance testing of 60,000 concurrent users and 60 million posts in the database, with a peak concurrent utilization safety factor of between 10 to 1 and 3 to 1, depending on the distribution of an organization across time zones. Peak concurrent usage in a single timezone is generally around the start of the day, probably 9am, and lunchtime when people are messaging to meet for a meal. Our monthly releases are tested at 20 million posts in the database.

Mattermost provides an open source, well-documented `load test simulator <https://github.com/mattermost/mattermost-load-test>`__ to verify that your Mattermost deployment can achieve the stated scale benchmarks ahead of production deployment.

How do I deploy the open source Mattermost Team Edition under an MIT license?
-----------------------------------------------------------------------------

The open source Mattermost Team Edition is functionally identical to the commercial Mattermost Enterprise Edition in its free “team mode”, but there is no ability to unlock enterprise features. It deploys as a single Linux binary with PostgreSQL under an MIT license.

We generally recommend installing Enterprise Edition, even if you don't currently need a license. This provides the flexibility to unlock Enterprise features seamlessly should you need them. However, if you only want to install software with a fully open source code base, then Team Edition is the best choice for you.

To deploy the Team Edition, download the :doc:`Mattermost Team Edition binary </product-overview/version-archive>`, and follow our standard install guides. The same applies to server upgrades.

What are the limitations for embargoed countries?
-------------------------------------------------

We greatly appreciate your interest in Mattermost. Due to recent sanctions from the United States government, we must pause interactions with your organization until the sanctions are lifted.

This includes:

- We must pause on selling, issuing, or renewing a Mattermost license key to your organization. If you have a Mattermost license key, or a trial key, we ask that you do not use it.
- We are not permitted to provide you technical support for our software. Moreover, we cannot answer questions about our software.
- We are not permitted to provide our software, including any updates, upgrades or cloud-hosted versions to your organization. We must ask that you do not use any software or online services provided by Mattermost, Inc., including any versions that have been provided online to the general public.

We deeply apologize for the inconvenience. We must abide by United States laws. We hope after sanctions are lifted that we can support your interest once again. Please reach out to compliance@mattermost.com for any questions around current export limitations.

How do I report illicit use of Mattermost software? 
---------------------------------------------------

Illicit use of Mattermost software to harm others, infringe on their rights, break laws or policies is explicitly against our `Terms of Use <https://mattermost.com/terms-of-use/>`__.

If the illicit use is happening on a web address ending in ``“mattermost.com”``, it means the suspected perpetrators are using Mattermost software controlled by our company, Mattermost, Inc. In this case, please get in touch with us at ``support@mattermost.com`` to report the issue for us to investigate.

If the illicit use is happening on a different web address, then it means the suspected perpetrators may be using Mattermost software controlled by a person or company other than Mattermost, Inc. In this case, you need to contact the person or company who controls the web address by using a lookup service such as https://www.whois.com/ to find the contact email to report abuse. You can use a link to this FAQ as a reference to our `Terms of Use <https://mattermost.com/terms-of-use/>`__ policy for Mattermost software.
