==================================================
Onboarding
==================================================

This document is intended for new hires to summarize norms for working at Mattermost, Inc. including:

- `Getting Started Checklist`_ - Getting ready to work here
- `Meetings`_ - When we get together and why
- `Mindsets`_ - Shared toolsets we have for solving problems
- `Terminology`_- Shared vocabulary to convey ideas quickly
- `Training`_ - Material available to help us ramp quickly in different areas

.. contents::
    :backlinks: top

---------------------------------------------------------
Getting Started Checklist
---------------------------------------------------------

Important things to know
---------------------------------------------------------

- Never sign any agreement on behalf of the company. The CEO is the only person authorized to sign an agreement on behalf of Mattermost, Inc. The only exception is that you are authorized to sign a non-disclosure agreement to enter a physical space. If you have questions, please check with your manager. 

Hiring
---------------------------------------------------------

- (People Ops & New Hire) Offer letter accepted via click-sign
- (Logistics) Mail t-shirt & track jacket

T-minus 1-3 weeks
---------------------------------------------------------

- (People Ops & New Hire) People Ops should find out new hire's preference for laptop, either to be purchased or taken from stock and shipped by People Ops or purchased locally by new hire and expensed. Windows laptops generally cost less than Macs so budget is based on Macs. For non-developers, budget is cost of a Macbook in your local area, for developers budget is cost of a Macbook Pro. Since these items are company property, you do not need to buy insurance or extended warranties for them, but you do need to report any loss or damage to People@mattermost.com as soon as it occurs.
- (New Hire) Read the entirety of Onboarding page for info on meetings, mindsets, terminology and training materials.
 
T-minus 1 week
---------------------------------------------------------

- (People Ops) Send email invite to New Hire to set up an @mattermost.com email address. New Hire should use this email address on pre-release.mattermost.com (replace personal email with company email if already registered there). `FIRST_NAME@mattermost.com` is the standard naming convention.

- (People Ops & New Hire) Set up payroll. Non-US Employee/Non-Canada Employee, complete bank info form for monthly wire transfer.

First Day
---------------------------------------------------------

- (Manager) Posts welcome message in stand-up channel
- (Manager) Meets New Hire for first 1-1 meeting
- (Buddy) Meets New Hire for first 1-1 meeting
- (CEO) Meets New Hire for welcome meeting 
- (New Hire) Confirm with Manager all HR paperwork is completed by end of first day (should have been sent in advance). 

---------------------------------------------------------
Meetings
---------------------------------------------------------

This section summarizes norms for public and private meetings for the Mattermost community and for Mattermost staff (people paid by Mattermost, Inc.).

Timezones 
---------------------------------------------------------

When proposing meetings use famous cities as references for time (e.g. 9am New York time), since it's clear and `easy to web search <https://www.google.com/search?q=time+in+new+york&oq=time+in+new+&aqs=chrome.1.0l2j69i57j0l3.3135j0j7&sourceid=chrome&ie=UTF-8>`_. Avoid using "UTC", as it has been shown to cause confusion.

When selecting a timezone city, use the most well-known city in a country where at least one team member is located. Exception: When possible, use a city where we have an official mailing address, e.g. In Western Americas use Palo Alto, instead of San Francisco. In Eastern Americas use Toronto, instead of New York. 

Scheduling Recurring Group Meetings
---------------------------------------------------------

Recurring meetings with more than two people should have one or more regular slots on the calendar reserved so that meetings can be coordinated in a straight-forward way. 

1. Meetings with internal colleagues should be coordinated by checking everyone's availability in G Suite Calendar. 
2. Meetings with external colleagues should be coordinated manually with one internal person coordinating everyone's G Suite Calendars 

For efficiency, when Mattermost works with advisors and consultants who engage with 2 or more internal team members, we aim to schedule meetings in regular slots (or a collection of regular slots) 2-4 weeks apart. 

Open Meetings
---------------------------------------------------------

Developer Meeting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Open to the public** - (Developers - 1-2 hours/week) Wednesdays 10:00 (`San Francisco Time <http://everytimezone.com/>`_)

- Goal: Discuss developer issues across Mattermost staff, key contributors and the contributor community.
- Attendees: (required) Mattermost staff developers, (optional) key contributors, contributors and anyone who would like to join.

Procedure:

