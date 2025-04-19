input_file="documents.jsonl"
output_file="processed_documents.jsonl"

DOCS_SITE_ORIGIN="${DOCS_SITE_ORIGIN:-http://localhost:8000}"

cat "documents.jsonl" | python3 -c "
import sys, json

for line in sys.stdin:
    try:
        doc = json.loads(line)
        for key in ['url', 'url_without_anchor', 'url_without_variables']:
            if key in doc and doc[key].startswith('${DOCS_SITE_ORIGIN}'):
                doc[key] = doc[key][len('${DOCS_SITE_ORIGIN}'):]
        print(json.dumps(doc))
    except Exception as e:
        print(f'// skipped invalid line: {line.strip()}', file=sys.stderr)
" > processed_documents.jsonl
