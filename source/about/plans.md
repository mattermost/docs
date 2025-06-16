# Mattermost Plans

<style>
  table.mattermost-plans {
    border-collapse: collapse;
    width: 100%;
    font-size: 0.95em;
  }
  table.mattermost-plans th, table.mattermost-plans td {
    border: 1px solid #888;
    padding: 6px 8px;
    vertical-align: top;
  }
  /* Dark mode border color */
  body:not([data-custom-theme="light"]) table.mattermost-plans th, 
  body:not([data-custom-theme="light"]) table.mattermost-plans td {
    border-color: #666;
  }
  table.mattermost-plans th {
    background: #f2f2f2;
    font-weight: bold;
    text-align: left;
  }
  /* Dark mode support for table headers */
  body:not([data-custom-theme="light"]) table.mattermost-plans th {
    background: #444;
    color: #fff;
  }
  table.mattermost-plans tr.section td {
    background: #f9f9f9;
    font-weight: bold;
    font-size: 1.05em;
    border-top: 2px solid #888;
  }
  /* Dark mode support for section rows */
  body:not([data-custom-theme="light"]) table.mattermost-plans tr.section td {
    background: #3a3a3a;
    color: #fff;
  }
  table.mattermost-plans tr.subsection td {
    background: #f6f6f6;
    font-style: italic;
    border-top: 1px solid #888;
  }
  /* Dark mode support for subsection rows */
  body:not([data-custom-theme="light"]) table.mattermost-plans tr.subsection td {
    background: #333;
    color: #eee;
  }
</style>

