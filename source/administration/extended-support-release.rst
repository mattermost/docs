Extended Support Release
========================

What is an Extended Support Release?
------------------------------------
During each monthly release, Mattermost backports security fixes to the previous two monthly releases. Extended Support Releases (ESRs) are releases that will receive backports for security fixes and major bug fixes for the length of their life cycle.  

What is the life cycle of an Extended Support Release?
------------------------------------------------------
Mattermost provides an ESR when a significant number of new features and improvements have been added to the product, and those new features have had sufficient time to stabilize. Depending on the product roadmap, there could be multiple Extended Support Releases at one time. 

When an ESR is at the end of its life cycle, there will be announcements ahead of time to provide time for people to test, certify, and deploy a newer ESR version before support ends. There will be a clear upgrade path provided between ESR versions. 

After a release reaches its end-of-life, no further updates will be provided for that version. 

To receive updates about Extended Support Releases, sign up for our mailing list `here <http://eepurl.com/dCKn2P>`__. 

What is included in an Extended Support Release dot release? 
------------------------------------------------------------
Dot releases for ESR versions will contain high severity or high impact security fixes and bug fixes. They will not include changes to product functionality or new features. 

Who should use an Extended Support Release? 
-------------------------------------------
ESRs are intended for organizations who value stability over having the newest features and improvements, or who have a long internal testing and certification process to undergo when upgrading.

If your organization prefers to have the newest features and improvements, Extended Support Releases may not be the best fit for you.

How do I install the Extended Support Release?
----------------------------------------------
Follow our normal `install <https://docs.mattermost.com/guides/administrator.html#installing-mattermost>`__ or `upgrade <https://docs.mattermost.com/administration/upgrade.html>`__ guides. When downloading the Mattermost version, choose an Extended Support Release from the list below. 

What are the current supported ESR versions? 
--------------------------------------------

+-------------+----------------+----------------+--------------------------------------------------------------------------------------------+-------------------------------------------------+
| Version     | Release Date   | End of Support | Latest Dot Release Download link                                                           | Upgrade Notes                                   |
+=============+================+================+============================================================================================+=================================================+
| 5.9         |  2019-04-16    | T.B.D.         | `5.9.5 <https://releases.mattermost.com/5.9.5/mattermost-5.9.5-linux-amd64.tar.gz>`_       | Please upgrade to 5.0 prior to upgrading to 5.9 |
+-------------+----------------+----------------+--------------------------------------------------------------------------------------------+-------------------------------------------------+
| 4.10        |  2018-05-16    | 2019-07-15     | `4.10.10 <https://releases.mattermost.com/4.10.10/mattermost-4.10.10-linux-amd64.tar.gz>`_ |                                                 |
+-------------+----------------+----------------+--------------------------------------------------------------------------------------------+-------------------------------------------------+

How do I restore a previous Extended Support Release?
-----------------------------------------------------
Before you perform an upgrade, please ensure you have done a full back up of your current version.  You can restore the database and previous version if you need to revert an upgrade.  Please note that previous ESR versions are subject to an end of support date. 
