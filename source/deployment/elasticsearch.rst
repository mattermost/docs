Elasticsearch Beta (E20)
========================

*Available in Enterprise Edition E20.*

_`Elasticsearch <https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html>`_ is a distributed, RESTful search engine capable of supporting search in large scale enterprise deployments with millions of messages. 

.. toctree::
    :maxdepth: 2

Deployment Guide
----------------

Overview
~~~~~~~~

Elasticsearch allows you to search large volumes of data quickly, and in near real time, by creating and managing an index of post data. The indexing process can be managed from the System Console after setting up and connecting an Elasticsearch server. The post index is stored on the Elasticsearch server and is updated constantly after new posts are made. In order to index existing posts, a bulk index of the enitre post database must be generated. 

Setting up an Elasticsearch Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The setup process for the Elasticsearch server is documented in the _`official Elasticsearch documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html>`_. 


Hardware Requirements
`````````````````````
Elasticsearch should run alone on a server and use all of the resources available to it.

XXXXXX George: hardware requirements for the elasticsearch server?

Configuring Elasticsearch in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

XXXXXX Eric: Setup steps in the system console for creating the first index and turning on elasticsearch

If Elasticsearch is enabled before the bulk indexing of posts is complete

Limitations
-----------


XXXXXX Eric: supports all current search features with limitations (list important known Elasticsearch issues) 

XXXXXX George: Can you please link to the list of stop words we are using. Anything else important you'd like to note here?


Frequently Asked Questions (FAQ)
--------------------------------

Why do I need to use Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Due to the limitations of scaling with database search, Enterprise deployments with more than 5,000,000 messages will require Elasticsearch

What search features are offered with Elasticsearch?
The Beta implementation of Elasticsearch matches the search features currently available with database search. The Mattermost team plans to add 


XXXXXX George: Anything you'd like to note here (common mistakes people might make during the deployment process?)



