FROM alpine:latest
MAINTAINER GitLab Build Team

ENV TF_VERSION=0.11.1
ENV TF_URL=https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip

ENV HELM_VERSION=2.8.2
ENV HELM_URL=https://kubernetes-helm.storage.googleapis.com/helm-v${HELM_VERSION}-linux-amd64.tar.gz

# kubectl (possibly in gcloud?)
ENV KUBECTL_VERSION=1.8.8
ENV KUBECTL_URL=https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl

# Install dependencies
RUN apk --no-cache add -U openssl curl tar gzip bash ca-certificates git python2 ruby\
  && mkdir /opt

# Install kubectl
RUN curl -L -o /usr/local/bin/kubectl ${KUBECTL_URL} \
  && chmod +x /usr/local/bin/kubectl \
  && kubectl version --client

# Install Terraform
RUN curl -LJO ${TF_URL} \
    && unzip terraform*.zip -d /usr/bin  && chmod +x /usr/bin/terraform \
    && rm terraform*.zip \
    && terraform version

# Install Helm
RUN wget -q -O - ${HELM_URL} | tar zxf - \
    && mv linux-amd64/helm /usr/bin/ \
    && chmod +x /usr/bin/helm \
    && helm version --client

# Install Ruby gems for changelog_manager
RUN apk add --no-cache --virtual .ruby-gem-builddeps \
        autoconf cmake make gcc coreutils glib-dev libc-dev libffi-dev \
        ruby-dev openssl-dev \
    && gem install -N rugged \
    && gem install -N activesupport \
    && apk del .ruby-gem-builddeps
