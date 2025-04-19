set -e

export TYPESENSE_ORIGIN="${TYPESENSE_ORIGIN:-http://localhost:8108}"
export TYPESENSE_API_KEY="${TYPESENSE_API_KEY:-test_api_key}"
export DOCS_SITE_ORIGIN="${DOCS_SITE_ORIGIN:-http://localhost:8000}"
export TYPESENSE_COLLECTION_NAME="${TYPESENSE_COLLECTION_NAME:-mm_product_docs}"

echo "Downloading typesense collection"
./scripts/download-typesense-collection.sh

echo "Cleaning relative links in typesense collection"
./scripts/clean-relative-links-in-typesense-collection.sh

echo "Importing typesense collection"
./scripts/import-typesense-collection.sh

echo "Making alias for typesense collection"
./scripts/make-alias-for-typesense-collection.sh
