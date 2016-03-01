FX Guidelines
========================

The purpose of the Mattermost Fan eXperience Guidelines ("FX Guidelines") is to deliver a level of usability and consistency that turns users of Mattermost software into fans of the Mattermost experience.


---------------------------

|

Design Principles
************************

“Fast, Obvious, and Forgiving” – These principles define the standard we’re setting for the Mattermost experience:

Fast
-----------------------------------

Fast has two parts: being _responsive_ and being _quick_.

**Responsive** means when a user clicks, taps, types or otherwise enters input we give immediate feedback that the input is received and something is happening. It could be a spinner animation, or just some text saying “Loading”, but something always responds to the user.

**Quick** means things happen as soon as they can. Loading pages, sending messages, receiving notifications and other vital actions should be automatically benchmarked for performance. Bugs should be opened on performance regressions.

Obvious
-----------------------------------

Obvious means users are never confused. Across product features, interface layout, labeling, help text, and documentation, it is critical that everything we offer makes sense in the mind of the user, even if it means oversimplifying how things technically work.

If a user doesn’t understand how to use a feature, all the underlying effort and code is wasted. The “Obvious” design principle also flows through to our [Documentation Guidelines](http://www.mattermost.org/documentation-guidelines/).

Given [Hick’s Law](https://en.wikipedia.org/wiki/Hick%27s_law), core functionality should be apparent, and advanced functionality should be possible via sub-menus and well documented and tested.

Functionality that is not fundamental to the product purpose should be ruthlessly omitted.

Forgiving
-----------------------------------

Forgiving means there’s no such thing as user error–-it’s always the fault of the product. This mindset means we can fix problems coming from users making unexpected decisions. Fixes could be through user interface improvements, adjustments to help text, or helping users recover when things go wrong–adding undelete, undo and rolling back for example.

Forgiving extends to compatibility as well, and whether you’re working from a PC, phone or tablet, Mattermost should adjust to reasonably serve your device, screen size, and major browser type.

|
---------------------------

|

Markup Guidelines
************************

|
Bootstrap Classes
-----------------------------------

Since we’re using [bootstrap](<http://getbootstrap.com/), try to utilize [bootstrap classes](<http://getbootstrap.com/css/>) as much as possible rather than creating new styles or using inline styles.

Custom Styles
-----------------------------------

We’re using [BEM methodology](https://en.bem.info/method/) and would advise everyone to do so when creating new classes or ids. There’s a lot of places in our app that currently don’t follow BEM but we’re trying to improve the codebase. [Here](http://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/) is a brief overview of the BEM syntax.


|
---------------------------

|

UI Elements
************************

|
Header Notification
---------------------------

Appears as an additional header at the top of the UI. May include an “x” button to dismiss. Limited to 60 characters. May include a time-out. Header notification should appear over the rest of the UI instead of pushing the UI down. Multiple header header can appear, with the earliest notification at the top and more recent notifications appearing underneath.

**Desktop**

..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/header1.png
    :alt: Header Notification Desktop

**Mobile**

..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/header2.png
    :alt: Header Notification Mobile

There are several modes for this element:

    **System-Wide Header Notification:**

        | Triggered on login. Includes “x” button to dismiss. No timeout. Removed when system admin cancels.
        |
        | Examples:
        | “Try our new Windows App. Click here to download.”,
        | “Scheduled maintenance 2:00am to 2:30am starts in 20 minutes, 3 seconds.”

        |

    **Action Required Header Notification:**

        | Triggered on login. No “x” button to dismiss. No timeout. Dismissed when action completed.
        |
        | Examples:
        | “We’re evolving. Please review and accept our new terms of service.”

        |

    **Persistent Error Header Notification:**

        | Triggered on error. No “x” button to dismiss. Dismissed when error no longer persists.
        |
        | Examples:
        | “You are not connected to the internet.”

|
---------------------------

|
Confirmation Messages
---------------------------

| Confirmation messages should look like this and should appear below the button that triggered them or at the top of the screen.
| Example:
| "Link copied to clipboard"
|

..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/confirm1.jpg
    :alt: Confirmation message

|
---------------------------

|
Saving Settings
---------------------------

| **Save Prompt**
| A prompt should appears if a user makes changes to a setting and attempts to navigate away without saving them.
|

..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/save1.png
    :alt: Save Prompt

|
---------------------------

|
Icons
---------------------------

1. When to use icons
    a. When there’s not enough space for the label and an icon can easily represent the label.
    b. When an icon can help the user more quickly understand a feature.

2. When not to use icons
    a. When the term/phrase is too specific or complicated.

3. Testing
    a. File a bug if the icon is difficult to understand or has cosmetic defects (size, blur, etc.)
    b. File a bug when an icon doesn’t obviously indicate the underlying feature

|
---------------------------

|
Input Hints
---------------------------

**Fieldname:**

    The labels on input fields should be as obvious as possible for the intended user.

    Incorrect:
        Handle: The name of the subdirectory used to navigate to a channel using the site URL appended with the handle name. Must use only valid URL inputs

    Correct:
        Channel URL: The web address used to reach your channel.




**Help text:**

    Text below an input field should clearly and concisely describe the PURPOSE of the input.

    In general, avoid describing the technical requirements of the field in Help Text, and use Placeholder input text, field validation and error messages to convey requirements.

    The exception to this guideline is if requirements are non-obvious, such as passwords needing different numbers of characters, symbols, etc.


**Placeholder input text:**

    Show examples of valid input, such as “name@example.com” for email addresses, as well as examples of functionality that is not obvious supported, for example in inputting team name, offer placeholder input text with “Example: Marketing, John’s Room, 中国业务”.


**Field validation:**

    Use field validation to help “prevent or correct” any mistakes a user might make.

        Example: If a field has a maximum of 22 characters, don’t allow the user to enter more than 22 characters in the field.

        Example 2: If a user enters invalid uppercase letters and spaces for a URL, show an error message and also offer a correction, substituting dashes for spaces and lower case letters for uppercase letters, so the user can resubmit immediately with valid input.

**Error messages:**

    Error messages should appear immediately below input fields and offer clear and concise information about why an input cannot be accepted.

    Error messages should aesthetically appear helpful, and not punishing.

    Error messages do not need to explain every error in a bad input, just clearly explain one error, and allow for that to be corrected before displaying next error, example: If an input is both short and contains invalid characters, show just the message about input being too short FIRST, and if the field isn’t valid on the second attempt, show the invalid character error message.

|
---------------------------

|
Input Fields
---------------------------

Users should enter information into fields without much thinking.

| ENTER button on last input field should trigger default dialog button.
| When last input field in a series has focus and user hits ENTER it should trigger the default button in the dialog.
|
Example:

    Correct:
        Having focus on last input field in dialog (“Miller”) and hitting ENTER triggers default dialog button (“Send Invitations”)

        ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/inputField1.png
            :alt: Input Field Enter
            :width: 500 px

    |

We should use radio buttons/checkboxes for input options rather than custom bootstrap on/off switches.

Example:

    Correct:
        Having radio buttons for input options.

        ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/inputField2.png
            :alt: Radio Buttons
            :width: 500 px

|
---------------------------

|
Button Placement
---------------------------

| **Dialog BOTTOM RIGHT BUTTONS should be either “Close”, or “Cancel” and [ACTION_BUTTON].**
| If there’s one button on the bottom right, it should be “Close”, if there are two, the one on the left should be “Cancel” and the one on the right should be an [ACTION_BUTTON], like “Save” or “Send Invitations”.

Example:

    Correct:
        Single button at the bottom right should be “Close”.

        ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/buttonPlacement1.png
            :alt: Button Placement 1
            :width: 500 px

    |

    Correct:
        When there are two buttons on bottom right, left button should be “Cancel” and the button on the right should be the [ACTION_BUTTON], in this case “Send Invitations”.

        ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/buttonPlacement2.png
            :alt: Button Placement 2
            :width: 500 px

    |

    Incorrect:
        When there are two buttons at the bottom right, left button should not be “Close”, as it’s not clear if closing will or won’t execute the [ACTION_BUTTON].

        ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/buttonPlacement3.png
            :alt: Button Placement 3
            :width: 500 px

|
---------------------------

|
Number of choices
---------------------------

To simplify decisions, when practical, limit the number of choices to 3 or 4, and add separators or headings between logical groups. See Hick’s Law for background on why this helps: https://en.wikipedia.org/wiki/Hick%27s_law

Example:

    Incorrect:
        No clear separation between distinct options.

        ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/choices1.png
            :alt: No separation
            :width: 500 px

    |

    Correct:
        A clear separation between distinct options.

        ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/choices2.png
            :alt: Clear separation
            :width: 500 px

|
---------------------------

|
Alignment of Elements
---------------------------

| **Elements should feature margins horizontally and vertically, evenly spaced.**
| Create space between elements, such as buttons, text, line separators, headers and backgrounds, by leaving even space around them (either equal space or at most 1 pixel difference).
|
Example:

    Correct:
        Button positioned in the middle of the header.

        ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/align1.jpg
            :alt: Button positioning
            :width: 500 px

    |

    Correct:
        Error message does not expand the horizontal separator

        ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/align2.png
            :alt: Confined messages with respect to width
            :width: 500 px

|

**Horizontally align multi-line elements along a vertical line.**

Example:

    Correct:
        Roles right justified with respect to the text and irrespective of the icon.

        ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/align3.jpg
            :alt: Vertically justified
            :width: 500 px


|

| **Instructions should be sentences, one-line links should be fragments.**
| Instructions, such as “A password reset link has been sent to you@email.com for your account.\nPlease check your inbox.”, should be displayed as sentences ending in periods. One-line links, such as “Find it here”, should not end in periods or commas, but question marks are okay.
|
Example:

    Incorrect:
        Instruction “Please check your inbox”, didn't end with a period.

        ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/align4.png
            :alt: Period Missing
            :width: 300 px


    |

    Correct:
        Instruction “Please check your inbox”, ended with a period.

        ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/align5.jpg
            :alt: Period added
            :width: 300 px

|
---------------------------

|
Reduce obvious steps
---------------------------

If what the users need to perform is obvious, we should make concious decisions and reduce some of the steps involved in that process.

Examples:

    Clicking on the search icon on mobile should focus the search bar when it slides in.

    ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/reduce1.png
        :alt: Search mobile

    |

    Clicking on the reply icon should move the focus to the comment box in the RHS.

    ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/reduce2.png
        :alt: Reply icon

    |

    Switching channels should move the focus to the post box in the center channel.

    ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/reduce3.png
        :alt: Switching channels


|
---------------------------

|
Input behaviours
---------------------------

All inputs such as textareas should behave consistently, if the default behaviour is to perform an action on "Enter", then all inputs for eg: The center channel post input, the comment thread textarea, the edit header modals etc should be consistent with that behaviour and perform an action on "Enter".

Examples:

    If pressing "Enter" posts a message in the center channel post input.

    ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/inputBehaviour1.png
        :alt: Center channel post area

    |

    Then pressing "Enter" in the comment thread textarea should also post a comment.

    ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/inputBehaviour2.png
        :alt: Comment thread textarea

    |

    And other textareas or inputs should also perform their primary action when "Enter" is pressed, here's an example of the "Edit Header" modal.

    ..  image:: https://raw.githubusercontent.com/mattermost/docs/master/source/images/inputBehaviour3.png
        :alt: Edit header modal
        :width: 500 px


|
|
|