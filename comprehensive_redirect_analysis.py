#!/usr/bin/env python3
"""
Comprehensive analysis to find ALL restructuring changes that might need redirects.
This goes beyond just renames to catch deletions, additions, and other structural changes.
"""

import subprocess
import sys
from pathlib import Path

def get_all_changes():
    """Get all file changes from git diff."""
    result = subprocess.run(
        ['git', 'diff', 'master..HEAD', '--name-status'],
        capture_output=True,
        text=True,
        cwd='.'
    )
    
    renames = []
    deletions = []
    additions = []
    modifications = []
    
    for line in result.stdout.strip().split('\n'):
        if not line:
            continue
            
        parts = line.split('\t')
        status = parts[0].strip()
        
        if status.startswith('R'):
            # Renames - we've already handled these
            if len(parts) >= 3:
                old_path = parts[1].strip()
                new_path = parts[2].strip()
                renames.append((old_path, new_path))
        elif status == 'D':
            # Deletions - might need redirects if content moved elsewhere
            deleted_file = parts[1].strip()
            deletions.append(deleted_file)
        elif status == 'A':
            # Additions - might be new location for deleted content
            added_file = parts[1].strip()
            additions.append(added_file)
        elif status == 'M':
            # Modifications - might indicate restructuring
            modified_file = parts[1].strip()
            modifications.append(modified_file)
    
    return renames, deletions, additions, modifications

def get_existing_redirects():
    """Get existing redirects from redirects.py."""
    sys.path.append('source')
    from redirects import redirects_map
    return redirects_map

def analyze_deletions(deletions, additions, existing_redirects):
    """Analyze deleted files to see if they might need redirects."""
    print("🔍 ANALYZING DELETED FILES FOR POTENTIAL REDIRECT NEEDS:")
    print("=" * 70)
    
    doc_deletions = []
    for deleted in deletions:
        if deleted.startswith('source/') and (deleted.endswith('.rst') or deleted.endswith('.md')):
            # Convert to URL format
            url = deleted.replace('source/', '').replace('.rst', '.html').replace('.md', '.html')
            doc_deletions.append((deleted, url))
    
    print(f"Found {len(doc_deletions)} deleted documentation files:")
    
    potential_missing = []
    for deleted_file, url in doc_deletions:
        if url not in existing_redirects:
            # Check if there's a likely new location in additions
            likely_new_location = find_likely_new_location(deleted_file, additions)
            potential_missing.append((url, deleted_file, likely_new_location))
            print(f"❌ {url}")
            print(f"   Original: {deleted_file}")
            if likely_new_location:
                print(f"   Possible new location: {likely_new_location}")
            print()
    
    return potential_missing

def find_likely_new_location(deleted_file, additions):
    """Try to find likely new location for deleted file."""
    # Extract just the filename
    filename = Path(deleted_file).name
    
    # Look for files with same name in additions
    for added in additions:
        if Path(added).name == filename:
            return added
    
    # Look for similar names (without extension matching)
    base_name = Path(deleted_file).stem
    for added in additions:
        if Path(added).stem == base_name:
            return added
    
    return None

def check_content_reorganization():
    """Check for major content reorganization by comparing directory structures."""
    print("\n🔍 CHECKING FOR DIRECTORY STRUCTURE CHANGES:")
    print("=" * 50)
    
    # Get current source directories
    result_current = subprocess.run(
        ['find', 'source', '-type', 'd', '-name', '*'],
        capture_output=True,
        text=True,
        cwd='.'
    )
    
    # Get master source directories  
    result_master = subprocess.run(
        ['git', 'show', 'master:source', '--name-only'],
        capture_output=True,
        text=True,
        cwd='.'
    )
    
    if result_current.returncode == 0:
        current_dirs = set(result_current.stdout.strip().split('\n'))
        print(f"Current branch directories: {len(current_dirs)}")
        
        # Look for significant structural changes
        major_dirs = [d for d in current_dirs if '/' in d and not d.startswith('source/_')]
        print(f"Major content directories: {len(major_dirs)}")

def main():
    print("🔍 COMPREHENSIVE REDIRECT ANALYSIS")
    print("=" * 50)
    
    renames, deletions, additions, modifications = get_all_changes()
    existing_redirects = get_existing_redirects()
    
    print(f"📊 CHANGE SUMMARY:")
    print(f"   Renames: {len(renames)}")
    print(f"   Deletions: {len(deletions)}")
    print(f"   Additions: {len(additions)}")
    print(f"   Modifications: {len(modifications)}")
    print(f"   Existing redirects: {len(existing_redirects)}")
    print()
    
    # Analyze deletions for potential missing redirects
    potential_missing = analyze_deletions(deletions, additions, existing_redirects)
    
    # Check for content reorganization
    check_content_reorganization()
    
    # Look for index files that might need special attention
    print("\n🔍 CHECKING FOR INDEX FILE REDIRECTS:")
    print("=" * 40)
    index_files = [d for d in deletions if 'index' in d.lower()]
    for idx_file in index_files:
        if idx_file.startswith('source/'):
            url = idx_file.replace('source/', '').replace('.rst', '.html').replace('.md', '.html')
            if url not in existing_redirects:
                print(f"❌ Potential missing index redirect: {url}")
    
    print(f"\n📋 SUMMARY:")
    print(f"   Potential missing redirects from deletions: {len(potential_missing)}")
    print(f"   Index files to check: {len(index_files)}")
    
    if potential_missing:
        print(f"\n🚨 POTENTIAL MISSING REDIRECTS:")
        for url, original, new_loc in potential_missing:
            print(f'"{url}":')
            if new_loc:
                new_url = new_loc.replace('source/', '').replace('.rst', '.html').replace('.md', '.html')
                print(f'        "https://docs.mattermost.com/{new_url}",')
            else:
                print(f'        "https://docs.mattermost.com/[NEEDS_MANUAL_REVIEW]",')
    else:
        print("\n✅ No additional missing redirects found!")

if __name__ == "__main__":
    main()