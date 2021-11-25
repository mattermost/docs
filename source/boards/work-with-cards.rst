Work with Cards
===============

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Cards can have different configuration fields, depending on the type of board you've selected. For example, in a Roadmap board you'll find the cards include an option for **Type** where you can add categories such as Bug, Triage, etc. A Task board doesn't include a Type field, but includes **Status** and **Priority**. All cards have a **New Property** field. For this field, you can select the type from the drop-down menu. It'll then be added to your card.

The default name for a new property is **New Property**. Ensure that you name your property as it's added to the filter list at the top of the board and having all your filters named **New Property** makes it difficult to work out what you're filtering. You can rename a property field by opening up a card and selecting **New Property**. Enter the new name in the field provided. The change is saved immediately and applied across all cards.

How to use properties
---------------------

Properties can be used for whatever situation you choose. Here are some use cases that you can use on your own boards.

Recurring events
~~~~~~~~~~~~~~~~

In some situations, such as a weekly meeting agenda, there may be agenda items that are regularly revisited. You can use the **Checkbox** property to create a property type (e.g., **Recurring** or **Revisit**). To display this information in the view you're using, select **Properties** and then select the property name to display the checkbox on the card.

Note that this setting is applied per board.

Calculations
------------

Each board includes calculations which allow users to answer basic metric questions without needing to create complex reports, such as:

- How many story points are planned for this release?
- How many tasks have been assigned or not assigned?
- How long has the oldest bug been sitting in the backlog?

The calculation options are available at the bottom of a board.

Mention people
--------------

You can include a team member in a card by mentioning them on the card. The format is the same as using mentions in Channels. The team member you mention will receive a Direct Message notification from the Boards bot with a link to the card you mentioned them on.

To mention multiple team members, separate each name with a comma. Ensure that you enter the correct username - auto-complete will be available in a future version of Boards.

Previews
--------

When you share a link to a card in Mattermost, the card details are automatically displayed in a preview so you can see what the card is about at a glance and without having to click through to it.

