Incident Response Application (EE, Closed Alpha)
------------------------------------------------------

The incident response application is available in closed Alpha, in `Enterprise Edition <https://mattermost.com/pricing/>`_.

// TODO: Add a screenshot or a video

Sample use cases you can accomplish with this app include the following:

1. Trigger automated incident response workflows based on keywords.
2. Automatically mention your InfoSec or DevSecOps teams when an incident occurs, including via email, mobile push and desktop notifications.
3. Auto-create "war rooms" and inviting key team members to immediately collaborate on a critical incident.
4. Take quick actions, review data and access relevant links all in one place.
5. Archive resolved incidents to declutter your channel sidebar without losing access to past information.
6. Pull summary statistics of the incident response workflow, including mean-time-to-acknowledgment (MTTA) and mean-time-to-resolution (MTTR).

To shape the direction of the incident response application, `sign up to our Alpha program here <https://docs.google.com/forms/d/e/1FAIpQLSf4Rr1YnofQQnKHJuL0Cgz_DaCUitt_Atik7K9KXsDefCyXlg/viewform>`_!

// TODO: Add another screenshot

.. contents:: Contents
  :backlinks: top
  :local:
  :depth: 1

How Can I Try The App?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. `Sign up for the closed Alpha program <https://docs.google.com/forms/d/e/1FAIpQLSf4Rr1YnofQQnKHJuL0Cgz_DaCUitt_Atik7K9KXsDefCyXlg/viewform>`_. If you're selected to join the Alpha program, you will receive an email from us with a plugin binary.

2. Upload the plugin binary in **System Console > Plugins > Plugin Management** `following these steps <https://about.mattermost.com/default-plugin-uploads>`_.

3. Enable the plugin from the **Installed Plugins** list.

4. Use `one of these sample app workflows <// TODO Add a link>`_ to try the app. To upload these workflows to your instance:

 - save the app workflow schema to a JSON file
 - go to any Mattermost channel and post ``/workflow edit`` to open the workflow editor
 - click **Choose .json file** and select the JSON file containing the app workflow schema
 - click **Upload**

5. Post the trigger word defined in the workflow schmea to start the workflow!

See the documentation below to get help on how to configure and manage your app workflows, or open an issue at https://forum.mattermost.org and we'd be happy to help you.

Incident Response App Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The app is configured through a JSON file, which you can upload as a System Administrator via ``/workflow edit``. We highly recommend using a text editor file that automatically validates syntax errors of your JSON file.

The JSON file looks something as follows.

  .. code-block:: json

    [
      {
        "name": "security_issue",
        "triggers": [
          {
            "name": "issuereported",
            "type": "text",
            "match": "#sec"
          }
        ],
        "steps": [
          {
            "name": "Setup",
            "start_actions": [
              {
                "name": "CreateWarroom",
                "type": "create_channel",
                "channel_name": "security-issue-{{.Instance.Number}}",
                "channel_displayname": "Security Issue {{.Instance.Number}}"
              },
              ...
              {
                "type": "transition_to",
                "name": "TransitionToTriage",
                "to": "Triage"
              }
            ]
          },
          ...
          {
            "name": "Resolved",
            "start_actions": [
              {
                "name": "ResolveWarroom",
                "type": "post",
                "channel_name": "{{.Action.CreateWarroom.ChannelName}}",
                "message": "Resolved."
              },
              ...
              {
                "name": "finished",
                "type": "finished_workflow"
              }
            ]
          }
        ]
      }
    ]

There are four components to an incident app workflow schema: triggers, steps, actions and transitions. Each one is explained in more detail below.

Trigger
^^^^^^^^^^^^^^^

A trigger is a condition on which a workflow can be started.

.. csv-table::
    :header: "Field", "Description", "Type", "Required"

    "name", "The name of the trigger", "string", "Yes. This field must be unique."
    "type", "The type of trigger. This refers to the internal name of the trigger being configured", "string, "Yes"
    "*additional fields", "Additional fields based on the type of trigger. See below for more details.", "string", "Yes"

Text Trigger (type: ``text``)
*******************************

An incident can be created when a text trigger is seen. The specified message then becomes the description of the incident.

For example, you can specify "#s1critical" as the text trigger and any post that contains this keyword is treated as an incident and starts the workflow.

.. csv-table::
    :header: "Field", "Description", "Type", "Required"

    "channel", "The channel(s) to look for the trigger. If none specified, all channels will be watched.", "[]string", "No"
    "team", "The team(s) to watch for the trigger in. If none specified, all teams will be watched.", "[]string, "No"
    "match", "The text string to match on", "string", "If ``match_regex`` not set, yes"
    "match_regex", "The regex to match on", "string", "If ``match`` not set, yes"

// TODO Verify JSON schema and add an example here.

Step
^^^^^^^^^^^^^^^

A step is the representation of a state the app workflow can be in. For now it contains a set of actions to be performed when it is started and when it is finished.

