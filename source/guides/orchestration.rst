========================================
WIP: Deployment Solution Programs 
========================================

As an open source, private cloud messaging and file sharing solution under MIT license, Mattermost is commonly added to packaging and orchestration frameworks to make it even easier to deploy. 

We started the **Deployment Solutions Programs** as a way to help IT admins understand how Mattermost was being delivered in these frameworks. This is an optional program, currently under development, to help developers of frameworks increase awareness about their work. 

We recognize three levels of participation: 

- **Community Deployment Solutions** - Basic orchestration solutions for Mattermost, typically from the open source community or hosting companies who let us know about their work. The work of partners is included in blog posts and on social media as a benefit to the user and customer communities. Community Orchestration Partners are invited to discuss their work in the Mattermost community site in the `Installers and Images channel <https://pre-release.mattermost.com/core/channels/installers-and-images>`_ 

   Examples: 

   - `Puppet deployment solution for Mattermost <https://forge.puppet.com/liger1978/mattermost>`_ by Richard Grainger
   - `Heroku deployment solution for Mattermost <https://chrisdecairos.ca/deploying-mattermost-to-heroku/>`_ by Christopher De Cairos

- **Registered Deployment Solutions** - Orchestration solutions that follow detailed Mattermost guidelines on keeping up-to-date with the latest Mattermost version and security updates (typically a one-line change), linking to official documentation, supporting branding guidelines, and maintaining a changelog. This level of engagement allows Mattermost to more prominently promote the work, knowing that it's committed to meeting explicit standards.


- **Certified Deployment Solutions** - These solutions meet all the requirements of Registered Deployment Solutions, with the addition that they'll automate the version upgrade and security update processes (typically a one-line change). There is the added benefit that when Mattermost announces new versions and security updates, we can also announce the availability of updates to Certified Deployment Solutions. 

To summarize the commitment level of different solutions: 

==================================  ========= =========== ===========
Deployment Solution Requirement     Community Registered  Certified 
==================================  ========= =========== ===========
Installation                        Yes       Yes         Yes
----------------------------------  --------- ----------- -----------
Security Updates                              Yes         Yes 
----------------------------------  --------- ----------- -----------
Documentation                                 Yes         Yes
----------------------------------  --------- ----------- -----------
Branding                                      Yes         Yes
----------------------------------  --------- ----------- -----------
Upgrade                                                   Yes
==================================  ========= =========== ===========




WIP: 

## How should I automate the install and upgrade of Mattermost when included in another application? 

Automating Mattermost installation within another application: 

1. Review the [Mattermost installation guides](https://docs.mattermost.com/guides/administrator.html#installing-mattermost) to understand configuration steps of the production deployment 
2. Install Mattermost files to a dedicated `/opt/mattermost` directory by decompressing the `tar.gz` file of the latest release for your target platform (for example `linux-amd64`). 
3. Review [Configuration Settings](http://docs.mattermost.com/administration/config-settings.html) in `config.json` and set your automation to customize your Mattermost deployment based on your requirements. 
4. For directory locations defined in `config.json`, such as the location of the local file storage directory (`./data/`) or logs directory (`./logs`), you can redefine those locations in your `config.json` settings and move the directories.
   - All other directories should remain as they are in `/mattermost` 
5. Test that your Mattermost server is running with your new configuration.
6. Also, from the commandline run `./bin/platform -version` to test that the commandline interface is functioning properly.

Automating Mattermost upgrade within another application: 

1. Review the [upgrade guide](http://docs.mattermost.com/administration/upgrade.html) for an overview of the upgrade procedure. 
2. Create automation to upgrade to the next Mattermost versions: 
    - backup the `config.json` file to preserve any settings a user may have made.
    - backup the `./data` directory if local storage is used for files.
    - replace the contents of `/mattermost` directory with the decompressed contents of the latest release.
    - restore `config.json` and `./data` to their previous locations (which may have been overwritten).
    - if you need to overwrite any `config.json` parameters use a [`sed` command](http://stackoverflow.com/questions/20568515/how-to-use-sed-to-replace-a-config-files-variable) or similar tool to update `config.json`
    - starting the Mattermost server to upgrade the database, `config.json` file, and `./data` as necessary. 
3. Optionally the upgrade procedure can be chained so users can upgrade across an arbitrary number of Mattermost versions rather than to just the latest release. 
