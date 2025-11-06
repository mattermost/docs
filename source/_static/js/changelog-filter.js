$(document).ready(function () {
    // Only run on the changelog pages.
    if (!window.location.pathname.includes('/product-overview/mattermost-v11-changelog') && 
        !window.location.pathname.includes('/product-overview/mattermost-v10-changelog') && 
        !window.location.pathname.includes('/product-overview/mattermost-v9-changelog')) {
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

    // Create filter controls
    const filterHTML = `
        <div class="changelog-filters">
            <h3>Filter Changelog</h3>
            <p>Select source and target versions to see only relevant changelog entries</p>
            <div>
                <label for="changelog-source-version">From version:</label>
                <select id="changelog-source-version">
                    <option value="all">All versions</option>
                    ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                </select>

                <label for="changelog-target-version">To version:</label>
                <select id="changelog-target-version">
                    <option value="all">All versions</option>
                    ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                </select>

                <button id="changelog-apply-filter">Apply Filter</button>
                <button id="changelog-reset-filter">Reset</button>
            </div>
        </div>
    `;

    // Insert filter controls above the content
    $('.content h1:first').after(filterHTML);

    // Add data attributes to sections for easier filtering
    sections.forEach(item => {
        item.section.attr('data-version', item.version);
    });

    // Apply filter function
    $('#changelog-apply-filter').on('click', function () {
        const sourceVersion = $('#changelog-source-version').val();
        const targetVersion = $('#changelog-target-version').val();

        // Clear any previous error messages
        $('.changelog-filter-error').remove();

        if (sourceVersion === 'all' && targetVersion === 'all') {
            // Show all sections and TOC items
            sections.forEach(item => {
                item.section.removeClass('filtered');
            });

            tocItems.forEach(item => {
                item.item.removeClass('filtered-toc');
            });
            return;
        }

        // Use the global parseVersion function
        const sourceV = parseVersion(sourceVersion);
        const targetV = parseVersion(targetVersion);

        // If both are specific versions, validate that target >= source
        if (targetV.major < sourceV.major ||
            (targetV.major === sourceV.major && targetV.minor < sourceV.minor)) {
            // Display error message
            $('.changelog-filters').append(
                '<div class="changelog-filter-error">' +
                'Error: Target version must be greater than or equal to source version.' +
                '</div>'
            );
            return; // Don't apply the filter
        }


        // Filter logic
        sections.forEach(item => {
            const sectionV = parseVersion(item.version);

            // Show the section if:
            // 1. Upgrading from a version before or equal to this section's version
            // 2. Upgrading to a version after or equal to this section's version
            const isRelevant = (
                (sourceVersion === 'all' ||
                    (sectionV.major > sourceV.major ||
                        (sectionV.major === sourceV.major && sectionV.minor >= sourceV.minor))) &&
                (targetVersion === 'all' ||
                    (sectionV.major < targetV.major ||
                        (sectionV.major === targetV.major && sectionV.minor <= targetV.minor)))
            );

            if (isRelevant) {
                item.section.removeClass('filtered');
            } else {
                item.section.addClass('filtered');
            }
        });

        // Apply the same filtering logic to TOC items
        tocItems.forEach(item => {
            const tocV = parseVersion(item.version);

            // Use the same relevance logic as for sections
            const isRelevant = (
                (sourceVersion === 'all' ||
                    (tocV.major > sourceV.major ||
                        (tocV.major === sourceV.major && tocV.minor >= sourceV.minor))) &&
                (targetVersion === 'all' ||
                    (tocV.major < targetV.major ||
                        (tocV.major === targetV.major && tocV.minor <= targetV.minor)))
            );

            if (isRelevant) {
                item.item.removeClass('filtered-toc');
            } else {
                item.item.addClass('filtered-toc');
            }
        });
    });

    // Reset filters
    $('#changelog-reset-filter').on('click', function () {
        $('#changelog-source-version, #changelog-target-version').val('all');
        sections.forEach(item => {
            item.section.removeClass('filtered');
        });
        tocItems.forEach(item => {
            item.item.removeClass('filtered-toc');
        });
    });

    // ===== UI-SPECIFIC FILTERING =====
    
    // Extract UI updates from all versions
    const uiUpdates = [];
    sections.forEach(sectionItem => {
        const section = sectionItem.section;
        const version = sectionItem.version;
        
        // Look for "User Interface (UI)" heading within this section
        const uiHeading = section.find('h4').filter(function() {
            return $(this).text().trim().includes('User Interface (UI)');
        });
        
        if (uiHeading.length > 0) {
            // Find all list items under the UI heading
            let currentElement = uiHeading.first();
            const uiItems = [];
            
            // Traverse siblings until we hit the next h4 or the end of section
            while (currentElement.length > 0) {
                currentElement = currentElement.next();
                if (currentElement.is('h4, h3, h2')) {
                    break;
                }
                if (currentElement.is('ul')) {
                    currentElement.find('li').each(function() {
                        const itemText = $(this).text().trim();
                        if (itemText) {
                            uiItems.push({
                                text: itemText,
                                element: $(this)
                            });
                        }
                    });
                }
            }
            
            if (uiItems.length > 0) {
                uiUpdates.push({
                    version: version,
                    items: uiItems
                });
            }
        }
    });
    
    // Only create UI filter if we found UI updates
    if (uiUpdates.length > 0) {
        // Create UI filter controls
        const uiFilterHTML = `
            <div class="ui-filters" style="margin-top: 20px;">
                <h3>Filter UI Updates Only</h3>
                <p>View User Interface updates by version range</p>
                <div>
                    <label for="ui-source-version">From version:</label>
                    <select id="ui-source-version">
                        <option value="all">All versions</option>
                        ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                    </select>
                    
                    <label for="ui-target-version">To version:</label>
                    <select id="ui-target-version">
                        <option value="all">All versions</option>
                        ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                    </select>

                    <button id="ui-apply-filter">Show UI Updates</button>
                    <button id="ui-reset-filter">Show Full Changelog</button>
                </div>
                <div id="ui-filter-results" class="ui-filter-results" style="display: none;">
                    <h4>UI Updates</h4>
                    <div id="ui-updates-content"></div>
                </div>
            </div>
        `;

        // Insert UI filter below the changelog filter
        $('.changelog-filters').after(uiFilterHTML);

        // Apply UI filter function
        $('#ui-apply-filter').on('click', function () {
            const sourceVersion = $('#ui-source-version').val();
            const targetVersion = $('#ui-target-version').val();

            // Clear any previous error messages
            $('.ui-filter-error').remove();

            // Validation for version range
            if (sourceVersion !== 'all' && targetVersion !== 'all') {
                const sourceV = parseVersion(sourceVersion);
                const targetV = parseVersion(targetVersion);
                
                if (targetV.major < sourceV.major ||
                    (targetV.major === sourceV.major && targetV.minor < sourceV.minor)) {
                    $('.ui-filters').append(
                        '<div class="ui-filter-error">' +
                        'Error: Target version must be greater than or equal to source version.' +
                        '</div>'
                    );
                    return;
                }
            }

            // Filter and display UI updates
            let filteredUpdates = uiUpdates.filter(updateGroup => {
                const updateV = parseVersion(updateGroup.version);
                
                const isRelevant = (
                    (sourceVersion === 'all' ||
                        (updateV.major > parseVersion(sourceVersion).major ||
                            (updateV.major === parseVersion(sourceVersion).major && 
                             updateV.minor >= parseVersion(sourceVersion).minor))) &&
                    (targetVersion === 'all' ||
                        (updateV.major < parseVersion(targetVersion).major ||
                            (updateV.major === parseVersion(targetVersion).major && 
                             updateV.minor <= parseVersion(targetVersion).minor)))
                );
                
                return isRelevant;
            });

            // Sort by version (newest first)
            filteredUpdates.sort((a, b) => {
                const vA = parseVersion(a.version);
                const vB = parseVersion(b.version);
                if (vB.major !== vA.major) {
                    return vB.major - vA.major;
                }
                return vB.minor - vA.minor;
            });

            // Generate HTML for filtered results
            let resultsHTML = '';
            if (filteredUpdates.length === 0) {
                resultsHTML = '<p>No UI updates found in the selected version range.</p>';
            } else {
                filteredUpdates.forEach(updateGroup => {
                    resultsHTML += `<div class="ui-version-group">`;
                    resultsHTML += `<h5>Version ${updateGroup.version}</h5>`;
                    resultsHTML += '<ul>';
                    updateGroup.items.forEach(item => {
                        resultsHTML += `<li>${item.text}</li>`;
                    });
                    resultsHTML += '</ul>';
                    resultsHTML += '</div>';
                });
            }

            $('#ui-updates-content').html(resultsHTML);
            $('#ui-filter-results').show();
            
            // Hide the main changelog content when showing UI-only view
            sections.forEach(item => {
                item.section.addClass('ui-filtered');
            });
        });

        // Reset UI filter
        $('#ui-reset-filter').on('click', function () {
            $('#ui-source-version, #ui-target-version').val('all');
            $('#ui-filter-results').hide();
            $('.ui-filter-error').remove();
            
            // Show the main changelog content again
            sections.forEach(item => {
                item.section.removeClass('ui-filtered');
            });
        });
    }
});
