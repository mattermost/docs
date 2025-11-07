$(document).ready(function () {
    // Only run on the legacy releases page
    if (!window.location.pathname.includes('/unsupported-legacy-releases')) {
        return;
    }

    // Extract versions from section IDs
    const versions = [];
    const sections = [];
    const tocItems = [];

    // Find all release sections based on the heading pattern
    $('section[id^="release-v"], section[id^="v"]').each(function () {
        const sectionId = $(this).attr('id');
        let versionMatch = sectionId.match(/release-v(\d+)-(\d+)/);
        
        // Also try matching direct version format like "v9-5"
        if (!versionMatch) {
            versionMatch = sectionId.match(/v(\d+)-(\d+)/);
        }

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

    // Find corresponding TOC items in the sidebar
    $('.toc-drawer li').each(function () {
        const $link = $(this).find('a').first();
        if ($link.length) {
            const href = $link.attr('href');
            if (href && href.includes('#')) {
                const sectionId = href.split('#')[1];
                let versionMatch = sectionId.match(/release-v(\d+)-(\d+)/);
                
                if (!versionMatch) {
                    versionMatch = sectionId.match(/v(\d+)-(\d+)/);
                }
                
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

    // Sort versions in descending order (newest first)
    versions.sort((a, b) => {
        const [aMajor, aMinor] = a.split('.').map(Number);
        const [bMajor, bMinor] = b.split('.').map(Number);
        
        if (aMajor !== bMajor) return bMajor - aMajor;
        return bMinor - aMinor;
    });

    // Only proceed if we found versions
    if (versions.length === 0) {
        return;
    }

    // Create filter controls
    const filterHTML = `
        <div class="ui-changelog-filter">
            <h3>Filter Legacy Releases</h3>
            <div class="ui-filter-description">Select version range and change types to filter legacy release notes</div>
            <div class="ui-filter-controls">
                <div class="ui-filter-group">
                    <label for="ui-from-version">From version (select your current version):</label>
                    <select id="ui-from-version">
                        <option value="all">All versions</option>
                        ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                    </select>
                </div>

                <div class="ui-filter-group">
                    <label for="ui-to-version">To version (select your target version):</label>
                    <select id="ui-to-version">
                        <option value="all">All versions</option>
                        ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                    </select>
                </div>

                <div class="ui-filter-group">
                    <label>Change types:</label>
                    <div class="ui-change-type-group">
                        <label>
                            <input type="radio" name="ui-change-type" value="all" checked>
                            All changes
                        </label>
                        <label>
                            <input type="radio" name="ui-change-type" value="ui-only">
                            UI changes only
                        </label>
                    </div>
                </div>
            </div>
            <div id="ui-filter-status" class="ui-filter-status" style="display: none;"></div>
            <div id="ui-filter-error" class="ui-filter-error" style="display: none;"></div>
        </div>
    `;

    // Insert filter controls above the content
    $('.content h1:first').after(filterHTML);

    // Helper function to parse version strings
    function parseVersion(versionStr) {
        if (versionStr === 'all') return { major: Infinity, minor: Infinity };
        const [major, minor] = versionStr.split('.').map(Number);
        return { major, minor };
    }

    // Helper function to find UI sections within a release section
    function findUISections(sectionEl) {
        const uiSections = [];
        
        // Look for "#### User Interface (UI)" headers
        sectionEl.find('h4').each(function() {
            const headerText = $(this).text().trim();
            if (headerText.includes('User Interface') || headerText.includes('UI')) {
                // Find all content until the next h4
                const uiContent = [];
                let nextEl = $(this).next();
                
                while (nextEl.length && !nextEl.is('h4') && !nextEl.is('h3') && !nextEl.is('h2')) {
                    uiContent.push(nextEl);
                    nextEl = nextEl.next();
                }
                
                if (uiContent.length > 0) {
                    uiSections.push({
                        header: $(this),
                        content: uiContent
                    });
                }
            }
        });
        
        return uiSections;
    }

    // Apply filter function
    function applyFilter() {
        const fromVersion = $('#ui-from-version').val();
        const toVersion = $('#ui-to-version').val();
        const changeType = $('input[name="ui-change-type"]:checked').val();

        // Clear previous messages
        $('#ui-filter-status, #ui-filter-error').hide();

        // Validate version range
        if (fromVersion !== 'all' && toVersion !== 'all') {
            const fromV = parseVersion(fromVersion);
            const toV = parseVersion(toVersion);
            
            if (toV.major < fromV.major || (toV.major === fromV.major && toV.minor < fromV.minor)) {
                $('#ui-filter-error').text('Target version must be greater than or equal to source version.').show();
                return;
            }
        }

        let visibleCount = 0;
        let totalCount = sections.length;
        let uiItemCount = 0;

        // Filter sections
        sections.forEach(item => {
            const sectionV = parseVersion(item.version);
            
            // Check version range
            const isInVersionRange = (
                (fromVersion === 'all' || 
                 (sectionV.major > parseVersion(fromVersion).major || 
                  (sectionV.major === parseVersion(fromVersion).major && sectionV.minor >= parseVersion(fromVersion).minor))) &&
                (toVersion === 'all' || 
                 (sectionV.major < parseVersion(toVersion).major || 
                  (sectionV.major === parseVersion(toVersion).major && sectionV.minor <= parseVersion(toVersion).minor)))
            );

            if (!isInVersionRange) {
                item.section.addClass('ui-hidden');
                return;
            }

            // If filtering for UI changes only
            if (changeType === 'ui-only') {
                const uiSections = findUISections(item.section);
                
                if (uiSections.length === 0) {
                    // No UI sections found, hide the entire section
                    item.section.addClass('ui-hidden');
                    return;
                }

                // Show the section but hide non-UI content
                item.section.removeClass('ui-hidden');
                
                // Hide all content first
                item.section.find('h4, p, ul, ol, div').each(function() {
                    if (!$(this).hasClass('ui-changelog-filter')) {
                        $(this).addClass('ui-hidden');
                    }
                });

                // Show UI sections and highlight them
                uiSections.forEach(uiSection => {
                    uiSection.header.removeClass('ui-hidden').addClass('ui-content-highlighted');
                    uiSection.content.forEach(el => {
                        $(el).removeClass('ui-hidden').addClass('ui-content-highlighted');
                    });
                    uiItemCount++;
                });

                // Always show the main section header
                item.section.find('h2, h3').first().removeClass('ui-hidden');

                visibleCount++;
            } else {
                // Show all content
                item.section.removeClass('ui-hidden');
                item.section.find('.ui-hidden').removeClass('ui-hidden ui-content-highlighted');
                visibleCount++;
            }
        });

        // Update TOC items
        tocItems.forEach(item => {
            const sectionV = parseVersion(item.version);
            const isInVersionRange = (
                (fromVersion === 'all' || 
                 (sectionV.major > parseVersion(fromVersion).major || 
                  (sectionV.major === parseVersion(fromVersion).major && sectionV.minor >= parseVersion(fromVersion).minor))) &&
                (toVersion === 'all' || 
                 (sectionV.major < parseVersion(toVersion).major || 
                  (sectionV.major === parseVersion(toVersion).major && sectionV.minor <= parseVersion(toVersion).minor)))
            );

            if (isInVersionRange && (changeType === 'all' || findUISections($('#' + item.id)).length > 0)) {
                item.item.removeClass('ui-hidden');
            } else {
                item.item.addClass('ui-hidden');
            }
        });

        // Show status message
        let statusMessage = '';
        if (fromVersion === 'all' && toVersion === 'all') {
            if (changeType === 'ui-only') {
                statusMessage = `Showing UI changes (${uiItemCount} UI sections found)`;
            } else {
                statusMessage = `Showing all changes (${visibleCount} of ${totalCount} releases)`;
            }
        } else {
            const fromText = fromVersion === 'all' ? 'earliest' : `v${fromVersion}`;
            const toText = toVersion === 'all' ? 'latest' : `v${toVersion}`;
            if (changeType === 'ui-only') {
                statusMessage = `Showing UI changes from ${fromText} to ${toText} (${uiItemCount} UI sections found)`;
            } else {
                statusMessage = `Showing changes from ${fromText} to ${toText} (${visibleCount} of ${totalCount} releases)`;
            }
        }
        
        $('#ui-filter-status').text(statusMessage).show();

        // Scroll to first visible section
        const firstVisible = $('.content section:not(.ui-hidden)').first();
        if (firstVisible.length && (fromVersion !== 'all' || toVersion !== 'all' || changeType !== 'all')) {
            setTimeout(() => {
                firstVisible[0].scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 100);
        }
    }

    // Event listeners with preventDefault to stop unwanted scrolling
    $('#ui-from-version, #ui-to-version').on('change', function(e) {
        e.preventDefault();
        applyFilter();
    });

    $('input[name="ui-change-type"]').on('change', function(e) {
        e.preventDefault();
        applyFilter();
    });

    // Initialize with current state
    applyFilter();
});