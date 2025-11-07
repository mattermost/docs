$(document).ready(function () {
    // Enhanced UI Changelog Filter - Support for v10, v11, and legacy releases
    const currentPath = window.location.pathname;
    const isChangelogPage = currentPath.includes('/mattermost-v10-changelog') || 
                           currentPath.includes('/mattermost-v11-changelog') || 
                           currentPath.includes('/unsupported-legacy-releases') ||
                           currentPath.includes('/about/mattermost-v10-changelog') || 
                           currentPath.includes('/about/mattermost-v9-changelog');

    if (!isChangelogPage) {
        return;
    }

    // UI-related keywords for smart content detection
    const uiKeywords = [
        'user interface', 'ui', 'interface', 'design', 'theme', 'styling', 'css',
        'button', 'menu', 'modal', 'dialog', 'popup', 'sidebar', 'navbar', 'header', 'footer',
        'layout', 'responsive', 'mobile view', 'desktop view', 'tablet view',
        'font', 'color', 'icon', 'logo', 'image', 'avatar', 'profile picture',
        'tooltip', 'dropdown', 'tab', 'panel', 'card', 'badge', 'tag', 'label',
        'form', 'input', 'textarea', 'checkbox', 'radio', 'select', 'slider',
        'loading', 'spinner', 'progress', 'animation', 'transition', 'hover',
        'dark mode', 'light mode', 'theme', 'appearance', 'visual',
        'accessibility', 'a11y', 'screen reader', 'keyboard navigation',
        'emoji', 'emoticon', 'reaction', 'status indicator'
    ];

    // Extract versions from section IDs
    const versions = [];
    const sections = [];
    const tocItems = [];

    // Find all release sections based on the heading pattern
    $('section[id^="release-v"]').each(function () {
        const sectionId = $(this).attr('id');
        const versionMatch = sectionId.match(/release-v(\d+)-(\d+)(-\d+)?/);

        if (versionMatch) {
            // Format: major.minor or major.minor.patch
            const major = parseInt(versionMatch[1]);
            const minor = parseInt(versionMatch[2]);
            const patch = versionMatch[3] ? parseInt(versionMatch[3].substring(1)) : null;
            const version = patch !== null ? `${major}.${minor}.${patch}` : `${major}.${minor}`;

            if (!versions.includes(version)) {
                versions.push(version);
            }

            // Associate section with version and detect UI content
            const $section = $(this);
            const sectionText = $section.text().toLowerCase();
            const hasUIContent = uiKeywords.some(keyword => sectionText.includes(keyword));

            sections.push({
                section: $section,
                version: version,
                id: sectionId,
                hasUI: hasUIContent,
                originalText: sectionText
            });
        }
    });

    // Find corresponding TOC items in the sidebar
    $('.toc-drawer li, .toctree-l1, .toctree-l2, .toctree-l3').each(function () {
        const $link = $(this).find('a').first();
        if ($link.length) {
            const href = $link.attr('href');
            if (href && href.includes('#')) {
                const sectionId = href.split('#')[1];
                // Check if this links to a version section using the same regex
                const versionMatch = sectionId.match(/release-v(\d+)-(\d+)(-\d+)?/);
                if (versionMatch) {
                    const major = parseInt(versionMatch[1]);
                    const minor = parseInt(versionMatch[2]);
                    const patch = versionMatch[3] ? parseInt(versionMatch[3].substring(1)) : null;
                    const version = patch !== null ? `${major}.${minor}.${patch}` : `${major}.${minor}`;

                    // This TOC item links to a version section
                    tocItems.push({
                        item: $(this),
                        version: version,
                        id: sectionId
                    });
                }
            }
        }
    });

    // Sort versions in descending order (newest first)
    versions.sort((a, b) => {
        const partsA = a.split('.').map(n => parseInt(n));
        const partsB = b.split('.').map(n => parseInt(n));
        
        for (let i = 0; i < Math.max(partsA.length, partsB.length); i++) {
            const partA = partsA[i] || 0;
            const partB = partsB[i] || 0;
            if (partA !== partB) {
                return partB - partA; // Descending order
            }
        }
        return 0;
    });

    // Create enhanced filter controls matching the mockup
    const filterHTML = `
        <div class="ui-changelog-filters">
            <h3>Filters</h3>
            <div class="filter-description">Filter changelog entries by version range and content type</div>
            <div class="ui-filter-controls">
                <div class="ui-filter-group">
                    <label for="ui-changelog-from-version">From version:</label>
                    <div class="helper-text">Choose the earliest version to include</div>
                    <select id="ui-changelog-from-version">
                        <option value="all">All versions</option>
                        ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                    </select>
                </div>
                
                <div class="ui-filter-group">
                    <label for="ui-changelog-to-version">To version:</label>
                    <div class="helper-text">Choose the latest version to include</div>
                    <select id="ui-changelog-to-version">
                        <option value="all">All versions</option>
                        ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                    </select>
                </div>
                
                <div class="ui-filter-group">
                    <label for="ui-changelog-change-type">Change type:</label>
                    <div class="helper-text">Filter by content type</div>
                    <select id="ui-changelog-change-type">
                        <option value="all">All changes</option>
                        <option value="ui">UI changes</option>
                    </select>
                </div>
                
                <div class="ui-filter-actions">
                    <button id="ui-changelog-apply-filter" class="ui-filter-btn primary">Apply</button>
                    <button id="ui-changelog-reset-filter" class="ui-filter-btn secondary">Reset</button>
                    <button id="ui-changelog-clear-filter" class="ui-filter-clear" style="display: none;">✕ Clear filters</button>
                </div>
            </div>
        </div>
    `;

    // Insert filter controls above the content
    $('.content h1:first, .document h1:first, main h1:first').first().after(filterHTML);

    // Add data attributes to sections for easier filtering
    sections.forEach(item => {
        item.section.attr('data-version', item.version);
        if (item.hasUI) {
            item.section.attr('data-has-ui', 'true');
        }
    });

    // Helper function to parse version strings
    function parseVersion(versionStr) {
        if (versionStr === 'all') return { major: 0, minor: 0, patch: 0 };
        const parts = versionStr.split('.').map(n => parseInt(n));
        return {
            major: parts[0] || 0,
            minor: parts[1] || 0,
            patch: parts[2] || 0
        };
    }

    // Helper function to compare versions
    function compareVersions(a, b) {
        if (a.major !== b.major) return a.major - b.major;
        if (a.minor !== b.minor) return a.minor - b.minor;
        return (a.patch || 0) - (b.patch || 0);
    }

    // Apply filters with auto-apply on change
    function applyFilters() {
        const fromVersion = $('#ui-changelog-from-version').val();
        const toVersion = $('#ui-changelog-to-version').val();
        const changeType = $('#ui-changelog-change-type').val();

        // Clear previous messages
        $('.ui-filter-status, .ui-filter-error').remove();
        $('.ui-content-highlighted').removeClass('ui-content-highlighted');

        // Validation
        if (fromVersion !== 'all' && toVersion !== 'all') {
            const fromV = parseVersion(fromVersion);
            const toV = parseVersion(toVersion);
            
            if (compareVersions(toV, fromV) < 0) {
                $('.ui-changelog-filters').append(
                    '<div class="ui-filter-error">' +
                    'Error: "To version" must be greater than or equal to "From version".' +
                    '</div>'
                );
                return;
            }
        }

        let visibleCount = 0;
        let totalCount = sections.length;

        // Filter sections
        sections.forEach(item => {
            const sectionV = parseVersion(item.version);
            let shouldShow = true;

            // Version range filtering
            if (fromVersion !== 'all') {
                const fromV = parseVersion(fromVersion);
                if (compareVersions(sectionV, fromV) < 0) {
                    shouldShow = false;
                }
            }

            if (toVersion !== 'all' && shouldShow) {
                const toV = parseVersion(toVersion);
                if (compareVersions(sectionV, toV) > 0) {
                    shouldShow = false;
                }
            }

            // Change type filtering
            if (changeType === 'ui' && shouldShow) {
                if (!item.hasUI) {
                    shouldShow = false;
                } else {
                    // Highlight UI content
                    item.section.addClass('ui-content-highlighted');
                }
            }

            // Apply visibility
            if (shouldShow) {
                item.section.removeClass('ui-filtered');
                visibleCount++;
            } else {
                item.section.addClass('ui-filtered');
            }
        });

        // Filter TOC items using same logic
        tocItems.forEach(item => {
            const tocV = parseVersion(item.version);
            let shouldShow = true;

            if (fromVersion !== 'all') {
                const fromV = parseVersion(fromVersion);
                if (compareVersions(tocV, fromV) < 0) {
                    shouldShow = false;
                }
            }

            if (toVersion !== 'all' && shouldShow) {
                const toV = parseVersion(toVersion);
                if (compareVersions(tocV, toV) > 0) {
                    shouldShow = false;
                }
            }

            // For UI filtering, also check if the linked section has UI content
            if (changeType === 'ui' && shouldShow) {
                const linkedSection = sections.find(s => s.id === item.id);
                if (!linkedSection || !linkedSection.hasUI) {
                    shouldShow = false;
                }
            }

            if (shouldShow) {
                item.item.removeClass('ui-filtered-toc');
            } else {
                item.item.addClass('ui-filtered-toc');
            }
        });

        // Status feedback
        let statusMessage = '';
        if (fromVersion === 'all' && toVersion === 'all') {
            if (changeType === 'ui') {
                statusMessage = `Showing UI changes (${visibleCount} of ${totalCount} sections)`;
            } else {
                statusMessage = `Showing all changes (${visibleCount} sections)`;
            }
        } else {
            const fromText = fromVersion === 'all' ? 'earliest' : `v${fromVersion}`;
            const toText = toVersion === 'all' ? 'latest' : `v${toVersion}`;
            const typeText = changeType === 'ui' ? ' UI changes' : '';
            statusMessage = `Showing${typeText} from ${fromText} to ${toText} (${visibleCount} of ${totalCount} sections)`;
        }

        $('.ui-changelog-filters').append(`<div class="ui-filter-status">${statusMessage}</div>`);

        // Show/hide clear filters button
        const hasFilters = fromVersion !== 'all' || toVersion !== 'all' || changeType !== 'all';
        $('#ui-changelog-clear-filter').toggle(hasFilters);

        // Scroll to first visible section if filters applied
        if (hasFilters && visibleCount > 0) {
            const firstVisible = sections.find(s => !s.section.hasClass('ui-filtered'));
            if (firstVisible) {
                $('html, body').animate({
                    scrollTop: firstVisible.section.offset().top - 100
                }, 500);
            }
        }
    }

    // Event handlers with auto-apply
    $('#ui-changelog-from-version, #ui-changelog-to-version, #ui-changelog-change-type').on('change', function (e) {
        // Prevent default navigation behavior for dropdowns
        e.preventDefault();
        applyFilters();
    });

    $('#ui-changelog-apply-filter').on('click', function (e) {
        e.preventDefault();
        applyFilters();
    });

    $('#ui-changelog-reset-filter').on('click', function (e) {
        e.preventDefault();
        $('#ui-changelog-from-version').val('all');
        $('#ui-changelog-to-version').val('all');
        $('#ui-changelog-change-type').val('all');
        
        // Clear filters
        $('.ui-filter-status, .ui-filter-error').remove();
        $('.ui-content-highlighted').removeClass('ui-content-highlighted');
        $('#ui-changelog-clear-filter').hide();
        
        sections.forEach(item => {
            item.section.removeClass('ui-filtered');
        });
        tocItems.forEach(item => {
            item.item.removeClass('ui-filtered-toc');
        });
    });

    $('#ui-changelog-clear-filter').on('click', function (e) {
        e.preventDefault();
        $('#ui-changelog-reset-filter').trigger('click');
    });

    // Keyboard accessibility
    $('.ui-filter-btn').on('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            $(this).trigger('click');
        }
    });
});
