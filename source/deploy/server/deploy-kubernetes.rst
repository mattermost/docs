Deploy Mattermost on Kubernetes
===============================

Mattermost server can be deployed on various Kubernetes platforms, providing a scalable and robust infrastructure for your team communication needs. This guide covers deployment options for major cloud providers and general Kubernetes installations.

Choose your preferred platform below for specific deployment instructions:

.. tab:: Azure

  .. include:: kubernetes/deploy-k8s-aks.rst
    :start-after: :nosearch:

.. tab:: Other Kubernetes

  .. include:: kubernetes/deploy-k8s.rst
    :start-after: :nosearch:

Secure your Mattermost deployment
---------------------------------

Deploying Mattermost in a Kubernetes environment allows you to harness Kubernetes-native features for scalability, security, and ease of management. By using an Ingress resource in combination with an ingress controller, you can enable secure HTTPS access to Mattermost while managing routing and TLS certificates effectively.

1. Deploy an ingress controller, such as the `NGINX Ingress Controller <https://kubernetes.github.io/ingress-nginx/>`_, in your Kubernetes cluster. 
2. Define an Ingress resource to route external traffic to your Mattermost service. Below is an example Ingress manifest:

  .. code-block:: yaml

    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: mattermost-ingress
      annotations:
        nginx.ingress.kubernetes.io/ssl-redirect: "true"
        nginx.ingress.kubernetes.io/proxy-body-size: "10m"  # Customize client body size limit
        nginx.ingress.kubernetes.io/proxy-read-timeout: "60" # Customize request timeout
    spec:
      tls:
      - secretName: mattermost-tls # Reference to the TLS secret
      rules:
      - host: <your-domain.com>
        http:
          paths:
          - path: /
            pathType: ImplementationSpecific
            backend:
              service:
                name: mattermost-service # Name of your Mattermost service
                port:
                  number: 80

3. Secure HTTPS access by using TLS certificates. You can either:

  - Provide your own TLS certificate and private key.
  - Automate TLS certificate issuance and management using `cert-manager <https://cert-manager.io/docs/>`_. If you are providing your own TLS certificate, create a Kubernetes secret to store it.
  - Ensure the Ingress resource references the secret name (mattermost-tls) in its tls section.

4. Save your Ingress and TLS YAML manifests to files (e.g., ``ingress.yaml`` and ``tls.yaml``) and apply them to your cluster using Kubernetes command-line tools. 

5. Configure DNS by ensuring your domain name ``your-domain.com`` is properly pointed to the external IP address of your cluster or ingress controller. You can verify this using tools like nslookup or dig.

6. After applying the Ingress, verify HTTPS Access by navigating to your domain (e.g., ``https://your-domain.com``) in a web browser to verify HTTPS access. If you encounter issues, check ingress controller logs (``kubectl logs -n <namespace> <ingress-controller-pod-name>``, DNS records, and TLS configurations.

7. Enable HSTS and Additional Security in your Ingress annotations.

Additionally, consider:

- Enforcing a minimum TLS version (e.g., TLS 1.2).
- Deploying a Web Application Firewall (WAF) for additional protection, if supported by your ingress controller.
- Limiting access using Kubernetes Network Policies.

By following these steps, your Mattermost deployment in Kubernetes will be securely accessible over HTTPS using TLS. With an NGINX Ingress controller managing routing and proxying, and proper security practices in place, you'll have a robust setup ready for production use.