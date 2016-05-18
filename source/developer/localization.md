# Localization 

The goal of the localization process is to consistently produce high quality translations release after release through collaboration between the international community, translators, project managers, language leads and the core team.

## Translation Process

If you're interested in contributing translations to Mattermost, please join the [Mattermost localization channel to discuss.](https://pre-release.mattermost.com/core/channels/localization) Below are descriptions of the overall localization process.

#### Initial Translation

To translate a language:
1. Join [Mattermost Translation Server](http://translate.mattermost.com)
2. Review and confirm that the language you want to help translate is listed
    - If it is, perhaps offer to help translate or review and make suggestions
    - If it's not, Ask on the [Mattermost localization channel](https://pre-release.mattermost.com/core/channels/localization) to setup your language so you can start helping with the translation.

#### Translations Updates

1. *New* and *updated* strings are imported to the [Mattermost Translation Server](http://translate.mattermost.com) on a daily basis at **12:00 GMT**
2. A new **Pull Request** is being made with the latest translations that reaches at least **Beta Quality** to the [Mattermost Platform Repo](https://github.com/mattermost/platform) every day at **22:00 GMT** without the need to do it on your own.

**IMPORTANT:** Please do not submit translations directly with your PR as they may be lost with the next Daily PR created from the Translation Server.

## Translation Quality

So users understand the accuracy and coverage of language translations, quality levels are explicitly defined for each language:

#### Official
- 100% of translation verified by someone deeply knowledgeble in Mattermost functionality
- 100% of translation verified by someone deeply knowledgeble in target language
- No translation may be out-of-date due to changes to English-language text since the last translation and review cycle.
- Language must have been in use for at least 1 full release cycle where end users in target language can share feedback and corrections

Language option is listed as an option in **Account Settings > Display > Language**.

#### Beta
- More than 95% of translation verified by someone deeply knowledgeble in Mattermost functionality
- More than 95% of translation verified by someone deeply knowledgeble in target language
- Up to 1% of translation may be out-of-date due to changes to English-language text since the last translation and review cycle.

Language option is listed as an option in **Account Settings > Display > Language** prefixed with **(Beta)**.

#### Alpha
- More than 85% of translation verified by someone deeply knowledgeble in Mattermost functionality
- More than 85% of translation verified by someone deeply knowledgeble in target language
- Up to 5% of translation may be out-of-date due to changes to English-language text since the last translation and review cycle.

Language option is listed as an option in **Account Settings > Display > Language** prefixed with **(Alpha)**.

#### Pre-Alpha
- Translation has not yet reached Alpha quality

As new languages are added, contributors may set up long running forks to translate and verify a new language prior to achieving Alpha-quality status and making a pull request to merge the new language option into `master`.

#### Translation Maintenance

Translations require updates on a monthly basis as features are added and changed. The formal process for updates has yet to be determined. If you're interested in contributing to the process, please join the [Mattermost localization channel to discuss](https://pre-release.mattermost.com/core/channels/localization).

Here are current maintainers for Alpha- or Beta-quality languages:

- French: [Pierre-Julien Grizel](https://github.com/pjgrizel)
- Spanish: [Elias Nahum](https://github.com/enahum)
- Portugese: TBD
- Japanese [Ryo Onodera](https://github.com/ryoon)
