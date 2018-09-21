# Required tools

1. [`kubectl`][kubectl] version 1.8 or higher, compatible with your cluster. ([+/- 1 minor release from your cluster](https://kubernetes.io/docs/tasks/tools/install-kubectl/#before-you-begin))
1. [`Helm`][helm] `v2.x`, we require 2.9 or higher.


### kubectl

You can setup kubectl using the installation documentation for [kubectl][].

At the time of writing this document, the output of `kubectl version`:

```
Client Version: version.Info{Major:"1", Minor:"8", GitVersion:"v1.8.2", GitCommit:"bdaeafa71f6c7c04636251031f93464384d54963", GitTreeState:"clean", BuildDate:"2017-10-24T19:48:57Z", GoVersion:"go1.8.3", Compiler:"gc", Platform:"linux/amd64"}
Unable to connect to the server:
```

> Note: The server version of kubectl cannot be obtained until we connect to a
cluster. Proceed with setting up Helm.

### Helm

Follow the [helm][] document for installation instructions.

# Next Steps

Once the tools are configured, you can continue to configuring your
[Kubernetes cluster](README.md#where-do-you-want-to-install-GitLab).

[kubectl]: https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl
[helm]: ../helm/README.md
