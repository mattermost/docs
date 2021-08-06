
Deployment Solution Programs 
============================

Mattermost's **Deployment Solutions Programs** help IT administrators understand how Mattermost is being offered in third-party deployment solutions, including other open source projects as well as in commercial solutions.

This is an optional program for third-party developers to increase awareness about their work and to enable Mattermost to refer its communities to different solutions.

Any person or any company interested in discussing deployment solutions with Mattermost can join the `Deployment Solutions discussion channel <https://community.mattermost.com/core/channels/installers-and-images>`__ on the Mattermost community server to speak to peers and Mattermost community managers.

Deployment solutions are recognized by Mattermost at three-levels:

- **Community Deployment Solutions** - Basic orchestration solutions for Mattermost, typically from the open source community or hosting companies who let us know about their work. The work of partners is included in blog posts and on social media as a benefit to the user and customer communities.

   Examples:

   - `Puppet deployment solution for Mattermost <https://forge.puppet.com/liger1978/mattermost>`__ by Richard Grainger
   - `Heroku deployment solution for Mattermost <https://chrisdecairos.ca/deploying-mattermost-to-heroku/>`__ by Christopher De Cairos

- **Registered Deployment Solutions** - Orchestration solutions that follow detailed Mattermost guidelines on keeping up-to-date with the latest Mattermost version and security updates (typically a one-line change), linking to official documentation, supporting branding guidelines, and maintaining a changelog. This level of engagement allows Mattermost to more prominently promote the work, knowing that it's committed to meeting explicit standards.

- **Certified Deployment Solutions** - These solutions meet all the requirements of Registered Deployment Solutions, with the addition that they'll automate the version upgrade and security update processes (typically a one-line change). There is the added benefit that when Mattermost announces new versions and security updates, we can also announce the availability of updates to Certified Deployment Solutions.

To summarize the commitment level of different solutions:

==================================  ========= =========== ===========
Deployment Solution Requirement     Community Registered  Certified 
==================================  ========= =========== ===========
Installation                        Yes       Yes         Yes
----------------------------------  --------- ----------- -----------
Minimum Documentation               Yes       Yes         Yes 
----------------------------------  --------- ----------- -----------
Security Updates                              Yes         Yes 
----------------------------------  --------- ----------- -----------
Branding                                      Yes         Yes
----------------------------------  --------- ----------- -----------
Upgrade                                                   Yes
==================================  ========= =========== ===========

Requirement details are outline below:

Deployment Solution Program Requirements 
----------------------------------------

Installation 
~~~~~~~~~~~~

1. **Installation is designed for officially supported operating systems and platforms**. EXCEPTION: RHEL equivalents (CentOS, Amazon Linux, Oracle Linux, Scientific Linux) are acceptable as long as the exception is noted in README or equivalent with ``This deployment uses [OPERATING_SYSTEM] as an equivalent to the officially supported version of Red Hat Enterprise Linux.``

2. **Automated installation passes basic testing**. After installation run the following manual tests:

  1) Create a new user account and use that account to create a new team and post to Town Square channel.
  2) Create a second user account and join the newly created team and reply to first user's post in Town Square.
  3) Go back to first user account and post reply with an image attached.
  4) Confirm there are no errors and no blue bar at the top of the screen with "Mattermost unreachable error" (which would indicate websocket configuration error).

Documentation 
~~~~~~~~~~~~~

1. **Include link to official Mattermost documentation**. README or equivalent contains statement ``Please see https://docs.mattermost.com for official documentation.``

  Include the following information in text, markdown, HTML or other format. Square brackets [] indicate optional statements depending on the configuration of your solution:
 
      This deployment solution installs [and upgrades] a Mattermost server to provide secure, private cloud messaging for teams and enterprises. More information is available at: https://about.mattermost.com
 
      Following automated deployment, the following steps are required to make your system production-ready:
      
      - [Configure SSL for Mattermost](https://about.mattermost.com/ssl-configuration/)
      - [Configure SMTP email for Mattermost](https://about.mattermost.com/smtp-configuration/)

2. **Unofficial deployment options should be documented**. Unofficial deployment configurations, such as use of Linux operating systems that are not officially supported, should be documented in the README.

Security Updates 
~~~~~~~~~~~~~~~~

1. **Document commitment to providing security updates.** README or equivalent states `We highly recommend users subscribe to the Mattermost security updates email list. When notified of a security update, the maintainers of this deployment solution will make an effort to update to the secure version within 10 days.`

2. **Commit to making an effort for your deployment to provide the latest security update within 10 days of announcement**. This is typically a one-line change.

Branding 
~~~~~~~~

1. **Support Mattermost branding and naming guidelines**. To ensure naming is clear across deployment solutions, README or equivalent should contain ``The name for this deployment solution in the context of [Mattermost branding guidelines](https://mattermost.org/brand-guidelines/) is `[NAME] for Mattermost by [CREATOR]`.`` For example, ``Multi-node Docker deployment solution for Mattermost by John Doe``. This is the name that will be used to refer to your work in Mattermost community materials.

Upgrade 
~~~~~~~

1. **Support upgrade of Mattermost**. Enable user interface or command line upgrade of a Mattermost deployment to latest version based on `upgrade procedure when Mattermost is embedded <https://docs.mattermost.com/developer/integration-faq.html#how-should-i-automate-the-install-and-upgrade-of-mattermost-when-included-in-another-application>`__
