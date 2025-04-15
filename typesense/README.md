# Using Typesense for documentation search

We'll have 3 terminals open, and run the following in the first two:
- `make livehtml` - Run Sphinx docs server
- `cd typesense && docker compose up typesense` - Run Typesense server

After those are running, in the third terminal:
- `cd typesense && docker compose up scraper` - Run scraper to populate Typesense. The process will exit once complete


If you'd like to re-index the docs, you can run:

```sh
cd typesense
./scripts/reset-typesense-collection.sh # This will delete all existing documents in the collection. Typesense will de-duplicate docs naturally, but this forces it to remove metadata from previous runs that we may want to remove as we change the schema/filters.
docker compose up scraper
```

To export the index into a jsonl file, run:

```sh
cd typesense
./scripts/download-typesense-collection.sh
```

---

The scripts mentioned above support the following environment variables for configuration:

- `TYPESENSE_API_KEY` - Defaults to `test_api_key`
- `TYPESENSE_HOST` - Defaults to `http://localhost:8108`
- `TYPESENSE_HOSTNAME` - Defaults to `localhost`
- `TYPESENSE_PORT` - Defaults to `8108`
- `TYPESENSE_PROTOCOL` - Defaults to `http`
