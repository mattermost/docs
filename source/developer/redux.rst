Working with Redux
==========================

This page describes how to add actions and selectors to the client service and storage layer built on Redux. This Redux service layer is what drives the majority of actions, storage and server interaction for both the Mattermost webapp and the React Native mobile apps.

As of Mattermost version 3.9, the webapp has begun moving to replace Flux with Redux. If you're interested in contributing to this campaign, please see `migrating webapp components to Redux <./migrating-to-redux>`__ and join the `Redux channel on pre-release.mattermost.com <https://pre-release.mattermost.com/core/channels/redux>`__.

The respository for the Redux service layer is here: https://github.com/mattermost/mattermost-redux

New to Redux? Then check out these links:

- http://redux.js.org/
- https://www.youtube.com/playlist?list=PLoYCgNOIyGADILc3iUJzygCqC8Tt3bRXt
- https://github.com/gaearon/redux-thunk

Adding an Action
------------------

Actions are any sort of logic that will result in the manipulation of store state. The means by which actions manipulate the store is through dispatches. Dispatches will take an object with an action type and some data, and pass it along to the reducers to be transformed into the correct format and placed in the state of the store. An example action might be getting a user, which would use the web client utility to fetch the user and then dispatch that user to the store.

Actions must:
- Return `asynch functions <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function>`__ so the caller can `await <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await>`__ on them
- The async function must return ``null`` on error, while dispatching an error to store state
- The async function must return the data result or return ``true`` if there is no data to return, while dispatching the data
- Be unit tested

Actions live in the ``src/actions/`` directory.

Add Action Types
~~~~~~~~~~~~~~~~~~

Action types are the constants the reducers use to know what type of data they are receiving and what to do with it. Generally, there are two kinds of action types you'll need to worry about: data and requests.

Data action types are what you'll use to dispatch the result of your action to the reducers. If your action is manipulating or fetching data in a format already handled by the store, then there might be no need to add a new action type. An example data action type is ``RECEIVED_USER``.

Request action types are used to track the state of server requests. Non-optimisitic actions that use the web client utility to interact with the server need three request action types, one for the start of the request, one for success and one for failure. If the request you're using already has action types, then no need to add any. Examples of request action types are ``USER_REQUEST``, ``USER_SUCCESS`` and ``USER_FAILURE``.

Note that if you're planning on writing an optimistic action, you do not need to specify request action types.

Add your action types to the appropriate file in ``src/action_types/``. When adding request action types you'll also need to add the reducer in ``src/reducers/requests/``. Just follow the examples in those files, it's fairly straight forward.

Add a Web Service Function
~~~~~~~~~~~~~~~~~~

If your action is going to use a new REST API endpoint on the server, you'll need to add a function to the web client utility.

The web client lives at ``src/client/client4.js``. `Fetch <https://developer.mozilla.org/en/docs/Web/API/Fetch_API>`__ is the library used to interact with the Mattermost REST API.

Adding a function should also be fairly straight-forward, just use the existing functions as an example.

Implementing the Action
~~~~~~~~~~~~~~~~~~

The actual implementation of the action will vary depending on what you're trying to accomplish. Actions live in the ``src/actions/`` directory. Make sure to add your action to the appropriate file.

If your action is a one-to-one mapping of a web client function, all you need to do is use the ``bindClientFunc`` function to do the mapping.

.. code-block:: javascript
  :linenos:

  export function getUser(userId) {
      return bindClientFunc(
          Client4.getUser,
          UserTypes.USER_REQUEST,
          [UserTypes.RECEIVED_USER, UserTypes.USER_SUCCESS],
          UserTypes.USER_FAILURE,
          userId
      );
  }

The above action just gets a user and is a one-to-one mapping to the ``getUser`` web client function.

If it's not a one-to-one mapping and you need to manipulate the data you get back from the web client, then you'll need to do a bit more manual work.

.. code-block:: javascript
  :linenos:

  export function getProfiles(page = 0, perPage = General.PROFILE_CHUNK_SIZE) {
      return async (dispatch, getState) => {
          dispatch({type: UserTypes.PROFILES_REQUEST}, getState);

          const {currentUserId} = getState().entities.users;

          let profiles;
          try {
              profiles = await Client4.getProfiles(page, perPage);
              removeUserFromList(currentUserId, profiles);
          } catch (error) {
              forceLogoutIfNecessary(error, dispatch);
              dispatch(batchActions([
                  {type: UserTypes.PROFILES_FAILURE, error},
                  getLogErrorAction(error)
              ]), getState);
              return null;
          }

          dispatch(batchActions([
              {
                  type: UserTypes.RECEIVED_PROFILES_LIST,
                  data: profiles
              },
              {
                  type: UserTypes.PROFILES_SUCCESS
              }
          ]));

          return profiles;
      };
  }

In the above action, we need to remove the current user from profile list so that we don't overwrite it in the state. Because of the need to do that, we could not use ``bindClientFunc``.

It is also possible to write optimistic actions that dispatch data to the store immediately before waiting for a response from the server. These are a little more advanced and should only be used in situations that warrant them. The framework that drives this is `redux-offline <https://github.com/jevakallio/redux-offline>`__.