.. csv-table::
    :header: "Field", "Description", "Type", "Required"

    "name", "The name of the step", "string", "Yes. This field must be unique."
    "start_actions", "Actions to perform when the step is reached.", "[]Action", "If ``finished_actions`` not set, yes"
    "finished_actions", "Actions to perform when the step is finished.", "[]Action", "If ``start_actions`` not set, yes"

Action
^^^^^^^^^^^^^^^

Actions are performed when steps are started and finished.

.. csv-table::
    :header: "Field", "Description", "Type", "Required"

    "name", "The name of the action", "string", "Yes. This field must be unique."
    "type", "The type of action to perform", "string", "Yes"
    "*additional fields", "Additional fields based on the type of action. See below for more details.", "string", "Yes"

Create Channel (type: ``create_channel``)
*******************************************

The create channel action creates a channel with the given parameters. The users listed will be automatically invited.

.. csv-table::
    :header: "Field", "Description", "Type", "Required"

    "channel", "A channel object supporting fields from model.Channel", "model.Channel", "Yes"

// TODO Verify JSON schema and add an example here. Example should include the supported fields of the channel model, e.g. type, team, ...

Add Users to Channel (type: ``add_users_channel``)
**************************************************************

The add users to channel action adds the specified users to the channel.

.. csv-table::
    :header: "Field", "Description", "Type", "Required"

    "channel_name", "The channel to create the post in. Can be name or ID.", "model.Channel", "Yes"
    "users", "Users to add to the channel after creation. Can be usernames, user IDs or AD/LDAP group names.", "[]string, "Yes"

// TODO Verify JSON schema and add an example here.

Create Post (type: ``post``)
*******************************

Creates a post in the specified channel.

.. csv-table::
    :header: "Field", "Description", "Type", "Required"

    "channel_name", "The channel to create the post in. Can be name or ID.", "string", "Yes"
    "message", "The contents of the message.", "string", "Yes"
    "fields", "A list of fields to show in the message. ", "[]Field", "No"
    "transition_button", "A label and a step to transition to when pressed.", "[]Button", "No"

// TODO Verify JSON schema and add an example here. Example should include fields and transition_button.

Archive Channel (type: ``archive_channel``)
**********************************************

Archives the specified channel.

.. csv-table::
    :header: "Field", "Description", "Type", "Required"

    "channel_name", "The channel to archive. Can be name or ID.", "string", "Yes"

// TODO Verify JSON schema and add an example here.

Transition to Another Step (type: ``transition_to``)
******************************************************

Specified which step to transition the workflow to. // TODO Add a more clear description

.. csv-table::
    :header: "Field", "Description", "Type", "Required"

    "to", "The name of the target step to transition to", "string", "Yes"

// TODO Verify JSON schema and add an example here.

Statistics
^^^^^^^^^^^^^^^

The incident response application also enables you to pull summary statistics, including mean-time-to-acknowledgment (MTTA) and mean-time-to-resolution (MTTR).

To pull a sample report, use ``/workflow stats`` in any Mattermost channel:

// TODO Add a screenshot - e.g. either re-use this screenshot or produce a new one: https://user-images.githubusercontent.com/1490756/65821266-4ad79d80-e201-11e9-8930-7beaa3dd0ed9.png

You may also reset statistics at any time via ``/workflow reset-stats.

Note that you must be a System Administrator to execute these commands.

Sample Schema
~~~~~~~~~~~~~~~~~~~~~~~~

Below is a full sample schema with a text trigger, four steps and multiple actions including transitions.

