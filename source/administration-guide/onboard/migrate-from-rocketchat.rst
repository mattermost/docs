Migrate from Rocket.Chat
========================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Overview
--------

Mattermost provides a migration path from Rocket.Chat, bringing your users, channels, messages, threads, direct messages, reactions, and file attachments into a self-hosted Mattermost environment.

Rocket.Chat has no hosted "export workspace" feature. Instead, you export the underlying MongoDB database with ``mongodump`` and transform that dump into a Mattermost bulk import file using the ``mmetl`` tool. This means the export step is a database operation that typically requires access to the Rocket.Chat server and its MongoDB instance.

The migration is a multi-step process:

1. `Preparations <#preparations>`__ — scope the migration, gather MongoDB and attachment-storage details, and prepare the Mattermost server.
2. `Export your Rocket.Chat data <#export-your-rocket-chat-data>`__ — produce a ``mongodump`` of the Rocket.Chat database.
3. `Transform the export <#transform-the-export-for-mattermost>`__ — validate with ``mmetl check rocketchat`` and convert with ``mmetl transform rocketchat``.
4. `Import into Mattermost <#import-into-mattermost>`__ — upload and process the archive with ``mmctl``.
5. Validate, test, and go live.

.. note::
  These instructions describe a *best effort* migration designed to preserve the majority of your messages, files, and channel structure. Manual adjustments are often required, and larger deployments should plan for multiple trial runs in a staging environment before a production import. Consider `talking to a Mattermost expert <https://mattermost.com/contact-sales/>`_ if your organization needs migration support.

1. Preparations
---------------

This guide assumes you already have a Mattermost server deployed and ready to accept your data. If not, review the :ref:`deployment documentation <deployment-guide/server/server-deployment-planning:deployment options>` first.

Scope definition
~~~~~~~~~~~~~~~~~

- **Data history**: Decide how much history you need. Because ``mongodump`` captures the whole database, scoping is done mainly through what you migrate and validate rather than by trimming the export.
- **Export size**: The size of your Rocket.Chat database and attachments directly affects processing and import time. Plan for longer iteration cycles on large deployments.
- **File attachments**: Consider excluding very large or non-critical attachments with ``--skip-attachments`` for early test runs to speed up iteration.

Rocket.Chat / MongoDB prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- You need access to the Rocket.Chat MongoDB instance and the ``mongodump`` tool from the `MongoDB Database Tools <https://www.mongodb.com/docs/database-tools/>`_.
- Identify the database name (commonly ``meteor``) and the connection URI.
- The transform reads these collections from the dump: ``users``, ``rocketchat_room``, ``rocketchat_message``, and ``rocketchat_subscription`` (all required), plus ``rocketchat_uploads`` and ``rocketchat_uploads.chunks`` (for attachments).

.. note::
  This tool was validated against **Rocket.Chat v8.5**. Rocket.Chat changes its MongoDB schema between versions, so exports from other versions may parse differently. If you hit unexpected parse errors, check for a newer ``mmetl`` release before assuming the export is at fault.

Attachment storage: GridFS vs. FileSystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rocket.Chat can store uploaded files in one of two ways. Confirm which your deployment uses (**Admin > Settings > File Upload > Storage Type**) before you export, because it changes how you run the transform:

- **GridFS** (stored inside MongoDB): attachments are captured directly in the ``mongodump`` (``rocketchat_uploads.chunks.bson``) and extracted automatically. No extra flag needed.
- **FileSystem** (stored on disk): the ``mongodump`` contains only file metadata. You must also copy the Rocket.Chat uploads directory and point ``--uploads-dir`` at it during the transform.

Infrastructure considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Test environment**: Always run the migration in a development or staging environment first. Most migrations require several iterations.
- **Operating system**: ``mmetl`` is supported on Linux and macOS. Windows (including WSL) is not recommended.
- **Storage requirements**: Ensure you have room for the ``mongodump`` output, the transformed import file, and the extracted attachments. Plan for several times the size of your Rocket.Chat data.
- **File storage**: Imports into AWS S3 (or S3-compatible storage) typically complete faster than local or NFS storage for large datasets.

