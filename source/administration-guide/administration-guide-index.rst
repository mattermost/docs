Administration Guide
=====================

This guide helps system administrators run a secure, reliable, and scalable Mattermost deployment. It’s organized as a clear journey, showing the outcomes you need to achieve and the tasks required to get there, from onboarding and identity management, to feature enablement, monitoring, scaling, compliance, and ongoing workspace management.

Get Started
-------------

Migrate users and data, connect workspaces, and establish initial governance and readiness.

- `Migrate users from Slack or HipChat <getting-started/getting-started-index>`_
- `Import data in bulk <getting-started/getting-started-index>`_
- `Connect multiple workspaces <getting-started/getting-started-index>`_
- `Follow the rollout checklist <getting-started/getting-started-index>`_
- `Complete administrator onboarding <getting-started/getting-started-index>`_

Learn about the first steps to take after your Mattermost server is live, including :doc:`migrating to Mattermost </administration-guide/getting-started/migrating-to-mattermost>`, :doc:`bulk loading data </administration-guide/getting-started/bulk-loading-data>`, :doc:`installing license key </administration-guide/admin-tools/installing-license-key>`, :doc:`connecting Mattermost workspaces </administration-guide/getting-started/connected-workspaces>`, and :doc:`initial rollout planning </administration-guide/getting-started/admin-onboarding-tasks>` to ensure a successful start with Mattermost.

- :doc:`Email templates </administration-guide/configuration-reference/email-templates>`


Identity & Access Management
----------------------------

Secure sign-in through centralized identity providers, map attributes, and govern access and membership.

- `Set up Active Directory (AD) or LDAP <identity-access/identity-access-index>`_
- `Configure SSO (SAML: Okta, ADFS, OneLogin, Keycloak; OIDC: GitLab, Google, Entra ID) <identity-access/identity-access-index>`_
- `Enforce multi-factor authentication (MFA) <identity-access/identity-access-index>`_
- `Enable client certificates <identity-access/identity-access-index>`_
- `Sync groups and manage membership <identity-access/identity-access-index>`_

Mattermost supports multiple authentication methods to meet your enterprise requirements. Choose from :doc:`SAML-based SSO </administration-guide/identity-access/authentication-methods/saml-based-sso/saml-based-sso-index>`, :doc:`OIDC-based SSO </administration-guide/identity-access/authentication-methods/sso/sso-index>`, and :doc:`AD/LDAP </administration-guide/identity-access/authentication-methods/ad-ldap/ad-ldap>`.

You can additionally increase your organization's secure collaboration posture by enabling :doc:`multi-factor authentication </administration-guide/identity-access/multi-factor-authentication>` and :doc:`enabling SSL client certificates </administration-guide/identity-access/ssl-client-certificates>`.

Platform Features
-----------------

Expand your deployment with core features, improve search relevance, and enable real-time voice and video.

- `Configure integrations and install plugins <platform-features/platform-features-index>`_

- :doc:`Install Boards for project management </administration-guide/configuration-reference/install-boards>`
- :doc:`Deploy Calls for real-time voice and video <platform-features/xxx>`_
- :doc:`Deploy Agents </administration-guide/configuration-reference/agents-admin-guide>`
- deploy enterprise search
- :doc:`Enabling Chinese, Japanese, Korean search </administration-guide/configuration-reference/enabling-chinese-japanese-korean-search>`


User Experience & Engagement
----------------------------

Deliver a consistent, branded workspace that drives adoption, engagement, and structured feedback.

- `Apply branding and customize the UI <user-experience/user-experience-index>`_
- `Manage in-product notices <user-experience/user-experience-index>`_
- `Run user satisfaction surveys <user-experience/user-experience-index>`_
- `Optimize workspace configuration <user-experience/user-experience-index>`_
- `Customize email templates <user-experience/user-experience-index>`_

Monitoring & Observability
--------------------------

Gain visibility into system health, define alerts, and proactively prevent incidents.

- `Configure logging, telemetry, and system statistics <monitoring-observability/monitoring-observability-index>`_
- `Set health probes <monitoring-observability/monitoring-observability-index>`_
- `Deploy Prometheus and Grafana <monitoring-observability/monitoring-observability-index>`_
- `Define alerting rules <monitoring-observability/monitoring-observability-index>`_
- `Request health checks <monitoring-observability/monitoring-observability-index>`_

