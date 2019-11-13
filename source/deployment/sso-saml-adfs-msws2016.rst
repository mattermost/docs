Configure SAML with Microsoft ADFS using Microsoft Windows Server 2016
======================================================================

This document provides steps to configure SAML 2.0 with Microsoft ADFS for Mattermost and Microsoft Windows Server 2016.

.. contents::
  :backlinks: top
  :local:

.. include:: sso-saml-before-you-begin.rst

## Prerequisites
 - An Active Directory instance where all users have specified email and username attributes. For Mattermost servers running 3.3 and earlier, users must also have their first name and last name attributes specified.
 - A running Microsoft Server. The screenshots used in this guide are from Microsoft Server 2012R2, but similar steps should work for other versions.
 - An SSL certificate to sign your ADFS login page.
 - ADFS installed on your Microsoft Server. You can find a detailed guide for deploying and configuring ADFS in `this article <https://msdn.microsoft.com/en-us/library/gg188612.aspx>`__.

On your ADFS installation, note down the value of the **SAML 2.0/W-Federation URL** in ADFS Endpoints section, also known as the **SAML SSO URL Endpoint** in this guide. If you chose the defaults for the installation, this will be ``/adfs/ls/``.

Add a Relying Party Trust
-------------------------

1. Open the ADFS management snap-in and select **AD FS > Relying Party Trusts > Add Relying Party Trust** on the right sidebar. You can also right-click **Relying Party Trusts** and choose **Add Relying Party Trust** from the context menu.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_000.png

2. In the **Welcome** screen of the configuration wizard choose **Claims aware** and select **Start**.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_001.png

3. In the **Select Data Source** screen, choose **Enter data about the relying party manually**.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_002.png

4. In the **Specify Display Name** screen enter a **Display Name** (e.g., ``Mattermost``). You can add optional notes.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_003.png

5. In the **Configure Certificate** screen, leave the certificate settings at their default values.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_004.png

However, if you would like to set up encryption for your SAML connection, click the **Browse** button and upload your Service Provider Public Certificate.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_005.png

6. In the **Configure URL** screen, select the option **Enable Support for the SAML 2.0 WebSSO protocol** and enter the **SAML 2.0 SSO service URL**, which is of the form ``https://<your-mattermost-url>/login/sso/saml`` where ``https://<your-mattermost-url>`` should typically match the `Mattermost Site URL <https://docs.mattermost.com/administration/config-settings.html#site-url>`__.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_006.png

7. In the **Configure Identifiers** screen, enter the **Relying party trust identifier** (also known as the **Identity Provider Issuer URL**) of the form ``https://<your-idp-url>/adfs/services/trust`` and click **Add**.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_007.png

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_008.png

Add your **SAML 2.0 SSO service URL** from above the same way.

8. In the **Choose Access Control Policy** screen select the access control policy suitable for your environment. This guide assumes the default values **Permit everyone** and an unchecked box are kept.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_009.png

9. In the **Ready to Add Trust** screen, you can review your settings.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_010.png

10. In the **Finish** screen, select the option **Configure claims issuance policy for this application**, and click **Close**. 

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_011.png

	You will now exit the configuration wizard and a **Claim Rules** editor opens.

Create Claim Rules
------------------

1. In the **Issuance Transform Rules** tab of the **Claim Rules** editor, click the **Add Rule…** button.

	.. image:: ../../source/images/SSO-SAML-ADFS_create-claim-rules_001.png

	This action opens an **Add Transform Claim Rule Wizard**.

2. In the **Choose Rule Type** screen, select **Send LDAP Attributes as Claims** from the drop-down menu, then click **Next**.

	.. image:: ../../source/images/SSO-SAML-ADFS_create-claim-rules_002.png

3. In the **Configure Claim Rule** screen, enter a **Claim Rule Name** of your choice, select **Active Directory** as the **Attribute Store** and add the following mapping:
  - From the LDAP Attribute column, **select** ``E-Mail-Addresses``. From the Outgoing Claim Type, **type** ``Email``
  - From the LDAP Attribute column, **select** ``Given-Name``. From the Outgoing Claim Type, **type** ``FirstName``
  - From the LDAP Attribute column, **select** ``Surname``. From the Outgoing Claim Type, **type** ``LastName``
  - From the LDAP Attribute column, **select** ``SAM-Account-Name``. From the Outgoing Claim Type, **type** ``Username``

For Mattermost 3.4 and later, the *FirstName* and *LastName* attributes are optional.

Then, click **Finish** to add the rule.

Note that the entries in the **Outgoing Claim Type** column can be chosen to be something else. They can contain dashes but no spaces. Note that they will be used to map the corresponding fields in Mattermost later.

	.. image:: ../../source/images/SSO-SAML-ADFS_create-claim-rules_003.png

4. Create another new rule by clicking the **Add Rule** button.

5. In the **Choose Rule Type** screen, select **Transform an Incoming Claim** from the drop-down menu, then click **Next**.

	.. image:: ../../source/images/SSO-SAML-ADFS_create-claim-rules_004.png

6. In the **Configure Claim Rule** screen, enter a **Claim Rule Name** of your choice, then
  - Select *Name ID* for the **Incoming claim type**
  - Select *Unspecified* for the **Incoming name ID format**
  - Select *E-Mail Address* for the **Outgoing claim type**

