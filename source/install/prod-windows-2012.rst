:orphan:

..  _prod-windows:

Production Install on Windows Server (Unofficial) 
=================================================

Install Mattermost in production mode on one, two or three machines.

.. important:: 

   This unofficial guide is maintained by the Mattermost community and this deployment configuration is not yet officially supported by Mattermost, Inc. `Community testing, feedback and improvements are welcome and greatly appreciated. <https://github.com/mattermost/docs/issues/360>`__
 
.. contents::
  :backlinks: top

Install Windows Server 2012+
----------------------------

1. Set up 3 machines with any edition of Windows Server 2012+ (except core) with 2GB of RAM or more. The
   servers will be used for the Web Proxy and SSL Termination, Mattermost, and Database.  The screenshots 
   used in this guide are from Microsoft Server 2012, but similar steps should work for other versions.

   -  **Optional:** You can also use a single machine for all 3
      components in this install guide, depending on the standards of
      your data center.  In this case, replace all 10.0.0.* IP addresses 
      with a single/common address.

2. Make sure the systems are up to date with the most recent security
   patches by executing Windows Update.

Set up Database Server
----------------------

1.  Log in to the database server. For the purposes of this guide we will assume this server has an IP address of 10.0.0.1.

Install and Configure MySQL
~~~~~~~~~~~~~~~~~~~~~~~~~~~

2. `Download the MySQL 5.6+ <https://dev.mysql.com/downloads/windows/installer/>`__ installer, (or PostgreSQL 10.0+).
   For the purposes of this guide, we'll be downloading and installing the latest version of MySQL Community Server
   Edition MSI-installer (version 5.7 at the time of writing this guide). Note that the appropriate link refers 
   to 32-bit (as shown in the figure below); however, this installer is 32-bit but is capable of installing the 
   64-bit version of MySQL.

3. Launch the installer.

4. On the **License Agreement** page, Check the box to accept the license terms and press Next.

5. On the **Choosing a Setup Type** choose **Custom** so you can decide exactly which packages to install. This 
   is the only place where you can specify whether to install 32-bit or 64-bit MySQL Server.

6. On the **Select Products and Features** page, select the **64bit** version of MySQL Server.

7. On the **Check Requirements** page, install any missing requirements by pressing the Execute button, or go back 
   to the previous page and change the packages that will be installed to remove the requirement. Once all of the 
   requirements are met, press the Next button.

8. On the **Installation** page, you will be shown a list of software that will be installed. Press the Execute 
   button to begin the installation.  Once the installations have completed, press the Next button.

9. On the **Product Configuration** page, press the Next button to begin the MySQL Server Configuration Wizard.

   a. On the **Type and Networking** page, select the appropriate **Config Type** based on your desired usage.
   b. On the **Accounts and Roles** page, enter a MySQL Root password and press the Next button.
   c. On the **Windows Service** page, keep the defaults and press the Next button.
   d. On the **Plugins and Extensions** page, keep the defaults and press the Next button.
   e. On the **Apply Server Configuration** page, press the Execute button to configure the MySQL Server installation.

10. Returning to the **Product Configuration** page, select **Next**.

11. On the **Installation Complete** page, select **Finish**.

Configure Windows PATH
~~~~~~~~~~~~~~~~~~~~~~~

Adding MySQL to the Windows PATH variable will allow you run various commands from the console, and allow third-party applications to execute various MySQL commands.

12. Press the ``WIN + PAUSEBREAK`` key combination to open the **System** Control Panel Applet.

13. Select the **Advanced System Settings** link.

14. Select the **Advanced** tab. 

15. Press the **Environment Variables** button.

16. In the **System Variables** section, select the **Path** variable in the list, then press the Edit button.

17. Append the path to your MySQL Server bin directory (make sure to add a semi-colon after any existing items in the path before appending the new path). The default path for a 64-bit  installation is ``C:\Program Files\MySQL\MySQL Server 5.7\bin``.

Create Mattermost Database
^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that MySQL has been installed and configured, a database and user account must be provisioned for Mattermost to utilize.

18. Open a command prompt and enter ``mysql -u root -p`` to connect to the MySQL server

