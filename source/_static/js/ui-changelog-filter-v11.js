$(document).ready(function () {
    // Only run on the v11 changelog page
    if (!window.location.pathname.includes('mattermost-v11-changelog')) {
        return;
    }

    // UI detection keywords
    const UI_KEYWORDS = [
        'interface', 'ui', 'user interface', 'button', 'menu', 'dialog', 'modal', 'popup',
        'theme', 'styling', 'css', 'design', 'layout', 'visual', 'display', 'appearance',
        'icon', 'color', 'font', 'typography', 'accessibility', 'screen reader', 'aria',
        'hover', 'click', 'focus', 'navigation', 'sidebar', 'toolbar', 'dropdown',
        'autocomplete', 'picker', 'selector', 'form', 'input', 'checkbox', 'tooltip',
        'notification', 'banner', 'alert', 'loading', 'spinner', 'animation', 'transition'
    ];

    // Parse version utility function
    function parseVersion(version) {
        if (version === 'all') return { major: Infinity, minor: Infinity };
        const parts = version.split('.');
        return {
            major: parseInt(parts[0]) || 0,
            minor: parseInt(parts[1]) || 0
        };
    }

    // Sort versions in descending order
    function sortVersions(versions) {
        versions.sort((a, b) => {
            const aV = parseVersion(a);
            const bV = parseVersion(b);
            if (aV.major !== bV.major) return bV.major - aV.major;
            return bV.minor - aV.minor;
        });
    }

    // Check if content contains UI-related keywords
    function containsUIContent(text) {
        const lowerText = text.toLowerCase();
        return UI_KEYWORDS.some(keyword => lowerText.includes(keyword));
    }

    // Extract versions from section IDs
    const versions = [];
    const sections = [];
    const tocItems = [];

    // Find all release sections
    $('section[id^="release-v"]').each(function () {
        const sectionId = $(this).attr('id');
        const versionMatch = sectionId.match(/release-v(\d+)[.-](\d+)/);

        if (versionMatch) {
            const major = parseInt(versionMatch[1]);
            const minor = parseInt(versionMatch[2]);
            const version = `${major}.${minor}`;

            if (!versions.includes(version)) {
                versions.push(version);
            }

            sections.push({
                section: $(this),
                version: version,
                id: sectionId
            });
        }
    });

    // Find corresponding TOC items
    $('.toc-drawer li').each(function () {
        const $link = $(this).find('a').first();
        if ($link.length) {
            const href = $link.attr('href');
            if (href && href.includes('#')) {
                const sectionId = href.split('#')[1];
                const versionMatch = sectionId.match(/release-v(\d+)[.-](\d+)/);
                if (versionMatch) {
                    const major = parseInt(versionMatch[1]);
                    const minor = parseInt(versionMatch[2]);
                    const version = `${major}.${minor}`;

                    tocItems.push({
                        item: $(this),
                        version: version,
                        id: sectionId
                    });
                }
            }
        }
    });

    // Sort versions
    sortVersions(versions);

    // Create filter controls HTML
    const filterHTML = `
        <div class="ui-changelog-filters">
            <h3>Filter Changelog</h3>
            <p class="filter-description">Select version range and content type to view specific changelog entries</p>
            
            <div class="ui-filter-controls">
                <div class="ui-filter-group">
                    <label for="ui-from-version">From version:</label>
                    <select id="ui-from-version">
                        <option value="all">All versions</option>
                        ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                    </select>
                    <div class="ui-filter-helper">Starting version for filtering</div>
                </div>

                <div class="ui-filter-group">
                    <label for="ui-to-version">To version:</label>
                    <select id="ui-to-version">
                        <option value="all">Current version</option>
                        ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                    </select>
                    <div class="ui-filter-helper">Ending version for filtering</div>
                </div>

                <div class="ui-filter-group">
                    <label for="ui-change-type">Change type:</label>
                    <select id="ui-change-type">
                        <option value="all">All changes</option>
                        <option value="ui">UI changes only</option>
                    </select>
                </div>

                <div class="ui-filter-buttons">
                    <button id="ui-reset-filter" class="ui-filter-button secondary">Reset</button>
                </div>
            </div>

            <div id="ui-filter-status" class="ui-filter-status"></div>
            <div id="ui-filter-error" class="ui-filter-error"></div>
        </div>
    `;

    // Insert filter controls
    $('.content h1:first').after(filterHTML);

    // Apply filter function
    function applyFilter() {
        const fromVersion = $('#ui-from-version').val();
        const toVersion = $('#ui-to-version').val();
        const changeType = $('#ui-change-type').val();

        // Clear previous messages
        $('#ui-filter-status, #ui-filter-error').hide().text('');

        // Validate version range
        if (fromVersion !== 'all' && toVersion !== 'all') {
            const fromV = parseVersion(fromVersion);
            const toV = parseVersion(toVersion);

            if (toV.major < fromV.major || (toV.major === fromV.major && toV.minor < fromV.minor)) {
                $('#ui-filter-error').text('Error: "To version" must be greater than or equal to "From version".').show();
                return;
            }
        }

        let visibleSections = 0;
        let totalSections = sections.length;

        // Filter sections
        sections.forEach(item => {
            const sectionV = parseVersion(item.version);
            const sectionText = item.section.text();

            // Check version range
            const inVersionRange = (
                (fromVersion === 'all' || 
                    (sectionV.major > parseVersion(fromVersion).major ||
                    (sectionV.major === parseVersion(fromVersion).major && sectionV.minor >= parseVersion(fromVersion).minor))) &&
                (toVersion === 'all' ||
                    (sectionV.major < parseVersion(toVersion).major ||
                    (sectionV.major === parseVersion(toVersion).major && sectionV.minor <= parseVersion(toVersion).minor)))
            );

            // Check UI content if filtering for UI changes
            const isUIContent = changeType === 'all' || containsUIContent(sectionText);

            const shouldShow = inVersionRange && isUIContent;

            if (shouldShow) {
                item.section.removeClass('ui-filtered');
                visibleSections++;

                // Highlight UI content if filtering for UI changes
                if (changeType === 'ui') {
                    item.section.addClass('ui-content-highlighted');
                } else {
                    item.section.removeClass('ui-content-highlighted');
                }
            } else {
                item.section.addClass('ui-filtered');
                item.section.removeClass('ui-content-highlighted');
            }
        });

        // Filter TOC items
        tocItems.forEach(item => {
            const tocV = parseVersion(item.version);

            const inVersionRange = (
                (fromVersion === 'all' || 
                    (tocV.major > parseVersion(fromVersion).major ||
                    (tocV.major === parseVersion(fromVersion).major && tocV.minor >= parseVersion(fromVersion).minor))) &&
                (toVersion === 'all' ||
                    (tocV.major < parseVersion(toVersion).major ||
                    (tocV.major === parseVersion(toVersion).major && tocV.minor <= parseVersion(toVersion).minor)))
            );

            // For TOC, we need to check if the corresponding section has UI content
            const correspondingSection = sections.find(s => s.version === item.version);
            const isUIContent = changeType === 'all' || 
                (correspondingSection && containsUIContent(correspondingSection.section.text()));

            const shouldShow = inVersionRange && isUIContent;

            if (shouldShow) {
                item.item.removeClass('ui-filtered-toc');
            } else {
                item.item.addClass('ui-filtered-toc');
            }
        });

        // Show status
        let statusMessage = '';
        if (fromVersion !== 'all' || toVersion !== 'all' || changeType !== 'all') {
            statusMessage = `Showing ${visibleSections} of ${totalSections} sections`;
            
            if (changeType === 'ui') {
                statusMessage += ' (UI changes only)';
            }
            
            if (fromVersion !== 'all' && toVersion !== 'all') {
                statusMessage += ` from v${fromVersion} to v${toVersion}`;
            } else if (fromVersion !== 'all') {
                statusMessage += ` from v${fromVersion}`;
            } else if (toVersion !== 'all') {
                statusMessage += ` to v${toVersion}`;
            }

            $('#ui-filter-status').text(statusMessage).show();

            // Scroll to first visible section if UI filtering is active
            if (changeType === 'ui' && visibleSections > 0) {
                setTimeout(() => {
                    const firstVisible = sections.find(item => !item.section.hasClass('ui-filtered'));
                    if (firstVisible) {
                        $('html, body').animate({
                            scrollTop: firstVisible.section.offset().top - 100
                        }, 500);
                    }
                }, 100);
            }
        }
    }

    // Auto-apply on dropdown change
    $('#ui-from-version, #ui-to-version, #ui-change-type').on('change', function(e) {
        e.preventDefault();
        applyFilter();
    });

    // Reset filters
    $('#ui-reset-filter').on('click', function(e) {
        e.preventDefault();
        $('#ui-from-version, #ui-to-version, #ui-change-type').val('all');
        
        sections.forEach(item => {
            item.section.removeClass('ui-filtered ui-content-highlighted');
        });
        
        tocItems.forEach(item => {
            item.item.removeClass('ui-filtered-toc');
        });
        
        $('#ui-filter-status, #ui-filter-error').hide().text('');
    });

    // Handle mutual exclusion for change type
    $('#ui-change-type').on('change', function() {
        const value = $(this).val();
        
        if (value === 'ui') {
            // When UI changes is selected, highlight that this filters content
            $('#ui-filter-status').text('Filtering for UI-related content...').show();
        }
    });
});