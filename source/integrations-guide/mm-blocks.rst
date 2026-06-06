MM Blocks
==========

.. include:: ../_static/badges/all-commercial.rst
  :start-after: :nosearch:

**Technical complexity:** :ref:`Low-code <low-code>`

MM Blocks are Mattermost's structured format for rich, interactive posts. Use them to build notifications with text, images, layouts, buttons, and menus directly in a post's ``props``—without relying on Slack-compatible `message attachments <https://developers.mattermost.com/integrate/reference/message-attachments/>`_.

MM Blocks replace message attachments as the recommended way to create `interactive messages <https://developers.mattermost.com/integrate/plugins/interactive-messages/>`_. Existing attachment-based payloads continue to work: clients translate them into MM Blocks at render time.

Overview
--------

Interactive posts combine:

- **Content blocks** in ``props.mm_blocks`` — text, images, dividers, containers, columns, collapsible sections, buttons, and static selects.
- **Action definitions** in ``props.mm_blocks_actions`` — maps each ``action_id`` to an integration URL or in-app navigation target.

When a post is created, the server encrypts ``mm_blocks_actions`` into a single cookie string before the post is sent to clients. Users interact with buttons and menus in the channel; Mattermost calls your integration and can update the post or return an ephemeral reply.

MM Blocks are supported on web, desktop, and mobile clients. Availability is controlled by the ``MmBlocksEnabled`` `feature flag <https://developers.mattermost.com/contribute/more-info/server/feature-flags/>`_ (enabled by default in current Mattermost releases). Self-hosted deployments can set ``MM_FEATUREFLAGS_MMBLOCKSENABLED=false`` to disable rendering and action dispatch for MM Blocks payloads.

Quick start
-----------

This incoming webhook payload renders a short message with a primary button. The button calls an external integration URL when clicked.

.. code-block:: json

    {
      "text": "Deployment finished",
      "props": {
        "mm_blocks": [
          {
            "type": "text",
            "text": "Build **#42** deployed to *staging*."
          },
          {
            "type": "divider"
          },
          {
            "type": "button",
            "text": "View logs",
            "style": "primary",
            "action_id": "view_logs"
          }
        ],
        "mm_blocks_actions": {
          "view_logs": {
            "type": "external",
            "url": "https://example.com/integrations/view-logs",
            "context": {
              "deployment_id": "42"
            }
          }
        }
      }
    }

Post properties
---------------

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Property
     - Description
   * - ``props.mm_blocks``
     - Array of block objects that define layout and interactive controls. See `Block types`_ below.
   * - ``props.mm_blocks_actions``
     - Object keyed by ``action_id``. Each value defines how Mattermost handles a button press or menu selection. Replaced on the wire by an encrypted cookie after the post is saved.

You can include ``mm_blocks`` in any post payload that supports ``props``, including :doc:`incoming webhooks </integrations-guide/incoming-webhooks>`, :doc:`outgoing webhook </integrations-guide/outgoing-webhooks>` responses, slash command responses, bot posts, and ephemeral posts created through the API.

