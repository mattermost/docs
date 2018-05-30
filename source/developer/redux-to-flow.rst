Migrating the Redux library to Flow
===================================

The Mattermost team want to improve the quality, security and stability of the
code, and one way to do that is introducing the usage of type checking. We have
decide to introduce Flow in our codebase. We want to start migrating the
mattermost-redux library as first step (in the future we will migrate the web
app and the mobile app too).

This campaign is meant to help with that by annotating the javascript code with
Flow annotations.

By completing this campaign, we're looking to:

- Reduce the errors derived from changes.
- Increase the consistency of the code.
- Ensure a more defensive programming in the code.

Contributing
------------

If you're interested in contributing please join the `Flow channel on pre-release.mattermost.com <https://pre-release.mattermost.com/core/channels/flow>`__. Progress on moving individual files to use Flow is `tracked on this spreadsheet <https://docs.google.com/spreadsheets/d/10FmRm5TgpsDIkpvqX1emwVYe33-NQShy4I7LZSZbkPA/edit#gid=0>`__. If you want to work on one of the files let us know in the Flow channel or by making a comment on the spreadsheet.

List of contributors, in alphabetical order:

 - Fede (`@gnufede <https://github.com/gnufede>`_)
 - Harrison Healey (`@hmhealey <https://github.com/hmhealey>`_)
 - Jesús Espino (`@jespino <https://github.com/jespino>`_)
 - Jesse Hallam (`@lieut-data <https://github.com/lieut-data>`_)
 - Sudheer (`@sudheerDev <https://github.com/sudheerDev>`_)

For guidance on migrating a file to Flow, read the next section.

Component Migration Steps
-------------------------

There are a few steps involved with migrating a file to use Flow. Some of them may not apply to every file and they may change slightly based on the file you're working on. In general, you can follow these steps as a checklist for work that needs to be done on each file.

1. If you are receiving or returning an object, must be defined as a flow type (If is not defined yet, go to `src/types` and create it)
  - An exception is a dynamic object where each key is an identifier, for example, you can return `{[string]: Post}`.
2. We prefer "strict" objects definitions (`{|key1: string, key2: string|}` is better than `{key1: string, key2: string}`).
  - An exception is if we can't determine all properties.
3. If the object is store in the global store in any way, we must add that data to the `src/types/store.js`.
4. Check that everything still passes the `make flow` command.

Examples
------------------
You can see some example pull requests here:

- https://github.com/mattermost/mattermost-redux/pull/489
- https://github.com/mattermost/mattermost-redux/pull/488
