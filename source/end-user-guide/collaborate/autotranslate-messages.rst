Autotranslate messages (Beta)
==============================

.. include:: ../../_static/badges/ent-adv.rst
  :start-after: :nosearch:

From Mattermost v11.5, messages in channels with autotranslation enabled are automatically translated into your preferred language. This enables seamless multilingual collaboration — you can read and respond in your own language while teammates do the same in theirs.

How autotranslation works
-------------------------

Your system admin must first enable autotranslation for your Mattermost instance. Then, a system admin or channel admin can enable it for individual channels. When autotranslation is enabled in a channel:

- The language of each message is automatically detected.
- Messages are translated into your preferred display language and shown in place of the original text.
- Code blocks, URLs, and @mentions are preserved and not translated.
- Translations happen asynchronously — there may be a brief delay before the translated text appears.
- Messages written in your preferred language are not translated.

View translated messages
-------------------------

Translated messages display in place of the original text. To view the original untranslated message, select the **translation** icon on the message.

Set your preferred language
----------------------------

Autotranslation translates messages into your Mattermost display language. To change your display language:

1. Select the gear icon to open **Settings**.
2. Select **Display > Language**.
3. Choose your preferred language.
4. Select **Save**.

See the :ref:`language <end-user-guide/preferences/manage-your-display-options:language>` documentation for more details.

Opt out of autotranslation in a channel
----------------------------------------

You can opt out of autotranslation on a per-channel basis if you prefer to see original messages in a specific channel. To opt out:

1. Open the channel where you want to disable autotranslation.
2. Select the channel name at the top to open the channel menu.
3. Disable the autotranslation option for this channel.

You'll see original, untranslated messages in that channel going forward. You can re-enable autotranslation at any time using the same steps.

Limitations
-----------

- **Direct and group messages**: Your system admin may have restricted autotranslation in direct and group messages. If autotranslation isn't available in a direct or group message, contact your system admin.
- **Short or mixed-language messages**: Very short messages or messages that mix multiple languages may not be reliably detected and translated.
- **Code-only messages**: Messages that contain only code blocks are skipped and not translated.
- **Translation accuracy**: Translation quality depends on the translation provider configured by your system admin. Some languages or specialized terminology may produce less accurate results.
