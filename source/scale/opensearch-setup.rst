AWS OpenSearch server setup
============================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

AWS OpenSearch Service allows you to search large volumes of data quickly, in near real-time, by creating and managing an index of post data. The indexing process can be managed from the System Console after setting up and connecting an OpenSearch server. The post index is stored on the OpenSearch server and updated constantly after new posts are made. In order to index existing posts, a bulk index of the entire post database must be generated.

Deploying AWS OpenSearch includes the following two steps: `setting up AWS OpenSearch <#set-up-aws-opensearch>`__, and `configuring Mattermost <#configure-mattermost>`_. 

Set up AWS OpenSearch
----------------------

From Mattermost v9.11, beta support is available for `AWS OpenSearch v1.x and v2.x <https://opensearch.org/>`_. This document covers both on‑premises and AWS OpenSearch setup, including manual steps and Terraform examples.

We highly recommend that you set up an AWS OpenSearch server on a separate machine from the Mattermost server.

.. tab:: On-Premises OpenSearch

  1. To install on-premise OpenSearch, provision a dedicated server (e.g. Ubuntu 22.04 LTS).
  2. Install Java (OpenSearch requires Java 11+):

    .. code-block:: sh

      sudo apt update 
      sudo apt install -y openjdk-11-jdk 
      java -version

  3. Download & extract OpenSearch 2.x:

    .. code-block:: sh

      wget https://artifacts.opensearch.org/releases/bundle/opensearch/2.9.0/opensearch-2.9.0-linux-x64.tar.gz 
      tar -xzf opensearch-2.9.0-linux-x64.tar.gz 
      sudo mv opensearch-2.9.0 /usr/share/opensearch

  4. Create a dedicated user & set permissions:

    .. code-block:: sh

      sudo useradd --no-create-home --shell /bin/false opensearch 
      sudo chown -R opensearch:opensearch /usr/share/opensearch

  5. Configure systemd:

    .. code-block:: sh

      [Unit] 
        Description=OpenSearch 
        Wants=network-online.target 
        After=network-online.target 
        
      [Service] 
        Type=notify 
        User=opensearch 
        Group=opensearch 
        ExecStart=/usr/share/opensearch/bin/opensearch 
        Restart=on-failure 
        LimitNOFILE=65536 
        LimitNPROC=4096 
        
      [Install] 
        WantedBy=multi-user.target

  6. Edit ``opensearch.yml`` to include the following:

    .. code-block:: sh

      cluster.name: mattermost-cluster node.name: 
      node-1 
      path.data: /var/lib/opensearch 
      path.logs: /var/log/opensearch
      network.host: 0.0.0.0 
      discovery.seed_hosts: ["<other-node-ip>"] 
      cluster.initial_master_nodes: ["node-1", "node-2"]

  7. Enable & start OpenSearch:

    .. code-block:: sh

      sudo systemctl daemon-reload 
      sudo systemctl enable opensearch 
      sudo systemctl start opensearch 
      sudo systemctl status opensearch


  **Terraform (Docker) Example**

  .. code-block:: sh

    provider "docker" { 
      host = "unix:///var/run/docker.sock" 
    }

    resource "docker_image" "opensearch" { 
      name = "opensearchproject/opensearch:2.9.0" 
    }

    resource "docker_container" "opensearch" { 
      name = "opensearch" 
      image = docker_image.opensearch.latest 

      ports { 
        internal = 9200 
        external = 9200 
      }
      ports { 
        internal = 9600 
        external = 9600 
      }

      env = [
        "cluster.name=mattermost-cluster",
        "network.host=0.0.0.0",
        "discovery.type=single-node", # remove for multi-node 
      ]

      restart = "unless-stopped" 
    }