19. When prompted, enter the password created in step 9.a.       

20. At the ``mysql>`` prompt, execute the following commands to create the database and user account:

    .. code:: sql

       CREATE DATABASE mattermost;
       CREATE USER mmuser IDENTIFIED BY 'mmuser-password';
       GRANT ALL ON mattermost.* TO mmuser;
       exit

21. To confirm the database and user were configured correctly:

    a. Connect to the MySQL server/database by executing ``mysql -u mmuser -p mattermost``.
    b. When prompted, entering ``mmuser-password``.
    c. If If successful, you will be at the ``mysql>`` prompt.
    d. Type ``exit`` to finish.

Set up Mattermost Server
------------------------

1. For the purposes of this guide we will assume this server has an IP address of 10.0.0.2.

2. `Download <https://mattermost.org/download/>`__ the latest Mattermost Server by opening your favorite browser and navigating to ``https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-windows-amd64.zip`` where `X.X.X` is the latest Mattermost release version. For example, 3.4.0.

3. Create the storage directory for files. We assume you will have attached a large drive for storage of images and files. For this setup we will assume the directory is located at ``c:\mattermost\data``. Your directory structure should look similar to the image below.

   .. image:: ../images/windows_1_expected_directory_structure.png

4. Configure Mattermost Server by editing the config.json file at ``c:\mattermost\config\config.json``.
   
   * Update database name and server in the the connection string:
     
     * Old: ``"DataSource": "mmuser:mostest@tcp(dockerhost:3306)/mattermost_test?charset=utf8mb4,utf8"``    
     * New: ``"DataSource": "mmuser:mmuser-password@tcp(10.0.0.1:3306)/mattermost?charset=utf8mb4,utf8"``

   .. note :: Optionally you may continue to edit configuration settings in ``config.json`` or use the 
      System Console described in a later section to finish the configuration.

5. Test the Mattermost server.

   a. Open a command prompt, and execute ``cd c:\mattermost\bin`` to change your working directory

   b. Execute ``mattermost.exe``
   
   c. Verify that mattermost is running and connected to the database successfully by confirmed a console 
      log like ``Server is listening on :8065`` letting you know the service is running.

      .. image:: ../images/windows_2_platform_exe_test.png

   d. Stop the server by pressing CTRL+C
   
Configure the Firewall
~~~~~~~~~~~~~~~~~~~~~~

.. note:: This is not required if you are installing on a single server.

6. Open a command prompt as an administrator

7. Execute the following command to allow inbound traffic to Mattermost

   .. code:: batch

      netsh advfirewall firewall add rule name="Mattermost" dir=in action=allow program="C:\mattermost\bin\mattermost.exe" enable=yes 

Establish a Windows Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Establishing a Windows service to supervise the Mattermost process is recommended to prevent the need to manually start/stop Mattermost. The included binary cannot be directly registered as a Windows service; therefore, a wrapper-utility must be used.

8. Download the latest version of `NSSM (Non-Sucking Service Manager) <https://nssm.cc/download>`__.

9. From the downloaded zip-file, extract ``win64\nssm.exe`` to ``C:\mattermost\bin\``.

10. Open the command line tool as an administrator.

11. To create the Windows service, execute the following:

    .. code:: batch

       cd c:\mattermost\bin
       nssm install mattermost c:\mattermost\bin\mattermost.exe
       nssm set mattermost AppDirectory c:\mattermost

12. Start the service by executing the following

    .. code:: batch

      net start mattermost
      tasklist /FI "IMAGENAME eq mattermost.exe"

Verify Mattermost Connectivity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To verify all steps executed thus far, we'll attempt to access Mattermost through standard HTTP traffic. To perform this step, you'll need access to a client machine with a compatible browser (e.g. Safari, Firefox, Edge, Chrome, etc).

13. From a client workstation meeting the criteria above, launch your favorite web browser.

14. Navigate to ``http://10.0.0.2:8065``.  If successful, you should reach an initialization web-page similar to the screenshot below.

    .. image:: ../images/windows_3_confirm_mattermost_browser.png

