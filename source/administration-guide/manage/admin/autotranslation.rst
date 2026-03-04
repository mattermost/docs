Set up autotranslation (Beta)
==============================

.. include:: ../../../_static/badges/ent-adv.rst
  :start-after: :nosearch:

From Mattermost v11.5, autotranslation automatically translates channel messages into each user's preferred display language. This enables multilingual teams to collaborate without language barriers.

Autotranslation uses an asynchronous queue-based architecture. When a message is posted in a channel with autotranslation enabled, the message is queued for translation into every configured target language. Translated messages replace the original display for users whose display language matches a target language, and they can toggle to view the original text at any time.

Two translation provider options are available:

- **LibreTranslate**: A self-hosted, open-source machine translation engine.
- **Agents**: Uses the Mattermost Agents plugin with a configured LLM backend.

Before you begin
----------------

- A Mattermost **Enterprise Advanced** license is required.
- Choose a translation provider and ensure its infrastructure is available:

  - **LibreTranslate**: A running LibreTranslate server reachable from the Mattermost server.
  - **Agents**: The :doc:`Mattermost Agents plugin </administration-guide/configure/agents-admin-guide>` installed and configured with at least one LLM service.

Enable autotranslation
----------------------

1. Go to **System Console > Site Configuration > Localization**.
2. Set :ref:`Enable autotranslation <administration-guide/configure/site-configuration-settings:enable autotranslation>` to **True**.
3. Select a :ref:`Translation provider <administration-guide/configure/site-configuration-settings:translation provider>` (``libretranslate`` or ``agents``).
4. Configure :ref:`Target languages <administration-guide/configure/site-configuration-settings:target languages>` — every message in autotranslation-enabled channels is translated into each language in this list.
5. Select **Save**.

See the :ref:`autotranslation configuration reference <administration-guide/configure/site-configuration-settings:autotranslation>` for all available settings.

Set up LibreTranslate
---------------------

`LibreTranslate <https://libretranslate.com/>`__ is a self-hosted, open-source machine translation engine. See the `LibreTranslate documentation <https://github.com/LibreTranslate/LibreTranslate>`__ for deployment instructions.

Once your LibreTranslate server is running:

1. Go to **System Console > Site Configuration > Localization**.
2. Set **Translation provider** to ``libretranslate``.
3. Enter the :ref:`LibreTranslate URL <administration-guide/configure/site-configuration-settings:libretranslate url>` (for example, ``http://libretranslate.internal:5000``).
4. If your LibreTranslate instance requires authentication, enter the :ref:`LibreTranslate API key <administration-guide/configure/site-configuration-settings:libretranslate api key>`.
5. Select **Save**.

.. important::

   The Mattermost server must be able to reach the LibreTranslate URL over the network. Ensure firewall rules and DNS resolution allow connectivity between the Mattermost server and the LibreTranslate instance.

Set up the Agents provider
--------------------------

The Agents provider uses the Mattermost Agents plugin to translate messages via a configured LLM service.

Prerequisites:

- The :doc:`Mattermost Agents plugin </administration-guide/configure/agents-admin-guide>` is installed and enabled.
- At least one LLM service is configured in the Agents plugin.

To configure:

1. Go to **System Console > Site Configuration > Localization**.
2. Set **Translation provider** to ``agents``.
3. Enter the :ref:`Agents LLM service ID <administration-guide/configure/site-configuration-settings:agents llm service id>` matching the LLM service configured in the Agents plugin.
4. Select **Save**.

.. tip::

   **Choosing between LibreTranslate and Agents**: LibreTranslate is a lightweight, self-hosted translation engine. The Agents provider uses an LLM backend and generally produces more accurate translations, especially for languages such as Japanese, Korean, and Chinese where contextual understanding improves quality. Consider your translation quality needs and existing infrastructure when choosing.

   **Choosing an LLM for the Agents provider**: Smaller, faster models are recommended for autotranslation. Translation is a well-defined task that doesn't benefit from the extended reasoning capabilities of larger models — larger models may actually overthink the task, adding unnecessary latency without improving quality. A model like ``gpt-3.5-turbo`` provides accurate translations with lower latency.

Manage autotranslation per channel
----------------------------------

Autotranslation is managed on a per-channel basis and is disabled by default for all channels. System admins and channel admins can enable or disable autotranslation for individual channels.

- When autotranslation is enabled or disabled in a channel, a system post notifies channel members of the change.
- Use the :ref:`Restrict autotranslation in direct and group messages <administration-guide/configure/site-configuration-settings:restrict autotranslation in direct and group messages>` setting to control whether autotranslation can be enabled in direct and group messages.

Tune worker performance
-----------------------

How the translation queue works
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a message is posted in a channel with autotranslation enabled, it's added to a per-node translation queue. A worker picks up the post and translates it sequentially into each configured target language. Each completed language translation triggers a websocket broadcast to the channel so users see translations arrive in real time.

In a high availability deployment, each node runs its own pool of workers and processes its own queue independently.

Calculate your worker count
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following formula to estimate how many workers each node needs:

.. code-block:: text

   required_workers = ceil(
     (posts_per_sec × pct_autotranslated × num_languages × avg_provider_latency_ms / 1000)
     / num_app_nodes
     × 1.2
   )

Where:

- **posts_per_sec** — average message rate across the server.
- **pct_autotranslated** — fraction of posts in autotranslation-enabled channels (0.0–1.0).
- **num_languages** — number of configured target languages.
- **avg_provider_latency_ms** — mean response time from the translation provider in milliseconds.
- **num_app_nodes** — number of Mattermost application nodes.
- **1.2** — headroom factor (20%) to absorb traffic bursts.

The following table shows results from load tests with 6,500 concurrent users, 2 app nodes, ~5 posts/sec, and ~2 s mean provider latency. The provider latency distribution used in testing was realistic, with buckets ranging from 500 ms to 10 s weighted toward the 500 ms–1.5 s range, producing a ~2 s mean.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Target languages
     - % autotranslated
     - Workers per node
   * - 7
     - 100%
     - 38
   * - 6
     - 100%
     - 32
   * - 3
     - 75%
     - 8

.. note::

   In the 6-language test the formula yields 33, but workers were capped at 32 due to the configured maximum. Adjust the :ref:`Translation workers <administration-guide/configure/site-configuration-settings:translation workers>` setting to match your calculated value.

Scaling considerations
~~~~~~~~~~~~~~~~~~~~~~

- **Target languages are the biggest multiplier.** Each additional language increases both worker time per post and the number of websocket broadcasts per post. Reducing the number of target languages is the most effective way to reduce load.
- **Websocket traffic scales with languages.** Each target language produces one channel-wide websocket broadcast per translated post. Under high load, the main symptom of saturation is websocket disconnects caused by per-connection send queues filling up.
- **Provider latency shapes traffic patterns.** Lower latency means translations complete in quicker bursts, concentrating websocket traffic. Higher latency spreads events over time. Monitor provider response times and factor them into your capacity planning.

Monitor with Prometheus
~~~~~~~~~~~~~~~~~~~~~~~

Mattermost exposes the following Prometheus metrics for autotranslation:

- ``mattermost_autotranslation_queue_depth_total`` *(Gauge)* — current tasks waiting in the queue. A steadily rising value means workers can't keep up with incoming posts.
- ``mattermost_autotranslation_provider_call_duration_seconds`` *(Histogram; labels: provider, result)* — translation provider latency. This is the ``avg_provider_latency_ms`` value used in the formula above. Calculate the average with the following PromQL query:

  .. code-block:: promql

     rate(mattermost_autotranslation_provider_call_duration_seconds_sum{result="success"}[10m])
     /
     rate(mattermost_autotranslation_provider_call_duration_seconds_count{result="success"}[10m])

- ``mattermost_autotranslation_worker_task_duration_seconds`` *(Histogram)* — total time for a worker to process one post across all target languages.

Configuration reference
~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`Translation workers <administration-guide/configure/site-configuration-settings:translation workers>`: The number of concurrent workers per node. Default is **6**. Increase this value for high-traffic deployments or decrease it to reduce resource consumption.
- :ref:`Translation timeout <administration-guide/configure/site-configuration-settings:translation timeout>`: The maximum time in milliseconds for a single translation request. Default is **5000** ms (5 seconds). Increase this value if your translation provider is experiencing timeouts due to network latency or high load.

You can also update the worker count from the command line using mmctl:

.. code-block:: shell

   mmctl config set AutoTranslationSettings.Workers <number>

Frequently asked questions
--------------------------

Why aren't messages being translated?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Verify autotranslation is enabled globally in **System Console > Site Configuration > Localization**.
- Verify autotranslation is enabled for the specific channel.
- Confirm a translation provider is selected and properly configured.
- Check that the Mattermost server can reach the translation provider (LibreTranslate URL or Agents plugin).
- Review Mattermost server logs for translation errors.

What happens when the translation provider is unavailable?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Messages are still posted normally. Translations that fail due to provider downtime are skipped, and users see the original untranslated message. When the provider recovers, new messages are translated as expected.

What languages are supported?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Supported languages depend on the translation provider:

- **LibreTranslate**: Supports the languages available in your LibreTranslate deployment. See the `LibreTranslate language list <https://libretranslate.com/languages>`__ for details.
- **Agents**: Language support depends on the capabilities of the configured LLM. Most modern LLMs support a wide range of languages.

Configure the :ref:`Target languages <administration-guide/configure/site-configuration-settings:target languages>` setting to specify which languages all messages are translated into.
