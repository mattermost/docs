UI and Accessibility Changes Rollup Strategy
============================================

This directory contains reusable content snippets for UI and accessibility improvements that are included in both individual release notes and master rollup pages.

The Include Strategy
-------------------

Each version's UI and accessibility changes are stored as separate snippet files:

* ``v11-1-ui-accessibility-changes.rst`` - Combined UI and accessibility changes for v11.1
* ``v11-2-ui-accessibility-changes.rst`` - Combined UI and accessibility changes for v11.2
* etc.

Usage
-----

**In Release Notes:**
Use ``.. include:: /snippets/v11-2-ui-accessibility-changes.rst`` to include version-specific changes.

**In Master Rollup Page:**
Include all version snippets to show consolidated view of changes across versions.

Benefits
--------

* Single source of truth for UI and accessibility content
* Automatic synchronization across release notes and rollup pages  
* Easy maintenance when updating content
* Consolidated view for admins upgrading across versions