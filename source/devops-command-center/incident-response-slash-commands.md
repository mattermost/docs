## What are slash commands?

Slash commands are shortcuts used to perform actions in Mattermost. To view the available slash commands in Mattermost begin by typing `/` and a list of slash command options appears above the text input box. The autocomplete suggestions help by providing a format example in black text and a short description of the slash command in grey text.

## Using slash commands

Mattermost Incident Management includes built-in slash commands:

- `/incident start` - Start a new incident.
- `/incident end` - Close the incident of that channel.
- `/incident restart` - Restart a closed incident.
- `/incident check [checklist #] [item #]` - Check/uncheck the checklist item.
- `/incident announce ~[channels]` - Announce the current incident in other channels.
- `/incident list` - List all your incidents.
- `/incident commander [@username]` - Show or change the current commander.
- `/incident info` - Show a summary of the current incident.
- `/incident stage [next/prev]` - Move to the next or previous stage.

## Adding slash commands to tasks

Slash commands can be added to tasks to initiate actions as part of your incident response playbook.

Here are some examples:

- Add a task called **Sync up** with the slash command `/zoom hello`. Running that slash command initiates a Zoom call in the incident channel. If you've installed Jitsi, you could use `/jitsi hello`. 

![Tasks and slash commands](../assets/stage_task_slashcommand.png)

- One of your tasks may require the header to be changed to reflect a new status. Create a task called **Change header** with the slash command `/header new header`.

![Tasks and slash commands](../assets/stage_task_header.png)
