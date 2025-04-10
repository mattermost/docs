Deploy Mattermost using Containers
==================================

You can deploy Mattermost Server using container technologies for exploring functionality, testing, and development purposes, as it allows you to quickly set up a Mattermost instance without needing to manage the underlying infrastructure. 
This deployment method shouldn't be used in production environments as it doesn't support clustered deployments or High Availability (HA) configurations out-of-the-box.

Choose your preferred container platform below for specific deployment instructions:

.. tab:: Docker

  .. include:: containers/install-docker.rst
    :start-after: :nosearch:

.. tab:: AWS Elastic Beanstalk

  .. include:: containers/install-aws-beanstalk.rst
    :start-after: :nosearch:

Secure your Mattermost deployment
---------------------------------

Deploying Mattermost using Docker containers can be made secure with proper configurations for HTTPS and reverse proxying. 
This guide outlines the steps to set up TLS and an NGINX reverse proxy for your Mattermost deployment, ensuring secure communication between users and your server.

1. Set Up an NGINX Container to serve as the reverse proxy. You can use NGINX either as a separate container or installed on the host machine.
2. Bind Volumes for NGINX Configuration and TLS Certificates:

  - Bind Docker volumes for NGINX configuration files and TLS certificates to ensure persistent and secure storage of these assets.
  - Use permission restrictions on host directories where sensitive files such as TLS keys are stored.

3. Create the NGINX Configuration File by designing a robust ``nginx.conf`` file to configure reverse proxying and HTTPS. Here's a basic example:

   .. code-block:: nginx

      server {
          listen 443 ssl;
          server_name your-domain.com;
          
          ssl_certificate /etc/nginx/certs/fullchain.pem;
          ssl_certificate_key /etc/nginx/certs/privkey.pem;

          ssl_protocols TLSv1.2 TLSv1.3;
          ssl_ciphers HIGH:!aNULL:!MD5;

          location / {
              proxy_pass http://mattermost:8065;
              proxy_set_header Host $host;
              proxy_set_header X-Real-IP $remote_addr;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
              proxy_set_header X-Forwarded-Proto https;
          }
      }

Verify the configuration with ``nginx -t`` before applying.

4. Obtain TLS Certificates:

  - Use Let's Encrypt for free, automated certificates. Tools like Certbot can help automate the process.
  - Alternatively, purchase certificates from a trusted certificate authority (CA) and ensure proper setup of intermediate and root certificate chains.

  Keep private keys secure and avoid storing them directly inside Docker images.

5. Connect Containers Using Docker Networking:

    - Use Docker's networking features to isolate and link containers.
    - Create a custom Docker bridge network to ensure secure communication. For example:

      .. code-block:: sh
  
          docker network create mattermost-network
  
    - Launch the Mattermost and NGINX containers on the same network:

      .. code-block:: sh
  
          docker network connect mattermost-network mattermost
          docker network connect mattermost-network nginx

6. Point your domain to the server IP address:

   Ensure your domain (e.g., your-domain.com) points to the public IP address of your server. If your IP is dynamic, consider setting up Dynamic DNS (DDNS) for seamless connectivity.

7. After placing the certificates and updating the configuration, restart the NGINX container:

8. Use logs (docker logs nginx) to troubleshoot and validate the container’s operation.

9. Verify HTTPS Access by visiting ``https://your-domain.com`` in a web browser to confirm Mattermost is running securely over HTTPS.

10. Use tools such as SSL Labs : https://www.ssllabs.com/ssltest/ to validate the quality of your TLS setup.

11. Enable HTTP Strict Transport Security (HSTS) in your NGINX configuration to prevent downgrade attacks.

12. Use NGINX rate-limiting features to restrict abusive traffic, such as excessive requests:

Additionally, consider:

- Use Docker's security features such as Seccomp profiles and AppArmor to secure your container runtime. 
- Avoid running containers with elevated privileges ``--privileged`` and utilize user namespaces.
- Always use trusted images (e.g., official NGINX and Mattermost images) to prevent exposure to vulnerabilities in third-party images.
- Update Mattermost, NGINX, and Docker to their latest versions regularly to ensure patches for known vulnerabilities are applied.
- Set up proper firewall rules to restrict unauthorized access and monitor traffic using tools like Fail2Ban or Wazuh.

By following these steps, your Mattermost deployment using Docker containers will be accessible securely over HTTPS with efficient proxying through NGINX. Implementing the additional security recommendations will further protect your environment against evolving threats.