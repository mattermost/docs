# Mattermost Agents URL Rendering Configuration

## Overview

Mattermost Agents are configured to handle URL rendering in a specific way to ensure security and maintain a clean chat experience.

## URL Rendering Behavior

**Important**: Mattermost Agents do not render clickable links in bot responses. This is a security feature designed to:

- Prevent potential security risks from malicious URLs
- Maintain a clean, text-based response format
- Ensure consistent bot behavior across different channels

### What This Means

When Mattermost Agents respond with content that contains URLs:
- URLs are displayed as plain text
- Links are not automatically converted to clickable elements
- Users must manually copy and paste URLs to navigate to them

### Examples

**Agent Response Format:**
```
Visit our documentation at https://docs.mattermost.com for more information.
```

**What Users See:**
The URL `https://docs.mattermost.com` appears as plain text and is not clickable.

### Configuration Notes

This URL rendering behavior is:
- **Built-in**: Part of the core Mattermost Agents functionality
- **Non-configurable**: Cannot be changed through system settings
- **Security-focused**: Designed to prevent potential security vulnerabilities
- **Consistent**: Applied to all agent responses regardless of channel or user

### Best Practices

When configuring Mattermost Agents:
1. Inform users that URLs in bot responses will appear as plain text
2. Consider providing instructions for copying URLs when necessary
3. Use clear, descriptive text around URLs to provide context
4. Train agents to provide concise, helpful text along with any URLs

## Related Configuration

This URL rendering behavior works in conjunction with other Mattermost Agents security features:
- Content filtering
- Response validation
- User permission checks
- Channel-specific configurations

For more information about configuring Mattermost Agents, see the [Agents Admin Guide](agents-admin-guide.rst).