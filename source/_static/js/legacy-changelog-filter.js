$(document).ready(function () {
    // Only run on the legacy releases page
    if (!window.location.pathname.includes('/product-overview/unsupported-legacy-releases')) {
        return;
    }

    // Extract versions and UI items from the legacy changelog
    const versions = [];
    const sections = [];
    const tocItems = [];
    const uiItems = [];

    // Find all release sections for legacy versions (v9, v8, v7, etc.)
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

            // Find UI items within this section
            const uiSection = $(this).find('h4:contains("User Interface"), h4:contains("UI")').next();
            const hasUIContent = uiSection.length > 0 || 
                                $(this).find('li:contains("Pre-packaged"), li:contains("UI"), li:contains("User Interface")').length > 0;

            sections.push({
                section: $(this),
                version: version,
                id: sectionId,
                hasUI: hasUIContent
            });

            // Extract specific UI-related items for legacy versions
            $(this).find('li').each(function() {
                const text = $(this).text().toLowerCase();
                if (text.includes('ui') || 
                    text.includes('user interface') || 
                    text.includes('pre-packaged') ||
                    text.includes('theme') ||
                    text.includes('styling') ||
                    text.includes('visual') ||
                    text.includes('display') ||
                    text.includes('appearance') ||
                    text.includes('plugin') ||
                    text.includes('boards') ||
                    text.includes('playbooks')) {
                    uiItems.push({
                        item: $(this),
                        version: version,
                        text: $(this).text()
                    });
                }
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

    // Sort versions in descending order
    sortVersions(versions);

    // Create the filter UI for legacy releases
    const filterHTML = `
        <div class="ui-changelog-filters">
            <div class="ui-changelog-filters-title">
                <h3>Filter Legacy Releases</h3>
                <a href="#" class="ui-clear-filters" id="legacy-clear-filters" style="display: none;">Clear filters</a>
            </div>
            
            <div class="ui-filter-bar">
                <div class="ui-filter-group">
                    <label class="ui-filter-label" for="legacy-from-version">From version:</label>
                    <select id="legacy-from-version" class="ui-version-select" aria-label="Select starting version">
                        <option value="all">All versions</option>
                        ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                    </select>
                    <small style="color: #6c757d; font-size: 12px;">Choose the earliest legacy version to include</small>
                </div>

                <div class="ui-filter-group">
                    <label class="ui-filter-label" for="legacy-to-version">To version:</label>
                    <select id="legacy-to-version" class="ui-version-select" aria-label="Select ending version">
                        <option value="all">All versions</option>
                        ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                    </select>
                    <small style="color: #6c757d; font-size: 12px;">Choose the latest legacy version to include</small>
                </div>

                <div class="ui-filter-group">
                    <label class="ui-filter-label" for="legacy-change-type">Change type:</label>
                    <select id="legacy-change-type" class="ui-change-type-select" aria-label="Select change type">
                        <option value="all">All changes</option>
                        <option value="ui">UI changes only</option>
                    </select>
                </div>

                <div class="ui-filter-actions">
                    <button id="legacy-apply-filter" class="ui-btn-primary">Apply</button>
                    <button id="legacy-reset-filter" class="ui-btn-secondary">Reset</button>
                </div>
            </div>

            <div id="legacy-filter-status" class="ui-filter-status"></div>
        </div>
    `;

    // Insert filter controls after the h1 title
    $('.content h1:first').after(filterHTML);

    // Add data attributes to sections for easier filtering
    sections.forEach(item => {
        item.section.attr('data-version', item.version);
        item.section.attr('data-has-ui', item.hasUI);
    });

    // Add data attributes to UI items
    uiItems.forEach(item => {
        item.item.attr('data-ui-item', 'true');
        item.item.attr('data-version', item.version);
    });

    // State management
    let currentFilters = {
        fromVersion: 'all',
        toVersion: 'all',
        changeType: 'all'
    };

    // Update status display
    function updateStatus() {
        const $status = $('#legacy-filter-status');
        const $clearFilters = $('#legacy-clear-filters');
        
        if (currentFilters.fromVersion === 'all' && 
            currentFilters.toVersion === 'all' && 
            currentFilters.changeType === 'all') {
            $status.removeClass('active error').hide();
            $clearFilters.hide();
            return;
        }

        $clearFilters.show();
        
        let statusText = 'Showing ';
        
        if (currentFilters.changeType === 'ui') {
            statusText += 'UI changes ';
        } else {
            statusText += 'all changes ';
        }
        
        if (currentFilters.fromVersion !== 'all' && currentFilters.toVersion !== 'all') {
            statusText += `from v${currentFilters.fromVersion} to v${currentFilters.toVersion}`;
        } else if (currentFilters.fromVersion !== 'all') {
            statusText += `from v${currentFilters.fromVersion}`;
        } else if (currentFilters.toVersion !== 'all') {
            statusText += `up to v${currentFilters.toVersion}`;
        }
        
        statusText += ' (legacy releases)';
        
        $status.removeClass('error').addClass('active').text(statusText).show();
    }

    // Show error message
    function showError(message) {
        const $status = $('#legacy-filter-status');
        $status.removeClass('active').addClass('error').text(message).show();
    }

    // Apply filtering logic
    function applyFilters() {
        const { fromVersion, toVersion, changeType } = currentFilters;

        // Clear any previous error messages
        $('#legacy-filter-status').removeClass('error');

        // Validate version range
        if (fromVersion !== 'all' && toVersion !== 'all') {
            const fromV = parseVersion(fromVersion);
            const toV = parseVersion(toVersion);
            
            if (toV.major < fromV.major || 
                (toV.major === fromV.major && toV.minor < fromV.minor)) {
                showError('Error: "To version" must be greater than or equal to "From version".');
                return;
            }
        }

        let visibleSections = 0;
        let visibleUIItems = 0;

        // Filter sections
        sections.forEach(item => {
            const sectionV = parseVersion(item.version);
            
            // Check version range
            let inVersionRange = true;
            if (fromVersion !== 'all') {
                const fromV = parseVersion(fromVersion);
                inVersionRange = inVersionRange && (
                    sectionV.major > fromV.major ||
                    (sectionV.major === fromV.major && sectionV.minor >= fromV.minor)
                );
            }
            if (toVersion !== 'all') {
                const toV = parseVersion(toVersion);
                inVersionRange = inVersionRange && (
                    sectionV.major < toV.major ||
                    (sectionV.major === toV.major && sectionV.minor <= toV.minor)
                );
            }

            // Check change type filter
            let matchesChangeType = true;
            if (changeType === 'ui') {
                matchesChangeType = item.hasUI;
            }

            const shouldShow = inVersionRange && matchesChangeType;

            if (shouldShow) {
                item.section.removeClass('ui-filtered');
                visibleSections++;
                
                // If filtering for UI only, highlight UI items
                if (changeType === 'ui') {
                    item.section.find('li[data-ui-item="true"]').each(function() {
                        $(this).addClass('ui-highlight');
                        visibleUIItems++;
                    });
                } else {
                    item.section.find('li').removeClass('ui-highlight');
                }
            } else {
                item.section.addClass('ui-filtered');
            }
        });

        // Filter TOC items
        tocItems.forEach(item => {
            const tocV = parseVersion(item.version);
            
            let inVersionRange = true;
            if (fromVersion !== 'all') {
                const fromV = parseVersion(fromVersion);
                inVersionRange = inVersionRange && (
                    tocV.major > fromV.major ||
                    (tocV.major === fromV.major && tocV.minor >= fromV.minor)
                );
            }
            if (toVersion !== 'all') {
                const toV = parseVersion(toVersion);
                inVersionRange = inVersionRange && (
                    tocV.major < toV.major ||
                    (tocV.major === toV.major && tocV.minor <= toV.minor)
                );
            }

            // For TOC, we show the item if the section would be visible
            const correspondingSection = sections.find(s => s.id === item.id);
            const matchesChangeType = changeType === 'all' || 
                                    (changeType === 'ui' && correspondingSection && correspondingSection.hasUI);

            if (inVersionRange && matchesChangeType) {
                item.item.removeClass('ui-filtered-toc');
            } else {
                item.item.addClass('ui-filtered-toc');
            }
        });

        updateStatus();
        
        // Smooth scroll to first visible section if filters were applied
        if ((fromVersion !== 'all' || toVersion !== 'all' || changeType !== 'all') && visibleSections > 0) {
            const firstVisible = $('section[id^="release-v"]:not(.ui-filtered)').first();
            if (firstVisible.length) {
                setTimeout(() => {
                    $('html, body').animate({
                        scrollTop: firstVisible.offset().top - 100
                    }, 500);
                }, 100);
            }
        }
    }

    // Event handlers
    $('#legacy-apply-filter').on('click', function () {
        currentFilters.fromVersion = $('#legacy-from-version').val();
        currentFilters.toVersion = $('#legacy-to-version').val();
        currentFilters.changeType = $('#legacy-change-type').val();
        
        applyFilters();
    });

    $('#legacy-reset-filter, #legacy-clear-filters').on('click', function (e) {
        e.preventDefault();
        
        // Reset UI state
        $('#legacy-from-version, #legacy-to-version').val('all');
        $('#legacy-change-type').val('all');
        
        // Reset filters
        currentFilters = {
            fromVersion: 'all',
            toVersion: 'all',
            changeType: 'all'
        };
        
        // Show all content
        sections.forEach(item => {
            item.section.removeClass('ui-filtered');
            item.section.find('li').removeClass('ui-highlight');
        });
        
        tocItems.forEach(item => {
            item.item.removeClass('ui-filtered-toc');
        });
        
        updateStatus();
    });

    // Auto-apply when selection changes (for better UX)
    $('#legacy-from-version, #legacy-to-version, #legacy-change-type').on('change', function() {
        currentFilters.fromVersion = $('#legacy-from-version').val();
        currentFilters.toVersion = $('#legacy-to-version').val();
        currentFilters.changeType = $('#legacy-change-type').val();
        
        applyFilters();
    });

    // Keyboard accessibility
    $('.ui-changelog-filters').on('keydown', function(e) {
        if (e.key === 'Enter' && e.target.tagName === 'BUTTON') {
            e.target.click();
        }
    });

    // Initialize with proper ARIA attributes
    $('#legacy-filter-status').attr('aria-live', 'polite');
    $('#legacy-filter-status').attr('aria-atomic', 'true');
    
    console.log('Legacy Changelog Filter initialized:', {
        versions: versions,
        sectionsFound: sections.length,
        uiItemsFound: uiItems.length,
        tocItemsFound: tocItems.length
    });
});