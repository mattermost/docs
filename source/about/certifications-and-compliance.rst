
Certifications and Compliance Overview
========================================

This overview summarizes how Mattermost can help users in support of their internal compliance initiatives, including:

- GDPR Compliance
- U.S. Export Compliance

GDPR Compliance
----------------

The following overview summarizes how Mattermost software can be used to assist in compliance programs covering the European Union's General Data Protection Regulation, also known as Regulation (EU): 2016/679 (`See full text <https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32016R0679&from=EN>`__) and how Mattermost, Inc., itself, adheres to regulatory requirements.

Continual Commitment to the Principles of GDPR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost is a collaboration hub for highly-trusted organizations and is committed to supporting the principles of GDPR to protect the data of people in the European Union. Mattermost adheres to this mission through the use of:

- **Security Infrastructure:** Continual investment in security, privacy and compliance capabilities.
- **Contractual Obligations:** Appropriate contractual obligations through our terms of service, including the `Data Processing Addendum <https://about.mattermost.com/default-data-processing-addendum/>`__ in our standard `Terms of Service <https://mattermost.com/terms-of-service/>`__.
- **Privacy Measures:** Privacy measures are outlined in our `Privacy Policy <https://mattermost.com/privacy-policy/>`__.
- **Product Features:** To ensure data management and data portability.

To stay up to date with our efforts, please subscribe to `our regular newsletter <https://about.mattermost.com/newsletter/>`__.

Security Infrastructure
~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost enables organizations to protect their information, and the information of their users and customers, through self-hosted communication infrastructure that has been developed with a high standard of security. The features of this security infrastructure include:

- **Security Features** in Mattermost open source and commercial offerings that enable deployment of your organization’s own infrastructure.
- **Responsible Disclosure Policy** for security researchers around the world to confidentially report suspected vulnerabilities, which can be addressed in updates to Mattermost software.
- **Security Reviews** conducted by both our own internal security review team and external security researchers.
- **ISO 27001 Standards** which are met to achieve alignment with international security guidelines.

Contractual Obligations
~~~~~~~~~~~~~~~~~~~~~~~

Mattermost adheres to contractual obligations for ensuring the proper management of data through:

- **GDPR-Compliant Data Processing Addendum** included with Mattermost’s standard terms.
- **Mattermost Privacy Policy** sharing how data is handled on the online infrastructure controlled by Mattermost, Inc.

Privacy Measures
~~~~~~~~~~~~~~~~~

Mattermost outlines security measures to maintain the safety of personal data submitted by our customers and partners in our `Privacy Policy <https://mattermost.com/privacy-policy/>`__.

Product Features
~~~~~~~~~~~~~~~~

Mattermost supports features that ensure data management and data portability.

Data Management
^^^^^^^^^^^^^^^^

- **Data Retention:** Use `data retention <https://docs.mattermost.com/comply/data-retention-policy.html>`__ to automatically erase data after a set period of time, a feature that meets the Right to Erasure principle. In Team Edition, you can use database scripts to achieve the same result.
- **Profile Deletion:** Delete a user’s personal information via `mmctl user delete <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-user-delete>`__, or via `the CLI <https://docs.mattermost.com/manage/command-line-tools.html#mattermost-user-delete>`__. Both the mmctl and the CLI command permanently deletes all user information including messages created by the user.
- **Self-Hosted Push Notification Service:** Self-host your own push notification service, or deploy mobile apps with any EMM provider that supports `AppConfig <https://www.appconfig.org/members/>`__ to meet security and compliance policies. See `our Mobile App deployment documentation <https://docs.mattermost.com/deploy/mobile-overview.html>`__ to learn more.

Data Portability
^^^^^^^^^^^^^^^^^

- **Data Import:** Use the `bulk loading tool <https://docs.mattermost.com/onboard/bulk-loading-data.html>`__ to migrate data from an existing messaging system, or for pre-populating a new installation with data. `Review this guide <https://docs.mattermost.com/onboard/migrating-from-hipchat-to-mattermost.html>`__ which summarizes the different approaches and meets the `Right to Data Portability <https://gdpr-info.eu/art-20-gdpr/>`__ principle.
- **Data Export:** Use `compliance exports <https://docs.mattermost.com/comply/compliance-export.html>`__ to export conversations from public, private and direct message channels in XML or EML format. Those in Team Edition can export conversations directly from the database, both `in MySQL <https://www.itworld.com/article/2833078/it-management/3-ways-to-import-and-export-a-mysql-database.html>`__ and `in PostgreSQL <https://www.a2hosting.com/kb/developer-corner/postgresql/import-and-export-a-postgresql-database>`__.