Operations & Scaling
--------------------

Keep your deployment reliable and performant, scale as needed, and upgrade safely with minimal downtime.

- `Plan and perform upgrades or downgrades <operations-scaling/operations-scaling-index>`_
- `Deploy high availability (HA) clusters <operations-scaling/operations-scaling-index>`_
- `Scale horizontally with Redis <operations-scaling/operations-scaling-index>`_
- `Configure Elasticsearch or OpenSearch <operations-scaling/operations-scaling-index>`_
- `Tune system performance and plan storage capacity <operations-scaling/operations-scaling-index>`_
- `Monitor push notification health <operations-scaling/operations-scaling-index>`_




- :doc:`Additional HA considerations </administration-guide/operations-scaling/additional-ha-considerations>`
- :doc:`Backing storage benchmarks </administration-guide/operations-scaling/backing-storage-benchmarks>`
- :doc:`Collect performance metrics </administration-guide/operations-scaling/collect-performance-metrics>`
- :doc:`Common: Configure Mattermost for Enterprise Search </administration-guide/operations-scaling/common-configure-mattermost-for-enterprise-search>`
- :doc:`Communicate scheduled maintenance </administration-guide/operations-scaling/communicate-scheduled-maintenance>`
- :doc:`Deploy Prometheus and Grafana for performance monitoring </administration-guide/operations-scaling/deploy-prometheus-grafana-for-performance-monitoring>`
- :doc:`Downgrading Mattermost Server </administration-guide/operations-scaling/downgrading-mattermost-server>`
- :doc:`Elasticsearch setup </administration-guide/operations-scaling/elasticsearch-setup>`
- :doc:`Enterprise install and upgrade </administration-guide/operations-scaling/enterprise-install-upgrade>`
- :doc:`Enterprise search </administration-guide/operations-scaling/enterprise-search>`
- :doc:`Ensuring releases perform at scale </administration-guide/operations-scaling/ensuring-releases-perform-at-scale>`
- :doc:`Estimated storage per user per month </administration-guide/operations-scaling/estimated-storage-per-user-per-month>`
- :doc:`High availability cluster-based deployment </administration-guide/operations-scaling/high-availability-cluster-based-deployment>`
- :doc:`Important upgrade notes </administration-guide/operations-scaling/important-upgrade-notes>`
- :doc:`Lifetime storage </administration-guide/operations-scaling/lifetime-storage>`
- :doc:`Notify admin </administration-guide/operations-scaling/notify-admin>`
- :doc:`Open source components </administration-guide/operations-scaling/open-source-components>`
- :doc:`OpenSearch setup </administration-guide/operations-scaling/opensearch-setup>`
- :doc:`Performance alerting </administration-guide/operations-scaling/performance-alerting>`
- :doc:`Performance monitoring metrics </administration-guide/operations-scaling/performance-monitoring-metrics>`
- :doc:`Prepare to upgrade Mattermost </administration-guide/operations-scaling/prepare-to-upgrade-mattermost>`
- :doc:`Push notification health targets </administration-guide/operations-scaling/push-notification-health-targets>`
- :doc:`Redis </administration-guide/operations-scaling/redis>`
- :doc:`Scale to 100000 users </administration-guide/operations-scaling/scale-to-100000-users>`
- :doc:`Scale to 15000 users </administration-guide/operations-scaling/scale-to-15000-users>`
- :doc:`Scale to 200 users </administration-guide/operations-scaling/scale-to-200-users>`
- :doc:`Scale to 2000 users </administration-guide/operations-scaling/scale-to-2000-users>`
- :doc:`Scale to 200000 users </administration-guide/operations-scaling/scale-to-200000-users>`
- :doc:`Scale to 30000 users </administration-guide/operations-scaling/scale-to-30000-users>`
- :doc:`Scale to 50000 users </administration-guide/operations-scaling/scale-to-50000-users>`
- :doc:`Scale to 80000 users </administration-guide/operations-scaling/scale-to-80000-users>`
- :doc:`Scale to 90000 users </administration-guide/operations-scaling/scale-to-90000-users>`
- :doc:`Scaling for enterprise </administration-guide/operations-scaling/scaling-for-enterprise>`
- :doc:`Upgrade Mattermost </administration-guide/operations-scaling/upgrade-mattermost>`
- :doc:`Upgrade Mattermost (Kubernetes HA) </administration-guide/operations-scaling/upgrade-mattermost-kubernetes-ha>`
- :doc:`Upgrading Mattermost Server </administration-guide/operations-scaling/upgrading-mattermost-server>`

