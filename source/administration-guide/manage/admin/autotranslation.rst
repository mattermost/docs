:orphan:

.. _autotranslation:

Set up Auto-translation (Beta)
==============================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v11.5, auto-translation automatically translates channel messages into each user's preferred display language. This enables multilingual teams to collaborate without language barriers.

Auto-translation uses an asynchronous queue-based architecture. When a message is posted in a channel with auto-translation enabled, the message is queued for translation into every configured target language. Translated messages replace the original display for users whose display language matches a target language, and they can view the original text at any time by selecting the translation icon on the message.

Two translation provider options are available:

- **LibreTranslate**: An open-source, self-hosted translation engine.
- **Agents**: The Mattermost Agents plugin, which uses an LLM backend for translation.

.. tip::

   **Choosing between LibreTranslate and Agents**: LibreTranslate is a lightweight, self-hosted translation engine. The Agents provider uses an LLM backend and generally produces more accurate translations, especially for languages such as Japanese, Korean, and Chinese where contextual understanding improves quality. Consider your translation quality needs and existing infrastructure when choosing.

   **Choosing an LLM for the Agents provider**: Smaller, faster models are recommended for auto-translation. Translation is a well-defined task that doesn't benefit from the extended reasoning capabilities of larger models — larger models may actually overthink the task, adding unnecessary latency without improving quality. A model like ``gpt-3.5-turbo`` provides accurate translations with lower latency.

Enable auto-translation
~~~~~~~~~~~~~~~~~~~~~~~

Auto-translation is managed on a per-channel basis and is disabled by default for all channels. System admins and channel admins can enable or disable auto-translation for individual channels.

- When auto-translation is enabled or disabled in a channel, a system post notifies channel members of the change.

.. note::

   Enabling auto-translation in a channel only translates new messages going forward. Existing message history is not retroactively translated.

Set up Auto-translation
-----------------------

Prerequisites:

- **LibreTranslate**: A running LibreTranslate server reachable from the Mattermost server.
- **Agents**: The :doc:`Mattermost Agents plugin </administration-guide/configure/agents-admin-guide>` installed and configured with at least one LLM service.

Configure a translation provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to **System Console > Site Configuration > Localization**.
2. Set :ref:`Enable autotranslation <administration-guide/configure/site-configuration-settings:enable autotranslation>` to **True**.
3. Select a :ref:`Translation provider <administration-guide/configure/site-configuration-settings:translation provider>` (``libretranslate`` or ``agents``).
4. Configure :ref:`Languages allowed <administration-guide/configure/site-configuration-settings:languages allowed>` — every message in auto-translation-enabled channels is translated into each language in this list.
5. Select **Save**.

Use the :ref:`Restrict autotranslation in direct and group messages <administration-guide/configure/site-configuration-settings:restrict autotranslation in direct and group messages>` setting to control whether auto-translation can be enabled in direct and group messages.

.. important::

   The languages available for selection in the **Languages allowed** list are controlled by two System Console settings under **Site Configuration > Localization**:

   - :ref:`Available languages <administration-guide/configure/site-configuration-settings:available languages>` (``AvailableLocales``): Defines the set of languages users can select as their display language. Only languages included here appear as selectable target languages for auto-translation. If left blank, all supported languages are available.
   - **Enable experimental locales** (``EnableExperimentalLocales``): When enabled, additional locale codes that are not yet fully supported in the Mattermost UI become available for selection.

   For example, to make Chinese Simplified available as a target language for auto-translation, add ``zh-CN`` to the **Available languages** field. If this field is left blank, all supported languages — including Chinese — are available without any additional configuration.

   **Note on beta and experimental locales**: Some languages, such as Chinese, may have a beta or incomplete UI localization. This means a portion of the Mattermost interface may still display in English even after switching to that locale. This is a known limitation of the UI localization status and is separate from the quality of the message translation itself.

Configure LibreTranslate
~~~~~~~~~~~~~~~~~~~~~~~~~

The LibreTranslate provider uses a self-hosted LibreTranslate instance to translate messages.

Prerequisites:

- A running LibreTranslate server reachable from the Mattermost server.

1. Go to **System Console > Site Configuration > Localization**.
2. Set **Translation provider** to ``libretranslate``.
3. Enter the :ref:`LibreTranslate URL <administration-guide/configure/site-configuration-settings:libretranslate url>` (for example, ``http://libretranslate.internal:5000``).
4. If your LibreTranslate instance requires authentication, enter the :ref:`LibreTranslate API key <administration-guide/configure/site-configuration-settings:libretranslate api key>`.

.. note::

   LibreTranslate does not support direct translation between all language pairs. For language combinations without a direct translation model, LibreTranslate performs a pivot translation through an intermediate language (typically English). For example, a message may be translated from Chinese to English, and then from English to Japanese. This intermediary step can reduce translation accuracy for affected language pairs.

Configure the Agents provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Agents provider uses the Mattermost Agents plugin to translate messages via a configured LLM service.

Prerequisites:

- The :doc:`Mattermost Agents plugin </administration-guide/configure/agents-admin-guide>` is installed and enabled.
- At least one LLM service is configured in the Agents plugin.

See the :ref:`auto-translation configuration reference <administration-guide/configure/site-configuration-settings:autotranslation>` for all available settings.

Translation language and user display language
----------------------------------------------

Auto-translation currently uses each user's Mattermost **display language** (set via **Settings > Display > Language**) to determine which translation to show. A translated version of a message is shown to a user only if their display language matches one of the configured **Languages allowed** target languages.

.. note::

   Because auto-translation target languages are tied to the Mattermost UI display language, users must set their display language to the desired translation language to receive translated messages. Decoupling the auto-translation target language from the UI display language is not currently supported.
