TYPESENSE_ORIGIN="${TYPESENSE_ORIGIN:-http://localhost:8108}"
TYPESENSE_API_KEY="${TYPESENSE_API_KEY:-test_api_key}"

curl "${TYPESENSE_ORIGIN}/collections" \
       -X POST \
       -H "Content-Type: application/json" \
       -H "X-TYPESENSE-API-KEY: ${TYPESENSE_API_KEY}" \
       -d '{
         "name": "mm_product_docs",
         "fields": [
           {"name": "category", "type": "string" },
           {"name": "weight", "type": "int32" }
         ],
         "default_sorting_field": "weight"
       }'
