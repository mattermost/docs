Frequently Asked Questions 
==========================

General Questions 
-----------------

Why was Mattermost created?
    Mattermost was created to offer an alternative to propreitary SaaS services. For more info, please go to mattermost.org and click "Why we made Mattermost".

Will the open source Team Edition offer more authentication add-ons?
    There are no current plans for auth add-ons for the following reasons: 
    1. Authentication is a critical path that needs to be tested, maintained and supported with each bi-monthly release and volunteers aren't prepared to bear the tax this change would impose on them, and
    2. Such a change increases the difficulty of creating high quality apps and drivers, as developers would be taxed with requests for support, troubleshooting, and debug set ups that would be expensive to reproduce.

Why does the open source repo contain code specific to the commercial version of Mattermost?
    The commercial versionw of Mattermost is designed to never lock-in your data. Portions of the commercial version are shared with the open source version to ensure upgrade and downgrade across editions happens without data loss. 

Enterprise Edition
------------------

What is Mattermost Enterprise Edition?
    Mattermost Enterprise Edition is a commercial workplace messaging solution for large organizations operating under compliance and security requirements that is built on top of the open source Mattermost Team Edition.

How can I be assured that my data will not be locked in to commercial software?
    Users of Mattermost Enterprise Edition can downgrade to the open source version without losing any data. Moreover, you always have control over your server and database, where the entirety of your Mattermost deployment is stored. 

How does Mattermost scale from teams to enterprises?
    Growing your Mattermost installation from supporting a team to supporting an enterprise requires two types of scaling: 

    1. Technical scaling - maintaining system responsiveness as large quantities of new users are added
    2. Functional scaling - adding advanced features to support the increased complexity of large organizations

    **Technical Scaling** - Whether used for teams or enterprises, the Mattermost platform is designed to support tens of thousands of users on a single server with appropriate hardware. The platform is built using Golang, the language developed by Google to create internet-scale applications, and supports highly scalable databases like MySQL, which is `used extensively by Facebook <https://www.facebook.com/notes/facebook-engineering/mysql-and-database-engineering-mark-callaghan/10150599729938920/>`_. Beyond tens of thousands of users,  Mattermost Enterprise Edition can offer high availability/horizontal scaling configurations using multiple servers to support even larger organizations. 

    **Functional Scaling** - Scaling from a team to an enterprise is like going from a "virtual office" to a "virtual campus". Advanced features like enterprise authentication, granular permissions, compliance and auditing, and advanced reporting become increasingly important as organizations grow beyond teams. Organizations needing this flexibility can easily upgrade from Mattermost Team Edition to Mattermost Enterprise Edition, as well as downgrade without data loss, should their needs change. 

    For more information on how Mattermost scales, technically and functionality, please `contact the Enterprise team <https://about.mattermost.com/contact/>`_.