Compliance, Security & Auditing
-------------------------------

Align with compliance requirements, enforce retention and holds, and ensure complete auditability.

- `Define data retention policies <compliance-security-auditing/compliance-security-auditing-index>`_
- `Enable legal holds <compliance-security-auditing/compliance-security-auditing-index>`_
- `Run eDiscovery and generate exports <compliance-security-auditing/compliance-security-auditing-index>`_
- `Review and analyze audit logs <compliance-security-auditing/compliance-security-auditing-index>`_
- `Set and enforce custom terms of service <compliance-security-auditing/compliance-security-auditing-index>`_
- `Follow compliance guidelines <compliance-security-auditing/compliance-security-auditing-index>`_

- :doc:`Compliance export </administration-guide/compliance-security-auditing/compliance-export>`
- :doc:`Compliance monitoring </administration-guide/compliance-security-auditing/compliance-monitoring>`
- :doc:`Compliance with Mattermost </administration-guide/compliance-security-auditing/compliance-with-mattermost>`
- :doc:`Custom terms of service </administration-guide/compliance-security-auditing/custom-terms-of-service>`
- :doc:`Data retention policy </administration-guide/compliance-security-auditing/data-retention-policy>`
- :doc:`Electronic discovery </administration-guide/compliance-security-auditing/electronic-discovery>`
- :doc:`Embedded JSON audit log schema </administration-guide/compliance-security-auditing/embedded-json-audit-log-schema>`
- :doc:`Export Mattermost channel data </administration-guide/compliance-security-auditing/export-mattermost-channel-data>`
- :doc:`Legal hold </administration-guide/compliance-security-auditing/legal-hold>`

Administration Tools & Utilities
--------------------------------

Streamline administration with automation tools, simplify troubleshooting, and maintain operational hygiene.

- `Use mmctl or the CLI for automation <admin-tools/admin-tools-index>`_
- `Generate and review support packets <admin-tools/admin-tools-index>`_
- `Manage system notices <admin-tools/admin-tools-index>`_
- `Track product limits and usage statistics <admin-tools/admin-tools-index>`_
- `Configure automated health checks <admin-tools/admin-tools-index>`_
- `Manage teams and channels <admin-tools/admin-tools-index>`_

- :doc:`Attribute-based access control </administration-guide/admin-tools/attribute-based-access-control>`
- :doc:`Bulk export tool </administration-guide/admin-tools/bulk-export-tool>`
- :doc:`Cloud BYOK </administration-guide/admin-tools/cloud-byok>`
- :doc:`Cloud data export </administration-guide/admin-tools/cloud-data-export>`
- :doc:`Cloud data residency </administration-guide/admin-tools/cloud-data-residency>`
- :doc:`Cloud IP filtering </administration-guide/admin-tools/cloud-ip-filtering>`
- :doc:`Code signing custom builds </administration-guide/admin-tools/code-signing-custom-builds>`
- :doc:`Command line tools </administration-guide/admin-tools/command-line-tools>`
- :doc:`Configure health check probes </administration-guide/admin-tools/configure-health-check-probes>`
- :doc:`Customize branding </administration-guide/admin-tools/customize-branding>`
- :doc:`Error codes </administration-guide/admin-tools/error-codes>`
- :doc:`Feature labels </administration-guide/admin-tools/feature-labels>`
- :doc:`Generating support packet </administration-guide/admin-tools/generating-support-packet>`
- :doc:`In-product notices </administration-guide/admin-tools/in-product-notices>`
- :doc:`Logging </administration-guide/admin-tools/logging>`
- :doc:`Migration </administration-guide/admin-tools/migration>`
- :doc:`mmctl command line tool </administration-guide/admin-tools/mmctl-command-line-tool>`
- :doc:`Monitoring and performance </administration-guide/admin-tools/monitoring-and-performance>`
- :doc:`Product limits </administration-guide/admin-tools/product-limits>`
- :doc:`Request server health check </administration-guide/admin-tools/request-server-health-check>`
- :doc:`Server configuration </administration-guide/admin-tools/server-configuration>`
- :doc:`Server maintenance </administration-guide/admin-tools/server-maintenance>`
- :doc:`Statistics </administration-guide/admin-tools/statistics>`
- :doc:`System-wide notifications </administration-guide/admin-tools/system-wide-notifications>`
- :doc:`Team and channel members </administration-guide/admin-tools/team-channel-members>`
- :doc:`Telemetry </administration-guide/admin-tools/telemetry>`
- :doc:`User attributes </administration-guide/admin-tools/user-attributes>`
- :doc:`User management </administration-guide/admin-tools/user-management>`
- :doc:`User provisioning </administration-guide/admin-tools/user-provisioning>`
- :doc:`User satisfaction surveys </administration-guide/admin-tools/user-satisfaction-surveys>`

