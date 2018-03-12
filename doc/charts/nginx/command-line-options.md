# Installation command line options

Table below contains all the possible charts configurations that can be supplied to `helm install` command using the `--set` flags

| Parameter                               | Description                                            | Default                                                        |
| ---                                     | ---                                                    | ---                                                            |
| nginx.replicaCount                      | Number of replicas                                     | 1                                                              |
| nginx.LoadBalancerIp                    | IP of the external load balancer                       | Required                                                       |
| nginx.images.defaultbackend.repository  | Default backend that nginx routes to eg: 404           | gcr.io/google_containers/defaultbackend                        |
| nginx.images.defaultbackend.tag         | dafault backend image tag                              | 1.4                                                            |
| nginx.images.defaultbackend.pullPolicy  | default backend pull policy                            | IfNotPresent                                                   |
| nginx.images.nginxIngress.repository    | nginx repository                                       | quay.io/kubernetes-ingress-controller/nginx-ingress-controller |
| nginx.images.nginxIngress.tag           | nginx image tag                                        | 0.9.0                                                          |
| nginx.images.nginxIngress.pullPolicy    | nginx image pull policy                                | IfNotPresent                                                   |
| nginx.service.name                      | nginx service name                                     | nginx                                                          |
| nginx.service.type                      | nginx service type                                     | LoadBalancer                                                   |
| nginx.service.ports                     | nginx service ports                                    | [{"http": 80}, {"https": 443}, {"ssh": 22}]                    |
| nginx.serviceAccount.autoGenerate       | Whether chart should generate service account for RBAC | true                                                           |
| nginx.serviceAccount.name               | Service account name                                   | default                                                        |
| nginx.proxyConnectTimeout               | Defines a timeout for establishing a connection        | 15                                                             |
| nginx.proxyReadTimeout                  | Defines a timeout for reading a response               | 600                                                            |
| nginx.proxySendTimeout                  | Sets a timeout for transmitting a request              | 600                                                            |
| nginx.proxyBodySize                     | body size                                              | 512m                                                           |
| nginx.hstsIncludeSubdomains             | set HSTS for all subdomains                            | false                                                          |
| nginx.serverNameHashBucketSize          | Sets the bucket size for the server names hash tables  | 256                                                            |
| nginx.global.hosts.domain               | Domain name                                            | example.local                                                  |
| nginx.global.hosts.hostSuffix           |                                                        | Undefined by default                                           |
| nginx.global.hosts.https                | True if nginx will serve over https                    | false                                                          |
| nginx.global.hosts.gitlab.serviceName   | Gitlab service name                                    | unicorn                                                        |
| nginx.global.hosts.gitlab.servicePort   | Gitlab service port name                               | workhorse                                                      |
| nginx.global.hosts.registry.serviceName | Registry service name                                  | registry                                                       |
| nginx.global.hosts.registry.servicePort | Registry port name                                     | registry                                                       |
| nginx.global.hosts.minio.serviceName    | Minio service name                                     | minio-svc                                                      |
| nginx.global.hosts.minio.servicePort    | Minio port name                                        | service                                                        |
| nginx.shell.name                        | Shell service name                                     | gitlab-shell                                                   |
| nginx.shell.port                        | Shell port name                                        | ssh                                                            |
| nginx.ingress.enabled                   | Enable ingress                                         | true                                                           |
| nginx.ingress.acme                      | Enable lets encrypt via kube-lego                      | true                                                           |
| nginx.ingress.hosts                     | Hosts ingress listens to                               | Empty array                                                    |
| nginx.ingress.annotations               | Annotations                                            | Undefined by default                                           |
| nginx.ingress.tls                       | Tls certificates (custom)                              | Undefined by default                                           |

