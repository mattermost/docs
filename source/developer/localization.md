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

Language option is listed as an option in **Account Settings > Display > Language** prefixed with **(Alpha)**.

#### Pre-Alpha 
- Translation has not yet reached Alpha quality 

As new languages are added, contributors may set up long running forks to translate and verify a new language prior to achieving Alpha-quality status and making a pull request to merge the new language option into `master`. 

## Translation Process

If you're interested in contributing translations to Mattermost, please join the [Mattermost localization channel to discuss.](https://pre-release.mattermost.com/core/channels/localization) Below are descriptions of the overall localization process.

#### Initial Translation 

To translate a language: 

1. Review GitHub issues and confirm someone else isn't already working on the same language
  - If they are, perhaps offer to help translate or review?
  - If no one is working on your language start a thread to see if others would collaborate with you
2. Follow the [developer setup guide](http://docs.mattermost.com/developer/developer-setup.html) and build Mattermost on your own machine
3. Set up translation for your language
   1. Create translation directories
    - Please create copies of the following files renamed using locale codes based on [Google's internationalization standard](https://developer.chrome.com/webstore/i18n): 
      - [`https://github.com/mattermost/platform/blob/master/i18n/en.json`](https://github.com/mattermost/platform/blob/master/i18n/en.json)
      - [`https://github.com/mattermost/platform/blob/master/web/static/i18n/en.json`](https://github.com/mattermost/platform/blob/master/web/static/i18n/en.json)
   2. Modify the following file to include your localization: [`https://github.com/mattermost/platform/blob/master/webapp/i18n/i18n.jsx`](https://github.com/mattermost/platform/blob/master/webapp/i18n/i18n.jsx)
   3. Compile and run Mattermost to confirm everything works
   4. Modify your `[locale].json` files  to translate the system to your choosen language
4. Follow the [contribution guide](http://docs.mattermost.com/developer/contribution-guide.html) to make a pull request with your translation 
   1. The Mattermost core team will set up a server for the community to test, review and contribute to your translation prior to merging it to `master`. 
   2. When there is consensus from at least 2 reviewers that the translation has achieved Alpha quality or higher, it will be merged
   3. The review and revision process may take days to weeks and the submitter may be requested to help rebase as needed until the PR can be merged

#### Using Mattermost Translation Server

Mattermost also hosts a Pootle server to perform collaborative internationalization online. Here's the process:

1. Sign-up to [Mattermost's Translation Server](http://186.202.167.109/)
2. Translate in your target language
3. Use [Mattermosti18n](https://github.com/rodrigocorsi2/mattermosti18n#convert-po---json) to convert Pootle's output into JSON files
4. Follow the [contribution guide](http://docs.mattermost.com/developer/contribution-guide.html) to make a pull request with your contribution

#### Translation Maintenance 

Translations require updates on a monthly basis as features are added and changed. The formal process for updates has yet to be determined. If you're interested in contributing to the process, please join the [Mattermost localization channel to discuss](https://pre-release.mattermost.com/core/channels/localization). 

Here are current maintainers for Alpha- or Beta-quality languages:

- French: [Pierre-Julien Grizel](https://github.com/pjgrizel) 
- Spanish: TBD
- Portugese: TBD
