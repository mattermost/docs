Overview
=========

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

The Intelligent Mission Environment (IME)
------------------------------------------

Mattermost is an Intelligent Mission Environment (IME), purpose-built for mission-critical operations. It delivers a unified platform for secure, extensible, AI-powered collaboration and automation, deployable across the most demanding environments—from classified networks to the tactical edge. Organizations use Mattermost to maintain full control over communications, workflows, and infrastructure while accelerating decision-making.

IME integrates secure messaging, workflow automation, task management, and real-time communication within a sovereign, cyber-resilient architecture. It supports extensibility through open APIs and integrations, and runs flexibly across on-premises, cloud, and air-gapped systems—enabling operational focus, adaptability, and resilience from edge nodes to centralized data centers.

.. image:: /images/ime.jpg
   :alt: Infographic titled "Mattermost: The Intelligent Mission Environment", showcasing Mattermost as an AI-powered, self-hosted collaboration platform for defense, security, and critical enterprises. It highlights use cases in Cyber Defense, Development, Security, and Operations (DevSecOps), and Mission Operations; a secure collaborative workflow with messaging, automation, audio/screenshare, project tracking, and AI tools; an integration platform with extensible architecture; and a deployment solution with Kubernetes-based, cyber-resilient scalability.

It is designed to meet the evolving needs of national security, defense, intelligence, cybersecurity, and critical infrastructure sectors for mission-critical workflows, including:

- **Cyber Defense**: Secure, out-of-band communications and automation for Security Operation Center (SOC)/Computer Emergency Response Team (CERT) workflows.
- **DevSecOps**: Sovereign Continuous Integration Continuous delivery (CI/CD), Information technology service management (ITSM), and digital system management at scale.
- **Mission Operations**: Collaboration across command, control, manufacturing, energy, and joint operations.

See the :doc:`Use Case Guide </about/use-cases>` to learn how operational teams use Mattermost to accelerate mission-critical work across a wide variety of disciplines.

Secure collaborative workflow
-----------------------------

Built on an extensible open-core architecture, Mattermost offers an array of collaborative tools across :doc:`managed Windows, Mac, or Linux desktop applications </deploy/desktop/desktop-app-deployment>`, secure web browsers with or without internet access, :doc:`Bring your own device (BYOD) or mobile device management (MDM)-managed mobile </about/security/mobile-security>`, and :doc:`embedded Microsoft 365 </integrate/mattermost-mission-collaboration-for-m365>` user experiences.

Messaging collaboration
~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Channels </guides/messaging-collaboration>` enables secure, real-time and asynchronous communication across web, desktop, and mobile—powering mission-critical collaboration and Chat Operations (ChatOps) workflows across connected, hybrid, and air-gapped environments. Channels feature the following capabilities: 

- :ref:`Public <collaborate/channel-types:public channels>` and :ref:`private <collaborate/channel-types:private channels>` channels, :ref:`direct messages <collaborate/channel-types:direct message channels>`, and :doc:`threaded conversations </collaborate/organize-conversations>` for structured operational coordination.
- :doc:`Role-based access controls </collaborate/learn-about-roles>` and :ref:`audit logs <manage/logging:audit logging>` to support need-to-know enforcement.
- Configurable :doc:`notifications </preferences/manage-your-notifications>` (e.g., :ref:`alerts <preferences/manage-your-notifications:default notifications>`, :doc:`keyword triggers </preferences/manage-your-mentions-keywords-notifications>`, :doc:`muting </preferences/manage-your-channel-specific-notifications>`) to surface high-priority activity.
- Integrated ChatOps capabilities via :ref:`slash commands <about/integrations:custom slash commands>`, :ref:`bots <about/integrations:bots>`, and :ref:`incoming webhooks <about/integrations:webhooks>` for real-time automation and system alerts.
- :ref:`Pinning <collaborate/save-pin-messages:pin messages>`, :doc:`bookmarking </collaborate/manage-channel-bookmarks>`, and :doc:`advanced search </collaborate/search-for-messages>` to maintain continuity and context in high-volume environments.
- Cross-platform support on web, desktop, and mobile clients for flexible field to command and control access.

.. image:: /images/messaging.png
   :alt: An image showing Mattermost messaging collaboration, highlighting the ability to create public and private channels, direct messages, and threaded conversations for secure, real-time communication across web, desktop, and mobile.

Workflow automation
~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Playbooks </guides/workflow-automation>` standardizes and automates mission workflows such as incident response, shift changeovers, and operational checklists—reducing human error and improving procedural consistency. Playbooks feature: 

