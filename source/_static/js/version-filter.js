$(document).ready(function () {
    if (!window.location.pathname.includes('/upgrade/important-upgrade-notes')) {
        return;
    }

    // Extract versions from the table
    const versions = [];
    const rows = [];
    let lastVersion = null;

    $('table.docutils tr').each(function (index) {
        if (index === 0) return; // Skip header row

        const firstCell = $(this).find('td').first();
        if (firstCell.length) {
            const versionText = firstCell.text().trim();
            const versionMatch = versionText.match(/v(\d+\.\d+)/);

            if (versionMatch) {
                // If we found a version in this row
                const version = versionMatch[1];
                if (!versions.includes(version)) {
                    versions.push(version);
                }
                lastVersion = version;

                // Associate row with version
                rows.push({
                    row: $(this),
                    version: version
                });
            } else if (lastVersion) {
                // If no version in this row but we have a previous version
                // This is a continuation row for the last version
                rows.push({
                    row: $(this),
                    version: lastVersion
                });
            }
        }
    });

    // Sort versions in descending order (newest first)
    sortVersions(versions);

    // Create filter controls
    const filterHTML = `
        <div class="version-filters">
            <h3>Filter Upgrade Notes</h3>
            <p>Select source and target versions to see only relevant upgrade notes</p>
            <div>
                <label for="source-version">From version:</label>
                <select id="source-version">
                    <option value="all">All versions</option>
                    ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                </select>
                
                <label for="target-version">To version:</label>
                <select id="target-version">
                    <option value="all">All versions</option>
                    ${versions.map(v => `<option value="${v}">v${v}</option>`).join('')}
                </select>

                <button id="apply-filter">Apply Filter</button>
                <button id="reset-filter">Reset</button>
            </div>
        </div>
    `;

    // Insert filter above the table
    $('table.docutils').first().before(filterHTML);

    // Add data attributes to rows for easier filtering
    rows.forEach(item => {
        item.row.attr('data-version', item.version);
    });

    // Apply filter function
    $('#apply-filter').on('click', function () {
        const sourceVersion = $('#source-version').val();
        const targetVersion = $('#target-version').val();

        if (sourceVersion === 'all' && targetVersion === 'all') {
            // Show all rows
            rows.forEach(item => {
                item.row.removeClass('filtered');
            });
            return;
        }

        // Use the global parseVersion function

        const sourceV = parseVersion(sourceVersion);
        const targetV = parseVersion(targetVersion);

        // Filter logic
        rows.forEach(item => {
            const rowV = parseVersion(item.version);

            // Show the row if:
            // 1. Upgrading from a version before or equal to this row's version
            // 2. Upgrading to a version after or equal to this row's version
            const isRelevant = (
                (sourceVersion === 'all' ||
                    (rowV.major > sourceV.major ||
                        (rowV.major === sourceV.major && rowV.minor >= sourceV.minor))) &&
                (targetVersion === 'all' ||
                    (rowV.major < targetV.major ||
                        (rowV.major === targetV.major && rowV.minor <= targetV.minor)))
            );

            if (isRelevant) {
                item.row.removeClass('filtered');
            } else {
                item.row.addClass('filtered');
            }
        });
    });

    // Reset filters
    $('#reset-filter').on('click', function () {
        $('#source-version, #target-version').val('all');
        rows.forEach(item => {
            item.row.removeClass('filtered');
        });
    });
});
