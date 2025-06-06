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
   :alt: Infographic titled "Mattermost: The Intelligent Mission Environment," showcasing Mattermost as an AI-powered, self-hosted collaboration platform for defense, security, and critical enterprises. It highlights use cases in Cyber Defense, DevSecOps, and Mission Operations; a secure collaborative workflow with messaging, automation, audio/screenshare, project tracking, and AI tools; an integration platform with extensible architecture; and a deployment solution with Kubernetes-based, cyber-resilient scalability.

It is designed to meet the evolving needs of national security, defense, intelligence, cybersecurity, and critical infrastructure sectors for mission-critical workflows, including:

- **Cyber Defense**: Secure, out-of-band communications and automation for SOC/CERT workflows.
- **DevSecOps**: Sovereign CI/CD, ITSM, and digital system management at scale.
- **Mission Operations**: Collaboration across command, control, manufacturing, energy, and joint operations.

See the :doc:`Use Case Guide </about/use-cases>` to learn how operational teams use Mattermost to accelerate mission-critical work across a wide variety of disciplines.

Secure collaborative workflow
-----------------------------

Built on an extensible open-core architecture, Mattermost offers an array of collaborative tools across :doc:`managed Windows, Mac, or Linux desktop applications </deploy/desktop/desktop-app-deployment>`, secure web browsers with or without internet access, :doc:`BYOD or MDM managed mobile </about/security/mobile-security>`, and :doc:`embedded Microsoft 365 </integrate/mattermost-mission-collaboration-for-m365>` user experiences.

Messaging collaboration
~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Channels </guides/messaging-collaboration>` enables secure, real-time and asynchronous communication across web, desktop, and mobile—powering mission-critical collaboration and ChatOps workflows across connected, hybrid, and air-gapped environments. Channels feature the following capabilities: 

- Public and private channels, direct messages, and threaded conversations for structured operational coordination.
- Role-based access controls and audit logs to support need-to-know enforcement.
- Configurable notifications (e.g., alerts, keyword triggers, muting) to surface high-priority activity.
- Integrated ChatOps capabilities via slash commands, bots, and incoming webhooks for real-time automation and system alerts.
- Pinning, bookmarking, and advanced search to maintain continuity and context in high-volume environments.
- Cross-platform support on web, desktop, and mobile clients for flexible field and enterprise access.

Workflow automation
~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Playbooks </guides/workflow-automation>` standardizes and automates mission workflows such as incident response, shift changeovers, and operational checklists—reducing human error and improving procedural consistency. Playbooks feature: 

- Structured checklists with assigned tasks and due dates to operationalize standard and incident or emergency operating procedures.
- Automated status updates and real-time notifications in linked channels to keep stakeholders informed of workflow progress or blockers.
- Embedded actions, assignments, and guidance for repeatable execution to ensure operational consistency.
- Timeline, retrospectives, and metric tracking for after-action reviews and accountability.
- Integration triggers (e.g., alerts from monitoring tools) to launch workflows automatically and decrease time to execution.

Audio and screenshare
~~~~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Calls </collaborate/make-calls>` enables real-time communication and troubleshooting through sovereign audio calling and screen sharing—supporting secure knowledge transfer and fast response in time-sensitive scenarios. Key capabilities include:

- 1:1 and group audio calling integrated with channels and DMs
- Secure screen sharing for collaborative analysis and coordination
- Sovereign deployment support for air-gapped or sensitive networks
- Optional AI-powered transcription and summarization of meetings
- Cross-platform access on web, desktop, and mobile endpoints

Project and task management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Boards </guides/project-task-management>` enables you to coordinate operational work with Kanban-style planning that integrates directly into messaging workflows—enabling transparency, prioritization, and accountability across teams with the following capabilities: 

- Visual task boards with drag-and-drop cards and customizable workflows.
- Real-time updates and synchronization with linked Mattermost channels.
- Card-level assignments, checklists, labels, and due dates.
- Filtering and sorting to manage backlogs and sprint planning.
- Supports project visibility without context switching from primary communication channels.

