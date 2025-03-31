Mobile app deployment
======================

The Mattermost mobile app is available for iPhone and Android devices, and provides a native experience on the go, ensuring you can stay connected and productive from anywhere.

Learn more about :ref:`mobile app software requirements <deploy/server/software-hardware-requirements:mobile apps>`, :doc:`available releases and server compatibility </about/mattermost-mobile-releases>`, :doc:`what's changed across releases </about/mobile-app-changelog>`, and :doc:`commonly asked questions </deploy/mobile/mobile-faq>`.

Download
--------

Mattermost users can download the Mattermost mobile app directly from the `Mattermost website <https://mattermost.com/apps/>`_. 

We recommend using an :doc:`EMM provider </deploy/mobile/deploy-mobile-apps-using-emm-provider>` to maintain full control over the distribution process, as well as enforce or restrict specific security policies.

Log in
~~~~~~ 

The first time you log in to Mattermost using the mobile app, connect to a Mattermost server by entering a **Server URL** and **Server display name**, then select **Connect**.

.. tip::

  Can't find your Mattermost server URL? Ask your company’s IT department or your Mattermost system admin for your organization’s **Mattermost Site URL**. It’ll look something like ``https://example.com/company/mattermost``, ``mattermost.yourcompanydomain.com``, or ``chat.yourcompanydomain.com``. These URLs could also end in ``.net``.

Deployment options
------------------

Learn what’s required to build and deploy Mattermost mobile apps.

.. toctree::
    :maxdepth: 2
    :hidden:
    :titlesonly:

    /deploy/mobile/deploy-mobile-apps-using-emm-provider.rst
    /deploy/mobile/distribute-custom-mobile-apps.rst
    /deploy/mobile/host-your-own-push-proxy-service.rst
    /deploy/mobile/consider-mobile-vpn-options.rst
    /deploy/mobile/mobile-faq.rst

* :doc:`Distribute custom mobile apps </deploy/mobile/distribute-custom-mobile-apps>`
* :doc:`Host your own push proxy service </deploy/mobile/host-your-own-push-proxy-service>`
* :doc:`Mobile VPN options </deploy/mobile/consider-mobile-vpn-options>`
* :doc:`Mobile apps FAQ </deploy/mobile/mobile-faq>`