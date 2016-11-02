====================================
Mattermost Documentation Style Guide
====================================

This is the Mattermost style guide for documentation. It acts as a reference for writers and editors to ensure that the Mattermost documentation is consistent and clear.

The style guide is definitely *not* intended to slow down or otherwise impede contributions, which are always welcome. No contribution will be rejected due to non-conforming style. Don't worry if you don't have time to read and comply with the guide; submit your work anyway.

The Mattermost documentation must be of high quality. It must be accurate and clear, and be presented with a style and tone that is appropriate for technical content. People who use Mattermost rely on the documentation to get their jobs done. We don't want to see an installation of Mattermost delayed because the documentation has an error or is difficult to understand.


The reStructuredText specification allows for a certain degree of flexibility in the use of overline and underline characters to delineate sections. However, for consistency and ease of use, the Mattermost documentation should use a single convention for title underlines.


Use the = character for the overline and underline. For example:

::
  
   ==================
   Document structure
   ==================

Note that unlike Markdown, overlines and underlines in reStructuredText must be at least as long as the title text.

Section titles
==============

If your document has more than one section, use the = character for the section title underline. For example:

::
  
  Section titles
  ==============

Note that in a properly chunked set of documents, with only one topic per file, you should never need more than two section levels: One for the page title, and one for each section on the page. However, we can't all reach Nirvana at once, so feel free to use subsections if they're needed.

If you do need subsections, use the following underline characters:

::
  
  Subsection One
  --------------
  
  Subsection Two
  ``````````````


relative links only, except of course for pages that are external to the docs

Main screen, Navigation panel, Message Details panel

main menu? 3-dot menu? three dot menu?

how to link to other documents. ie, not click here

should be no need for section breaks, ie ---------- that gets output as <br>

avoid documenting features; instead, document tasks. describe things that people want to do

simple sentences, less than 25 words.

Steps: Each step should describe one action. Each step should be a complete sentence.

avoid noun clusters. that is, three or more nouns in a row

Use might or can instead of may. use 'may' only when giving permission. 

Cross references
================

Use cross references carefully.
