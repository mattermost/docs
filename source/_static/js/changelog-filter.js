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
            <p>Select source and target versions to see only relevant changelog entries, or filter by audience type.</p>
            
            <div class="version-filters">
                <h4>Version Range Filter</h4>
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

            <div class="audience-filters">
                <h4>Audience Filter</h4>
                <p>Click audience tags to show/hide relevant items:</p>
                <div class="audience-buttons">
                    <button class="audience-filter-btn" data-audience="admin">Admin</button>
                    <button class="audience-filter-btn" data-audience="end-user">End-user</button>
                    <button class="audience-filter-btn" data-audience="developer">Developer / API / Integrator</button>
                    <button class="audience-filter-btn" data-audience="security">Security</button>
                    <button class="audience-filter-btn" data-audience="platform">Platform</button>
                    <button class="audience-filter-btn" data-audience="accessibility">Acessibility</button>
                    <button id="audience-show-all">Show All</button>
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
        // Reset audience filters
        $('.audience-filter-btn').removeClass('active');
        $('li').removeClass('audience-filtered');
        $('.changelog-filter-error').remove();
    });

    // Audience filtering functionality
    let activeAudiences = new Set();

    function applyAudienceFilter() {
        if (activeAudiences.size === 0) {
            // Show all items if no audience filter is active
            $('li').removeClass('audience-filtered');
            return;
        }

        // Find all list items in changelog content
        $('.content li').each(function() {
            const $item = $(this);
            const itemText = $item.text();
            let hasMatchingAudience = false;

            // Check if the item contains any of the active audience tags
            activeAudiences.forEach(audience => {
                let audiencePattern = '';
                switch (audience) {
                    case 'admin':
                        audiencePattern = '[Admin]';
                        break;
                    case 'end-user':
                        audiencePattern = '[End-user]';
                        break;
                    case 'developer':
                        audiencePattern = '[Developer / API / Integrator]';
                        break;
                    case 'security':
                        audiencePattern = '[Security]';
                        break;
                    case 'platform':
                        audiencePattern = '[Platform]';
                        break;
                    case 'accessibility':
                        audiencePattern = '[Accessibility]';
                        break;
                }
                if (itemText.includes(audiencePattern)) {
                    hasMatchingAudience = true;
                }
            });

            // Show or hide the item based on audience match
            if (hasMatchingAudience) {
                $item.removeClass('audience-filtered');
            } else {
                $item.addClass('audience-filtered');
            }
        });
    }

    // Audience filter button click handlers
    $('.audience-filter-btn').on('click', function() {
        const audience = $(this).data('audience');
        const $btn = $(this);

        if ($btn.hasClass('active')) {
            // Deactivate this audience filter
            $btn.removeClass('active');
            activeAudiences.delete(audience);
        } else {
            // Activate this audience filter
            $btn.addClass('active');
            activeAudiences.add(audience);
        }

        applyAudienceFilter();
    });

    // Show all audience items
    $('#audience-show-all').on('click', function() {
        $('.audience-filter-btn').removeClass('active');
        activeAudiences.clear();
        applyAudienceFilter();
    });
});