1. (Chair): Post meeting agenda in `Developers channel <https://pre-release.mattermost.com/core/channels/developers>`_ (open to the public), tagged with ``#devmeeting``
2. (Team and Public): At the time of the meeting:

      - Join the **Hangouts** link posted in the meeting agenda in the `Developers channel <https://pre-release.mattermost.com/core/channels/developers>`_

To review past agendas for the Developer meeting in the `Developers channel <https://pre-release.mattermost.com/core/channels/developers>`_ click on the ``#devmeeting`` hashtag in any of the meeting notes, or search for it directly.


Mattermost Staff Meetings
----------------------------------------------------

For confidentiality of customers, internal process meetings are limited to Mattermost staff only.


Sprint Planning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Mattermost staff only** - (Developer - 5-10 minutes/week) Tuesdays between 10:00 and 11:00 (`San Francisco Time <http://everytimezone.com/>`_)

- Goal: Review and discuss tickets selected by developer for next sprint
- Attendees: (required) Each developer in sequence, plus spint planners (one dev, one PM), (optional) Mattermost staff colleagues welcome

Note:

- This meeting uses a special `Mattermost staff-only BACKLOG query <https://mattermost.atlassian.net/secure/RapidBoard.jspa?rapidView=1&view=planning.nodetail&quickFilter=7>`_ showing tickets by sprint, with tabs across the top for each developer
- Prior to meeting, developers drag and drop tickets from their backlog to next sprint based on team priorities
- Developers are welcome at any time to discuss reassigning tickets with colleagues using common sense (if both are okay with the change, add "triage" tag to fix version with comment and triage team will review to make the change)
- During the meeting, developer's next sprint is reviewed, discussed, possibly adjusted and locked

Procedure:

1. (Chair): Just prior to meeting, post **Hangout** link in `Standup private channel <https://pre-release.mattermost.com/private-core/channels/stand-up>`_
2. (Developer): Replies in Standup private channel when sprint is ready for review
3. (Chair): Will (at)mention next developer to join **Hangout** to review tickets. Developer joins, tickets are discussed and finalized for next sprint. Developer leaves **Hangout** and next developer rotates in.

Triage Meeting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Mattermost staff-only** - (Triage team - 1-3 hours/week) Monday, Wednesday, Friday 09:00 (`San Francisco Time <http://everytimezone.com/>`_)

- Goal: To provide consistent review, prioritization and ownership assignment of all tickets
- Attendees: (required) dev and PM from Mattermost staff, typically leads (optional) other Mattermost staff welcome

Note:

- ONLY TRIAGE TEAM should set or change the **Fix Version** of a ticket.

    - When tickets are first created, they go to triage to be reviewed for clarity and priority and assigned a **Fix Version**. Unclear tickets may be assigned to their creator for more information.
    - The **Fix Version** determines the sequence in which tickets are addressed and triage team is accountable for that sequence.

- If you're ever unsure about a ticket (if it's not clear, or doesn't seem appropriate) add a comment and add **triage** to the **Fix Version** field, which will trigger a review by the triage team in 1-2 working days.

    - It's the responsibility of the triage team to make sure tickets are clear before they're assigned a **Fix Version**.

- ONLY TRIAGE TEAM can close a ticket resolved as **Won't Fix** or **Won't do**

    - These tickets resolved in such a way are reviewed by triage team.
    - Only resolve a ticket as **Won't Fix** or **Won't Do** if you're highly confident it's the correct decision, otherwise, add "triage" to Fix Version for review. In either case, include a comment with your reason.

Procedure:

1. (Chair): Just prior to meeting, post **Hangout** link in `Standup private channel <https://pre-release.mattermost.com/core/channels/stand-up>`_ (Mattermost staff only)

2. (Attendees): Join the link

3. (Attendees): Review `query for tickets needing triage <https://mattermost.atlassian.net/browse/PLT-1203?filter=10105>`_ and assign owner and fix version

Leads Meeting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Mattermost staff-only** - (Leads - 1-3 hours/week) Monday and Wednesday (9:00 `San Francisco Time <http://everytimezone.com/>`_)

- Goal: Address leadership and process topics
- Attendees: (Required) Dev, PM, community/marketing leads from Mattermost staff, with sales lead and other Mattermost staff optional. 

Note:

- Decisions should go to Leads meetings when there is lack of clarity or ownership, or to discuss special case topics where process is not well defined. 

    - When possible, decision-making should belong to the people closes to details
    - Individual developers or PMs should make most decisions, and raise to developer or PM team if things are unclear, and go to Leads if lack of clarify persists.

