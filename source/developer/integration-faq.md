# Integrations FAQ
---

## What's the difference between incoming and outgoing webhooks? 

A webhook is a way for one app to send real-time data to another app. 

In Mattermost, incoming webhooks receive data from external applications and make a post in a specified channel. They're great for setting up notifications when something happens in an external application. 

Outgoing webhooks take data from Mattermost, and send it to an external application. Then the outgoing webhook can post a response back in Mattermost. They're great for listening in on channels, and then notifying external applications when a trigger word is said. 

## What is a slash command? 

A slash command is similar to an outgoing webhook, but instead of listening to a channel it is used as a command tool. This means if you type in a slash command it will not be posted to a channel, whereas an outgoing webhook is only triggered by posted messages. 

## What does Slack compatible mean?

Slack compatible means that Mattermost accepts integrations that have a payload in the same format as Slack.  

If you have a Slack integration, you should be able to set it up in Mattermost without changing the format.   

## What if I have a webhook from somewhere other than Slack? 

If you have an integration that outputs a payload in a different format you need to write an intermediate application to act as a translation layer to change it to the format Mattermost uses. Since there’s currently no general standard for webhook formatting, this is unavoidable and just a part of how webhooks work. 

If there's no translation layer, Mattermost won't understand the data you're sending. 

## What are attachments? 

When "attachments" are mentioned in the integrations documentation, it refers to Slack's Message Attachments. These "attachments" can be optionally added as an array in the data sent by an integration, and are used to customize the formatting of the message.

We currently don't support the ability to attach files to a post made by an integration. 

## What do I do if my webhook post is too long?

We recommend breaking up the information into separate posts. 

If you're interested in Mattermost automatically splitting up integration posts that are too long, please [upvote this feature idea](https://mattermost.uservoice.com/forums/306457-general/suggestions/13878750-automatically-break-long-responses-from-integratio), or comment if it's something you would be interested in working on. 

If you would like to suggest alternative solutions, please [discuss here](https://forum.mattermost.org/t/recommendations-for-handling-automation-that-wants-to-post-messages-longer-than-4000-characters-per-message/1393).

## Where should I install my integrations? 

If you want to keep all your integrations on your own servers, we suggest the following as general guidelines:


- Small Organizations: Set integrations up on the same server machine Mattermost runs on.  
- Medium-sized Organizations: Set up a separate server machine just for integrations.  
- Large Organizations: Consider using a different box for each integration.  

These are approximate suggestions, but overall where you install your integrations should be dependent on how many integrations you have, how often they’re used, and the size of your team. 

If it’s not necessary for your organization to host their own integrations, we recommend using a hosting service such as Heroku.
