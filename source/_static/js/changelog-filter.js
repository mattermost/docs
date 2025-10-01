$(document).ready(function () {
    // Only run on the changelog pages.
    if (!window.location.pathname.includes('/about/mattermost-v10-changelog') && !window.location.pathname.includes('/about/mattermost-v9-changelog')) {
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
            <p>Select source and target versions to see only relevant changelog entries, or filter by audience type</p>
            
            <div class="version-filters">
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

            <div class="audience-filters">
                <h4>Filter by Audience:</h4>
                <div class="audience-buttons">
                    <button class="audience-filter-btn" data-audience="all">Show All</button>
                    <button class="audience-filter-btn" data-audience="Admin">Admin</button>
                    <button class="audience-filter-btn" data-audience="End-user">End-user</button>
                    <button class="audience-filter-btn" data-audience="Developer">Developer / API / Integrator</button>
                    <button class="audience-filter-btn" data-audience="Security">Security</button>
                    <button class="audience-filter-btn" data-audience="Platform">Platform</button>
                </div>
                <p class="audience-help-text">Click audience buttons to show only relevant items. Multiple audiences can be selected.</p>
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
        // Reset audience filters
        $('.audience-filter-btn').removeClass('active');
        $('.audience-filter-btn[data-audience="all"]').addClass('active');
        $('li[data-audience-tags]').removeClass('audience-filtered');
    });

    // Audience filtering functionality
    let activeAudiences = new Set(['all']); // Track active audience filters

    // Add data attributes to list items based on their audience tags
    function addAudienceDataAttributes() {
        // Find all list items with bold audience tags
        $('li').each(function() {
            const listItem = $(this);
            const html = listItem.html();
            const audiences = [];
            
            // Check for audience tags in the format <strong>[AudienceType]</strong>
            const audienceMatches = html.match(/<strong>\[([^\]]+)\]<\/strong>/g);
            if (audienceMatches) {
                audienceMatches.forEach(match => {
                    const audience = match.replace(/<strong>\[([^\]]+)\]<\/strong>/, '$1');
                    audiences.push(audience);
                });
                
                // Store audiences as a data attribute
                listItem.attr('data-audience-tags', audiences.join(','));
            }
        });
    }

    // Apply audience data attributes
    addAudienceDataAttributes();

    // Audience filter button click handler
    $('.audience-filter-btn').on('click', function() {
        const selectedAudience = $(this).data('audience');
        
        if (selectedAudience === 'all') {
            // Clear all other selections and show all
            activeAudiences.clear();
            activeAudiences.add('all');
            $('.audience-filter-btn').removeClass('active');
            $(this).addClass('active');
        } else {
            // Toggle the selected audience
            if (activeAudiences.has(selectedAudience)) {
                activeAudiences.delete(selectedAudience);
                $(this).removeClass('active');
            } else {
                activeAudiences.add(selectedAudience);
                $(this).addClass('active');
                // Remove "all" if other audiences are selected
                if (activeAudiences.has('all')) {
                    activeAudiences.delete('all');
                    $('.audience-filter-btn[data-audience="all"]').removeClass('active');
                }
            }
            
            // If no audiences selected, default to "all"
            if (activeAudiences.size === 0) {
                activeAudiences.add('all');
                $('.audience-filter-btn[data-audience="all"]').addClass('active');
            }
        }
        
        // Apply the audience filter
        applyAudienceFilter();
    });

    // Function to apply audience filtering
    function applyAudienceFilter() {
        if (activeAudiences.has('all')) {
            // Show all items
            $('li[data-audience-tags]').removeClass('audience-filtered');
        } else {
            // Filter items based on selected audiences
            $('li[data-audience-tags]').each(function() {
                const listItem = $(this);
                const itemAudiences = listItem.attr('data-audience-tags').split(',');
                
                // Check if any of the item's audiences match active filters
                const hasMatchingAudience = itemAudiences.some(audience => 
                    activeAudiences.has(audience) || 
                    (audience === 'Developer / API / Integrator' && activeAudiences.has('Developer'))
                );
                
                if (hasMatchingAudience) {
                    listItem.removeClass('audience-filtered');
                } else {
                    listItem.addClass('audience-filtered');
                }
            });
        }
    }

    // Set initial state - show all
    $('.audience-filter-btn[data-audience="all"]').addClass('active');
});
