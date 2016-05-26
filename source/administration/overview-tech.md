# Overview

Mattermost is a production-quality, self-hosted workplace messaging solution. 

We offer modern communication from behind your firewall. Your users can securely share messages and files across PCs and phones with continuous archiving and instant search while integrating with dozens of popular and custom tools. 

## Feature List 

#### Sharing Messaging and Files

- Send messages, comments, files and images across public, private and 1-1 channels
- Personalize notifications for unreads and mentions by channel and keyword
- Use #hashtags to tag and find messages, discussions and files

#### Archiving and Search 

- Search historical messages and comments with filtering by sender and channel
- View recent mentions of your name, username, nickname, and custom search terms
- Import Slack user accounts and channel archives

#### Anywhere Access

- Native apps on iOS, Android, Windows, Linux and Mac, plus desktop and mobile web experience
- Attach sound, video and image files from mobile devices 
- Define team-specific branding and color themes across your devices

#### Self-Host Ready

- Host and manage dozens of teams from a single Mattermost server 
- Easily manage your Mattermost server using a web-based System Console
- Script setup and maintenance using Mattermost command line tools 

#### Multi-Language Support

- English, Spanish, Brazilian Portuguese, French, and Japanese

## Release Numbering 

Mattermost numbers releases based on the following format: 

  `[Version Number].[Major Build Number].[Minor Build Number]`

- Major Version Number: Indicates a major system release (e.g. 1.x.x, 2.x.x)
   - Incrementing this number represents a major change to the codebase and potentially incompatibility with the previous major version release. 

- Major Build Number: Indicates significant new functionality, (e.g. 0.5.x, 0.6.x, 0.7.x)
   - This number is incremented with each monthly release on the 16th of the month, and represents significant code changes from the previous major build release. 

- Minor Build Number: Indicates a bug fix or security release (e.g. 1.2.5, 1.2.6)
   - This number is incremented for high priority bug fixes or security releases and does not typically contain significant code changes.

## Release Schedule

Mattermost releases new major builds monthly on the 16th from http://www.mattermost.org/download/. 

## Components 

Following installation, Mattermost state is stored in two places, a **system configuration** file and the **Mattermost database**. 

### System Configuration File 

This file, located in `config/config.json` stores Mattermost system settings. This file should be backed up before any upgrade or migration attempt. 

### Mattermost Database 

The Mattermost database set up during installation stores user and system data. This database is versioned and the Mattermost server has two requirements for the database version: 

1. The major build number of the executable is THE SAME as the major build number of the database.
   - For example, if the executable were 1.3.x and the database version was 1.3.x, Mattermost runs properly
2. The major build number of the executable is ONE HIGHER than the major build number of the database.
   - For example, if the executable were 1.4.x and the database version was 1.3.x, then when run the executable would detect the version difference and upgrade the database to the same version as the executable. 





