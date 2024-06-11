/*
This script is used to open external links in a new tab.

All the internal site-wide links will open in the same tab.
The links that direct the user to an external website will
open in a new tab.
*/

document.addEventListener('DOMContentLoaded', (event) => {
    const internalLinks = location.host;
    document.querySelectorAll('a').forEach((link) => {
        if (link.host !== internalLinks) {
            link.setAttribute('target', '_blank');
        }
    });
});