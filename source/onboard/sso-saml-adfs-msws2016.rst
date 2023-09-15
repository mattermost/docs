Configure SAML with Microsoft ADFS using Microsoft Windows Server 2016
======================================================================

This document provides steps to configure SAML 2.0 with Microsoft ADFS for Mattermost and Microsoft Windows Server 2016.

.. contents:: On this page
  :backlinks: top
  :local:

.. include:: sso-saml-before-you-begin.rst
	  :start-after: :nosearch:

Prerequisites
-------------

- An Active Directory instance where all users have specified email and username attributes. For Mattermost servers running 3.3 and earlier, users must also have their first name and last name attributes specified.
- A running Microsoft Server. The screenshots used in this guide are from Microsoft Server 2012R2, but similar steps should work for other versions.
- An SSL certificate to sign your ADFS login page.
- ADFS installed on your Microsoft Server. You can find a detailed guide for deploying and configuring ADFS in `this article <https://msdn.microsoft.com/en-us/library/gg188612.aspx>`__.

On your ADFS installation, open the ADFS console. Select **Service**, then select **Endpoints**. In the **Type** column, search for ``SAML 2.0/WS-Federation`` and note down the value of **URL Path** column. This is also known as the **SAML SSO URL Endpoint** in this guide. If you chose the defaults for the installation, this will be ``/adfs/ls``.

Add a relying party trust
-------------------------

1. Open the ADFS management snap-in, then select **AD FS > Relying Party Trusts > Add Relying Party Trust** from the right sidebar. You can also right-click **Relying Party Trusts**, then select **Add Relying Party Trust** from the context menu.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_000.png

2. On the **Welcome** screen of the configuration wizard, select **Claims aware**, then select **Start**.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_001.png

3. On the **Select Data Source** screen, select **Enter data about the relying party manually**.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_002.png

4. On the **Specify Display Name** screen, enter a **Display Name** (e.g., ``Mattermost``). You can add optional notes.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_003.png

5. On the **Configure Certificate** screen, leave the certificate settings at their default values.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_004.png

If you would like to set up encryption for your SAML connection, select **Browse**, then upload your Service Provider Public Certificate.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_005.png

6. On the **Configure URL** screen, select **Enable Support for the SAML 2.0 WebSSO protocol**, then enter the **SAML 2.0 SSO service URL** in the following format:``https://<your-mattermost-url>/login/sso/saml`` where ``<your-mattermost-url>`` should typically match the `Mattermost Site URL </configure/configuration-settings.html#site-url>`__.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_006.png

7. On the **Configure Identifiers** screen, enter the **Relying party trust identifier**. This identifies the claims being requested. The **SAML 2.0 SSO service URL** format should be ``https://<your-mattermost-url>/login/sso/saml`` where ``<your-mattermost-url>`` matches your `Mattermost Site URL </configure/configuration-settings.html#site-url>`_. Then choose **Next**. 

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_007.png

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_008.png

This string must match the **Service Provider Identifier** string. For more information about the Relying party trust identifier and how prefix matching is applied see `this documentation <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/technical-reference/how-uris-are-used-in-ad-fs>`_.

Add your **SAML 2.0 SSO service URL** using this same process.

8. On the **Choose Access Control Policy** screen, select the access control policy suitable for your environment. This guide assumes the default values **Permit everyone** and an unchecked box.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_009.png

9. On the **Ready to Add Trust** screen, review your settings.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_010.png

10. On the **Finish** screen, select **Configure claims issuance policy for this application**, then select **Close**.

	.. image:: ../../source/images/SSO-SAML-ADFS_add-new-relying-party-trust_011.png

Create claim rules
------------------

1. In the **Issuance Transform Rules** tab of the **Claim Rules** editor, select **Add Rule…**.

	.. image:: ../../source/images/SSO-SAML-ADFS_create-claim-rules_001.png

2. On the **Choose Rule Type** screen, select **Send LDAP Attributes as Claims** from the drop-down menu, then select **Next**.

	.. image:: ../../source/images/SSO-SAML-ADFS_create-claim-rules_002.png

3. On the **Configure Claim Rule** screen, enter a **Claim Rule Name** of your choice, select **Active Directory** as the **Attribute Store**, then add the following mapping:

  - From the **LDAP Attribute column**, select ``E-Mail-Addresses``. From the **Outgoing Claim Type**, type ``Email``.
  - From the **LDAP Attribute column**, select ``E-Mail-Addresses``. From the **Outgoing Claim Type**, type ``Name ID``.
  - From the **LDAP Attribute column**, select ``Given-Name``. From the **Outgoing Claim Type**, type ``FirstName``.
  - From the **LDAP Attribute column**, select ``Surname``. From the **Outgoing Claim Type**, type ``LastName``.
  - From the **LDAP Attribute column**, select ``SAM-Account-Name``. From the **Outgoing Claim Type**, type ``Username``.

The ``FirstName`` and ``LastName`` attributes are optional.

Select **Finish** to add the rule.

The entries in the **Outgoing Claim Type** column can be modified. The entries may contain dashes but no spaces. They are used to map the corresponding fields in Mattermost.

	.. image:: ../../source/images/SSO-SAML-ADFS_create-claim-rules_003.png

4. Select **Add Rule** to create another new rule.

5. On the **Choose Rule Type** screen, select **Transform an Incoming Claim** from the drop-down menu, then select **Next**.

	.. image:: ../../source/images/SSO-SAML-ADFS_create-claim-rules_004.png

6. On the **Configure Claim Rule** screen, enter a **Claim Rule Name** of your choice, then:

  - Select **Name ID** for the **Incoming claim type**
  - Select **Unspecified** for the **Incoming name ID format**
  - Select **E-Mail Address** for the **Outgoing claim type**

