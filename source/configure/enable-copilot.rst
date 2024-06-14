Enable Copilot (Beta)
=======================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Signficantly increase team productivity and decision-making speed by enhancing your real-time collaboration capabilities with instant access to AI-generated information, discussion summaries, and contextually-aware action recommendations with Mattermost's Copilot. Your users can interact with AI capabilities directly within their daily communication channels without needing to switch between multiple tools or platforms

Setup
------

Mattermost AI Copilot comes preinstalled from Mattermost Server v9.7 or later. You must be a Mattermost system admin to `enable it <#enable>`__ and `configure it <#mattermost-configuration>`__ using the System Console.

.. note::
  If you're running Mattermost Server v9.6 or earlier, AI Copilot must be installed using the `latest binary available for download from the plugin repository <https://github.com/mattermost/mattermost-plugin-ai/releases>`_. For an optimized user experience and compatibility, we recommend using AI Copilot with Mattermost v9.7 and later.
  
  The Copilot integration is compatible with the following :doc:`Mattermost Server versions </deploy/mattermost-changelog>`:

  - v9.6 or later
  - v9.5.2+ (Extended Support Release - ESR)
  - v9.4.4+
  - v9.3.3+
  - v8.1.11+ (Extended Support Release - ESR)

Enable
------

Go to **System Console > Plugins > Copilot** to enable this feature.

Once the integration is installed and enabled, complete configuration in the System Console as described below, then notify your teams that they can use the Copilot in any Mattermost team or channel.

Mattermost configuration
~~~~~~~~~~~~~~~~~~~~~~~~

With extensive customization and extensibility options, you can tailor Copilot to meet your specific needs, whether it's integrating with internal systems, customizing AI responses based on the team or project needs, or developing new capabilities that are unique to your operational requirements. You can also create custom integrations, workflows, and bots that leverage AI to meet your unique business needs.

Configure a large language model (LLM) for your Copilot integration by going to **System Console > Plugins > Copilot**. Mattermost supports the following LLMs:

- `OpenAI <https://platform.openai.com/account/api-keys>`_
- `Anthropic (Claude) <https://console.anthropic.com/account/keys>`_
- `Azure OpenAI <https://learn.microsoft.com/en-us/azure/ai-services/openai/overview>`_
- `OpenAI Compatible <https://github.com/go-skynet/LocalAI>`_

.. tab:: Open AI

  1. Obtain an `OpenAI API key <https://platform.openai.com/account/api-keys>`_.
  2. Select **OpenAI** in the **AI Service** dropdown.
  3. Enter your OpenAI API key in the **API Key** field.
  4. Enter a model name in the **Default Model** field, such as `gpt-4` or `gpt-3.5-turbo`.
  5. (Optional) If using multiple organizations on OpenAI, specify your **Organization ID** to direct API usage and billing accordingly.

.. tab:: Anthropic (Claude)

  1. Obtain an `Anthropic API key <https://console.anthropic.com/account/keys>`_.
  2. Select **Anthropic** in the **AI Service** dropdown.
  3. Enter your Anthropic API key in the **API Key** field.
  4. Specify a model name in the **Default Model** field, like `claude-v1`.

.. tab:: Azure OpenAI

  For integrating with Microsoft Azure's OpenAI services, `see the official Azure Open AI documentation <https://learn.microsoft.com/en-us/azure/ai-services/openai/overview>`_.

  1. Get `access to Azure OpenAI <https://learn.microsoft.com/en-us/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai>`_.
  2. Create a new OpenAI resource in Azure.
  3. Ensure your model resource on Azure does not auto-update.
  4. In Mattermost, choose **OpenAI Compatible** in the **AI Service** dropdown.
  5. Enter your Azure resource's URL in the **API URL** field.
  6. Input your Azure resource API key in the **API Key** field.
  7. Specify your model name in the **Default Model** field, for example, `gpt-3.5-turbo`.

.. tab:: OpenAI Compatible

  The OpenAI Compatible option allows integration with any OpenAI-compatible LLM provider:

  1. Deploy your model, for example, on LocalAI.
  2. Select **OpenAI Compatible** in the **AI Service** dropdown.
  3. Enter the URL to your AI service in the **API URL** field.
  4. Enter your API key in the **API Key** field.
  5. Specify your model name in the **Default Model** field.

Upgrade
~~~~~~~

We recommend updating this integration as new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost.

Visit the `Releases page <https://github.com/mattermost/mattermost-plugin-ai/releases>`_ for the latest release, available releases, and compatibiilty considerations.

Usage
-----

See the :doc:`chat with Copilot </collaborate/chat-with-copilot>` documentation for details on using Copilot to overcome information overload and streamline communication and collaboration.