15. Assuming your test was successful, close the browser as we'll finish initializing Mattermost later in this guide.

Set up Web Proxy Server
-----------------------

A reverse proxy is recommended in order to provide:

- SSL termination
- HTTP to HTTPS redirection
- Port mapping :80/:443 to :8065
- Standard request logs
- Load balancing (not described in this guide).

Internet Information Server (IIS) for Windows Server is the standard capability provided out-of-the-box that provides this function.  

1. For the purposes of this guide we will assume this server has an IP address of 10.0.0.3.

2. Map a FQDN (fully qualitified domain name), like **mattermost.example.com** to the proxy server (e.g. 10.0.0.2).

Install IIS
~~~~~~~~~~~

3. On the **Start** page, click the **Server Manager** tile, and then select **OK**.

4. In **Server Manager**, select **Dashboard**, and click **Add roles and features**.

5. In the **Add Roles and Features Wizard**, on the **Before you begin** page, select **Next**.

6. On the **Select installation type** page, select Role-based or feature-based installation, and select **Next**.

7. On the **Select destination server** page, select **Select a server from the server pool**, select your server, and choose Next.

8. On the **Select server roles** page, select **Web Server (IIS)**.

9. Expand **Web Server (IIS) > Web Server > Application Development** and select **WebSockets Protocol**, and then select **Next**.

10. On the **Add Roles and Features Wizard** popup dialog, click Add Features, and select **Next**.

11. On the **Select features** page, select **Next**.

12. On the **Web Server Role (IIS)** page, select **Next**.

13. On the **Select role services** page, accept the default selections, and select **Next**.

14. On the **Summary of Features to Install** page, select **Install**.

15. On the Installation progress page, confirm that your installation of the Web Server (IIS) role and required role services completed successfully, and then select **Close**.
 
16. To verify that IIS installed successfully, navigate to ``http://localhost`` in a web browser on the server, and confirm the default IIS Welcome page is displayed.

Configure Reverse Proxy
~~~~~~~~~~~~~~~~~~~~~~~

Reverse proxying involves rewriting an HTTP request and relaying it to a back-end server. IIS does not natively support this; however, Microsoft provides a `URL Rewrite <https://www.iis.net/learn/extensions/url-rewrite-module>`__ module and an `Application Request Routing 
<https://www.iis.net/downloads/microsoft/application-request-routing>`__ module which, when combined, are capable of performing these functions. We'll start by installing these module, and then configure the proxy.

17. `Download <https://go.microsoft.com/fwlink/?LinkID=615137>`__ the URL Rewrite 2.0 x64 module.

18. `Download <https://go.microsoft.com/fwlink/?LinkID=615136>`__ the Application Request Routing 3.0 x64 module.

19. Install the modules (trivial installers with no customizations or options to select).

20. On the **Start** page, click the **Server Manager** tile, and then select **OK**.

21. Expand the **Tools** menu, and select **Information Information Services (IIS) Manager**.

    .. image:: ../images/windows_4_IIS_manager.png

22. In the left-hand navigation tree, expand the server node, expand **Sites**, and select **Default Web Site**.

23. Double-click the URL Rewrite feature, as shown below.

    .. image:: ../images/windows_5_iis_manager_url_rewrite.png

24. In the actions pane (far-right), select **Add Rule(s)...**

25. Select **Reverse Proxy** and select **OK**.

26. If prompted to enable proxy functionality, select **OK**.

27. In the **Add Reverse Proxy Rules** dialog:

    a. Enter ``10.0.0.2:8065`` in the **Enter the server name or IP address where HTTP requests will be forwarded** field.

    b. Ensure the **Enable SSL Offloading** option is checked.

    c. Check **Rewrite the domain names of the links in HTTP responses**.

    d. Enter ``10.0.0.2:8065`` in the **From** field.

    e. Enter ``mattermost.example.com`` in the **To** field.

    f. Select **OK**.

28. At this point, your configuration will relay all incoming traffic from `http://mattermost.example.com` to `http://10.0.0.2:8065/`.  To confirm this, open your favorite browser and attempt to access `http://mattermost.example.com`, and upon success, you'll see the Mattermost initialization screen.

