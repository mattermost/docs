Business Questions
==================

How can I create an open source derivative work of Mattermost?
--------------------------------------------------------------

If you're looking to customize the look and feel of Mattermost, see `documentation on customization <https://github.com/mattermost/docs/issues/1006>`__. For advanced customization, the system's user experience is available in different repositories for web, mobile apps, and desktop apps and custom experiences can be developed and integrated with either Mattermost Team Edition or Mattermost Enterprise Edition via the system APIs and drivers.

If, instead of using Mattermost Team Edition or Mattermost Enterprise Edition, you choose to compile your own version of the system using the open source code from ``/mattermost-server``, there are a number of factors to consider:

Security
~~~~~~~~

- If you run a fork of the Mattermost server, we highly recommend you only deploy the system securely behind a firewall and to pay close attention to `Mattermost security updates <https://mattermost.com/security-updates/>`__. Mattermost Team Edition and Mattermost Enterprise Edition release security update patches when reports of new attacks are received and verified. Mattermost waits until 14 days after a security patch is released before publicly detailing its nature so that users and customers can upgrade before the security vulnerability is widely known. A malicious user can potentially make use of Mattermost security disclosures to exploit a fork of Mattermost if the security upgrade is not promptly incorporated into the forked version.

Rebranding
~~~~~~~~~~

- When you create a derivative version of Mattermost and share it with others as a product, you need to replace the Mattermost name and logo from the system, among other requirements, per the `Mattermost trademark policy <https://mattermost.org/trademark-standards-of-use/>`__.
- You can rebrand your system using convenience tools for `custom branding <https://docs.mattermost.com/configure/configuration-settings.html#customization>`__.
- For advanced whitelabelling, and to whitelabel in Team Edition under MIT license without Enterprise Edition branding tools, you can manually update files on the Mattermost server `per product documentation. <https://github.com/mattermost/docs/issues/1006>`__ This can also be done without forking.

Copyright and Licensing of ``/mattermost-server`` open source code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Compiling and distributing your own version of the open source Mattermost ``/mattermost-server`` repo requires a) compliance with licenses in the repo, including `NOTICE.txt <https://github.com/mattermost/mattermost-server/blob/master/NOTICE.txt>`__, and b) the compiled version of the ``/mattermost-server`` source code should have the same open source license as the source code, `per our licensing policy <https://mattermost.org/licensing/>`__.

Other considerations
~~~~~~~~~~~~~~~~~~~~

- Mattermost has a default `Terms of Use <https://docs.mattermost.com/administration/config-settings.html#terms-of-service-link>`__ agreement for the Terms of Use link at the bottom of login screen that should be incorporated into any additional Terms of Use you may add.

- The Mattermost copyright notices on the user interface should remain.
- There may be additional legal and regulatory issues to consider and we recommend you employ legal counsel to fully understand what's involved in creating and selling a derivative work.

Will Mattermost complete questionnaires requiring confidential data without an NDA?
-----------------------------------------------------------------------------------

No, Mattermost will not complete questionnaires requiring confidential data without a non-disclosure agreement. You can find `Mattermost's standard mutual non-disclosure agreement online <https://docs.google.com/document/d/10Qc2kxxZGYNzp9b19oEhItRM01OPyrWRISJ2rbm1gvc/edit>`__.

Why does Mattermost have a discount for certain kinds of non-profits but not for others?
----------------------------------------------------------------------------------------

While we welcome anyone to use the open source version of Mattermost Team Edition free of charge, Mattermost, Inc., like any software company, has specific discounting programs for its commercial Mattermost Enterprise Edition based on business objectives. Objectives of the discounting programs include the suitability of potential case studies, references, word-of-mouth promotion and public promotion of solutions, among many other factors.

See our `License and Subscription <https://docs.mattermost.com/about/license-and-subscription.html#do-you-have-a-program-for-official-non-profits-open-source-projects-and-charities>`__ documentation for details.

Can I create a derivative work of the Mattermost /mattermost-server repository that is not open source?
-------------------------------------------------------------------------------------------------------

The Mattermost open source project was created by `a group of developers who had their data paywalled by a proprietary online messaging service <https://mattermost.org/why-we-made-mattermost-an-open-source-slack-alternative/>`__ and felt it was unfair.

Because of this, the Mattermost /mattermost-server repository uses an open source license that requires derivative works to use the same open source license. This prevents the creation of derivative works that are not open source, and the situation where end users would not have access to the source code of the systems they use, and hence be at risk of "lock in".

For companies purchasing Enterprise Edition subscriptions for use by internal staff, who need to modify /mattermost-server, and who also have legal departments that won't allow their staff to work under an open source software license, a special "Advanced Licensing Option" can be purchased to modify /mattermost-server for internal use under a commercial software license. This option is not available for companies that would offer a modified, non-open source version of Mattermost to external parties.

Will Mattermost, Inc. offer the ability to resell Mattermost software without a reseller agreement?
----------------------------------------------------------------------------------------------------

No.

If there is a case where the reseller agreement is under review and a customer urgently needs an order, Mattermost may, with internal approvals, accept a reseller purchase order with the following language:

"Any statements, clauses, or conditions included on or referenced by buyer's purchase order forms, which forms modify, add to, or are inconsistent with Mattermost’s standard terms and conditions are expressly rejected. Such orders will only be accepted by Mattermost upon the condition and with the express understanding that despite any such statements, clauses, or conditions contained in any order forms of the buyer are void and have no effect.

EXCEPT AS OTHERWISE EXPRESSLY AGREED BY THE PARTIES IN WRITING, MATTERMOST MAKES NO WARRANTIES OR REPRESENTATIONS WITH RESPECT TO ANY MATTERMOST PRODUCTS, DOCUMENTATION OR SUPPORT, AND HEREBY DISCLAIMS ALL OTHER EXPRESS AND ALL IMPLIED WARRANTIES, INCLUDING BUT NOT LIMITED TO IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT."

Does Mattermost answer questions about open source licenses authored by other organizations?
---------------------------------------------------------------------------------------------

No, if you have questions about an open source license, please consult the original author, or FAQs they offer.