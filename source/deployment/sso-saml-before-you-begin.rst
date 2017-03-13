Before you begin
----------------

Before you configure SAML:

1. Make sure you have the `XML Security Library <https://www.aleksey.com/xmlsec/download.html>`_ installed on your Mattermost instance. The XML Security Library is usually included as part of Debian GNU/Linux.

2. Install the *xmlsec1-openssl* library
 - On Ubuntu: ``sudo apt-get install libxmlsec1-openssl``
 - On RHEL: ``sudo yum install xmlsec1-openssl``

3. Generate encryption certificates for encrypting the SAML connection.
  a. You can use the `Bash script <https://github.com/mattermost/docs/tree/master/source/scripts/generate-certificates>`_ from the *mattermost/docs* repository on GitHub, or any other suitable method.
  b. Save the two files that are generated. They are the private key and the public key. In the System Console, they are referred to as the **Service Provider Private Key** and the **Service Provider Public Certificate** respectively.