Moreover, select the **Pass through all claim values** option. Then click **Finish**.

	.. image:: ../../source/images/SSO-SAML-ADFS_create-claim-rules_005.png

7. Click **Finish** to create the claim rule, then **OK** to finish creating rules.

8. Open Windows PowerShell as an administrator and run the following command:

  ``Set-ADFSRelyingPartyTrust -TargetName <display-name> -SamlResponseSignature "MessageAndAssertion"``

where <display-name> is the name you specified in step 6. In our example it would be ``mattermost``.

This action will add the signature to SAML messages, making verification successful.

Export Identity Provider Certificate
-------------------------------------

Next, we export the identity provider certificate, which will be later uploaded to Mattermost to finish SAML configuration.

1. Open the ADFS management snap-in, select **AD FS > Service > Certificates** and double click on the certificate under **Token-signing**. You can also right-click the field, then click **View Certificate** in the context menu.

	.. image:: ../../source/images/SSO-SAML-ADFS_export-id-provider-cert_001.png

2. In the **Certificate** screen, go to the **Details** tab and click **Copy to File**, then **OK**.

	.. image:: ../../source/images/SSO-SAML-ADFS_export-id-provider-cert_003.png

	This opens the **Certificate Export Wizard**.

3. In the **Certificate Export Wizard** screen, click **Next**.

	.. image:: ../../source/images/SSO-SAML-ADFS_export-id-provider-cert_004.png

	Then, select the option **Base-64 encoded X.509 (.CER)** and click **Next** again.

	.. image:: ../../source/images/SSO-SAML-ADFS_export-id-provider-cert_005.png

4. In the **Certificate Export Wizard** screen, click **Browse** to specify the location you want the Identity Provider Certificate to be exported, and specify the file name.

	.. image:: ../../source/images/SSO-SAML-ADFS_export-id-provider-cert_006.png

5. Click **Save**. In the **Certificate Export Wizard** screen, verify the file path is correct, and click **Next**.

6. In the **Completing the Certificate Export Wizard**, click **Finish**, then **OK** to confirm the export was successful.

	.. image:: ../../source/images/SSO-SAML-ADFS_export-id-provider-cert_007.png

You’re now about to finish configuring SAML for Mattermost!

Configure SAML sign-in for Mattermost
--------------------------------------

1. Start Mattermost server and sign into Mattermost as a System Administrator. Go to **System Console > Authentication > SAML**.
  - Set *Enable Login With SAML 2.0* to *true*.
  - Set *Enable Synchronizing SAML Accounts With AD/LDAP* to suit your environment.
  - Set *Override SAML bind data with AD/LDAP information* to suit your environment.
  - For *SAML SSO URL* use ``SAML 2.0/W-Federation URL ADFS Endpoint`` you copied earlier.
  - For Identity Provider Issuer URL* use ``Relying party trust identifier`` from ADFS you specified earlier.
  - For *Identity Provider Public Certificate* use ``X.509 Public Certificate`` you downloaded earlier.

	.. image:: ../../source/images/SSO-SAML-ADFS_configure-saml_001.png

2. Configure Mattermost to verify the signature. 
  - Set *Verify Signature* to *true*.
  - For *Service Provider Login URL* use the ``SAML 2.0 SSO service URL`` you specified in ADFS earlier.

	.. image:: ../../source/images/SSO-SAML-ADFS_configure-saml_002.png

3. Enable encryption.
  - Set *Enable Encryption* to *true*.
  - For *Service Provider Private Key* use the Service Provider Private Key you generated at the beginning.
  - For *Service Provider Public Certificate* use the Service Provider Public Certificate you generated at the beginning.
  - Set *Sign Request* to suit your environment.

	.. image:: ../../source/images/SSO-SAML-ADFS_configure-saml_003.png

4. Set attributes for the SAML Assertions, which will be used to update user information in Mattermost. Attributes for email and username are required and should match the values you entered in ADFS earlier. See :ref:`documentation on SAML configuration settings <saml-enterprise>` for more detail.

For Mattermost servers running 3.3 and earlier, the first name and last name attributes are also required fields.

	.. image:: ../../source/images/SSO-SAML-ADFS_configure-saml_004.png

5. Click **Save**.

6. (Optional) If you configured First Name Attribute and Last Name Attribute, go to **System Console > General > Users and Teams** in prior versions or **System Console** > **Site Configuration** > **Users and Teams** in versions after 5.12 and set **Teammate Name Display** to *Show first and last name*. This is recommended for a better user experience.


You’re done! If you’d like to confirm SAML SSO is successfully enabled, switch your System Administrator account from email to SAML-based authentication via **Account Settings > General > Sign-in Method > Switch to SAML SSO** and sign in with your SAML credentials to complete the switch.

It is also recommended to post an announcement about how the migration will work to users.

You may also configure SAML for ADFS by editing ``config.json`` to enable SAML based on :ref:`SAML configuration settings <saml-enterprise>`. You must restart the Mattermost server for the changes to take effect.

.. include:: sso-saml-faq.rst

.. include:: sso-saml-ldapsync.rst

.. include:: sso-saml-troubleshooting.rst
