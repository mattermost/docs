Cloud
======

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   Cloud Dedicated </product-overview/cloud-dedicated>
   Cloud Shared </product-overview/cloud-shared>
   Cloud VPC Private Connectivity </product-overview/cloud-vpc-private-connectivity>

Mattermost offers secure, cloud-based collaboration for fast moving enterprises that’s private, scaleable, and low maintenance. Cloud-native architecture supports organizations of any size for a deployment that scales with your team, without any resource planning.

Enterprises can choose between dedicated and shared infrastructure based on your organizations’ size, budget, technical requirements, and level of control and customization needed:

- :doc:`Mattermost Cloud Dedicated </product-overview/cloud-dedicated>`: Better suited for larger organizations or those with specific needs around security, compliance, and customization, who are willing to pay a premium for dedicated resources and enhanced support.
- :doc:`Mattermost Cloud Shared </product-overview/cloud-shared>`: A cost-effective solution for companies who don't have strict security and compliance requirements that need a straightforward, managed communication platform without the necessity for extensive customization or dedicated resources.
- :doc:`Cloud VPC Private Connectivity </product-overview/cloud-vpc-private-connectivity>`: Learn how to access Mattermost Cloud within your own internal network.

Compare offerings
-----------------

+-------------------------------+---------------+-------------+
| **Resource**                  | **Dedicated** | **Shared**  |
+===============================+===============+=============+
| Mattermost High Availability  | |checkmark|   | |checkmark| |
| cluster-based deployment      |               |             |
+-------------------------------+---------------+-------------+
| Network policy                | |checkmark|   | |checkmark| |
+-------------------------------+---------------+-------------+
| Namespace                     | |checkmark|   | |checkmark| |
+-------------------------------+---------------+-------------+
| Network                       | |checkmark|   |             |
+-------------------------------+---------------+-------------+
| Kubernetes High Availability  | |checkmark|   |             |
+-------------------------------+---------------+-------------+
| Database High Availability    | |checkmark|   |             |
+-------------------------------+---------------+-------------+
| Object storage                | |checkmark|   |             |
+-------------------------------+---------------+-------------+
| Encryption keys               | |checkmark|   |             |
+-------------------------------+---------------+-------------+
| Custom backup schedule        | |checkmark|   |             |
+-------------------------------+---------------+-------------+
| IP Filtering                  | |checkmark|   | |checkmark| |
+-------------------------------+---------------+-------------+
| Bring your own key            | |checkmark|   |             |
+-------------------------------+---------------+-------------+

Frequently asked questions about Mattermost Cloud
-------------------------------------------------

How do I buy a Mattermost Cloud subscription?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud subscriptions are offered as an annual subscription. Contact a `Mattermost Expert <https://mattermost.com/contact-sales/>`_ to buy a new subscription, or to renew, change, or cancel your existing subscription.

If you’re currently using a Mattermost Cloud trial, contact a `Mattermost Expert <https://mattermost.com/contact-sales/>`_ to upgrade to Mattermost Enterprise. Your plan immediately changes to your upgraded plan. You will be invoiced as specified in your sales agreement.

What is the minimum number of users I can purchase on a subscription? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The minimum purchase for a Mattermost license subscription is 100 users, with no set maximum. You can buy as many user seats as needed. 

Is Mattermost Cloud subject to taxes?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Mattermost reserves the right to assess applicable taxes as required by local law. Depending on location, you may be charged transaction taxes when purchasing our product. `Prices <https://mattermost.com/pricing/>`_ on our website are exclusive of sales tax or VAT.

Where does instance and data reside?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dedicated instance and data, including logs and backups, resides in the **AWS us-east-1 region**, located in Virginia, United States.

For data residency options outside of the US, contact a `Mattermost Expert <https://mattermost.com/contact-sales/>`_, or work with a `Mattermost partner <https://mattermost.com/partners/>`_.

When will more region support be available?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Cloud Dedicated </product-overview/cloud-dedicated>` will support data residency based on feedback from our customers.

If you require your data to reside in an area outside of the United States, please contact a `Mattermost Expert <https://mattermost.com/contact-sales/>`_ or consider deploying one of our `self-hosted options <https://mattermost.com/download/>`_ that provides you with full control of your data. 

Do you provide cross-region failover in the event of an outage in AWS us-east-1 region?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud is hosted in AWS us-east-1 region. Cross-region failover is planned, but not yet in the roadmap. If you have feedback or require cross-region failover, please reach out to a `Mattermost Expert <https://mattermost.com/contact-sales/>`_.

Is Mattermost Cloud a dedicated instance running on AWS systems?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud Dedicated can be deployed as a dedicated Mattermost environment running with separate infrastructure for your requirements (e.g., separate database, separate VMs, separate Kubernetes cluster).

How is customer data in Mattermost Cloud Dedicated encrypted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost uses AWS-provided functionality to enable encryption-at-rest for both databases and file stores. See `Encrypting Amazon RDS resources - Amazon Relational Database Service <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>`_ and `Protecting data using server-side encryption - Amazon Simple Storage Service <https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html>`_ for details.

Whether customer data should be stored in Mattermost Cloud depends heavily on the nature of the data and compliance requirements. We recommend that customers set up their own internal policies or controls around what can and cannot be put into Mattermost.

Are S3-managed keys used for server-side encryption?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, with Mattermost Cloud Dedicated. You can also bring your own keys for database and Amazon S3.

Are you SOC2 Type 2 certified?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes.

Who is responsible for server maintenance and upgrades?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Mattermost Cloud deployments, Mattermost is responsible for regular security patches, software updates/releases, performance tuning, and ensuring uptime commitments.

Mattermost performs monthly upgrades to your instance with the latest patch release during your preferred maintenance window.

Mattermost may conduct unscheduled maintenance to address high-severity issues affecting the security, availability, or reliability of your instance. Maintenance windows are announced in advance on https://status.mattermost.com/

Mattermost Cloud uses a Cloud-First Release Strategy with Ring-Based staged releases aligned to Mattermost licenses with a 24 hour soak time for :doc:`Mattermost Cloud Dedicated </product-overview/cloud-dedicated>` and for Enterprise customers using :doc:`Mattermost Cloud Shared </product-overview/cloud-shared>`.

Can I use a custom URL at my organization's domain?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Custom URLs are not currently supported for Mattermost Cloud deployments.

`Book a live demo <https://mattermost.com/request-demo/>`_  or `talk to a Mattermost expert <https://mattermost.com/contact-sales/>`_ to explore tailored solutions for your organization's secure collaboration needs. Or try Mattermost yourself with a `1-hour preview <https://mattermost.com/sign-up/>`_ for instant access to a live sandbox environment.
