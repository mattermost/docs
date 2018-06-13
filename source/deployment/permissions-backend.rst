Advanced Permissions: Backend Infrastructure
=============================================

This document outlines the backend server infrastructure for permissions in Mattermost and is recommdended only for technical Admins or developers looking to make modifications to their installation.


.. note::

  The contents of this document apply to Mattermost Server version 5.0 and later. 


.. contents::
  :backlinks: top
  :local:
  
Entity Definitions
--------------------

Permissions
~~~~~~~~~~~~


List of perms
ID, name, description, scope | frontend permission map or if granted by default

Default permission assignment to roles can be found in: link f

Roles
~~~~~~

Scope
~~~~~~

Context
~~~~~~~~

Schemes
~~~~~~~~~


Data Structure
----------------

Applicable database fields and tables.

Permissions
~~~~~~~~~~~~~~

perms have scope (sys, team, chan)

``User`` ``TeamMember`` ``Channel Member`` Tables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Roles`` Table
~~~~~~~~~~~~~~~~

``Schemes`` Table
~~~~~~~~~~~~~~~~



  
