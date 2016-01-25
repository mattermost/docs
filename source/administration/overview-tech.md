# Technical Overview

## Release Numbering 

Mattermost numbers releases based on the following format: 

  `[Version Number].[Major Build Number].[Minor Build Number]`

- Version Number: Indicates a major system release (e.g. 1.x.x, 2.x.x)
- Major Build Number: Indicates significant new functionality, (e.g. 0.5.x, 0.6.x, 0.7.x)
- Minor Build Number: Indicates a bug fix or security release (e.g. 1.2.5, 1.2.6)

## Release Schedule

Mattermost releases new major builds monthly on the 16th from http://www.mattermost.org/download/. 

## Components 

Following installation, Mattermost state is stored in three places: 

### 1) Executable file

Mattermost runs off this single executable file located in `bin/platform`. You can query its version with `platform -version`. 

### 2) Configuration file 

This file, located in `bin/config.json` stores Mattermost system settings. This file should be backed up before any upgrade or migration attempt. 

### 3) Database 

The Mattermost database set up during installation stores user and system data. This database is versioned and the Mattermost server has two requirements for the database version: 

1. The major build number of the executable is THE SAME as the major build number of the database.
   - For example, if the executable were 1.3.x and the database version was 1.3.x, Mattermost runs properly
2. The major build number of the executable is ONE HIGHER than the major build number of the database.
   - For example, if the executable were 1.4.x and the database version was 1.3.x, then when run the executable would detect the version difference and upgrade the database to the same version as the executable. 





