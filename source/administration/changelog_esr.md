# Mattermost Extended Support Release (ESR) Changelog

This changelog summarizes updates to [Mattermost Team Edition ESR](http://www.mattermost.org/) and [Mattermost Enterprise Edition ESR](https://mattermost.com/pricing/)

## Release v5.9.1

 - Mattermost v5.9.1 contains a high level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

## Release v5.9

Released 2019-03-16

Mattermost v5.9.0 contains low to medium level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Breaking Changes since last release

 - If **DisableLegacyMfa** setting in ``config.json`` is set to ``true`` and multi-factor authentication is enabled, ensure your users have upgraded to mobile app version 1.17 or later. Otherwise, users who have MFA enabled may not be able to log in successfully. See [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html) for more details.
 - The public IP of the Mattermost application server is considered a reserved IP for additional security hardening in the context of untrusted external requests such as Open Graph metadata, webhooks or slash commands. See [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html) for more details.

**IMPORTANT:** If you upgrade from another release than 5.8, please read the [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

### Bug Fixes

 - Fixed an issue where emoji reactions did not appear on posts right away.
 - Fixed an issue where the emoji `Recently Used` cleared entirely after logging out and back in.
 - Fixed an issue where emoji not included in our list of text-based emoji were not rendered as jumboemoji.
 - Fixed an issue where the default server/client locales got reverted to ``en`` on server startup.
 - Fixed an issue where email notification setting in the webapp was out of sync with the mobile apps.
 - Fixed an issue where a broken image displayed on login page if custom branding was enabled but no image had been uploaded.
 - Fixed an issue where at-channel, at-all, at-here followed by a period were not highlighted as mentions.
 - Fixed an issue where the Mattermost icon was pixelated in bookmark rendering on Google Chrome.
 - Fixed an issue where **System Console > Users** page had broken user interface on narrow screens.
 - Fixed an issue where at-channel notification showed incorrect number of timezones.
 - Fixed an issue where leading whitespace with emoji affected emoji size so that they didn't render as jumboemoji.
 - Fixed an issue where the System Console graphs did not load smoothly.
 - Fixed an issue with inconsistent formatting in page header on **System Console > Notifications > Mobile Push**.
 - Fixed an issue where invite tokens with a 48-hour expiry expired after 24 hours.
 - Fixed an issue where a blank screen appeared when opening a group message channel from "More" modal using Enter key.
 - Fixed an issue where Zoom plugin caused link metadata code to print warnings in the System Console.

### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.
 
#### Changes to Team Edition and Enterprise Edition:
 
 - **Enable Image Proxy** setting is now ``false`` by default. See [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html) for more details.
 - Under ``"ServiceSettings"`` in ``config.json``:
    - Added ``"DisableLegacyMFA": false,`` to keep the legacy checkMfa endpoint enabled to support mobile versions 1.16 and earlier. See [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html) for more details.

### Known Issues

 - On a server using a subpath, the URL opens a blank page if the system admin changes the Site URL in the System Console UI. The system admin should restart the server to fix it.
 - Login does not work when Custom Terms of Service is enabled and MFA is enforced.
 - Google login fails on the Classic mobile apps.
 - User can receive a video call from another browser tab while already on a call.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - CTRL/CMD+U shortcut to upload a file doesn’t work on Firefox.
 
### Contributors

Thank you to everyone who contributed to the Mattermost project in February 2019!

[adzimzf](https://github.com/adzimzf), [aeomin](https://translate.mattermost.com/user/aeomin/), [amyblais](https://github.com/amyblais), [asaadmahmood](https://github.com/asaadmahmood), [aswathkk](https://github.com/aswathkk), [awbraunstein](https://github.com/awbraunstein), [bbodenmiller](https://github.com/bbodenmiller), [BK1603](https://github.com/BK1603), [bradjcoughlin](https://github.com/bradjcoughlin), [chikei](https://github.com/chikei), [cometkim](https://github.com/cometkim), [comharris](https://github.com/comharris), [courtneypattison](https://github.com/courtneypattison), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [danmaas](https://github.com/danmaas), [dannymohammad](https://github.com/dannymohammad), [deanwhillier](https://github.com/deanwhillier), [der-test](https://github.com/der-test), [DHaussermann](https://github.com/DHaussermann), [dom3k](https://github.com/dom3k), [dos1701](https://github.com/dos1701), [DSchalla](https://github.com/DSchalla), [ejachang](https://github.com/ejachang), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [fcorrea](https://github.com/fcorrea), [gabrieljackson](https://github.com/gabrieljackson), [gruceqq](https://translate.mattermost.com/user/gruceqq/), [gupsho](https://github.com/gupsho), [hannaparks](https://github.com/hannaparks), [hanzei](https://github.com/hanzei), [hectorskypl](https://github.com/hectorskypl), [hmhealey](https://github.com/hmhealey), [icelander](https://github.com/icelander), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jdillard](https://github.com/jdillard), [jespino](https://github.com/jespino), [jfcastroluis](https://github.com/jfcastroluis), [jfrerich](https://github.com/jfrerich), [JtheBAB](https://github.com/JtheBAB), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [Kaya_Zeren](https://twitter.com/kaya_zeren), [kosgrz](https://github.com/kosgrz), [koukouloforos](https://github.com/koukouloforos), [kscheel](https://github.com/kscheel), [Lena](https://translate.mattermost.com/user/Lena/), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [manland](https://github.com/manland), [maruTA-bis5](https://github.com/maruTA-bis5), [meilon](https://github.com/meilon), [mgdelacroix](https://github.com/mgdelacroix), [migbot](https://github.com/migbot), [MirlanMaksv](https://github.com/MirlanMaksv), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [onnadi-work](https://github.com/onnadi-work), [patniharshit](https://github.com/patniharshit), [pichouk](https://github.com/pichouk), [R-Wang97](https://github.com/R-Wang97), [Robbe7730](https://github.com/Robbe7730), [rodcorsi](https://github.com/rodcorsi), [sadohert](https://github.com/sadohert), [sandlis](https://github.com/sandlis), [sanojsubran](https://github.com/sanojsubran), [saturninoabril](https://github.com/saturninoabril), [staabm](https://github.com/staabm), [sudheerDev](https://github.com/sudheerDev), [svelle](https://github.com/svelle), [tauu](https://github.com/tauu), [thedingwing](https://github.com/thedingwing), [thePanz](https://github.com/thepanz), [ulhosting](https://github.com/uhlhosting), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [yuya-oc](https://github.com/yuya-oc), [zetaab](https://github.com/zetaab)
