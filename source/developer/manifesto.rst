==============================================
Mattermost Manifesto
==============================================

Mattermost is an open source, private cloud alternative to proprietary communication services. Hundreds of contributors around the world help develop the software in 11 languages. 

Mattermost Team Edition is an open source workplace messaging solution. Combined with native Mattermost apps on mobile and desktop, it brings all your team communication to one place, with web, mobile and PC interfaces, continuous archiving, instant search and a host of 3rd party integrations. It deploys as a single Linux binary under MIT license, with either MySQL or PostgreSQL as a database. 

Mattermost Enterprise Edition is a commercial extension of the Mattermost software offering enterprise-grade messaging and advanced security, configurability and scalability benefits beyond the scope of team communication. 

History 
---------------

The project was `created by a video game company <https://www.mattermost.org/why-we-made-mattermost-an-open-source-slack-alternative/>`_ who previously used a proprietary, SaaS-based messenger which was bought by a big company and neglected. The SaaS messenger started having outages, it crashed, it lost files, and export didn't work. When they stopped their subscription, the SaaS messenger paywalled them from their own data. 

Lesson learned, the company started using messaging software they'd developed for their video game players, and eventually open sourced the software in 2015. The software because surprisingly popular and eventually the company left the video game business, renamed itself "Mattermost, Inc." and shifted focus to expanding the open source project, funded by creating commercial Enterprise Edition extensions. 

Because of how we started, we're committed to never allowing commercial versions of Mattermost to lock in user's data--organizations using Mattermost must always have full access to their information and be able to downgrade to the open source version to continue accessing their information. 

Design Principles 
------------------

The work of the Mattermost open source project is governed by key principles: 

1. Anywhere office empowering trusted teams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"Anywhere office" means team members should be able to access the software across web, mobile and PC from wherever you are (eventually offline as well). "Empowering trusted team" means enabling people to achieve what the team needs without limits or monitoring. Features needed to enforce corporate policy (e.g. sophisticated permissions, etc.), degrade the team experience and aren't included. 

2. Primary, not secondary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The purpose of Mattermost is to become the primary way a team communicates. It's for vital conversations that "matter most". Deployment as a secondary system, where not everyone in a team can be reached, fails to achieve the software's purpose. Because of this we don't offer email as a Mattermost interface (impoverished experience). Also, while you can use your Mattermost account to sign-in to other apps via features like OAuth2 provider support, we don't offer SSO into Mattermost from another account [1]. 

[1] There is an exception with GitLab SSO, which is a legacy feature from an early partnership. 

3. Private cloud alternative
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your vital communications stay behind your firewall, on infrastructure you control. We should constantly invest in simplifying install and maintenance to eventually create a fully-automated "private SaaS" deployment model that is extremely easy to administer and 100% under your control. 

Mattermost Team Edition is focused on private cloud deployment over public web because we believe: a) public web security threats are constantly escalating, b) admins don't always have time to apply security updates, c) Mattermost contains your most important communications. 

4. Minimalist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Minimalism is providing just the right amount of functionality and not more and not less. Make decisions instead of providing options. Every time you present an option, you force the user to make a decision which can lead to frustration if it's not for the majority of users. Great design is about doing important things extremely well, and not many things poorly. 

That said, Mattermost should offer APIs, drivers, and a plug-in architecture that enables a wide range of add-on functionality aligned with Mattermost design principles. 

