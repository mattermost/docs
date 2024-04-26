Admin Guide: Mattermost AI Copilot
==================================

This document provides instructions for administrators to configure `Mattermost AI Copilot <https://github.com/mattermost/mattermost-plugin-ai>`_. For the corresponding user guide, refer to the `Mattermost AI Copilot end user documentation <../guides/mattermost-ai-copilot-user-guide.html>`_.

Mattermost AI Copilot is a plugin that comes preinstalled on Mattermost Server v9.7 or later, and can be configured in the System Console using the steps below. 

If you're running Mattermost Server v9.6 or earlier, AI Copilot must be installed using the `latest binary available for download from the plugin repository <https://github.com/mattermost/mattermost-plugin-ai/releases>`_ . For an optimized user experience and compatibility, we recommend using AI Copilot with Mattermost v9.7 and later; however, the AI Copilot plugin is compatible with the following `Mattermost Server versions <https://docs.mattermost.com/deploy/mattermost-changelog.html>`_:

- **v9.6** or later
- **v9.5.2+** (Extended Support Release - ESR)
- **v9.4.4+**
- **v9.3.3+**
- **v8.1.11+** (Extended Support Release - ESR)

Once the plugin is installed and enabled, proceed with the configuration steps below.

Configuration Steps
-------------------

Configure the plugin via **System Console ➡️ Mattermost AI Copilot Plugin**. The following AI services are supported:

- `OpenAI <https://platform.openai.com/account/api-keys>`_
- `Anthropic (Claude) <https://console.anthropic.com/account/keys>`_
- `Azure OpenAI <https://learn.microsoft.com/en-us/azure/ai-services/openai/overview>`_
- `Ask Sage <https://asksage.ai>`_
- `OpenAI Compatible <https://github.com/go-skynet/LocalAI>`_

OpenAI Configuration
--------------------

1. Obtain an `OpenAI API key <https://platform.openai.com/account/api-keys>`_.
2. Select **OpenAI** in the **AI Service** dropdown.
3. Enter your OpenAI API key in the **API Key** field.
4. Enter a model name in the **Default Model** field, such as `gpt-4` or `gpt-3.5-turbo`.
5. *(Optional)* If using multiple organizations on OpenAI, specify your **Organization ID** to direct API usage and billing accordingly.

Anthropic (Claude)
------------------

1. Obtain an `Anthropic API key <https://console.anthropic.com/account/keys>`_.
2. Select **Anthropic** in the **AI Service** dropdown.
3. Enter your Anthropic API key in the **API Key** field.
4. Specify a model name in the **Default Model** field, like `claude-v1`.

Azure OpenAI
------------

For integrating with Microsoft Azure's OpenAI services, `refer to the official documentation <https://learn.microsoft.com/en-us/azure/ai-services/openai/overview>`_.

1. Get `access to Azure OpenAI <https://learn.microsoft.com/en-us/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai>`_.
2. Create a new OpenAI resource in Azure.
3. Ensure your model resource on Azure does not auto-update.
4. In Mattermost, choose **OpenAI Compatible** in the **AI Service** dropdown.
5. Enter your Azure resource's URL in the **API URL** field.
6. Input your Azure resource API key in the **API Key** field.
7. Specify your model name in the **Default Model** field, for example, `gpt-3.5-turbo`.

Ask Sage
--------

Ask Sage is an experimental feature with certain limitations:

1. Obtain `access to Ask Sage <https://asksage.ai>`_.
2. Choose **Ask Sage** in the **AI Service** dropdown.
3. Enter your username and password for Ask Sage in the respective fields.
4. Specify a default model name, such as `gpt-4`.

OpenAI Compatible
-----------------

This option allows integration with any OpenAI-compatible LLM provider:

1. Deploy your model, for example, on LocalAI.
2. Select **OpenAI Compatible** in the **AI Service** dropdown.
3. Enter the URL to your AI service in the **API URL** field.
4. Enter your API key in the **API Key** field.
5. Specify your model name in the **Default Model** field.
