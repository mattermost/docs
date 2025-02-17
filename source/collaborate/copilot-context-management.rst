Copilot Context Management
=========================


.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:


Copilot is designed to handle context efficiently, ensuring that only necessary information is sent to the Large Language Model (LLM) for generating accurate responses. This document outlines how Copilot processes and includes relevant context. The company name, the server name and the time are always passed to the LLM to ensure accurate and contextually relevant responses.


.. note::
  **Ensuring Data Privacy**

  To prevent any sensitive data—including personally identifiable information (PII) and message content—from being shared with an external LLM hosting vendor, it is advisable to run the LLM locally. This setup ensures that data privacy is maintained while still leveraging Copilot’s capabilities. Because Copilot relies on sharing specific user details and other PII (such as message content) with the LLM to function effectively, hosting the model on-premises is the only suitable option for customers with strict data privacy requirements.


Direct Messages to the Copilot Bot
------------------------------------

When you send a direct message to the Copilot bot, the context sent to the LLM includes:

- The profile information of the user sending the prompt
- Chat messages exchanged between the user and the bot


**Additional Context in Direct Messages**

When the "Enable Tools" bot configuration option is enabled (default: true), additional context may be sent to the LLM, depending on the prompt. This includes:

- Jira tickets (public tickets)

  - Example: Summarize the Jira ticket: <LINK TO TICKET>

- GitHub issues

  - Example: Summarize the GitHub issue: <LINK TO ISSUE>

- User data

  - Example: What is @Bob's position?


@-Mentions in Channels
------------------------

For @-mentions in channels, the context includes:

**Standalone Messages (@-mentions in a channel)**

- The post containing the @-mention, including any attachments
- The channel name and display name
- The team name and display name
- The profile information of the user sending the prompt

**Threaded Messages (@-mentions in a thread)**

- Everything sent when used in a standalone message
- Messages within the thread, including the usernames of the users involved, as well as any attachments and their filenames

**Differences Between Standalone and Threaded Messages:**

- For @-mentions in standalone messages, the context includes only the mentioned post
- For @-mentions in threads, the entire thread's messages are included, along with usernames of the authors of the messages


Built-in Ways to Trigger Copilot
---------------------------------

In addition to regular chat interactions, Copilot provides specialized features where extra context is sent to the LLM. Each one provides specialized context tailored to the task being performed. Below are the scenarios where extra context is sent to the LLM:

- **Thread Summarization**: Includes thread messages and the usernames of the authors
- **Meeting Summar**: Incorporates transcriptions from calls
- **Channel Summary Since Last Visit Feature**: Uses channel posts along with their authors to create summaries.
- **Finding Action Items & Open Questions Features**: Analyzes thread and channel messages to identify action items or open questions