Localization
============

The goal of the localization process is to consistently produce high quality translations release after release through collaboration between the international community, translators, project managers, language leads and the core team.

Translation Process
-------------------

If you're interested in contributing translations to Mattermost, please join the `Mattermost localization channel to discuss <https://community.mattermost.com/core/channels/localization>`_. Below are descriptions of the overall localization process.

Initial Translation
-------------------

To translate a language:

1. Join the `Mattermost Translation Server <http://translate.mattermost.com>`_.

2. Check whether the language you want to help translate is listed in the `Translation Server <https://translate.mattermost.com/projects/>`_.

   * If it is, perhaps offer to help translate or review and make suggestions.
   * If not, ask to setup your language on the `Mattermost localization channel <https://community.mattermost.com/core/channels/localization>`_, so you can start helping with the translation.

   Note: Languages are grouped either as "shipped" or as "work in progress". A language `ships in Mattermost <https://docs.mattermost.com/help/settings/account-settings.html#language>`_ if it meets specified `translation quality`_.

3. Review translation rules written by localization leads, when applicable:

   * `German (Regeln zur Übersetzung von Mattermost) <https://gist.github.com/der-test/6e04bff8a173e053811cb93e08838ca2>`_
   * `French (Règles pour la traduction francophone de Mattermost) <https://github.com/wget/mattermost-localization-french-translation-rules>`_
   * `Dutch translation rules for Mattermost <https://github.com/ctlaltdieliet/mattermost-localization-dutch-translation-rules>`_

Translations Updates
--------------------

1. New and updated source strings are automatically added to the translation server each time a GitHub pull request containing string changes is merged.

2. A new pull request with latest translations that reach at least Beta quality is submitted to the `mattermost-mobile <https://github.com/mattermost/mattermost-mobile>`_, `mattermost-server <https://github.com/mattermost/mattermost-server>`_, and `mattermost-webapp <https://github.com/mattermost/mattermost-webapp>`_ repos each Monday at 22:00 GMT.

   * A pull request will also be submitted on the day of major feature complete and code complete to ensure latest translations are included in the release.
   * A pull request may also be submitted for a release candidate.

**IMPORTANT:** Please do **not** submit translations directly via a pull request as they may be lost with the next pull request update from the Mattermost Translation Server.

Translation Quality
-------------------

In order for users to understand the accuracy and coverage of language translations, quality levels are explicitly defined for each language:

Official
~~~~~~~~

* 100% of translation verified by someone deeply knowledgeable in Mattermost functionality.
* 100% of translation verified by someone deeply knowledgeable in target language.
* No translation may be out-of-date due to changes to English-language text since the last translation and review cycle.
* Language must have at least one official reviewer who maintains the language with updated strings imported to the `Translation Server <http://translate.mattermost.com>`_ over time.
* Language must have been in use for **at least 3 full release cycles** where end users in target language can share feedback and corrections.

Official languages are listed in **Account Settings > Display > Language**.

Beta
~~~~

* 90% of translation verified by someone deeply knowledgeable in Mattermost functionality and in the target language.
* Up to 10% of translation may be out-of-date due to changes to English-language text since the last translation and review cycle.

Beta languages are listed in **Account Settings > Display > Language** appended with **(Beta)**.

Alpha
~~~~~

* Translation has not yet reached Beta quality.

An official language may be changed back to Beta or Alpha if the specified requirements are not met for a release. Similarly, Beta languages may be dropped back to Alpha.

Message Syntax 
-----------------

To format localized messages, `mattermost-webapp <https://github.com/mattermost/mattermost-webapp>`_ uses the `react-intl <https://formatjs.io/docs/react-intl>`_, a Javascript library from `FormatJS <https://formatjs.io/>`_. This library uses the `ICU Message syntax <http://userguide.icu-project.org/formatparse/messages>`_, which is the standard syntax for many programming languages.

If you don't know about the ICU syntax, please familiarize yourself by reading the `ICU Message Syntax simplified documentation <https://formatjs.io/docs/icu-syntax/>`_. What's most important here is to read the section dedicated to how plural terms are managed.

In order to ease the manipulation of strings like these with a special syntax (ICU as a reminder), a developer has created an online tool allowing to test an ICU string. This tool, called `Online ICU Message Editor <https://format-message.github.io/icu-message-format-for-translators/editor.html>`_, is displayed as a live editor previewing how a string will appear in context. This tool has been reported by some members of our community as really helpful to translate strings containing an ICU syntax. Don't hesitate to use it.

Knowledge Base
-----------------

Some terms used in Mattermost may be technical. If you don't know how to translate a specific term:

* If applicable, check how the term has been translated in other locations of the translation you are contributing to.
* Use a translation engine to know how others have translated the term.
* Use the `Microsoft open linguistic portal <https://www.microsoft.com/en-us/language/Search>`_.
* Ask your question on the `Mattermost localization channel <https://community.mattermost.com/core/channels/localization>`_.

Test Translations
-----------------

If you'd like to review and verify translations prior to achieving Beta-quality status, you can follow these steps:

