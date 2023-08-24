Legal hold
===========

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

A legal hold, also known as a litigation hold, is a process that an organization uses to preserve all forms of relevant information when litigation is reasonably anticipated. It's a requirement established by the Federal Rules of Civil Procedure (FRCP) in the United States and similar laws in other jurisdictions.

Primary use cases include:

1. **Litigation**: In anticipation or in the event of a lawsuit, organizations need to preserve all relevant documents and electronic data to ensure they can adequately defend their position. A failure to do so could result in court penalties.
2. **Regulatory investigation**: If an organization is being investigated by a regulatory body, it may be required to preserve and produce certain documents or data.
3. **Audits**: During an audit, whether internal or external, an organization might need to put a hold on certain data that is relevant to the audit.
4. **Records management**: In some cases, organizations might use a legal hold to temporarily suspend the deletion of data that would otherwise be purged as part of its records management policy.

Mattermost is used as a secure collaboration hub by technical and operational teams, with critical documents and data shared on a daily basis. Thus, legal hold is a key requirement for Enterprises and public sector organizations who have deployed Mattermost for their teams, to meet compliance & auditory requirements while minimizing risk.

Below are step-by-step instructions on how to carry out a legal hold for Mattermost with XML-formatted data, Amazon S3 file storage, and archiving and compliance tools, such as `Smarsh <https://www.smarsh.com/>`__.

.. contents:: On this page:
  :backlinks: top
  :local:
  :depth: 2

How to carry out a legal hold
-----------------------------

Step 1: Upgrade to Mattermost Enterprise
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Legal hold is available in `Mattermost Enterprise </about/editions-and-offerings.html#mattermost-enterprise-edition>`__. Learn more about the Enterprise plan & request a quote online at https://mattermost.com/pricing/

Step 2: Establish a legal hold policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Establish a policy for when to implement a legal hold. This should be developed in consultation with your legal counsel and should include procedures for identifying relevant custodians (those who have potentially relevant information).

Establishing a legal hold policy first enables you to configure the Mattermost system correctly to meet your compliance & auditory requirements, minimizing associated risk.

Step 3: Enable legal hold in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1 - Configure your file storage as Amazon S3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. In Mattermost, go to **System Console > Environment > File Storage**.
2. Set the **File Storage System** to **Amazon S3**.
3. Connect the Amazon S3 storage with Mattermost by specifying the S3 bucket name, prefix, AWS region, and hostname. You may optionally specify the access keys if using IAM roles.
4. Learn more about file storage configuration options in our `product documentation </configure/environment-configuration-settings.html#file-storage>`__.

.. note::

    - For legal hold, only Amazon S3 is supported at this time, for increased reliability, compliance and automation capabilities.
    - Support for additional file storage options such as MinIO or local file storage are under consideration.
    - You may also optionally use our API to preserve data for legal hold. See our `electronic discovery </comply/electronic-discovery.html#mattermost-restful-api>`__ product documentation to learn more.

2 - Enable compliance exports
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enable compliance exports containing all messages and file uploads in an XML format to your AWS S3 file storage.

The exports include information on channel member history at the time the message was posted, which is critical information for some legal hold use cases. Entries for deleted messages and files are also included.

1. In Mattermost, go to **System Console > Compliance > Compliance Export**.
2. Set **Enable Compliance Exports** to **true**.
3. Set the **Compliance Export time**. Choose a time when fewer people are using your system, such as 2:00AM your local time.
4. Set the export file format to **Actiance XML**.
5. Learn more about compliance export configuration options in our `product documentation </comply/compliance-export.html>`__.

.. note::

    - For legal hold, only XML format is supported at this time. 
    - Support for additional file formats, such as CSV or EML, are under consideration.

3 - Leverage compliance API in your DLP tool of choice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Connect it directly to the Amazon S3 bucket where compliance exports are stored. Our recommended DLP tool of choice is `Smarsh <https://www.smarsh.com/>`__. Learn more about their legal hold & e-discovery processes in their `documentation <https://www.smarsh.com/platform/enterprise/discovery>`__.

You may optionally also use other tools that connect with Amazon S3, such as Active360, AwareHQ, Onna, or Trellix, though our team will be able to provide limited support using these tools.

4 - (Optional) Configure a data retention policy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is typically implemented alongside legal hold, though is not required.

1. In Mattermost, go to **System Console > Compliance > Data Retention Policies**.
2. Set either a **Global retention policy** that applies to all messages and files older in your system, or a **custom retention policy** for specific teams or channels.
3. Learn more about data retention configuration options in our `product documentation </comply/data-retention-policy.html>`__.

Step 4: Identify custodians
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the individuals or user groups that you want to place on legal hold.

Step 5: Initiate legal hold
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the built-in functionality in Smarsh to specify one or more custodians for legal hold, and the number of days the custodian(s) are placed on legal hold.

While the legal hold is in place, you may edit it by adding or removing custodians, as well as access the preserved data.

Step 6: Release legal hold
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the legal hold has completed, release it in Smarsh. This action will take custodians off of the legal hold.

Frequently asked questions
---------------------------

Who can implement legal hold?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only the System Administrator in Mattermost has the ability to implement legal hold.

Does a user know if they're placed under a legal hold in Mattermost?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, users will not be notified if they're placed under a legal hold. This allows for investigations to be conducted without influencing user behavior and without conflicts of interest.

What types of content does legal hold cover?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The legal hold covers all messages and file uploads shared in conversations where the legal hold is active, including messages posted by plugins, bots or webhooks. This includes messages or files shared in public channels, private channels, direct messages and group messages.

However, legal hold does not apply to reactions, playbooks, or audio calls.

Can users delete their messages while on a legal hold?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, users can delete messages, but they are retained for the purposes of legal hold when implemented with the aforementioned steps.

Can a legal hold be applied retroactively to collect past data?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, but this is only guaranteed for existing and future messages/files once legal hold is activated. It won't recover messages or files that were deleted before the legal hold was activated.

Is legal hold the same as e-discovery?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. While they serve a related use case, they are not the same.

Legal hold is an initial step to ensure relevant electronically stored information (ESI) is preserved. On the other hand, e-discovery is a multi-step process that uses this preserved data to identify, collect, preserve, process, review, and produce ESI in the context of a legal or investigative process.

How do I enable e-discovery for Mattermost?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Learn more about extracting data for e-discovery in our `product documentation </comply/electronic-discovery.html>`__.