
Community Engagement Guidelines 
=======================================

Below is a list of guidelines for maintainers, key contributors and Mattermost, Inc. staff to use when engaging with the broader community in forums, GitHub issues, Twitter, our Mattermost servers and other places of online conversation. 

Best Practices 
============================================================================

1. Don't offer advice on database modification without a clear warning
----------------------------------------------------------------------------

Never give DB advice without a warning similar to: 

``Manual database modification bypasses checks in the code and could make a system unrecoverable. It's not recommended and if you do make a change, make sure to back up your DB, and verify changes carefully.``

2. Answer with docs
----------------------------------------------------------------------------

When answering a common question, always include a link to the docs so the person asking--along with people in future who read your response--has a reference. If no doc exists, do one of two things: 

1. Add the documentation, then answer the question with a link to the information, or 
2. Answer the question and open a ticket for the missing information to be added to docs.

During the triage process, if the information missed should have obviously been included, assign the ticket to the last approver for the doc PR, otherwise assign to doc PR author. 

3. Avoid speculation 
----------------------------------------------------------------------------

Circumstances change frequently. Don't set expectations for something that you're not 100% sure will happen. If it doesn't happen, people will be more upset than if you didn't say anything. 

For example, if you haven't seen a feature merged into a specific product in a specific edition, don't tell people the feature will be in until you see it merged. 



Speaking in the Voice of Mattermost 
============================================================================

Mattermost serves a global audience, who might not use English as their first language.

To keep Mattermost “obvious” to users, please keep community discussion, documentation and on-screen help simple, effective and ready-to-translate.

**Simple** 

- Aim for the reading ability of an 11-year old. Use short sentences. Avoid large words.

**Effective**

- Start with what’s important, and leave less important details to the end, or omit them.
- Focus on achieving understanding in the reader, over total correctness or completeness.

**Ready-to-translate**

- Avoid slang.
- Avoid Western-centric, or culture-centric examples (example: instead of “fiddle with settings”, say “adjust settings”).

If you’re not sure, try using machine translation to turn your content into a foreign language then back into English.

Machine-Translation Example:
------------------------------------------------

Here’s an example of culture-specific content with the word “fiddle” (meaning “to adjust repeatedly”):

  There are a few configuration settings you might want to fiddle with when setting up your instance of Mattermost.

That documentation machine-translated into German and then back into English looks like this:

  There are some configuration settings you could know if your instance Matter Most violin.

The sentence would be more ready-to-translate to say “There are a few configuration settings you can adjust when setting up your instance of Mattermost.”

Testing our documentation:
------------------------------------------------

One technique to use to review content is to ask: “How would Agent Coulson explain this concept to Thor?” [1]

Agent Coulson takes complex ideas and explains them simply and effectively. Thor isn’t from earth, so we have to filter out ideas that are culturally specific-–fiddles, baseball, wedding rings, etc.--and that makes things easy-to-translate.

As a communications company, clarity matters. If you see content that doesn't speak in the "Voice of Mattermost", we’d gladly accept issue reports and pull requests.

[1] This example relies on knowledge of the 2012 movie "Avengers", which we consider a "global" reference, not a culture-specific reference, since it achieved `record-breaking sales <https://en.wikipedia.org/wiki/The_Avengers_(2012_film)>`__ around the world--in the United States, Mexico, Brazil, Ecuador, Bolivia, Taiwan, the Philippines, Hong Kong, the United Arab Emirates, Argentina, Peru and Central America, among other regions. 