Mattermost server considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Fresh server**: The most reliable imports happen on a fresh installation. If importing into an existing server, never import over an existing team, and back up the database and data directory first.
- **Server version**: Run the latest supported version of :doc:`Mattermost </product-overview/mattermost-server-releases>`.
- **The target team must already exist** in Mattermost, and **Allow any user with an account on this server to join this team** must be enabled for it.
- **Configuration settings**: Before importing, adjust:

  - ``TeamSettings.MaxChannelsPerTeam`` and ``TeamSettings.MaxUsersPerTeam``: set well above the number of channels/users you are migrating.
  - ``EmailSettings.EnableSignUpWithEmail`` and ``EmailSettings.EnableSignInWithEmail``: both ``true``.
  - ``FileSettings.MaxFileSize``: higher than the largest file in your export.
  - ``ElasticsearchSettings.EnableIndexing``, ``EnableSearching``, and ``EnableAutocomplete``: set to ``false`` during the import, then purge and reindex afterward.

2. Export your Rocket.Chat data
-------------------------------

Export the Rocket.Chat MongoDB database with ``mongodump``. Replace the URI and database name to match your deployment:

.. code-block:: sh

    mongodump --uri="mongodb://localhost:3001/meteor" --out=/tmp/rc-dump

This creates a subdirectory named after the database (for example ``/tmp/rc-dump/meteor``) containing the ``.bson`` files. That database subdirectory — not the parent — is what you pass to ``--dump-dir`` in the next step.

If your deployment uses **FileSystem** storage for attachments, also copy the Rocket.Chat uploads directory to a known location so you can reference it with ``--uploads-dir``.

3. Transform the export for Mattermost
--------------------------------------

`Download the latest release of mmetl <https://github.com/mattermost/mmetl/releases/>`__ for your OS and architecture. Run ``mmetl help`` to learn more about the tool.

Validate the export
~~~~~~~~~~~~~~~~~~~~~

Before transforming, check the integrity of the dump:

.. code-block:: sh

    ./mmetl check rocketchat --dump-dir /tmp/rc-dump/meteor

This reports structural issues (for example, missing required collections or invalid records) that would cause the transform or import to fail. Details are written to ``check-rocketchat.log``.

Run the transform
~~~~~~~~~~~~~~~~~~

Convert the dump into a Mattermost bulk import file. Replace ``<TEAM-NAME>`` with your Mattermost team name, which must be one word and lowercase (a team named ``My Team`` becomes ``my-team``):

.. code-block:: sh

    ./mmetl transform rocketchat --team <TEAM-NAME> --dump-dir /tmp/rc-dump/meteor --output mattermost_import.jsonl

For **FileSystem** attachment storage, add ``--uploads-dir``:

.. code-block:: sh

    ./mmetl transform rocketchat --team <TEAM-NAME> --dump-dir /tmp/rc-dump/meteor --uploads-dir /path/to/rocketchat/uploads --output mattermost_import.jsonl

The tool produces a `.jsonl <https://jsonlines.org/examples>`__ file containing your users, channels, and posts, plus a ``data`` folder containing the extracted attachments.

A successful run ends with a summary line in ``transform-rocketchat.log`` like:

.. code-block:: text

    Transformation succeeded! Users: 152, Public channels: 48, Private channels: 12, Posts: 39184

If the run stops with an error instead — for example, ``the RocketChat export contains bot users but --bot-owner was not specified`` — no valid import file is produced. Resolve the error (see the flags below) and re-run.

.. tip::
  **Iterate incrementally.** Run a small trial first: transform, import into a throwaway team, and confirm a few channels look right before committing to a full production import. Because ``mmctl import`` is idempotent, re-running an import with the same data will not create duplicate posts — so repeated trial runs are safe.

Useful transform flags
~~~~~~~~~~~~~~~~~~~~~~~~

- ``--uploads-dir <PATH>``: Path to the Rocket.Chat FileSystem uploads directory. Required when attachments are not stored in GridFS.
- ``--bot-owner <USERNAME>``: Username of the Mattermost user who will own all imported bots. **Required if the export contains any bot users** — the transform errors out otherwise.
- ``--skip-attachments`` / ``-a``: Skip extracting file attachments. Useful for faster iteration while testing.
- ``--attachments-dir <PATH>``: Directory for extracted attachments (default ``data``).
- ``--default-email-domain <DOMAIN>``: When a user's email is missing, generate one from their username and this domain (for example ``example.com``).
- ``--skip-empty-emails``: Allow users with empty emails. Note that this produces invalid import data that must be corrected before importing.
- ``--debug``: Emit ``DEBUG``-level detail to ``transform-rocketchat.log`` to help diagnose slow or failing runs.