- To queue an item for Leads ask the dev or PM lead

- Leads is also used for cross-discipline Q&A

    - Rather than randomize individual contributors, cross-discipline discussion (e.g. marketing to PM, community to dev, etc.) can happen in leads

Procedure:

1. (Leads): Queue items in Leads channel for discussion. 

2. (Leads): During meeting discuss agenda items in sequence. 

Platform Meeting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Mattermost Inc-only** - (Product Staff - 1 hour/week) Thursday's at 10:00 (`San Francisco Time <http://everytimezone.com/>`_).

Regular team meeting for product staff team at Mattermost Inc.

- Goal: Increase team output by effectively reviewing priorities and finding blindspots
- Scope: Mattermost Inc-only meeting given confidential customer issues discussed
- Attendees: Mattermost Inc colleagues working on mattermost-server and mattermost-webapp

Platform meeting consists of two parts, Team Operation Review Meeting and Product Staff Meeting.

All Mattermost staff attends the Team Operation Review Meeting. It provides an opportunity to teach and learn between people who don’t otherwise deal with each other much. Includes presentations and demos.

Only the product team attends the Product Staff Meeting, others' attendance is optional. The meeting consists of people who work closely together. Includes controlled agenda items (e.g. queued items) with an "open session" where staff can bring up anything they want. Staff should arrive at decisions during the meeting or schedule further discussion for the next meeting.

Procedure:

1. (Chair) 3-hours before standup, post reminders in `Platform Meeting private channel <https://pre-release.mattermost.com/core/channels/platform-meeting>`_ (Mattermost Inc only)

::

   #### @channel Platform Meeting Reminder
   Everyone please:
   - **Prepare your demos**
   - **Prepare your roundtable open discussion**

   @[RELEASE MANAGER] please:
   - **Prepare your roadmap checkin**

   @[WHOEVER] are you ready for your "Ice-breaker"?


2. (Team) At time of meeting:

   - Join the **Hangout** link in the header of the `Platform private channel <https://pre-release.mattermost.com/core/channels/platform-discussion>`_
   - Open the **Notes** link in the header to see the agenda

3. (Vice-Chair) Post `"Standing Items" template <https://docs.google.com/document/d/1ImSgkF7T03wbKwz_t4-Dr4n3I8LixVbFb2Db_u0FmdM>`_ into Platform Meeting Notes

    - Add **Follow-ups** from previous meeting
    - Add **New items** queued in `Platform private channel <https://pre-release.mattermost.com/core/channels/platform-discussion>`_ (Mattermost Inc only)

Meeting Agenda:

Team Operation Review Meeting

- **Warm-up** - Currently: "Share something interesting about your weekend."
- **Roadmap check-in** - Review of roadmap status in current and next release
- **Demos (optional)** - Team members show highlights of what's been completed this week. Relevant follow-ups noted.
- **New items** - New team relevant items are discussed

Product Staff Meeting

- **Roundtable Open Discussion** - Each colleague shares something important to discuss with the team. Examples: external customer or user issue, potential process improvement. Follow-ups noted.
- **New items** - New product staff relevant items are discussed
- **Follow-ups** - Follow-ups from previous meeting are discussed
- **Questions** - To find blindspots, meeting does not end until 3 open questions are asked and answered.

Post Meeting:

- Follow-up items are posted to the  `Platform private channel <https://pre-release.mattermost.com/core/channels/platform-discussion>`_ (Mattermost Inc only)

Meeting Elements
-----------------------

Here we summarize meeting elements that can be re-used for meetings across teams.

Warm-ups
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- 2-3 minute exercises designed to learn more a colleagues at the start of a recurring meeting
- Typically rotates alphabetically by first name, one colleague per meeting
- Examples:

   - "Hobby talk" - sharing about an interesting hobby, past or present
   - "My home town" - sharing something interesting about where you grew up
   - "Two truths and a lie" - share two true facts about yourself and one lie, team guesses which is the lie.

Open Questions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Exercise to find blindspots in team thinking at the end of a meeting
- Meeting does not end until 3 questions are asked and answered, typically at least one of the questions reveals a blindspot or opportunity to improve communication.
- Examples of questions:

    - "What's the status on X?" // often an important item that got forgotten
    - "Who owns X?" // reveals need for more clarity or communication
    - "Why do we do X?" // let's us verify if a process is needed, and if we're handling it the right way



