# Preparing EKS resources

For a fully functional GitLab instance, you will need a few resources before deployment of this chart.

1. An [EKS cluster](#creating-the-EKS-cluster)
1. [Persistent volume settings](#persistent-volume-management)
1. [TLS certificates](#external-access-to-gitlab)

## Creating the EKS cluster

For the most up to date instructions, follow Amazon's [EKS getting started guide](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html).

Administrators may also want to consider the [new AWS Service Operator for Kubernetes](https://aws.amazon.com/blogs/opensource/aws-service-operator-kubernetes-available/)
to simplify this process.

> **Note:**
>
> Enabling the AWS Service Operator requires a method of managing roles within the cluster. The initial
> services handling that management task are provided by third party developers. Administrators should
> keep that in mind when planning for deployment.

## Persistent Volume Management

There are two methods to manage volume claims on Kubernetes:
1. Manually create a persistent volume
1. Automatic persistent volume creation through dynamic provisioning

Learn more in the  [cluster storage](../installation/storage.md) documentation.

> **Special Consideration:**
>
> We currently recommend using manual provisioning of persistent volumes. Amazon EKS
> clusters default to spanning multiple zones. Dynamic provisioning, if not configured
> to use a storage class locked to a particular zone leads to a scenario where pods may
> exist in a different zone from storage volumes and be unable to access data.
>
> Administrators who need to deploy in multiple zones should familiarize themselves
> with [how to set up cluster storage](../installation/storage.md) and review
> [Amazon's own documentation on storage classes](https://docs.aws.amazon.com/eks/latest/userguide/storage-classes.html)
> when defining their storage solution.

## External Access to GitLab

By default, GitLab will an deploy an ingress which will create an associated Elastic Load Balancer. Since the DNS names of ELB's cannot be known ahead of time, it is difficult to utilize Let's Encrypt to automatically provision HTTPS certificates. 

We recommend [using your own certificates](../installation/tls.md#option-2-use-your-own-wildcard-certificate), and then mapping your desired DNS name to the created ELB using a CNAME record.

Also consider that [Amazon's Elastic Load Balancers](https://docs.aws.amazon.com/eks/latest/userguide/load-balancing.html) require adding the special annotation below:

```yaml
nginx-ingress:
  controller:
    service:
      annotations:
        service.beta.kubernetes.io/aws-load-balancer-internal: 0.0.0.0/0
        service.beta.kubernetes.io/aws-load-balancer-backend-protocol: tcp
```

# Next Steps

Continue with the [installation of the chart](../installation/README.md) once you have the cluster up and running, and have the static IP and DNS entry ready.
