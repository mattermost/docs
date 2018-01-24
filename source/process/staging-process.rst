=====================
Staging Process
=====================

This document outlines the process that should be used to push staging, in order to avoid the following issues:

 - There is no way to tell if people have work in progress in staging.
 - It is unclear when/how often we push staging, which can then lead to bugs not being pushed live soon.

All members in the marketing team should be aware of the following steps:

1. Every time somebody makes an update on staging, post to the Marketing: Website channel starting with the web hashtag and a description of the change made. An automation process has been set up so that anything that starts with `#web` posted in the Marketing: Website channel will be added to a spreadsheet for tracking.
 - If the edit is something that will take a while, post when you start making an edit so that other people have visibility into what you are doing.
 - If you publish an update, make sure you preview it before publishing and do a quick test to make sure there are no issues/bugs.
 
2. All changes go through Asaad, unless it is something minor such as editing text or creating a new text-based page.
 - If something breaks, limiting or revoking wordpress permissions until there is a development environment might be proposed.
 
3. Start pushing staging daily if changes were made. After staging push, make sure to:
 - Update the Recapthca keys in the Trial page in production.
    - Go to `Forms` -> `Settings` -> apply these keys:
        `6LeBaz4UAAAAAK3pfaOM0EKl-4ytidGheU16U6yj` (top)
        `6LeBaz4UAAAAAAUPesMvczuP6knCm4C9F3m8wlTn` (bottom)
 - Scout the main pages located in the header and footer in the website for any bugs and broken links.