<table class="mattermost-plans">
  <thead>
    <tr>
      <th>Feature Category</th>
      <th>Team Edition</th>
      <th>E0/Starter</th>
      <th>Professional</th>
      <th>Enterprise</th>
      <th>Enterprise Advanced</th>
      <th>Available From</th>
    </tr>
  </thead>
  <tbody>
    <!-- Channel-based messaging -->
    <tr class="section"><td colspan="7"><strong>Channel-based messaging</strong></td></tr>
    <tr class="subsection"><td colspan="7"><strong>1-1, group messaging, public and private channels, file sharing, link and media previews across web, PC, Mac, iOS and Android devices, with 1-1 audio calls and screen share, threaded discussions, search, custom branding themes and emojis, and availability in 20+ languages.</strong></td></tr>
    <tr>
      <td><strong>Messaging, file sharing, and link and file previews across device platforms</strong>: Channels-based messaging including 1-1, group messaging, public and private channels, file sharing, link and media previews across web, PC, Mac, iOS, and Android devices.</td>
      <td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>1:1 audio calls and screen sharing</strong>: Call another user to start a 1-1 audio discussion in web, desktop, and mobile experiences with optional screen sharing.</td>
      <td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Threaded discussions</strong>: Organize discussions within channels using <a href="https://docs.mattermost.com/collaborate/organize-conversations.html">threaded discussions</a> and the thread inbox to follow-up on threaded discussions in addition to channels.</td>
      <td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Core search</strong>: Search over messages and files in Mattermost. Core search happens in a relational database and is intended for deployments under about 2–3 million posts and file entries. Beyond that scale, <a href="https://docs.mattermost.com/scale/enterprise-search.html">Enterprise Search</a> is recommended.</td>
      <td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Custom branding, themes, and emojis</strong>: Match your organizations look, feel and brand by <a href="https://docs.mattermost.com/configure/custom-branding-tools.html">customizing</a> the site name, description, login brand image and text, as well as <a href="https://docs.mattermost.com/preferences/customize-your-theme.html">theme colors</a>.</td>
      <td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Available in 20 languages</strong>: Support for English (U.S., Australian), Japanese, Korean, Swedish, Dutch, French, German, Italian, Spanish, Turkish, Polish, Portuguese (Brazil), Romanian, Vietnamese, Ukrainian, Bulgarian, Hungarian, Persian, Russian, and Chinese (Simplified and Traditional) languages.</td>
      <td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <!-- AI-accelerated collaboration -->
    <tr class="section"><td colspan="7"><strong>AI-accelerated collaboration</strong></td></tr>
    <tr class="subsection"><td colspan="7"><strong>Integrate your preferred LLM in 1-1, group messaging, public and private channels, with audio calls and screen share, and threaded discussions to speed workflows, increase efficiency and unlock innovation.</strong></td></tr>
    <tr>
      <td><strong>Interactive AI bot support</strong>: Enable organizations to work with LLM-powered AI bots through Direct Messages, Group Messages, threads and @mentions to bot in private and public channels with full commercial support from Mattermost, Inc.</td>
      <td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Flexible bring-your-own-LLM integration</strong>: Connect Mattermost to any LLM platform compatible with OpenAI protocol across public cloud, private cloud and air gapped edge including OpenAI, Llama, Anthropic, and custom LLMs.</td>
      <td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Contextual summarization and composition</strong>: Enable organizational interaction with LLMs with permission-restricted access to Mattermost conversations, threads, call and meeting summaries to summarize topics, answer questions and follow-ups, note action items and open questions and compose draft messages and responses.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Private, air-gapped &amp; DDIL AI operations</strong>: Run AI-accelerated operations in private cloud, air-gapped and disconnected, denied, intermittent and limited-bandwidth (DDIL) environments with open source and custom LLMs self-hosted alongside workflow, chat operations, audio calling, screen sharing, recording, transcription, analysis, workflow and summarization capabilities.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Real-time channel briefing</strong>: Concisely summarize unread messages, action items and unanswered questions in channels to focus attention and accelerate priority responses and workflows.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Q&A with access-controlled backend systems</strong>: Receive secure and compliant real-time answers to questions about permission-controlled backend systems connected with Mattermost channels which can optionally pass back end user credentials to work with access-controlled data. For example, asking a channel connected with an issue tracking system which code defect tickets they have access to which could expose security vulnerabilities.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Optional full trace mode</strong>: Optional full trace mode for detailed monitoring and to verify Responsible AI/LLM assurances by recording every prompt, question, AI request and response across users, systems and LLM-backends and platform source code into specialized audit logs for analysis.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <!-- Operational & technical collaboration -->
    <tr class="section"><td colspan="7"><strong>Operational &amp; technical collaboration</strong></td></tr>
    <tr class="subsection"><td colspan="7"><strong>Accelerate operational and technical success with a collaboration platform integrating with mainstream and customer toolchains, with information rich visualizations of systems and processes, prioritized message broadcasting, and conversational interoperability with technical systems through platform-level Markdown support.</strong></td></tr>
    <tr>
      <td><strong>Integrations platform</strong>: Tailor fit and transform your mission-critical collaboration infrastructure with a <a href="https://docs.mattermost.com/about/integrations.html">broad range of configuration and extension options</a> ranging from webhooks and custom slash commands, to bots and API integrations, to building out plug-ins and making source code customizations.</td>
      <td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Operational and DevOps integrations</strong>: Accelerate operational and technical workflows by integrating Mattermost’s collaborative platform with data and automation from an array of systems ranging from modern, cloud-based applications and tools to legacy and on-prem infrastructure, including <a href="https://mattermost.com/marketplace/jira-plugin/">Jira</a>, <a href="https://mattermost.com/marketplace/github-plugin/">GitHub</a>, <a href="https://mattermost.com/marketplace/gitlab-plugin/">GitLab</a>, and <a href="https://mattermost.com/marketplace/servicenow/">ServiceNow</a> among others.</td>
      <td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Compact view</strong>: Increase the efficiency of technical teams with <a href="https://docs.mattermost.com/preferences/manage-your-display-options.html#message-display">compact display</a> views of discussions and tooling notifications integrated in Mattermost channels.</td>
      <td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Markdown compatibility</strong>: Easily move information across Mattermost discussions and technical tooling outputs with built-in support for the Markdown technical formatting standard. Text formatting, code snippets, media embedding, tables, status indicators, and emojis render consistently across the Mattermost user experience and Markdown-compatible tools.</td>
      <td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Message priority</strong>: Elevate the focus of organizations with the ability for end users to <a href="https://docs.mattermost.com/collaborate/message-priority.html#set-message-priority">specify the priority of messages</a> as Standard (Default), Important, and Urgent.</td>
      <td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Persistent notifications</strong>: Replace phone-based confirmations with <a href="https://docs.mattermost.com/collaborate/message-priority.html#send-persistent-notifications">message-based acknowledgement requests</a> that can persist on a recipient’s Mattermost interface until acknowledged.</td>
      <td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <!-- Advanced access controls & automation -->
    <tr class="section"><td colspan="7"><strong>Advanced access controls &amp; automation</strong></td></tr>
    <tr class="subsection"><td colspan="7"><strong>Centralize and automate user identity and permissions with a range of single-sign-on (SSO), user synchronization and advanced access control capabilities.</strong></td></tr>
    <tr>
      <td><strong>Email authentication</strong>: Basic email-based authentication with username and password is available in Mattermost Free and higher-level Mattermost packages. While the method includes a number of core admin features around email address verification, password complexity, maximum login attempts, and password reset, among others, it is highly recommended that this method of authentication is only used in small teams on private networks.</td>
      <td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Single sign-on w/SAML 2.0, Entra ID, Okta, and others</strong>: Centralize, integrate, and automate identify management and access controls by enabling Mattermost to operate as a SAML 2.0 service provider. Integrate with SAML 2.0-based providers including Entra ID (formerly Office365 SSO), Okta, OneLogin, Microsoft ADFS SAML Configuration, and Keycloak, among others.</td>
      <td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>SSO with AD/LDAP, OpenID, and others</strong>: Simplify sign-on and user management with non-SAML-based SSO options including <a href="https://docs.mattermost.com/onboard/sso-openidconnect.html">Open ID</a>, Google SSO, and <a href="https://docs.mattermost.com/onboard/sso-gitlab.html">GitLab SSO</a>. Moreover, Mattermost offers “same sign-on” with Active Directory/LDAP by enabling the same credentials used in on-prem AD/LDAP deployments to be reused in Mattermost, with optional multi-factor authentication (MFA).</td>
      <td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>AD/LDAP user sync</strong>: Simplify and accelerate user administration, access control, and compliance by <a href="https://docs.mattermost.com/onboard/ad-ldap.html">synchronizing Active Directory and LDAP with Mattermost</a>, including single-sign-on with AD/LDAP credentials, synchronization of user display attributes (e.g., first name, last name, email, and username), automated account provisioning on a user’s first sign-on, automated assignment of Mattermost roles based on a user’s LDAP group, and compliance with administrator settings managed in AD/LDAP by having the Mattermost System Console honor LDAP filters for disabled users, guest users, and administrative users.</td>
      <td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>MFA enforcement for email and LDAP accounts</strong>: Fulfill MFA compliance requirements by <a href="https://docs.mattermost.com/onboard/multi-factor-authentication.html#enforcing-mfa">enforcing an MFA requirement</a> for login with email and LDAP accounts.</td>
      <td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Advanced access controls</strong>: Empower admins to <a href="https://docs.mattermost.com/manage/team-channel-members.html#channel-moderation">manage and moderate multi-team deployments</a> with the ability to configure channels to be read-only, to restrict channel mentions and emoji reactions, and to lock down channels so that users can only be added or removed by selected administrators.</td>
      <td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <!-- Multi-team collaboration -->
    <tr class="section"><td colspan="7"><strong>Multi-team collaboration</strong></td></tr>
    <tr class="subsection"><td colspan="7"><strong>Work across teams and organizations with real-time calling and screen share, guest accounts to integrate internal and external stakeholders, customer user groups to organize teams within teams, and system-wide notifications to share organization-wide messages.</strong></td></tr>
    <tr>
      <td><strong>Group calling and screen share</strong>: Streamline real-time collaboration with complete privacy by enabling group audio calling and screen share up to approximately 50 concurrent users in any group call per self-hosted server. High-scale options for private, self-hosted group calling and screen share are available in Mattermost Enterprise with the setup of its horizontal scaling option.</td>
      <td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Guest accounts</strong>: Bring external users and users who need to have restricted access into your Mattermost instance as guests who can interact with your team with limited permissions. For billing purposes, activated guest accounts do consume a licensed seat, which is returned when the guest account is deactivated.</td>
      <td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Custom user groups</strong>: Simplify communication by creating custom user groups to mention and notify up to 256 users who work together on projects or in functions or have other ties. Examples include creating custom groups for cross-functional teams, for job types, or organization membership within an enterprise.</td>
      <td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>System-wide notifications</strong>: Notify users across teams of upcoming system maintenance, service changes, and other announcements using system-wide announcement banners.</td>
      <td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <!-- Scale & high availability -->
    <tr class="section"><td colspan="7"><strong>Scale &amp; high availability</strong></td></tr>
    <tr class="subsection"><td colspan="7"><strong>Achieve scale and resilience with cluster-based deployment, horizontal system architecture, advanced performance monitoring and logging and Kubernetes-based deployment.</strong></td></tr>
    <tr>
      <td><strong>High availability cluster-based deployment</strong>: Enable business continuity through component failures using <a href="https://docs.mattermost.com/scale/scaling-for-enterprise.html#cluster-based-deployment">cluster-based deployment</a> with multiple application servers, multiple database servers, and multiple front-end proxies and/or load balancers.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Horizontal scalability architecture</strong>: Scale to tens of thousands of users with <a href="https://docs.mattermost.com/scale/scaling-for-enterprise.html#cluster-based-deployment">horizontal scale-out architectures</a> offering a range of deployment options from on-prem data centers to cloud-based hyperscalers including AWS and Azure.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Enterprise search (3M+ posts)</strong>: Enable enterprise-scale search after exceeding 3 million posts in the Mattermost database by <a href="https://docs.mattermost.com/scale/elasticsearch.html">deploying Elasticsearch</a> with dedicated indexing and usage resourcing via cluster support.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Performance monitoring</strong>: Track system health in large deployments, including deployments on high availability clusters, using <a href="https://docs.mattermost.com/scale/deploy-prometheus-grafana-for-performance-monitoring.html">advanced performance monitoring</a> integrated with Grafana and Prometheus.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Advanced logging</strong>: Enable <a href="https://docs.mattermost.com/manage/logging.html#audit-logging-experimental">advanced logging</a> for optimizing and troubleshooting high-scale, mission-critical deployments including error, panic, debug, trace and conditional logging to a full range of destinations including Syslog and TCP target options.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>High availability, horizontally scalable calls and screen share</strong>: Enable <a href="https://docs.mattermost.com/configure/calls-deployment.html#the-rtcd-service">high-scale, high availability deployment of audio calling and screen share</a> through dedicated servers managed on an integrated Kubernetes platform.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Supported Kubernetes deployment</strong>: Simplify and automate IT administration through Mattermost’s supported options for <a href="https://docs.mattermost.com/deploy/server/deploy-kubernetes.html">deploying to Kubernetes clusters</a> running either on-prem in data centers or in managed services such as Amazon EKS, Azure Kubernetes Service, Google Kubernetes Engine, and DigitalOcean Kubernetes, among others.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <!-- Advanced compliance & administration -->
    <tr class="section"><td colspan="7"><strong>Advanced compliance &amp; administration</strong></td></tr>
    <tr class="subsection"><td colspan="7"><strong>Fulfill enterprise- and critical infrastructure-level compliance and administration requirements with advanced identity and access control synchronization, delegated administration, granular configuration of data retention, eDiscovery, and legal hold and information export requirements while automating disclosures and agreements with end users.</strong></td></tr>
    <tr>
      <td><strong>AD/LDAP group, channel, and team sync</strong>: Automate management of users, groups, access controls, and channel and team membership through <a href="https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html">synchronizing with Entra ID/AD/LDAP Groups</a>.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Delegated granular administration</strong>: In large deployments where administrative tasks need to be separated and delegated, Mattermost supports the <a href="https://docs.mattermost.com/onboard/delegated-granular-administration.html">creation and customization of system administrator roles with specific granular permissions</a> in order to offer specialized administration delegated from senior administrators.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Data retention policy</strong>: Meet data retention compliance requirements. By default Mattermost uses a “soft delete” system where messages and files deleted based on user actions are removed from the user interface, but persist in the Mattermost database. <p>By activating <a href="https://docs.mattermost.com/comply/data-retention-policy.html">Mattermost’s data retention policy capability</a>, rules can be set to permanently delete all messages and files in a Mattermost system, or in specific teams or channels, that are beyond a specific age (e.g., 30 days, 90 days, or other options). This feature should be used carefully; once data is removed using data retention policies, the action is irreversible.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Legal hold</strong>: Comply with legal hold and litigation hold requests to preserve information in anticipation of legal action. The <a href="https://docs.mattermost.com/comply/legal-hold.html">legal hold capability</a> can be combined with eDiscovery integration and data retention policies to customize the data retained and deleted to meet compliance requirements.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Compliance export and eDiscovery automation</strong>: Fulfill eDiscovery and compliance requirements <a href="https://docs.mattermost.com/comply/compliance-export.html">with manual and automated export of message history</a> to Actiance, Global Relay, and custom compliance formats.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Channel export</strong>: Archive, backup, or submit the contents of a channel into other systems to fulfill reporting and auditability requirements as needed.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Custom end user Terms of Service</strong>: Increase clarity on legal expectations for internal employees and guests with the ability to set <a href="https://docs.mattermost.com/comply/custom-terms-of-service.html">custom Terms of Service (“ToS”) agreements</a> and re-acceptable periods.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <!-- Enterprise mobility -->
    <tr class="section"><td colspan="7"><strong>Enterprise mobility</strong></td></tr>
    <tr class="subsection"><td colspan="7"><strong>Speed real-world workflows with enterprise-grade mobility and security through EMM, MDM, and AppConfig integration across iOS and Android mobile platforms.</strong></td></tr>
    <tr>
      <td><strong>Enterprise Mobility Management (AppConfig) support</strong>: Enhance mobile security by <a href="https://docs.mattermost.com/deploy/mobile/deploy-mobile-apps-using-emm-provider.html">deploying with Enterprise Mobility Management (EMM)</a> to secure mobile endpoints with management application configuration, and <a href="https://docs.mattermost.com/deploy/mobile/deploy-mobile-apps-using-emm-provider.html#manage-app-configuration-using-appconfig">Mattermost AppConfig compatibility</a>.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Private mobility with ID-only push notifications</strong>: This capability protects a Mattermost customer against breaches in iOS and Android notification infrastructure by enabling mobile notifications to be fully private. The standard way to send notifications to iOS and Android applications requires sending clear text messages to Apple or Google so they can be forwarded to a user’s phone and displayed on iOS or Android. <p> While Apple and Google assure the data is not collected or stored, all standard mobile notifications on the platform could be compromised should the organizations be breached or coerced. To avoid this risk, Mattermost can be configured to replace mobile notification text with message ID numbers that pass no information to Apple of Google, and which, when received by the Mattermost mobile application on a user’s phone, are used to privately communicate with their Mattermost server and use the message ID to retrieve mobile notification messages over an encrypted channel. This means at no time will the message text be visible to Apple or Google’s message relay system. </p> <p>Because of the extra steps to retrieve the notifications messages under Mattermost’s private mobility capability with ID-only push notifications, end users may experience a slight delay before the mobile notification is fully displayed compared to sending clear text through Apple and Google’s platform.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <!-- Workflow automation -->
    <tr class="section"><td colspan="7"><strong>Workflow automation</strong></td></tr>
    <tr class="subsection"><td colspan="7"><strong>Streamline and automate workflows to reduce errors and delays while increasing efficiency and innovation using collaborative playbooks to speed structured team processes, from incident response and software release cycle management to accelerating operational logistics, as well as workflow dashboards to assess and refine process outcomes and operations.</strong></td></tr>
    <tr>
      <td><strong>Collaborative playbooks</strong>: <a href="https://docs.mattermost.com/repeatable-processes/learn-about-playbooks.html">Collaborative playbooks</a> provide structure, monitoring and automation for repeatable, team-based processes integrated with the Mattermost platform. Use cases include incident response, software release management, and logistical operations. Playbooks monitor channels for keywords or user actions to trigger structured processes, which bring up a set of individual or shared tasks, each associated with manual or automated actions. <p>As playbooks execute, some may have requirements for broadcasting status updates to stakeholders at regular intervals, conducting retrospectives after the core process is complete, or meeting other customer needs as exit criteria for each playbook “run.” Advanced permissions are also available to delegate and manage playbook controls in larger organizations.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Workflow dashboards</strong>: <a href="https://docs.mattermost.com/repeatable-processes/metrics-and-goals.html">Workflow dashboards</a> unlock insights about the performance of collaborative workflows across organizations. They compare the output metrics from different runs of collaborative playbooks against targets and historical performance. <p>Examples of metrics-based workflow dashboards that can be set up to monitor and inform performance include time to detect and time to resolve in incident response workflows, workplan completion percentage for monthly software releases management workflows, and launch success rate for logistical workflows involving launch operations.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <!-- Federated communications -->
    <tr class="section"><td colspan="7"><strong>Federated communications</strong></td></tr>
    <tr class="subsection"><td colspan="7"><strong>Connect across organizations using Mattermost and Microsoft Teams to share information and accelerate collaborative, cross-organizational workflows.</strong></td></tr>
    <tr>
      <td><strong>Microsoft Teams messaging integration</strong>: Increase focus and adaptability across your organization by <a href="https://docs.mattermost.com/about/maximize-microsoft-investments.html">connecting users across Microsoft Teams and Mattermost</a>. Microsoft Teams often serves as a centralized, organization-wide standard for general collaboration and everyday productivity, which can complicate the business case for customizing workflows and integrated toolsets to meet the specialized needs of technical and operational teams. <p>Mattermost is often deployed to supplement a centralized, general purpose Microsoft Teams deployment with a dedicated environment for developers, security professionals, and operators. Integrated direct messaging and group messaging across Microsoft Teams and Mattermost deployments connects an organization to the best of both worlds, helping teams unlock their full potential.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Connected Workspaces</strong>: Communicate across organizations using Mattermost by synchronizing messages, emoji reactions, and file sharing in real time through <a href="https://docs.mattermost.com/onboard/connected-workspaces.html">Mattermost Connected Workspaces</a>.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <!-- Support -->
    <tr class="section"><td colspan="7"><strong>Support</strong></td></tr>
    <tr class="subsection"><td colspan="7"><strong>A range of support options are available across Mattermost Free, Professional, and Enterprise offerings.</strong></td></tr>
    <tr>
      <td><strong>Community Support</strong>: Community support for all Mattermost offerings is available on peer-to-peer <a href="https://forum.mattermost.com/c/trouble-shoot/16">trouble shooting forums</a>. Organizations using Mattermost Free to evaluate a future purchase of Mattermost Enterprise can <a href="https://mattermost.com/contact-sales/">contact sales</a> to apply for early access to commercial support as part of the evaluation process.</td>
      <td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Professional Support</strong>: Professional Support includes business hours support from 8am to 8pm United States Pacific Time (UTC-8 except for U.S. daylight savings time), with next business day response time via email and the Mattermost <a href="https://support.mattermost.com/hc/en-us/requests/new">online ticketing system</a>. For more information, please see <a href="https://mattermost.com/support-terms/">Support Terms</a>.</td>
      <td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Enterprise Support</strong>: Enterprise Support is available 24×7 at all times on all days via email and the Mattermost <a href="https://support.mattermost.com/hc/en-us/requests/new">online ticketing system</a> with a 4-hour response time service-level target. For more information, please see <a href="https://mattermost.com/support-terms/">Support Terms</a>.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
    <tr>
      <td><strong>Premier Support</strong>: Available as an additional purchase offering additional license entitlements for non-production environments, direct access to senior support team members, screen-sharing and audio calling for P1 and P2 tickets, and access to a private channel with Mattermost technical staff. For more information, please see <a href="https://mattermost.com/support-terms/">Support Terms</a>.</td>
      <td></td><td></td><td></td><td><img src="../_static/images/check-circle-green.svg"></td><td><img src="../_static/images/check-circle-green.svg"></td><td>v9.11+</td>
    </tr>
  </tbody>
</table>

See a [complete list of features](https://mattermost.com/pricing) on the Mattermost website.

Note: Mattermost Enterprise Advanced requires a Mattermost Server running v10.9 or later and a PostgreSQL database. Enterprise plugins must be updated to support the new license (most of which are pre-packaged from v10.9)
