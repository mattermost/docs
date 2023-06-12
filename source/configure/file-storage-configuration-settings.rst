:orphan:
:nosearch:

Configure file storage settings by going to **System Console > Environment > File Storage**, or by editing the ``config.json`` file as described in the following tables.

.. note::

  Mattermost currently supports storing files on the local filesystem and Amazon S3 or S3-compatible containers. We have tested Mattermost with `MinIO <https://min.io/>`__ and `Digital Ocean Spaces <https://docs.digitalocean.com/products/spaces/>`__ products, but not all S3-compatible containers on the market. If you are looking to use other S3-compatible containers, we recommend completing your own testing.

.. config:setting:: file-storagesystem
  :displayname: File storage system (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.DriverName
  :environment: MM_FILESETTINGS_DRIVERNAME
  :description: The type of file storage system used.

  - **local**: **(Default)** Files and images are stored in the specified local file directory.
  - **amazons3**: Files and images are stored on Amazon S3 based on the access key, bucket, and region fields provided.

File storage system
~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The type of file storage system used.                         | - System Config path: **Environment > File Storage**                     |
| Can be either Local File System or Amazon S3.                 | - ``config.json`` setting: ``".FileSettings.DriverName:  local”,``       |
|                                                               | - Environment variable: ``MM_FILESETTINGS_DRIVERNAME``                   |
| - **local**: **(Default)** Files and images are stored in     |                                                                          |
|   the specified local file directory.                         |                                                                          |
| - **amazons3**: Files and images are stored on Amazon S3      |                                                                          |
|   based on the access key, bucket, and region fields          |                                                                          |
|   provided. The driver is compatible with MinIO (beta)        |                                                                          |
|   and Digital Ocean Spaces.                                   |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-localstoragedirectory
  :displayname: Local storage directory (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.Directory
  :environment: MM_FILESETTINGS_DIRECTORY
  :description: The local directory to which files are written when the **File storage system** is set to **local**. Default value is **./data/**.

Local storage directory
~~~~~~~~~~~~~~~~~~~~~~~

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

.. config:setting:: file-maxfilesize
  :displayname: Maximum file size (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.MaxFileSize
  :environment: MM_FILESETTINGS_MAXFILESIZE
  :description: The maximum file size, in bytes, for message attachments. Default value is **104857600** bytes (1 megabyte).

Maximum file size
~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The maximum file size for message attachments.                | - System Config path: **Environment > File Storage**                     |
| This value must be specified in megabytes in the              | - ``config.json`` setting: ``".FileSettings.MaxFileSize: 104857600",``   |
| System Console, and in bytes in the ``config.json`` file.     | - Environment variable: ``MM_FILESETTINGS_MAXFILESIZE``                  |
|                                                               |                                                                          |
| The default is ``104857600`` bytes (**1** megabyte).          |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Warning**: Verify server memory can support your setting choice. Large file sizes increase the risk of server crashes and failed       |
| uploads due to network disruptions.                                                                                                      |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: If you use a proxy or load balancer in front of Mattermost, the following proxy settings must be adjusted accordingly:         |
|                                                                                                                                          |
| - For NGINX, use ``client_max_body_size``.                                                                                               |
| - For Apache use ``LimitRequestBody``.                                                                                                   |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-enabledocsearchbycontent
  :displayname: Enable document search by content (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.ExtractContent
  :environment: MM_FILESETTINGS_EXTRACTCONTENT
  :description: Enable users to search the contents of documents attached to messages.

  - **true**: **(Default)** Documents are searchable by their content.
  - **false**: Documents aren’t searchable by their content.

Enable document search by content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
| extraction command is executed using the `CLI </manage/command-line-tools.html#mattermost-extract-documents-content>`__                             |
| or the `mmctl </manage/mmctl-command-line-tool.html?highlight=mmctl#mmctl-extract>`__. If this command is not run,                                  |
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

.. config:setting:: file-enabledocsearchwithinzipfile
  :displayname: Enable searching content of documents within ZIP files (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.ArchiveRecursion
  :environment: MM_FILESETTINGS_ARCHIVERECURSION
  :description: Enables users to search the contents of compressed ZIP files attached to messages.

  - **true**: Contents of documents within ZIP files are returned in search results.
  - **false**: **(Default)** The contents of documents within ZIP files aren’t returned in search results.

Enable searching content of documents within ZIP files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Enables users to search the contents of compressed ZIP files  | - System Config path: **Environment > File Storage**                                   |
| attached to messages.                                         | - ``config.json`` setting: ``".FileSettings.ArchiveRecursion: false",``                |
|                                                               | - Environment variable: ``MM_FILESETTINGS_ARCHIVERECURSION``                           |
| - **true**: Contents of documents within ZIP files are        |                                                                                        |
|   returned in search results. This may have an impact on      |                                                                                        |
|   server performance for large files.                         |                                                                                        |
|   the specified local file directory.                         |                                                                                        |
| - **false**: **(Default)** The contents of documents within   |                                                                                        |
|   ZIP files aren’t returned in search results.                |                                                                                        |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| **Note**: Document content search within ZIP files is available, with mobile support coming soon.                                                      |
| Searching document contents adds load to your server. For large deployments, or teams that share many large, text-heavy documents,                     |
| we recommend you review our `hardware requirements </install/software-hardware-requirements.html#hardware-requirements>`__,                            |
| and test enabling this feature in a staging environment before enabling it in a production environment.                                                |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. config:setting:: file-s3bucket
  :displayname: Amazon S3 bucket (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3Bucket
  :environment: MM_FILESETTINGS_AMAZONS3BUCKET
  :description: The name of the bucket for your S3-compatible object storage instance.

Amazon S3 bucket
~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The name of the bucket for your S3-compatible object          | - System Config path: **Environment > File Storage**                     |
| storage instance.                                             | - ``config.json`` setting: ``".FileSettings.AmazonS3Bucket",``           |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3BUCKET``               |
| A string with the S3-compatible bucket name.                  |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-s3pathprefix
  :displayname: Amazon S3 path prefix (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.AmazonS3PathPrefix
  :environment: MM_FILESETTINGS_AMAZONS3PATHPREFIX
  :description: The prefix you selected for your **Amazon S3 bucket** in AWS.

Amazon S3 path prefix
~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The prefix you selected for your **Amazon S3 bucket** in AWS. | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".FileSettings.AmazonS3PathPrefix",``       |
| A string containing the path prefix.                          | - Environment variable: ``MM_FILESETTINGS_AMAZONS3PATHPREFIX``           |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-s3region
  :displayname: Amazon S3 region (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3Region
  :environment: MM_FILESETTINGS_AMAZONS3REGION
  :description: The AWS region you selected when creating your **Amazon S3 bucket** in AWS. For MinIO or Digital Ocean Spaces, leave this setting empty.

Amazon S3 region
~~~~~~~~~~~~~~~~

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

.. config:setting:: file-s3accesskeyid
  :displayname: Amazon S3 access key ID (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3AccessKeyId
  :environment: MM_FILESETTINGS_AMAZONS3ACCESSKEYID
  :description: A string with the access key for the S3-compatible storage instance.

Amazon S3 access key ID
~~~~~~~~~~~~~~~~~~~~~~~

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

.. config:setting:: file-s3endpoint
  :displayname: Amazon S3 endpoint (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3Endpoint
  :environment: MM_FILESETTINGS_AMAZONS3ENDPOINT
  :description: The hostname of your S3-compatible instance. Default value is **s3.amazonaws.com**.

Amazon S3 endpoint
~~~~~~~~~~~~~~~~~~

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

.. config:setting:: file-s3secretaccesskey
  :displayname: Amazon S3 secret access key (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3SecretAccessKey
  :environment: MM_FILESETTINGS_AMAZONS3SECRETACCESSKEY
  :description: The secret access key associated with your Amazon S3 Access Key ID.

Amazon S3 secret access key
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The secret access key associated with your Amazon S3          | - System Config path: **Environment > File Storage**                     |
| Access Key ID.                                                | - ``config.json`` setting: ``".FileSettings.AmazonS3SecretAccessKey",``  |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SECRETACCESSKEY``      |
| A string with the secret access key for the S3-compatible     |                                                                          |
| storage instance.                                             |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-s3secureconnection
  :displayname: Enable secure Amazon S3 connections (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3SSL
  :environment: MM_FILESETTINGS_AMAZONS3SSL
  :description: Enable or disable secure Amazon S3 connections. Default value is **true**.

Enable secure Amazon S3 connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Enable or disable secure Amazon S3 connections.               | - System Config path: **Environment > File Storage**                     |
|                                                               | - ``config.json`` setting: ``".FileSettings.AmazonS3SSL: true",``        |
| - **true**: **(Default)** Enables only secure Amazon          | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SSL``                  |
|   S3 connections.                                             |                                                                          |
| - **false**: Allows insecure connections to Amazon S3.        |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-s3signv2
  :displayname: Amazon S3 signature v2 (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.AmazonS3SignV2
  :environment: MM_FILESETTINGS_AMAZONS3SIGNV2

  - **true**: Use Signature v2 signing process.
  - **false**: **(Default)** Use Signature v4 signing process.

Amazon S3 signature v2
~~~~~~~~~~~~~~~~~~~~~~

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

.. config:setting:: file-s3sse
  :displayname: Enable server-side encryption for Amazon S3 (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3SSE
  :environment: MM_FILESETTINGS_AMAZONS3SSE

  - **true**: Encrypts files in Amazon S3 using server-side encryption with Amazon S3-managed keys.
  - **false**: **(Default)** Doesn’t encrypt files in Amazon S3.

Enable server-side encryption for Amazon S3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Enable server-side encryption for Amazon S3.                  | - System Config path: **Environment > File Storage**                     |
|                                                               | - ``config.json`` setting: ``".FileSettings.AmazonS3SSE: false",``       |
| - **true**: Encrypts files in Amazon S3 using server-side     | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SSE``                  |
|   encryption with Amazon S3-managed keys.                     |                                                                          |
| - **false**: **(Default)** Doesn’t encrypt files in           |                                                                          |
|   Amazon S3.                                                  |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-s3trace
  :displayname: Enable Amazon S3 debugging (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3Trace
  :environment: MM_FILESETTINGS_AMAZONS3TRACE

  - **true**: Log additional debugging information is logged to the system logs.
  - **false**: **(Default)** No Amazon S3 debugging information is included in the system logs.

Enable Amazon S3 debugging
~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Enable or disable Amazon S3 debugging to capture additional   | - System Config path: **Environment > File Storage**                     |
| debugging information in system logs                          | - ``config.json`` setting: ``".FileSettings.AmazonS3Trace: false",``     |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3TRACE``                |
| - **true**: Log additional debugging information is logged    |                                                                          |
|   to the system logs.                                         |                                                                          |
| - **false**: **(Default)** No Amazon S3 debugging information |                                                                          |
|   is included in the system logs. Typically set to **false**  |                                                                          |
|   in production.                                              |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Select the **Test Connection** button in the System Console to validate the settings and ensure the user can access the server.          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-initialfont
  :displayname: Initial font (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.InitialFont
  :environment: MM_FILESETTINGS_INITIALFONT
  :description: The font used in auto-generated profile pictures with colored backgrounds and username initials. Default value is **nunito-bold.ttf**.

Initial Font
~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------------+
| The font used in auto-generated profile pictures with colored | - System Config path: N/A                                                      |
| backgrounds and username initials.                            | - ``config.json`` setting: ``".FileSettings.InitialFont: nunito-bold.ttf",``   |
|                                                               | - Environment variable: ``MM_FILESETTINGS_INITIALFONT``                        |
| A string with the font file name. Default is                  |                                                                                |
| **nunito-bold.ttf**.                                          |                                                                                |
+---------------------------------------------------------------+--------------------------------------------------------------------------------+