AI Agents and open APIs
~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Agents </guides/agents>` accelerate decisions and streamline repetitive tasks with AI-driven assistance, fully controllable within sovereign infrastructure—offering intelligent support for both users and workflows: 

- Configurable AI assistants for summarizing threads, extracting action items, and answering questions.
- Direct interactions in dedicated threads or channels.
- Semantic search using natural language queries across Mattermost data.
- Support for Retrieval-Augmented Generation (RAG), custom instructions, and responsible AI guardrails.
- Integration with local models (e.g., Ollama, vLLM) or cloud LLMs via OpenAI-compatible APIs.

Integrations and AI platform
-----------------------------

The Intelligent Mission Environment (IME) is built for secure, extensible integration with mission-critical systems and AI workflows. Designed to operate in sovereign, regulated, and disconnected environments, IME supports modular automation, multi-agent orchestration, and the secure deployment of both local and cloud-based AI models—enabling faster decision-making while maintaining full control over data, infrastructure, and model behavior.

Layered extensibility
~~~~~~~~~~~~~~~~~~~~~~

Built to integrate securely with complex enterprise and mission-critical environments, this model enables teams to tailor workflows, automate operations, and connect to external systems using open standards and modular components—supporting rapid deployment of automation while maintaining flexibility and compliance across both air-gapped and connected environments.

Key capabilities include:

- Secure video integrations: Embed secure video platforms such as Pexip, Webex, and Jitsi for sovereign mission collaboration.
- Pre-packaged and custom integrations: Quickly connect with systems like GitHub, GitLab, Jira, ServiceNow, Jenkins, and PagerDuty.
- Webhooks and slash commands: Enable real-time, event-driven automation and user-triggered actions directly from chat.
- Plugin architecture: Extend the Mattermost core with custom UI components, server-side logic, and third-party services.

Learn more in our :doc:`Integrations Guide </about/integrations>`.

Multi-Agent, Multi-LLM integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A secure, extensible foundation for integrating multiple large language models (LLMs) and autonomous agents within a sovereign control plane enables organizations to operationalize AI within sovereign infrastructure—fusing data across systems, accelerating decisions, and maintaining full control over AI model access and performance. Organizations can leverage the following capabilities to operationalize AI:

- Sovereign AI model support: Integrate with OpenAI, Anthropic, Meta Llama, and other LLMs via secure APIs.
- Custom instructions and Retrieval-Augmented Generation (RAG): Adapt agent behavior to domain-specific tasks using internal data and policies.
- Semantic search and natural language interaction: Provide operational teams with intuitive ways to retrieve and act on information.
- Responsible AI control plane: Define model access policies, enforce guardrails, and monitor agent activity with feedback loops.
- Multi-agent orchestration: Use the Mission Control Plane (MCP) and agent-to-agent protocols to coordinate actions across multiple autonomous agents.

Sovereign & cyber-resilient deployment flexibility
--------------------------------------------------

The Intelligent Mission Environment (IME) is engineered for resilient, mission-critical operations—whether at the tactical edge, inside sovereign data centers, or across regulated cloud environments. Built on Kubernetes and designed for high availability, IME ensures continuity, scalability, and full operational control across diverse infrastructure profiles.

Tactical edge
~~~~~~~~~~~~~

IME runs on lightweight, ruggedized, or mobile infrastructure, optimized for disconnected, denied, intermittent, and limited (DDIL) conditions.

- Supports single-node Linux binary and container-based deployments.
- Operates without internet, DNS, or centralized authentication.
- Enables secure communications, screen sharing, and automation in fully air-gapped environments.

Private Cloud & sovereign datacenter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For high-security environments requiring full infrastructure control, IME supports scalable, highly available deployment within sovereign datacenters.

- Kubernetes-native architecture enables containerized services, self-healing workloads, and zero-downtime updates.
- High availability through clustering across application, database, and proxy layers.
- Horizontal scalability to tens of thousands of users per instance.
- Complies with STIG, FIPS 140-2, and FedRAMP-aligned security standards.

Hyperscaler & sovereign Cloud support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IME is deployable across major cloud providers with support for hybrid and sovereign architectures:

- Microsoft Azure – Supports VM and Kubernetes deployments across Global, Government, and Local Regions; roadmap includes Azure Air-Gapped.
- Amazon Web Services (AWS) – Deployable on AWS Global, GovCloud (US), and Outposts; marketplace support in development.
- Google Cloud – Supports Google Cloud Platform and Distributed Cloud (Edge and Hosted); roadmap to marketplace availability.
- Oracle Cloud Infrastructure – Available in the Oracle Marketplace for VM and Kubernetes deployments, including Oracle Sovereign Cloud; roadmap includes Oracle Air-Gapped.

Get started
-----------

Mattermost provides mission-critical teams with a sovereign, extensible, and AI-integrated collaboration platform designed for secure operations across the most challenging environments. `Talk to an Expert <https://mattermost.com/contact-sales/>_ to explore how to architect your Intelligent Mission Environment.
