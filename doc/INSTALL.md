# Installing via helm

This document provides all steps in installing a complete GitLab environment via
[helm][]

Items and information needed:
- GKE cluster (via `gcloud`)
- [kunectl][] latest version (part of `gcloud`)
- [helm][] latest version
- SSL certificates
- Secrets for Certificates, Registry, Redis
- A regional static IP in Google Cloud, with an A record in DNS

## Install Software Requirements

The [gcloud][] sdk & command contains `kubectl`. Install this per [documentation][gcloud].
If already installed, ensure they are up to date with `gcloud components update`

```
$ gcloud version
Google Cloud SDK 179.0.0
app-engine-python 1.9.62
bq 2.0.27
core 2017.11.06
gcloud
gsutil 4.28
kubectl
$ kubectl version
Client Version: version.Info{Major:"1", Minor:"8", GitVersion:"v1.8.2", GitCommit:"bdaeafa71f6c7c04636251031f93464384d54963", GitTreeState:"clean", BuildDate:"2017-10-24T19:48:57Z", GoVersion:"go1.8.3", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"7+", GitVersion:"v1.7.8-gke.0", GitCommit:"a7061d4b09b53ab4099e3b5ca3e80fb172e1b018", GitTreeState:"clean", BuildDate:"2017-10-10T18:48:45Z", GoVersion:"go1.8.3", Compiler:"gc", Platform:"linux/amd64"}
```

