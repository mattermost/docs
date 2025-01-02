Code signing custom builds
==========================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Code signing is an essential process for ensuring the authenticity and integrity of your custom ``Mattermost`` builds. This guide provides steps on how to code sign a build using your own certificates for Windows, Mac, and Linux.

.. important::

  Make sure to follow each operating system's guidelines and best practices for signing applications.

Prerequisites
-------------

.. tab:: Windows

   1. **Code Signing Certificate**: Obtain a certificate from a Certificate Authority (CA) or use a self-signed certificate if suitable.
   2. **SignTool**: Available as part of the Windows SDK.

.. tab:: Linux

   1. **GPG Key**: Create a GPG key if you don't have one.
   2. **GnuPG**: Install `GnuPG <https://gnupg.org/howtos/card-howto/en/ch02.html>`_ if not already installed.

.. tab:: Mac

   1. **Developer ID Application Certificate**: Obtain from Apple. It requires an `Apple Developer account <https://developer.apple.com/account/>`_.
   2. **Xcode**: Ensure `Xcode <https://developer.apple.com/xcode/>`_ is installed.

Process
-------

.. tab:: Windows

   1. **Install SignTool**
   
      Install the Windows SDK to access the ``SignTool`` utility.

   2. **Obtain a Code Signing Certificate**
      
      Purchase or create a certificate (``.pfx`` file) via a CA.

   3. **Import the Certificate**
      
      Open the ``.pfx`` file and import it into the Windows Certificate Store.

   4. **Sign the Executable**

      - Open the command prompt as Administrator.
      - Use ``SignTool`` to sign your executable:

      .. code-block:: sh

         signtool sign /v /s "My" /sha1 <cert hash> /fd SHA256 /tr http://timestamp.digicert.com /td SHA256 <path-to-your-executable>

.. tab:: Linux

   1. **Create or Import Your GPG Key**

      If you don't have a GPG key, create one:

      .. code-block:: sh

         gpg --full-generate-key

      Import an existing GPG key, if you have one:

      .. code-block:: sh

         gpg --import /path/to/your-key.asc

   2. **Sign the Package**

      Use ``dpkg-sig`` to sign a Debian package:

      .. code-block:: sh

         dpkg-sig --sign builder your-package.deb

      Use ``rpmsign`` to sign an RPM package:

      .. code-block:: sh

         rpmsign --addsign your-package.rpm

   3. **Verify the Signature**

      Verify the signature of a ``.deb`` package:

      .. code-block:: sh

         dpkg-sig --verify your-package.deb

      Verify the signature of an ``.rpm`` package:

      .. code-block:: sh

         rpm --checksig your-package.rpm

.. tab:: Mac

   1. **Obtain a Code Signing Certificate**

      Create a ``Developer ID Application`` certificate in your Apple Developer account and download it.

   2. **Import the Certificate**

      Double-click the certificate to import it into the Keychain.

   3. **Sign the Application**

      Use the ``codesign`` tool from Xcode to sign your application:

      .. code-block:: sh

         codesign --deep --force --verify --verbose --sign "Developer ID Application: Your Name (TeamID)" /path/to/your.app

   4. [Optional] **Verify the Signature**

      Verify the signature to ensure everything is correctly signed:

      .. code-block:: sh

         spctl --assess --verbose=4 /path/to/your.app
         codesign -dv --verbose=4 /path/to/your.app

Summary
-------

- **Windows**: Use ``SignTool`` from the Windows SDK with your imported code signing certificate.
- **Mac**: Use ``codesign`` and ``spctl`` tools from Xcode with your Apple Developer ID certificate.
- **Linux**: Use ``GnuPG`` to create/sign with your GPG key, ``dpkg-sig`` for ``.deb`` packages, and ``rpmsign`` for ``.rpm`` packages.