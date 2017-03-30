Frequently Asked Questions (FAQ) 
=================================

General Questions 
-----------------

Why was Mattermost created?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Mattermost was created to offer an alternative to propreitary SaaS services. For more information, please see the article `Why we made Mattermost <https://www.mattermost.org/why-we-made-mattermost-an-open-source-slack-alternative/>`_.

Why does the open source repository contain code specific to the commercial version of Mattermost?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The commercial version of Mattermost is designed to never lock-in your data. Portions of the commercial version are shared with the open source version to ensure upgrade and downgrade across editions happens without data loss. 


Mobile Applications
-------------------

Are push notifications free? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, push notifications are free if you compile your own `push-proxy service <https://github.com/mattermost/mattermost-push-proxy>`_. Push notifications are also free if you use the hosted Test Push Notification Service (TPNS) provided by Mattermost, Inc.

TPNS, hosted at ``http://push.mattermost.com``, doesn't offer transport-level encryption or production-level service level agreements (SLAs), so if you choose this option we recommend you configure your system to not include message contents in push notifications and not reply on the service for vital functions.

If you need encrypted transport or production-level SLAs for push notifications, you can either compile your own push-proxy service, with your own key, or you can use a paid option and become a Mattermost Enterprise Edition E10 subscriber `agreeing to our Conditions of Use <https://about.mattermost.com/default-terms/>`_, which enables you to use a production-level Hosted Push Notification Service (HPNS) at ``https://push.mattermost.com``, offering transport-level encryption. 

Learn more about `our mobile apps and push notification service <https://docs.mattermost.com/deployment/push.html>`_. 


Video, Audio and Screensharing 
----------------------------------------

What support is available for video and audio calling and screensharing?  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In all editions, open source `one-on-one video and audio calling is currently available in beta <https://docs.mattermost.com/deployment/webrtc.html>`_ using the WebRTC standard.  

After many conversations with users and customers we realized: 

1. Most people using Mattermost need top quality video/audio/screensharing solutions, which are predominantly propreitary.   
2. Integrating an organization's choice of video/audio/screensharing solution is paramount. 

Today, you can neatly link video/audio/screensharing solutions, like Zoom and Skype for Business, to channels by using markdown formatting the header (Example: ``[Click for video call](https://link_to_solution)``). 

In future, we plan to add: 

- A plug-in option for user profiles to connect directly to a person using 3rd party video/audio/screensharing products, including custom and phone-based solutions. 
- A plug-in option for linking channels and teams to on-demand video/audio/screensharing solutions 
- A default, open source one-on-one video and audio calling plug-in based on WebRTC 
- A directory of 3rd party video/audio/screensharing solutions that plug-in to Mattermost 

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

    **Technical Scaling** - Whether used for teams or enterprises, the Mattermost platform is designed to support tens of thousands of users on a single server with appropriate hardware. The platform is built using Golang, the language developed by Google to create internet-scale applications, and supports highly scalable databases like MySQL, which is `used extensively by Facebook <https://www.facebook.com/notes/facebook-engineering/mysql-and-database-engineering-mark-callaghan/10150599729938920/>`_. Beyond tens of thousands of users,  Mattermost Enterprise Edition can offer high availability/horizontal scaling configurations using multiple servers to support even larger organizations. 

    **Functional Scaling** - Scaling from a team to an enterprise is like going from a "virtual office" to a "virtual campus". Advanced features like enterprise authentication, granular permissions, compliance and auditing, and advanced reporting become increasingly important as organizations grow beyond teams. Organizations needing this flexibility can easily upgrade from Mattermost Team Edition to Mattermost Enterprise Edition, as well as downgrade without data loss, should their needs change. 

    For more information on how Mattermost scales, technically and functionally, please `contact the Enterprise team <https://about.mattermost.com/contact/>`_ and `read about scaling for Enterprise <https://docs.mattermost.com/deployment/scaling.html>`_.

Can I use Mattermost for customer service? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You are welcome to use the open source Mattermost Team Edition and its extensive API library to build your own solution. 

Mattermost Enterprise Edition is designed for self-hosted, enterprise-grade communication. It is not recommended for primarily providing customer service or customer support, and does not currently offer a licensing model nor technical advice for this use case. 

Integration
------------------

Can I use Mattermost to add messaging functionality to my proprietary SaaS service? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost is an open source, self-hosted alternative to proprietary SaaS services that lock in the data of users and customers. 

While you're welcome to use the Mattermost source code under its open source license, Mattermost, Inc. does not offer support or technical advice for proprietary SaaS projects that result in customers potentially being paywalled from their data should they stop paying SaaS fees. 
 
To learn more about why we strongly believe that users and customers should always have access to their data, please read `why we created Mattermost <https://www.mattermost.org/why-we-made-mattermost-an-open-source-slack-alternative/>`_

Configuration
------------------

Does Mattermost support external guests? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not yet. Guest accounts are a feature planned for Enterprise Edition.

Does Mattermost have an official website-based plug-in to offer annonymous chat to visitors? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not yet. You can `upvote the feature proposal online <https://mattermost.uservoice.com/forums/306457-general/suggestions/8810731-implement-a-site-chat-feature>`_ to add your support. 




Business Questions 
------------------

How can I create a derivative work of Mattermost as my own commercial solution? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is broad question with many topics, here are a few: 

Security

- If you offer Mattermost as a commercial solution we highly recommend you promptly provide customers any `security updates <http://about.mattermost.com/security-updates/>`_ that may be released. 

Enterprise Edition partnership 

- To build your own commercial solution reselling Mattermost Enterprise Edition please `contact us <https://about.mattermost.com/contact/>`_ and let us know what you're considering. Strategic partnerships that won't confuse customers are the most favored. 

Re-branding 

- When you create a derivative version of Mattermost and share it with others as a product, you need to replace the Mattermost name and logo from the system, among other requirements, per the `Mattermost trademark policy. <https://www.mattermost.org/trademark-standards-of-use/>`_ 
- In Enterprise Edition you can re-brand your system using convenience tools for `custom branding <https://docs.mattermost.com/administration/config-settings.html#customization>`_. 
- For advanced whitelabelling, and to whitelabel in Team Edition under MIT license without Enterprise Edition branding tools, you can manually update files on the Mattermost server `per product documentation. <https://github.com/mattermost/docs/issues/1006>`_  

Using /platform open source code 

- Creating a solution using the open source Mattermost /platform repo requires a) compliance with licenses in the repo, including `NOTICE.txt <https://github.com/mattermost/platform/blob/master/NOTICE.txt>`_, and b) the solution remain open source, `per our licensing policy <https://www.mattermost.org/licensing/>`_.

Other considerations: 

- Mattermost has a default `Conditions of Use <https://docs.mattermost.com/administration/config-settings.html#terms-of-service-link>`_ agreement for the Terms of Service link at the bottom of login screen that should be incorporated into any additional Terms of Use you may add. 
- The Mattermost copyright notices on the user interface should remain. 
- There may be additional legal and regulatory issues to consider and we recommend you employ legal council to fully understand what's involved in creating and selling a derivative work. 


Will Mattermost complete questionaires requiring confidential data without an NDA? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, Mattermost will not complete questionaires requiring confidential data without a non-disclosure agreement. You can find `Mattermost's standard mutual non-disclosure agreement online. <https://docs.google.com/document/d/10Qc2kxxZGYNzp9b19oEhItRM01OPyrWRISJ2rbm1gvc/edit>`_ 

