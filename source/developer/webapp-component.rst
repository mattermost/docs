Building a Webapp React Component
==========================

This page describes how to build a new React component in the webapp. All new components must meet the following requirements:

1. Be pure, meaning that all information required to render are passed in by props
2. Have no direct store interaction, use an index.js to wrap the component if needed
3. Have component tests
4. Be generic and re-usable when possible

These requirements will be talked about in more detail in the following sections.

None of that make any sense to you, or new to React and Redux? Then check out these links:

- https://facebook.github.io/react/tutorial/tutorial.html
- http://redux.js.org/

The components for the webapp currently live in the ``webapp/components/`` directory in the `platform repository <https://github.com/mattermost/platform>`__.

Designing your Component
------------------

The most important part of designing your component is decidiing on what the props will be. Props are very much the API for your component, think of them as a contract between your component and the users of it.

Props are read-only variables that get passed down to your component either directly from a parent component or from an `index.js` container that pulls some data from the Redux store. More on that later, for now you can see all the different prop types here: https://facebook.github.io/react/docs/typechecking-with-proptypes.html#proptypes.

Alright, so how do you decide what props your component should have? Think about your component is trying to display to the user. Any data you need to accomplish that should be part of the props.

As an example, let's imagine we're building an ItemList component with the purpose of displaying a list of items. The props for such a component might look like:

.. code-block:: javascript
  :linenos:

  static propTypes = {
      title: PropTypes.string,
      items: PropTypes.arrayOf(PropTypes.object).isRequired
  }

The ``title`` prop would control the string to display for the title, while ``items`` would be an array of the item objects we would like to display. Note that ``items`` has ``.isRequired`` appended while ``title`` does not. This means that to render our component must have the ``items`` prop set, while it can still render if we don't set ``title``. Use this to provide optional props.

Our ItemList component would live in a file named ``item_list.js``.

Using a Container
------------------

The next question to ask yourself is if you're going to need a container for your component. This is the ``index.js`` file mentioned above. If your component needs either of the following then you'll need a container:

1. Needs some data injected into it's props that the parent component doesn't have access to
2. Needs to be able to perform some sort of action that affects the state of the store

Continuing the ItemList example above, maybe our parent component doesn't care about our list of items and doesn't have access to them. Let's also imagine that we want to let the user remove items from the list by clicking on them. This means our component now needs a container for both criteria above and our props will change slightly:

.. code-block:: javascript
  :linenos:

  static propTypes = {
      title: PropTypes.string,
      items: PropTypes.arrayOf(PropTypes.object).isRequired,
      actions: PropTypes.shape({
          removeItem: React.PropTypes.func.isRequired
      }).isRequired
  }

The container will then need to import selectors and actions from Redux and the connect them to the component and the store.

.. code-block:: javascript
  :linenos:

  import {connect} from 'react-redux';
  import {bindActionCreators} from 'redux';
  import {removeItem} from 'mattermost-redux/actions/items';
  import {getItems} from 'mattermost-redux/selectors/entities/items';

  import ItemList from './item_list.js';

  function mapStateToProps(state, ownProps) {
      return {
          ...ownProps,
          items: getItems(state)
      };
  }

  function mapDispatchToProps(dispatch) {
      return {
          actions: bindActionCreators({
              removeItem
          }, dispatch)
      };
  }

  export default connect(mapStateToProps, mapDispatchToProps)(ItemList);

If the selectors and/or actions you need don't yet exist in Redux then you should go add those first by following the `guide to adding actions and selectors <./redux>`.

Your ``index.js`` and ``item_list.js`` files will live together in an ``item_list/`` directory.

Implementing your Component
------------------

With the props defined and, if necessary, the container built, you're ready to implement your component. For the most part implementing a component for the webapp is no different than building any other React component. That said, we do have a few rules to abide by:

1. All components must extend ``React.PureComponent``
2. All data for rendering must come from props
3. Local rendering information that does not affect the store may be kept in state

Our ItemList example might look something like this:

.. code-block:: javascript
  :linenos:

  export default class ItemList extends React.PureComponent {
      static propTypes = {
          title: PropTypes.string,
          items: PropTypes.arrayOf(PropTypes.object).isRequired,
          actions: PropTypes.shape({
              removeItem: React.PropTypes.func.isRequired
          }).isRequired
      }

      render() {
          const items = [];

          this.props.items.forEach((item) => {
              items.push(
                  <Item
                      item={item}
                      onClick={this.props.actions.removeItem}
                  />
              );
          });

          return (
              <div className='backstage-header'>
                  <h1>
                      {this.props.title}
                  </h1>
                  {items}
              </div>
          );
      }
  }

Testing your Component
------------------

The last required piece of building a webapp component is to test it. That can be done using the component testing framework described in this blog post:

https://grundleborg.github.io/posts/react-component-testing-in-mattermost/