Block types
-----------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Type
     - Description
   * - ``text``
     - Markdown text. Optional ``size`` (``small`` or ``default``) and ``is_subtle`` (muted color).
   * - ``divider``
     - Horizontal rule between blocks.
   * - ``image``
     - Image with ``url``, optional ``alt_text``, ``title``, ``size`` (``auto``, ``xsmall``, ``small``, ``medium``, ``large``, ``stretch``), ``max_width``, ``max_height``, ``image_style``, and ``horizontal_alignment``.
   * - ``button``
     - Labeled button. Requires ``text`` and ``action_id``. Optional ``style`` (``default``, ``primary``, ``danger``, ``good``, ``success``, ``warning``, or ``#RRGGBB`` hex), ``tooltip``, ``disabled``, and per-control ``query``.
   * - ``static_select``
     - Dropdown menu. Requires ``action_id`` and ``placeholder``. Optional ``options`` (``text`` / ``value`` pairs), ``initial_option``, ``disabled``, ``data_source`` (``users`` or ``channels`` for dynamic pickers), and ``query``.
   * - ``container``
     - Groups nested blocks in ``content``. Optional ``border``, ``accent_color``, ``background`` (``gray`` or ``none``), ``gap``, ``flow`` (``horizontal`` or ``vertical``), and ``max_height`` (``none``, ``small``, ``medium``, ``large``) to clip and scroll overflowing content.
   * - ``column_set`` / ``column``
     - Multi-column layout. A ``column_set`` contains ``columns``; each ``column`` has ``items`` and optional ``width`` (``auto`` or ``stretch``).
   * - ``collapsible``
     - Expandable section with ``header`` and ``content`` block arrays. Optional ``collapsed`` (defaults to expanded).

Malformed block entries are skipped at render time; valid blocks in the same array still display.

Container example
~~~~~~~~~~~~~~~~~

.. code-block:: json

    {
      "props": {
        "mm_blocks": [
          {
            "type": "container",
            "accent_color": "#439FE0",
            "border": true,
            "gap": "small",
            "content": [
              {"type": "text", "text": "**Incident summary**"},
              {"type": "text", "text": "Severity: high", "is_subtle": true, "size": "small"},
              {
                "type": "column_set",
                "columns": [
                  {
                    "type": "column",
                    "width": "stretch",
                    "items": [{"type": "text", "text": "Service: **payments**"}]
                  },
                  {
                    "type": "column",
                    "width": "stretch",
                    "items": [{"type": "text", "text": "Region: **us-east-1**"}]
                  }
                ]
              }
            ]
          }
        ]
      }
    }

Interactive actions
-------------------

Define one entry in ``mm_blocks_actions`` for each ``action_id`` used by a ``button`` or ``static_select`` block.

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Action type
     - Behavior
   * - ``external``
     - Mattermost sends an HTTP POST to ``url`` with the user's selection, a ``trigger_id`` for follow-up calls (such as opening an `interactive dialog <https://developers.mattermost.com/integrate/plugins/interactive-dialogs/>`_), and optional ``context``. Your integration can update the original post or return an ephemeral message.
   * - ``openURL``
     - Navigates the user to ``url`` inside Mattermost (relative paths such as ``/team/channels/town-square``) or in the system browser for absolute ``http``/``https`` links. The response may include ``goto_location`` for client-side routing.

Optional ``query`` on an action definition is merged into the target URL. Per-control ``query`` on a block is sent in the post-action request body and merged after the action-level query.

When a user selects a menu option, Mattermost includes ``selected_option`` in the post-action request with the chosen value.

Action API
----------

When a user activates a control, the client calls:

``POST /api/v4/posts/{post_id}/actions/{action_id}``

The request body may include:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Field
     - Description
   * - ``cookie``
     - Encrypted action cookie for the post (supplied automatically by Mattermost clients).
   * - ``selected_option``
     - Value from a ``static_select`` menu selection.
   * - ``query``
     - Per-control query parameters from the block definition.
   * - ``integration_format``
     - Source format for the action: ``mm_block``, ``attachment``, ``block``, ``card``, or ``apps_binding``.

A successful response returns ``status``, ``trigger_id``, and optionally ``goto_location`` for ``openURL`` actions.

``action_id`` values may contain letters, numbers, underscores (``_``), and hyphens (``-``).

Legacy formats
--------------

Mattermost clients still accept older interactive payload shapes and translate them into MM Blocks for rendering. When multiple formats are present, clients use this priority:

1. ``props.mm_blocks`` (native)
2. ``props.blocks`` (Slack Block Kit)
3. ``props.cards`` (Adaptive Cards)
4. ``props.attachments`` (Slack-compatible message attachments)

.. note::

   Message attachments remain supported for backward compatibility. New integrations should use ``mm_blocks`` and ``mm_blocks_actions`` instead of nesting interactive controls under ``attachments``.

Attachment actions map to MM Blocks as follows:

- Attachment ``actions[].id`` becomes ``action_id`` on buttons and selects.
- Attachment ``actions[].integration.url`` is used for external dispatch (equivalent to ``mm_blocks_actions`` entries).
- Button ``style`` values (``primary``, ``good``, ``danger``, hex colors, and so on) are preserved.

Migrating from attachments
--------------------------

1. Move visual content (text, fields, images) into typed MM Blocks—use ``container`` blocks with ``accent_color`` instead of attachment ``color``, and ``text`` blocks instead of ``pretext`` / ``text`` / field values.
2. Replace ``actions`` arrays with ``button`` and ``static_select`` blocks that reference ``action_id`` values.
3. Add an ``mm_blocks_actions`` map keyed by those IDs with ``type``, ``url``, and ``context`` (previously ``integration.url`` and ``integration.context``).
4. Optionally add ``text`` (or ``message``) above the blocks for notifications and search when the block content alone is not enough context.

Example migration — attachment button:

.. code-block:: json

    {
      "attachments": [
        {
          "text": "Approve this change?",
          "actions": [
            {
              "type": "button",
              "id": "approve",
              "name": "Approve",
              "style": "primary",
              "integration": {
                "url": "https://example.com/actions/approve",
                "context": {"id": "cr-1"}
              }
            }
          ]
        }
      ]
    }

Equivalent MM Blocks payload:

.. code-block:: json

    {
      "text": "Approve this change?",
      "props": {
        "mm_blocks": [
          {"type": "text", "text": "Approve this change?"},
          {
            "type": "button",
            "text": "Approve",
            "style": "primary",
            "action_id": "approve"
          }
        ],
        "mm_blocks_actions": {
          "approve": {
            "type": "external",
            "url": "https://example.com/actions/approve",
            "context": {"id": "cr-1"}
          }
        }
      }
    }

End-user experience
-------------------

See :doc:`Extend Mattermost with integrations </end-user-guide/collaborate/extend-mattermost-with-integrations>` for end-user guidance on buttons, menus, collapsible sections, and expandable content. See :doc:`Troubleshoot MM Blocks </get-help/mm-blocks-troubleshooting>` if content does not render or respond as expected.

On all supported clients, users can tap buttons, open static select menus, and expand or collapse ``collapsible`` sections inline in the channel.

Containers with a ``max_height`` preset clip overflowing content. On mobile, users select the expand control on a clipped region to open a full-screen **Scrollable content** view. On web and desktop, the same regions scroll inside the post.

Legacy attachment posts render with the same MM Blocks UI after client-side translation, so button and menu behavior is consistent across formats.

Related documentation
---------------------

- :doc:`Incoming webhooks </integrations-guide/incoming-webhooks>` — post MM Blocks through a webhook URL.
- :doc:`Outgoing webhooks </integrations-guide/outgoing-webhooks>` — return MM Blocks in webhook responses.
- `Interactive messages <https://developers.mattermost.com/integrate/plugins/interactive-messages/>`_ — action handling, ephemeral updates, and integration responses.
- `Message attachments <https://developers.mattermost.com/integrate/reference/message-attachments/>`_ — legacy Slack-compatible format (still supported).
- `Interactive dialogs <https://developers.mattermost.com/integrate/plugins/interactive-dialogs/>`_ — collect structured input after a button click.
