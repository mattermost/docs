# Localization 

The goal of the localization process is to consistently produce high quality translations release after release through collaboration between the international community, translators, project managers, language leads and the core team.

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

Alpha quality translations may be checked into `master` so long as they are disabled by default and enabled using **Account Settings > Advanced > Preview pre-released features > Include Alpha-quality languages**, after which they would appear in **Account Settings > Display > Language** prefixed with **(Alpha)**.

#### Pre-Alpha 
- Translation has not yet reached Alpha quality 

As new languages are added, contributors may set up long running forks to translate and verify a new language prior to achieving Alpha-quality status and making a pull request to merge the new language option into `master`. 

## Translation Process

If you're interested in contributing translations to Mattermost, please join the [Mattermost localization channel to discuss.](https://pre-release.mattermost.com/core/channels/localization)


