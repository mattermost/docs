Enterprise Edition questions
============================

What is Mattermost Enterprise Edition?
--------------------------------------

Mattermost Enterprise Edition is a commercial workplace messaging solution for large organizations operating under compliance and security requirements built on top of the open source Mattermost Team Edition.

How can U.S. government customers procure Mattermost licenses? 
--------------------------------------------------------------

Please review our U.S. government offerings at https://mattermost.com/solutions/industries/government/ to contact channel partners and resellers. You can also contact Carahsoft regarding Mattermost by phone or email with the information at https://www.carahsoft.com/mattermost. 

How can government organizations outside the U.S. procure Mattermost licenses?
-------------------------------------------------------------------------------

Governmental organizations outside the U.S. that need to procure licenses through resellers can contact the Mattermost sales organization at https://mattermost.com/contact-sales/ to connect with existing resellers by country and geographic region, or to onboard new approved resellers.

I’d like to buy Mattermost through a reseller--or I am a reseller--how do I get in touch?
-----------------------------------------------------------------------------------------
Please contact the Mattermost sales team at https://mattermost.com/contact-sales/ to find a reseller for your geography and organization. Resellers can read about our partner programs at https://handbook.mattermost.com/operations/sales/partner-programs. 

How are Mattermost licenses sold?
---------------------------------

Mattermost Enterprise and Mattermost Professional licenses are sold as prepaid annual subscriptions based on the number of annual seat licenses purchased, or “seats”. Each seat license purchased entitles a customer to an “activated user”, which is a user registered on a specific Mattermost server and not deactivated. Administrators can view user status in the System Console and activate and deactivate registered users at any time. Deactivated users have history and preferences saved. 

What happens when activated users exceed the number of licensed seats?
-----------------------------------------------------------------------

During the period of the annual license, when the number of activated users exceeds the number of seat licenses purchased, additional seats should be purchased on a quarterly “true forward” basis. 

For example, if activated users exceed licensed seats in the first quarter since annual licenses were purchased, then additional seat licenses should be purchased for the remaining three quarters until renewal, with an invoice amount prorated for the annual cost of the license. 

Where can I find more information on subscriptions and billing?
---------------------------------------------------------------

Please visit ouere :doc:`subscription overview </about/subscription>` documentation for details.

Where can I find a full list of feature comparisons between plans?
-------------------------------------------------------------------

You can see the full list of capabilities by visiting the `Mattermost Pricing page <https://mattermost.com/pricing/>`_.

Does Mattermost have a Software-as-a-Service offering?
------------------------------------------------------

Yes, Enterprises can inquire about `Mattermost Cloud Enterprise <https://mattermost.com/enterprise/cloud/>`_, as a single-tenant cloud-managed service for Mattermost Enterprise hosted by Mattermost, Inc. The system is offered on the same Kubernetes-based platform as the :ref:`self-hosted edition <about/editions-and-offerings:self-hosted editions>`, and managed by Mattermost, Inc. 

For more information, contact the Mattermost Sales organization at https://mattermost.com/contact-sales/

For small businesses, :ref:`Mattermost Professional <about/editions-and-offerings:mattermost professional>` is available as a self-serve, multi-tenant, software-as-a-service offering, which can be purchased with a credit card at https://customers.mattermost.com/cloud/connect-workspace

Do you offer special programs for non-profit organizations, open source projects, or educational institutions?
----------------------------------------------------------------------------------------------------------------

Yes. See the :ref:`Mattermost nonprofit license program <about/subscription:mattermost nonprofit license program>` documentation for details.

How can I be assured that my data will not be locked in to commercial software?
-------------------------------------------------------------------------------

You always have control over your own server and databases, where the entirety of your Mattermost deployment is stored. Users of :ref:`Mattermost Enterprise Edition <about/editions-and-offerings:mattermost enterprise edition>` can downgrade to the :ref:`open source version <about/editions-and-offerings:mattermost team edition>` at any time, without losing any data. 

