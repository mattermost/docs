TYPESENSE_HOST="${TYPESENSE_HOST:-http://localhost:8108}"
TYPESENSE_API_KEY="${TYPESENSE_API_KEY:-test_api_key}"

curl "${TYPESENSE_HOST}/collections/mm_product_docs/documents/export" \
       -X GET \
       -H "X-TYPESENSE-API-KEY: ${TYPESENSE_API_KEY}" \
       -o documents.jsonl
