$(document).ready(function () {
    // Only run on the unsupported legacy releases page
    if (!window.location.pathname.includes('/unsupported-legacy-releases')) {
        return;
    }

    // Extract versions from table rows
    const versions = [];
    const rows = [];
    let lastVersion = null;

    $('table.docutils tr').each(function (index) {
        if (index === 0) return; // Skip header row

        const cells = $(this).find('td');
        if (cells.length > 1) {
            const firstCell = cells.first();
            const versionText = firstCell.text().trim();
            const versionMatch = versionText.match(/v(\d+\.\d+)/);

            if (versionMatch) {
                const version = versionMatch[1];
                if (!versions.includes(version)) {
                    versions.push(version);
                }
                lastVersion = version;

                rows.push({
                    row: $(this),
                    version: version
                });
                return;
            }
        }
        
        // This is a continuation row for the last version
        if (lastVersion) {
            rows.push({
                row: $(this),
                version: lastVersion
            });
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
            <p class="filter-description">Filter legacy release notes by version range and content type</p>
            
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

    // Insert filter controls above the table
    $('table.docutils').first().before(filterHTML);

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
        
        statusMsg += ` (${visibleCount} of ${totalCount} entries)`;
        
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
        const totalCount = rows.length;

        // Filter rows
        rows.forEach(item => {
            const rowV = parseVersion(item.version);
            const fromV = parseVersion(fromVersion);
            const toV = parseVersion(toVersion);

            // Version range check
            const inVersionRange = (
                (fromVersion === 'all' || 
                 rowV.major > fromV.major || 
                 (rowV.major === fromV.major && rowV.minor >= fromV.minor)) &&
                (toVersion === 'all' || 
                 rowV.major < toV.major || 
                 (rowV.major === toV.major && rowV.minor <= toV.minor))
            );

            if (!inVersionRange) {
                item.row.addClass('ui-filtered');
                return;
            }

            // Content type check
            if (changeType === 'ui') {
                const rowText = item.row.text();
                const hasUIContent = containsUIContent(rowText);
                
                if (hasUIContent) {
                    item.row.removeClass('ui-filtered').addClass('ui-item-highlighted');
                    visibleCount++;
                } else {
                    item.row.addClass('ui-filtered');
                }
            } else {
                item.row.removeClass('ui-filtered');
                visibleCount++;
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
        rows.forEach(item => {
            item.row.removeClass('ui-filtered ui-item-highlighted');
        });
        
        // Hide status
        $('#ui-filter-status').hide().removeClass('has-filters');
        
        // Remove any error messages
        $('.ui-changelog-error').remove();
    });

    // Initialize with no filters applied
    rows.forEach(item => {
        item.row.attr('data-version', item.version);
    });

    // CSS for table row filtering
    if (!document.getElementById('ui-table-filter-styles')) {
        const style = document.createElement('style');
        style.id = 'ui-table-filter-styles';
        style.textContent = `
            .docutils tr.ui-filtered {
                display: none;
            }
            .docutils tr.ui-item-highlighted td {
                background: linear-gradient(90deg, rgba(22, 109, 224, 0.05) 0%, rgba(22, 109, 224, 0.02) 100%);
                border-left: 3px solid #166de0;
                padding-left: 12px;
            }
            [data-custom-theme="dark"] .docutils tr.ui-item-highlighted td {
                background: linear-gradient(90deg, rgba(52, 152, 219, 0.1) 0%, rgba(52, 152, 219, 0.05) 100%);
                border-left-color: #3498db;
            }
        `;
        document.head.appendChild(style);
    }
});