- Structured :ref:`checklists <repeatable-processes/work-with-playbooks:make checklists>` with assigned :ref:`tasks and due dates <repeatable-processes/work-with-tasks:tasks and due dates>` to operationalize standard and incident or emergency operating procedures.
- Automated :doc:`status updates and real-time notifications </repeatable-processes/notifications-and-updates>` in linked channels to keep stakeholders informed of workflow progress or blockers.
- Embedded :ref:`actions , assignments, and guidance <repeatable-processes/work-with-playbooks:actions>` for repeatable execution to ensure operational consistency.
- Timeline, :ref:`retrospectives <repeatable-processes/learn-about-playbooks:retrospective>`, and :ref:`metric tracking <repeatable-processes/metrics-and-goals:metrics>` for after-action reviews and accountability.
- Integration :ref:`triggers <repeatable-processes/work-with-runs:send outgoing webhooks>` (e.g., alerts from monitoring tools) to launch workflows automatically and decrease time to execution.

.. image:: /images/playbooks.png
   :alt: An image showing Mattermost playbooks, highlighting the ability to create structured checklists with tasks and due dates, automate status updates, and track metrics for operational workflows.

Audio and screenshare
~~~~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Calls </collaborate/audio-and-screensharing>` enables real-time communication and troubleshooting through sovereign audio calling and screen sharing—supporting secure knowledge transfer and fast response in time-sensitive scenarios. Key capabilities include:

- Enables :ref:`1:1 and group audio calls <collaborate/make-calls:join a call>` directly within channels and direct messages, maintaining contextual awareness and access control based on channel membership.
- Supports secure :ref:`screen sharing <collaborate/make-calls:share your screen>` for visual coordination and analysis.
- Operates in :doc:`sovereign, air-gapped, or sensitive network </configure/calls-deployment>` environments.
- Offers optional :ref:`AI-based transcription <collaborate/make-calls:transcribe recorded calls>` and :ref:`summarization <guides/agents:analyze threads and channels>` for meeting capture and follow ups.
- Works across web, desktop, and mobile for flexible, secure access.

.. image:: /images/call-window.png
   :alt: An image showing a Mattermost call window, highlighting the ability to make secure audio calls and share screens within channels or direct messages, with options for live text captions, transcription, and summarization.

Project and task management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Boards </guides/project-task-management>` enables you to coordinate operational work with Kanban-style planning that integrates directly into messaging workflows—enabling transparency, prioritization, and accountability across teams with the following capabilities: 

- Provides visual task :doc:`boards </boards/work-with-boards>` with drag-and-drop :doc:`cards </boards/work-with-cards>` and customizable workflows, supporting contextual awareness and :ref:`role-based task visibility <boards/share-and-collaborate:board permissions>`.
- Delivers real-time updates and synchronization with :ref:`linked Mattermost channels <boards/navigate-boards:link a board to a channel>`.
- Supports :ref:`card-level assignments, checklists, labels, and due dates <boards/work-with-cards:card properties>` for operational clarity.
- Enables :ref:`filtering <boards/groups-filter-sort:filters>` and :ref:`sorting <boards/groups-filter-sort:sorting cards>` to manage backlogs, priorities, and forward planning.
- Maintains :ref:`project visibility <boards/navigate-boards:sidebar categories>` without requiring users to switch away from primary communication channels.

