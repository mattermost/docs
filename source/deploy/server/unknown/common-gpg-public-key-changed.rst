:orphan:
:nosearch:

.. important::

  The GPG public key has changed. You can `import the new public key <https://deb.packages.mattermost.com/pubkey.gpg>`_ or run the automatic Mattermost PPA repository setup script provided below. Depending on your setup, additional steps may also be required, particularly for installations that didn't rely on the repository setup script. We recommend deleting the old key from ``/etc/apt/trusted.gpg.d`` before adding the apt repository.

  - For Ubuntu Focal - 20.04 LTS:

    ``sudo apt-key del A1B31D46F0F3A10B02CF2D44F8F2C31744774B28``

    ``curl -sL -o- https://deb.packages.mattermost.com/pubkey.gpg | gpg --dearmor | sudo apt-key add``

  - For Ubuntu Jammy - 22.04 LTS and Ubuntu Noble - 24.04 LTS:

    ``sudo rm /usr/share/keyrings/mattermost-archive-keyring.gpg``

    ``curl -sL -o- https://deb.packages.mattermost.com/pubkey.gpg |  gpg --dearmor | sudo tee /usr/share/keyrings/mattermost-archive-keyring.gpg > /dev/null``