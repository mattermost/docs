Frequently Asked Questions 
==========================

General Questions 
-----------------

Why was Mattermost created?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Mattermost was created to offer an alternative to propreitary SaaS services. For more information, please see the article `Why we made Mattermost <https://www.mattermost.org/why-we-made-mattermost-an-open-source-slack-alternative/>`_.

Why does the open source repository contain code specific to the commercial version of Mattermost?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The commercial version of Mattermost is designed to never lock-in your data. Portions of the commercial version are shared with the open source version to ensure upgrade and downgrade across editions happens without data loss. 

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