.. image:: /images/boards-kanban.png
   :alt: An image showing a Kanban board in Mattermost, highlighting the ability to manage tasks and projects visually with drag-and-drop functionality, customizable workflows, and real-time updates.

AI Agents and open APIs
~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Agents </guides/agents>` accelerate decisions and streamline repetitive tasks with AI-driven assistance, fully controllable within sovereign infrastructure—offering intelligent support for both users and workflows: 

- Provides configurable AI assistants that :ref:`summarize threads <guides/agents:summarize discussion threads>`, :ref:`extract action items and answer questions <guides/agents:chat with agents>` with contextual insight and operational awareness.
- Supports :ref:`direct interactions with AI agents <guides/agents:chat with agents>` in dedicated threads or channels.
- Enables :ref:`semantic search <guides/agents:search with ai>` using natural language to surface relevant content across Mattermost data.
- Supports Retrieval-Augmented Generation (RAG), :ref:`custom instructions <configure/agents-admin-guide:custom instructions>`, and responsible :ref:`AI guardrails <configure/agents-admin-guide:permission configuration>` for secure automation.
- Integrates with :doc:`local models </agents/docs/providers>` (e.g., Ollama, vLLM) and cloud LLMs via OpenAI-compatible APIs for flexible deployment.

.. image:: /images/agents-meeting-summary.png
   :alt: An image showing an AI agent summarizing a meeting in Mattermost, highlighting the agent's ability to extract key points and action items from the conversation.

Integrations and AI platform
-----------------------------

The Intelligent Mission Environment (IME) is built for secure, extensible integration with mission-critical systems and AI workflows. Designed to operate in sovereign, regulated, and disconnected environments, IME supports modular automation, multi-agent orchestration, and the secure deployment of both local and cloud-based AI models—enabling faster decision-making while maintaining full control over data, infrastructure, and model behavior.

Layered extensibility
~~~~~~~~~~~~~~~~~~~~~~

Built to integrate securely with complex enterprise and mission-critical environments, this model enables teams to tailor workflows, automate operations, and connect to external systems using open standards and modular components—supporting rapid deployment of automation while maintaining flexibility and compliance across both air-gapped and connected environments.

Key capabilities include:

- Secure video integrations: Embed secure video platforms such as `Pexip <https://mattermost.com/marketplace/pexip-video-connect/>`_, `Webex <https://mattermost.com/marketplace/webex-cloud/>`_, and Jitsi for sovereign mission collaboration.
- Pre-packaged and custom integrations: Quickly connect with systems like :doc:`GitHub </integrate/github>`, :doc:`GitLab </integrate/gitlab>`, :doc:`Jira </integrate/jira>`, :doc:`ServiceNow </integrate/servicenow>`, `Jenkins <https://mattermost.com/marketplace/jenkins-plugin-2/>`_, and `PagerDuty <https://mattermost.com/marketplace/pagerduty/>`_.
- :ref:`Webhooks <about/integrations:webhooks>` and :ref:`slash commands <about/integrations:custom slash commands>`: Enable real-time, event-driven automation and user-triggered actions directly from chat.
- Plugin architecture: Extend the Mattermost core with `custom UI components, server-side logic, and third-party services <https://developers.mattermost.com/integrate/customization/>`_.

Learn more in our :doc:`Integrations Guide </about/integrations>`.

.. image:: /images/github-integration.png
   :alt: An image showing the GitHub integration in Mattermost, highlighting the ability to receive notifications and manage pull requests directly within channels.

Multi-Agent, Multi-LLM integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A secure, extensible foundation for integrating multiple large language models (LLMs) and autonomous agents within a sovereign control plane enables organizations to operationalize AI within sovereign infrastructure—fusing data across systems, accelerating decisions, and maintaining full control over AI model access and performance. Organizations can leverage the following capabilities to operationalize AI:

- :doc:`Sovereign AI </agents/docs/sovereign_ai>` model support: Integrate with :doc:`OpenAI, Anthropic, Meta Llama, and other LLMs </agents/docs/providers>` via secure APIs.
- :ref:`Custom instructions <configure/agents-admin-guide:custom instructions>` and Retrieval-Augmented Generation (RAG): Adapt agent behavior to domain-specific tasks using internal data and policies.
- :ref:`Semantic search <guides/agents:search with ai>` and natural language interaction: Provide operational teams with intuitive ways to retrieve and act on information.
- :ref:`Responsible AI control plane <agents/docs/sovereign_ai:security and compliance features>`: Define model access policies, enforce guardrails, and monitor agent activity with feedback loops.
- Multi-agent orchestration: Use the :ref:`Mission Control Plane (MCP) <configure/agents-admin-guide:model context protocol (mcp) integration>` and agent-to-agent protocols to coordinate actions across multiple autonomous agents. *

Sovereign & cyber-resilient deployment flexibility
--------------------------------------------------

The Intelligent Mission Environment (IME) is engineered for resilient, mission-critical operations—whether at the tactical edge, inside sovereign data centers, or across regulated cloud environments. Built on Kubernetes and designed for high availability, IME ensures continuity, scalability, and full operational control across diverse infrastructure profiles.

Tactical edge
~~~~~~~~~~~~~

IME runs on lightweight, ruggedized, or mobile infrastructure, optimized for disconnected, denied, intermittent, and limited (DDIL) conditions.

- Supports :doc:`single-node Linux binaries </deploy/server/deploy-linux>` and :doc:`containerized deployments in local Kubernetes environments </deploy/server/deploy-containers>` for rapid, lightweight setup.
- Enables flexible deployment on compact, portable compute platforms—ideal for ships, forward operating bases, mobile command units, or disconnected kits. *
- Operates fully :doc:`air-gapped </deploy/server/air-gapped-deployment>` without reliance on internet, Domain Name System (DNS), or external authentication systems.
- Delivers secure communications, screen sharing, and workflow automation in isolated or DDIL conditions.

Private Cloud & sovereign datacenter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For high-security environments requiring full infrastructure control, IME supports scalable, highly available deployment within sovereign datacenters.

- :doc:`Kubernetes-native architecture </deploy/server/deploy-kubernetes>` enables containerized services, self-healing workloads, and zero-downtime updates.
- :doc:`High availability </scale/high-availability-cluster-based-deployment>` through clustering across application, database, and proxy layers.
- :doc:`Horizontal scalability </scale/scaling-for-enterprise>` to tens of thousands of users per instance.
- Complies with Security Technical Implementation Guide (STIG), Federal Information Processing Standard 140-3 (FIPS 140-3), and Federal Risk and Authorization Management Program (FedRAMP)-aligned security standards. *

Hyperscaler & sovereign Cloud support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IME is deployable across :doc:`major cloud providers </deploy/server/deploy-kubernetes>` with support for hybrid and sovereign architectures:

- Microsoft Azure – Supports virtual machines (VM) and Kubernetes deployments across Global, Government, and Local Regions.
- Amazon Web Services (AWS) – Deployable on AWS Global, GovCloud (US), and Outposts.
- Google Cloud – Supports Google Cloud Platform and Distributed Cloud (Edge and Hosted) * roadmap to marketplace availability.
- Oracle Cloud Infrastructure – Available in the Oracle Marketplace for VM and Kubernetes deployments, including Oracle Sovereign Cloud.

Get started
-----------

Mattermost provides mission-critical teams with a sovereign, extensible, and AI-integrated collaboration platform designed for secure operations across the most challenging environments. `Talk to an Expert <https://mattermost.com/contact-sales/>`_ to explore how to architect your Intelligent Mission Environment.