4. Import into Mattermost
-------------------------

Package the ``.jsonl`` file and ``data`` folder into a single zip:

.. code-block:: sh

  zip -r mattermost-bulk-import.zip data mattermost_import.jsonl

Validate the archive locally before uploading:

.. code-block:: sh

  mmctl import validate ./mattermost-bulk-import.zip

Ensure ``mmctl`` is installed and :ref:`authenticated <administration-guide/manage/mmctl-command-line-tool:mmctl auth>`. Then choose an upload method.

Standard upload
~~~~~~~~~~~~~~~

For most imports, upload through ``mmctl``:

.. code-block:: sh

  mmctl import upload ./mattermost-bulk-import.zip
  mmctl import list available

Process the import using the name returned by ``import list available``:

.. code-block:: sh

  mmctl import process <IMPORT FILE NAME>

Check the job status. If it shows ``pending``, wait and re-run. The ``--json`` flag is required to see error messages:

.. code-block:: sh

  mmctl import job show <JOB ID> --json

Large imports (file store method)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For large archives (multiple GB), uploading through ``mmctl`` is slow and error-prone. Instead, place the archive directly into the server's import directory and let the server process it in place:

1. Copy ``mattermost-bulk-import.zip`` (with a unique name) into ``data/import`` in the Mattermost file store — the local data directory, or the ``import`` prefix of your S3 bucket.
2. Run ``mmctl import list available`` to confirm the server sees the file.
3. Run ``mmctl import process <IMPORT FILE NAME>`` and monitor with ``mmctl import job show <JOB ID> --json``.

This avoids re-uploading gigabytes through the API and is the recommended path for large migrations.

Fixing unread channels and threads
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After importing, messages may appear unread for all users. Run the following against the Mattermost database to resolve it:

.. code-block:: sql

   begin;
   UPDATE channelmembers
   SET
       msgcount = channels.totalmsgcount,
       lastupdateat = channels.lastpostat,
       lastviewedat = channels.lastpostat,
       msgcountroot = channels.totalmsgcountroot
   FROM channels
   WHERE channelmembers.channelid = channels.id;

   INSERT INTO preferences (UserId, Category, Name, Value)
   SELECT
       cm.userid,
       'channel_approximate_view_time',
       cm.channelid,
       cm.lastupdateat
   FROM
       channelmembers cm
   ON CONFLICT (userid, category, name)
   DO UPDATE SET
       Value = EXCLUDED.Value;

   update preferences set value = false where category = 'direct_channel_show';
   update preferences set value = false where category = 'group_channel_show';

   commit;

Placeholder emails and account activation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost accounts are created from the emails and usernames in the export. Where an email is missing, a placeholder (for example ``username@local``) is generated and must be corrected by a system administrator. Search the final ``.jsonl`` file for placeholder emails before importing.

Users activate their accounts through Mattermost's **Password Reset** screen using their email address:

- **Imports performed by a system administrator**: emails are automatically verified, and users can reset their password immediately.
- **Imports performed by a non-administrator**: users must verify their email address before resetting their password.

See how to :ref:`migrate user authentication to LDAP or SAML <administration-guide/manage/mmctl-command-line-tool:mmctl user migrate-auth>` if you use SSO.

What migrates and what doesn't
------------------------------

For core collaboration data — posts, threads, reactions, attachments, users, and channels — you can expect high fidelity. Integrations and Rocket.Chat-specific features do not carry over.