For other sample schemas, `see here <// TODO Add other samples in https://github.com/mattermost/docs/tree/master/source/samples and link them here. See MM-18870>`_.

  .. code-block:: json

    [
      {
        "name": "security_issue",
        "triggers": [
          {
            "name": "issuereported",
            "type": "text",
            "match": "#sec"
          }
        ],
        "steps": [
          {
            "name": "Setup",
            "start_actions": [
              {
                "name": "CreateWarroom",
                "type": "create_channel",
                "channel_name": "security-issue-{{.Instance.Number}}",
                "channel_displayname": "Security Issue {{.Instance.Number}}"
              },
              {
                "name": "AddUsers",
                "type": "add_users_channel",
                "channel_name": "{{.Action.CreateWarroom.ChannelName}}",
                "users": [
                  "jon",
                  "chris"
                ]
              },
              {
                "type": "post",
                "name": "attention_post",
                "channel_name": "Town Square",
                "message": "Security issue reported. War room created: ~{{.Action.CreateWarroom.ChannelName}}"
              },
              {
                "type": "transition_to",
                "name": "TransitionToTriage",
                "to": "Triage"
              }
            ]
          },
          {
            "name": "Triage",
            "start_actions": [
              {
                "name": "TriagePost",
                "type": "post",
                "channel_name": "{{.Action.CreateWarroom.ChannelName}}",
                "message": "New issue to triage:\n ```{{.Trigger.Message}}```",
                "fields": [
                  {
                    "name": "Alert",
                    "type": "button",
                    "description": "Alert the Sysadmin to take immediate action"
                  },
                  {
                    "name": "Likelihood",
                    "description": "How likely the security issue is to be exploited.",
                    "type": "options",
                    "options": [
                      "L1",
                      "L2",
                      "L3"
                    ]
                  },
                  {
                    "name": "Impact",
                    "type": "options",
                    "description": "The impact of the security issue if exploited",
                    "options": [
                      "I1",
                      "I2",
                      "I3"
                    ]
                  },
                  {
                    "name": "Severity",
                    "type": "options",
                    "description": "Derived from Impact and Likelihood",
                    "options": [
                      "S1",
                      "S2",
                      "S3"
                    ]
                  }
                ],
                "transition_button": [
                  {
                    "label": "Triaged",
                    "description": "Move to developing a fix",
                    "to": "DevelopFix"
                  },
                  {
                    "label": "Resolved",
                    "description": "Close issue as resolved",
                    "to": "Resolved"
                  }
                ]
              }
            ],
            "finish_actions": [
              {
                "name": "TriageConfirmation",
                "type": "post",
                "channel_name": "{{.Action.CreateWarroom.ChannelName}}",
                "message": "Finished Triage"
              }
            ]
          },
          {
            "name": "DevelopFix",
            "start_actions": [
              {
                "name": "InfoPost",
                "type": "post",
                "channel_name": "{{.Action.CreateWarroom.ChannelName}}",
                "message": "Developing a fix underway. Issue information:\n\nLikelihood: {{.Action.TriagePost.Likelihood}}\nImpact: {{.Action.TriagePost.Impact}}\nSeverity: {{.Action.TriagePost.Severity}}",
                "transition_button": [
                  {
                    "label": "Triage",
                    "description": "Return to triage.",
                    "to": "Triage"
                  },
                  {
                    "label": "Resolved",
                    "description": "Close issue as resolved",
                    "to": "Resolved"
                  }
                ]
              }
            ]
          },
          {
            "name": "Resolved",
            "start_actions": [
              {
                "name": "ResolveWarroom",
                "type": "post",
                "channel_name": "{{.Action.CreateWarroom.ChannelName}}",
                "message": "Resolved."
              },
              {
                "name": "PostResolved",
                "type": "post",
                "channel_name": "town-square",
                "message": "Resolved Security Issue {{.Instance.Number}}"
              },
              {
                "name": "ArchiveSecurityChannel",
                "type": "archive_channel",
                "channel_name": "security-issue-{{.Instance.Number}}"
              },
              {
                "name": "finished",
                "type": "finished_workflow"
              }
            ]
          }
        ]
      }
    ]

Permissions and Management of the App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only System Administrators can edit the incident response app by uploading a JSON file via the ``/workflow edit`` command. This allows System Administrators to have full control over what app workflows are configured in a Mattermost server.

Later, permissions to allow other users to edit app workflows may be supported.

Roadmap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following are some of the use cases we plan to support in a future Beta or stable release:

1. Pulling remote data to, for instance, look up responders who are on duty from an external system or from AD/LDAP, and notifying them about a new incident.
2. Creating and managing workflows through the user interface instead of a JSON schema file.
3. Supporting branching and IF conditions for more complex incident management workflows.
4. Exporting all actions and conversations into a PDF for post-mortem and root cause analysis.
5. Richer analytics for measuring the effectiveness of incident response processes.
6. Deeper integrations with existing monitoring and ticketing systems for streamlined incident response management.

If you have any feedback on the incident response application, let us know at https://forum.mattermost.org.

Troubleshooting
~~~~~~~~~~~~~~~~~~

Below are common error messages and how to resolve them.

Always review your Mattermost server logs in **System Console > Server Logs** for errors with the keyword ``workflow`` for more details. If you need any help with configuring the app, let us know at https://forum.mattermost.org and we'd be happy to assist you.

``Error parsing workflow: workflow name must not be blank``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The app workflow name is empty. Please specify a name for the app workflow and try again.

``Error parsing workflow: unable to load triggers``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One or more of the app workflow triggers are misconfigured. For each trigger, make sure to
1. define the trigger type as ``text``;
2. specify a ``match`` or ``match_regex`` for the trigger;
3. if you specified a ``match_regex`` trigger, confirm the regex is valid.

``Error parsing workflow: ... step name must not be blank``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At least one of the step names is empty. Please specify a name for the step and try again.

``Error parsing workflow: ... unable to load actions``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One or more of the app workflow actions are misconfigured. For each action, make sure to

1. define the action type as one of ``add_users_channel``, ``archive_channel``, ``create_channel``, or ``post``;
2. use the correct JSON for each action type as defined earlier in this document;
3. confirm the name in ``transition_to`` actions matches the name of another step in the app workflow.

Validation errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The incident response app validates template variables used in the app workflow. The error message indicates which specific variable is leading to the error.
