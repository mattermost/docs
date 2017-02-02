================================================
Deployment Solution Programs (Work-in-progress) 
================================================

*This program is under development, please consider below a work-in-progress*

Mattermost's **Deployment Solutions Programs** help IT administrators understand how Mattermost is being offered in third-party deployment solutions. 

This is an optional program for third-party developers to increase awareness about their work and to enable Mattermost to refer its communities to different solutions. 

Any person or any company interested in discussing deployment solutions with Mattermost can join the `Deployment Solutions discussion channel <https://pre-release.mattermost.com/core/channels/installers-and-images>`_ on the Mattermost community server to speak to peers and Mattermost community managers. 

Deployment solutions are recognized by Mattermost at three-levels: 

- **Community Deployment Solutions** - Basic orchestration solutions for Mattermost, typically from the open source community or hosting companies who let us know about their work. The work of partners is included in blog posts and on social media as a benefit to the user and customer communities. 

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

Requirement details are outline below: 

Deployment Solution Program Requirements 
------------------------------------------

Installation 
~~~~~~~~~~~~~~~~~~~~~~~

1. **Installation is designed for officially supported operating systems and platforms**. EXCEPTION: RHEL equivalents (CentOS, Amazon Linux, Oracle Linux, Scientific Linux) are acceptable as long as the exception is noted in README or equivalent with ``This deployment uses [OPERATING_SYSTEM] as an equivalent to the officially supported version of Red Hat Enterprise Linux.``

Security Updates 
~~~~~~~~~~~~~~~~~~~~~~~

1. **Document commitment to providing security updates.** README or equivalent states `We highly recommend users subscribe to the Mattermost security updates email list. When notified of a security update, the maintainers of this deployment solution will make an effort to update to the secure version within 10 days.`

2. **Commit to making an effort for your deployment to provide the latest security update within 10 days of announcement**. This is typically a one-line change. 

Documentation 
~~~~~~~~~~~~~~~~~~~~~~~

1. **Include link to official Mattermost documentation**. README or equivalent contains statement ``Please see https://docs.mattermost.com for official documentation.``

Branding 
~~~~~~~~~~~~~~~~~~~~~~~

1. **Support Mattermost branding and naming guidelines**. To ensure naming is clear across deployment solutions, README or equivalent should contain ``The name for this deployment solution in the context of [Mattermost branding guidelines](https://www.mattermost.org/brand-guidelines/) is `[NAME] for Mattermost by [CREATOR]`.`` For example, ``Multi-node Docker deployment solution for Mattermost by John Doe``. This is the name that will be used to refer to your work in Mattermost community materials. 

Upgrade 
~~~~~~~~~~~~~~~~~~~~~~~

1. **Support upgrade of Mattermost**. Enable user interface or commandline upgrade of a Mattermost deployment to latest version based on upgrade guide instructions. 
