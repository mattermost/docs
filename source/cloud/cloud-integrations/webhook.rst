
Using Mattermost with Webhook
==============================

`Webhook <https://github.com/adnanh/webhook>`__ is a Golang application for setting up webhooks on a server with minimal configuration. It provides a simple way to trigger events on a server while keeping it separate from your web server.

Mattermost's outgoing webhooks feature  can be used with this fairly easily as long as you take a few things into account.

Sending information from Mattermost
------------------------------------

Mattermost's :doc:`interactive message buttons <../developer/interactive-messages>` send information using a parameter called "context." The easiest way to get all the information from Mattermost is to use the following configuration, which will pass the entire payload to your script as a string:


  {
  	"source": "entire-payload"
  }


Responding to the request
-------------------------

If you don't respond to the request you'll see an error in your Mattermost logs that looks like ``Action integration error [details: err=EOF]``.

To solve this, use the ``response-message`` configuration property to send back a response to prevent this. This response is sent immediately after receiving the webhook. 

If your script doesn't take very long to run you can use the ``include-command-output-in-response`` property to send that output to the Mattermost server.

Authenticating Requests
-----------------------

Mattermost can be configured to send a token with an outgoing webhook to make sure that your webhook only responds to authorized requests. To enable this, use the following in your webhook configuration:


    "trigger-rule":
    {
      "match":
      {
        "type": "value",
        "value": "<Outgoing webhook token>",
        "parameter":
        {
          "source": "request",
          "name": "token"
        }
      }
    }