Accessibility Compliance
-------------------------

Adherence with accessibility standards is assisted in the following ways:

- **508 Compliance:** For U.S. public sector organizations seeking to confirm 508 compliance, Mattermost publicly shares its `Voluntary Product Accessibility Template (VPAT) online <https://docs.mattermost.com/about/vpat.html>`__.
- **WCAG 2.0L:** For meeting Web Contact Accessibility Guidelines 2.0 (WCAG), Mattermost has received a third-party "A" rating and is working towards an "AA" rating.
- **ADA:** Mattermost compliance with the Americans with Disabilities Act (ADA) is achieved by offering the accessibility support detailed in the VPAT and WCAG 2.0 guidelines with Mattermost's online experience as the interface to accessibility tools.
- **Remediation:** Any technical issue in a current or future product release that would prevent compliance with accessibility ratings stated in product documentation would be considered a product defect and Mattermost would welcome the `public filing of an issue report against the defect <https://mattermost.org/filing-issues/>`__ so that it may be resolved.

U.S. Export Compliance Overview
-------------------------------

Summary Table
~~~~~~~~~~~~~

+-----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Mattermost Product                            | Export Control Classification Number (ECCN)                                                                                                     |
+===============================================+=================================================================================================================================================+
| Mattermost Enterprise Edition E10             | `ECCN 5D002 <https://www.bis.doc.gov/index.php/documents/regulations-docs/federal-register-notices/federal-register-2014/951-ccl5-pt2/file>`__  |
|                                               | with a License Exception available of `ENC <https://www.bis.doc.gov/index.php/documents/regulation-docs/415-part-740-license-exceptions/file>`__|
+-----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Mattermost Enterprise Edition E20             | `ECCN 5D002 <https://www.bis.doc.gov/index.php/documents/regulations-docs/federal-register-notices/federal-register-2014/951-ccl5-pt2/file>`__  |
|                                               | with a License Exception available of `ENC <https://www.bis.doc.gov/index.php/documents/regulation-docs/415-part-740-license-exceptions/file>`__|
+-----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Mattermost Team Edition                       | Not subject to the U.S. Export Administration Regulations (EAR) given software is publicly available                                            |
|                                               | and fully available to compile from publicly available source code at https://github.com/mattermost/                                            |
+-----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

Overview
~~~~~~~~~

The U.S. government regulates the transfer of information, commodities, technology and software considered
to be strategically important to the U.S. in the interest of national security, economic and/or foreign policy
concerns. Many countries outside of the U.S. have similar controls on exports for the same reasons.

There is a complex network of U.S. agencies and inter-related regulations that govern exports collectively referred
to as “Export Controls."

It is the policy of Mattermost to comply with all export compliance laws in all countries in which it transacts
business. Because Mattermost is a U.S.-based global company, our products, collectively referred to as “Commodities,"
which include our software as well as our equipment, materials and services, are subject to the export laws and regulations
of every country in which we conduct business. Non-compliance with export control regulations can subject Mattermost
and its affiliates, including its customers, employees and business partners to criminal and civil penalties, the seizure
of assets, the denial of export privileges, and suspension or debarment from Government Contracts.

For these reasons, please take the time to familiarize yourself with applicable export (and import) controls in the
jurisdictions in which you operate. Although Mattermost cannot provide advice on export matters, this web page provides the information needed in order export Mattermost products.

This overview is specific to the `U.S. Export Administration Regulations <https://www.bis.doc.gov/index.php/regulations/export-administration-regulations-ear>`__ (EAR), however, business operations may subject you to other regulations such as the `International Traffic in Arms Regulations <https://www.pmddtc.state.gov/regulations_laws?id=ddtc_kb_article_page&sys_id=24d528fddbfc930044f9ff621f961987>`__.

General Information
~~~~~~~~~~~~~~~~~~~~

Start by taking a look at the `U.S. Bureau of Industry and Security <https://www.bis.doc.gov/>`__ website. Then, navigate to `Part 730 <https://www.bis.doc.gov/index.php/documents/regulation-docs/410-part-730-general-information/file>`__ of the U.S. Export Administration Regulations to understand what the regulations cover and what is “Subject to
the EAR” under `734.2 <https://www.bis.doc.gov/index.php/documents/regulation-docs/412-part-734-scope-of-the-export-administration-regulations/file>`__ (“export controlled”).