.. code-block:: javascript
  :linenos:

  export function deletePost(post) {
      return async (dispatch) => {
          const delPost = {...post};

          dispatch({
              type: PostTypes.POST_DELETED,
              data: delPost,
              meta: {
                  offline: {
                      effect: () => Client4.deletePost(post.id),
                      commit: {type: PostTypes.POST_DELETED},
                      rollback: {
                          type: PostTypes.RECEIVED_POST,
                          data: delPost
                      }
                  }
              }
          });
      };
  }

There can also be actions that just wrap one or more existing actions.

.. code-block:: javascript
  :linenos:

  export function flagPost(postId) {
      return async (dispatch, getState) => {
          const {currentUserId} = getState().entities.users;
          const preference = {
              user_id: currentUserId,
              category: Preferences.CATEGORY_FLAGGED_POST,
              name: postId,
              value: 'true'
          };

          savePreferences(currentUserId, [preference])(dispatch, getState);
      };
  }

Make sure to also add your function to the default export at the bottom of the file.

Testing the Action
~~~~~~~~~~~~~~~~~~

The final piece is testing your action. We use the `mochajs framework <https://mochajs.org/>`__ for testing, along with the `nock server mocking framework <https://github.com/node-nock/nock>`__ to mock the server where needed.

The tests for actions live in ``test/actions/``. Add your test to the appropriate file following one of the many examples for the other actions.

Make sure to read the `README <https://github.com/mattermost/mattermost-redux/blob/master/README.md>`__ for information on running the tests.


Adding a Selector
------------------

Selectors are the method used to retrieving data from the state of the store. We use `reselect <https://github.com/reactjs/reselect>`__. If you'd like to know more about reselect and how we use it at Mattermost, `check out this developer talk given by core developer Harrison Healey <https://www.youtube.com/watch?v=6N2X7gEwmaQ>`__.

Selectors must:
- Receive ``state`` as the first argument and data returned must be solely based on what's in the state
- Be created with ``createSelector`` whenever the data is manipulated or formatted before return
- Be unit tested

Selectors live in the ``src/selectors/`` directory.

Implementing the Selector
~~~~~~~~~~~~~~~~~~

If your selector is just pulling data directly from the state without any manipulation, simply just return the data you need.


.. code-block:: javascript
  :linenos:

  export function getUser(state, id) {
      return state.entities.users.profiles[id];
  }

The above example is just simply pulling a user out of the profiles entity and requires no computation or formatting.

If your selector needs to select based on some more advanced requirements or needs the result in a specific format then you'll need to make use of the ``createSelector`` function from `reselect <reselect <https://github.com/reactjs/reselect>`__. If you're not sure what this is good for, `check out the previously mentioned developer talk <https://www.youtube.com/watch?v=6N2X7gEwmaQ>`__. The short form reason is using reselect allows for memoization and only runs the computation of selectors when the state affecting that selector has actually changed.

The basic usage for ``createSelector`` is pass it all the selector functions needed as inputs to your computation. The last argument will then be a function that takes in the results of each selector you specified and performs your computation on that data before returning it.

.. code-block:: javascript
  :linenos:

  export const getUsersByUsername = createSelector(
      getUsers,
      (users) => {
          const usersByUsername = {};

          for (const id in users) {
              if (users.hasOwnProperty(id)) {
                  const user = users[id];
                  usersByUsername[user.username] = user;
              }
          }

          return usersByUsername;
      }
  );

Here we're using the ``getUsers`` selector to feed users into our function that builds a map of users with username as the key.

So far that's pretty straight forward but what if you want to select some data based on an argument but also need to do some computation? That is a little more tricky if you haven't wrapped your head around the purpose of reselect and how createSelector works, so if you haven't watched the developer talk linked above I would strongly suggest it.

To accomplish this we need to create factory function that will create the selector, instead of just creating the selector directly.

.. code-block:: javascript
  :linenos:

  function getAllFiles(state) {
      return state.entities.files.files;
  }

  function getFilesIdsByPosts(state, post) {
      return state.entities.files.fileIdsByPostId;
  }

  export function makeGetFilesForPost() {
      return createSelector(
          getAllFiles,
          getFilesIdsForPost,
          (state, postId) => postId,
          (allFiles, fileIdsForPost, postId) => {
              return fileIdsForPost.map((id) => allFiles[id]);
          }
      );
  }

  // Usage by a third party application
  const getFilesForPost = makeGetFilesForPost();
  const files = getFilesForPost(state, 'somepostid');

This can look a bit confusing but there is little happening here we haven't seen before. All that we're doing is using three selectors with ``createSelector``, the third selector just happens to be returning an argument so that our final function has access to it. Remember that every selector always takes state in as the first argument.

If you're thinking, I don't get it why can't we just create the selector normally? Then think about how selectors work and remember that if the state changes then the computation happens again. In this case if our ``postId`` changes that counts as a state change since one of our selectors is returning it. This means every time we provide a different ``postId`` to our selector we lose all the benefits of memoization, which is the whole reason for using reselect. So instead we create a new selector for every post id that we want to select for. That may seem a little crazy at first, but think about how componentized React is and it's not that crazy. All you really need to do is use the factory function to create your selector in the constructor or container of your component and use it solely for that component.

Testing the Selector
~~~~~~~~~~~~~~~~~~

To test your selector you'll want to add a test to the appropriate file in the ``tests/selectos`` directory.

Testing selectors invovles building some test state and confirming that the data returned from your selector matches what you would expect it to return. Use other tests as examples and make sure to read the `README <https://github.com/mattermost/mattermost-redux/blob/master/README.md>`__ for information on running the tests.
