Cloud subscriptions
===================

.. include:: ../_static/badges/ent-cloud-only.rst
  :start-after: :nosearch:

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   Cloud Dedicated </about/cloud-dedicated>
   Cloud Shared </about/cloud-shared>

Mattermost offers secure, cloud-based collaboration for fast moving enterprises that’s private, scaleable, and low maintenance. Cloud-native architecture supports organizations of any size for a workspace that scales with your team, without any resource planning.

Enterprises can choose between dedicated and shared infrastructure based on your organizations’ size, budget, technical requirements, and level of control and customization needed:

- :doc:`Mattermost Cloud Dedicated </about/cloud-dedicated>`: Better suited for larger organizations or those with specific needs around security, compliance, and customization, who are willing to pay a premium for dedicated resources and enhanced support.
- :doc:`Mattermost Cloud Shared </about/cloud-shared>`: A cost-effective solution for companies who don't have strict security and compliance requirements that need a straightforward, managed communication platform without the necessity for extensive customization or dedicated resources.

Compare offerings
-----------------

+-------------------------------+---------------+------------+
| **Resource**                  | **Dedicated** | **Shared** |
+===============================+===============+============+
| Mattermost High Availability  |      YES      |     YES    |
| cluster-based deployment      |               |            |
+-------------------------------+---------------+------------+
| Network policy                |      YES      |     YES    |
+-------------------------------+---------------+------------+
| Namespace                     |      YES      |     YES    |
+-------------------------------+---------------+------------+
| Network                       |      YES      |     NO     |
+-------------------------------+---------------+------------+
| Kubernetes High Availability  |      YES      |     NO     |
+-------------------------------+---------------+------------+
| Database High Availability    |      YES      |     NO     |
+-------------------------------+---------------+------------+
| Object storage                |      YES      |     NO     |
+-------------------------------+---------------+------------+
| Encryption keys               |      YES      |     NO     |
+-------------------------------+---------------+------------+
| Custom backup schedule        |      YES      |     NO     |
+-------------------------------+---------------+------------+
| IP Filtering                  |      YES      |     YES    |
+-------------------------------+---------------+------------+
| Bring your own key            |      YES      |     NO     |
+-------------------------------+---------------+------------+

Frequently asked questions about Mattermost Cloud
-------------------------------------------------

How do I buy a Mattermost Cloud subscription?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud subscriptions are offered as an annual subscription. Contact a `Mattermost Expert <https://mattermost.com/contact-sales/>`_ to buy a new subscription, or to renew, change, or cancel your existing subscription.

If you’re currently using a Mattermost Cloud trial, contact a `Mattermost Expert <https://mattermost.com/contact-sales/>`_ to upgrade to Mattermost Enterprise. Your plan immediately changes to your upgraded plan. You will be invoiced as specified in your sales agreement.

Is Mattermost Cloud subject to taxes?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Mattermost reserves the right to assess applicable taxes as required by local law. Depending on location, you may be charged transaction taxes when purchasing our product. `Prices <https://mattermost.com/pricing/>`_ on our website are exclusive of sales tax or VAT.

Where does instance and data reside?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dedicated instance and data, including logs and backups, resides in the **AWS us-east-1 region**, located in Virginia, United States.

For data residency options outside of the US, contact a `Mattermost Expert <https://mattermost.com/contact-sales/>`_, or work with a `Mattermost partner <https://mattermost.com/partners/>`_.

When will more region support be available?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Cloud Dedicated </about/cloud-dedicated>` will support data residency based on feedback from our customers.

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

Mattermost Cloud uses a Cloud-First Release Strategy with Ring-Based staged releases aligned to Mattermost licenses with a 24 hour soak time for :doc:`Mattermost Cloud Dedicated </about/cloud-dedicated>` and for Enterprise customers using :doc:`Mattermost Cloud Shared </about/cloud-shared>`.
