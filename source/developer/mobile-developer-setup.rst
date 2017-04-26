..  _mobile-developer-setup:

Mobile Developer Machine Setup
==================================

The following instructions apply to new unreleased mobile apps for iOS and Android built in React Native. They are intended to release in Beta at the end of March 2017. Source code can be found at: https://github.com/mattermost/mattermost-mobile

.. contents:: Contents:
  :backlinks: top
  :local:

If you run into any issues getting your environment set up, check the Troubleshooting section at the bottom for common solutions.

Development Environment Setup
---------------------------------

Mac OS X
~~~~~~~~~~~~

1. Install `XCode 8.3 <https://developer.apple.com/download/>`_.

2. Install `Homebrew <http://brew.sh/>`_.

3. Using Homebrew, install `Node.js <https://nodejs.org>`_ and npm.

  ``brew install node``

4. Using Homebrew, install `Watchman <https://github.com/facebook/watchman>`_.

  ``brew install watchman``

5. Using npm, install the React Native CLI tools globally.

  ``npm install -g react-native-cli``

6. Using Homebrew or npm install `Yarn <https://yarnpkg.com>`_.

   ``brew install yarn`` or ``npm install -g yarn``

6. Fork `mattermost-mobile <https://github.com/mattermost/mattermost-mobile>`_ on GitHub.

7. Clone your fork locally.

  ``cd`` into the folder that you want to store the local copy of your code

  ``git clone https://github.com/<username>/mattermost-mobile.git``

  ``cd mattermost-mobile``

8. Using npm, download any other dependencies.

  ``make pre-run``

9. *Optional:* Install Mattermost locally so that you can run unit tests and connect to the server while doing development.

  a. Follow the steps in the `Developer Machine Setup <developer-setup.html>`_ to install Mattermost.

  b. Edit your Mattermost instance's configuration file to allow sign-up without an invite.

    In ``config/config.json``, set ``"EnableOpenServer"`` to ``true``

  c. Start/restart your server.

    ``make restart-server``

Test Environment Setup
--------------------------

Android (Device)
~~~~~~~~~~~~~~~~~~~

1. Install the Android SDK (can be skipped if you already have Android Studio installed).

  a. Go to `the Android developer downloads page <https://developer.android.com/studio/index.html#downloads>`_, scroll down to the Get Just the Command Line Tools, and download the zip file suitable for your operating system.

  b. Unzip the SDK to somewhere on your hard drive. For example, ``/Users/<username>/Library/Android/sdk`` on Mac OS X.

  c. Configure the following environment variables:

    - Set ``ANDROID_HOME`` to the location that you unzipped the SDK to.

    - Add ``ANDROID_HOME/tools`` and ``ANDROID_HOME/platform-tools`` to the ``PATH``.

2. Run ``android`` to open the Android SDK Manager and install the following packages:

  - Tools > Android SDK Tools 25.2.5 or higher

  - Tools > Android SDK Platform-tools 25.0.3

  - Tools > Android SDK Build-tools 25.0.2

  - Tools > Android SDK Build-tools 25.0.1

  - Android 6.0 > SDK Platform 23

  - Android 6.0 > Google APIs 23

  - Android 5.1.1 > SDK Platform 22

  - Android 5.1.1 > Google APIs 22

  - Extras > Android Support Repository and/or Androud Support Library
  
  - Extras > Google Play Services
  
  - Extras > Google Repository

3. Connect your Android device to your computer.

4. Enable USB Debugging on your device.

5. Ensure that your device is listed in the output of ``adb devices``.

6. Start the React Native packager to deploy the APK to your device.

  ``make run-android``

7. The installed APK may not be opened automatically. You may need to manually open the Mattermost app on your device.

Troubleshooting
------------------

Errors when running 'make run-android'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Error message
  .. code-block:: none

    React-native-vector-icons: cannot find dependencies

Solution
  Make sure the **Extras > Android Support Repository** package is installed with the Android SDK.

Error message
  .. code-block:: none

    Execution failed for task ':app:packageAllDebugClassesForMultiDex'.
    > java.util.zip.ZipException: duplicate entry: android/support/v7/appcompat/R$anim.class

Solution
  Clean the Android part of the mattermost-mobile project. Issue the following commands:

  1. ``cd android``
  2. ``./gradlew clean``

Error message
  .. code-block:: none

    Execution failed for task ':app:installDebug'.
    > com.android.builder.testing.api.DeviceException: com.android.ddmlib.InstallException: Failed to finalize session : INSTALL_FAILED_UPDATE_INCOMPATIBLE: Package com.mattermost.react.native signatures do not match the previously installed version; ignoring!

Solution
  The development version of the Mattermost app cannot be installed alongside a release version. Open ``android/app/build.gradle`` and change the applicationId from ``"com.mattermost.react.native"`` to a unique string for your app.
