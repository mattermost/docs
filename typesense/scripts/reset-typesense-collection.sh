TYPESENSE_HOST="${TYPESENSE_HOST:-http://localhost:8108}"
TYPESENSE_API_KEY="${TYPESENSE_API_KEY:-test_api_key}"
TYPESENSE_COLLECTION_NAME="mm_product_docs"

curl -X DELETE \
  "${TYPESENSE_HOST}/collections/${TYPESENSE_COLLECTION_NAME}/documents?truncate=true&filter_by=anchor:!=none" \
  -H "X-TYPESENSE-API-KEY: ${TYPESENSE_API_KEY}"
