.. meta::
   :name: robots
   :content: noindex

:orphan:
:nosearch:

You can deploy Mattermost server in **Preview Mode** on AWS Elastic Beanstalk using a Docker container. This is a great option for exploring functionality, testing, and development purposes, as it allows you to quickly set up a Mattermost instance without needing to manage the underlying infrastructure. This deployment method shouldn't be used in production environments.

The Elastic Beanstalk application creation process below combines Application and Environment creation in a single workflow:

1.  From your `AWS console <https://console.aws.amazon.com/console/home>`__ select **Elastic Beanstalk**.
2.  Select the **Create Application** button on the Elastic Beanstalk home page.
3.  Enter an **Application name** for the Elastic Beanstalk application.
4.  (Optional) Specify **Application tags**.
5.  Select **Docker** for the Platform.
6.  Choose **Docker running on 64bit Amazon Linux 2** for the **Platform** branch. Note that multi-container Docker is now deprecated.
7.  Leave the platform version preselected as **3.4.8 (Recommended)**.
8.  For **Application code**, select **Upload your code**.
9.  Download the ``Dockerrun.aws.json`` file from
    https://raw.githubusercontent.com/mattermost/mattermost-docker-preview/master/Dockerrun.aws.json.
10.  Set a unique **Version Label**, choose **Local File**, then select **Choose file** button to browse for the downloaded file in the previous step. You should see a **File successfully uploaded** message.
11. Select **Create Application**. It may take a few minutes for Beanstalk to launch your environment. If the launch is successful, you will see a see a large green checkmark and the **Health status** displayed in green.
12. Test your environment by selecting the domain link next to your application name at the top of the dashboard. Alternatively, enter the domain into your browser in the form of ``http://<your-ebs-application-url>.elasticbeanstalk.com``. You can also map your own domain if you prefer. When everything is working correctly, the domain navigates you to the Mattermost Login page. Enjoy exploring Mattermost!

Enable Email (Recommended)
-----------------------------

The default Docker instance for Mattermost is designed for product evaluation, and sets ``SendEmailNotifications=false`` so the product can function without enabling email. To see the product's full functionality, we recommend :doc:`enabling SMTP email </administration-guide/configure/smtp-email>`.

See :doc:`Configuration Settings </administration-guide/configure/configuration-settings>` documentation for more configuration and customization options for your deployment.