Select **Pass through all claim values**, then select **Finish**.

	.. image:: ../../source/images/SSO-SAML-ADFS_create-claim-rules_005.png

7. Select **Finish** to create the claim rule, then select **OK** to finish creating rules.

8. Open Windows PowerShell as an administrator, then run the following command:

  ``Set-ADFSRelyingPartyTrust -TargetName <display-name> -SamlResponseSignature "MessageAndAssertion"``

where ``<display-name>``is the name you specified in step 4 when you added a relying party trust. In this example, ``<display-name>`` would be ``mattermost``.

This action adds the signature to SAML messages, making verification successful.

Export identity provider certificate
-------------------------------------

Next, export the identity provider certificate, which will be later uploaded to Mattermost to finish SAML configuration.

1. Open the ADFS management snap-in, select **AD FS > Service > Certificates**, then double-click on the certificate under **Token-signing**. You can also right-click the field, then select **View Certificate** in the context menu.

	.. image:: ../../source/images/SSO-SAML-ADFS_export-id-provider-cert_001.png

2. On the **Certificate** screen, open the **Details** tab, select **Copy to File**, then select **OK**.

	.. image:: ../../source/images/SSO-SAML-ADFS_export-id-provider-cert_003.png

3. On the **Certificate Export Wizard** screen, select **Next**.

	.. image:: ../../source/images/SSO-SAML-ADFS_export-id-provider-cert_004.png

4. Select **Base-64 encoded X.509 (.CER)**, then select **Next** again.

	.. image:: ../../source/images/SSO-SAML-ADFS_export-id-provider-cert_005.png

5. On the **Certificate Export Wizard** screen, select **Browse** to specify the location where you want the Identity Provider Certificate to be exported, then specify the file name.

	.. image:: ../../source/images/SSO-SAML-ADFS_export-id-provider-cert_006.png

6. Select **Save**. On the **Certificate Export Wizard** screen, verify the file path is correct, then select **Next**.

7. In the **Completing the Certificate Export Wizard**, select **Finish**, then select **OK** to confirm the export was successful.

	.. image:: ../../source/images/SSO-SAML-ADFS_export-id-provider-cert_007.png

Configure SAML Sign-On for Mattermost
--------------------------------------

Create a metadata URL by appending "FederationMetadata/2007-06/FederationMetadata.xml" to the root URL of the ADFS server, for example: ``https://<adfs.domain.com>/federationmetadata/2007-06/FederationMetadata.xml>``.

Next, start the Mattermost server, then log in to Mattermost as a System Administrator. Go to **System Console > Authentication > SAML**, paste the metadata URL in the **Identity Provider Metadata URL** field, then select **Get SAML Metadata from IdP**.

This populates the **SAML SSO URL** and the **Identity Provider Issuer URL** fields automatically. The Identity Provider Public Certificate is also downloaded from the server and set locally.

The following fields can be selected:
  - Set **Enable Login With SAML 2.0** to **true**.
  - Set **Enable Synchronizing SAML Accounts With AD/LDAP** to suit your environment.
  - Set **Override SAML bind data with AD/LDAP information** to suit your environment.

If you don't plan to use a metadata URL, you can manually enter the following fields:
  - For **SAML SSO URL** use the ``SAML 2.0/W-Federation URL ADFS Endpoint`` you copied at the beginning of the process.
  - For **Identity Provider Issuer URL** use the ``Relying party trust identifier`` from ADFS.
  - For **Identity Provider Public Certificate** use  the``X.509 Public Certificate``.

	.. image:: ../../source/images/SSO-SAML-ADFS_configure-saml_001.png

2. Configure Mattermost to verify the signature.

  - Set **Verify Signature** to ``true``.
  - For **Service Provider Login URL** use the ``SAML 2.0 SSO service URL`` you specified in ADFS.

	.. image:: ../../source/images/SSO-SAML-ADFS_configure-saml_002.png

3. Enable encryption.

  - Set **Enable Encryption** to ``true``.
  - For **Service Provider Private Key** use the Service Provider Private Key generated at the start of this process.
  - For **Service Provider Public Certificate** use the Service Provider Public Certificate you generated at the start of this process.
  - Set **Sign Request** to suit your environment.

	.. image:: ../../source/images/SSO-SAML-ADFS_configure-saml_003.png

4. Set attributes for the SAML Assertions, which will be used to update user information in Mattermost. Attributes for email and username are required and should match the values you entered in ADFS earlier. See :ref:`documentation on SAML configuration settings <saml-enterprise>` for more detail.

For Mattermost servers running 3.3 and earlier, the first name and last name attributes are also required fields.

	.. image:: ../../source/images/SSO-SAML-ADFS_configure-saml_004.png

5. Select **Save**.

6. (Optional) If you configured ``First Name`` Attribute and the ``Last Name`` Attribute, go to **System Console > Site Configuration > Users and Teams**, then set **Teammate Name Display** to **Show first and last name**. This is recommended for a better user experience.

You’re done! If you’d like to confirm SAML SSO is successfully enabled, switch your System Administrator account from email to SAML-based authentication from your profile picture via **Profile > Security > Sign-in Method > Switch to SAML SSO**, then log in with your SAML credentials to complete the switch.

We also recommend that you post an announcement about how the migration will work to your users.

You may also configure SAML for ADFS by editing the ``config.json`` file to enable SAML based on :ref:`SAML configuration settings <saml-enterprise>`. You must restart the Mattermost server for the changes to take effect.

.. include:: sso-saml-faq.rst
	  :start-after: :nosearch:

.. include:: sso-saml-ldapsync.rst
	  :start-after: :nosearch:
