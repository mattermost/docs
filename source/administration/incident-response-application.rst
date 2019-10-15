Incident Response Application (EE, Closed Alpha)
------------------------------------------------------

Available in closed Alpha, in `Enterprise Edition <https://mattermost.com/pricing/>`_. `Sign up to our closed Alpha program <https://docs.google.com/forms/d/e/1FAIpQLSf4Rr1YnofQQnKHJuL0Cgz_DaCUitt_Atik7K9KXsDefCyXlg/viewform>`_ and shape the direction of the incident response application.

.. contents:: Contents
  :backlinks: top
  :local:
  :depth: 2

1 - Selection of supported use cases.

// TODO: Add a screenshot or a video

2 - How to try it out?
 - sign up for the closed Alpha program (Add some clause that not everyone may be selected to join the program)
 - receive a plugin binary from us
 - install the plugin, then enable
 - use one of these sample workflows to try the plugin in your instance
 - post <trigger word> to start the workflow!

3 - Supported features
 - triggers
 - steps
 - actions
 - transitions
 - statistics

Sample Workflow Schema
~~~~~~~~~~~~~~~~~~~~~~~~

Below is a full sample workflow schema with a text trigger, four steps and multiple actions including transitions.

For other sample workflow schemas, `see here <// TODO Add other samples in https://github.com/mattermost/docs/tree/master/source/samples and link them here. See MM-18870>`_.

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

Permissions and Management of Workflows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only System Administrators can edit workflows by uploading a JSON file via the ``/workflow edit`` command. This allows System Administrators to have full control over what workflows are configured in a Mattermost server.

Later, permissions to allow other users to edit workflows may be supported.

6 - Roadmap (focus on use cases we plan to support to help paint a vision, instead of features which are likely to change and give narrow idea of future)

<Offer a link for sharing feedback>

7 - Troubleshooting (use examples from this PR: https://github.com/mattermost/mattermost-plugin-workflow/pull/24)

<Offer a link to ask for help>

