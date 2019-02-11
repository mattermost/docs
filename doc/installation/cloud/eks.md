# Preparing EKS resources

For a fully functional GitLab instance, you will need a few resources before
deploying the `gitlab` chart.

## Creating the EKS cluster

For the most up to date instructions, follow Amazon's
[EKS getting started guide](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html).

Administrators may also want to consider the
[new AWS Service Operator for Kubernetes](https://aws.amazon.com/blogs/opensource/aws-service-operator-kubernetes-available/)
to simplify this process.

NOTE: **Note:**
Enabling the AWS Service Operator requires a method of managing roles within the cluster. The initial
services handling that management task are provided by third party developers. Administrators should
keep that in mind when planning for deployment.

## Persistent Volume Management

There are two methods to manage volume claims on Kubernetes:

- Manually create a persistent volume.
- Automatic persistent volume creation through dynamic provisioning.

We currently recommend using manual provisioning of persistent volumes. Amazon EKS
clusters default to spanning multiple zones. Dynamic provisioning, if not configured
to use a storage class locked to a particular zone leads to a scenario where pods may
exist in a different zone from storage volumes and be unable to access data.

Administrators who need to deploy in multiple zones should familiarize themselves
with [how to set up cluster storage](../storage.md) and review
[Amazon's own documentation on storage classes](https://docs.aws.amazon.com/eks/latest/userguide/storage-classes.html)
when defining their storage solution.

## External Access to GitLab

By default, GitLab will deploy an ingress which will create an associated
Elastic Load Balancer (ELB). Since the DNS names of the ELB cannot be known
ahead of time, it's difficult to utilize Let's Encrypt to automatically provision
HTTPS certificates.

We recommend [using your own certificates](../tls.md#option-2-use-your-own-wildcard-certificate),
and then mapping your desired DNS name to the created ELB using a CNAME record.

NOTE: **Note:**
For environments where internal load balancers are required,
[Amazon's Elastic Load Balancers](https://docs.aws.amazon.com/eks/latest/userguide/load-balancing.html)
require [special annotations](https://gitlab.com/charts/gitlab/blob/master/examples/eks_loadbalancer_annotations.yml).

## Next Steps

Continue with the [installation of the chart](../deployment.md) once you have
the cluster up and running, and the static IP and DNS entry ready.
