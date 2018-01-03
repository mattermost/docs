Migrating the Webapp to Redux
=============================

The Mattermost webapp is going through a big restructuring effort to move from using Flux and Redux. When we first started building the webapp, React was still new to the world, and so were the frameworks and design patterns. As a result, the webapp has had a lot of organic growth over the last couple of years, and is using an assortment of different design patterns. 

This campaign is meant to help with that by moving app state and logic into our `Redux repository <https://github.com/mattermost/mattermost-redux>`__, and by migrating the webapp components to be pure and use Redux to supply their props.

By completing this campaign, we're looking to:

- Reduce complexity of the webapp and consolidate into a single design pattern.
- Increase webapp performance through pure components and selector memoization.
- Share state related logic with other Mattermost clients such as the mobile apps.

Contributing
------------------

If you're interested in contributing please join the `Redux channel on pre-release.mattermost.com <https://pre-release.mattermost.com/core/channels/redux>`__. Progress on moving individual components over to use Redux is `tracked on this spreadsheet <https://docs.google.com/spreadsheets/d/1AlFS2F4H74JsONxIS_VNZBxrVJolZxFh7yN46RNCwyg/edit#gid=0>`__. If you want to work on one of the components let us know in the Redux channel or by making a comment on the spreadsheet.

List of contributors, in alphabetical order:

 - Adrian Carolli (`@adriancarolli <https://github.com/watadarkstar>`_)
 - Aibulatov Alex (`@Zapix <https://github.com/Zapix>`_)
 - Andre Vasconcelos (`@avasconcelos114 <https://github.com/avasconcelos114>`_)
 - Carlos Panato (`@cpanato <https://github.com/cpanato>`_)
 - Devesh Jadon (`@deveshjadon98 <https://github.com/deveshjadon98>`_)
 - Eric Webster (`@ericwebster <https://github.com/QuantumKing>`_)
 - Hyeseong Kim (`@CometKim <https://github.com/CometKim>`_)
 - Jesús Espino (`@jespino <https://github.com/jespino>`_)
 - Joram Wilander (`@jwilander <https://github.com/jwilander>`_)
 - K.Y. (`@tkbky <https://github.com/tkbky>`_)
 - Nazar Laba (`@n1aba <https://github.com/n1aba>`_)
 - (`@panditsavitags <https://github.com/panditsavitags>`_)
 - Ryan Wang (`@R-Wang97 <https://github.com/R-Wang97>`_)
 - Sam Kvale (`@skvale <https://github.com/skvale>`_)
 - Shengying Pan (`@h2oloopan <https://github.com/h2oloopan>`_)
 - Sudheer Timmaraju (`@sudheerDev <https://github.com/sudheerDev>`_)
 - Taehyeon Yun (`@yth0625 <https://github.com/yth0625>`_)

For guidance on migrating a webapp component to Redux, read the next section.

Component Migration Steps
-------------------------

There are a few steps involved with migrating a component to use Redux. Some of them may not apply to every component and they may change slightly based on the component you're working on. In general, you can these steps as a checklist for work that needs to be done on each component.


1. Move any ``PropTypes`` from the bottom of the file to be defined at the top of the component, `as shown here <./webapp-component.html#designing-your-component>`__.
 - Also replace any ``React.PropTypes`` usages with just ``PropTypes`` and add ``import PropTypes fron 'prop-types';`` to the file imports.
 - Please make sure to add documentation for each prop, as shown in the above link.
2. Switch the component to extend ``React.PureComponent`` instead of ``React.Component`` and remove the ``shouldComponentUpdate`` function if it exists.
3. If the component imports any stores (ex. ``user_store.jsx``), create a container by:
 1. Creating props to hold the data pulled from the stores.
 2. `Following this guide <./webapp-component.html#using-a-container>`__ and creating a folder and ``index.js`` for the component.
 3. Using selectors from Redux inside the container to fill the props of the component.
  - The `existing Redux selectors are here <https://github.com/mattermost/mattermost-redux/tree/master/src/selectors/entities>`__. If one does not exist for the data you need, you can `follow these steps to add new selectors <./redux.html#adding-a-selector>`__.
 4. Remove all store imports from the component.
4. If the component imports any actions (ex. ``user_actions.jsx``), then:
 1. Create an ``actions`` prop with each action as a child, `similar to this <./webapp-component.html#using-a-container>`__.
 2. Use actions from Redux to fill the action props of the ``mapDispatchToProps`` function.
  - The `existing Redux actions are here <https://github.com/mattermost/mattermost-redux/tree/master/src/actions>`__. If the action you need does not exist, you can `follow these steps to add a new action <./redux.html#adding-an-action>`__.
 3. Replace each action call to use the actions in the props (ex. ``this.props.actions.someAction()``).
 4. Remove all action imports from the component.
5. Move any other variables holding store state into props fed from Redux or parent components.
6. Add component tests `as described by this blog post <https://grundleborg.github.io/posts/react-component-testing-in-mattermost/>`__ and by following the `example of other tests <https://github.com/mattermost/mattermost-webapp/tree/master/tests/components>`__.

Examples
------------------
You can see some example pull requests here:

- https://github.com/mattermost/mattermost-server/pull/6416