Configure SSL
~~~~~~~~~~~~~

.. note:: 

   SSL communication requires that the web server have a well-formed and trusted certificate. A common freely-available SSL encryption and certificate managemet is Let's Encrypt; however, this service does not formally support the Windows Operating system. A number of third-parties have created clients to support this, and you are free to try out any of them.  This section assumes that you have taken the necessary steps to obtain a web-server certificate that will be trusted by your users.

29. Within the IIS Manager, select the server node in the left-hand connections pane.

30. Double-click the **Server Certificates** option.

31. Select **Import...** from the list of actions on the right-hand-side.

32. Press the ... button to locate your PFX formatted certificate.

33. Enter the password to the certificate file.

34. Select the **Web Hosting** certificate store, and select **OK**.

35. In the left-hand navigation tree, expand the server node, expand **Sites**, and select **Default Web Site**.

36. In the right-hand-side **Actions** pane, select **Bindings...**.

37. Select **Add**,

38. In the **Add Site Binding** dialog, Set the type to **https** and set the **SSL Certificate** to the certificate loaded previously.  Press OK.

Redirect HTTP to HTTPS
~~~~~~~~~~~~~~~~~~~~~~

39. In the left-hand navigation tree, expand the server node, expand **Sites** and select **Default Web Site**.

40. Double-click to open the **Url Rewrite** feature.

41. In the actions-pane (far-right), select **Add Rule(s)..**.

42. Under the **Inbound Rules** section, select **Blank rule** and select **OK**.

43. Populate the fields in the rule to match the screenshot below:

    .. image:: ../images/windows_6_http_to_https_redirect.png   

44. Select **Apply**, and then **Back to Rules**.

45. Ensure that the **HTTP to HTTPS Redirect** rule is at the top of the list of inbound rules. If nceessary, you can select a rule and use the **Move Up** and **Move Down** actions to reorganize.

46. On a client workstation, open your favorite browser and navigate to `http://mattermost.example.com` and confirm that you are redirected to `https://mattermost.example.com`.

Finish Mattermost Server Setup
------------------------------

1. Navigate to ``https://mattermost.example.com`` and create a user and team.

2. The first user in the system is automatically granted the ``system_admin`` role, which gives you access to the System Console.

3. From the ``town-square`` channel select the dropdown next to your team name and choose **System Console**.
   
4. Update **Environment > Web Server** to properly configure your reverse proxy by entering `https://mattermost.example.com` as the **Site URL**.

.. important::
   Failure to properly set the Site URL properly will result in unexpected behavior.

5. Update **Authentication > SMTP** to set up an SMTP email service. The example below assumes AmazonSES.

   a. Set **SMTP Username** to ``[YOUR_SMTP_USERNAME]``.
   b. Set **SMTP Password** to ``[YOUR_SMTP_PASSWORD]``.
   c. Set **SMTP Server** to ``email-smtp.us-east-1.amazonaws.com``.
   d. Set **SMTP Port** to ``465``.
   e. Set **Connection Security** to ``TLS``.
   f. Set **Send Email Notifications** to **true** (located at **Site Configuration > Notifications**).
   g. Set **Notification Display Name** to **No-Reply** (located at **Site Configuration > Notifications**).
   h. Set **Notification From Address** to ``mattermost@example.com`` (located at **Site Configuration > Notifications**).
   i. Set **Require Email Verification** to **true** (located at **Authentication > Email**).

6. (Optional) Update **Authentication > Signup**:

   - Set **Enable Email Invitations** to **true**.

7. Update **Environment > File Storage**:

   - Change **Local Directory Location** from ``./data/`` to ``/mattermost/data``

8. Update **General > Logging** settings:

   - Set **Log to The Console** to **false**.

9. Update **Environment > Rate Limiting** settings:

   - Set **Vary By Remote Address** to **false**.
   - Set **Vary By HTTP Header** to **X-Real-IP**.

10. Feel free to modify other settings.

11. Login to the Mattermost server (10.0.0.2) and restart the Mattermost Service by typing the following into a command line:

   .. code:: batch

      net stop mattermost
      net start mattermost
