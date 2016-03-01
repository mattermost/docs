# Executing Commands
___
Slash commands allow users to perform operations in Mattermost or interact with external applications by typing into the text input box. A user will enter a `/` followed by a command and some arguments to perform actions. There are built-in slash commands that come with all Mattermost installations, and optionally, custom slash commands may be configured to interact with external applications. To learn more about configuring custom slash commands, please visit the [developer slash command documentation page](../developer/slash-commands.md).

## Built-in Commands

The following slash commands are available on all Mattermost installations:

![commands](../../images/slashCommandsTable.PNG)

Begin by typing `/` and a list of slash command options appears above the text input box. The autocomplete suggestions help by providing a format example in black text and a short description of the slash command in grey text.

![autocomplete](../../images/slashCommandsAutocomplete.PNG)

## Custom Commands
Custom slash commands are used to integrate with external applications. For example, a team might configure a custom slash command to check internal health records with `/patient joe smith` or check the weekly weather forcast in a city with `/weather toronto week`. Check with your System Admin or open the autocomplete list by typing `/` to find out if your team has configured any custom slash commands.

Custom slash commands are disabled by default and can be enabled by the System Admin in the System Console > Service Settings. To learn more about configuring custom slash commands, please visit the [developer slash command documentation page](../developer/slash-commands.md).
