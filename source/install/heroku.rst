:orphan:

Mattermost Preview using Heroku
===============================

Quickly set up Mattermost in Preview Mode to explore product functionality using Heroku.

This configuration is not recommended for use in production, as it currently does not support email notifications. Also note that for persistent file storage AmazonS3 must be used, as local storage will be deleted periodically when the Heroku process restarts.

Heroku Installation
--------------------

1. Sign up for a free account on `Heroku <https://www.heroku.com/>`__

2. Click the |HerokuDeploy|_ button

.. |HerokuDeploy| image:: https://www.herokucdn.com/deploy/button.svg
.. _HerokuDeploy: https://heroku.com/deploy?template=https://github.com/mattermost/mattermost-heroku

3. (Optional) Customize the default settings in Heroku

  - ``App Name``: Optionally select a name for your application (this will be used in the app URL)
  - ``Runtime Selection``: Select which region your app should run in (United States or Europe)
  - ``Config Variables``:

    - ``MATTERMOST_DOWNLOAD_URI``: The URI to the compiled Mattermost binary you would like to run. Defaults to current release.
    - ``FILE_SETTINGS__DRIVER_NAME``: Select the type of file storage to use (``local`` or ``amazons3``). AmazonS3 is required for persistent file storage.
    - ``FILE_SETTINGS__AMAZON_S3_ACCESS_KEY_ID``: The access key for your Amazon S3. Only required for driver name `amazons3`.
    - ``FILE_SETTINGS__AMAZON_S3_SECRET_ACCESS_KEY``: The secret access key for your Amazon S3. Only required for driver name amazons3.
    - ``FILE_SETTINGS__AMAZON_S3_BUCKET``: The name you selected for your S3 bucket in AWS. Only required for driver name amazons3.
    - ``FILE_SETTINGS__AMAZON_S3_REGION``: The AWS region you selected when creating your S3 bucket. Refer to `AWS Reference Documentation <https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`__ and choose this variable from the Region column.

4. Click **"Deploy for Free"**


After Heroku finishes setting up the app, click "View" and your Mattermost Preview should be up and running. You will be taken to the account creation page, where you can enter credentials to create an account and get started.
