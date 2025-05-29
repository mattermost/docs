#!/usr/bin/env python3

"""
Script to detect duplicate redirects in conf.py
"""

import os
import sys
from collections import defaultdict


def load_redirects():
    """Load redirects dictionary from conf.py"""
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'source'))
    import redirects as redirects_py
    return redirects_py.redirects_map

def find_duplicate_redirects(redirects):
    """
    Analyze redirects dictionary for duplicates
    Returns tuple of (duplicate_sources, sources_to_same_target)
    """
    # Track sources that map to the same target
    target_to_sources = defaultdict(list)
    # Track duplicate sources
    source_to_targets = defaultdict(list)

    for source, target in redirects.items():
        # Track this source->target mapping
        source_to_targets[source].append(target)
        # Track this target's source
        target_to_sources[target].append(source)

    # Find duplicates
    duplicate_sources = {
        source: targets
        for source, targets in source_to_targets.items()
        if len(targets) > 1
    }

    sources_to_same_target = {
        target: sources
        for target, sources in target_to_sources.items()
        if len(sources) > 1
    }

    return duplicate_sources, sources_to_same_target

def write_warnings(duplicate_sources, sources_to_same_target):
    """Write warning messages to warnings.log"""
    os.makedirs('build', exist_ok=True)

    with open('build/warnings.log', 'a') as log:
        if duplicate_sources:
            warning = "\nDuplicate sources found (same source maps to multiple targets):\n"
            log.write(warning)
            print(warning)

            for source, targets in duplicate_sources.items():
                msg = f"Source: {source}\n"
                msg += f"Maps to multiple targets: {targets}\n"
                log.write(msg)
                print(msg)

        if sources_to_same_target:
            warning = "\nMultiple sources map to same target:\n"
            log.write(warning)
            print(warning)

            for target, sources in sources_to_same_target.items():
                msg = f"Target: {target}\n"
                msg += f"Has multiple sources: {sources}\n"
                log.write(msg)
                print(msg)

def main():
    redirects = load_redirects()
    duplicate_sources, sources_to_same_target = find_duplicate_redirects(redirects)
    write_warnings(duplicate_sources, sources_to_same_target)

    # Return non-zero exit code if duplicates found
    return 1 if duplicate_sources else 0

if __name__ == '__main__':
    sys.exit(main())
