.. _ediscovery:

Electronic discovery
=====================

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

Electronic discovery (also known as eDiscovery) refers to a process where electronic data is searched with the intent to use it as evidence in a legal case.

This page describes how to extract data from Mattermost for eDiscovery. There are three primary methods that can be used to accomplish the goal of extracting user post data from Mattermost:

- `Mattermost Compliance Exports </comply/compliance-export.html>`__
- `Mattermost RESTful API </comply/electronic-discovery.html#mattermost-restful-api>`__
- `Mattermost database using standard SQL queries </comply/electronic-discovery.html#mattermost-database>`__

Each of the options is discussed in detail below.

.. note::
  Litigation hold (also known as legal hold) is an extension of eDiscovery where in addition to searching for records, no electronically stored information nor paper documents may be discarded if they may be deemed relevant for a present or future legal case.

Mattermost compliance exports
-----------------------------

Mattermost Enterprise has compliance report export capabilities.

Mattermost can export compliance related data, including the content of messages and who might have seen those messages, in three formats: Actiance XML, Global Relay EML, and generic CSV. Reports can be configured to run on a delay basis and stored in a shared location.

For more information about the exports feature and how to set up reporting, see `our documentation </comply/compliance-export.html>`__.

Mattermost RESTful API
----------------------

The Mattermost API can be used to export a user's posts in CSV compliance format that is part of Mattermost Enterprise. The following section outlines how to use the API to create and retrieve a report for a specific user via the API. Please note that full documentation for the Mattermost API can be found at https://api.mattermost.com.

To use the API, you must first authenticate `as described here <https://api.mattermost.com/#tag/authentication>`__. The account you are authenticating with must have ``manage_system`` permissions. If you are using curl, you can authenticate using the following command:

.. code-block:: text

  curl -i -d '{"login_id": "username", "password": "password"}' https://yourmattermosturl/api/v4/users/login

Mattermost will return a response that looks like this:

.. code-block:: text

  HTTP/2 200
  server: nginx/1.10.3 (Ubuntu)
  date: Thu, 12 Jul 2018 14:43:45 GMT
  content-type: application/json
  content-length: 679
  set-cookie: MMAUTHTOKEN=yi94pwci6ibjfc9phbikhqutbe; Path=/; Expires=Sat, 11 Aug 2018 14:43:45 GMT; Max-Age=2592000; HttpOnly; Secure
  set-cookie: MMUSERID=qfjzamfg47bu9gsyyfbqjk4s6a; Path=/; Expires=Sat, 11 Aug 2018 14:43:45 GMT; Max-Age=2592000; Secure
  token: yi94pwci6ibjfc9phbikhqutbe
  x-request-id: 5y45pxyfxpb8updtge1zts39he
  x-version-id: 5.0.0.5.0.1.18c0fbd759664a85fe95132bb7fc04cf.true

Include the ``token`` value sent in the response as part of the Authorization header on your future API requests with the Bearer method, e.g.:

.. code-block:: text

  curl -i -H 'Authorization: Bearer yi94pwci6ibjfc9phbikhqutbe http://yourmattermosturl/api/v4/users/me

Once you're authenticated into Mattermost, you can use the `Compliance API to create a new compliance report <https://api.mattermost.com/#tag/compliance%2Fpaths%2F~1compliance~1reports%2Fpost>`__. The curl based example below demonstrates how to send a request that bases the authentication token and asks Mattermost to create a report that spans posts from Dec 31, 2017 - 8:15 PM to Dec 31, 2018 - 8:15 PM for a user with the email address craig@mattermost.com:

.. note::

  The data in the JSON payload must be formatted as Unix Epoch. A tool like https://www.epochconverter.com/ can be useful when converting to and from the required format.

.. code-block:: text

  curl --header "Content-Type: application/json" \
  --request POST \
  -H 'Authorization: Bearer yi94pwci6ibjfc9phbikhqutbe \
  --data '{"id":"","create_at":0,"user_id":"craig","status":"","count":0,"desc":" ","type":"","start_at":1514769359000,"end_at": 1546305359000,"keywords":"","emails":"craig@mattermost.com"}' \
  https://yourmattermosturl/api/v4/compliance/reports

If the post is successful, Mattermost will return a message that looks like the following, indicating that the server is running the compliance export process:

.. code-block:: json

  {"id":"du6kektczifqxexeroywpz3nbc"," create_at":1531444617901, "user_id":"qfjzamfg47bu9gsyyfbqjk4s6a", "status":"running", "count":0, "desc":" ", "type":"adhoc", "start_at":1514769359000, "end_at":1546305359000, "keywords":"", "emails":"craig@mattermost.com"}

When the export process is complete (the execution time is based on the number of records to return and the current server load), you will need to send another HTTP Post request to Mattermost to retrieve and download a zip file containing the report that looks like the following curl request:

.. code-block:: text

  curl --request GET \
  -H 'Authorization: Bearer p9o1qx457fbc9gdrn39z9ah59o' \
  --data '{"status_code":0,"id":"du6kektczifqxexeroywpz3nbc","message":"","requestion_id":""}' \
  --output report-zip.zip \
  https://yourmattermosturl/api/v4/compliance/reports/du6kektczifqxexeroywpz3nbc/download

When sending the request, you need to get the report ID from the response returned by Mattermost when the report was created. You also need to supply a name to save that file as. In the example above, the file will be saved as ``report-zip.zip``.

Mattermost database
-------------------

Selecting messages from the Mattermost database using standard SQL is quite easy. If you know the username, the following query can be used to select all messages for the specified user:

.. code-block:: sql

  SELECT * FROM mattermost.Posts WHERE UserId = (SELECT Id FROM mattermost.Users WHERE Username = 'username');

If you want to limit the results of the query based on the date and time that the messages were posted, you can modify the above query to:

.. code-block:: sql

  SELECT * FROM mattermost.Posts WHERE UserId = (SELECT Id FROM mattermost.Users WHERE Username = 'username' AND CreateAt > 1530405832000 AND CreateAt < 1532997832000);

.. note::
  The Mattermost database stores date and time stamps in the `Unix Epoch <https://en.wikipedia.org/wiki/Unix_time>`__ format. A tool like the `Epoch Converter <https://www.epochconverter.com/>`__ can be useful in converting to and from the required format.
