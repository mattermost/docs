Configure SAML with Microsoft ADFS for Windows Server 2012
==========================================================

The following process provides steps to configure SAML 2.0 with Microsoft ADFS for Mattermost.

.. contents:: On this page
  :backlinks: top
  :local:

.. include:: sso-saml-before-you-begin.rst
	:start-after: :nosearch:

The following are basic requirements to use ADFS for Mattermost:
 - An Active Directory instance where all users have a specified email and username attributes. For Mattermost servers running 3.3 and earlier, users must also have their first name and last name attributes specified.
 - A Microsoft Server running. The screenshots used in this guide are from Microsoft Server 2012R2, but similar steps should work for other versions.
 - An SSL certificate to sign your ADFS login page.
 - ADFS installed on your Microsoft Server. You can find a detailed guide for deploying and configuring ADFS in `this article <https://msdn.microsoft.com/en-us/library/gg188612.aspx>`__.

On your ADFS installation, note down the value of the **SAML 2.0/W-Federation URL** in ADFS Endpoints section, also known as the **SAML SSO URL Endpoint** in this guide. If you chose the defaults for the installation, this will be ``/adfs/ls/``.

Add a relying party trust
-------------------------

1. In the ADFS management sidebar, go to **AD FS > Trust Relationships > Relying Party Trusts**, then select **Add Relying Party Trust**. A configuration wizard opens for adding a new relying party trust. 

	.. image:: ../../source/images/adfs_1_add_new_relying_party_trust.png

2. On the **Welcome** screen, select **Start**.

	.. image:: ../../source/images/adfs_2_start_wizard.png

3. On the **Select Data Source** screen, select **Enter data about the relying party manually**.

	.. image:: ../../source/images/adfs_3_select_data_source.png

4. On the **Specify Display Name** screen, enter a **Display Name** to recognize the trust, such as ``Mattermost``, then add any notes you want to make.

	.. image:: ../../source/images/adfs_4_specify_display_name.png

5. On the **Choose Profile** screen, select **AD FS profile**.

	.. image:: ../../source/images/adfs_5_choose_profile.png

6. On the **Configure Certificate** screen, leave the certificate settings at their default values.

	.. image:: ../../source/images/adfs_6_configure_certificate_default.png

However, if you would like to set up encryption for your SAML connection, select **Browse**, then upload your Service Provider Public Certificate.

	.. image:: ../../source/images/adfs_7_configure_certificate_encryption.png

7. On the **Configure URL** screen, select **Enable Support for the SAML 2.0 WebSSO protocol**, then enter the **SAML 2.0 SSO service URL**, similar to ``https://<your-mattermost-url>/login/sso/saml`` where ``<your-mattermost-url>`` should typically match the `Mattermost Site URL </configure/configuration-settings.html#site-url>`__.

	.. image:: ../../source/images/adfs_8_configure_url.png

8. On the **Configure Identifiers** screen, enter the **Relying party trust identifier** (also known as the **Identity Provider Issuer URL**) of the form ``https://<your-idp-url>/adfs/services/trust``, then click **Add**.

	.. image:: ../../source/images/adfs_9_configure_identifiers.png

9. On the **Configure Multi-factor Authentication Now** screen, you may enable multi-factor authentication. This is beyond the scope of this documentation.

	.. image:: ../../source/images/adfs_10_configure_mfa.png

10. On the **Choose Issuance Authorization Rules** screen, select **Permit all users to access this relying party**.

	.. image:: ../../source/images/adfs_11_authorization.png

11. On the **Ready to Add Trust** screen, review your settings.

	.. image:: ../../source/images/adfs_12_ready_to_add_trust.png

12. On the **Finish** screen, select **Open the Edit Claim Rules dialog for this relying party trust when the wizard closes**, then select **Close**. You exit the configuration wizard, and a **Claim Rules** editor opens.

	.. image:: ../../source/images/adfs_13_finish_trust.png

Create claim rules
------------------

1. In the **Issuance Transform Rules** section of the **Claim Rules** editor, select **Add Rule…** to open an **Add Transform Claim Rule Wizard**.

	.. image:: ../../source/images/adfs_14_claim_rules_editor.png

2. On the **Choose Rule Type** screen, select **Send LDAP Attributes as Claims** from the drop-down menu, then select **Next**.

	.. image:: ../../source/images/adfs_15_choose_rule_type.png

3. In the **Configure Claim Rule** screen, enter a **Claim Rule Name** of your choice, select **Active Directory** as the **Attribute Store**, then complete the following:

  - From the **LDAP Attribute column**, select ``E-Mail-Addresses``. From the **Outgoing Claim Type**, type ``Email``.
  - From the **LDAP Attribute column**, select ``E-Mail-Addresses``. From the **Outgoing Claim Type**, type ``Name ID``.
  - From the **LDAP Attribute column**, select ``Given-Name``. From the **Outgoing Claim Type**, type ``FirstName``.
  - From the **LDAP Attribute column**, select ``Surname``. From the **Outgoing Claim Type**, type ``LastName``.
  - From the **LDAP Attribute column**, select ``SAM-Account-Name``. From the **Outgoing Claim Type**, type ``Username``.

The ``FirstName`` and ``LastName`` attributes are optional.

Select **Finish** to add the rule.

Note that the entries in the **Outgoing Claim Type** column can be chosen to be something else. They can contain dashes but no spaces. They will be used to map the corresponding fields in Mattermost later.

	.. image:: ../../source/images/adfs_16_configure_claim_rule.png

4. Create another new rule by selecting **Add Rule**.

