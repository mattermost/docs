$(document).ready(function () {
    // Only run on the changelog pages.
    if (!window.location.pathname.includes('/product-overview/mattermost-v10-changelog') && !window.location.pathname.includes('/about/mattermost-v10-changelog') && !window.location.pathname.includes('/about/mattermost-v9-changelog')) {
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
        // Reset audience filters
        $('.audience-filter-btn').removeClass('active');
        $('.audience-filtered').removeClass('audience-filtered');
        activeAudiences.clear();
    });

    // Audience filtering functionality
    const audiences = ['Admin', 'End-user', 'Developer / API / Integrator', 'Security', 'Platform'];
    const activeAudiences = new Set();

    // Create audience filter interface
    const audienceFilterHTML = `
        <div class="audience-filters" style="margin-top: 15px;">
            <h4>Filter by Audience</h4>
            <p>Select one or more audience types to see only relevant items:</p>
            <div class="audience-buttons">
                ${audiences.map(audience => `
                    <button class="audience-filter-btn" data-audience="${audience}">${audience}</button>
                `).join('')}
                <button class="audience-filter-btn show-all-btn" data-audience="all">Show All</button>
            </div>
        </div>
    `;

    // Insert audience filters after version filters
    $('.changelog-filters').append(audienceFilterHTML);
    
    // Set "Show All" as active by default
    $('.show-all-btn').addClass('active');

    // Find all items with audience tags and mark them
    $('li').each(function() {
        const $item = $(this);
        const text = $item.html();
        
        // Check for audience tags in the format **[Audience]**
        audiences.forEach(audience => {
            if (text && text.includes(`**[${audience}]**`)) {
                $item.addClass(`audience-${audience.toLowerCase().replace(/\s+/g, '-').replace(/\//g, '-')}`);
                $item.attr('data-audiences', ($item.attr('data-audiences') || '') + audience + ',');
            }
        });

        // Mark Important notices to always be visible
        const $parent = $item.parent();
        const parentText = $parent.text();
        
        if (text && (
            text.includes('{Important}') || 
            text.includes('```{Important}') ||
            $item.closest('.admonition').hasClass('important') ||
            $item.closest('section').find('.admonition.important').length > 0 ||
            parentText.includes('Important Upgrade Notes')
        )) {
            $item.addClass('always-visible');
        }
        
        // Also mark entire Important sections
        if ($item.is('h3, h4') && text.includes('Important')) {
            $item.addClass('always-visible');
            // Mark all following siblings until next heading
            $item.nextUntil('h1, h2, h3, h4').addClass('always-visible');
        }
    });

    // Handle audience filter clicks
    $('.audience-filter-btn').on('click', function() {
        const $btn = $(this);
        const audience = $btn.data('audience');

        if (audience === 'all') {
            // Show all - reset audience filtering
            $('.audience-filter-btn').removeClass('active');
            $btn.addClass('active');
            $('.audience-filtered').removeClass('audience-filtered');
            activeAudiences.clear();
            return;
        }

        // Toggle audience filter
        if ($btn.hasClass('active')) {
            $btn.removeClass('active');
            activeAudiences.delete(audience);
        } else {
            $btn.addClass('active');
            activeAudiences.add(audience);
            // Remove "Show All" active state
            $('.show-all-btn').removeClass('active');
        }

        // Apply audience filtering
        applyAudienceFilter();
    });

    function applyAudienceFilter() {
        if (activeAudiences.size === 0) {
            // No filters active, show all
            $('.audience-filtered').removeClass('audience-filtered');
            return;
        }

        // Hide all items first
        $('li').each(function() {
            const $item = $(this);
            
            // Always keep Important notices visible
            if ($item.hasClass('always-visible')) {
                $item.removeClass('audience-filtered');
                return;
            }

            const itemAudiences = $item.attr('data-audiences');
            if (!itemAudiences) {
                // No audience tags, hide during filtering
                $item.addClass('audience-filtered');
                return;
            }

            // Check if item has any of the active audiences
            let hasActiveAudience = false;
            for (const audience of activeAudiences) {
                if (itemAudiences.includes(audience)) {
                    hasActiveAudience = true;
                    break;
                }
            }

            if (hasActiveAudience) {
                $item.removeClass('audience-filtered');
            } else {
                $item.addClass('audience-filtered');
            }
        });
    }
});