-----------------------------
Mindsets
-----------------------------

Mindsets are "tool sets for the mind" that help us find blindspots and increase performance in specific situations. They're a reflection of our shared learnings and culture in the Mattermost community and at Mattermost Inc.

To make the most out of mindsets, remember:

- **Mindsets are tools** - Use common sense to find the right mindset for your situation. Avoid using ones that don't fit.
- **Mindsets are temporary** - Try on a mindset the way you'd try a tool. You can always put it down if it doesn't work.
- **Mindsets are not laws** - Mindsets are situation-specific, not universal. Don't use them to debate.

When you read about great leaders, they share mindsets relevant to success in their specific situations, which differ from their peers. Remember that "advice is personal experience generalized" so be mindful about what you apply.

In this context, here are mindsets for Mattermost:

Learn, Master, Teach
---------------------------------------------

**Learn** a new topic quickly, develop **mastery** (be the smartest person at the team/company/community on the topic), then **teach** it to someone who will start the cycle over.

If you're a strong teacher, their mastery should surpass yours. This mindset helps us constantly grow and rotate into new roles, while preventing "single-points of failure" where only one person is qualified for a certain task.

Slow is smooth, smooth is fast
---------------------------------------------

When you rush to get something done quickly, it can actually increase the time and cost for the project.

Rushing means a higher chance of missing things that need to be done, and the cost of doing them later is significantly higher because you have to re-create your original setup to add on the work.

Emotion, Assumption, and Priority
---------------------------------------------

Consider when two rational people disagree, the cause often comes from one of three areas:

1. **Emotion** - There could be an **emotion** biasing the discussion. Just asking if this might be the case can clear the issue. It's okay to have emotions. We are humans, not robots.

2. **Assumption** - People may have different underlying **assumptions** (including definitions). Try to understand each other's assumptions and get to agreement or facts when you can.

3. **Priorities** - Finally people can have different **priorities**. When everyone's priorities are shared and understood it's easier to find solutions that satisfy everyone's criteria.

While the emotions, assumptions, priority mindset won't work for everyone in every case, it's helped resolve complex decisions in our company's history.


Likes & Wishes
---------------------------------------------

An easy way to check in with team members about how things are going.

- What do you *like* about how things are going?
- What do you *wish* we might change?

Use these one-on-one or in a group as a way to open conversations about what to keep and what to change in how we do things.


Mini-boss, End-boss
---------------------------------------------

When reviewing user interface design, pull requests, or marketing materials, there are ideally two reviewers:

- **Mini-boss**: Reviewer with less experience to do the first review
- **End-boss**: More experienced reviewer to do the final review

This system has several benefits:

1. The Mini-boss provides feedback on the most obvious issues, allowing the End-boss to focus on nuanced issues the Mini-boss didn't find.
2. The Mini-boss learns from the End-boss feedback, understanding what was missed, and becoming a better reviewer.
3. Eventually the Mini-boss will be as skilled at reviewing as the End-boss, who will have nothing futher to add after the Mini-boss review. At this point, the Mini-boss becomes an End-boss, ready to train a new Mini-boss.


Medic, Field Surgeon, Plastic Surgeon
---------------------------------------------

When making project investment decisions we optimize for high impact in the context of customer obsession, empowered by ownership, while being constrained by "be proud of what you build". 

The failure case is over-investing in processes and infrastructure, stealing mana from higher priority work, reducing speed and agility for the company, and unnecessarily increasing cost and bureacracy. 

In making these trade-offs, consider the following mindsets:

- **Medic** 

   Fix something that's important, broken and dangerous as fast as possible. Speed is critical, do not care about "leaving a scar" in our architecture or business process, just own it and get it done. Solve the problem, DO NOT OVER BUILD.
 
   *Example:* Something incorrect on our public website with more than 100,000 page views a month should be fixed immediately and not put on a queue tied to a longer term project. 

- **Field Surgeon** 

   Triage things that are important, broken but not dangerous, and fix the most important things with a minimum of time and cost. Scarring should be a low-priority consideration--it is fine to leave scars and it is fine to spend a little energy to avoid big ones.  Solve the problem for the next stage of growth, but don't solve if to two to three stages ahead. 

   *Example:* In Mattermost, spend 2 mana to enable automated messages over 4000 characters to be broken into multiple posts instead of being rejected, which is a problem every developer hits when they attempt to output log information via curl commands.

