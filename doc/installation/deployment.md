To deploy, we'll run `helm install` with our configuration file, from the
root of this repository:

```
$ helm install -f configuration.yaml .
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
