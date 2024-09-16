Cloud VPC Private Connectivity
===============================

.. include:: ../_static/badges/ent-cloud-only.rst
   :start-after: :nosearch:

VPC Private Connectivity (Private Link) offers Enterprise Cloud customers tailored solutions for private connectivity needs with Mattermost. These options enable customers to access Mattermost through AWS's network without using the public internet, or allow the Mattermost Infrastructure team to manage a Mattermost workspace hosted in the customer's VPC via an EKS cluster.

The key objectives of this offering are:

- Allowing customers to access Mattermost within their internal network
- Enabling the Mattermost infrastructure team to perform operations on a Mattermost workspace hosted in the customer’s VPC, upon request
- Establishing connectivity between the customer's VPC and Mattermost exclusively through AWS’s network, without exposure to the public internet
- Ensuring the setup process is straightforward and easy to implement
- Adhering to all security best practices

Configure VPC Private Connectivity
-----------------------------------

- Mattermost will provide Terraform modules tailored to the customer’s requirements
- Both Mattermost and customer Infrastructure teams will collaborate to establish connectivity on both sides
- AWS Private Link will be used to connect AWS accounts

Requirements
~~~~~~~~~~~~~

- Customers must own their AWS Account

Considerations
~~~~~~~~~~~~~~~

- Proper communication is essential for setting expectations and scheduling changes.

