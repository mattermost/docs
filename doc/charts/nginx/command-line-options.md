# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                         | Description                                            | Default                                                        |
| ---                               | ---                                                    | ---                                                            |
| replicaCount                      | Number of replicas                                     | 1                                                              |
| LoadBalancerIp                    | IP of the external load balancer                       | Required                                                       |
| images.defaultbackend.repository  | Default backend that nginx routes to eg: 404           | gcr.io/google_containers/defaultbackend                        |
| images.defaultbackend.tag         | dafault backend image tag                              | 1.4                                                            |
| images.defaultbackend.pullPolicy  | default backend pull policy                            | IfNotPresent                                                   |
| images.nginxIngress.repository    | nginx repository                                       | quay.io/kubernetes-ingress-controller/nginx-ingress-controller |
| images.nginxIngress.tag           | nginx image tag                                        | 0.9.0                                                          |
| images.nginxIngress.pullPolicy    | nginx image pull policy                                | IfNotPresent                                                   |
| service.name                      | nginx service name                                     | nginx                                                          |
| service.type                      | nginx service type                                     | LoadBalancer                                                   |
| service.ports                     | nginx service ports                                    | [{"http": 80}, {"https": 443}, {"ssh": 22}]                    |
| serviceAccount.autoGenerate       | Whether chart should generate service account for RBAC | true                                                           |
| serviceAccount.name               | Service account name                                   | default                                                        |
| proxyConnectTimeout               | Defines a timeout for establishing a connection        | 15                                                             |
| proxyReadTimeout                  | Defines a timeout for reading a response               | 600                                                            |
| proxySendTimeout                  | Sets a timeout for transmitting a request              | 600                                                            |
| proxyBodySize                     | body size                                              | 512m                                                           |
| hstsIncludeSubdomains             | set HSTS for all subdomains                            | false                                                          |
| serverNameHashBucketSize          | Sets the bucket size for the server names hash tables  | 256                                                            |
| global.hosts.domain               | Domain name                                            | example.local                                                  |
| global.hosts.hostSuffix           |                                                        | Undefined by default                                           |
| global.hosts.https                | True if nginx will serve over https                    | false                                                          |
| global.hosts.gitlab.serviceName   | Gitlab service name                                    | unicorn                                                        |
| global.hosts.gitlab.servicePort   | Gitlab service port name                               | workhorse                                                      |
| global.hosts.registry.serviceName | Registry service name                                  | registry                                                       |
| global.hosts.registry.servicePort | Registry port name                                     | registry                                                       |
| global.hosts.minio.serviceName    | Minio service name                                     | minio-svc                                                      |
| global.hosts.minio.servicePort    | Minio port name                                        | service                                                        |
| shell.name                        | Shell service name                                     | gitlab-shell                                                   |
| shell.port                        | Shell port name                                        | ssh                                                            |
| ingress.enabled                   | Enable ingress                                         | true                                                           |
| ingress.acme                      | Enable lets encrypt via kube-lego                      | true                                                           |
| ingress.hosts                     | Hosts ingress listens to                               | Empty array                                                    |
| ingress.annotations               | Annotations                                            | Undefined by default                                           |
| ingress.tls                       | Tls certificates (custom)                              | Undefined by default                                           |
