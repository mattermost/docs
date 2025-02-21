import re
import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("Usage: python fix_config_settings.py <rst_file_path>")
    sys.exit(1)

def to_slug(text):
    # Convert text to lowercase and replace spaces with hyphens
    slug = text.lower().replace(' ', '-')
    # Remove any characters that aren't alphanumeric or hyphens
    slug = re.sub(r'[^a-z0-9-]', '', slug)
    # Replace multiple hyphens with single hyphen
    slug = re.sub(r'-+', '-', slug)
    return slug

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all config:setting directives and their associated headings
    pattern = r'\.\.[\s]*config:setting::[\s]*([^\n]+)[\s\S]*?(?=^[^\s#].*$\n[-~=]+$)(.*?)\n[-~=]+'
    matches = re.finditer(pattern, content, re.MULTILINE)

    for match in matches:
        directive_value = match.group(1).strip()
        heading = match.group(2).strip()
        
        # Convert heading to slug format
        heading_slug = to_slug(heading)
        
        if directive_value != heading_slug:
            # Replace the directive value with the heading slug
            old_directive = f'.. config:setting:: {directive_value}'
            new_directive = f'.. config:setting:: {heading_slug}'
            content = content.replace(old_directive, new_directive)

    # Write the modified content back to the file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    filepath = sys.argv[1]
    process_file(filepath)
