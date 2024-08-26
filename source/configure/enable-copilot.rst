Enable Copilot
==============

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Signficantly increase team productivity and decision-making speed by enhancing your real-time collaboration capabilities with instant access to AI-generated information, discussion summaries, and contextually-aware action recommendations with Mattermost's Copilot. Your users can interact with AI capabilities directly within their daily communication channels without needing to switch between multiple tools or platforms

Setup
------

Mattermost AI Copilot comes pre-installed from Mattermost Server v9.7 or later. You must be a Mattermost system admin to `enable <#enable>`__ and `configure  <#mattermost-configuration>`__ it using the System Console.

.. note::
  If you're running Mattermost Server v9.6 or earlier, AI Copilot must be installed using the `latest binary available for download from the plugin repository <https://github.com/mattermost/mattermost-plugin-ai/releases>`_. For an optimized user experience and compatibility, we recommend using Mattermost Copilot with Mattermost v9.7 and later.
  
  The Copilot integration is compatible with the following Mattermost Server versions:

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

Configure a large language model (LLM) for your Copilot integration by going to **System Console > Plugins > Copilot** and selecting **Add an AI Bot**. Mattermost supports the following LLMs:

- `OpenAI <https://openai.com/index/openai-api/>`_
- `Anthropic (Claude) <https://console.anthropic.com/account/keys>`_
- `Azure OpenAI <https://learn.microsoft.com/en-us/azure/ai-services/openai/overview>`_
- `OpenAI-compatible (e.g., LocalAI) <https://github.com/go-skynet/LocalAI>`_

.. tab:: Open AI

  1. Obtain an `OpenAI API key <https://platform.openai.com/account/api-keys>`_.
  2. Select **OpenAI** in the **Service** dropdown.
  3. Enter your OpenAI API key in the **API Key** field.
  4. Enter a model name in the **Default Model** field corresponding with the model's label in the API, such as `gpt-4o` or `gpt-3.5-turbo`.
  5. (Optional) If your API key belongs to an OpenAI organization, specify your **Organization ID**.

.. tab:: Anthropic (Claude)

  1. Obtain an `Anthropic API key <https://console.anthropic.com/account/keys>`_.
  2. Select **Anthropic** in the **Service** dropdown.
  3. Enter your Anthropic API key in the **API Key** field.
  4. Specify a model name in the **Default Model** field corresponding with the model's label in the API, such as `claude-3-5-sonnet-20240620`.

.. tab:: Azure OpenAI

  For more details about integrating with Microsoft Azure's OpenAI services, `see the official Azure OpenAI documentation <https://learn.microsoft.com/en-us/azure/ai-services/openai/overview>`_.

  1. Provision sufficient `access to Azure OpenAI <https://learn.microsoft.com/en-us/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai>`_ for your organization and access your `Azure portal <https://portal.azure.com/>`_.
  2. If you do not already have one, deploy an Azure AI Hub resource within Azure AI Studio
  3. Once the deployment is complete, navigate to the resource and select **Launch Azure AI Studio**.
  4. In the side navigation pane, select **Deployments** under **Shared resources**.
  5. Select **Deploy model** then **Deploy base model**.
  6. Select your model, such as `gpt-4o` and select **Confirm**.
  7. Select **Deploy** to start your model.
  8. In Mattermost, select **OpenAI Compatible** in the **Service** dropdown.
  9. In the **Endpoint** panel for your new model deployment, copy the base URI of the **Target URI** (everything up to and including `.com`) and paste it in the **API URL** field in Mattermost.
  10. In the **Endpoint** panel for your new model deployment, copy the **Key** and paste it in the **API Key** field in Mattermost.
  11. In the **Deployment** panel for your new model deployment, copy the **Model name** and paste it in the **Default Model** field in Mattermost.

.. tab:: OpenAI Compatible


  The OpenAI Compatible option allows integration with any OpenAI-compatible LLM provider, such as `Ollama <https://ollama.com/>`_:

  1. Deploy your model, for example, on `Ollama <https://ollama.com/>`_.
  2. Select **OpenAI Compatible** in the **AI Service** dropdown.
  3. Enter the URL to your AI service from your Mattermost deployment in the **API URL** field.
  4. If using Ollama, leave the **API Key** field blank.
  5. Specify your model name in the **Default Model** field.

Custom instructions
====================

Text input here is included in the prompt for every request. Use this to give your bots extra context or instructions. For example, you could list all of your organization's specific acronyms so the bot knows your vernacular and users can ask for definitions. Or you could give it specialized instructions such as adopting a specific personality or following a certain workflow. By customizing the instructions for each individual bot, you can create a more tailored AI experience for your specific needs.

Enable vision (Beta)
~~~~~~~~~~~~~~~~~~

Enabling vision allows images that are attached to posts to be sent to the upstream LLM for analysis. This requires that your upstream LLM supports these features. Only available with OpenAI and OpenAI-compatable services.

Disable tools (Beta)
~~~~~~~~~~~~~~~~~~~

Disabling tools will prevent the LLM from making function calls. This is useful when a model technically supports tool usage but you want to prevent it from being used within Mattermost. Try toggling this feature if you encounter unpredictable tool-related behavior with your model.

Copilot plugin metrics
~~~~~~~~~~~~~~~~~~~~~~~

Metrics for Copilot are exposed through the ``/plugins/mattermost-ai/metrics`` subpath under the existing Mattermost server metrics endpoint. This is controlled by the :ref:`Listen address for performance <configure/performance-monitoring-configuration-settings:listen address for performance>` configuration setting. It defaults to port ``8067``, and the following metrics are available:

- ``copilot_system_plugin_start_timestamp_seconds``: The time the plugin started.
- ``copilot_system_plugin_info``: The plugin version and installation ID.
- ``copilot_api_time_seconds``: How long to execute API.
- ``copilot_http_requests_total``: The total number of API requests.
- ``copilot_http_errors_total``: The total number of http API errors.
- ``copilot_llm_requests_total``: The total number of requests to upstream LLMs.

Integrations
~~~~~~~~~~~~

Currently integrations are limited to direct messages between users and the bots. The integrations won't operate from within public, private, or group message channels.

Jira
====

Issues with public Jira instances can be fetched. No configuration is required for this integration.

GitHub
======

If you have the Mattermost GitHub plugin enabled, you can use the integration to fetch issues and PRs from your public and private GitHub repositories. The user must be logged in to their GitHub account through the Mattermost GitHub plugin.

Upgrade
~~~~~~~

We recommend updating this integration as new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost.

Visit the `Releases page <https://github.com/mattermost/mattermost-plugin-ai/releases>`_ for the latest release, available releases, and compatibiilty considerations.

Usage
-----

See the :doc:`chat with Copilot </collaborate/chat-with-copilot>` documentation for details on using Copilot to overcome information overload and streamline communication and collaboration.
