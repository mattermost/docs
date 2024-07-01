Editions and offerings 
======================

Mattermost is an open core platform. 

This means we develop both an open source, self-hosted edition of our software provided free to our community, as well as a commercial edition that extends and enhances our open source software with paid, subscription-based offerings available both in self-hosted and cloud deployment modes.

You can choose between one of two compiled code bases, either open source (`Team Edition <#mattermost-team-edition>`__) or commercial (`Enterprise Edition <#mattermost-enterprise-edition>`__).

We offer a range of `plans <#mattermost-plans>`__, which are sets of features and entitlements available either free or as a paid subscription service. Mattermost sells subscriptions for both self-hosted and cloud deployments.

Self-hosted editions
--------------------

Self-hosted editions support deploying Mattermost within IT-controlled private environments in public clouds, including AWS, Azure, GCP and Oracle Cloud, as well as on-premises in private clouds and virtual or physical servers. When you're using a self-hosted deployment, a license file is provided and needs to be uploaded to activate your subscription.

For customers using our service in a self-hosted deployment, the `Mattermost Free <#mattermost-free>`__ offering is available in both our open source and commercial code bases (called `Mattermost Team Edition <#mattermost-team-edition>`__ and `Mattermost Enterprise Edition <#mattermost-enterprise-edition>`__, respectively). 

