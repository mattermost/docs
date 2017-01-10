Creating Teams
==============

New teams can be created if the System Admin has **Enable Team Creation** set to true from the System Console.

Methods to Create a Team
------------------------

Teams can be created from the team sidebar or Main Menu. The person who creates a team will automatically be given the Team Admin role for that team.

Team Sidebar
~~~~~~~~~~~~~~~~~~~~
If you belong to more than one team, a team sidebar will appear left of your channel list on the left-hand sidebar.

.. image:: ../images/team-sidebar.png

Click the "+" icon at the bottom of the team sidebar, then click **Create a new team** on the team selection page, which guides you through the rest of the setup steps. If this option is not visible on the web page, then the System Admin has disabled team creation.

If you have no other teams to join, clicking the "+" icon brings you directly to the team creation page if team creation is enabled.

Main Menu
~~~~~~~~~~
From your current Mattermost team, click on the **Main Menu** > **Create a New Team**. If this option is not visible in the menu, then the System Admin has disabled team creation.

Team Name and URL Selection
---------------------------

There are a few details and restrictions to consider when selecting a team name and team URL.

Team Name
~~~~~~~~~~~~~

This is the display name of your team that appears in menus and
headings.

-  It can contain any letters, numbers or symbols.
-  It is case sensitive.
-  It must be 2 - 15 characters in length.

Team URL
~~~~~~~~~~~

The team URL is part of the web address that navigates to your team on
the system domain, ``https://domain.com/teamurl/``.

-  It may contain only lowercase letters, numbers and dashes.
-  It must start with a letter and cannot end in a dash.
-  It must be 2 - 15 characters in length.
-  It cannot start with the following restricted words: ``signup``,
   ``login``, ``admin``, ``channel``, ``post``, ``api``, ``oauth``
