Health Check
============

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This page describes how to configure health check probes for a Mattermost server.

Before you begin, you should have a running Mattermost server. If you don't, you can `install Mattermost on various distributions <https://docs.mattermost.com/guides/deployment.html>`__ or deploy a `Kubernetes cluster with Minikube <https://github.com/mattermost/mattermost-kubernetes>`__.  Note that `highly available Mattermost cluster support <https://docs.mattermost.com/scale/high-availability-cluster.html>`__ is available in Mattermost Enterprise.

You can perform a health check with two methods:

``/ping`` APIv4 Endpoint
-------------------------

From Mattermost v3.10 and later, you can use the `GET /system/ping APIv4 endpoint <https://api.mattermost.com/#tag/system%2Fpaths%2F~1system~1ping%2Fget>`__ to check for system health.

A sample request is included below. The endpoint checks if the server is up and healthy based on the configuration setting ``GoRoutineHealthThreshold``.

- If ``GoRoutineHealthThreshold`` and the number of goroutines on the server exceeds that threshold, the server is considered unhealthy.
- If ``GoRoutineHealthThreshold`` is not set or the number of goroutines is below the threshold the server is considered healthy.

This endpoint can also be provided to schedulers like `Kubernetes <https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/#before-you-begin>`__.

.. code-block:: go

  import "github.com/mattermost/mattermost-server/model"
  
  Client := model.NewAPIv4Client("https://your-mattermost-url.com")
  Client.Login("email@domain.com", "Password1")
  
  // GetPing
  status, err := Client.GetPing()

Mattermost Probe
----------------

The `Mattermost Probe <https://github.com/csduarte/mattermost-probe>`__ constantly pings a Mattermost server using a variety of probes.

These probes can be configured to verify core features, including sending and receiving messages, joining channels, pinging a login page, and searching of users and channels.

The project is contributed by the Mattermost open source community. Suggestions and contributions for the project are welcome.