5. On the **Choose Rule Type** screen, select **Transform an Incoming Claim** from the drop-down menu, then select **Next**.

	.. image:: ../../source/images/adfs_17_transformation_of_incoming_claim.png

6. On the **Configure Claim Rule** screen, enter a **Claim Rule Name** of your choice, then:

  - Select **Name ID** for the **Incoming claim type**.
  - Select **Unspecified** for the **Incoming name ID format**.
  - Select **E-Mail Address** for the **Outgoing claim type**.

Select **Pass through all claim values**, then select **Finish**.

	.. image:: ../../source/images/adfs_18_configure_incoming_claim.png

7. Select **Finish** to create the claim rule, then select **OK** to finish creating rules.

8. Open Windows PowerShell as an administrator, then run the following command:

  ``Set-ADFSRelyingPartyTrust -TargetName <display-name> -SamlResponseSignature "MessageAndAssertion"``

where ``<display-name>`` is the name you specified in step 4 when adding a relying party trust. In this example, ``<display-name>`` would be ``mattermost``.

This action adds the signature to SAML messages, making verification successful.

Export identity provider certificate
-------------------------------------

Next, export the identity provider certificate, which will be later uploaded to Mattermost to finish SAML configuration.

1. In the ADFS management sidebar, go to **AD FS > Service > Certificates**, then double click on the certificate under **Token-signing**. Alternatively, you can right-click on the field, then select **View Certificate**.

	.. image:: ../../source/images/adfs_19_export_idp_cert_start.png

2. On the **Certificate** screen, go to the **Details** tab, then select **Copy to File**, followed by **OK**. This opens a **Certificate Export Wizard**.

	.. image:: ../../source/images/adfs_20_export_idp_cert_copy.png

3. On the **Certificate Export Wizard** screen, select **Next**, then, select the option **Base-64 encoded X.509 (.CER)**, and select **Next** again.

	.. image:: ../../source/images/adfs_21_export_idp_cert_wizard.png

4. On the **Certificate Export Wizard** screen, select **Browse** to specify the location where you want the Identity Provider Certificate to be exported, then specify the file name.

	.. image:: ../../source/images/adfs_21-2_export_idp_cert_wizard.png

5. Select **Save**. In the **Certificate Export Wizard** screen, verify the file path is correct, then select **Next**.

6. In the **Completing the Certificate Export Wizard**, select **Finish**, then select **OK** to confirm the export was successful.

	.. image:: ../../source/images/adfs_21-3_export_idp_cert_wizard.png

Configure SAML Sign-On for Mattermost
--------------------------------------

Create a metadata URL by appending "FederationMetadata/2007-06/FederationMetadata.xml" to the root URL of the ADFS server, for example: ``https://<adfs.domain.com>/federationmetadata/2007-06/FederationMetadata.xml>``.

Next, start the Mattermost server and log in to Mattermost as a System Administrator. Go to **System Console > Authentication > SAML**, paste the metadata URL in the **Identity Provider Metadata URL** field, then select **Get SAML Metadata from IdP**.

This populates the **SAML SSO URL** and the **Identity Provider Issuer URL** fields automatically. The Identity Provider Public Certificate is also downloaded from the server and set locally.

Alternatively you can enter the following fields manually:
  - **SAML SSO URL**: **SAML 2.0/W-Federation URL** ADFS Endpoint you copied earlier.
  - **Identity Provider Issuer URL**: ``Relying party trust identifier`` from ADFS you specified earlier.
  - **Identity Provider Public Certificate**: ``X.509 Public Certificate`` you downloaded earlier.

	.. image:: ../../source/images/adfs_22_mattermost_basics.png

2. Configure Mattermost to verify the signature. The **Service Provider Login URL** is the SAML 2.0 SSO service URL you specified in ADFS earlier.

	.. image:: ../../source/images/adfs_23_mattermost_verification.png

3. Enable encryption by uploading the Service Provider Private Key and Service Provider Public Certificate you generated earlier.

	.. image:: ../../source/images/adfs_24_mattermost_encryption.png

4. Configure Mattermost to sign SAML requests using the Service Provider Private Key.

5. Set attributes for the SAML Assertions, which will be used to update user information in Mattermost. Attributes for email and username are required and should match the values you entered in ADFS earlier. See :ref:`documentation on SAML configuration settings <saml-enterprise>` for more detail.

For Mattermost servers running 3.3 and earlier, the ``FirstName`` and ``LastName`` attributes are also required fields.

	.. image:: ../../source/images/adfs_25_mattermost_attributes.png

6. (Optional) Customize the login button text.

  .. image:: ../../source/images/adfs_26_mattermost_login_button.png

7. Select **Save**.

8. (Optional) If you configured a ``FirstName`` and ``LastName`` Attribute, go to **System Console > Site Configuration > Users and Teams**, then set **Teammate Name Display** to **Show first and last name**. This is recommended for a better user experience.

If you’d like to confirm SAML SSO is successfully enabled, switch your System Administrator account from email to SAML-based authentication from your profile picture via **Profile > Security > Sign-in Method > Switch to SAML SSO**, then log in with your SAML credentials to complete the switch.

We recommend that you post an announcement about how the migration will work for your users.

You may also configure SAML for ADFS by editing the ``config.json`` file to enable SAML based on :ref:`SAML configuration settings <saml-enterprise>`. You must restart the Mattermost server for the changes to take effect.

.. include:: sso-saml-ldapsync.rst
	:start-after: :nosearch:

.. include:: sso-saml-faq.rst
	:start-after: :nosearch:
