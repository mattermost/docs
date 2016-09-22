# Mattermost APIs

With Mattermost you have complete access to the server's [Web Service APIs](https://docs.mattermost.com/developer/api.html#mattermost-web-service-api), along with [language specific drivers](https://docs.mattermost.com/developer/api.html#mattermost-drivers) (the same used by the web, desktop and mobile experiences), plus [Slack-compatible webhooks](https://docs.mattermost.com/developer/api.html#incoming-webhooks) and [Slash commands](https://docs.mattermost.com/developer/api.html#slash-commands) for creating quick integrations. 

There's a [vibrant community developing open source apps on Mattermost](https://docs.mattermost.com/developer/api.html#community-apps-and-integrations) and you can start your work based on their code, or use [a pre-made sample](https://docs.mattermost.com/developer/api.html#matermost-golang-bot-sample) provided by the Mattermost team. 

Slack Compatible Webhooks & Slash Commands 
- [Incoming Webooks](https://docs.mattermost.com/developer/api.html#incoming-webhooks)
- [Outgoing Webooks](https://docs.mattermost.com/developer/api.html#outgoing-webhooks)
- [Slash Commands](https://docs.mattermost.com/developer/api.html#slash-commands)

API and Drivers 
- [Mattermost Web Service API](https://docs.mattermost.com/developer/api.html#mattermost-web-service-api)
- [Golang Driver](https://docs.mattermost.com/developer/api.html#golang-driver)
- [JavaScript Driver](https://docs.mattermost.com/developer/api.html#golang-driver)

Building API Integrations 
- [Mattermost Golang Bot Sample](https://docs.mattermost.com/developer/api.html#matermost-golang-bot-sample)
- [Community Apps and Integrations](https://docs.mattermost.com/developer/api.html#community-apps-and-integrations) 

## Slack-compatible Webhooks

To offer an alternative to propreitary SaaS services, Mattermost focuses on being "Slack-compatible, but not Slack limited". That means providing support for developers of Slack applications to easily extend their apps to Mattermost, as well as support and capabilities beyond what Slack offers. 

### [Incoming Webhooks](http://docs.mattermost.com/developer/webhooks-incoming.html)

Incoming webhooks allow external applications to post messages into Mattermost channels and private groups by sending a JSON payload via HTTP POST request to a secret Mattermost URL generated specifically for each application.

In addition to supporting Slack's incoming webhook formatting, Mattermost webhooks offer full support of industry-standard markdown formatting, including headings, tables and in-line images. 

### [Outgoing Webhooks](http://docs.mattermost.com/developer/webhooks-outgoing.html) 

Outgoing webhooks allow external applications to receive webhook events from events happening within Mattermost channels and private groups via JSON payloads via HTTP POST requests sent to incoming webhook URLs defined by your applications. 

Over time, Mattermost outgoing webhooks will support not only Slack applications using a compatible format, but also offer optional events and triggers beyond Slack's feature set. 

### [Slash Commands](http://docs.mattermost.com/developer/slash-commands.html) 

Slash commands, like outgoing webhooks, allow users to interact with external applications right from within Mattermost. The user will enter a / followed by a command, and optionally some arguments, then an HTTP request will be sent to an external application. What occurs next is decided by how the application responds to the HTTP request.

## Mattermost Web Service API

Mattermost offers a Web Service API accessible by Mattermost Drivers, listed below. See: 

- [Documentation for the transport layer for the web service](http://docs.mattermost.com/developer/web-service.html) 
- [Web Service API Reference](https://api.mattermost.com/) (Work in Progress)

## Mattermost Drivers

Mattermost drivers offer access to the Mattermost web service API in different languages and frameworks.

### [ReactJS Javascript Driver](https://github.com/mattermost/platform/blob/master/webapp/client/client.jsx)

[web-client.jsx](https://github.com/mattermost/platform/blob/master/webapp/client/client.jsx) - This Javascript driver connects with the ReactJS components of Mattermost. The web client does the vast majority of its work by connecting to a RESTful JSON web service. There is a very small amount of processing for error checking and set up that happens on the web server.

- The Javascript Driver is [mirrored in an external repository](https://github.com/mattermost/mattermost-driver-javascript) that can be included in custom projects. 

### [Golang Driver](https://github.com/mattermost/platform/blob/master/model/client.go)

[client.go](https://github.com/mattermost/platform/blob/master/model/client.go) - This is a RESTful driver connecting with the Golang-based webservice of Mattermost and is used by unit tests. 

- See [GoDocs](https://godoc.org/github.com/mattermost/platform/model) for documentation on the Golang Driver.

## Building API Integrations 

If you're building a deep integration with Mattermost, for example a mobile native client, and there is a driver available to support the programming language you are using, it's best to use the driver available to access the [Mattermost Web Service APIs](http://docs.mattermost.com/developer/web-service.html).

If no driver is available for the programming language of your choice, you can view the [Golang Driver](https://github.com/mattermost/platform/blob/master/model/client.go) source code to understand how it exercises the Web Service API. You can also learn more by reviewing open source projects that use the Web Service API, like [matterircd](https://github.com/42wim/matterircd).

There are a wide range of [installation guides](http://www.mattermost.org/installation/) for setting up your own Mattermost server on which to develop and test your integrations. 

## Mattermsot Golang Bot Sample (Driver Example) 

Mattermost provides a [Golang Bot Sample](https://github.com/mattermost/mattermost-bot-sample-golang) to demonstration how Mattermost works with the Golang driver and the APIs.

## Community Apps and Integrations 

The Mattermost community has shared back dozens of open source integrations showing how to use webhooks, drivers and APIs in different ways. See the [Community Applications Directory](https://www.mattermost.org/community-applications/) to learn more. 