How does Mattermost scale from teams to enterprises?
----------------------------------------------------

Growing your Mattermost installation from supporting a team to supporting an enterprise requires two types of scaling:

1. Technical scaling: Maintaining system responsiveness as large quantities of new users are added.
2. Functional scaling: Adding advanced features to support the increased complexity of large organizations.

**Technical Scaling:** Whether used for teams or enterprises, the Mattermost server is designed to support tens of thousands of users on a single server with appropriate hardware. The server is built using Golang, the language developed by Google to create internet-scale applications, and supports highly scalable databases. Beyond tens of thousands of users, Mattermost Enterprise Edition can offer high availability cluster-based/horizontal scaling configurations using multiple servers to support even larger organizations.

**Functional Scaling:** Scaling from a team to an enterprise is like going from a "virtual office" to a "virtual campus". Advanced features like enterprise authentication, granular permissions, compliance and auditing, and advanced reporting become increasingly important as organizations grow beyond teams. Organizations needing this flexibility can easily upgrade from Mattermost Team Edition to Mattermost Enterprise Edition as well as downgrade without data loss, should their needs change.

For more information on how Mattermost scales, technically, and functionally, talk to a `Mattermost Expert <https://mattermost.com/contact-sales/>`_, and :doc:`read about scaling for Enterprise </scale/scaling-for-enterprise>`.

What does it take to manage a Mattermost deployment?
----------------------------------------------------

For a small deployment of Mattermost up to a few hundred users, we'd recommend a part-time, mid-level IT admin with a senior IT admin for supervision and as a backup resource. They should have the ability to administer a basic Linux server, a PostgreSQL database, and web proxy configuration with web sockets.

For a medium deployment of 500 to 2000 users, we'd recommend a senior IT administrator who has the capability to configure Mattermost in a High Availability cluster-based deployment with redundant database and application servers. They should also be able to activate performance monitoring and health check features in Prometheus and Grafana.

How do you manage multiple messaging solutions in an enterprise?
----------------------------------------------------------------

Our customers address multiple collaboration solutions in different ways depending on whether the organization is more top down or bottom up.

**For top-down, customers want to simplify and leverage investments in a central, flexible, innovative solution that can scale.** There's generally a lot of pain with different teams and departments running their own messaging tools, creating silos, redundancy, and significant productivity loss. They'll roll out Mattermost as an official solution and centralize communication there. Visit the `Mattermost customers page <https://mattermost.com/customers/>`_ for examples. 

**For bottom-up, customers want to supplement for strategic advantage.** We've seen teams flock to Mattermost because of its productivity benefits for DevOps, remote work, rapid response, and scaling large teams where people are overloaded with email. Those organizations, which can have hundreds to thousands of users, will use Mattermost in parallel with general-purpose messaging that doesn't meet their specific needs.

One example is Wargaming, one of the world's largest real-time online video game operators, with over 150 million players on their system. They've moved their DevOps, design, analytics and support teams to Mattermost to supplement Skype for Business. This is their company-wide, general-purpose messenger that isn't optimized for large DevOps organizations and the degree of integration and flexibility they need - specifically for DevOps. People want support for Linux and Mac desktops, lots of APIs and hooks to integrate. They also need help for plugins to embed certain types of reports and interactive controls into messages, friendly keyboard shortcuts, and dozens of other enhancements that provide a distinct advantage to their counterparts at other companies.
  
What happens when the Enterprise Edition subscription expires?
--------------------------------------------------------------

Sixty days prior to expiry, Mattermost system administrators receive notifications that the Enterprise Edition license key will expire on the anniversary of its purchase. After expiry, there is a 10-day grace period to upload a new license key. After the grace period, Enterprise features will be disabled. At any time, Enterprise Edition can be downgraded to the free Team Edition without data loss by switching off any Enterprise features enabled and then removing the license key.

How does the licensing key work?
--------------------------------

See our :doc:`frequently asked questions about licensing </about/faq-license>`.