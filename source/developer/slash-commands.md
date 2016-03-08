# Slash Commands

Slash commands, like outgoing webhooks, allow users to interact with external applications right from within Mattermost. The user will enter a `/` followed by a command, and optionally some arguments, then an HTTP request will be sent to an external application. What occurs next is decided by how the application responds to the HTTP request.

A couple key points:

- **Mattermost slash commands are Slack-compatible.** If you've used Slack's slash commands to interact with external applications, you can reuse those same applications with Mattermost. Mattermost will automatically translate Slack's proprietary JSON payload format into markdown to render in Mattermost messages
- **Custom commands support auto-complete.** When you a create a custom command for your teammates, you have the option to fill in information about how auto-complete should work with that command. This gives your teammates quick and easy access to use your custom slash command

_Example:_

Suppose you had an external application that had the ability to check the weather for certain cities. By creating a custom slash command, and setting up the application to handle the HTTP POST or GET from the command, you could allow your users to check the weather in their city using your command. For example, a user might be able to type:

`/weather toronto week`

Your external weather application would receive an HTTP request letting it know the user is interested in Toronto and would like to know the weather for the week. The application could simply respond to the HTTP request with the following JSON payload:

```
{"response_type": "in_channel", "text": "
---
#### Weather in Toronto, Ontario for the Week of February 16th, 2016

| Day                 | Description                      | High   | Low    |
|:--------------------|:---------------------------------|:-------|:-------|
| Monday, Feb. 15     | Cloudy with a chance of flurries | 3 °C   | -12 °C |
| Tuesday, Feb. 16    | Sunny                            | 4 °C   | -8 °C  |
| Wednesday, Feb. 17  | Partly cloudly                   | 4 °C   | -14 °C |
| Thursday, Feb. 18   | Cloudy with a chance of rain     | 2 °C   | -13 °C |
| Friday, Feb. 19     | Overcast                         | 5 °C   | -7 °C  |
| Saturday, Feb. 20   | Sunny with cloudy patches        | 7 °C   | -4 °C  |
| Sunday, Feb. 21     | Partly cloudy                    | 6 °C   | -9 °C  |
---
"}
```
Which would render in a Mattermost message as follows:
![weather bot](../images/weatherBot.PNG)

### Built-in Commands
Each Mattermost installation comes with some built-in slash commands that are ready to use. These commands are listed below:

![commands](../images/slashCommandsTable.PNG)

### Enabling Custom Commands
Custom slash commands are off by default, and can be enabled by the system administrator. If you are the system administrator you can enable them by doing the following:

1. Login to your Mattermost team account that has the system administrator role.
2. Enable slash commands from **System Console -> Service Settings**.
3. (Optional) Configure the **Enable Overriding Usernames from Webhooks and Slash Commands** option to allow custom slash commands to post under any name. If not enabled, the username of the user who activated the command will be used
4. (Optional) Configure the **Enable Overriding Icon from Webhooks and Slash Commands** option to allow custom slash commands to post using any icon. If not enabled, the icon of the user who activated the command will be used
5. (Optional) Configure the **Enable Integrations for Admin Only** option to allow only system and team admins to create slash commands

### Set Up a Custom Command
Once slash commands are enabled, you will be able to set some up through the Mattermost UI. You can do so by following these steps:

1. Login to your Mattermost team site and go to **Account Settings -> Integrations**
2. Next to **Slash Commands** click **Edit**
3. Under **Add a new command** select your options
   1. Fill in **Command Trigger Word**, this will be the word that is your command
   2. Enter a **Request URL** that will be the endpoint Mattermost hits to reach your external application
   3. Select an HTTP **Request Method** from the dropdown
   4. (Optional) Type in a **Response Username** that will be used with any messages your command responds with
   5. (Optional) Enter the URL to a **Reponse Icon** that will be used with any messages your command responds with
   6. (Optional) Check the **Show this command in the autocomplete list.** to let users autocomplete your command
   7. (Optional) Fill in an **Autocomplete Hint** to let users know about possible arguments to your command
   8. (Optional) Add an **Autocomplete Description** to help users understand your command
   9. (Optional) Type in a **Descriptive Label** to provide a bit more information about your command
4. Click **Add** to add your command to the system
5. Your new slash command will be displayed below with a **Token** that your external application should use to verify the request came from Mattermost

### Creating Integrations with Commands
If you'd like to build your own integration that uses slash commands, you can follow these general guidelines:

1. In the programming language of your choice, write your integration to perform what you had in mind
    1. Your integration should have a function for receiving HTTP POSTs or GETs from Mattermost that look like this example:
        ```
        Content-Length: 244
        User-Agent: Go 1.1 package http
        Host: localhost:5000
        Accept: application/json
        Content-Type: application/x-www-form-urlencoded

        channel_id=cniah6qa73bjjjan6mzn11f4ie&
        channel_name=town-square&
        command=/somecommand&
        response_url=not+supported+yet&
        team_domain=someteam&
        team_id=rdc9bgriktyx9p4kowh3dmgqyc&
        text=hello+world&
        token=xr3j5x3p4pfk7kk6ck7b4e6ghh&
        user_id=c3a4cqe3dfy6dgopqt8ai3hydh&
        user_name=somename
        ```
    2. Your integration must have a configurable **MATTERMOST_TOKEN** variable that is the Token given to you when you set up the custom command in Mattermost as decribed in the previous section _Set Up a Custom Command_. This configurable **MATTERMOST_TOKEN** must match the token in the request body so your application can be sure the request came from Mattermost
    3. If you want your integration to post a message back to the same channel, it can respond to the HTTP POST request from Mattermost with a JSON response body similar to this example:
        ```
        {
          "response_type": "in_channel",
          "text": "This is some response text."
        }
        ```
        - Change `response_type` to "ephemeral" to have the message appear temporarily and only display to the user who activated the command
        - Use the field `goto_location` with a URL as the value to redirect the user of the command to a webpage
2. Set up your integration running on Heroku, an AWS server or a server of your own to start using your application from within Mattermost

Additional Notes:

1. As mentioned previously, [markdown](../../usage/Markdown.md) can be used to create richly formatted responses, for example: ```{"text": "# A Header\nThe _text_ below **the** header."}``` creates a messages with a header, a carriage return, italicized text for "text" and bold text for "the"

2. Just like regular posts, the text in a response will be limited to 4000 characters at maximum

### Slack Compatibility

As mentioned above, Mattermost makes it easy to take integrations written for Slack's proprietary JSON payload format and repurpose them to become Mattermost integrations. The following automatic translations are supported:

1. The HTTP POST and GET request body is formatted the same as Slack's, which means your Slack integration's receiving function should not need to change at all to be compatible with Mattermost
2. JSON responses designed for Slack using `<>` to note the need to hyperlink a URL, such as ```{"text": "<http://www.mattermost.com/>"}```, are translated to the equivalent markdown in Mattermost and rendered the same as you would see in Slack
3. Similiarly, responses designed for Slack using `|` within a `<>` to define linked text, such as ```{"text": "Click <http://www.mattermost.com/|here> for a link."}```, are also translated to the equivalent markdown in Mattermost and rendered the same as you would see in Slack

#### Known Issues in v2.0

- Conversion of Slack attachments and link conversion isn't working
- Disabling slash commands from the system console only disables creation, not execution of user created slash commands
- /me command sometimes posts as the webhook bot instead of the user


### Pre-Released feature : Enabling external application to offer slash command autocomplete

**Please note that you may experience lag as autocomplete request goes to Mattermost server, then to 3rd party, then back, then back on every keystroke.**

#### What problem does it solve

If your team relies heavily on slash commands, managing them directly in mattermost can become painfull.
You have to create them one by one, add a trigger, an url, etc…

With this feature, you will be able to add them on an external application the way you decided to.
So you can manage roles on your side to offer commands to selected users.

Another problem is that the auto-completion only works with command names, not their arguments.
For commands that needs some object ids, you have to remember them, and mistakes may be dangerous.

With this approach, you can send your own suggestions based on the current command content.
This allows you to prevent any errors as your users don't have to remember anything.

This post exposes the idea (originally based on outgoing webhooks): https://forum.mattermost.org/t/add-suggestion-autocompletion-webhook-setting/460

#### Setup

Under Account Settings > Advanced > Preview pre-released features check `Enable external application to offer slash command autocomplete`

Under Account Settings / Integration / Slash Commands, **add only one new with this params** (others params are not needed and untested for now, and having several ones breaks everything, more known bugs below)

- check "Enable external application to offer autocomplete"
- leave trigger blank
- enter an url
- keep POST format

#### Slash command auto-completion

When `/` is entered in text box, and with any additional keystroke, a request is made to the url with this payload:
```
{
  channel_id: 'xxxxx',
  channel_name: 'xxxxx',
  command: '<text box first word including />',
  response_url: 'not supported yet',
  suggest: 'true',
  team_domain: 'xxxxx',
  team_id: 'xxxxx',
  text: '<remaining text box content>',
  token: 'xxxxx',
  user_id: 'xxxxx',
  user_name: 'xxxxx'
}
```

ie: if `/start webserver alpha` is typed in text box, we'll have this
payload:
```
{
  channel_id: 'xxxxx',
  channel_name: 'xxxxx',
  command: '/start',
  response_url: 'not supported yet',
  suggest: 'true',
  team_domain: 'xxxxx',
  team_id: 'xxxxx',
  text: 'webserver alpha'
  token: 'xxxxx',
  user_id: 'xxxxx',
  user_name: 'xxxxx'
}
```

The server must respond with an array of objects:
```
[
    {
        auto_complete_desc: <command description>,
        external_management: true,
        trigger: <command trigger>
    }
]
```

ie, with '/sta' in the text box:
```
[
    {
        "auto_complete_desc": "start sub command  webserver
description",
        "external_management": true,
        "trigger": "start webserver"
    },
    {
        "auto_complete_desc": "start sub command  dbserver description",
        "external_management": true,
        "trigger": "start dbserver"
    },
    {
        "auto_complete_desc": "start sub command  coffeeMachine
description",
        "external_management": true,
        "trigger": "start coffeeMachine"
    }
]
```

#### Command execution

Then, when command is send, regular slash command system is used:
same payload is send, but without `suggest` param:
```
{
  channel_id: 'xxxxx',
  channel_name: 'xxxxx',
  command: '<text box first word including />',
  response_url: 'not supported yet',
  team_domain: 'xxxxx',
  team_id: 'xxxxx',
  text: '<remaining text box content>',
  token: 'xxxxx',
  user_id: 'xxxxx',
  user_name: 'xxxxx'
}
```

Server must return this:
```
{
    "response_type": "in_channel",
    "text": <command output>,
}
```

#### Known bugs

##### Multiple setup breaks everything
If you use more than one slash command autocomplete, no auto-complete suggestions are shown, even the built in ones.

##### Double trigger character
Sometimes, an extra `/` is added at the beginning of the text box content.

##### Sub auto-completion

When selecting first auto-completed command in the suggestion box, keystroke is needed to get sub auto-completion triggered. It should be triggered instantly.
