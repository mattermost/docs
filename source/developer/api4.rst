APIv4 Contribution Processes
============================

`Mattermost API version 4 <https://docs.google.com/document/d/197JwEBMnK8okFilTfGSpbsrXPY5RZOJ4gG2DXwcbwYE/edit>`_ is an active and on-going project. We're
looking for contributors to code server endpoints, build drivers and
write documentation. If you're interested `please join our Mattermost
instance <https://pre-release.mattermost.com/signup_user_complete/?id=f1924a8db44ff3bb41c96424cdc20676>`__
and join the `APIv4
channel <https://pre-release.mattermost.com/core/channels/apiv4>`__.

This page will describe the processes for contributing to APIv4. If you
have questions please ask in the `APIv4
channel <https://pre-release.mattermost.com/core/channels/apiv4>`__. The
project leads are Joram Wilander (@joram) on development and Jason Blais
(@jason) on product management.

Adding an Endpoint
------------------

To add an endpoint to API version 4, each item must be completed on the
following checklist:

-  `Select an endpoint to
   implement <https://docs.mattermost.com/developer/api4.html#selecting-an-endpoint>`__
-  `Document the
   endpoint <https://docs.mattermost.com/developer/api4.html#documenting-the-endpoint>`__
-  `Implement the API handler on the
   server <https://docs.mattermost.com/developer/api4.html#implementing-the-api-handler>`__
-  `Add a function to the Go
   driver <https://docs.mattermost.com/developer/api4.html#updating-the-go-driver>`__
-  `Write a unit
   test <https://docs.mattermost.com/developer/api4.html#writing-a-unit-test>`__
-  `Submit your
   implementation! <https://docs.mattermost.com/developer/api4.html#submitting-your-pull-request>`__

A full example can be found through these two pull requests:

-  `Documenting the ``POST /teams`` endpoint <>`__
-  `Implementing the ``POST /teams`` endpoint <>`__

Selecting an Endpoint
~~~~~~~~~~~~~~~~~~~~~

Select an endpoint `from the progress spreadsheet <https://docs.google.com/spreadsheets/d/1nPoLgwh_9zRFECpqRUZAKIWihCmX27pnDtFGLtG_WnY/edit#gid=0>`__ that you would
like to implement and post in the `APIv4
channel <https://pre-release.mattermost.com/core/channels/apiv4>`__,
letting us know that you'd like to work on it. One of us will then
update the spreadsheet so other contributors know you're implementing the
endpoint.

If you have a suggestion for an endpoint that is not on the spreadsheet,
let us know and we will consider adding it.

Documenting the Endpoint
~~~~~~~~~~~~~~~~~~~~~~~~

At Mattermost we use the `OpenAPI
specification <https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md>`__
for API documentation. That documentation lives in the
`mattermost-api-reference <https://github.com/mattermost/mattermost-api-reference>`__
repository. To document an endpoint, follow these steps:

1. Fork
   `mattermost-api-reference <https://github.com/mattermost/mattermost-api-reference>`__
   and create a branch for your changes.
2. Find the ``.yaml`` file in the
   `/source/v4 <https://github.com/mattermost/mattermost-api-reference/tree/master/source/v4>`__
   directory that fits your endpoint.

   -  For example, if you were adding the ``GET /users/{user_id}`` endpoint
   you would be looking for
   `users.yaml <https://github.com/mattermost/mattermost-api-reference/tree/master/source/v4/users.yaml>`__
   -  If the file doesn't exist yet, you might need to create it and update
   the
   `Makefile <https://github.com/mattermost/mattermost-api-reference/tree/master/Makefile>`__
   to include it

3. Copy an existing endpoint from the same or a different file.
4. Update the documention you copied with the correct information for
   your endpoint, including:

   -  Tag - The resource type
   -  Summary - A few word summary
   -  Description - A brief 1-2 sentence description
   -  Permissions - The permission required
   -  Parameters - The URL and body parameters
   -  Responses - The success and error responses

5. Confirm you don't have any syntax errors by running ``make build-v4``
   and copying ``/html/static/mattermost-openapi-v4.yaml`` into the
   `Swagger editor <http://editor.swagger.io>`__.
