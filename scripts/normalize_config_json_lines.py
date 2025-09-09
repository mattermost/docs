import re
import sys
from pathlib import Path


SMART_QUOTES = {
    "“": '"',
    "”": '"',
    "’": "'",
    "‘": "'",
}


def normalize_quotes(text: str) -> str:
    for bad, good in SMART_QUOTES.items():
        text = text.replace(bad, good)
    return text


def parse_setting_value(raw: str):
    raw = normalize_quotes(raw.strip())
    # Trim trailing commas or stray quotes
    raw = raw.rstrip(',')
    # Remove surrounding backticks if present (defensive)
    raw = raw.strip('`')

    # Fix unmatched quotes if present (e.g., 2048" or "2048)
    if raw.endswith('"') and not raw.startswith('"'):
        raw = raw[:-1]
    if raw.startswith('"') and not raw.endswith('"'):
        raw = raw[1:]

    # Detect empties like "" or ''
    if raw in ('""', "''"):
        return '""', 'string'

    # Detect arrays/objects
    if raw.startswith('[') or raw.startswith('{'):
        return raw, 'json'

    # Booleans
    if raw.lower() in ('true', 'false'):
        return raw.lower(), 'bool'

    # Numeric (int/float, allow leading -)
    if re.fullmatch(r'-?\d+(?:\.\d+)?', raw):
        return raw, 'number'

    # If value is quoted, keep as string
    if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
        # Normalize to double quotes
        inner = raw[1:-1]
        inner = inner.replace('"', '\\"')
        return f'"{inner}"', 'string'

    # Heuristics: treat everything else as string; ensure double quotes
    # Examples: 03:00, s3.amazonaws.com, #f2a93b
    return f'"{raw}"', 'string'


def convert_path_to_section_key(dotted: str):
    dotted = normalize_quotes(dotted.strip())
    # Remove surrounding stray quotes and leading dots
    dotted = dotted.lstrip("\"'")
    dotted = dotted.lstrip('.')
    # Extract path and default (if path contains ':')
    default_part = None
    # Split on first ':' that separates default; allow values like 03:00 by splitting only on the first colon after the key
    if ':' in dotted:
        parts = dotted.split(':', 1)
        path_part = parts[0].strip()
        default_part = parts[1].strip()
    else:
        path_part = dotted.strip()

    # Sometimes path may still end with quotes or commas
    path_part = path_part.strip('",')

    tokens = path_part.split('.')
    if len(tokens) < 2:
        # Unexpected; return as-is
        section = tokens[0] if tokens else ''
        key = ''
    else:
        section, key = tokens[0], tokens[1]

    # Normalize common casing mishaps like Elasticsearchsettings -> ElasticsearchSettings
    # Only fix if the exact lowercase pattern 'settings' is present at the end of the word
    if section.lower().endswith('settings') and not section.endswith('Settings'):
        base = section[:-8]
        section = f'{base}Settings'

    return section, key, default_part


def rewrite_line(line: str) -> str:
    # Replace the backticked inner content after the label with normalized form
    pattern = re.compile(r'(``config\.json`` setting:\s*)``([^`]*)``')

    def _repl(m: re.Match) -> str:
        inner = m.group(2)
        section, key, default_raw = convert_path_to_section_key(inner)
        default_text = ''
        if default_raw is not None and default_raw != '':
            value, _ = parse_setting_value(default_raw)
            default_text = f' > ``{value}``'
        new_rhs = f'``{section}`` > ``{key}``{default_text}'
        return f'{m.group(1)}{new_rhs}'

    return pattern.sub(_repl, line)


def process_file(path: Path) -> str:
    content = path.read_text(encoding='utf-8')
    lines = content.splitlines(keepends=True)
    new_lines = []
    for line in lines:
        if '``config.json`` setting:' in line:
            line = rewrite_line(line)
        new_lines.append(line)
    new_content = ''.join(new_lines)
    path.write_text(new_content, encoding='utf-8')
    return new_content


def main():
    if len(sys.argv) != 2:
        print('Usage: python scripts/normalize_config_json_lines.py <rst_file_path>')
        sys.exit(1)
    target = Path(sys.argv[1])
    if not target.exists():
        print(f'File not found: {target}')
        sys.exit(2)
    process_file(target)


if __name__ == '__main__':
    main()


