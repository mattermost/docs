##########################
Web Service API Reference 
##########################

Documentation for the Web Service API is under development. 

Final documentation will cover the following sections: 

- User
- Team
- Channel
- Posts
- Admin
- General
- Emoji
- Preferences
- Files
- OAuth
- Public

User API Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-------------------------+-------------+-------------------------------------------------+------------------------------------------------------------------------------------------------------+---------------------+
| Route                   | HTTP Method | Description                                     | Request Body                                                                                         | Response            |
+=========================+=============+=================================================+======================================================================================================+=====================+
| /users/create           | POST        | Create a user.                                  | User object                                                                                          | Created user object |
+-------------------------+-------------+-------------------------------------------------+------------------------------------------------------------------------------------------------------+---------------------+
| /users/update           | POST        | Update a user.                                  |  User object                                                                                         | Updated user object |
+-------------------------+-------------+-------------------------------------------------+------------------------------------------------------------------------------------------------------+---------------------+
| /users/update_roles     | POST        | Updates a user's permission roles               | Map with the keys `user_id` and `new_roles`                                                          | Map with `user_id`  |
+-------------------------+-------------+-------------------------------------------------+------------------------------------------------------------------------------------------------------+---------------------+
| /users/update_active    | POST        | Sets whether a user's account is active or not. | Map with the keys `user_id` and `active`                                                             | Updated user object |
+-------------------------+-------------+-------------------------------------------------+------------------------------------------------------------------------------------------------------+---------------------+
| /users/update_notify    | POST        | Updates the user's notification properties.     | Map with the keys `user_id`, `email`, `desktop_sound`, `comments` and other notification properties. | Updated user object |
+-------------------------+-------------+-------------------------------------------------+------------------------------------------------------------------------------------------------------+---------------------+
| /users/me               | GET         | Get the current logged in user.                 | N/A                                                                                                  | User object         |
+-------------------------+-------------+-------------------------------------------------+------------------------------------------------------------------------------------------------------+---------------------+

Team API Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under development.

Channel API Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under development.

Posts API Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under development.

Admin API Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under development.

General API Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under development.

Emoji API Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under development.

Preferences API Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under development.

Files API Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under development.

OAuth API Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under development.

Public API Reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Under development.

