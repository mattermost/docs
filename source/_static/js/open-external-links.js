/*
This script ensures that all external links (those with the 'external' class)
open in a new tab or window by setting their 'target' attribute to '_blank'.
*/
document.addEventListener("DOMContentLoaded", function() {
    // Select all anchor tags with the 'external' class
    var links = document.querySelectorAll('a');
    for (var i = 0; i < links.length; i++) {
        var link = links[i];
        // Check if the link has the 'external' class
        var isExternal = link.classList.contains('external');
        if (isExternal) {
            // If it's an external link, set the 'target' attribute to '_blank'
            // This makes the link open in a new tab/window when clicked
            link.setAttribute('target', '_blank');
        }
    }
});
