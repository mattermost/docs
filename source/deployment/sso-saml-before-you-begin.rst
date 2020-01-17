Before You Begin
----------------

Starting with version 5.20, a new SAML library implementation is available. This implementation does not require the installation of the XML Security Library. It is recommended that you use this new implementation as the old implementation will eventually be deprecated.

To use the new implementation, navigate to **System Console > Experimental Features > Use Improved SAML Library**. Activate the feature and choose **Save** and then restart the server. The configuration change will not take effect until the server is restarted.

To change the configuration file directly, edit the “UseNewSamlLibrary” setting under “ExperimentalSettings”. 

To use the existing implementation:

1. Make sure you have the `XML Security Library <https://www.aleksey.com/xmlsec/download.html>`__ installed on your Mattermost instance. The XML Security Library is usually included as part of Debian GNU/Linux.

2. Install the *xmlsec1-openssl* library
 - On Ubuntu: ``sudo apt-get install xmlsec1``
 - On RHEL: ``sudo yum install xmlsec1-openssl``

3. Generate encryption certificates for encrypting the SAML connection.
  a. You can use the `Bash script <https://github.com/mattermost/docs/tree/master/source/scripts/generate-certificates>`__ from the *mattermost/docs* repository on GitHub, or any other suitable method.
  b. Save the two files that are generated. They are the private key and the public key. In the System Console, they are referred to as the **Service Provider Private Key** and the **Service Provider Public Certificate** respectively.
