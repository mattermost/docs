TYPESENSE_ORIGIN="${TYPESENSE_ORIGIN:-http://localhost:8108}"
TYPESENSE_API_KEY="${TYPESENSE_API_KEY:-test_api_key}"
TYPESENSE_COLLECTION_NAME="${TYPESENSE_COLLECTION_NAME:-mm_product_docs}"

curl "${TYPESENSE_ORIGIN}/aliases/mm_product_docs" -X PUT \
    -H "Content-Type: application/json" \
    -H "X-TYPESENSE-API-KEY: ${TYPESENSE_API_KEY}" -d "{
        \"collection_name\": \"${TYPESENSE_COLLECTION_NAME}\"
    }"
