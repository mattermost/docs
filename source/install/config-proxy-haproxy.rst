.. config-proxy-haproxy:

Configuring HAProxy as a proxy for Mattermost Server
====================================================

HAProxy is configured using a file in the ``/etc/haproxy/`` directory.  You need to edit the ``haproxy.cfg`` file.  When editing the file, you need the IP address of your Mattermost server and fully qualifed domain (FQDN) of your Mattermost website.

**To configure HAProxy as a proxy**

1. Login in to the server that hosts HAProxy and open a terminal window.
2. Open the file ``/etc/haproxy/haproxy.cfg`` as root in a text editor and add the following lines at the end of the file.  Make sure that you use your own values for the Mattermost server IP address and FQDN for *server_name*.

  .. code-block:: none
  
    frontend www-http
    bind :80
    mode http
    default_backend mattermost
    
    backend mattermost
    mode http
    server 10.10.10.2:8065 check
3. Restart HAProxy

  On Ubuntu 14.04 and RHEL 6.6: ``sudo service haproxy restart``
  
  On Ubuntu 16.04, Debian Jessie, and RHEL 7.1: ``sudo systemctl restart haproxy``
  
4. Verify you can see Mattermost through the proxy.

  ``curl http://localhost``
  
  If everything is working, you will see the HTML for the Mattermost signup page.
  
8. Restrict access to port 8065.
  By default, the Mattermost server accepts connections on port 8065 from every machine on the network. Use your firewall to deny connections on port 8065 to all machines except the machine that hosts HAProxy and the machine that you use to administer Mattermost server. If you're installing on Amazon Web Services, you can use security groups to restrict access.

Now that HAProxy is installed and running, you can configure it to use SSL, which allows you to use HTTPS connections and the HTTP/2 protocol.
