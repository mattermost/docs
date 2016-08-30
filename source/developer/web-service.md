# Web Service API 

_API Version v3.0_

Mattermost offers a RESTful Web Service API for interacting with the server, along with JavaScript and Golang drivers to integrate into your applications and bots. 

The document includes: 

- Web Service API Schema 
- Authentication Examples
- Client Errors 
- Rate Limiting 
- API Reference 
- Bot Example

All examples assume there is a Mattermost instance running at http://localhost:8065.

## Web Service API Schema

All API access is done through `yourdomain.com/api/v3/`, with all data being sent and received as JSON.

## Authentication Examples 

The majority of the Mattermost API involves interacting with teams. Therefore, most API methods require authentication as a user. There are two ways to authenticate into a Mattermost system.

### Session Token

Make an HTTP POST to `yourdomain.com/api/v3/users/login` with a JSON body indicating the `name` of the team, the user's `login_id` and `password`.

```
curl -i -d '{"name":"exampleteam","login_id":"someone@nowhere.com","password":"thisisabadpassword"}' http://localhost:8065/api/v3/users/login
```

If successful, the response will contain a `Token` header and a User object in the body.

```
HTTP/1.1 200 OK
Set-Cookie: MMSID=hyr5dmb1mbb49c44qmx4whniso; Path=/; Max-Age=2592000; HttpOnly
Token: hyr5dmb1mbb49c44qmx4whniso
X-Ratelimit-Limit: 10
X-Ratelimit-Remaining: 9
X-Ratelimit-Reset: 1
X-Request-Id: smda55ckcfy89b6tia58shk5fh
X-Version-Id: developer
Date: Fri, 11 Sep 2015 13:21:14 GMT
Content-Length: 657
Content-Type: application/json; charset=utf-8

{{user object as json}}
```

Include the `Token` as part of the `Authentication` header on your future API requests with the `Bearer` method.

```
curl -i -H 'Authorization: Bearer hyr5dmb1mbb49c44qmx4whniso' http://localhost:8065/api/v3/users/me
```

You should now be able to access the API as the user you logged in as.

### OAuth2 Provider

Mattermost offers an OAuth2 provider to allow secure authentication for bot accounts. 

An example of how to setup an OAuth2 provider integration can be found in the [Mattermost-Zapier integration documentation.](https://docs.mattermost.com/integrations/zapier.html#register-zapier-as-an-oauth-2-0-application). 

Additional documentation on using the OAuth2 provider will be added here in future. 

## Client Errors

All errors will return an appropriate HTTP response code along with the following JSON body:

```
{
    "message": "", // the reason for the error
    "detailed_error": "", // some extra details about the error
    "request_id": "", // the ID of the request
    "status_code": 0 // the HTTP status code
}
```

## Rate Limiting

Whenever you make an HTTP request to the Mattermost API you might notice the following headers included in the response:
```
X-Ratelimit-Limit: 10
X-Ratelimit-Remaining: 9
X-Ratelimit-Reset: 1441983590

```

These headers are telling you your current rate limit status.

|Header                | Description|
|:--------------------- |:-----------
|X-Ratelimit-Limit     | The maximum number of requests you can make per second.|
|X-Ratelimit-Remaining | The number of requests remaining in the current window.|
|X-Ratelimit-Reset     | The remaining UTC epoch seconds before the rate limit resets.|

If you exceed your rate limit for a window you will receive the following error in the body of the response:
```
HTTP/1.1 429 Too Many Requests
Date: Tue, 10 Sep 2015 11:20:28 GMT
X-RateLimit-Limit: 10
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1

limit exceeded
```

## Web Service API Reference 

The easiest way to interact with the Mattermost Web Service API is through a language specific driver, such as: 

- Mattermost JavaScript Driver
- Mattermost Golang Driver 

The API implementation contained in these drivers demonstrates their schema and use. 

### API documentation using GoDoc and Golang Driver 

GoDoc automatically generates documentation for the Golang driver, which links to Golang code demonstrating the specific use of the Web Service API calls. 

You can view GoDocs for the Golang driver at: https://godoc.org/github.com/mattermost/platform/model

For example:

1. If you want to add a user to a team, you can reference the [AddUserToTeam function](https://godoc.org/github.com/mattermost/platform/model#Client.AddUserToTeam) in the Golang driver documentation to understand the available method 
2. You can click on the name of the function to view how the Web Service API is used, which leads you to https://github.com/mattermost/platform/blob/master/model/client.go#L368, showing the following: 

```
//  Adds a user directly to the team without sending an invite.
//  The teamId and userId are required.  You must be a valid member of the team and/or
//  have the correct role to add new users to the team.  Returns a map of user_id=userId
//  if successful, otherwise returns an AppError.
func (c *Client) AddUserToTeam(teamId string, userId string) (*Result, *AppError) {
	if len(teamId) == 0 {
		teamId = c.GetTeamId()
	}

	data := make(map[string]string)
	data["user_id"] = userId
	if r, err := c.DoApiPost(fmt.Sprintf("/teams/%v", teamId)+"/add_user_to_team", MapToJson(data)); err != nil {
		return nil, err
	} else {
		defer closeBody(r)
		return &Result{r.Header.Get(HEADER_REQUEST_ID),
			r.Header.Get(HEADER_ETAG_SERVER), MapFromJson(r.Body)}, nil
	}
}
```

Code examples like this are used to demonstrate the schema and functionality of the underlying Web Service API. 

### API documentation via JavaScript driver 

If you're developing in JavaScript-style languages, you can reference the Web Service API using the implementation shown in the JavaScript driver. 

For example, to add a user to a team using the Web Service API you can reference the JavaScript driver implementation at: 
https://github.com/mattermost/mattermost-driver-javascript/blob/master/client.jsx#L552

```
    addUserToTeam(teamId, userId, success, error) {
        let nonEmptyTeamId = teamId;
        if (nonEmptyTeamId === '') {
            nonEmptyTeamId = this.getTeamId();
        }

        request.
            post(`${this.getTeamsRoute()}/${nonEmptyTeamId}/add_user_to_team`).
            set(this.defaultHeaders).
            type('application/json').
            accept('application/json').
            send({user_id: userId}).
            end(this.handleResponse.bind(this, 'addUserToTeam', success, error));

        this.track('api', 'api_teams_invite_members');
    }
```

Code examples like this are used to demonstrate the schema and functionality of the underlying Web Service API. 

