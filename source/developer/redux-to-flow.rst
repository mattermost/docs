Migrating the Redux Library to Flow
===================================

The Mattermost team wants to improve the quality, security and stability of the
code, and one way to do this is by introducing the usage of type checking. Thus, we have
decided to introduce Flow in our codebase. As a first step, we want to start migrating the
mattermost-redux library (in the future we will also migrate the webapp and mobile app).

This campaign will help with the migration by annotating the javascript code with
Flow annotations.

By completing this campaign, we are looking to:

- reduce the errors derived from changes.
- increase the consistency of the code.
- ensure a more defensive programming in the code.

Contributing
------------

If you're interested in contributing, please join the `Flow channel on pre-release.mattermost.com <https://pre-release.mattermost.com/core/channels/flow>`__. Progress on moving individual files to use Flow is `tracked on this spreadsheet <https://docs.google.com/spreadsheets/d/10FmRm5TgpsDIkpvqX1emwVYe33-NQShy4I7LZSZbkPA/edit#gid=0>`__. If you want to work on one of the files, let us know in the Flow channel or by making a comment on the spreadsheet.

List of current contributors, in alphabetical order:

 - Fede (`@gnufede <https://github.com/gnufede>`_)
 - Harrison Healey (`@hmhealey <https://github.com/hmhealey>`_)
 - Jesús Espino (`@jespino <https://github.com/jespino>`_)
 - Jesse Hallam (`@lieut-data <https://github.com/lieut-data>`_)
 - Sudheer (`@sudheerDev <https://github.com/sudheerDev>`_)

For guidance on migrating a file to Flow, please read the next section.

Component Migration Steps
-------------------------

There are a few steps involved with migrating a file to use Flow. Some of them may not apply to every file and they may change slightly based on the file you're working on. In general, you can follow these steps as a checklist for work that needs to be done on each file.

1. If you are receiving or returning an object, it must be defined as a flow type (if the flow type is not defined yet, go to ``src/types`` and create it).
  - An exception is a dynamic object where each key is an identifier -- for example, you can return ``{[string]: Post}``.
2. We prefer "strict" objects definitions -- for example, ``{|key1: string, key2: string|}`` is better than ``{key1: string, key2: string}``.
  - An exception is if we are not able to determine all properties.
3. If the object is stored in the global store in any way, the data must be added to the ``src/types/store.js``.
4. Check that everything still passes in the ``make flow`` command.

Examples
------------------

You can see example pull requests here:

- https://github.com/mattermost/mattermost-redux/pull/489
- https://github.com/mattermost/mattermost-redux/pull/488
