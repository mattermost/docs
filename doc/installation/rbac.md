# Role Based Access Control

Until Kubernetes 1.7, there were no permissions within a cluster. With the launch of 1.7, there is now a role based access control system (RBAC) which determines what services can perform actions within a cluster.

RBAC affects a few different aspects of GitLab:
* [Installation of GitLab using Helm](../helm/README.md#preparing-for-helm-with-rbac)
* Prometheus monitoring
* GitLab Runner
* Kube-Lego
* nginx-ingress