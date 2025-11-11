$(document).ready(function () {
    // Only run on the legacy releases page
    if (!window.location.pathname.includes('/product-overview/unsupported-legacy-releases')) {
        return;
    }

    // Extract versions from section IDs
    const versions = [];
    const sections = [];
    const tocItems = [];

    // Find all release sections based on the heading pattern
    $('section[id^="release-v"]').each(function () {
        const sectionId = $(this).attr('id');
        const versionMatch = sectionId.match(/release-v(\d+)-(\d+)/);

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
                id: sectionId
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
                // Check if this links to a version section using the same regex
                const versionMatch = sectionId.match(/release-v(\d+)-(\d+)/);
                if (versionMatch) {
                    const major = parseInt(versionMatch[1]);
                    const minor = parseInt(versionMatch[2]);
                    const version = `${major}.${minor}`;

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
    sortVersions(versions);

    // Create filter controls with compact design
    const filterHTML = `
        <div class="changelog-filters">
            <div class="changelog-filters__header">
                <span class="changelog-filters__label">Filters:</span>
                <div class="changelog-filters__controls">
                    <div class="changelog-filters__dropdown-wrapper">
                        <select id="legacy-version-filter" class="changelog-filters__select">
                            <option value="all">All versions</option>
                            ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                        </select>
                    </div>
                    <div class="changelog-filters__dropdown-wrapper">
                        <select id="legacy-change-type-filter" class="changelog-filters__select">
                            <option value="all">All changes</option>
                            <option value="ui">UI changes</option>
                        </select>
                    </div>
                    <button id="legacy-apply-filter" class="changelog-filters__apply-btn">Apply</button>
                    <button id="legacy-reset-filter" class="changelog-filters__clear-btn">
                        <span class="clear-icon">✕</span> Clear filters
                    </button>
                </div>
            </div>
            <div id="legacy-filter-status" class="changelog-filters__status" style="display: none;"></div>
        </div>
    `;

    // Insert filter controls above the content
    $('.content h1:first').after(filterHTML);

    // Add data attributes to sections for easier filtering
    sections.forEach(item => {
        item.section.attr('data-version', item.version);
    });

    // Apply filter function
    $('#legacy-apply-filter').on('click', function () {
        const selectedVersion = $('#legacy-version-filter').val();
        const changeType = $('#legacy-change-type-filter').val();

        // Clear any previous error messages
        $('.changelog-filter-error').remove();

        // Reset all filters first
        sections.forEach(item => {
            item.section.removeClass('filtered version-filtered ui-filtered');
        });
        tocItems.forEach(item => {
            item.item.removeClass('filtered-toc version-filtered ui-filtered');
        });

        let appliedFilters = [];

        // Apply version filtering
        if (selectedVersion !== 'all') {
            const selectedV = parseVersion(selectedVersion);
            
            sections.forEach(item => {
                const sectionV = parseVersion(item.version);
                
                if (!(sectionV.major === selectedV.major && sectionV.minor === selectedV.minor)) {
                    item.section.addClass('filtered version-filtered');
                }
            });

            tocItems.forEach(item => {
                const tocV = parseVersion(item.version);
                
                if (!(tocV.major === selectedV.major && tocV.minor === selectedV.minor)) {
                    item.item.addClass('filtered-toc version-filtered');
                }
            });
            
            appliedFilters.push(`v${selectedVersion}`);
        }

        // Apply UI change type filtering
        if (changeType === 'ui') {
            sections.forEach(item => {
                const hasUIChanges = item.section.find('h4:contains("User Interface (UI)")').length > 0 ||
                                   item.section.find('h4:contains("Web User Interface (UI)")').length > 0;
                
                if (!hasUIChanges) {
                    item.section.addClass('filtered ui-filtered');
                }
            });

            // For TOC items, we need to check if their corresponding sections have UI changes
            tocItems.forEach(item => {
                const correspondingSection = sections.find(s => s.id === item.id);
                if (correspondingSection) {
                    const hasUIChanges = correspondingSection.section.find('h4:contains("User Interface (UI)")').length > 0 ||
                                       correspondingSection.section.find('h4:contains("Web User Interface (UI)")').length > 0;
                    
                    if (!hasUIChanges) {
                        item.item.addClass('filtered-toc ui-filtered');
                    }
                }
            });
            
            appliedFilters.push('UI changes');
        }

        // Update status feedback
        const statusElement = $('#legacy-filter-status');
        if (appliedFilters.length > 0) {
            statusElement.text(`Showing ${appliedFilters.join(' → ')}`).show();
        } else {
            statusElement.hide();
        }
    });

    // Reset filters
    $('#legacy-reset-filter').on('click', function () {
        $('#legacy-version-filter, #legacy-change-type-filter').val('all');
        sections.forEach(item => {
            item.section.removeClass('filtered version-filtered ui-filtered');
        });
        tocItems.forEach(item => {
            item.item.removeClass('filtered-toc version-filtered ui-filtered');
        });
        $('#legacy-filter-status').hide();
    });
});