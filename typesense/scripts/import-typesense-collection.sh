TYPESENSE_ORIGIN="${TYPESENSE_ORIGIN:-http://localhost:8108}"
TYPESENSE_API_KEY="${TYPESENSE_API_KEY:-test_api_key}"
TYPESENSE_COLLECTION_NAME="${TYPESENSE_COLLECTION_NAME:-mm_product_docs}"

curl -X POST "${TYPESENSE_ORIGIN}/collections/${TYPESENSE_COLLECTION_NAME}/documents/import?action=upsert" \
     -H "X-TYPESENSE-API-KEY: ${TYPESENSE_API_KEY}" \
     -H "Content-Type: text/plain" \
     --data-binary @processed_documents.jsonl