- **Plastic Surgeon** 

   Fix and optimize critical, high volume flows in our customer experience and product with heavy investment if needed to make high impact changes. Scars can be avoided and removed to produce a high impact result.  

   *Example:* Click-tracking traffic on Mattermost.com and optimizing flows to direct visitors to convert into contact and purchase actions. 

--------------------------
Terminology
--------------------------

Designing world-class software means bringing people together across disciplines and cultures. We want to create a limited amount of shared terminology to help us work better together, while being careful not to make it difficult for newcomers to follow our conversation.

Perhaps in future we'll have a bot that helps teach newcomers about the terminology in-context. Until then we have this guide.

Purpose
---------------------------

We use Mattermost terminology to achieve specific benefits:

1) Increase precision through unambiguous definitions of useful terms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For example, "0/5" and "5/5" help convey the level of conviction behind an opinion. Also, a precise classification of tickets as "Bug" or "Improvement" is critical since it affects scheduling and decision making, and so forth.

2) Increase the speed of communication via a small number of frequently used acronyms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`LHS`_ and `RHS`_ are examples of a very limited number of acronyms to use to speed discussions, specifications, and ticket writing.

3) Reduce repeated mistakes by naming very specific undesirable behaviors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Naming specific repeated mistake helps us find patterns, avoid repeated mistakes in future, and helps newcomers avoid making similar mistakes as they learn our organization's terminology.

List of Terms
---------------------------

0/5, 1/5, 2/5, 3/5, 4/5, 5/5
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use "x/5" to concisely communicate conviction. 0/5 means you don't have a strong opinion, you are just sharing an idea or asking a question. 5/5 means you are highly confident and would stake your reputation on the opinion you're expressing.

Bug
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An obvious error in Mattermost software. Changes required to accommodate unsupported 3rd party software (such as browsers or operating systems) are not considered bugs, they are considered improvements.

Dead Tarzan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Discarding an imperfect solution without a clearly thought out and working alternative. Based on idea of `Tarzan of the Jungle <https://en.wikipedia.org/wiki/Tarzan>`_ letting go of a vine without having a new vine to swing to.

Decking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A term for shipping something that is below quality standards. This term is used by mountain climbers to describe falling off the side of a mountain, which often involves a series of failures, not just one.

Dev Mana
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A specific type of mana for developers similar to "points" or "jelly beans" in an Agile/Scrum methodology. On average, full time Mattermost developers each complete tickets adding up to approximately 28 mana per week. A "small" item is 2 mana, a "medium" is 4, a "large" is 8 and any project bigger needs to be broken down into smaller tickets.

Expert Mode (and Crimson Force Field)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When documentation or on-screen text is written for someone with considerable knowledge or expertise, instead of being designed for a new learner. In general, try to state things simply rather than speaking to just the "experts" reading the text.

If something is extremely difficult to understand, and yet still justified in the mind of the writer, we call it "Crimson Force Field". This term is intended to evoke the emotional response of coming across something that is difficult to understand, so writers of Crimson Force Field material can empathize with the readers. Crimson Force Field is drawn from an esoteric episode of Star Trek and it is unlikely anyone but the originator of the term understands its complete meaning. Crimson Force Field is itself Crimson Force Field.

Help Wanted
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Help Wanted tickets <http://docs.mattermost.com/process/help-wanted.html>`_, which are vetted changes to the source code open for community contributions.

Improvement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A beneficial change to code that is not fixing a bug.

LHS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The "Left-Hand Sidebar" in the Mattermost team site, used for navigation.

Mana
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An estimate of total energy, attention and effort required for a task.

A one-line change to code can cost more mana than a 100-line change due to risk and the need for documentation, testing, support and all the other activities needed.

Every feature added has an initial and on-going mana cost, which is taken into account in feature decisions.

RHS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The "Right-Hand Sidebar" in the Mattermost team site, used for navigation.

Windows Vista approach
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An attempt to add functionality through a massive, complex one-time re-write hoping to improve the architecture, but which likely ends in repeated delays, wasted effort, buggy code and limited architectural improvement (compared to re-writing the architecture in phases). This tempting, high risk approach is named after Microsoft's "Windows Vista" operating system, one of its most famous examples.



