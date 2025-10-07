$(document).ready(function () {
    // Only run on the changelog pages.
    if (!window.location.pathname.includes('/about/mattermost-v10-changelog') && !window.location.pathname.includes('/about/mattermost-v9-changelog') && !window.location.pathname.includes('/product-overview/mattermost-v10-changelog')) {
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
                <h4>Filter by Audience</h4>
                <p>Click audience tags to show/hide relevant items</p>
                <div class="audience-buttons">
                    <button class="audience-btn" data-audience="admin">Admin</button>
                    <button class="audience-btn" data-audience="end-user">End-user</button>
                    <button class="audience-btn" data-audience="developer">Developer / API / Integrator</button>
                    <button class="audience-btn" data-audience="security">Security</button>
                    <button class="audience-btn" data-audience="platform">Platform</button>
                    <button class="audience-btn" data-audience="accessibility">Accessibility</button>
                    <button id="audience-show-all" class="audience-btn show-all">Show All</button>
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

    // Audience filtering functionality
    let selectedAudiences = new Set();

    function findAllListItems() {
        return $('section[id^="release-v"] li, section[id^="release-v"] ul ul li');
    }

    function preserveImportantNotices() {
        // Find and mark Important notices to always be visible
        $('div.admonition.important, .admonition-important, [class*="important"]').addClass('always-visible');
        $('div:contains("Important")').filter(function() {
            return $(this).text().match(/^Important/);
        }).addClass('always-visible');
        
        // Also preserve MyST Important directive content
        $('div[class*="admonition"], div[class*="note"]').each(function() {
            if ($(this).find('.admonition-title:contains("Important")').length > 0 ||
                $(this).text().toLowerCase().includes('important upgrade') ||
                $(this).text().toLowerCase().includes('important notice')) {
                $(this).addClass('always-visible');
            }
        });
    }

    function applyAudienceFilter() {
        const allItems = findAllListItems();
        
        // First preserve important notices
        preserveImportantNotices();
        
        if (selectedAudiences.size === 0) {
            // Show all items
            allItems.removeClass('audience-filtered');
            return;
        }

        allItems.each(function() {
            const $item = $(this);
            const text = $item.text();
            
            // Skip if this is marked as always visible (Important notices)
            if ($item.hasClass('always-visible') || $item.closest('.always-visible').length > 0) {
                $item.removeClass('audience-filtered');
                return;
            }
            
            let hasMatchingAudience = false;
            
            // Check if item contains any of the selected audience tags
            selectedAudiences.forEach(audience => {
                const patterns = {
                    'admin': /\*\*\[Admin\]\*\*/i,
                    'end-user': /\*\*\[End-user\]\*\*/i,
                    'developer': /\*\*\[Developer \/ API \/ Integrator\]\*\*/i,
                    'security': /\*\*\[Security\]\*\*/i,
                    'platform': /\*\*\[Platform\]\*\*/i
                    'accessibility': /\*\*\[Accessibility\]\*\*/i
                };
                
                if (patterns[audience] && patterns[audience].test(text)) {
                    hasMatchingAudience = true;
                }
            });
            
            if (hasMatchingAudience) {
                $item.removeClass('audience-filtered');
            } else {
                $item.addClass('audience-filtered');
            }
        });
    }

    // Audience button click handlers
    $('.audience-btn:not(#audience-show-all)').on('click', function() {
        const audience = $(this).data('audience');
        
        if (selectedAudiences.has(audience)) {
            selectedAudiences.delete(audience);
            $(this).removeClass('active');
        } else {
            selectedAudiences.add(audience);
            $(this).addClass('active');
        }
        
        applyAudienceFilter();
    });

    // Show all button handler
    $('#audience-show-all').on('click', function() {
        selectedAudiences.clear();
        $('.audience-btn').removeClass('active');
        applyAudienceFilter();
    });

    // Initial setup
    preserveImportantNotices();
});
