.. _bot-accounts:

Bot Accounts
========================================

Use Bot Accounts to integrate with Mattermost through plugins or the `Mattermost RESTful API <https://api.mattermost.com>`_.

Bot accounts are just like user accounts, except they
  - Cannot be logged into
  - Cannot be used to create other bot accounts
  - Do not count as a registered user and therefore do not count towards the total users for an Enterprise Edition license


Use them instead of creating

Bot accounts are available to everyone on your server.

.. contents::
  :backlinks: top
  :depth: 1
  :local:



Overview with use cases

Screenshot

--

How to create one

---

Other miscellaneous

-- 

Unresolved tickets
https://mattermost.atlassian.net/browse/MM-15336
https://mattermost.atlassian.net/browse/MM-15545
https://mattermost.atlassian.net/browse/MM-15478
Next step on https://mattermost.atlassian.net/browse/MM-15037
CURL command to do a bot post: curl -i -X POST -H 'Content-Type: application/json' -d '{"channel_id":"3wbu8ue9g3fj7eobezpsqnamih", "message":"This is a message from a bot", "props":{"attachments": [{"pretext": "Look some text","text": "This is text"}]}}' -H 'Authorization: Bearer 669dydgnytbb9qcsbhuqz3imhe' https://botaccounts.test.spinmint.com/api/v4/posts
Plugins can take over a bot, or via the API
  Add to bot account FAQ, helpful when plugin is disabled or uninstalled
Do bot tokens expire?
Uber note about migrating all their integrations to use bot accounts

Reference to personal access token doc