Mattermost Enterprise Edition 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our commercial, self-hosted software is called Mattermost Enterprise Edition, and it's available as a Linux binary that deploys identically to our open source version - including upgrading in an identical fashion - with two key differences: It contains code for advanced commercial features and it's offered under a commercial license (https://mattermost.com/enterprise-edition-license/). The commercial license prohibits reverse engineering and tampering with our license key mechanism unlocking paid features so that we can run a compliant and fair commercial business.

Once you’ve downloaded and installed Mattermost Enterprise Edition within your preferred environment, you have the option to use it as-is in a "free" mode, or you can access Mattermost's commercial features by starting a trial or by purchasing a subscription. You can start a 30-day free Enterprise trial via **System Console > Edition and License > Start trial**, or request a trial online at https://mattermost.com/trial/.

Mattermost Team Edition
~~~~~~~~~~~~~~~~~~~~~~~

Team Edition is a free-to-use, open source, self-hosted collaboration platform offering all the core productivity benefits of competing SaaS solutions. It deploys as a single Linux binary with PostgreSQL under an MIT license.

Mattermost Team Edition is also bundled inside of the free Mattermost Enterprise Edition code base, which provides the same functionality as Mattermost Team Edition, with the additional benefit of being able to trial as well as upgrade into an expanded set of features available with paid subscription, including Mattermost Professional and Mattermost Enterprise. 

Because of the benefits of Mattermost Enterprise Edition, we recommend installing it instead of Mattermost Team Edition, even if you don’t currently need a subscription, so you'll have the flexibility to trial or enable additional features should you need them. However, if you only want to install software with a fully open source license, then Mattermost Team Edition is the best choice.

Mattermost plans
----------------

Mattermost plans consist of features and entitlements available either a paid subscription service or free. 

We have three primary plans available: 

* `Mattermost Enterprise <#mattermost-enterprise>`__: This is a paid subscription service for large and sophisticated enterprise-scale deployments of the Mattermost platform.
* `Mattermost Professional <#mattermost-professional>`__: This is a paid subscription service providing advance access controls and user management for managers leading teams of teams.
* `Mattermost Free <#mattermost-free>`__: This a free version of our collaboration platform designed for single teams (self-hosted only).

The Mattermost Professional and Mattermost Enterprise editions are only available after deploying our Mattermost Enterprise Edition code base, and then applying a valid license key that comes with a subscription purchase. Alternatively, you can start a 30-day free trial that can be activated either in-product (**System Console > Edition and License > Start trial**) or online at https://mattermost.com/trial/.

Mattermost Enterprise 
~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost Enterprise is an enterprise-grade collaboration system that supports and helps you scale your mission-critical enterprise workflows, meet strict enterprise security, compliance, and privacy requirements, as well as provide executive reporting, dashboards, and productivity metrics.

* *Self-hosted deployments* - **Mattermost Enterprise** is available to our self-hosted community who either run, or upgrade to, our self-hosted commercial Mattermost Enterprise Edition, who purchase by `contacting Mattermost Sales <https://mattermost.com/contact-sales/>`_, and who then install the license key onto their Mattermost server. A 30-day free trial to preview the features in this subscription can be activated either in-product (**System Console > Edition and License > Start trial**) or via an online request at https://mattermost.com/trial/.
* *Cloud deployments* - For our cloud community, **Mattermost Enterprise** can be purchased by `contacting Mattermost Sales <https://mattermost.com/contact-sales/>`_.

This offering includes all the features of `Mattermost Professional <#mattermost-professional>`__, plus: 

- :doc:`Enterprise-scale search with dedicated indexing and usage resourcing via cluster support </scale/elasticsearch>`.
- :doc:`Sychronization of access controls, channels, and teams with AD/LDAP Groups </onboard/ad-ldap-groups-synchronization>`.
- :doc:`eDiscovery and compliance export automation </comply/compliance-export>`.
- :doc:`Enterprise mobile device management with custom EMM support via AppConfig </deploy/mobile-appconfig>`.
- :doc:`Advanced legal controls with customizable end-user terms of service and re-acceptance duration </comply/custom-terms-of-service>`.
- :ref:`Private mobility with ID-only push notifications <configure/site-configuration-settings:push notification contents>`.
- :doc:`Enhanced compliance with global and custom retention policies for messages and files </comply/data-retention-policy>`.
- :doc:`Playbooks with ad hoc add/remove tasks, automated triggers, and stakeholders dashboard </repeatable-processes/learn-about-playbooks>`.
- :doc:`Granular administrative control with custom system admin roles </onboard/system-admin-roles>`.
- :doc:`Advanced configuration of playbook permissions, and analytics dashboards </repeatable-processes/share-and-collaborate>`
- :doc:`Channel export </comply/export-mattermost-channel-data>`
- :ref:`Enhanced compliance controls and granular audit logs with data export <manage/logging:audit logging (beta)>`.
- :doc:`Advanced collaboration with shared channels across Mattermost instances </onboard/shared-channels>`.
- :doc:`High availability support with multi-node database deployment </scale/high-availability-cluster>`.
- :doc:`Horizontal scaling through cluster-based deployment </scale/scaling-for-enterprise>`.
- :doc:`Advanced performance monitoring </scale/deploy-prometheus-grafana-for-performance-monitoring>`.
- `Eligibility for Premier Support add-on <https://mattermost.com/support/>`__.
- 99% uptime SLA guarantee (Cloud only, via dedicated virtual secure Cloud add-on option).

Mattermost Professional 
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Mattermost Professional is the set of collaboration features that enables you to build and scale your sophisticated technical workflows across multiple cross-functional teams to deliver mission-critical software.

* *Self-hosted deployments* - **Mattermost Professional** is available to our self-hosted community who either run, or upgrade to, our self-hosted commercial Mattermost Enterprise Edition (see :doc:`deployment guides </guides/deployment>`), who purchase the appropriate subscription license key through a `channel reseller <https://mattermost.com/partners/#resellers>`_ or by contacting `Mattermost Sales <https://mattermost.com/contact-sales/>`_, and who then install the license key onto their Mattermost server. A 30-day free trial to preview the features in this subscription can be activated in-product (**System Console > Edition and License > Start trial**).

This offering includes all the features of `Mattermost Free <#mattermost-free>`__, plus: 

- :doc:`Guest access </onboard/guest-accounts>` and :doc:`custom user groups </collaborate/organize-using-custom-user-groups>`.
- :doc:`Active Directory/LDAP Single Sign-on and user synchronization </onboard/ad-ldap>`.
- Single Sign-on with :doc:`GitLab </onboard/sso-gitlab>` using the OpenID Connect standard, :doc:`Google </onboard/sso-google>`, :doc:`OpenID Connect </onboard/sso-openidconnect>`, :doc:`SAML </onboard/sso-saml>` or :doc:`Office365 </onboard/sso-office>`.
- :ref:`MFA enforcement <onboard/multi-factor-authentication:enforcing mfa>`.
- :ref:`Advanced team permissions <onboard/advanced-permissions:team override scheme>`.
- :ref:`Read-only announcement channels <manage/team-channel-members:channel moderation>`.
- :doc:`System-wide announcement banners </manage/announcement-banner>`.
- O365 integration with `Microsoft Teams Calling <https://mattermost.com/marketplace/microsoft-teams-meetings/>`_ and `Jira multi-server <https://mattermost.com/marketplace/jira-plugin/>`_.
- `Next business day support via online ticketing system <https://mattermost.com/support/>`_.

See a `complete list of Mattermost features <https://mattermost.com/pricing>`_.

Mattermost Free
~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Mattermost Free is a set of collaboration features for accelerating your technical team’s productivity, shipping software faster with higher quality, and improving alignment among team members.

Mattermost Free is available to our self-hosted community through both our open source Mattermost Team Edition offering, and in our commercial Mattermost Enterprise Edition offering (when no subscription license key is active). It is best suited for teams of up to 50 members. See deployment options at: https://mattermost.com/deploy/.

.. important::

    For teams of less than 50 users, a standalone, single-node deployment of `Mattermost Team Edition <#mattermost-team-edition>`__ with frequent backups is appropriate.
    
    For teams larger than 50 users, it's strongly advised to deploy Mattermost with `Mattermost Enterprise <#mattermost-enterprise>`__ or `Mattermost Professional <#mattermost-professional>`__ to deliver a more secure, reliable, scalable, and resilient service.

Features include:

- Teams and channels for one-to-one and group messaging, file sharing, and unlimited search history with threaded messaging, emoji, and custom emoji.
- Native apps for iOS, Android, Windows, macOS, and Linux.
- Pre-packaged integrations with most common developer tools, including Jira, Confluence, GitHub, GitLab, CircleCI, Zoom, Jitsi, and more.
- Tools for :doc:`custom branding </configure/custom-branding-tools>` and :doc:`themes </preferences/customize-your-theme>`.
- :doc:`Multi-factor authentication </onboard/multi-factor-authentication>`.
- Single Sign-on with :doc:`GitLab </onboard/sso-gitlab>` using the OAuth 2.0 standard.
- :doc:`Granular system permissions </onboard/advanced-permissions>`.
- Highly customizable `third-party bots, integrations <https://mattermost.com/marketplace/#publicApps>`_, and :doc:`command line tools </manage/mmctl-command-line-tool>`.
- Extensive integration support via `webhooks, APIs, drivers <https://developers.mattermost.com/integrate/other-integrations/>`_, and `third-party extensions <https://mattermost.com/marketplace/>`_.
- Multiple languages including English (Australian, US), Bulgarian, Chinese (Simplified and Traditional), Dutch, French, German, Hungarian, Italian, Japanese, Korean, Persian, Polish, Portuguese (Brazil), Romanian, Russian, Spanish, Swedish, Turkish, Ukrainian, and Vietnamese.
- `Community support <https://mattermost.com/support/>`_.

See a complete list of features `here <https://mattermost.com/pricing>`_.

Other Mattermost plans
----------------------

Mattermost introduced a new pricing and packaging structure on October 13, 2021. The plans listed below reached end-of-life on October 31, 2023. We're no longer selling these products to new customers. For existing customers, we highly recommend working with your Mattermost Account team to plan for a migration to our new plans. We honored existing pricing and features for renewals and expansions of E10/20 until October 31, 2022. Please contact our `Sales team <https://mattermost.com/contact-sales/>`_ with questions.

Mattermost Enterprise Edition E10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost E10 was offered as a commercial enterprise messaging solution for teams, groups, and departments working on multiple projects scaling from hundreds to thousands of users. Many E10 features are now offered in Mattermost Professional. Features included: Active Directory/LDAP Single Sign-on; OAuth 2.0 authentication for team creation, account creation, and user login; encrypted push notifications with service level agreements (SLAs) via HPNS; advanced access control policy; next business day support via online ticketing system; scale to handle hundreds of users per team.

Mattermost Enterprise Edition E20
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Enterprise E20 was offered as a commercial enterprise-grade messaging system that scales from hundreds to tens of thousands of users. Enterprise Edition E20 authentication features are now offered in Mattermost Professional, and High Availability and compliance features are offered in Mattermost Enterprise.

Features included: Advanced SAML 2.0 authentication with Okta, OneLogin, and Active Directory Federation Services; Active Directory/LDAP group synchronization; OpenID Connect authentication for team creation, account creation, and user login; compliance exports of message histories with oversight protection; custom retention policies for messages and files; high availability support with multi-node database deployment; horizontal scaling through cluster-based deployment; Elasticsearch support for highly efficient database searches in a cluster environment; advanced performance monitoring; eligibility for Premier Support add-on.

Product decisions
-----------------

As the platform matures and new features are added, they're evaluated to be included in the plan that best aligns with the organizational use cases outlined by the editions above. Multiple factors are considered in determining the appropriate plan to include a feature including mission-critical impact, relative value to a single team, cross-functional teams, and the enterprise, as well as security, compliance, and scalability.

We recognize there aren't any features that are only useful to managers, directors, and executives. Individual practitioners may want certain features; however, we think that other buyers are relatively more likely to care about it. We also recognize that there may be some features that are put into an edition to find later there is much demand for it by individuals or a singular team; we will not hesitate to move that feature. We value feedback from our community and iterate based on that feedback. Simultaneously, we also need to offer commercial products that hold value and do our best to find the right balance. We believe the more of Mattermost that you use, the more likely it is that you benefit from the advanced editions we offer.

You can provide us with feedback via `our idea portal <https://mattermost.com/suggestions/>`, where ideas and input influences the future of the platform.