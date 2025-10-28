.. meta::
   :name: robots
   :content: noindex

:orphan:
:nosearch:

From Mattermost v11, each release provides two variants: a FIPS-compliant build and a non-FIPS build. This ensures that organizations with strict compliance requirements can adopt the FIPS version while others can continue with the standard release, both staying in sync with Mattermost’s overall product lifecycle.

Mattermost FIPS-compliant Docker images are built using Chainguard’s FIPS-certified base containers. These images help organizations meet stringent security requirements by ensuring compliance with the Federal Information Processing Standards (FIPS).

On top of this foundation, Mattermost product code itself is aligned with FIPS requirements, using only FIPS-approved cryptographic algorithms. This ensures that both the underlying container base and the application layer meet compliance expectations.

In addition, the Chainguard base images are STIG-hardened and rigorously scanned against the DISA General Purpose Operating System SRG, providing a robust and secure operational posture.

Mattermost FIPS Overview
-------------------------

Mattermost’s FIPS-compliant images are built using two Chainguard base images:

- `Build-Time Image <https://images.chainguard.dev/directory/image/go-msft-fips/overview>`_: Ensures compiled Mattermost binaries invoke OpenSSL through CGO for FIPS-compliance during compilation.
- `Runtime Image <https://images.chainguard.dev/directory/image/glibc-openssl-fips/overview>`_: Enforces FIPS compliance in the runtime environment using strict OpenSSL configurations.

All application-level code uses only FIPS-approved algorithms, ensuring that cryptographic requirements are consistently enforced across every layer of the system.

.. note::

   - The Mattermost FIPS image includes only prepackaged Boards, Playbooks, and Agents. Additional plugins can be added to the Mattermost FIPS image, but they will run in non-FIPS mode. 
   - Existing Docker or Kubernetes-based deployments can change the image from ``mattermost/mattermost-enterprise-edition`` to ``mattermost/mattermost-enterprise-fips-edition``. 
