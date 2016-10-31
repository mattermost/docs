====================================
Mattermost Documentation Style Guide
====================================

The Mattermost documentation must be of high quality. It must be accurate and clear, and be presented with a style and tone that is appropriate for technical content. People who use Mattermost rely on the documentation to get their jobs done. We don't want to see an installation of Mattermost delayed because the documentation has an error or is difficult to understand.

The style and tone must be consistent throughout the documentation. People need to feel confident that what they're reading is carefully attended to by its creators.  and that we have taken care and have paid attention to detail. 


Goals of the style guide
========================




Document Structure
==================

The reStructuredText specification allows for a certain degree of flexibility in the use of overline and underline characters to delineate sections. However, for consistency and ease of use, the Mattermost documentation will use the following convention:

Page title: overline and underline character will be the = character. For example:
===============
Creating a team
===============
equivalent to H1

Level one headings: ============ (h2)
Level two headings: ------------ (h3)
Level three headings: ^^^^^^^^^^^^^ (h4)

Note that in a properly chunked set of documents, with only one topic per file, you should never need more than two section levels: One for the page title, and one for each section on the page. However, we can't all reach Nirvana at once, so feel free to use sub sections if they're needed.

filepath - monospace (directory paths, file names)
inline code - monospace
code block - monospace
Menu selection - bold
UI selection - bold (includes buttons and links, names of controls, field names)
text that user enters - monospace
references - italic

relative links only, except of course for pages that are external to the docs

Main screen, Navigation panel, Message Details panel

main menu? 3-dot menu? three dot menu?

how to link to other documents. ie, not click here

should be no need for section breaks, ie ---------- that gets output as <br>

avoid documenting features; instead, document tasks. describe things that people want to do

simple sentences, less than 25 words.

Cross references
^^^^^^^^^^^^^^^^

Use cross references carefully.
