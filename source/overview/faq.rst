Frequently Asked Questions (FAQ)
=================================

.. toctree::
  :maxdepth: 2

General Questions
-----------------

Why was Mattermost created?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost was created to offer an alternative to proprietary SaaS services. For more information, please see the article `Why we made Mattermost <https://www.mattermost.org/why-we-made-mattermost-an-open-source-slack-alternative/>`_.

Why does the open source repository contain code specific to the commercial version of Mattermost?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The commercial version of Mattermost is designed to never lock-in your data. Portions of the commercial version are shared with the open source version to ensure upgrade and downgrade across editions happens without data loss.

Does Mattermost support 508 Compliance? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, please see our `VPAT <https://docs.mattermost.com/overview/vpat.html>`_ form for details. Mattermost Enterprise Edition has been purchased by multiple US public sector organizations, including US federal agencies and the Department of Defense. 

What's the largest Mattermost deployment you have?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our largest contractual obligation is for over a quarter of a million registered users. Our most typical large enterprise deployment size is between 10,000 and 40,000 users in Dev and Ops organizations who use Mattermost for DevOps workflows, remote work, mission-critical and rapid response, and to address email overload.

We test to 60,000 concurrent users regularly, and have a peak concurrent utilization safety factor of between 10 to 1 and 3 to 1, depending on distribution of an organization across time zones. Peak concurrent usage in a single timezone is generally around start of day, probably 9am, and lunch time when people are messaging to meet for a meal.

Mattermost provides an open source, well-documented load test simulator to verify that your Mattermost deployment can achieve the stated scale benchmarks ahead of production deployment. 

Community Questions
-------------------

How can I get involved or contribute to Mattermost? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can get involved and contribute to Mattermost in the following ways:

- Contribute Code
- Find "Help Wanted" projects
- Join Developer Discussion on a Mattermost Server for contributors
- File Bugs
- Share Feature Ideas
- Get Troubleshooting Help
- Help translate Mattermost

See the `Get Involved <https://github.com/mattermost/mattermost-server#get-involved>`_ section of the Mattermost GitHub README for more information.

Can contributors add themselves to the Mattermost company page on LinkedIn? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes! If you have contributed to the Mattermost project we think you should be recognized for it professionally beyond GitHub.
To add yourself to the Mattermost company page on LinkedIn, do the following:

