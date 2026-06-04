:orphan:

.. _autotranslation:

Set up Auto-translation (Beta)
==============================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v11.5, auto-translation automatically translates channel messages into each user's preferred display language. This enables multilingual teams to collaborate without language barriers.

Auto-translation uses an asynchronous queue-based architecture. When a message is posted in a channel with auto-translation enabled, the message is queued for translation into every configured target language. Translated messages replace the original display for users whose display language matches a target language, and they can view the original text at any time by selecting the translation icon on the message. Note that a user's auto-translation target language is determined by their Mattermost display language (set via **Settings > Display > Language**); decoupling the translation target from the display language is not currently supported.

Two translation provider options are available:

- **LibreTranslate**: An open-source, self-hosted translation engine.
- **Agents**: The Mattermost Agents plugin, which uses an LLM backend for translation.

.. tip::

   **Choosing between LibreTranslate and Agents**: LibreTranslate is a lightweight, self-hosted translation engine. The Agents provider uses an LLM backend and generally produces more accurate translations, especially for languages such as Japanese, Korean, and Chinese where contextual understanding improves quality. Consider your translation quality needs and existing infrastructure when choosing. Note that LibreTranslate does not support direct translation between all language pairs; for unsupported combinations it performs a pivot translation through an intermediate language (typically English), which can reduce accuracy for those pairs.

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

.. note::

   The languages available for selection in the **Languages allowed** list are controlled by the :ref:`Available languages <administration-guide/configure/site-configuration-settings:available languages>` setting (``AvailableLocales``) under **Site Configuration > Localization**. If that field is left blank, all supported languages are available. If it is not blank, only the languages listed there will appear as selectable auto-translation targets — so any language you want to use for auto-translation must be included in that list. The ``EnableExperimentalLocales`` setting can additionally make locale codes that are not yet fully supported in the Mattermost UI available for selection. Note that some locales (such as ``zh-CN``) are in beta, meaning portions of the Mattermost interface may still display in English even when that locale is active; this is a known limitation of the UI localization status and does not affect the translation of messages themselves.

Use the :ref:`Restrict autotranslation in direct and group messages <administration-guide/configure/site-configuration-settings:restrict autotranslation in direct and group messages>` setting to control whether auto-translation can be enabled in direct and group messages.

Configure LibreTranslate
~~~~~~~~~~~~~~~~~~~~~~~~~

The LibreTranslate provider uses a self-hosted LibreTranslate instance to translate messages.

Prerequisites:

- A running LibreTranslate server reachable from the Mattermost server.

1. Go to **System Console > Site Configuration > Localization**.
2. Set **Translation provider** to ``libretranslate``.
3. Enter the :ref:`LibreTranslate URL <administration-guide/configure/site-configuration-settings:libretranslate url>` (for example, ``http://libretranslate.internal:5000``).
4. If your LibreTranslate instance requires authentication, enter the :ref:`LibreTranslate API key <administration-guide/configure/site-configuration-settings:libretranslate api key>`.

Configure the Agents provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Agents provider uses the Mattermost Agents plugin to translate messages via a configured LLM service.

Prerequisites:

- The :doc:`Mattermost Agents plugin </administration-guide/configure/agents-admin-guide>` is installed and enabled.
- At least one LLM service is configured in the Agents plugin.

See the :ref:`auto-translation configuration reference <administration-guide/configure/site-configuration-settings:autotranslation>` for all available settings.
