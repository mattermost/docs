Configure SAML with Microsoft ADFS for Windows Server 2012
==========================================================

The following process provides steps to configure SAML 2.0 with Microsoft ADFS for Mattermost.

.. contents::
  :backlinks: top
  :local:

.. include:: sso-saml-before-you-begin.rst

The following are basic requirements to use ADFS for Mattermost:
 - An Active Directory instance where all users have a specified email and username attributes. For Mattermost servers running 3.3 and earlier, users must also have their first name and last name attributes specified.
 - A Microsoft Server running. The screenshots used in this guide are from Microsoft Server 2012R2, but similar steps should work for other versions.
 - An SSL certificate to sign your ADFS login page.
 - ADFS installed on your Microsoft Server. You can find a detailed guide for deploying and configuring ADFS in `this article <https://msdn.microsoft.com/en-us/library/gg188612.aspx>`__.

On your ADFS installation, note down the value of the **SAML 2.0/W-Federation URL** in ADFS Endpoints section, also known as the **SAML SSO URL Endpoint** in this guide. If you chose the defaults for the installation, this will be ``/adfs/ls/``.

Add a Relying Party Trust
-------------------------

1. In ADFS management sidebar, go to **AD FS > Trust Relationships > Relying Party Trusts** and click **Add Relying Party Trust**.

	.. image:: ../../source/images/adfs_1_add_new_relying_party_trust.PNG

2. A configuration wizard for adding a new relying party trust opens. In the **Welcome** screen, click **Start**.

	.. image:: ../../source/images/adfs_2_start_wizard.PNG

3. In the **Select Data Source** screen, select the option **Enter data about the relying party manually**.

	.. image:: ../../source/images/adfs_3_select_data_source.PNG

4. In the **Specify Display Name** screen, enter a **Display Name** to recognize the trust, such as ``Mattermost``, and add any notes you want to make.

	.. image:: ../../source/images/adfs_4_specify_display_name.PNG

5. In the **Choose Profile** screen, select the option **AD FS profile**.

	.. image:: ../../source/images/adfs_5_choose_profile.PNG

6. In the **Configure Certificate** screen, leave the certificate settings at their default values.

	.. image:: ../../source/images/adfs_6_configure_certificate_default.PNG

However, if you would like to set up encryption for your SAML connection, click the **Browse** button and upload your Service Provider Public Certificate.

	.. image:: ../../source/images/adfs_7_configure_certificate_encryption.PNG

7. In the **Configure URL** screen, select **Enable Support for the SAML 2.0 WebSSO protocol** and enter the **SAML 2.0 SSO service URL**, similar to ``https://<your-mattermost-url>/login/sso/saml`` where ``<your-mattermost-url>`` should typically match the `Mattermost Site URL <https://docs.mattermost.com/administration/config-settings.html#site-url>`__.

	.. image:: ../../source/images/adfs_8_configure_url.PNG

8. In the **Configure Identifiers** screen, enter the **Relying party trust identifier** (also known as the **Identity Provider Issuer URL**) of the form ``https://<your-idp-url>/adfs/services/trust`` and click **Add**.

	.. image:: ../../source/images/adfs_9_configure_identifiers.PNG

9. In the **Configure Multi-factor Authentication Now** screen, you may enable multi-factor authentication, but this is beyond the scope of this guide.

	.. image:: ../../source/images/adfs_10_configure_mfa.PNG

10. In the **Choose Issuance Authorization Rules** screen, select the option **Permit all users to access this relying party**.

	.. image:: ../../source/images/adfs_11_authorization.PNG

11. In the **Ready to Add Trust** screen, you can review your settings.

	.. image:: ../../source/images/adfs_12_ready_to_add_trust.PNG

12. In the **Finish** screen, select the option **Open the Edit Claim Rules dialog for this relying party trust when the wizard closes**, and click **Close**. You will now exit configuration wizard and a **Claim Rules** editor opens.

	.. image:: ../../source/images/adfs_13_finish_trust.PNG

Create Claim Rules
------------------

1. In the **Issuance Transform Rules** of the **Claim Rules** editor, click the **Add Rule…** button. This action opens an **Add Transform Claim Rule Wizard**.

	.. image:: ../../source/images/adfs_14_claim_rules_editor.PNG

2. In the **Choose Rule Type** screen, select **Send LDAP Attributes as Claims** from the drop-down menu, then click **Next**.

	.. image:: ../../source/images/adfs_15_choose_rule_type.PNG

3. In the **Configure Claim Rule** screen, enter a **Claim Rule Name** of your choice, select **Active Directory** as the **Attribute Store** and do the following:
  - From the **LDAP Attribute column**, select ``E-Mail-Addresses``. From the **Outgoing Claim Type**, type ``Email``.
  - From the **LDAP Attribute column**, select ``Given-Name``. From the **Outgoing Claim Type**, type ``FirstName``.
  - From the **LDAP Attribute column**, select ``Surname``. From the **Outgoing Claim Type**, type ``LastName``.
  - From the **LDAP Attribute column**, select ``SAM-Account-Name``. From the **Outgoing Claim Type**, type ``Username``.

For Mattermost 3.4 and later, the *FirstName* and *LastName* attributes are optional.

Then, click **Finish** to add the rule.

Note that the entries in the **Outgoing Claim Type** column can be chosen to be something else. They can contain dashes but no spaces. Note that they will be used to map the corresponding fields in Mattermost later.

	.. image:: ../../source/images/adfs_16_configure_claim_rule.PNG

