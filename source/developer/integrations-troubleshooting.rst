Integrations Troubleshooting
=====================================

Slash Commands
-----------------

 `Command with a trigger of 'trigger_word' returned an empty response`

Slack assumes default values for some fields if they are not specified by the integration. In this case, for slash commands Slack assumes the "response_type" is "ephemeral" while Mattermost does not. To fix this issue, try specifying the "response_type" and the slash command should now work in Mattermost. 