1. Build Mattermost on your machine following the `Developer Machine Setup Guides <https://docs.mattermost.com/developer/dev-setup.html>`_.

2. Download a copy of your translations to your local machine by going to the language of your choice, e.g. `German <https://translate.mattermost.com/projects/mattermost/mattermost-server_master/de/>`_, then **Files > Download original translation file (go-i18n JSON file)**.

3. Copy the generated ``[locale].json`` files to the corresponding directories:

   * For the server, copy the files to the i18n directory of the ``mattermost-server`` project.
   * For the webapp, copy the files to the i18n directory of the ``mattermost-webapp`` project.

4. Modify the file ``i18n/i18n.jsx`` in the ``mattermost-webapp`` project to include your translated strings.

5. Compile and run **Mattermost** to confirm everything works. You can then review and verify translations from your machine.

   If you find a string that has not been translated, search for the string in the respective localization file to confirm it's included for translations. You can find the English version for server, webapp, and mobile projects below

   * https://github.com/mattermost/mattermost-server/blob/master/i18n/en.json
   * https://github.com/mattermost/mattermost-webapp/blob/master/i18n/en.json
   * https://github.com/mattermost/mattermost-mobile/blob/master/assets/base/i18n/en.json

   If it’s included in the file, then most likely it hasn't been translated yet, but is in https://translate.mattermost.com.

   If you want to confirm if it's translated, you can check for the respective .json file in ``/i18n`` folder. 

Translation Maintenance
-----------------------

Translations require updates on a monthly basis as features are added and changed.

While the formal process for updates has yet to be determined, currently the Release Manager notifies one of the official translation reviewers who then forwards the message to the community of translators. This reminder tends to induce a virtuous cycle of motivation into the community of translators.

Below are current official reviewers and maintainers for languages that have reached at least Beta-quality. Official reviewers submit final translations for languages; maintainers suggest translations and step in when official reviewers aren't able to help in a certain release.

If you're interested in contributing to the process, please join the `Mattermost localization channel to discuss <https://community.mattermost.com/core/channels/localization>`_. Creating localization channels is also encouraged - see examples of current channels including `Italian <https://community.mattermost.com/core/channels/i18n-italian>`_, `German <https://community.mattermost.com/core/channels/i18n-german>`_ and `Swedish <https://community.mattermost.com/core/channels/i18n-swedish>`_.

.. csv-table::
    :header: "Language", "Official Reviewer(s)", "Maintainers"

    "Deutsch - German", "`Christian Arnold (meilon) <https://github.com/meilon>`_", "`Tim Estermann (der-test) <https://github.com/der-test>`_"
    "Español - Spanish", "`Elias Nahum (enahum) <https://github.com/enahum>`_", "`Jesús Espino <http://github.com/jespino>`_"
    "Français - French", "`William Gathoye (wget) <https://github.com/wget>`_", ""
    "Italiano - Italian", "`Michael Longo (mlongo4290) <https://github.com/mlongo4290>`_, `Ema Panz (thepanz) <https://github.com/thepanz>`_", ""
    "日本語 - Japanese", "`Yusuke Nemoto (kaakaa) <https://github.com/kaakaa>`_", ""
    "한국어 - Korean", "TBD (Open Role)", ""
    "Nederlands - Dutch", "`Tom De Moor <https://github.com/ctlaltdieliet>`_", ""
    "Polski - Poland", "`Daniel Burzmiński (hectorskypl) <https://github.com/hectorskypl>`_, `Tomasz Gruca (gruceqq) <https://translate.mattermost.com/user/gruceqq/>`_",
    "Português do Brasil - Portuguese", "`Rodrigo Corsi (rodcorsi) <https://github.com/rodcorsi>`_", "`Carlos Tadeu Panato Junior (cpanato) <https://github.com/cpanato>`_"
    "Română - Romanian", "`Viorel-Cosmin Miron (uhlhosting) <https://github.com/uhlhosting>`_", ""
    "Türkçe - Turkish", "`Kaya Zeren <https://twitter.com/kaya_zeren>`_", ""
    "Pусский - Russian", "`Alexey Napalkov <https://github.com/flynbit>`_", ""
    "Yкраїнська - Ukrainian", "TBD (Open Role)", ""
    "中文 (简体) - Simplified Chinese", "`aeomin <http://translate.mattermost.com/user/aeomin/>`_", ""
    "中文 (繁體) - Traditional Chinese", "`Tze-Kei Lee (chikei) <https://github.com/chikei>`_", ""

Administrative tasks
~~~~~~~~~~~~~~~~~~~~~~~~

To grant trusted translators additional permissions as Weblate admin:

1. Add the user to the ``mattermost@TrustedReviewers`` group in Weblate.
2. Select **Admin interface** (tool icon in Weblate).
3. Go to **Users > Django Admin Interface**.
4. Select the user you want to grant permissions to.
5. Go to **Groups**.
6. Add the user to ``mattermost@TrustedReviewers`` group.
7. Hit **Save**.
