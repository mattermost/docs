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
            
            <!-- Version Filtering -->
            <div class="filter-section">
                <h4>Filter by Version Range</h4>
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

                    <button id="changelog-apply-filter">Apply Version Filter</button>
                    <button id="changelog-reset-filter">Reset All</button>
                </div>
            </div>

            <!-- Audience Filtering -->
            <div class="filter-section">
                <h4>Filter by Audience</h4>
                <p class="filter-description">Click audience tags to show/hide relevant items</p>
                <div class="audience-filters">
                    <button class="audience-filter-btn" data-audience="admin">Admin</button>
                    <button class="audience-filter-btn" data-audience="end-user">End-user</button>
                    <button class="audience-filter-btn" data-audience="developer">Developer / API / Integrator</button>
                    <button class="audience-filter-btn" data-audience="security">Security</button>
                    <button class="audience-filter-btn" data-audience="platform">Platform</button>
                    <button class="audience-filter-btn" accessibility="accessibility">Accessibility</button>
                </div>
            </div>
        </div>
    `;

    // Insert filter controls above the content
    $('.content h1:first').after(filterHTML);

    // Add data attributes to sections for easier filtering
    sections.forEach(item => {
        item.section.attr('data-version', item.version);
    });

    // Global variables to track filter states
    let activeAudienceFilters = new Set();
    let versionFilterActive = false;

    // Add data attributes to all bullet points with audience tags
    function setupAudienceData() {
        $('li').each(function() {
            const $li = $(this);
            const text = $li.html();
            
            // Skip Important notices - never filter these
            if ($li.closest('.admonition').hasClass('important') || 
                $li.closest('div[class*="important"]').length > 0 ||
                text.includes('{Important}') ||
                $li.parent().prev().text().includes('Important')) {
                $li.addClass('always-visible');
                return;
            }

            // Extract audience tags from the text
            const audiences = [];
            const audienceMap = {
                'Admin': 'admin',
                'End-user': 'end-user', 
                'Developer / API / Integrator': 'developer',
                'Security': 'security',
                'Platform': 'platform'
                'Accessibility': 'accessibility'
            };

            // Look for bold audience tags
            const boldMatches = text.match(/\*\*\[([^\]]+)\]\*\*/g);
            if (boldMatches) {
                boldMatches.forEach(match => {
                    const audienceText = match.replace(/\*\*\[|\]\*\*/g, '');
                    const audienceKey = audienceMap[audienceText];
                    if (audienceKey) {
                        audiences.push(audienceKey);
                    }
                });
            }

            if (audiences.length > 0) {
                $li.attr('data-audiences', audiences.join(','));
            }
        });
    }

    // Initialize audience data
    setupAudienceData();

    // Audience filter functionality
    $('.audience-filter-btn').on('click', function() {
        const $btn = $(this);
        const audience = $btn.data('audience');
        
        if ($btn.hasClass('active')) {
            // Deactivate this filter
            $btn.removeClass('active');
            activeAudienceFilters.delete(audience);
        } else {
            // Activate this filter
            $btn.addClass('active');
            activeAudienceFilters.add(audience);
        }
        
        applyAudienceFiltering();
    });

    // Apply audience filtering
    function applyAudienceFiltering() {
        if (activeAudienceFilters.size === 0) {
            // No audience filters active, show all items
            $('li').removeClass('audience-filtered');
            return;
        }

        $('li').each(function() {
            const $li = $(this);
            
            // Always show Important notices
            if ($li.hasClass('always-visible')) {
                $li.removeClass('audience-filtered');
                return;
            }

            const itemAudiences = $li.attr('data-audiences');
            if (!itemAudiences) {
                // No audience tags, hide when filtering
                $li.addClass('audience-filtered');
                return;
            }

            // Check if this item matches any active filters
            const itemAudienceList = itemAudiences.split(',');
            const hasMatch = itemAudienceList.some(aud => activeAudienceFilters.has(aud));
            
            if (hasMatch) {
                $li.removeClass('audience-filtered');
            } else {
                $li.addClass('audience-filtered');
            }
        });
    }

    // Version filtering (existing functionality)
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
            versionFilterActive = false;
            return;
        }

        versionFilterActive = true;

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
        // Reset version filters
        $('#changelog-source-version, #changelog-target-version').val('all');
        sections.forEach(item => {
            item.section.removeClass('filtered');
        });
        tocItems.forEach(item => {
            item.item.removeClass('filtered-toc');
        });
        versionFilterActive = false;

        // Reset audience filters
        $('.audience-filter-btn').removeClass('active');
        activeAudienceFilters.clear();
        $('li').removeClass('audience-filtered');
    });
});