Licensing & Workspace Management
--------------------------------

Govern your workspace, control data residency and billing, and enable licensed features.

- `Manage license keys for self-hosted deployments <licensing/licensing-index>`_
- `Administer Cloud workspaces <licensing/licensing-index>`_
- `Configure BYOK, data residency, and IP filtering <licensing/licensing-index>`_
- `Set account details and billing information <licensing/licensing-index>`_

- :doc:`Cloud workspace management </administration-guide/licensing/cloud-workspace-management>`
- :doc:`Self-hosted billing </administration-guide/licensing/self-hosted-billing>`

Configuration Settings (Reference)
---------------------------------

Apply precise configuration changes with confidence, using fully documented and traceable settings.

- `Reference and update System Console settings <configuration-reference/configuration-reference-index>`_
- `Modify config.json parameters <configuration-reference/configuration-reference-index>`_
- `Configure environment variables <configuration-reference/configuration-reference-index>`_
- `Apply advanced options across all areas <configuration-reference/configuration-reference-index>`_

- :doc:`Authentication configuration settings </administration-guide/configuration-reference/authentication-configuration-settings>`
- :doc:`Bleve search </administration-guide/configuration-reference/bleve-search>`
- :doc:`Cloud billing account settings </administration-guide/configuration-reference/cloud-billing-account-settings>`
- :doc:`Compliance configuration settings </administration-guide/configuration-reference/compliance-configuration-settings>`
- :doc:`Configuration in your database </administration-guide/configuration-reference/configuration-in-your-database>`
- :doc:`Configuration settings </administration-guide/configuration-reference/configuration-settings>`
- :doc:`Custom branding tools </administration-guide/configuration-reference/custom-branding-tools>`
- :doc:`Customize Mattermost </administration-guide/configuration-reference/customize-mattermost>`
- :doc:`Deprecated configuration settings </administration-guide/configuration-reference/deprecated-configuration-settings>`
- :doc:`Environment configuration settings </administration-guide/configuration-reference/environment-configuration-settings>`
- :doc:`Environment variables </administration-guide/configuration-reference/environment-variables>`
- :doc:`Experimental configuration settings </administration-guide/configuration-reference/experimental-configuration-settings>`
- :doc:`Integrations configuration settings </administration-guide/configuration-reference/integrations-configuration-settings>`
- :doc:`Manage user surveys </administration-guide/configuration-reference/manage-user-surveys>`
- :doc:`Optimize your workspace </administration-guide/configuration-reference/optimize-your-workspace>`
- :doc:`Plugins configuration settings </administration-guide/configuration-reference/plugins-configuration-settings>`
- :doc:`Push notification server configuration settings </administration-guide/configuration-reference/push-notification-server-configuration-settings>`
- :doc:`Rate limiting configuration settings </administration-guide/configuration-reference/rate-limiting-configuration-settings>`
- :doc:`Reporting configuration settings </administration-guide/configuration-reference/reporting-configuration-settings>`
- :doc:`Self-hosted account settings </administration-guide/configuration-reference/self-hosted-account-settings>`
- :doc:`Site configuration settings </administration-guide/configuration-reference/site-configuration-settings>`
- :doc:`SMTP email </administration-guide/configuration-reference/smtp-email>`
- :doc:`System attributes </administration-guide/configuration-reference/system-attributes>`
- :doc:`User management configuration settings </administration-guide/configuration-reference/user-management-configuration-settings>`