--------------------------
Training
--------------------------

At Mattermost, "Learn, Master, Teach" cycles are core to our culture. You should be constantly growing and cross-training into new skills and responsibilities, developing expertise, and then training your replacement as you prepare to take on new challenges.

Cross-training creates a culture of constant growth, protects against single-points of failure, and challenges each of us to rise to our fullest potential.


Roles
--------------------------

The "Learn, Master, Teach" cycle happens in the context of roles. Roles are sets of responsibility needed to achieve objectives. Roles aren't necessarily job titles, for small projects, a developer might take on a product manager role, or vice versa. Each team member has a "primary role" and training should move people to mastery and teaching in that role, before moving to the next role.

Developer
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Developers are responsible for architecting and delivering software improvements, and for technical leadership among the Mattermost community.

- Architecture
    - Developers are responsible for researching, analyzing, designing and reviewing technical solutions to achieve functional requirements. Solutions should thoroughly consider trade-offs and be evaluated based on the effectiveness of the end implementation.

- Delivery
   - Based on technical designs, developers estimate, implement, test, maintain, review, debug and release software improvements in collaboration with teammates. This includes working closely with product managers to validate requirements and the output of designs and making appropriate adjustments. The success of implementation is judged on the end results achieved by the changes.

- Technical Community Leadership
   - As leading experts on Mattermost technology, developers support and engage constantly with the broader Mattermost community to accelerate adoption and to discover new ways to improve Mattermost software and processes. This includes investigating and  supporting issues from users and customers, reviewing and providing feedback on projects from contributors, and understanding priorities, trends and patterns across the community.

Product Managers
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Product managers are responsible for aligning teams to strategic priorities, leading and managing the product development process, and working effectively with marketing to bring the full benefits of Mattermost solutions to users and customers.

- Strategy
   - Every project and every team needs to align to strategic priorities and focus on intended outcomes developed through a deep understanding of the market, user, customers and competing products and services. Amid a flood of compelling suggestions, opinions, and data, product managers must find what's vital, and rally teams around a shared vision.

- Product development
   - Product managers lead both the functional design process (user, customer and competitor research, analysis, ideation, prioritization, functional and user experience design, functional specification, user and customer validation), and the software development process (ticketing, prioritization, roadmap design, scheduling, sprint planning, triage, functional verification, implementation validation with users and customers, documentation, and release logistics).
   - It's the product manager's responsibility to see features shipped predictably and at high quality through planning, attention to detail and thoughtful persuasion.

- Marketing connection
   - Delivering benefits to users and customers based on product features is a core responsibility of product managers, working in conjunction with marketing to shape messaging and positioning and delivering collateral, events, and user and customer discussions to support sales.

Resources
--------------------------

The following is a list of recommended resources for developing skills "the Mattermost way" in different areas. For the ones that require purchase you can message @matterbot to request an order, whether as physical books, digital books, audiobooks or other formats.


Developers
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Books
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. `Code Complete, Steve McConnell <https://www.amazon.com/Code-Complete-Practical-Handbook-Construction/dp/0735619670>`_ - Best practices and guidelines for writing high quality code.
2. `Design Patterns,  Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides (aka "Group of Four") <https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented-ebook/dp/B000SEIBB8>`_ - Fundamental reading on design patterns. Other design pattern books work too, this is one of the most popular.

Product Management
^^^^^^^^^^^^^^^^^^

Courses

1. `Harvard Business School PM 101 <https://sites.google.com/site/hbspm101/home/2015-16-sessions/the-mrd-customer-discovery>`_

Relevant Docs

1. :doc:`design-process`

Software Strategy
^^^^^^^^^^^^^^^^^^^

1. `Monetizing Open Source (Or, All Enterprise Software) <http://a16z.com/2017/04/10/monetizing-open-source-enterprise-software/>`_ - Required reading for business roles

System Security
^^^^^^^^^^^^^^^

Papers & Course Materials

1. `Framework for Improving Critical Infrastructure Cybersecurity. National Institute of Standards and Technology <https://www.nist.gov/sites/default/files/documents/cyberframework/cybersecurity-framework-021214.pdf>`_ - Standards for internal Mattermost security processes and safeguards.
2. `Computer Security in the Real World. Butler Lampson <http://research.microsoft.com/en-us/um/people/blampson/69-SecurityRealIEEE/69-SecurityRealIEEE.pdf>`_ - Fundamental challenges with system security.
3. `Course notes from CS513: System Security (Cornell University). Fred B. Schneider <http://www.cs.cornell.edu/courses/cs513/2007fa/02.outline.html>`_ - Well written introduction to system security from one of the leaders in the field.

