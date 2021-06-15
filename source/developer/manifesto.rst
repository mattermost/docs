About the Mattermost Open Source Project 
========================================

Mattermost is an open source, private cloud alternative to proprietary communication services. Hundreds of contributors around the world help develop the software in over 10 languages. 

- **Mattermost Team Edition** is an open source, private cloud workplace messaging solution designed for deployment by non-technical users with basic IT skills. Combined with native Mattermost apps on mobile and desktop, it brings all your team communication to one place, with web, mobile and PC interfaces, continuous archiving, instant search and a host of 3rd party integrations. It deploys as a single Linux binary under MIT license, with either MySQL or PostgreSQL as a database, with a host of simple, automated deployment options created by our community. 

- **Mattermost Enterprise Edition** is a commercial extension of Mattermost offering enterprise-grade messaging and advanced security, configurability and scalability benefits for sophisticated organizations and users. 

History 
-------

The project was `created by a video game company <https://mattermost.org/why-we-made-mattermost-an-open-source-slack-alternative/>`__ who previously used a proprietary, SaaS-based messenger which was bought by a big company and neglected. The SaaS messenger started having outages, it crashed, it lost files, and export didn't work. When they stopped their subscription, the SaaS messenger paywalled them from their own data. 

Lesson learned, the company started using messaging software they'd developed for their video game players, and eventually open sourced the software in 2015. The software became surprisingly popular and eventually the company left the video game business, renamed itself "Mattermost, Inc." and shifted focus to expanding the open source project, funded by creating commercial Enterprise Edition extensions. 

Because of how we started, we're committed to never allowing commercial versions of Mattermost to lock in a user's data--organizations using Mattermost must always have full access to their information and be able to downgrade to the open source version.

Stewardship Principles for the Mattermost Open Source Project  
--------------------------------------------------------------

Mattermost, Inc. is for-profit company focused on making the open source `Mattermost Team Edition <https://docs.mattermost.com/overview/product.html#mattermost-editions>`__ highly successful and popular for teams, while also generating revenue for our commercial `Mattermost Enterprise Edition <https://docs.mattermost.com/overview/product.html#mattermost-editions>`__ for large and sophisticated organizations. 

The following stewardship principles for our open source work helps keep our intent and purpose clear: 

1. Never locked-in 
~~~~~~~~~~~~~~~~~~~

Mattermost software, whether open source or commercial, should never withhold an organization's data from the organization. Commercial versions of Mattermost should always have a path to downgrade to the open source version without loss of access to data. 

2. Quick Time-to-Value 
~~~~~~~~~~~~~~~~~~~~~~

Great software creates value quickly. A non-technical user with basic IT skills should be able to set up Team Edition, understand every feature in the UI, and roll out the product and increase team productivity in just a few minutes. We should automate as much as possible in a standard install, ask few technical questions, and provide full explanations for any decisions that need to be made.  

3. Minimalist
~~~~~~~~~~~~~~

Minimalism is providing the correct amount of functionality and not more and not less. Great design is about doing important things extremely well, and not many things poorly. Make features work well for their intended purpose before adding new features. 

4. Decisions not options
~~~~~~~~~~~~~~~~~~~~~~~~

Make decisions instead of providing options. Every time you present an option, you force the user to make a decision which can lead to frustration if it's not for the majority of users. 

5. Built for teams behind firewalls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Team Edition is built for teams needing a modern communication experience secured behind a firewall. For our target audience, we should be by far the best solution in the world. 

6. No surprises 
~~~~~~~~~~~~~~~

Users should never run into anything unexpected with Mattermost. We ship on time and document our features and product changes. Users should be able to know well in advance what is being considered for inclusion and change in upcoming versions. 

7. Near zero administration 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let people work simply. Team Edition is for teams needing a "virtual office" where everyone knows each other and is trusted to get things done appropriately, without hard limits and policies. The non-technical user who deployed Team Edition should spend zero time on any administration tasks. 

8. Open source alternative  
~~~~~~~~~~~~~~~~~~~~~~~~~~

For non-technical users with basic IT skills, Team Edition aspires to be an ideal workplace messaging solution deployed on a private network, emphasizing simplicity and fast time-to-value. For sophisticated organizations with advanced security, configurability and scalability needs, the commercial Enterprise Edition extension strives to be an ideal solution. 

For organizations who seek other options, full source code of the server and webapp for creating Team Edition should be available for the development of open source variants, including commercial variants, `provided the Mattermost trademark is not used and other protocols are respected. <https://docs.mattermost.com/overview/faq.html#can-i-create-a-derivative-work-of-the-mattermost-mattermost-server-repository-that-is-not-open-source>`__ 

These principles were inspired by WordPress Philosophy: https://wordpress.org/about/philosophy/
