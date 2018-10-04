Bind Authentication to ID Attribute instead of Email
------------------------------------------

Alternatively, you can use an Id Attribute instead of email to bind the user.  We recommend choosing an ID that is unique and will not change over time.  

Configuring with an Id Attribute allows you to reuse an email address for a new user without the old user's information being exposed. For instance, if a user with an email address joe.smith@mattermost.com was once an employee, a new employee named Joe Smith can use the same email. This configuration is also useful when a user's name changes and their email needs to be updated. 

This process was designed with backwards compatibility to email binding. Here is the process applied to new account creations and to accounts logging in after the configuration:

 - A user authenticated with SAML is bound to the SAML service user using the Id Attribute (as long as it has been configured) or bound by email using the email received from SAML. 
 - When the user tries to login and the SAML server responds with a valid authentication, then the server uses the "Id" field of the SAML authentication to search the user. 
 - If a user bound to that ID already exists, it logs in as that user. 
 - If a user bound to that ID does not exist, it will search base on the email. 
 - If a user bound to the email exists, it logs in with email and updates the autentication data to the ID, instead of the email. 
 - If a user bound to the ID or email does not exist, it will create a new Mattermost account bound to the SAML account by ID and will allow the user to log in. 

 Note:  Existing accounts will not update until they log in to the server. 
 
