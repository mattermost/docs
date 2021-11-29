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

Mention people
--------------

You can include a team member on a card by mentioning them on a card <https://docs.mattermost.com/messaging/mentioning-teammates.html>__ the same way you would in Channels. The team member you mention will receive a Direct Message notification from the Boards bot with a link to the card you mentioned them on. To mention multiple team members, separate each name with a comma.

Mention auto-completes will be available in a future release.

[Note that I've started simple with user mentions, rather than diving right into the properties. This provides foundational grounding for the reader because user mentions in boards work exactly the same way as something they are likely already experienced with: Channels!]

Share card previews
-------------------

When you share a link to a card within Mattermost, the card details are automatically displayed in a preview. This preview highlights what the card is about at a glance without having to click through to it.

[Similar philosophy here - a simple concept that ideally works the same as Channels via link previews; this helps users extend existing knowledge to new functional areas.]

Customize card properties
-------------------------

Cards can contain different data fields depending on the purpose of the board. For example, in a Roadmap board, cards include a Type field where you can add categories such as Bug, Triage, etc. In a Task board, cards include Status and Priority fields instead.

Add and manage properties
-------------------------

On a card, you can create a new property field by selecting Add a property, then selecting the type of property from the drop-down menu. The property type specifies the type of data you plan to capture within that field. When you create new card properties, they are added to all new and all existing cards on the current board.

Properties are automatically added to the board filter list at the top of the page, so ensure you customize all property names to make it easy to filter your board by specific properties later.

You can rename a property at any time by opening a card, then selecting New Property. Your changes are saved immediate, and applied across all cards on the current board.

You can also delete properties you no longer need by selecting the property, then choosing Delete.  You'll be asked to confirm that you want to removes that property from every card on the current board.

Once you have card properties defined, you have full control over which properties are visible on the board. Click Properties at the top of the board, then enable all properties you want to see at a glance, and hide all properties you don't want to see.

Work with property types

    checkboxes are useful for agenda items that are regularly revisited in weekly sprint or grooming meetings
    multi-select allows you to create badges to indicate things like status
    numbers are useful to capture metrics such as task sizing or effort estimates
    person provides a quick way to capture user assignments
    etc.

****

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

