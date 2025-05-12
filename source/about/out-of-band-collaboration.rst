Out-of-Band Collaboration
==========================

Out-of-Band (OOB) collaboration is a method of communication that occurs outside an organization’s primary business systems on a separate communications channel. 

This approach ensures teams can communicate and coordinate even when their main networks are compromised. Learn more about `key use cases <#key-use-cases>`__ below, and visit the Mattermost blog to learn how OOB collaboration helps you `maintain business continuity <https://mattermost.com/blog/out-of-band-communication-maintaining-business-continuity/>`_.

Mattermost for OOB
------------------

Organizations can use Mattermost as an OOB solution by either :doc:`self-hosting their instance </deploy/server/deploy-oob>` or leveraging :doc:`Mattermost’s Cloud SaaS offering </about/cloud-subscriptions>`.

Self-hosted
~~~~~~~~~~~~

We recommend one of the following self-hosted deployment options:

- `Azure Marketplace Offering <http://mattermost-docs-preview-pulls.s3-website-us-east-1.amazonaws.com/7816/deploy/server/deploy-kubernetes.html>`__: Use a Kubernetes deployment option available on the Azure Marketplace, separate from your own infrastructure.

- `Self-Hosted Kubernetes Deployment <http://mattermost-docs-preview-pulls.s3-website-us-east-1.amazonaws.com/7816/deploy/server/deploy-kubernetes.html>`__: Deploy Mattermost on Kubernetes in your own separate infrastructure or cloud, ensuring full control and customization.

Cloud
~~~~~

If you’d prefer a turnkey out-of-band solution that requires minimal IT overhead, we recommend Mattermost’s :doc:`Cloud SaaS offering </about/cloud-subscriptions>` for your out-of-band solution.

Why Mattermost is ideal for OOB
-------------------------------

Mattermost is uniquely suited for defense, intelligence, and security operations, and critical infrastructure OOB collaboration. Unlike traditional messaging tools that rely on third-party cloud services, Mattermost allows critical infrastructure teams to maintain ownership of their data, ensure lines of communication remain open during crises, improve their security posture, and ensure compliance with industry regulations.

- Mattermost delivers persistent, real-time collaboration that enables teams to coordinate seamlessly across channels — even during network disruptions and incidents.  

- Integration with mission-critical tooling connects Mattermost with popular monitoring and alerting systems — including ServiceNow, Prometheus, and Grafana — to streamline incident response and management.

- Customizable role-based access controls (RBACs) ensures the right people — and only the right people — have access to the right information, reducing security risks.  

- Mattermost uses encryption at rest and in transit to protect sensitive communications from unauthorized access, ensuring confidentiality in high-stakes scenarios.

Learn more about the `features to look for <https://mattermost.com/blog/out-of-band-communication-features/>`__ in an out-of-band communication solution by visiting the Mattermost blog. And then download our `Deploying an out-of-band collaboration environment <https://mattermost.com/mattermost-out-of-band-deployment-guide/>`__ guide.

Key use cases
--------------

When cyberattacks or system breaches occur, organizations need an independent communication channel to coordinate response efforts without relying on compromised networks. Out-of-Band collaobration is essential for the following use cases:

- **Failover communications**: During network outages and failures, businesses need a backup communication system to maintain operational continuity.

- **Red team exercises**: Security teams use OOB to conduct realistic penetration testing and cyber defense drills without tipping off employees or exposing test plans on shared networks.

- **Business continuity and risk mitigation**: Navigate network failures, downtime, security vulnerabilities, and delayed incident response with a backup communications channel for coordinating responses and keeping teams stay focused during outages, cyber incidents, and system failures.

- **Regulatory compliance**: Strengthen compliance and security by protecting sensitive information to meet regulatory requirements and prevent data breaches.

Best practices
--------------

Set up secure, dedicated, always-available communication channels, separate from primary networks, to ensure continuity during disruptions.

Ensure your teams know when to switch to backup systems by defining clear usage policies.

Use Mattermost Playbooks to build your prescribed workflows and streamline recurring processes, and accelerate response time by ensuring your collaborative playbooks in Mattermost are up-to-date.

Test and train regularly. Conduct routine drills and tabletop exercises to ensure teams are familiar with OOB procedures before a crisis occurs.  

Use role-based access controls to minimize security risks by restricting access to OOB tools based on roles.