Incident Response Application (EE, Closed Alpha)
------------------------------------------------------

The incident response application is available in closed Alpha, in `Enterprise Edition <https://mattermost.com/pricing/>`_. 

`Sign up to our Alpha program <https://docs.google.com/forms/d/e/1FAIpQLSf4Rr1YnofQQnKHJuL0Cgz_DaCUitt_Atik7K9KXsDefCyXlg/viewform>`_ and shape the direction of the incident response application!

.. contents:: Contents
  :backlinks: top
  :local:
  :depth: 2

1 - Selection of supported use cases.

// TODO: Add a screenshot or a video

How can I try the app?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. `Sign up for the closed Alpha program <https://docs.google.com/forms/d/e/1FAIpQLSf4Rr1YnofQQnKHJuL0Cgz_DaCUitt_Atik7K9KXsDefCyXlg/viewform>`_. If you're selected to join the Alpha program, you will receive an email from us with a plugin binary.
3. Upload the plugin binary in **System Console > Plugins > Plugin Management** `following these steps <https://about.mattermost.com/default-plugin-uploads>`_.
4. Enable the plugin from the **Installed Plugins** list.
5. Use `one of these sample app workflows <// TODO Add a link>`_ to try the app. To upload these workflows to your instance:
 
 - save the app workflow schema to a JSON file
 - go to any Mattermost channel and post ``/workflow edit`` to open the workflow editor
 - click **Choose .json file** and select the JSON file containing the app workflow schema
 - click **Upload**

6. Post the trigger word defined in the workflow schmea to start the workflow!

See the documentation below to get help on how to configure and manage your app workflows, or open an issue at https://forum.mattermost.org and we'd be happy to help you.

3 - Supported features
 - triggers
 - steps
 - actions
 - transitions
 - statistics

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

6 - Roadmap (focus on use cases we plan to support to help paint a vision, instead of features which are likely to change and give narrow idea of future)

<Offer a link for sharing feedback>

Troubleshooting
~~~~~~~~~~~~~~~~~~

Below are common error messages and how to resolve them. If you need any further help with configuring the app, let us know at https://forum.mattermost.org and we'd be happy to assist you.

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