.. list-table::
   :header-rows: 1
   :widths: 30 15 55

   * - Content type
     - Migrates?
     - Notes
   * - Posts and threads
     - Yes
     - Rocket.Chat threads become Mattermost threaded replies. Oversized posts are split into continuation replies rather than truncated.
   * - Public channels
     - Yes
     - Display name, purpose (description), and header (topic) are preserved.
   * - Private channels
     - Yes
     -
   * - Discussions
     - Yes (converted)
     - Rocket.Chat discussions are converted to standalone Mattermost channels (public or private, matching the discussion's visibility). The parent-child relationship is not preserved.
   * - 1:1 direct messages
     - Yes
     - Map directly. Self-DMs are preserved as a direct channel with yourself.
   * - Group DMs (3–8 members)
     - Yes (converted)
     - Become Mattermost **Group Messages** — functionally equivalent, different terminology.
   * - Group DMs (over 8 members)
     - Converted
     - Mattermost group messages support at most 8 members, so larger group DMs are converted to **private channels**.
   * - Reactions
     - Yes
     - Emoji skin-tone modifiers are stripped to a default rendering. Custom emoji require matching names (see below).
   * - File attachments
     - Yes
     - From GridFS or FileSystem storage. Auto-generated thumbnails are skipped to avoid duplicates.
   * - Users
     - Yes
     - Inactive Rocket.Chat users are imported as deactivated accounts.
   * - Bots
     - Yes
     - Reassigned to the ``--bot-owner`` user.
   * - Channel mentions
     - Best effort
     - ``#channel`` references are translated to Mattermost ``~channel`` links where the channel exists.
   * - Join / leave / add / remove events
     - Yes
     - Converted to Mattermost system messages.
   * - Custom emoji images
     - No
     - Reaction *names* are preserved, but the emoji images are not imported (see below).
   * - Guest users
     - Yes
     - Rocket.Chat guest accounts are imported as Mattermost :doc:`guest users </administration-guide/onboard/guest-accounts>`. Ensure :ref:`guest access <administration-guide/configure/authentication-configuration-settings:guest access>` is enabled on the target server before importing, otherwise these accounts fail to import.
   * - Encrypted (E2E) channels
     - No
     - End-to-end encrypted rooms are skipped entirely, including their messages.
   * - Apps, integrations, slash commands, webhooks
     - No
     - Recreate using Mattermost :doc:`integrations </integrations-guide/integrations-guide-index>`.
   * - Avatars, user status, custom profile fields
     - No
     - Users update their profiles in Mattermost after import.
   * - Pinned/starred messages, topic-change and mute events
     - No
     - These Rocket.Chat-specific records are not migrated.

Custom emoji
~~~~~~~~~~~~

Custom emoji images are **not** imported with your messages — only the emoji *names* used in reactions are preserved. A reaction is stored as text (``:emoji-name:``) and resolved at render time:

- If a custom emoji with the same name exists in Mattermost, the reaction renders correctly.
- If not, it shows as a placeholder until the emoji is added.

Because resolution happens at render time, you can add custom emoji to Mattermost **at any time** — before or after the import — and reactions on historical messages will render once a matching name exists. Names must match exactly.

FAQ
---

**Do I need to create users before importing?**
No. ``mmetl`` and the import process handle user creation and ordering automatically.

**What happens if I run the same import twice?**
Nothing harmful. ``mmctl import`` is idempotent — duplicate posts are not created — so incremental and repeated trial imports are safe.

**Where do all my channels and DMs go?**
Into the single team you specify with ``--team``. Rocket.Chat has no multi-workspace concept, so there is no team-mapping step.

**How are attachments stored, and why do I need ``--uploads-dir``?**
Rocket.Chat stores files either in MongoDB (GridFS) or on disk (FileSystem). GridFS files are captured in the ``mongodump`` automatically; FileSystem files are not, so you point ``--uploads-dir`` at the uploads directory. See `Attachment storage <#attachment-storage-gridfs-vs-filesystem>`__.

**Why are some channels missing after import?**
End-to-end encrypted rooms are skipped and their messages are not migrated. Check ``transform-rocketchat.log`` for skipped rooms.

**Do I need to import custom emoji before messages?**
No. Emoji resolve at render time, so you can add them whenever.

**How do I handle a very large import?**
Use the file store method — copy the archive directly into the server's ``data/import`` directory rather than uploading through ``mmctl``. See `Large imports <#large-imports-file-store-method>`__.

**I hit a parse error. Is my export broken?**
Possibly not. Rocket.Chat changes its MongoDB schema between versions (this tool was validated against v8.5). Run ``mmetl check rocketchat`` first, and check for a newer ``mmetl`` release before assuming the data is at fault.