1. Login to LinkedIn or create an account.
2. Go to "Me" > "View profile"
3. Under Experience, click on “plus” symbol and edit the following:
  - Title: Developer (if you contributed code or created a plug-in, integration, or other enhancement), Contributor (if you've contributed without writing code--e.g. filed bug report, updated documentation, supported troubleshooting questions, proposed a feature, etc.) 
  - Company: Find “Mattermost” (you’ll see the Mattermost logo)
  - Location: Enter where you live
  - From: Date of first contribution or perhaps month you cloned github.com/mattermost
  - I currently work here: Check
  - Update my industry: Leave unchecked
  - Update my headline: Leave unchecked
  - Description: Leave blank or write a sentence about what you have contributed. 

Mobile Applications
-------------------

Are push notifications free?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, push notifications are free if you compile your own `push-proxy service <https://github.com/mattermost/mattermost-push-proxy>`_. Push notifications are also free if you use the hosted Test Push Notification Service (TPNS) provided by Mattermost, Inc.

TPNS, hosted at ``http://push.mattermost.com``, doesn't offer transport-level encryption or production-level service level agreements (SLAs), so if you choose this option we recommend you configure your system to not include message contents in push notifications and not rely on the service for vital functions.

If you need encrypted transport or production-level SLAs for push notifications, you can either compile your own push-proxy service, with your own key, or you can use a paid option and become a Mattermost Enterprise Edition E10 subscriber `agreeing to our Conditions of Use <https://about.mattermost.com/default-terms/>`_, which enables you to use a production-level Hosted Push Notification Service (HPNS) at ``https://push.mattermost.com``, offering transport-level encryption.

Learn more about `our mobile apps and push notification service <https://docs.mattermost.com/deployment/push.html>`_.

Video, Audio, and Screen Sharing
----------------------------------------

What support is available for video and audio calling and screen sharing?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In all editions, open source `one-on-one video and audio calling is currently available in beta <https://docs.mattermost.com/deployment/webrtc.html>`_ using the WebRTC standard.

After many conversations with users and customers we realized:

1. Most people using Mattermost need top quality video/audio/screen sharing solutions, which are predominantly proprietary.
2. Integrating an organization's choice of video/audio/screen sharing solution is paramount.

Today, you can neatly link video/audio/screen sharing solutions, like Zoom and Skype for Business, to channels by using markdown formatting the header (Example: ``[Click for video call](https://link_to_solution)``).

In future, we plan to add:

- A plug-in option for user profiles to connect directly to a person using 3rd party video/audio/screen sharing products, including custom and phone-based solutions.
- A plug-in option for linking channels and teams to on-demand video/audio/screen sharing solutions
- A default, open source one-on-one video and audio calling plug-in based on WebRTC
- A directory of 3rd party video/audio/screen sharing solutions that plug-in to Mattermost

The timeline for these additions would not be before the second half of 2017.

Enterprise Edition
------------------

What is Mattermost Enterprise Edition?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Mattermost Enterprise Edition is a commercial workplace messaging solution for large organizations operating under compliance and security requirements that is built on top of the open source Mattermost Team Edition.

How can I be assured that my data will not be locked in to commercial software?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Users of Mattermost Enterprise Edition can downgrade to the open source version without losing any data. Moreover, you always have control over your server and database, where the entirety of your Mattermost deployment is stored.

How does Mattermost scale from teams to enterprises?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Growing your Mattermost installation from supporting a team to supporting an enterprise requires two types of scaling:

    1. Technical scaling - maintaining system responsiveness as large quantities of new users are added
    2. Functional scaling - adding advanced features to support the increased complexity of large organizations

    **Technical Scaling** - Whether used for teams or enterprises, the Mattermost server is designed to support tens of thousands of users on a single server with appropriate hardware. The server is built using Golang, the language developed by Google to create internet-scale applications, and supports highly scalable databases like MySQL, which is `used extensively by Facebook <https://www.facebook.com/notes/facebook-engineering/mysql-and-database-engineering-mark-callaghan/10150599729938920/>`_. Beyond tens of thousands of users,  Mattermost Enterprise Edition can offer high availability/horizontal scaling configurations using multiple servers to support even larger organizations.

    **Functional Scaling** - Scaling from a team to an enterprise is like going from a "virtual office" to a "virtual campus". Advanced features like enterprise authentication, granular permissions, compliance and auditing, and advanced reporting become increasingly important as organizations grow beyond teams. Organizations needing this flexibility can easily upgrade from Mattermost Team Edition to Mattermost Enterprise Edition, as well as downgrade without data loss, should their needs change.

    For more information on how Mattermost scales, technically and functionally, please `contact the Enterprise team <https://about.mattermost.com/contact/>`_ and `read about scaling for Enterprise <https://docs.mattermost.com/deployment/scaling.html>`_.

What does it take to manage a Mattermost deployment? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a small deployment of Mattermost up to a few hundred users, we'd recommend a part-time, mid-level IT admin, with a senior IT admin for supervision and as a backup resource. They should have the ability to administer a basic Linux server, a MySQL or PostgreSQL database, and web proxy configuration with web sockets.

For a medium deployment of 500 to 2000 users, we'd recommend a senior IT administrator who has the capability to configure Mattermost in a high-availability cluster with redundant database and application servers. They should also be able to activate performance monitoring and health check features in Prometheus and Grafana. 

How do you manage multiple messaging solutions in an enterprise? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our customers address multiple collaboration solutions in different ways depending on whether the organization is more tops down or bottoms up. 

**For tops-down, customers want to simplify and leverage investments in a central, flexible, innovative solution that can scale**. There's generally a lot of pain with different teams and departments running their own messaging tools, creating silos, redundancy and significant productivity loss. They'll roll out Mattermost as an official solution and centralize communication there. For an example of this, see our `Uber case study <https://about.mattermost.com/blog/how-uber-uses-mattermost-to-enhance-enterprise-wide-communications/>`_.

**For bottoms-up, customers want to supplement for strategic advantage**. We've seen teams flock to Mattermost because of its productivity benefits for DevOps, remote work, rapid response, and scaling large teams where people are overloaded with email. Those organizations, which can have hundreds to thousands of users, will use Mattermost in parallel with general purpose messaging that doesn't meet their specific needs. One example is Wargaming, one of the world's largest operators of real-time online video games, with over a 150 million players on their system. They've moved their DevOps, design, analytics and support teams to Mattermost as a supplement to Skype for Business. This is their company-wide, general purpose messenger, that isn't optimized for large DevOps organizations and the degree of integration and flexibility that they need -- specifically for DevOps. People want support for Linux and Mac desktops, lots of APIs and hooks to integrate, plug-ins to embed certain types of reports and interactive controls into messages, friendly keyboard shortcuts and dozens of other enhancements that provide a distinct advantage to their counterparts at other companies. 

What are the options to purchase a subscription to Mattermost Enterprise Edition? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To simplify procurement and to keep prices low, Mattermost offers the following options to purchase: 

1. **Purchasing a subscription online via credit card** (https://about.mattermost.com/pricing/) under standard Mattermost terms (https://about.mattermost.com/enterprise-edition-terms/) used by hundreds of other Enterprise Edition customers. 

2. **Purchasing via a Mattermost reseller** (https://about.mattermost.com/partners/) under terms agreed between the customer and reseller, and then agreeing to **Mattermost Enterprise Edition Subscription Terms for Purchase by Resale** (https://about.mattermost.com/customer-terms-and-conditions/) prior to being provided a license key for the purchase by Mattermost, Inc. 

3. **Purchase via a purchase order referencing a Mattermost quotation number**, and where the quotation is valid, unexpired and references the **Mattermost Enterprise Edition Subscription Terms** (https://about.mattermost.com/enterprise-edition-terms/): 

   i. If the PO references any special terms and conditions, it cannot be accepted by Mattermost, Inc. without the following special note: ``This Purchase Order is governed solely by the terms and conditions of the Mattermost Enterprise Edition Subscription Terms at https://about.mattermost.com/enterprise-edition-terms/. Despite anything to the contrary, no other terms and conditions printed on, or incorporated into or referenced by, shall apply.``

4. **Purchase via a purchase order referencing a Master Services Agreement** or similar agreement executed by Mattermost and the customer for subscription purchases over $100,000 USD. 

   i. If the PO references any special terms and conditions, it cannot be accepted by Mattermost, Inc. without the following clause included in the prior signed agreement: ``THE PARTIES AGREE THAT ANY ADDITIONAL OR DIFFERENT TERMS AND CONDITIONS CONTAINED ON OR INCORPORATED INTO YOUR PURCHASE ORDER ARE EXPRESSLY REJECTED AND SHALL NOT BE CONSIDERED AN AMENDMENT TO THIS AGREEMENT.`` If the agreement does not include such a clause the following purchase order note is required: ``This purchase order is governed solely by the terms and conditions of the [AGREEMENT_TITLE] dated [AGREEMENT_DATE] between [CUSTOMER_NAME] and Mattermost, Inc..  All other terms and conditions contained on or referenced by this purchase order shall not apply.``

How does the licensing key work?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See our `frequently asked questions about licensing <https://about.mattermost.com/pricing/#frequently-asked-questions-about-licensing>`_.

What happens when the Enterprise Edition subscription expires?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See our `frequently asked questions about licensing <https://about.mattermost.com/pricing/#frequently-asked-questions-about-licensing>`_.

How is user defined for Enterprise Edition subscriptions?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See our `frequently asked questions about licensing <https://about.mattermost.com/pricing/#frequently-asked-questions-about-licensing>`_.

How can I add more users to my subscription?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See our `frequently asked questions about licensing <https://about.mattermost.com/pricing/#frequently-asked-questions-about-licensing>`_.

Do I need to pay for deactivated users?  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. If you deactivate a user that user is not counted as an active user during your annual renewal process. You can deactivate users manually via System Console and also via Active Directory/LDAP synchronization, the CLI tool and the server APIs. 

If you choose to pull SQL reports from the database to monitor individual activity to make deactivation decisions, and you are running under high user load, we recommend the reports are pulled from a read replica of the database.

Can I use the same license key on multiple Enterprise Edition servers?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Customers who purchase the Premier Support add-on to E20 are licensed to run with the same Mattermost license key in a production deployment and up to 4 non-production deployments of Mattermost (for example: development, staging, user acceptance testing, etc.).

Without the purchase of Premier Support, license keys for unlocking the advanced features in Mattermost Enterprise Edition should only be applied to a single deployment. A deployment consists of either a single Mattermost application server, or multiple linked Mattermost application servers in a high availability configuration.

Do you have a program for official non-profits and charities?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See our `frequently asked questions about licensing <https://about.mattermost.com/pricing/#frequently-asked-questions-about-licensing>`_.

Do you have discounted licenses for academic institutions?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See our `frequently asked questions about licensing <https://about.mattermost.com/pricing/#frequently-asked-questions-about-licensing>`_.

Where can I find the license agreement for Mattermost Enterprise Edition?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See our `frequently asked questions about licensing <https://about.mattermost.com/pricing/#frequently-asked-questions-about-licensing>`_.

Integration
------------------

Can I use Mattermost to add messaging functionality to my proprietary SaaS service?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost is an open source, self-hosted alternative to proprietary SaaS services that lock in the data of users and customers.

While you're welcome to use the Mattermost source code under its open source license, Mattermost, Inc. does not offer support or technical advice for proprietary SaaS projects that result in customers potentially being paywalled from their data should they stop paying SaaS fees.

To learn more about why we strongly believe that users and customers should always have access to their data, please read `why we created Mattermost <https://www.mattermost.org/why-we-made-mattermost-an-open-source-slack-alternative/>`_

Use Cases
------------------

Does Mattermost support external guests?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not yet. Guest accounts are a feature planned for Enterprise Edition. A pricing model proportional to a fraction of the value this new feature provides is expected. 

Can I use Mattermost for customer service?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You are welcome to use the open source Mattermost Team Edition and its extensive API library to build your own solution.

Mattermost Enterprise Edition is designed for self-hosted, enterprise-grade communication. It is not recommended for primarily providing customer service or customer support, and does not currently offer a licensing model nor technical advice for this use case.

If you'd like to create an open source derivative version of Mattermost using the ``/mattermost-server`` source code to support your use case please see below. 

Does Mattermost have an official website-based plug-in to offer anonymous chat to visitors?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not yet. You can `upvote the feature proposal online <https://mattermost.uservoice.com/forums/306457-general/suggestions/8810731-implement-a-site-chat-feature>`_ to add your support. If you create such a plug-in, we would love to see it open sourced and made available to the community. 


Design Decisions
----------------

Why does Mattermost disclose whether or not an account exists when a user enters an incorrect password?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost's core design principle is to be `"fast, obvious, forgiving" <https://docs.mattermost.com/developer/fx-guidelines.html#fast-obvious-forgiving>`_ and, telling users that they made a mistake in entering their password, is in service of our principle of prioritizing user interests. 

When using username-password authentication, especially with AD/LDAP, there's the possibility of usernames being email addresses, Mattermost username, AD/LDAP username, AD/LDAP ID or other AD/LDAP attributes and our design principle intends to help end users understand if their login error came from having the wrong password or the wrong email/username.

We believe this design increases productivity, speeds up user adoption and reduces help desk tickets and support costs and that these benefits outweigh the trade-offs. 

The trade-off with this design is that if physical security is not in effect, and network security is not in effect (i.e. no VPN, or a malicious user within the private network), and username-password authentication is used, an attacker may be able to enumerate email addresses or usernames by sending HTTP requests to the system, up to the maximum number of requests per second defined in Mattermost's `API rate limiting settings <https://docs.mattermost.com/administration/config-settings.html#rate-limiting>`_. 

For organizations who choose to deploy in such a configuration, please consider the following mitigations: 1) instead of username-password, use a single-sign-on provider in Mattermost Enterprise Edition like OneLogin, Okta or ADFS, use the open source GitLab SSO option available with Mattermost Team Edition, 2) per the recommended install instructions, use a VPN client to apply network security to your deployment, 3) enable monitoring and alerting from your proxy server to detect and isolate malicious behavior reaching your deployment. 

Above all, make sure to subscribe to the `Mattermost Security Bulletin <https://about.mattermost.com/security-bulletin/>`_ and apply security patches as recommended.  

Business Questions
------------------

How can I create an open source derivative work of Mattermost?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're looking to customize the look and feel of Mattermost, see `documentation on customization <https://github.com/mattermost/docs/issues/1006>`_. For advanced customization, the user experience of the system is available in different repositories for web, mobile apps and desktop apps, and custom experiences can be developed and integrated with either Mattermost Team Edition or Mattermost Enterprise Edition via the system APIs and drivers. 

If, instead of using Mattermost Team Edition or Mattermost Enterprise Edition, you choose to compile your own version of the system using the open source code from ``/mattermost-server``, there are a number of factors to consider: 

Security

- If you run a fork of the Mattermost server we highly recommend you only deploy the system securely behind a firewall and to pay close attention to `Mattermost security updates <http://about.mattermost.com/security-updates/>`_. Mattermost Team Edition and Mattermost Enterprise Edition release security update patches when reports of new attacks are received and verified. Mattermost waits until 14 days after a security patch is released before publicly detailing its nature, so that users and customers can upgrade before the security vulnerability is widely known. A malicous user can potentially make use of Mattermost security disclosures to exploit a fork of Mattermost if the security upgrade is not promptly incorporated into the forked version. 

Re-branding

- When you create a derivative version of Mattermost and share it with others as a product, you need to replace the Mattermost name and logo from the system, among other requirements, per the `Mattermost trademark policy. <https://www.mattermost.org/trademark-standards-of-use/>`_
- In Enterprise Edition you can re-brand your system using convenience tools for `custom branding <https://docs.mattermost.com/administration/config-settings.html#customization>`_.
- For advanced whitelabelling, and to whitelabel in Team Edition under MIT license without Enterprise Edition branding tools, you can manually update files on the Mattermost server `per product documentation. <https://github.com/mattermost/docs/issues/1006>`_ This can also be done without forking. 

Copyright and Licensing of ``/mattermost-server`` open source code

- Compiling and distributing your own version of the open source Mattermost ``/mattermost-server`` repo requires a) compliance with licenses in the repo, including `NOTICE.txt <https://github.com/mattermost/mattermost-server/blob/master/NOTICE.txt>`_, and b) the compiled version of the ``/mattermost-server`` source code should have the same open source license as the source code, `per our licensing policy <https://www.mattermost.org/licensing/>`_.

Other considerations:

- Mattermost has a default `Conditions of Use <https://docs.mattermost.com/administration/config-settings.html#terms-of-service-link>`_ agreement for the Terms of Service link at the bottom of login screen that should be incorporated into any additional Terms of Use you may add.
- The Mattermost copyright notices on the user interface should remain.
- There may be additional legal and regulatory issues to consider and we recommend you employ legal counsel to fully understand what's involved in creating and selling a derivative work.


Will Mattermost complete questionnaires requiring confidential data without an NDA?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, Mattermost will not complete questionnaires requiring confidential data without a non-disclosure agreement. You can find `Mattermost's standard mutual non-disclosure agreement online. <https://docs.google.com/document/d/10Qc2kxxZGYNzp9b19oEhItRM01OPyrWRISJ2rbm1gvc/edit>`_

Why does Mattermost have a discount for certain kinds of non-profits but not for others?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While we welcome anyone to use the open source version of Mattermost Team Edition free of charge, Mattermost, Inc., like any software company, has specific discounting programs for its commercial Mattermost Enterprise Edition based on business objectives. Objectives of the discounting programs include the suitability of potential case studies, references, word-of-mouth promotion as well as public promotion of solutions, among many other factors.

Learn more about our non-profit discount program at https://about.mattermost.com/mattermost-mondays/

Can I create a derivative work of the Mattermost /mattermost-server repository that is not open source? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Mattermost open source project was created by `a group of developers who had their data paywalled by a proprietary online messaging service <https://www.mattermost.org/why-we-made-mattermost-an-open-source-slack-alternative/>`_ and felt it was unfair. 

Because of this, the Mattermost /mattermost-server repository uses an open source license that requires derivative works to use the same open source license. This prevents the creation of derivative works that are not open source, and the situation where end users would not have access to the source code of the systems they use, and hence be at risk of "lock in". 

For companies purchasing Enterprise Edition subscriptions for use by internal staff, who need to modify /mattermost-server, and who also have legal departments that won't allow their staff to work under an open source software license, a special "Advanced Licensing Option" can be purchased to modify /mattermost-server for internal use under a commercial software license. This option is not available for companies that would offer a modified, non-open source version of Mattermost to external parties. 

Will Mattermost, Inc. offer the ability to resell Mattermost software without a reseller agreement?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No.

If there is a case where the reseller agreement is under review and an order is urgently needed by a customer, Mattermost may, with internal approvals, accept a reseller purchase order with the following language:

Any statements, clauses, or conditions included on or referenced by buyer's purchase order forms, which forms modify, add to, or are inconsistent with Mattermost’s standard terms and condtions are expressly rejected. Such orders will only be accepted by Mattermost upon the condition and with the express understanding that despite any such statements,clauses, or conditions contained in any order forms of the buyer are void and have no effect.

EXCEPT AS OTHERWISE EXPRESSLY AGREED BY THE PARTIES IN WRITING, MATTERMOST MAKES NO WARRANTIES OR REPRESENTATIONS WITH RESPECT TO ANY MATTERMOST PRODUCTS, DOCUMENTATION OR SUPPORT, AND HEREBY DISCLAIMS ALL OTHER EXPRESS AND ALL IMPLIED WARRANTIES, INCLUDING BUT NOT LIMITED TO IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.


