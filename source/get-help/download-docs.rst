Download Documentation for Offline Use
=======================================

Mattermost product documentation is available for offline use as a self-contained HTML package or a PDF file. These are generated automatically with every release and are always up-to-date with the latest published documentation.

Download Formats
-----------------

HTML Package (.zip)
~~~~~~~~~~~~~~~~~~~~

The HTML package is a complete, self-contained copy of this documentation site. It includes all pages, images, stylesheets, and search functionality, and can be browsed offline in any modern web browser.

**Best for:** Air-gapped environments, local intranets, offline reference.

`Download HTML package <https://docs.mattermost.com/downloads/mattermost-docs-html.zip>`__

After downloading, extract the zip file and open ``mattermost-docs/index.html`` in your browser.

PDF
~~~~

The PDF is a single-document version of the full documentation, suitable for printing or reading in a PDF viewer.

**Best for:** Printing, compliance archives, sharing with stakeholders.

`Download PDF <https://docs.mattermost.com/downloads/mattermost-docs.pdf>`__

Build Locally
--------------

You can also build the documentation locally from the `source repository <https://github.com/mattermost/docs>`__. This is useful if you need a customized build or want to package documentation for a specific version.

Prerequisites
~~~~~~~~~~~~~~

- Python 3.11 or later
- pipenv
- GNU Make 3.82 or later

Build the HTML package
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Clone the repository
   git clone https://github.com/mattermost/docs.git
   cd docs

   # Install dependencies
   make python-deps

   # Build HTML and package it as a zip
   make html
   make html-package

The zip file will be created at ``build/downloads/mattermost-docs-html.zip``.

Build the PDF
~~~~~~~~~~~~~~

.. code-block:: bash

   # Build the PDF (builds single-page HTML first, then converts to PDF)
   make pdf

The PDF file will be created at ``build/downloads/mattermost-docs.pdf``.

.. note::

   PDF generation requires `WeasyPrint <https://weasyprint.org/>`__ and its system dependencies. On Ubuntu/Debian, install them with:

   .. code-block:: bash

      sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz-subset0

   See the `WeasyPrint installation guide <https://doc.courtbouillon.org/weasyprint/stable/first_steps.html>`__ for other platforms.

Build all formats at once
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Build HTML first, then generate all download artifacts
   make html
   make downloads

This creates both the HTML zip and the PDF in the ``build/downloads/`` directory.