Additional Training Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Recommended training materials are recommended by role at three different levels of priority:

1. P1 - Required - Complete within 30 days of starting in role.
2. P2 - Priority - Complete within 30-90 days of starting.
3. P3 - Supplementry - Complete within 180 days.

The following chart outlines training materials by category, with notes on which materials are relevant to which disciplines by P1, P2, P3 priority:

.. raw:: html

    <embed>
        <iframe class="airtable-embed" src="https://airtable.com/embed/shrbjzgakQoNaXhYt?backgroundColor=gray&viewControls=on" frameborder="0" onmousewheel="" width="100%" height="1320" style="background: transparent; border: 1px solid #ccc;"></iframe>
        <p>&nbsp;</p>
    </embed>

The following table summarizes abbreviations used in the above table:

.. raw:: html

    <embed>
        <iframe class="airtable-embed" src="https://airtable.com/embed/shrlwbsr0Y9telZn8?backgroundColor=gray&viewControls=on" frameborder="0" onmousewheel="" width="100%" height="395" style="background: transparent; border: 1px solid #ccc;"></iframe>
        <p>&nbsp;</p>
    </embed>

Leadership Coaching
--------------------------

To advance the skills of senior and functional leaders, we bring in experts to advise on key functions, including sales, operations, product, marketing, strategy, general management, and other specialized topics. 

- As an example, `Jono Bacon <http://www.jonobacon.org/about/>`_--a leading author, speaker and consultant on open source community advocacy--meets with our community team regularly to refine our processes and understanding. There's a range of similiarly adept company advisers that help advance our thinking and capabilities in critical ways.

Many thought leaders and conference speakers are open to consulting projects with the right clients, and Mattermost is a flexible client. There's no travel involved, we meet over video conference, `our consulting process is straight forward <https://docs.google.com/document/d/1G4wFLq_wHHEDJ-hrv5Kmu022mFJgh3rJ4-glM0W6riI/edit#heading=h.pwxwwq4ezzfx>`_, we're easy to work with, and we take advising seriously. 

When hiring, we are also open to bringing in a leader's personal mentors as consultants and company advisers when skill sets are appropriate.

---------------------------------------------------------
Mattermost Avatar
---------------------------------------------------------

When becoming a core committer to the Mattermost project we create a "Mattermost Avatar" for you as a fun way to recognize your new level of contribution. 

Mattermost avatars are caricatures of core committers in the costume of a popular culture character (e.g. Spiderman, Wonder Woman, Luke Skywalker, etc.) created for personal use, and which may be potentially used in team rosters, demonstration sites, "group photos" where avatar images from the team are collected in one image of all the characters together, and other public uses. 

To have a Mattermost avatar created, you'll be invited to create a Mattermost avatar via email: 

1. Please use the email subject "[YOUR_FULL_NAME] as [CHARACTER_NAME]", for example "Corey Hulen as Han Solo". 
2. Attach a clear image at least 600 pixels high and 600 pixels wide showing your character's full body in a standing pose. 
3. Send a clear photo of your face at least 600 pixels high and 600 pixels wide facing the same direction as your character image.

Notes: 

1. Character should be human-sized (no giant characters).  
2. Character's appearance should be family-friendly. For example, no gory or provocative costumes.
 
You should receive your digital Mattermost avatars by email in 6-8 weeks. 

In special cases, a Mattermost avatar may be created for someone from the Mattermost community who has made an extraordinary contribution to the open source project. 

- Example of photo from core committer: `Corey Hulen, co-creator of the Mattermost open source project <https://cloud.githubusercontent.com/assets/177788/25364362/c2fee10c-2916-11e7-9de3-2947987a9dce.png>`_  

- Example of reference image for popular culture character: `Han Solo from the movie Star Wars  <https://cloud.githubusercontent.com/assets/177788/25364375/e49415bc-2916-11e7-94ae-038a120743b3.png>`_ 

Example of finished Mattermost Avatar: 

.. image:: https://cloud.githubusercontent.com/assets/177788/25364270/0425b738-2916-11e7-9a23-5ced2d9dfc8f.png