Follow the [helm][] document for [installation instructions](https://github.com/kubernetes/helm#install)

```
$ helm version
Client: &version.Version{SemVer:"v2.7.0", GitCommit:"08c1144f5eb3e3b636d9775617287cc26e53dba4", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.5.1", GitCommit:"7cf31e8d9a026287041bae077b09165be247ae66", GitTreeState:"clean"}
```


## Connect to the cluster

The command for connection to the cluster can be obtained from the [Google Cloud Platform Console][gcp-k8s]
under the individual cluster. Look for `Connect to the cluster` link at the top
of the cluster properties page.

```
$ gcloud container clusters get-credentials cloud-native --zone <zone> --project <project-id>
$ kubectl get endpoints
NAME         ENDPOINTS           AGE
kubernetes   <cluster-ip>:443   22d
```

The above command will configure `kubectl`, and thus `helm` to make use of the GKE cluster.

## Install Helm/Tiller to the cluster

See [helm][] documentation for installation & initialization.

## Create Secrets

For a functional deployment, these secrets are needed: Certificates, Registry
certificates, Redis password, GitLab Shell Secret, and Gitaly Secret.

### Certificates

Fetch the certificates from a source. For this guide, we will be using wildcard
certificates. Ensure that the `.crt` file used is a properly structured full-chain
certificate. GitLab employees on this project can find them in the `Cloud Native`
vault in `1Password`.

```
$ kubectl create secret tls helm-charts-win-tls --cert=certs/-.helm-charts.win.chained.crt --key=certs/-.helm-charts.win.key
secret "helm-charts-win-tls" created
```

### Registry certificates

To ensure the [omnibus][] chart can talk to the [registry][] chart, we'll need to
create a certificate pair. We'll do this with the `openssl` command:

```
$ openssl req -new -newkey rsa:4096 -subj="/CN=gitlab-issuer" -nodes -x509 -keyout certs/helm-charts-win-registry.key -out certs/helm-charts-win-registry.crt
Generating a 4096 bit RSA private key
..................................................................................................................................................++
..............................................................................................................................................................++
writing new private key to 'certs/helm-charts-win-registry.key'
-----
```

Next, we'll create a secret containing these certificates that both charts will use.
In more isolated clusters, these certificates can be in separate secrets, as long
as the configuration information as to which secret to use is passed to the appropriate
chart. We will create `registry-auth.key` and `registry-auth.crt` keys inside the
`gitlab-registry` secret.

```
$ kubectl create secret generic gitlab-registry --from-file=registry-auth.key=certs/helm-charts-win-registry.key --from-file=registry-auth.crt=certs/helm-charts-win-registry.crt
secret "gitlab-registry" created
```

### Redis password

We'll generate a random password for Redis, alpha-numeric and at least 64 characters
long. For GitLab, this has already been done and is stored in the GitLab `1Password`.

```
$ kubectl create secret generic gitlab-redis --from-literal=redis-password=<password>
secret "gitlab-redis" created
```

### GitLab Shell

Generate a random secret for GitLab Shell, and use it to create the secret

```
$ ruby -e "require 'securerandom'; print SecureRandom.hex(64)" > ./shell_secret
$ kubectl create secret generic gitlab-shell-secret --from-file=secret=shell_secret
```

### Gitaly Secret

```
$ ruby -e "require 'securerandom'; print SecureRandom.hex(64)" > ./gitaly_secret
$ kubectl create secret generic gitaly-secret --from-file=token=gitaly_secret
```

## Configure

TODO: add sanitized config yaml file to repo.

Create `helm-charts-win.yaml`

Set the following properties in `helm-charts-win.yaml`:
- nginx.service.loadBalancerIP: [static-ip]
- nginx.ingress.hosts[0].name: gitlab.helm-charts.win
- nginx.ingress.hosts[1].name: registry.helm-charts.win
- nginx.ingress.tls[0].secretName: helm-charts-win-tls
- nginx.ingress.tls[0].hosts[]: gitlab.helm-charts.win, registry.helm-charts.win
- registry.service.type: NodePort
- registry.registry.authEndpoint: 'https://gitlab.helm-charts.win'
- registry.registry.tokenIssuer: gitlab-issuer
- registry.registry.certBundle.secretName: gitlab-registry
- registry.registry.certBundle.bundleName: registry-auth.crt
- gitlab.omnibus.service.type: NodePort
- gitlab.omnibus.enabled: true
- gitlab.omnibus.external_url: 'https://gitlab.helm-charts.win'
- gitlab.omnibus.initial_root_password: [from 1Password]
- gitlab.omnibus.redis.enabled: true
- gitlab.omnibus.redis.password.secret: gitlab-redis
- gitlab.omnibus.redis.password.key: redis-password
- gitlab.omnibus.psql.enabled: true
- gitlab.omnibus.registry.host: registry.helm-charts.win
- gitlab.omnibus.registry.port: 80
- gitlab.omnibus.registry.secret: gitlab-registry
- gitlab.omnibus.registry.certificate: registry-auth.key

## Deploy

To deploy, we'll simply run `helm install` with our configuration file, from the
root of this repository:

```
$ helm install -f helm-charts-win.yaml .
NAME:   ill-dachshund
LAST DEPLOYED: Wed Nov  8 15:40:40 2017
NAMESPACE: master
STATUS: DEPLOYED

RESOURCES:
==> v1/ConfigMap
NAME                     DATA  AGE
ill-dachshund-omnibus    1     2s
ill-dachshund-nginx-tcp  1     2s
ill-dachshund-nginx      7     2s
ill-dachshund-registry   1     2s

==> v1/Service
NAME                                 TYPE          CLUSTER-IP     EXTERNAL-IP  PORT(S)                                                                                AGE
ill-dachshund-omnibus                NodePort      10.43.248.194  <none>       80:30181/TCP,6397:32469/TCP,5432:30780/TCP,22:30538/TCP,8080:31541/TCP,8005:31941/TCP  2s
ill-dachshund-nginx-default-backend  ClusterIP     10.43.250.159  <none>       80/TCP                                                                                 2s
ill-dachshund-nginx                  LoadBalancer  10.43.245.12   <pending>    80:30875/TCP,443:30374/TCP,22:32110/TCP                                                2s
ill-dachshund-registry               NodePort      10.43.247.50   <none>       5000:32416/TCP                                                                         2s

==> v1beta1/DaemonSet
NAME                 DESIRED  CURRENT  READY  UP-TO-DATE  AVAILABLE  NODE SELECTOR  AGE
ill-dachshund-nginx  2        2        0      2           0          <none>         2s

==> v1beta1/Deployment
NAME                                 DESIRED  CURRENT  UP-TO-DATE  AVAILABLE  AGE
ill-dachshund-omnibus                1        1        1           0          2s
ill-dachshund-nginx-default-backend  1        1        1           0          2s
ill-dachshund-registry               1        1        1           0          2s

==> v1beta1/Ingress
NAME                 HOSTS                                            ADDRESS  PORTS  AGE
ill-dachshund-nginx  registry.helm-charts.win,gitlab.helm-charts.win  80       2s

==> v1/Pod(related)
NAME                                                  READY  STATUS             RESTARTS  AGE
ill-dachshund-nginx-4mf86                             0/1    ContainerCreating  0         2s
ill-dachshund-nginx-j5p3w                             0/1    ContainerCreating  0         2s
ill-dachshund-omnibus-2367403649-tn2hx                0/1    ContainerCreating  0         2s
ill-dachshund-nginx-default-backend-2589959935-b19c8  0/1    ContainerCreating  0         2s
ill-dachshund-registry-3838581850-45x30               0/1    ContainerCreating  0         2s
```

Later, the status of the deployment can be checked with `helm status <deployemnt-name>`.

```
$ helm status ill-dachshund
```

[gcloud]: https://cloud.google.com/sdk/gcloud/
[kubectl]: https://kubernetes.io/docs/tasks/tools/install-kubectl/
[helm]: helm/README.md
[gcp-k8s]: https://console.cloud.google.com/kubernetes/list
[registry]: ../charts/registry
[omnibus]: ../charts/gitlab/charts/omnibus
