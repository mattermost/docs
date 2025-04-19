# Using Typesense for documentation search

With 3 terminals open, and run the following in the first two:
- `make livehtml` - Run Sphinx docs server
- `cd typesense && docker compose` - Run Typesense server and Typesense dashboard. You can access the Typesense dashboard at http://localhost:8001

After those are up and running, run this in the third terminal:
- `cd typesense && docker compose --profile optional up scraper` - Run scraper to populate Typesense. The process will exit once complete.

After running the scraper, we need to do some processing to make search result urls relative to the docs site.
- `cd typesense && ./post-process-typesense-data.sh`

If you'd like to re-index the Typesense collection, you can run:

```sh
cd typesense

# Optionally delete all existing documents in the collection. Typesense will de-duplicate docs naturally, but this reset operation forces it to remove metadata from previous runs that we may want to remove as we change the schema/filters.
./scripts/reset-typesense-collection.sh

# Re-run scraper to populate Typesense
docker compose --profile optional up scraper
```

To export the index into a jsonl file, run:

```sh
cd typesense

./scripts/download-typesense-collection.sh
```

The output of the command will be a `documents.jsonl` file in the current directory.

---

The scripts mentioned above support the following environment variables for configuration:

- `TYPESENSE_API_KEY` - Defaults to `test_api_key`
- `TYPESENSE_ORIGIN` - Defaults to `http://localhost:8108`
- `TYPESENSE_HOSTNAME` - Defaults to `localhost`
- `TYPESENSE_PORT` - Defaults to `8108`
- `TYPESENSE_PROTOCOL` - Defaults to `http`
