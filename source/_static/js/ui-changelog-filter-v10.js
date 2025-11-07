$(document).ready(function () {
    // Only run on the v10 changelog page
    if (!window.location.pathname.includes('/mattermost-v10-changelog')) {
        return;
    }

    // Extract versions from section IDs
    const versions = [];
    const sections = [];
    const tocItems = [];

    // Find all release sections
    $('section[id^="release-v"]').each(function () {
        const sectionId = $(this).attr('id');
        const versionMatch = sectionId.match(/release-v(\d+)-(\d+)/);

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
                const versionMatch = sectionId.match(/release-v(\d+)-(\d+)/);
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

    // Sort versions (newest first)
    versions.sort((a, b) => {
        const [aMajor, aMinor] = a.split('.').map(n => parseInt(n));
        const [bMajor, bMinor] = b.split('.').map(n => parseInt(n));
        
        if (bMajor !== aMajor) return bMajor - aMajor;
        return bMinor - aMinor;
    });

    // UI detection keywords
    const uiKeywords = [
        'ui', 'user interface', 'interface', 'design', 'layout', 'theme', 'styling', 'css',
        'button', 'menu', 'dialog', 'modal', 'popup', 'dropdown', 'sidebar', 'navigation',
        'header', 'footer', 'banner', 'tooltip', 'icon', 'visual', 'display', 'view',
        'appearance', 'look', 'feel', 'color', 'font', 'text', 'formatting', 'responsive',
        'mobile', 'desktop', 'tablet', 'screen', 'resize', 'scroll', 'hover', 'focus',
        'click', 'tap', 'gesture', 'accessibility', 'a11y', 'keyboard', 'screen reader'
    ];

    // Create filter controls HTML
    const filterHTML = `
        <div class="ui-changelog-filters">
            <h3>Filters</h3>
            <p class="filter-description">Filter changelog entries by version range and content type</p>
            
            <div class="filter-controls">
                <div class="filter-group">
                    <label for="ui-from-version">From version:</label>
                    <select id="ui-from-version">
                        <option value="all">All versions</option>
                        ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                    </select>
                    <small style="color: #6c757d; font-size: 0.8em;">Choose the earliest version to include</small>
                </div>
                
                <div class="filter-group">
                    <label for="ui-to-version">To version:</label>
                    <select id="ui-to-version">
                        <option value="all">All versions</option>
                        ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                    </select>
                    <small style="color: #6c757d; font-size: 0.8em;">Choose the latest version to include</small>
                </div>
                
                <div class="filter-group">
                    <label for="ui-change-type">Change type:</label>
                    <select id="ui-change-type">
                        <option value="all">All changes</option>
                        <option value="ui">UI changes only</option>
                    </select>
                    <small style="color: #6c757d; font-size: 0.8em;">Filter by content type</small>
                </div>
                
                <div class="button-group">
                    <button type="button" class="btn-primary" id="ui-apply-filter">Apply</button>
                    <button type="button" class="btn-secondary" id="ui-reset-filter">Reset</button>
                </div>
                
                <a href="#" class="clear-link" id="ui-clear-filters">✕ Clear filters</a>
            </div>
            
            <div id="ui-filter-status" class="ui-changelog-status" style="display: none;"></div>
        </div>
    `;

    // Insert filter controls
    $('.content h1:first').after(filterHTML);

    // Helper function to parse version
    function parseVersion(versionStr) {
        if (versionStr === 'all') return { major: Infinity, minor: Infinity };
        const [major, minor] = versionStr.split('.').map(n => parseInt(n));
        return { major, minor };
    }

    // Helper function to check if content contains UI-related terms
    function containsUIContent(text) {
        const lowerText = text.toLowerCase();
        return uiKeywords.some(keyword => lowerText.includes(keyword));
    }

    // Helper function to update status message
    function updateStatus(fromVersion, toVersion, changeType, visibleCount, totalCount) {
        const statusEl = $('#ui-filter-status');
        
        if (fromVersion === 'all' && toVersion === 'all' && changeType === 'all') {
            statusEl.hide();
            return;
        }

        let statusMsg = 'Showing ';
        
        if (changeType === 'ui') {
            statusMsg += 'UI changes ';
        } else {
            statusMsg += 'all changes ';
        }
        
        if (fromVersion !== 'all' || toVersion !== 'all') {
            statusMsg += 'from ';
            statusMsg += fromVersion === 'all' ? 'earliest' : `v${fromVersion}`;
            statusMsg += ' to ';
            statusMsg += toVersion === 'all' ? 'latest' : `v${toVersion}`;
        }
        
        statusMsg += ` (${visibleCount} of ${totalCount} sections)`;
        
        statusEl.text(statusMsg).addClass('has-filters').show();
    }

    // Auto-apply function (no scrolling)
    function applyFilters() {
        const fromVersion = $('#ui-from-version').val();
        const toVersion = $('#ui-to-version').val();
        const changeType = $('#ui-change-type').val();

        // Clear previous error messages
        $('.ui-changelog-error').remove();

        // Version validation
        if (fromVersion !== 'all' && toVersion !== 'all') {
            const fromV = parseVersion(fromVersion);
            const toV = parseVersion(toVersion);
            
            if (toV.major < fromV.major || (toV.major === fromV.major && toV.minor < fromV.minor)) {
                $('.ui-changelog-filters').append(
                    '<div class="ui-changelog-error">Error: "To version" must be greater than or equal to "From version".</div>'
                );
                return;
            }
        }

        // Clear previous highlighting
        $('.ui-item-highlighted').removeClass('ui-item-highlighted');
        
        let visibleCount = 0;
        const totalCount = sections.length;

        // Filter sections
        sections.forEach(item => {
            const sectionV = parseVersion(item.version);
            const fromV = parseVersion(fromVersion);
            const toV = parseVersion(toVersion);

            // Version range check
            const inVersionRange = (
                (fromVersion === 'all' || 
                 sectionV.major > fromV.major || 
                 (sectionV.major === fromV.major && sectionV.minor >= fromV.minor)) &&
                (toVersion === 'all' || 
                 sectionV.major < toV.major || 
                 (sectionV.major === toV.major && sectionV.minor <= toV.minor))
            );

            if (!inVersionRange) {
                item.section.addClass('ui-filtered');
                return;
            }

            // Content type check
            if (changeType === 'ui') {
                const sectionText = item.section.text();
                const hasUIContent = containsUIContent(sectionText);
                
                if (hasUIContent) {
                    item.section.removeClass('ui-filtered').addClass('ui-item-highlighted');
                    visibleCount++;
                } else {
                    item.section.addClass('ui-filtered');
                }
            } else {
                item.section.removeClass('ui-filtered');
                visibleCount++;
            }
        });

        // Filter TOC items
        tocItems.forEach(item => {
            const tocV = parseVersion(item.version);
            const fromV = parseVersion(fromVersion);
            const toV = parseVersion(toVersion);

            const inVersionRange = (
                (fromVersion === 'all' || 
                 tocV.major > fromV.major || 
                 (tocV.major === tocV.major && tocV.minor >= fromV.minor)) &&
                (toVersion === 'all' || 
                 tocV.major < toV.major || 
                 (tocV.major === toV.major && tocV.minor <= toV.minor))
            );

            if (!inVersionRange) {
                item.item.addClass('ui-filtered-toc');
            } else {
                // For UI filtering, check if the corresponding section is visible
                if (changeType === 'ui') {
                    const correspondingSection = sections.find(s => s.version === item.version);
                    if (correspondingSection && correspondingSection.section.hasClass('ui-filtered')) {
                        item.item.addClass('ui-filtered-toc');
                    } else {
                        item.item.removeClass('ui-filtered-toc');
                    }
                } else {
                    item.item.removeClass('ui-filtered-toc');
                }
            }
        });

        // Update status message
        updateStatus(fromVersion, toVersion, changeType, visibleCount, totalCount);
    }

    // Event handlers with auto-apply (NO SCROLLING)
    $('#ui-from-version, #ui-to-version, #ui-change-type').on('change', function(e) {
        e.preventDefault(); // Prevent any default behavior that might cause scrolling
        applyFilters();
    });

    $('#ui-apply-filter').on('click', function(e) {
        e.preventDefault();
        applyFilters();
    });

    $('#ui-reset-filter, #ui-clear-filters').on('click', function(e) {
        e.preventDefault();
        
        // Reset all form controls
        $('#ui-from-version, #ui-to-version').val('all');
        $('#ui-change-type').val('all');
        
        // Show all content
        sections.forEach(item => {
            item.section.removeClass('ui-filtered ui-item-highlighted');
        });
        
        tocItems.forEach(item => {
            item.item.removeClass('ui-filtered-toc');
        });
        
        // Hide status
        $('#ui-filter-status').hide().removeClass('has-filters');
        
        // Remove any error messages
        $('.ui-changelog-error').remove();
    });

    // Initialize with no filters applied
    sections.forEach(item => {
        item.section.attr('data-version', item.version);
    });
});