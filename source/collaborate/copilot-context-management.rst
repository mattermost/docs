Copilot context management
===========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Copilot is designed to handle context efficiently, ensuring that only necessary information is sent to the Large Language Model (LLM) for generating accurate responses. This document outlines how Copilot processes and includes relevant context. The company name, the server name, and the time are always passed to the LLM to ensure accurate and contextually relevant responses.

.. note::
  **Ensure data privacy**

  We recommend that customers with strict privacy requirements run the LLM locally to prevent sensitive data, including personally identifiable information (PII) and message content, from being shared with an external LLM hosting vendor. This ensures data privacy while enabling Copilot’s functionality.

Direct messages to the Copilot Bot
------------------------------------

When you send a direct message to the Copilot bot, the context sent to the LLM includes:

- The profile information of the user sending the prompt.
- Chat messages exchanged between the user and the bot.

**Additional context in direct messages**

By default, some tool use is enabled to allow for features such as integrations with JIRA, and additional context may be sent to the LLM, depending on the prompt that includes:

- Jira tickets (public tickets)

  - Example: Summarize the Jira ticket: <LINK TO TICKET>

- GitHub issues

  - Example: Summarize the GitHub issue: <LINK TO ISSUE>

- User data

  - Example: What is @Bob's position?

@-Mentions in channels
------------------------

When you @-mention Copilot in a channel, the context sent to the LLM includes:

**Standalone messages (@-mentions in a channel)**

- The message containing the @-mention, including any attachments.
- The channel name and display name.
- The team name and display name.
- The profile information of the user sending the prompt.

**Threaded messages (@-mentions in a thread)**

- Everything sent when used in a standalone message.
- Messages within the thread, including the usernames of the users involved, as well as any attachments and their filenames.

**Context differences between standalone and threaded messages:**

- For @-mentions in standalone messages, the context includes only the mentioned message.
- For @-mentions in threads, the entire thread's messages are included, along with usernames of the authors of the messages.

Built-in ways to trigger Copilot
---------------------------------

In addition to regular chat interactions, Copilot provides specialized features where extra context is sent to the LLM. Each feature provides specialized context tailored to the task being performed. Below are the scenarios where extra context is sent to the LLM:

- **Thread summarization**: Includes thread messages and the usernames of the authors
- **Meeting summary**: Incorporates transcriptions from calls
- **Channel summary since last visit**: Uses channel posts along with their authors to create summaries.
- **Finding action items & open questions**: Analyzes thread and channel messages to identify action items or open questions.