4. Create another new rule by clicking the **Add Rule** button.

5. In the **Choose Rule Type** screen, select **Transform an Incoming Claim** from the drop-down menu, then click **Next**.

	.. image:: ../../source/images/adfs_17_transformation_of_incoming_claim.PNG

6. In the **Configure Claim Rule** screen, enter a **Claim Rule Name** of your choice, then
  - Select *Name ID* for the **Incoming claim type**.
  - Select *Unspecified* for the **Incoming name ID format**.
  - Select *E-Mail Address* for the **Outgoing claim type**.

Moreover, select the **Pass through all claim values** option. Then click **Finish**.

	.. image:: ../../source/images/adfs_18_configure_incoming_claim.PNG

7. Click **Finish** to create the claim rule, then **OK** to finish creating rules.

8. Open Windows PowerShell as an administrator and run the following command:

  ``Set-ADFSRelyingPartyTrust -TargetName <display-name> -SamlResponseSignature "MessageAndAssertion"``

where <display-name> is the name you specified in step 7. In our example it would be ``mattermost``.

This action will add the signature to SAML messages, making verification successful.

Export Identity Provider Certificate
-------------------------------------

Next, we export the identity provider certificate, which will be later uploaded to Mattermost to finish SAML configuration.

1. In ADFS management sidebar, go to **AD FS > Service > Certificates** and double click on the certificate under **Token-signing**. You may alternatively right-click the field, then click **View Certificate**.

	.. image:: ../../source/images/adfs_19_export_idp_cert_start.PNG

2. In the **Certificate** screen, go to the **Details** tab and click **Copy to File**, then **OK**. This opens a **Certificate Export Wizard**.

	.. image:: ../../source/images/adfs_20_export_idp_cert_copy.PNG

3. In the **Certificate Export Wizard** screen, click **Next**. Then, select the option **Base-64 encoded X.509 (.CER)** and click **Next** again.

	.. image:: ../../source/images/adfs_21_export_idp_cert_wizard.PNG

4. In the **Certificate Export Wizard** screen, click **Browse** to specify the location you want the Identity Provider Certificate to be exported, and specify the file name.

	.. image:: ../../source/images/adfs_21-2_export_idp_cert_wizard.PNG

5. Click **Save**. In the **Certificate Export Wizard** screen, verify the file path is correct, and click **Next**.

6. In the **Completing the Certificate Export Wizard**, click **Finish**, then **OK** to confirm the export was successful.

	.. image:: ../../source/images/adfs_21-3_export_idp_cert_wizard.PNG

Configure SAML Sign-in for Mattermost
--------------------------------------

Create a metadata URL by appending "FederationMetadata/2007-06/FederationMetadata.xml" to the root URL of the ADFS server, for example: ``https://<adfs.domain.com>/federationmetadata/2007-06/FederationMetadata.xml>``.

Next, start Mattermost server and sign into Mattermost as a System Administrator. Go to **System Console > Authentication > SAML**, paste the metadata URL in the **Identity Provider Metadata URL** field, and then select **Get SAML Metadata from IdP**.

This populates the **SAML SSO URL** and the **Identity Provider Issuer URL** fields automatically and the Identity Provider Public Certificate is also downloaded from the server and set locally.

Alternatively you can enter the following fields manually:
  - **SAML SSO URL**: **SAML 2.0/W-Federation URL** ADFS Endpoint you copied earlier.
  - **Identity Provider Issuer URL**: ``Relying party trust identifier`` from ADFS you specified earlier.
  - **Identity Provider Public Certificate**: ``X.509 Public Certificate`` you downloaded earlier.

	.. image:: ../../source/images/adfs_22_mattermost_basics.PNG

2. Configure Mattermost to verify the signature. The **Service Provider Login URL** is the SAML 2.0 SSO service URL you specified in ADFS earlier.

	.. image:: ../../source/images/adfs_23_mattermost_verification.PNG

3. Enable encryption by uploading the Service Provider Private Key and Service Provider Public Certificate you generated earlier.

	.. image:: ../../source/images/adfs_24_mattermost_encryption.PNG

4. Configure Mattermost to sign SAML requests using the Service Provider Private Key.

5. Set attributes for the SAML Assertions, which will be used to update user information in Mattermost. Attributes for email and username are required and should match the values you entered in ADFS earlier. See :ref:`documentation on SAML configuration settings <saml-enterprise>` for more detail.

For Mattermost servers running 3.3 and earlier, the first name and last name attributes are also required fields.

	.. image:: ../../source/images/adfs_25_mattermost_attributes.PNG

6. (Optional) Customize the login button text.

  .. image:: ../../source/images/adfs_26_mattermost_login_button.PNG

7. Click **Save**.

8. (Optional) If you configured First Name Attribute and Last Name Attribute, go to **System Console > Site Configuration > Users and Teams** (or **System Console > General > Users and Teams** in versions prior to 5.12) and set **Teammate Name Display** to **Show first and last name**. This is recommended for a better user experience.

If you’d like to confirm SAML SSO is successfully enabled, switch your System Administrator account from email to SAML-based authentication via **Account Settings > General > Sign-in Method > Switch to SAML SSO** and sign in with your SAML credentials to complete the switch.

It's also recommended to post an announcement about how the migration will work to users.

You may also configure SAML for ADFS by editing ``config.json`` to enable SAML based on :ref:`SAML configuration settings <saml-enterprise>`. You must restart the Mattermost server for the changes to take effect.

.. include:: sso-saml-ldapsync.rst

.. include:: sso-saml-faq.rst
