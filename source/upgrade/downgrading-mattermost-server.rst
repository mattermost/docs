Downgrade Mattermost Server
===========================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

In most cases you can downgrade Mattermost Server using the same steps as :doc:`upgrading-mattermost-server`. The binaries can be found in the :doc:`version-archive`. We do not recommend downgrading more than one version back from your current installation.

Downgrade Mattermost v6.0 to v5.38
-----------------------------------

Run the following set of queries, specific to your database, to downgrade the schema from v6.0 to v5.38.

.. important::

  The performance impact of a downgrade from v6.0 is similar to the v6.0 database migration. See the `Upgrading Mattermost Server </upgrade/upgrading-mattermost-server.html#preparing-to-upgrade-to-the-latest-version>`__ documentation for details.

.. code-block:: sh

  INSERT INTO Systems (Name,Value) VALUES ('Version','5.38.0') ON CONFLICT (name) DO UPDATE SET Value = '5.38.0';

  CREATE INDEX idx_status_status ON Status (Status);
  DROP INDEX idx_status_status_dndendtime;
  CREATE INDEX idx_channelmembers_user_id ON ChannelMembers (UserId);
  DROP INDEX idx_channelmembers_user_id_channel_id_last_viewed_at;
  DROP INDEX idx_channelmembers_channel_id_scheme_guest_user_id;
  CREATE INDEX idx_threads_channel_id ON Threads (ChannelId);
  DROP INDEX idx_threads_channel_id_last_reply_at;
  CREATE INDEX idx_channels_team_id ON Channels (TeamId);
  DROP INDEX idx_channels_team_id_type;
  DROP INDEX idx_channels_team_id_display_name;
  CREATE INDEX idx_posts_root_id ON Posts (RootId);
  DROP INDEX idx_posts_root_id_delete_at;

  ALTER TABLE CommandWebhooks ADD COLUMN ParentId varchar(26);
  UPDATE CommandWebhooks SET ParentId = '';
  ALTER TABLE Posts ADD COLUMN ParentId varchar(26);
  UPDATE Posts SET ParentId = '';

  ALTER TABLE users ALTER COLUMN timezone TYPE varchar(256);
  ALTER TABLE users ALTER COLUMN notifyprops TYPE varchar(2000);
  ALTER TABLE users ALTER COLUMN props TYPE varchar(4000);
  ALTER TABLE threads ALTER COLUMN participants TYPE text;
  ALTER TABLE sessions ALTER COLUMN props TYPE varchar(1000);
  ALTER TABLE posts ALTER COLUMN props TYPE varchar(8000);
  ALTER TABLE linkmetadata ALTER COLUMN data TYPE varchar(4096);
  ALTER TABLE jobs ALTER COLUMN data TYPE varchar(1024);
  ALTER TABLE channelmembers ALTER COLUMN notifyprops TYPE varchar(2000);

.. note:: 
        
  The inverse of `the final v6.0 upgrade query <https://gist.github.com/streamer45/59b3582118913d4fc5e8ff81ea78b055#postgresql-1>`__ is intentionally omitted from these downgrade queries because its result is backwards compatible, and running the query would unnecessarily delay the downgrade process.