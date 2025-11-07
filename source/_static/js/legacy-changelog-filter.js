$(document).ready(function () {
    // Only run on the unsupported legacy releases page
    if (!window.location.pathname.includes('/unsupported-legacy-releases')) {
        return;
    }

    // Extract versions from section IDs for legacy releases format
    const versions = [];
    const sections = [];
    const tocItems = [];
    let uiKeywords = [
        'user interface', 'ui', 'theme', 'sidebar', 'channel header', 'message', 'modal', 'button',
        'dropdown', 'menu', 'navigation', 'accessibility', 'responsive', 'mobile', 'desktop',
        'emoji', 'reaction', 'autocomplete', 'search', 'filter', 'notification', 'badge',
        'tooltip', 'hover', 'click', 'scroll', 'layout', 'design', 'visual', 'style',
        'color', 'font', 'icon', 'image', 'avatar', 'profile', 'status', 'presence',
        'dark mode', 'light mode', 'contrast', 'display', 'view', 'panel', 'tab',
        'checkbox', 'input', 'form', 'dialog', 'popup', 'overlay', 'loading', 'spinner',
        'banner', 'header', 'footer', 'toolbar', 'shortcut', 'keyboard', 'mouse',
        'touch', 'gesture', 'animation', 'transition', 'focus', 'blur', 'highlight'
    ];

    // Find all release sections based on the legacy releases heading pattern
    $('section[id^="release-v"]').each(function () {
        const sectionId = $(this).attr('id');
        const versionMatch = sectionId.match(/release-v(\d+)[\.-](\d+)/);

        if (versionMatch) {
            // Format: major.minor
            const major = parseInt(versionMatch[1]);
            const minor = parseInt(versionMatch[2]);
            const version = `${major}.${minor}`;

            if (!versions.includes(version)) {
                versions.push(version);
            }

            // Associate section with version
            sections.push({
                section: $(this),
                version: version,
                id: sectionId,
                major: major,
                minor: minor
            });
        }
    });

    // Find corresponding TOC items in the sidebar
    $('.toc-drawer li').each(function () {
        const $link = $(this).find('a').first();
        if ($link.length) {
            const href = $link.attr('href');
            if (href && href.includes('#')) {
                const sectionId = href.split('#')[1];
                // Check if this links to a legacy version section
                const versionMatch = sectionId.match(/release-v(\d+)[\.-](\d+)/);
                if (versionMatch) {
                    const major = parseInt(versionMatch[1]);
                    const minor = parseInt(versionMatch[2]);
                    const version = `${major}.${minor}`;

                    // This TOC item links to a version section
                    tocItems.push({
                        item: $(this),
                        version: version,
                        id: sectionId,
                        major: major,
                        minor: minor
                    });
                }
            }
        }
    });

    // Sort versions in descending order (newest first) with proper semantic versioning
    versions.sort((a, b) => {
        const [aMajor, aMinor] = a.split('.').map(Number);
        const [bMajor, bMinor] = b.split('.').map(Number);
        if (aMajor !== bMajor) return bMajor - aMajor;
        return bMinor - aMinor;
    });

    // Create enhanced filter controls matching the mockup design for legacy releases
    const filterHTML = `
        <div class="ui-changelog-filters" role="region" aria-label="Legacy Changelog Filters">
            <h3>Filter Legacy Releases</h3>
            <p class="help-text">Filter legacy releases (v9.x, v8.x, v7.x) by version range and change types</p>
            
            <div class="filter-row">
                <div class="filter-group">
                    <label for="legacy-changelog-from-version">From version:</label>
                    <select id="legacy-changelog-from-version" aria-describedby="from-version-help">
                        <option value="all">All versions</option>
                        ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                    </select>
                </div>
                
                <div class="filter-group">
                    <label for="legacy-changelog-to-version">To version:</label>
                    <select id="legacy-changelog-to-version" aria-describedby="to-version-help">
                        <option value="all">All versions</option>
                        ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                    </select>
                </div>
            </div>
            
            <div class="filter-row">
                <div class="checkbox-group" role="group" aria-labelledby="change-type-label">
                    <span id="change-type-label" class="sr-only">Change Types</span>
                    <div class="checkbox-item">
                        <input type="checkbox" id="legacy-show-all-changes" checked aria-describedby="all-changes-help">
                        <label for="legacy-show-all-changes">All changes</label>
                    </div>
                    <div class="checkbox-item">
                        <input type="checkbox" id="legacy-show-ui-changes" aria-describedby="ui-changes-help">
                        <label for="legacy-show-ui-changes">UI changes only</label>
                    </div>
                </div>
            </div>
            
            <div class="filter-buttons">
                <button id="legacy-changelog-apply-filter" class="btn-primary" type="button" aria-describedby="apply-help">
                    Apply Filters
                </button>
                <button id="legacy-changelog-reset-filter" class="btn-secondary" type="button" aria-describedby="reset-help">
                    Reset
                </button>
            </div>
            
            <div id="legacy-filter-status" class="filter-status" role="status" aria-live="polite"></div>
            <div id="legacy-filter-error" class="filter-error" role="alert" aria-live="assertive"></div>
            
            <!-- Screen reader helper text -->
            <div class="sr-only">
                <div id="from-version-help">Select the earliest legacy version to include in the filter</div>
                <div id="to-version-help">Select the latest legacy version to include in the filter</div>
                <div id="all-changes-help">Show all types of changes</div>
                <div id="ui-changes-help">Show only user interface related changes</div>
                <div id="apply-help">Apply the selected filters to the legacy changelog</div>
                <div id="reset-help">Clear all filters and show all legacy content</div>
            </div>
        </div>
    `;

    // Insert filter controls above the content
    $('.content h1:first').after(filterHTML);

    // Add data attributes to sections for easier filtering
    sections.forEach(item => {
        item.section.attr('data-version', item.version);
        item.section.attr('data-major', item.major);
        item.section.attr('data-minor', item.minor);
    });

    // Detect UI-related content
    function detectUIContent(element) {
        const text = element.text().toLowerCase();
        return uiKeywords.some(keyword => text.includes(keyword));
    }

    // Highlight UI sections
    function highlightUISections(highlight = false) {
        $('.ui-item-highlighted, .ui-section-highlighted').removeClass('ui-item-highlighted ui-section-highlighted');
        
        if (!highlight) return;
        
        sections.forEach(item => {
            const section = item.section;
            const uiSection = section.find('h4:contains("User Interface (UI)")').closest('div, section');
            
            if (uiSection.length) {
                uiSection.addClass('ui-section-highlighted');
                uiSection.find('li, p, div').each(function() {
                    if (detectUIContent($(this))) {
                        $(this).addClass('ui-item-highlighted');
                    }
                });
            }
        });
    }

    // Update filter status
    function updateFilterStatus(fromVersion, toVersion, showAll, showUI) {
        const statusEl = $('#legacy-filter-status');
        const errorEl = $('#legacy-filter-error');
        
        // Clear previous states
        statusEl.removeClass('active').text('');
        errorEl.removeClass('active').text('');
        
        if (fromVersion === 'all' && toVersion === 'all' && showAll && !showUI) {
            statusEl.text('Showing all legacy changelog entries').addClass('active');
            return;
        }
        
        let statusText = 'Showing ';
        
        if (fromVersion !== 'all' || toVersion !== 'all') {
            if (fromVersion !== 'all' && toVersion !== 'all') {
                statusText += `v${fromVersion} → v${toVersion}`;
            } else if (fromVersion !== 'all') {
                statusText += `v${fromVersion} and newer`;
            } else {
                statusText += `up to v${toVersion}`;
            }
        } else {
            statusText += 'all legacy versions';
        }
        
        if (showUI && !showAll) {
            statusText += ' (UI changes only)';
        } else if (showAll && showUI) {
            statusText += ' (all changes + UI highlighting)';
        }
        
        statusEl.text(statusText).addClass('active');
    }

    // Parse version for comparison
    function parseVersion(versionStr) {
        if (versionStr === 'all') return { major: Infinity, minor: Infinity };
        const [major, minor] = versionStr.split('.').map(Number);
        return { major, minor };
    }

    // Checkbox mutual exclusion logic
    $('#legacy-show-all-changes, #legacy-show-ui-changes').on('change', function() {
        if ($(this).is(':checked')) {
            if ($(this).attr('id') === 'legacy-show-all-changes') {
                $('#legacy-show-ui-changes').prop('checked', false);
            } else {
                $('#legacy-show-all-changes').prop('checked', false);
            }
        } else {
            // Ensure at least one is always checked
            if (!$('#legacy-show-all-changes').is(':checked') && !$('#legacy-show-ui-changes').is(':checked')) {
                $('#legacy-show-all-changes').prop('checked', true);
            }
        }
    });

    // Apply filter function
    $('#legacy-changelog-apply-filter').on('click', function () {
        const fromVersion = $('#legacy-changelog-from-version').val();
        const toVersion = $('#legacy-changelog-to-version').val();
        const showAllChanges = $('#legacy-show-all-changes').is(':checked');
        const showUIChanges = $('#legacy-show-ui-changes').is(':checked');
        
        const errorEl = $('#legacy-filter-error');
        errorEl.removeClass('active').text('');

        // Validate version range
        if (fromVersion !== 'all' && toVersion !== 'all') {
            const fromV = parseVersion(fromVersion);
            const toV = parseVersion(toVersion);
            
            if (fromV.major > toV.major || 
                (fromV.major === toV.major && fromV.minor > toV.minor)) {
                errorEl.text('Error: "To version" must be greater than or equal to "From version".')
                       .addClass('active');
                return;
            }
        }

        // Filter sections
        sections.forEach(item => {
            const sectionV = { major: item.major, minor: item.minor };
            let showSection = true;

            // Version range filtering
            if (fromVersion !== 'all') {
                const fromV = parseVersion(fromVersion);
                if (sectionV.major < fromV.major || 
                    (sectionV.major === fromV.major && sectionV.minor < fromV.minor)) {
                    showSection = false;
                }
            }

            if (toVersion !== 'all' && showSection) {
                const toV = parseVersion(toVersion);
                if (sectionV.major > toV.major || 
                    (sectionV.major === toV.major && sectionV.minor > toV.minor)) {
                    showSection = false;
                }
            }

            // Change type filtering
            if (showUIChanges && !showAllChanges) {
                // Show only sections with UI content
                const hasUIContent = item.section.find('h4:contains("User Interface (UI)")').length > 0 ||
                                   detectUIContent(item.section);
                if (!hasUIContent) {
                    showSection = false;
                }
            }

            // Apply visibility
            if (showSection) {
                item.section.removeClass('ui-filtered');
            } else {
                item.section.addClass('ui-filtered');
            }
        });

        // Apply same filtering to TOC items
        tocItems.forEach(item => {
            const tocV = { major: item.major, minor: item.minor };
            let showTocItem = true;

            if (fromVersion !== 'all') {
                const fromV = parseVersion(fromVersion);
                if (tocV.major < fromV.major || 
                    (tocV.major === tocV.major && tocV.minor < fromV.minor)) {
                    showTocItem = false;
                }
            }

            if (toVersion !== 'all' && showTocItem) {
                const toV = parseVersion(toVersion);
                if (tocV.major > toV.major || 
                    (tocV.major === tocV.major && tocV.minor > toV.minor)) {
                    showTocItem = false;
                }
            }

            if (showTocItem) {
                item.item.removeClass('ui-filtered-toc');
            } else {
                item.item.addClass('ui-filtered-toc');
            }
        });

        // Handle UI highlighting
        highlightUISections(showUIChanges);

        // Update status
        updateFilterStatus(fromVersion, toVersion, showAllChanges, showUIChanges);

        // Scroll to first visible section for better UX
        const firstVisible = sections.find(item => !item.section.hasClass('ui-filtered'));
        if (firstVisible) {
            setTimeout(() => {
                firstVisible.section[0].scrollIntoView({ 
                    behavior: 'smooth', 
                    block: 'start' 
                });
            }, 100);
        }
    });

    // Reset filters
    $('#legacy-changelog-reset-filter').on('click', function () {
        $('#legacy-changelog-from-version, #legacy-changelog-to-version').val('all');
        $('#legacy-show-all-changes').prop('checked', true);
        $('#legacy-show-ui-changes').prop('checked', false);
        
        sections.forEach(item => {
            item.section.removeClass('ui-filtered');
        });
        
        tocItems.forEach(item => {
            item.item.removeClass('ui-filtered-toc');
        });

        highlightUISections(false);
        
        $('#legacy-filter-status, #legacy-filter-error').removeClass('active').text('');
        
        // Return to top of content
        setTimeout(() => {
            $('.ui-changelog-filters')[0].scrollIntoView({ 
                behavior: 'smooth', 
                block: 'start' 
            });
        }, 100);
    });

    // Auto-apply on dropdown change for immediate feedback
    $('#legacy-changelog-from-version, #legacy-changelog-to-version').on('change', function() {
        $('#legacy-changelog-apply-filter').click();
    });

    // Initialize with default state
    updateFilterStatus('all', 'all', true, false);
});