6. Commit your changes and submit a pull request to
   `mattermost-api-reference <https://github.com/mattermost/mattermost-api-reference>`__.

If you're looking for examples, see
`users.yaml <https://github.com/mattermost/mattermost-api-reference/tree/master/source/v4/users.yaml>`__.

Implementing the API Handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To implement the API handler you'll first need to `setup your developer
environment <https://docs.mattermost.com/developer/developer-setup.html>`__, then follow these steps:

1. Add the declaration for your endpoint.

   -  For example, see
   `/api4/user.go <https://github.com/mattermost/platform/tree/master/api4/user.go>`__

2. Implement the handler for your endpoint.

   -  The general pattern for handlers is 
   
   .. code-block::
   
     func handlerName(c *Context, w http.ResponseWriter, r *\ http.Request) { 
     
       // 1. Parsing of request URL and body

       // 2. Permissions check if required

       // 3. Invoke logic through the app package

       // 4. (Optional) Check the Etag

       // 5. Format the response and write the response 
     }

   - For examples, see the [updateUser()](https://github.com/mattermost/platform/tree/master/api4/user.go#L86) and the [getUser()](https://github.com/mattermost/platform/tree/master/api4/user.go#L58) handlers 

3. Run the server using ``make run-server`` to check for syntax errors. 
4. (Optional) Use ``curl`` or `Postman <https://www.getpostman.com/>`__ to test the basics of your endpoint. 
   - This step is optional since you can use the unit test you're going to write to test the endpoint

Updating the Go Driver
~~~~~~~~~~~~~~~~~~~~~~

The Go driver for APIv4 is in
`/model/client4.go <https://github.com/mattermost/platform/tree/master/model/client4.go>`__.
To add a function to support your new endpoint:

1. Copy an existing driver function, such as
   `CreateUser <https://github.com/mattermost/platform/tree/master/model/client4.go#L186>`__.
2. Paste the function into the section for your endpoint.

   -  For example, ``POST /teams`` would go in the Teams section

3. Modify the function to correctly hit your endpoint.

   -  Make sure to update the request method to match your endpoint's HTTP
   method

That's it, you'll be able to test your function in the next section.

Writing a Unit Test
~~~~~~~~~~~~~~~~~~~

The most important part of this process is to make sure your endpoint
works correctly. Follow these steps to write a test:

1. Open the test Go file related to your endpoint.

   -  For example, if you put your handler in
   `/api4/user.go <https://github.com/mattermost/platform/tree/master/api4/user.go>`__
   your test will go in
   `/api4/user\_test.go <https://github.com/mattermost/platform/tree/master/api4/user_test.go>`__

2. Write your test based on the other tests in your file

   -  There are several helper functions in
   `/api4/apitestlib.go <https://github.com/mattermost/platform/tree/master/api4/apitestlib.go>`__
   that you may use

3. Make sure your test covers the following:

   -  All combinations of correct inputs to your endpoint
   -  Etags for your endpoint, if applicable
   -  Incorrect URL or body parameters return a **400 Bad Request** status code
   -  Requests without a token return a **401 Unauthorized** status code (for
   endpoints requiring a session)
   -  Requests with insufficent permissions return a **403 Forbidden** status
   code (for endpoints requiring a permission)
   -  Requests to non-existent resources or URLs return a **404 Not Found**
   status code

Returning the correct error code might require investigation in the
`app <https://github.com/mattermost/platform/tree/master/app>`__ or
`store <https://github.com/mattermost/platform/tree/master/store>`__
packages to find the source of errors. Status codes on errors should be
set at the creation of the error. 

When completing this step, please make sure to
use the new ``model.NewAppError()`` function (`see example <https://github.com/mattermost/platform/tree/master/store/sql_user_store.go#L112>`__).

Submitting your Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You've done it! You've implemented an APIv4 endpoint and we really
appreciate your help. You can now submit a pull request against the
`mattermost/platform <https://github.com/mattermost/platform>`__
repository by `following the instructions
here <https://docs.mattermost.com/developer/contribution-guide.html#preparing-a-pull-request>`__.
