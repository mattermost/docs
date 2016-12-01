# Mattermost APIs

With Mattermost you have complete access to the server's [Web Service APIs](https://docs.mattermost.com/developer/api.html#mattermost-web-service-api), along with [language specific drivers](https://docs.mattermost.com/developer/api.html#mattermost-drivers) (the same used by the web, desktop and mobile experiences).

There's a [vibrant community developing open source apps on Mattermost](https://docs.mattermost.com/developer/api.html#community-apps-and-integrations) and you can start your work based on their code, or use [a pre-made sample](https://docs.mattermost.com/developer/api.html#matermost-golang-bot-sample) provided by the Mattermost team.

## Mattermost Web Service API

To learn more about the Mattermost Web Service API, see the references listed below:

- [API Reference for latest Mattermost release](https://api.mattermost.com/)
- [API Reference for master branch](https://api.mattermost.com/master.html)

We accept bug reports and contributions to our API references at [our repository here](https://github.com/mattermost/mattermost-api-reference).

## Mattermost Drivers

Mattermost drivers offer access to the Mattermost web service API in different programming languages and frameworks.

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

## Mattermost Golang Bot Sample (Driver Example)

Mattermost provides a [Golang Bot Sample](https://github.com/mattermost/mattermost-bot-sample-golang) to demonstration how Mattermost works with the Golang driver and the APIs.

## Community Apps and Integrations

The Mattermost community has shared back dozens of open source integrations showing how to use webhooks, drivers and APIs in different ways. See the [Community Applications Directory](https://www.mattermost.org/community-applications/) to learn more.
