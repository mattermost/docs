==============================================
WIP: About the Mattermost Open Source Project 
==============================================

Mattermost is an open source, private cloud alternative to proprietary communication services. Hundreds of contributors around the world help develop the software in over 10 languages. 

Mattermost Team Edition is an open source workplace messaging solution. Combined with native Mattermost apps on mobile and desktop, it brings all your team communication to one place, with web, mobile and PC interfaces, continuous archiving, instant search and a host of 3rd party integrations. It deploys as a single Linux binary under MIT license, with either MySQL or PostgreSQL as a database. 

Mattermost Enterprise Edition is a commercial extension of Mattermost offering enterprise-grade messaging and advanced security, configurability and scalability benefits beyond the scope of team communication. 

History 
---------------

The project was `created by a video game company <https://www.mattermost.org/why-we-made-mattermost-an-open-source-slack-alternative/>`_ who previously used a proprietary, SaaS-based messenger which was bought by a big company and neglected. The SaaS messenger started having outages, it crashed, it lost files, and export didn't work. When they stopped their subscription, the SaaS messenger paywalled them from their own data. 

Lesson learned, the company started using messaging software they'd developed for their video game players, and eventually open sourced the software in 2015. The software because surprisingly popular and eventually the company left the video game business, renamed itself "Mattermost, Inc." and shifted focus to expanding the open source project, funded by creating commercial Enterprise Edition extensions. 

Because of how we started, we're committed to never allowing commercial versions of Mattermost to lock in a user's data--organizations using Mattermost must always have full access to their information and be able to downgrade to the open source version.

Stewardship Principles for the Mattermost Open Source Project  
------------------------------------------------------------------

Mattermost, Inc. is for-profit company that balances the need to improve the open source `Mattermost Team Edition <https://docs.mattermost.com/overview/product.html#mattermost-editions>`_ for teams with the need to add improvements to our commercial `Mattermost Enterprise Edition <https://docs.mattermost.com/overview/product.html#mattermost-editions>`_ to generate income through subscriptions. 

We want both products to be outrageously successful for teams and enterprises respectively. The following stewardship principles (XXX is this the right word?) for our open source work helps keep our intent and purpose clear: 

1. Never locked-in 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost software, whether open source or commercial, should never withhold an organization's data from the organization. Commercial versions of Mattermost should always have a path to downgrade to open source version without loss of access to data. 

2. Quick Time-to-Value 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Great software creates value quickly. Ideally, a novice IT admin should be able to set up Mattermost and roll it out to their team in just a few minutes and it should increase everyone's productivity. We should automate as much as possible in a standard install, ask few technical questions, and provide full explanations for any decisions an IT admin or end user needs to make. 

3. Minimalist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Minimalism is providing just the right amount of functionality and not more and not less. Make decisions instead of providing options. Every time you present an option, you force the user to make a decision which can lead to frustration if it's not for the majority of users. Great design is about doing important things extremely well, and not many things poorly. 

That said, Mattermost should enable options for extending team communication benefits through high quality plug-ins

4. Built for teams on private clouds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost is built for teams who work on private clouds who prefer open source software and need a modern communication experience secured behind a firewall. 

5. No surprises 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users should never run into anything unexpected with Mattermost. We ship on time and document our features and product changes. Users should be able to know well in advance what is included, not included, and changed in upcoming versions. 

6. Empower trusted teams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable people to achieve what the team needs simply. Focus on building trust and education within a team and control via social norms instead of features to force a policy decisions. For large or regulated organizations that require enforcing strict corporate policies, Enterprise Edition can be used. 

7. Primary, not secondary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

XXXX needs work 

The purpose of Mattermost is to be the primary way a team communicates. Deployment as a secondary system, where not everyone in a team can be reached, fails to achieve the software's purpose. Because of this we don't offer features such as using email as a Mattermost interface (impoverished experience). Also, while you can use your Mattermost account to sign-in to other apps via features like OAuth2 provider support, we generally don't offer SSO into Mattermost from another account. 

-----

These principles were inspired by WordPress Philosophy: https://wordpress.org/about/philosophy/

