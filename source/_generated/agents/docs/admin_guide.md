# Mattermost Agents Admin Guide

This guide covers installing, configuring, and managing the Mattermost Agents plugin. You'll learn how to set up AI capabilities for your Mattermost instance and configure them for your organization's needs.

## Installation

### Prerequisites

Before installing the Agents plugin, ensure your environment meets these requirements:

- Mattermost Server v10.0+
- PostgreSQL database
- For semantic search: PostgreSQL with pgvector extension
- Network access to your chosen LLM provider
- API keys if using a cloud LLM service

### Installation Steps

#### Use pre-installed plugin

From Mattermost v10.3, Agents comes installed automatically and ready for you to configure a large language model (LLM). When no LLMs are configured, the Agents panel prompts users to configure one.

#### Install latest version

For the most recent features and improvements, you can download and install the latest plugin version from the [GitHub releases page](https://github.com/mattermost/mattermost-plugin-ai/releases). 

Install the plugin through the System Console by navigating to **System Console > Plugin Management**, clicking **Upload Plugin**, selecting the downloaded plugin file (.tar.gz), and clicking **Upload**. Enable the plugin after upload completes, then configure plugin settings as detailed in the Configuration section below.

## Configuration

### Access plugin settings

Navigate to **System Console > Plugins > Agents** to access the configuration interface.

### Enable the plugin

Agents is enabled automatically when using the pre-installed version. If you've manually installed a newer version, you may need to enable it by going to **System Console > Plugins > Agents** and setting **Enable Plugin** to **True**, then complete configuration in the System Console.

### Basic configuration

If you have an Enterprise, or Enterprise Advanced license, upload it to unlock additional features. If you don't have a license but are running Mattermost Enterprise Edition, an Entry license will be automatically applied for you.

For general settings, you can toggle to enable or disable the plugin system-wide, enable debug logging for troubleshooting (use only when needed), enable token usage logging for tracking LLM interactions, and configure the hostname allowlist for API calls.

### Agent configuration

Configure an LLM for your Agents integration by going to **System Console > Plugins > Agents** and selecting **Add an Agent**. The plugin supports creating multiple Agents with different configurations. See [license requirements](#license-requirements) for details on features that require a license.

Select **Add an Agent** to create a new Agent, then configure the agent settings:

| Setting | Description |
|---------|-------------|
| **Display Name** | User-facing name shown in Mattermost |
| **Agent Username** | The mattermost username for the agent. @ mentions to the agent will use this name |
| **Agent Avatar** | Custom image for the agent |
| **Service** | LLM provider for this agent (OpenAI, Anthropic, Cohere, Azure OpenAI, OpenAI-compatible) |
| **Send User ID** | Whether to send Mattermost user IDs to the LLM provider |
| **Default Model** | Specific model to use from your chosen provider |
| **Input Token Limit** | Maximum tokens allowed in input (model-dependent) |
| **Output Token Limit** | Maximum tokens allowed in output (model-dependent) |
| **Streaming Timeout Seconds** | Timeout in seconds for streaming responses |
| **Custom Instructions** | Custom instructions that define the agent's personality and capabilities |
| **Enable Vision** | Enable Vision to allow the agent to process images. Requires a compatible model. |
| **Enable Tools** | By default some tool use is enabled to allow for features such as integrations with JIRA. Disabling this allows use of models that do not support or are not very good at tool use. Some features will not work without tools. |
| **Access Control** | Set which teams, channels, and users can access this agent |

Select **Save** to create the agent.

### Provider configuration

For each LLM provider you want to use, you'll need to configure authentication. The basic requirements are:

| Provider | Required | Optional |
|----------|----------|----------|
| **OpenAI** | API Key | Organization ID |
| **Anthropic** | API Key | |
| **Cohere** | API Key | |
| **Azure OpenAI** | API Key, Resource Name, Deployment ID | |

See the [Provider Guide](https://docs.mattermost.com/agents/docs/providers.html) for detailed provider-specific configuration.

### Custom instructions

Text input in the custom instructions field is included in the prompt for every request. Use this to give your agents extra context or instructions. 

For example, you could list your organization's specific acronyms so the agent knows your vernacular and users can ask for definitions. Or you could give it specialized instructions like adopting a specific personality or following a certain workflow. By customizing the instructions for each individual agent, you can create a more tailored AI experience for your specific needs.

### Embed search configuration

To enable semantic search capabilities, you'll need to enable the `pgvector` extension in your PostgreSQL database, then configure embeddings provider settings including the provider (OpenAI, etc.), model for embeddings, and dimensions that match your chosen embedding model. Embedding search requires a license (see [license requirements](#license-requirements)) and is available as an [experimental](https://docs.mattermost.com/manage/feature-labels.html#experimental) feature. Performance may vary with large datasets.

Configure chunking options based on your needs:

| Setting | Recommended Value | Description |
|---------|-------------------|-------------|
| **Chunking Strategy** | Sentences, Paragraphs, or Fixed Size | Choose based on your content type |
| **Chunk Size** | 512-1024 tokens | Varies by strategy |
| **Chunk Overlap** | 20-50 tokens | For better context continuity |
| **Minimum Size Ratio** | Default | Minimum ratio for chunk size validation |

Run the initial indexing process after configuration.

### Permission configuration

Configure who can access AI features by setting team-level, channel-level, and user-level permissions for each agent.

## Management tasks

### Plugin metrics

Metrics for Agents are exposed through the `/plugins/mattermost-ai/metrics` subpath under the existing Mattermost server metrics endpoint. This is controlled by the Listen address for performance configuration setting. It defaults to port `8067`, and the following metrics are available:

- `agents_system_plugin_start_timestamp_seconds`: The time the plugin started.
- `agents_system_plugin_info`: The plugin version and installation ID.
- `agents_api_time_seconds`: How long to execute API.
- `agents_http_requests_total`: The total number of API requests.
- `agents_http_errors_total`: The total number of http API errors.
- `agents_llm_requests_total`: The total number of requests to upstream LLMs.

### Token usage tracking

The Agents plugin can track token usage for all LLM interactions to support billing and usage analytics. When enabled, token usage data is logged to a dedicated file at `logs/agents/token_usage.log` in JSON format, capturing detailed information about each request:

- **User ID**: The Mattermost user who initiated the request
- **Team ID**: The team context for the request
- **Bot Username**: Which agent was used for the interaction
- **Input Tokens**: Number of tokens in the request to the LLM
- **Output Tokens**: Number of tokens in the LLM response
- **Total Tokens**: Combined input and output token count

To enable token usage tracking, navigate to **System Console > Plugins > Agents** and set **Enable Token Usage Logging** to **True**. When enabled, log files automatically rotate when they reach 100MB in size, and rotated log files are compressed to save disk space. The token usage logs provide administrators with visibility into LLM usage patterns and can be used for cost tracking and resource planning. All major LLM providers (OpenAI, Anthropic) report usage data that gets captured by this logging system.

#### Converting token usage logs for analysis

The token usage log file contains one JSON object per line, which is not directly compatible with tools like Microsoft Excel. Use these commands to convert the logs to different formats. Each requires `jq` to be installed for easy JSON parsing:

**Convert to Excel-compatible JSON:**

```bash
jq -s '.' logs/agents/token_usage.log > token_usage.json
```

**Convert to CSV format:**

```bash
echo "timestamp,user_id,team_id,bot_username,input_tokens,output_tokens,total_tokens" > token_usage.csv
jq -r '[.timestamp, .user_id, .team_id, .bot_username, .input_tokens, .output_tokens, .total_tokens] | @csv' logs/agents/token_usage.log >> token_usage.csv
```

### Post indexing

Post indexing occurs automatically during initial setup and when changing embedding providers:

1. Navigate to **System Console > Plugins > Agents > Embedding Search**
2. Use the reindex controls to:
   
   - Monitor indexing progress during initial setup.
   - Trigger reindexing when changing embedding providers.
   - Check indexing status.

### Backup and restore

The plugin configuration is stored in the Mattermost database. To backup:

1. Ensure your regular Mattermost backup includes plugin configurations
2. For larger deployments, consider backing up indexed vector data separately

## Troubleshooting

### Logging

Enhanced logging can help diagnose issues:

1. Check server logs for entries with the structured logging field `plugin_ai` set to `mattermost-ai`.
2. Enable **LLM Trace** in the plugin configuration to see detailed request/response information for all LLM interactions.
3. Enable debug logging in the plugin configuration for additional diagnostic information.
4. For production environments, disable debug logging and LLM Trace after troubleshooting to reduce log volume.

## Integrations

Currently integrations are limited to direct messages between users and the agents. The integrations won't operate from within public, private, or group message channels.

### Built-in tool integrations

#### Server Search

- **Function**: Semantic search across Mattermost content.
- **Requirements**: Embedding search must be configured and enabled.
- **Security**: Respects user permissions - users only see content they have access to.

#### User Lookup

- **Function**: Look up Mattermost user information by username
- **Data Available**: Username, full name, email, nickname, position, locale, timezone, last activity, status
- **Permissions**: Requires `VIEW_MEMBERS` permission

#### Jira Integration

- **Function**: Fetch issues from public Jira instances
- **Requirements**: No additional configuration needed
- **Usage**: Provide Jira instance URL and issue keys
- **Data Retrieved**: Issue summary, description, status, assignee, comments, metadata

#### GitHub Integration

- **Function**: Fetch GitHub issues and pull requests
- **Requirements**: Mattermost GitHub plugin must be installed and running
- **Authentication**: Users must be logged into GitHub through the Mattermost GitHub plugin
- **Access**: Works with both public and private repositories (based on user permissions)
- **Data Retrieved**: Issue/PR title, number, state, submitter, body content

**Security Note**: All tool integrations are restricted to direct messages to maintain security boundaries and require explicit user approval before execution.

## Model Context Protocol (MCP) Integration

The Model Context Protocol (MCP) integration allows Agents to connect to external tools and services through standardized MCP servers. This [experimental](https://docs.mattermost.com/manage/feature-labels.html#experimental) feature enables expanding AI capabilities with custom integrations.

### Configuration

1. Navigate to **System Console > Plugins > Agents > MCP Servers**.
2. Enable MCP integration by setting **Enable MCP** to **True**.
3. Configure connection settings:
   
   - **Idle Timeout**: Set timeout in minutes for inactive client connections (default: 30 minutes)

### Add MCP servers

1. Select **Add MCP Server** to configure a new server.
2. Configure server settings:
   
   - **Server URL**: The endpoint URL for your MCP server.
   - **Custom Headers**: Additional headers required by your MCP server (optional).
   - **Server Name**: Descriptive name for the server (auto-generated if not provided).
     
4. Select **Save** to add the server.

### Management

- **Connection Management**: The system automatically manages user connections to MCP servers
- **Idle Cleanup**: Inactive client connections are automatically closed after the configured timeout
- **Per-User Connections**: Each user gets their own connection to MCP servers for security and isolation

> **Note:** The plugin currently doesn't render Markdown links (e.g., JIRA ticket links) in bot responses. URLs are displayed in plain text rather than as clickable Markdown-rendered links. This is not a bug but intended security behavior to prevent potential data exfiltration through links. While this limitation exists, improvements to link handling are being considered for future development. 

### License requirements

The following table outlines which features require a license:

| Feature | License Required |
|---------|------------------|
| Basic agent configuration (single agent) | No license required |
| Chat with agents in DMs and channels | No license required |
| Image analysis (vision capabilities) | No license required |
| Basic tool integrations | No license required |
| Multiple agent configurations | Entry, Enterprise, and Enterprise Advanced |
| Fine-grained access controls | Entry, Enterprise, and Enterprise Advanced |
| Embedding search (semantic AI search) | Entry, Enterprise, and Enterprise Advanced |
| MCP Support | Entry, Enterprise, and Enterprise Advanced |
| Usage analytics and token tracking | Entry, Enterprise, and Enterprise Advanced |
| AI Actions menu (thread summarization) | Entry, Enterprise, and Enterprise Advanced |
| Channel summarization (unread messages) | Entry, Enterprise, and Enterprise Advanced |
| Recorded meeting transcripts and summarization | Entry, Enterprise, and Enterprise Advanced |

