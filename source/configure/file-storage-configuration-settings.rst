File storage configuration settings
===================================

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 25
  :target: https://mattermost.com/sign-up
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 25
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Configure file storage configuration by going to **System Console > Environment > File Storage**, or by editing the ``config.json`` file as described in the following table. 

Mattermost currently supports storing files on the local filesystem and Amazon S3 or S3-compatible containers. We have tested Mattermost with `MinIO <https://min.io/>`__ and `Digital Ocean Spaces <https://docs.digitalocean.com/products/spaces/>`__ products, but not all S3-compatible containers on the market. If you are looking to use other S3-compatible containers, we recommend completing your own testing.

.. include:: common-config-settings-notation.rst
    :start-after: :nosearch:

File storage system
-------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Select which file storage system is used.                     | - System Config path: **Environment > File Storage**                     |
| Can be either Local File System or Amazon S3.                 | - ``config.json`` setting: ``".FileSettings.DriverName:  local”,``       |
|                                                               | - Environment variable: ``MM_FILESETTINGS_DRIVERNAME``                   |
| - **local**: **(Default)** Files and images are stored in     |                                                                          |
|   the specified local file directory.                         |                                                                          |
| - **amazons3**: Files and images are stored on Amazon S3      |                                                                          |
|   based on the access key, bucket, and region fields          |                                                                          |
|   provided. The driver is compatible with MinIO (beta)        |                                                                          |
|   and Digital Ocean Spaces.                                   |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Local storage directory
-----------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The local directory to which files are written when the       | - System Config path: **Environment > File Storage**                     |
| **File storage system** is set to **local**.                  | - ``config.json`` setting: ``".FileSettings.Directory”,``                |
| Can be any directory writable by the user Mattermost is       | - Environment variable: ``MM_FILESETTINGS_DIRECTORY``                    |
| running as, and is relative to the directory where            |                                                                          |
| Mattermost is installed.                                      |                                                                          |
|                                                               |                                                                          |
| Defaults to **./data/**.                                      |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: When **File storage system** is set to **amazons3**, this setting has no effect.                                               |                      
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Maximum file size
-----------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Maximum file size for message attachments.                    | - System Config path: **Environment > File Storage**                     |
| This value must be specified in megabytes in the              | - ``config.json`` setting: ``".FileSettings.MaxFileSize: 104857600",``   |
| System Console, and in bytes in the ``config.json`` file.     | - Environment variable: ``MM_FILESETTINGS_MAXFILESIZE``                  |
|                                                               |                                                                          |
| The default is ``1048576`` bytes (**1** megabyte).            |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Warning**: Verify server memory can support your setting choice. Large file sizes increase the risk of server crashes and failed       |
| uploads due to network disruptions.                                                                                                      |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: If you use a proxy or load balancer in front of Mattermost, the following proxy settings must be adjusted accordingly:         |
|                                                                                                                                          |
| - For NGINX, use ``client_max_body_size``.                                                                                               |
| - For Apache use ``LimitRequestBody``.                                                                                                   |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Enable document search by content
---------------------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Enable users to search the contents of documents attached     | - System Config path: **Environment > File Storage**                                |
| to messages.                                                  | - ``config.json`` setting: ``".FileSettings.ExtractContent: true",``                |
|                                                               | - Environment variable: ``MM_FILESETTINGS_EXTRACTCONTENT``                          |
| - **true**: **(Default)** Documents are searchable by         |                                                                                     |
|   their content.                                              |                                                                                     |
| - **false**: Documents aren’t searchable by their content.    |                                                                                     |
|   When document content search is disabled, users can search  |                                                                                     |
|   for files by file name only.                                |                                                                                     |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| **Note**: Document content search results for files shared before upgrading to Mattermost Server v5.35 may be incomplete until an                   |
| extraction command is executed using the `CLI <https://docs.mattermost.com/manage/command-line-tools.html#mattermost-extract-documents-content>`__  | 
| or the `mmctl <https://docs.mattermost.com/manage/mmctl-command-line-tool.html?highlight=mmctl#mmctl-extract>`__. If this command is not run,       |
| users can search older files based on file name only.                                                                                               |
|                                                                                                                                                     |
| You can optionally install the following `dependencies <https://github.com/sajari/docconv#dependencies>`__ to extend content searching support in   |
| Mattermost to include file formats beyond PDF, DOCX, and ODT, such as DOC, RTF, XML, HTML, and PAGES:                                               |
|                                                                                                                                                     |
| - **tidy**: Used to search the contents of HTML and PAGES documents.                                                                                |
| - **wv**: Used to search the contents of DOC documents.                                                                                             |
| - **popplerutils**: Used to significantly improve server performance when extracting the contents of PDF documents.                                 |
| - **unrtf**: Used to search the contents of RTF documents.                                                                                          |
| - **Justtext**: Used to search HTML documents.                                                                                                      |
|                                                                                                                                                     |
| If you choose not to install these dependencies, you’ll see log entries for documents that couldn’t be extracted.                                   |
| Any documents that can’t be extracted are skipped and logged so that content extraction can proceed.                                                |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+

Enable searching content of documents within ZIP files
------------------------------------------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| This configuration setting enables users to search the        | - System Config path: **Environment > File Storage**                     |
| contents of compressed ZIP files attached to messages.        | - ``config.json`` setting: ``".FileSettings.ArchiveRecursion: false",``  |
|                                                               | - Environment variable: ``MM_FILESETTINGS_ARCHIVERECURSION``             |
| - **true**: Contents of documents within ZIP files are        |                                                                          |
|   returned in search results. This may have an impact on      |                                                                          |
|   server performance for large files.                         |                                                                          |
|   the specified local file directory.                         |                                                                          |
| - **false**: **(Default)** The contents of documents within   |                                                                          | 
|   ZIP files aren’t returned in search results.                |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: Document content search within ZIP files is available in Mattermost Server from v5.35, with mobile support coming soon.        |
| Searching document contents adds load to your server. For large deployments, or teams that share many large, text-heavy documents,       |
| we recommend you review our hardware requirements, and test enabling this feature in a staging environment before enabling it in         |
| a production environment.                                                                                                                |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Amazon S3 bucket
----------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The name of the bucket for your S3-compatible object          | - System Config path: **Environment > File Storage**                     |
| storage instance.                                             | - ``config.json`` setting: ``".FileSettings.AmazonS3Bucket",``           |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3BUCKET``               |
| A string with the S3-compatible bucket name.                  |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Amazon S3 path prefix
---------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Prefix you selected for your **Amazon S3 bucket** in AWS.     | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".FileSettings.AmazonS3PathPrefix",``       |
| A string containing the path prefix.                          | - Environment variable: ``MM_FILESETTINGS_AMAZONS3PATHPREFIX``           |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Amazon S3 region
----------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The AWS region you selected when creating your                | - System Config path: **Environment > File Storage**                     |
| **Amazon S3 bucket** in AWS.                                  | - ``config.json`` setting: ```".FileSettings.AmazonS3Region",``          |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3REGION``               |
| A string with the AWS region containing the bucket.           |                                                                          |
| If no region is set, Mattermost attempts to get the           |                                                                          |
| appropriate region from AWS, and sets it to **us-east-1**     |                                                                          |
| if none found.                                                |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: For MinIO or Digital Ocean Spaces, leave this setting empty.                                                                   |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Amazon S3 access key ID
-----------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| A string with the access key for the S3-compatible storage    | - System Config path: **Environment > File Storage**                     |
| instance. Your EC2 administrator can supply you with the      | - ``config.json`` setting: ``".FileSettings.AmazonS3AccessKeyId",``      |
| Access Key ID.                                                | - Environment variable: ``MM_FILESETTINGS_AMAZONS3ACCESSKEYID``          | 
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: This is required for access unless you are using an                                                                            |
| `Amazon S3 IAM Role <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html>`__ with       |
| Amazon S3.                                                                                                                               |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Amazon S3 endpoint
------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| The hostname of your S3-compatible instance.                  | - System Config path: **Environment > File Storage**                               |
|                                                               | - ``config.json`` setting: ``".FileSettings.AmazonS3Endpoint: s3.amazonaws.com",`` |
| A string with the hostname of the S3-compatible storage       | - Environment variable: ``MM_FILESETTINGS_AMAZONS3ENDPOINT``                       |
| instance. Defaults to **s3.amazonaws.com**.                   |                                                                                    |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| **Note**: For Digital Ocean Spaces, the hostname should be set to **<region>.digitaloceanspaces.com**, where **<region>** is the abbreviation      |
| for the region you selected when setting up the Space. It can be **nyc3**, **ams3**, or **sgp1**.                                                  |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+

Amazon S3 secret access key
---------------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The secret access key associated with your Amazon S3          | - System Config path: **Environment > File Storage**                     |
| Access Key ID.                                                | - ``config.json`` setting: ``".FileSettings.AmazonS3SecretAccessKey",``  |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SECRETACCESSKEY``      |
| A string with the secret access key for the S3-compatible     |                                                                          | 
| storage instance.                                             |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Enable secure Amazon S3 connections
-----------------------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Secure Amazon S3 connections can be disabled.                 | - System Config path: **Environment > File Storage**                     |
|                                                               | - ``config.json`` setting: ``".FileSettings.AmazonS3SSL: true",``        |
| - **true**: **(Default)** Enables only secure Amazon          | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SSL``                  |
|   S3 connections.                                             |                                                                          |
| - **false**: Allows insecure connections to Amazon S3.        |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Amazon S3 signature v2
----------------------

|all-plans| |self-hosted|

*Not available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| By default, Mattermost uses Signature v4 to sign API calls    | - System Config path: N/A                                                |              
| to AWS, but under some circumstances, v2 is required.         | - ``config.json`` setting: ``".FileSettings.AmazonS3SignV2: false",``    |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SIGNV2``               |
| - **true**: Use Signature v2 signing process.                 |                                                                          |
| - **false**: **(Default)** Use Signature v4 signing process.  |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| See the `AWS <https://docs.aws.amazon.com/general/latest/gr/signature-version-2.html>`__ documentation for information about when to     |
| use the Signature v2 signing process.                                                                                                    |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Enable server-side encryption for Amazon S3
-------------------------------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Enable server-side encryption for Amazon S3.                  | - System Config path: **Environment > File Storage**                     |
|                                                               | - ``config.json`` setting: ``".FileSettings.AmazonS3SSE: false",``       |
| - **true**: Encrypts files in Amazon S3 using server-side     | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SSE``                  |
|   encryption with Amazon S3-managed keys.                     |                                                                          |
| - **false**: **(Default)** Doesn’t encrypt files in           |                                                                          |
|   Amazon S3.                                                  |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Enable Amazon S3 debugging
--------------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Additional debugging information can be captured in           | - System Config path: **Environment > File Storage**                     |
| system logs.                                                  | - ``config.json`` setting: ``".FileSettings.AmazonS3Trace: false",``     |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3TRACE``                |
| - **true**:Log additional debugging information is logged     |                                                                          |
|   to the system logs.                                         |                                                                          |
| - **false**: **(Default)** No Amazon S3 debugging information |                                                                          |
|   is included in the system logs.Typically set to **false**   |                                                                          |
|   in production.                                              |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Select the **Test Connection** button in the System Console to validate the settings and ensure the user can access the server.          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Amazon S3 request timeout
-------------------------

|all-plans| |self-hosted|

*Not available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| Configure a timeout, in milliseconds, for requests to Amazon  | - System Config path: N/A                                                                 |
| S3.                                                           | - ``config.json`` setting: ``".FileSettings.AmazonS3RequestTimeoutMilliseconds: 30000",`` |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3REQUESTTIMEOUTMILLISECONDS``            |
| Numerical input. Default is 30000 milliseconds (30 seconds).  |                                                                                           |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------+

Initial font
-------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------------+
| Font used in auto-generated profile pictures with colored     | - System Config path: N/A                                                      |
| backgrounds and username initials.                            | - ``config.json`` setting: ``".FileSettings.InitialFont: nunito-bold.ttf",``   |
|                                                               | - Environment variable: ``MM_FILESETTINGS_INITIALFONT``                        |
| A string with the font file name. Default is                  |                                                                                |
| **nunito-bold.ttf**.                                          |                                                                                | 
+---------------------------------------------------------------+--------------------------------------------------------------------------------+