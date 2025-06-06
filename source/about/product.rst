Mattermost: The Intelligent Mission Environment (IME)
======================================================

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   /about/editions-and-offerings.rst
   /about/plans.md
   /about/subscription.rst
   /about/certifications-and-compliance.rst
   /about/accessibility-compliance-policy.rst
   /about/releases-lifecycle.rst
   /about/frequently-asked-questions.rst

Overview
--------

Mattermost is the secure collaboration and workflow platform purpose-built for mission-critical operations. Designed to operate across the most demanding environments — from classified networks to the tactical edge — Mattermost enables organizations to maintain full control of their communications, workflows, and infrastructure while accelerating decision-making.

The platform provides sovereign, AI-integrated capabilities for secure messaging, workflow automation, task management, and real-time communication. It offers extensibility through open APIs and integrations, and deploys flexibly across on-premises, cloud, and air-gapped environments. Whether operating in a disconnected edge node or a centralized data center, Mattermost delivers operational resilience, adaptability, and focus.

What is the Intelligent Mission Environment (IME)?
--------------------------------------------------

The Intelligent Mission Environment (IME) is Mattermost’s unified platform for secure, extensible, AI-powered collaboration and automation within a sovereign and cyber-resilient deployment architecture.

.. image:: /images/ime.jpg
   :alt: Infographic titled "Mattermost: The Intelligent Mission Environment," showcasing Mattermost as an AI-powered, self-hosted collaboration platform for defense, security, and critical enterprises. It highlights use cases in Cyber Defense, DevSecOps, and Mission Operations; a secure collaborative workflow with messaging, automation, audio/screenshare, project tracking, and AI tools; an integration platform with extensible architecture; and a deployment solution with Kubernetes-based, cyber-resilient scalability.

It is designed to meet the evolving needs of national security, defense, intelligence, cybersecurity, and critical infrastructure sectors for mission-critical workflows, including:

- **Cyber Defense**: Secure, out-of-band communications and automation for SOC/CERT workflows.
- **DevSecOps**: Sovereign CI/CD, ITSM, and digital system management at scale.
- **Mission Operations**: Collaboration across command, control, manufacturing, energy, and joint operations.

See the :doc:`Use Case Guide </about/use-cases>` to learn how operational teams use Mattermost to accelerate mission-critical work across a wide variety of disciplines.

Secure collaborative workflow
-----------------------------

Built on an extensible open-core architecture, Mattermost offers an array of collaborative tools across desktop, web, mobile, and embedded Microsoft user experiences.

- **Secure Web**: Works in browser with or without internet access.
- :doc:`Managed Desktop </deploy/desktop/desktop-app-deployment>`: MSI-supported clients for Windows, Mac, Linux.
- :doc:`Mobile & MDM </about/security/mobile-security>`: Pre-packaged or ID-only notification modes for secure BYOD.
- :doc:`Microsoft 365 Integration </integrate/mattermost-mission-collaboration-for-m365>`: Embed into Teams, Outlook, and M365 with SSO and shared presence.

Messaging collaboration
~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Channels </guides/collaborate>` delivers secure messaging and file sharing across desktop, web, and mobile. Features include:

- Public/private channels, direct messages, and threads.
- Role-based access controls and audit logs.
- Configurable notifications (alerts, keywords, muting).
- Pinning, bookmarking, search, and channel context.

Workflow automation
~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Playbooks </guides/repeatable-processes>` enables repeatable process automation for mission workflows such as incident response, shift changes, and logistics. With playbooks, you can:

- Define checklists, assign tasks, track status.
- Receive real-time updates via integrated channels.
- Automate response workflows with consistency.

Audio and screenshare
~~~~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Calls </collaborate/make-calls>` enables secure, real-time communication via 1:1 and group audio with screensharing. Features include:

- :doc:`Sovereign deployment </configure/calls-deployment>` for air-gapped or sensitive environments.
- Optional AI-based call :ref:`transcription <collaborate/make-calls:transcribe recorded calls>` and :ref:`summarization <collaborate/chat-with-copilot:summarize mattermost call recordings>`.

Project and task management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Boards provides Kanban-style project tracking, integrated directly with collaboration workflows. With Boards, you can:

- Assign, prioritize, and update tasks in real time.
- Seamlessly synchronize with messages and channels.

AI Agents and open APIs
~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Agents support customizable AI automation and integration with sovereign LLMs. Features include:

- AI-enabled assistance within chat and workflows.
- Retrieval-Augmented Generation (RAG), Semantic Search, and Responsible AI Guardrails support.

Integrations and AI platform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Layered extensibility enables full customization of workflows and automations:

- :ref:`Slash commands <about/integrations:custom slash commands>` and :ref:`webhooks <about/integrations:webhooks>`.
- `Open APIs <https://developers.mattermost.com/api-documentation/>`__ and :ref:`plugin architecture <about/integrations:plugins>` for full customization.
- Out-of-the-box support for :doc:`Jira </integrate/jira>`, :doc:`GitHub </integrate/github>`, :doc:`GitLab </integrate/gitlab>`, :doc:`ServiceNow </integrate/servicenow>`, `Jenkins <https://mattermost.com/marketplace/jenkins-plugin-2/>`_, and `PagerDuty <https://mattermost.com/marketplace/pagerduty/>`_.
- Secure video integrations: `Pexip <https://mattermost.com/marketplace/pexip-video-connect/>`_, Jitsi, `Webex <https://mattermost.com/marketplace/webex-cloud/>`_, :doc:`Zoom </integrate/zoom>`, and :doc:`Microsoft Teams </integrate/microsoft-teams-sync>`.
- Multi-agent coordination with MCP and Agent-to-Agent architectures (pre-release).

Sovereign & cyber-resilient deployment flexibility
--------------------------------------------------

IME supports operations :doc:`across any infrastructure </deploy/server/server-deployment-planning>`:

- **Tactical Edge**: DDIL-ready deployments on portable, ruggedized systems.
- **Air-Gapped**: Operate with no internet or DNS connectivity.
- **Private Data Centers**: Fully self-hosted, sovereign infrastructure.
- **Cloud Options**: Supported on Oracle Cloud, Azure (Gov, Global, Local), AWS GovCloud, GCP, and edge clouds.

Resilient by design
-------------------

IME is architected for operational continuity in all conditions:

- :doc:`High Availability </scale/high-availability-cluster-based-deployment>`: Auto-healing Kubernetes clusters.
- :doc:`Scalable </scale/scaling-for-enterprise>`: From a suitcase deployment to geo-distributed multi-tenant nodes.
- **STIG and FIPS-Compliant**: Meets FedRAMP, NIST 800-53, and other mandates.
- :doc:`Air-Gapped and Sovereign </deploy/server/air-gapped-deployment>`: Built for national-level trust and data control.

Get started
-----------

Mattermost empowers mission-critical teams with a sovereign, extensible, AI-ready collaboration platform that works where others cannot.

`Talk to an Expert <https://mattermost.com/contact-sales/>`_