Export Classification and Licensing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although what is subject to the Export Administration Regulations is quite broad, that does not mean an export license
is required for every transaction. The foundation of understanding export controls related to hardware, software and
technology can be found within the `Commerce Control List <https://www.bis.doc.gov/index.php/regulations/commerce-control-list-ccl>`__ (CCL), which has 10 categories, 0-9, and is set up as a positive list. The first step is determining if the item to be exported is subject to the EAR.

At Mattermost, our Team Edition software is `outside the scope of the EAR <https://www.bis.doc.gov/index.php/policy-guidance/encryption/1-encryption-items-not-subject-to-the-ear>`__, as it is derived from publicly available encryption source code and the complete software package for both the source code (https://github.com/mattermost/) and binary versions are publicly available. Mattermost enterprise software is found in `Category 5, Part 2 <https://www.bis.doc.gov/index.php/documents/regulations-docs/federal-register-notices/federal-register-2014/951-ccl5-pt2/file>`__ of the CCL as Telecommunications and Information Security items (hardware, software and technology). Most items in this category have encryption.

Often a license exception under `Part 740 <https://www.bis.doc.gov/index.php/documents/regulation-docs/415-part-740-license-exceptions/file>`__ is available where a Commerce Control List item lists the available license exception(s) specific to an Export Control Classification Number (ECCN), based on a combination of factors.

Mattermost Enterprise Edition software is found under `ECCN 5D002 <https://www.bis.doc.gov/index.php/documents/regulations-docs/federal-register-notices/federal-register-2014/951-ccl5-pt2/file>`__, with a license exception available from `“ENC” <https://www.bis.doc.gov/index.php/documents/regulation-docs/415-part-740-license-exceptions/file>`__ for our Enterprise and Professional software, with encryption features derived from open-source software. Encryption products, under the export regulations, have multiple levels of controls and requirements. BIS has a separate section of their website that has an overview, and many links, covering encryption under `Policy Guidelines <https://www.bis.doc.gov/index.php/policy-guidance/encryption>`__ that you may want to review. These guidelines include helpful flow charts for determining if an item is subject to encryption controls, tables and other details.

The other key areas to be aware of for an export of Mattermost software or technology are:

**Sanctions**: There are comprehensive sanctions to Cuba, Iran, North Korea, Syria, and other countries/territories.
with specific prohibitions, such as Russia and Venezuela. Details can be
located at `BIS <https://www.bis.doc.gov/index.php/forms-documents/regulations-docs/federal-register-notices/federal-register-2014/1063-746-1/file>`__ and `OFAC <https://www.treasury.gov/resource-center/sanctions/Pages/default.aspx>`__. The countries and their sanctions are subject to change.

**WMD (Weapons of Mass Destruction)**: Mattermost, its customers and its business partners may not export to parties involved
in `proliferation <https://www.bis.doc.gov/index.php/documents/regulation-docs/413-part-736-general-prohibitions/file>`__ of weapons of mass destruction, along with other prohibited end-uses under the U.S. Export Administration Regulations (“EAR”).

**General Prohibitions**: Information on General Prohibitions under the EAR is located `here <https://www.bis.doc.gov/index.php/documents/regulations-docs/413-part-736-general-prohibitions/file>`__. Application of the applicability of these General Prohibitions is based on a combination of factors. These include: classification of the commodity, destination, end-user, end-use and conduct.

**Restricted Parties**: You may not export to parties listed on the US government's `restricted parties lists <https://www.bis.doc.gov/index.php/policy-guidance/lists-of-parties-of-concern>`__, and should be screening against these prior to export. There is a `consolidated screening list <https://www.trade.gov/consolidated-screening-list>`__ provided by the U.S. government at export.gov at no charge that can be used for screening.

**Deemed Exports**:  Release of controlled technology to foreign persons in the U.S. is "deemed" to be an export to the
person’s country or countries of nationality and is found in `734.2(b) <https://www.bis.doc.gov/index.php/documents/regulation-docs/412-part-734-scope-of-the-export-administration-regulations/file>`__ of the EAR, which you can read about under the Export Administration Regulations on the BIS website.

**Know Your Customer**: By reviewing the BIS website, you will notice that it is very important to “know your customers," and to be aware of “Red Flags”. Be sure to screen business partners and customers to ensure compliance.

Disclaimer
~~~~~~~~~~

Mattermost makes this data available for informational purposes only. It may not reflect the most current legal
developments, and Mattermost does not represent, warrant or guarantee that it is complete, accurate or up to date.
This information is subject to change without notice. The materials on this site are not intended to constitute legal
advice or to be used as a substitute for specific legal advice. You should not act (or refrain from acting) based upon
information on this site without obtaining professional advice regarding particular facts and circumstances.

Frequently Asked Questions
--------------------------

To be compliant with GDPR, do I need to remove message contents of email notifications?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Based on our interpretation of GDPR, it is not required to hide message contents in email notifications to remain compliant for the following reasons:

1. Every user has the ability to disable email notifications in **Settings**. Therefore, every user has the ultimate control over whether or not they want information sent via email. This option aligns with most other products, but we will follow updates on interpretations of GDPR closely to see if we need to make changes in this area.
2. Mattermost offers :ref:`TLS encryption <email-tls>` to protect communication between the Mattermost server and the SMTP email server.
3. For those who are uncertain if the first two points cover GDPR compliance, we offer the ability to `disable notifications completely <https://docs.mattermost.com/configure/configuration-settings.html#enable-email-notifications>`__ on your Mattermost server. To use Mattermost in production with no email notifications, you also need to `disable a "preview mode" notice banner <https://docs.mattermost.com/configure/configuration-settings.html#enable-preview-mode-banner>`__.

What information is shared when I click **Contact us** on a Mattermost Admin Advisor notification?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Selecting **Contact us** in the Mattermost Admin Advisor will send some information to us. This may include the email address and name associated with your Mattermost account as well as the number of registered users on your system, the site URL, and a Mattermost diagnostic server ID number. This information is used to contact you as requested and to help us better understand your needs.

.. note::
    `Mattermost Admin Advisor notices are disabled <https://docs.mattermost.com/manage/in-product-notices.html#admin-advisor-notices>`__ in v5.35 and later.

Are the server access logs containing IP addresses a GDPR compliance issue?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Based on our interpretation of `article 49 of GDPR <https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32016R0679&from=EN>`_, processing personal data for the purpose of ensuring network and information security is acceptable. Moreover:

- You can control access to the logs via restricted access to the System Console and the server.
- As a self-hosted software, you have full control and ownership of the logs, with the ability to set up a purge schedule to meet your needs.
- You can use a reverse proxy to provide obfuscation to IP addresses.

Do you have Fed or Department of Defense (DOD) Certification?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are in the process of acquiring Authority to Operate (ATO) and Certificate of Networthiness (CON) certifications.

How do you ensure personal data stays within European Union?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the customer’s installation of Mattermost is self-hosted, Mattermost does not process any personal data under the jurisdiction of the data privacy laws governing within the European Union. The Mattermost support team leverages Zendesk customer service software, which hosts Mattermost information within the United States. For more information on Zendesk, please see their `Privacy and Data Protection <https://www.zendesk.com/company/privacy-and-data-protection/#gdpr-sub>`__ page.

Zendesk privacy and data protection safeguards notwithstanding, the provision of support services is part of the contractual obligations between Mattermost and its customers. In order for Mattermost to provide such support, a customer must be able to identify as a licensed user, therefore requiring the user to provide personal data to the support agent. Regardless of where the support agent is located, the personal data will indeed be hosted outside of the EU.

However, pursuant to Section (b) of Article 49 of GDPR, transfers of personal data which are "necessary for the performance of a contract between the data subject and the controller" may be transferred to a third country or international organization. Accordingly these transfers would be done in alignment with the requirements of GDPR. For more information, see our `Mattermost Privacy Policy <https://mattermost.com/privacy-policy/>`__ page.

***DISCLAIMER:** MATTERMOST DOES NOT POSITION ITS PRODUCTS AS “GUARANTEED COMPLIANCE SOLUTIONS”. WE MAKE NO GUARANTEE THAT YOU WILL ACHIEVE REGULATORY COMPLIANCE USING MATTERMOST PRODUCTS. YOUR LEVEL OF SUCCESS IN ACHIEVING REGULATORY COMPLIANCE DEPENDS ON YOUR INTERPRETATION OF THE APPLICABLE REGULATION, AND THE ACTIONS YOU TAKE TO COMPLY WITH THEIR REQUIREMENTS. SINCE THESE FACTORS DIFFER ACCORDING TO INDIVIDUALS AND BUSINESSES, WE CANNOT GUARANTEE YOUR SUCCESS, NOR ARE WE RESPONSIBLE FOR ANY OF YOUR ACTIONS. NO GUARANTEES ARE MADE THAT YOU WILL ACHIEVE ANY SPECIFIC COMPLIANCE RESULTS FROM THE USE OF MATTERMOST OR FROM ANY RECOMMENDATIONS CONTAINED ON OUR WEBSITES, AND AS SUCH, THIS SHOULD NOT BE A SUBSTITUTE TO CONSULTING WITH YOUR OWN LEGAL AND COMPLIANCE REPRESENTATIVES ON THESE MATTERS.
