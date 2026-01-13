========================================
Release Notes Snippets Documentation
========================================

This directory contains reusable snippets for release notes that can be included in both individual release pages and master rollup pages using Sphinx's ``.. include::`` directive.

Strategy Overview
=================

The "Include" strategy addresses the customer feedback: *"Release notes already list UI items under 'User Interface (UI),' but admins want to easily see the changes rolled up across versions ('What changed in the UI from the version we were on to the one we're upgrading to?'). They also want to more easily track Accessibility (ADA) improvements/fixes release to release."*

How It Works
============

1. **Single Source of Truth**: UI changes and ADA improvements for each version are written once in snippet files.
2. **Multiple Display Locations**: The same content appears in:
   - Individual release notes (e.g., ``mattermost-v11-changelog.md``)
   - Master rollup pages (``ui-changes-history.rst`` and ``ada-improvements-history.rst``)
3. **Automatic Updates**: When snippet content is updated, it automatically reflects in all places where it's included.

Directory Structure
===================

::

   snippets/
   ├── README.rst                    # This documentation file
   ├── .gitkeep                      # Ensures directory is tracked by Git
   ├── v11-1-ui-changes.rst         # UI changes for v11.1
   ├── v11-1-ada-improvements.rst    # ADA improvements for v11.1
   ├── v11-2-ui-changes.rst         # UI changes for v11.2
   └── v11-2-ada-improvements.rst    # ADA improvements for v11.2

Usage Examples
==============

In Release Notes (Markdown)
----------------------------

.. code-block:: markdown

   ```{eval-rst}
   .. include:: /snippets/v11-2-ui-changes.rst
   ```

In Master Rollup Pages (reStructuredText)
------------------------------------------

.. code-block:: rst

   .. include:: /snippets/v11-2-ui-changes.rst

Master Rollup Pages
====================

Two master pages have been created to provide consolidated views:

- ``/product-overview/ui-changes-history.rst`` - Consolidated UI changes across versions
- ``/product-overview/ada-improvements-history.rst`` - Consolidated ADA improvements across versions

These pages are included in the product overview navigation and provide admins with the rolled-up view they requested.

Adding New Versions
====================

For each new version, create:

1. ``snippets/vX-Y-ui-changes.rst`` - UI changes for version X.Y
2. ``snippets/vX-Y-ada-improvements.rst`` - ADA improvements for version X.Y
3. Update the individual release notes to use ``.. include:: /snippets/vX-Y-ui-changes.rst``
4. Add the new includes to the master rollup pages

This ensures consistent formatting and easy maintenance across all documentation.