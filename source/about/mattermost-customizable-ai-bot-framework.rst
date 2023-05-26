.. _mattermost-customizable-chatgpt-bot-framework:

Customizable AI bot framework
=============================

Mattermost is committed to providing an open source platform for secure collaboration and control, especially in strict security environments. 

With a focus on AI augmentation and integration, Mattermost envisions providing an open source customizable AI bot framework with full control and data privacy for organizations that want to deploy AI solutions without sacrificing security.

The vision is to allow users to integrate generative AI solutions like OpenAI's ChatGPT and private cloud LLMs (Large Language Models) into their Mattermost workflows. This integration can streamline communication, enhance decision-making, and automate tasks, enabling increased speed and efficiency in government, defense, and technology organizations.

Control and data privacy
------------------------

Mattermost's open source platform provides verifiable privacy assurances, data control, and granular permissions solutions. As AI becomes more prevalent globally, organizations need control over the AI's access to their data and the ability to use private cloud AI solutions like `Azure AI <https://azure.microsoft.com/en-us/solutions/ai/#benefits>`_ or `AWS AI <https://aws.amazon.com/machine-learning/ai-services/>`_.

In the near term, this may involve integrating private-cloud AI with Mattermost, while in the long term, it could include training foundation models with an organization's data in a controlled environment.

Example open source Mattermost app AI framework
------------------------------------------------

The `mattermost/mattermost-ai-framework repository <https://github.com/mattermost/mattermost-ai-framework>`__ demonstrates a self-hosted AI app in a multi-user chat environment that can be fully private and off-grid AKA air-gapped. For demo purposes, deploy locally or in the browser via `Gitpod <https://github.com/mattermost/mattermost-ai-framework#gitpod>`__.

Example open source OpenAI plugin
---------------------------------

The `mattermost/mattermost-plugin-ai repository <https://github.com/mattermost/mattermost-plugin-ai>`__ demonstrates a self-hosted AI app in a multi-user chat environment that connects to the OpenAI API, streams responses, summarizes threads, and emoji reacts. It can be deployed locally for demo purposes.

Third-party example open source OpenAI plugin
----------------------------------

An example of an OpenAI integration is the  `open source OpenAI plugin for Mattermost <https://github.com/Brightscout/mattermost-plugin-openai>`_ developed by Brightscout:

1. Visit the `GitHub repository <https://github.com/Brightscout/mattermost-plugin-openai>`_ for the ChatGPT plugin.
2. Download the `latest release <https://github.com/Brightscout/mattermost-plugin-openai/releases>`_ from the **Releases** section.
3. Upload the release file to your Mattermost server by going to **System Console > Plugins > Plugin Management**.
4. Enable the plugin and configure it using your OpenAI API key.

Now, you can start using the OpenAI plugin in your Mattermost instance.

Two other examples of ChatGPT integrations built by Sebastian Müller include:

- `ChatGPT Mattermost Bot with OpenAI <https://github.com/yGuy/chatgpt-mattermost-bot>`__
- `ChatGPT Mattermost Bot with LLaMa <https://github.com/yGuy/chatgpt-mattermost-bot/tree/llama>`__

*The LLaMa version, however, is not available for commercial use due to licensing restrictions on the language model.*

Join the community
-------------------

To learn more about Mattermost's AI bot framework, share ideas, and contribute to the development, visit the `Mattermost AI developer blog <https://ai.mattermost.com>`__, join the `community channel <https://community.mattermost.com/core/channels/ai-exchange>`__, and check out the `peer-to-peer forums <https://forum.mattermost.com/c/ai-frameworks/40>`__ today.