.. tab:: AWS OpenSearch Console Setup

  1. To install AWS OpenSearch, open the **AWS Console > OpenSearch Service**.

  2. Create a domain, where:
  
    - Domain name: ``mattermost-os``
    - Engine version: ``OpenSearch 2.x``.

  3. Configure the cluster, where:
  
    - instance type: ``r6g.xlarge.search``
    - data nodes: 2
    - master nodes: 2
    - storage: EBS gp3 (1536 GiB, 4608 IOPS, 250 MiB/s)

  4. Specify the network for: VPC with 2 subnets, and a security group allowing Mattermost IPs on port ``9200``.

  5. Configure the access policy (JSON):

    .. code-block:: sh

      {
        "Version": "2012-10-17", 
        "Statement": [{ 
          "Effect": "Allow", 
          "Principal": { "AWS": 
      "arn:aws:iam::123456789012:role/MattermostAppRole" }, 
          "Action": "es:*", 
          "Resource": "arn:aws:es:us-east-1:123456789012:domain/mattermost-os/*" }] 
      }

  6. Configure the following advanced settings (JSON):

    .. code-block:: sh

      {
        "action.destructive_requires_name": "false", 
        "rest.action.multi.allow_explicit_index": "true", 
        "indices.query.bool.max_clause_count": "1024", 
        "indices.fielddata.cache.size": "20" 
      }

  7. Configure the automated snapshot start hour as 23 (UTC), enforce HTTPS, then review & create. 
  
  8. To test, run the following command:

    .. code-block:: sh

      curl https://mattermost-os-xxxxxxxxxxx.us-east-1.es.amazonaws.com

  **AWS Terraform Example**

  .. code-block:: sh

    provider "aws" { 
      region = "us-east-1" 
    }

    resource "aws_iam_role" "os_service_role" { 
      name = "OSServiceRole" 
      assume_role_policy = <<EOF 
    {
      "Version": "2012-10-17", 
      "Statement": [{ 
        "Action": "sts:AssumeRole", 
        "Effect": "Allow", 
        "Principal": { "Service": "es.amazonaws.com" } 
      }]
    }
    EOF
    }

    resource "aws_opensearch_domain" "mattermost" { 
      domain_name = "mattermost-os" 
      engine_version = "OpenSearch_2.9"
      cluster_config { 
        instance_type = "r6g.xlarge.search" 
        instance_count = 2 
        dedicated_master_enabled = true 
        dedicated_master_type = "r6g.xlarge.search" 
        dedicated_master_count = 2 
        zone_awareness_enabled = true 
      }

      ebs_options { 
        ebs_enabled = true 
          volume_type = "gp3" 
          volume_size = 1536 
          iops = 4608 
      }

      vpc_options { 
        subnet_ids = ["subnet-blah1", "subnet-blah2"] 
        security_group_ids = ["sg-1234567890"] 
      }

      advanced_options = { 
        "rest.action.multi.allow_explicit_index" = "true" 
        "indices.query.bool.max_clause_count" = "1024" 
        "indices.fielddata.cache.size" = "20" 
        "action.destructive_requires_name" = "false" 
      }

      access_policies = <<POLICY 
    {
      "Version": "2012-10-17", 
      "Statement": [{ 
        "Effect": "Allow", 
        "Principal": { 
          "AWS": "arn:aws:iam::123456789012:role/MattermostAppRole" 
        },
          "Action": "es:*", 
          "Resource": "arn:aws:es:us-east-1:123456789012:domain/mattermost-os/*" 
        }]
      }
      POLICY
        service_software_options { 
          automated_snapshot_start_hour = 23 
        }

        domain_endpoint_options { 
          enforce_https = true 
        }
    }

Configure Mattermost
---------------------

Follow these steps to configure Mattermost to use your AWS OpenSearch server and to generate the post index:

1. Go to **System Console > Environment > Elasticsearch**.
2. Set **Enable Elasticsearch Indexing** to ``true`` to enable the other the settings on the page.
3. Ensure **Backend type** is set to ``opensearch``.
4. Set the **Server Connection Address** to your Elasticsearch or OpenSearch cluster endpoint.
5. Monitor cluster health: ``curl https://mattermost-os-xxxxx.us-east-1.es.amazonaws.com/_cluster/health``

.. include:: /scale/common-configure-mattermost-for-enterprise-search.rst
   :start-after: :nosearch:
