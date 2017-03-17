==================================================
Onboarding
==================================================

This document in intended for new hires to summarize norms for working at Mattermost, Inc. including:

- `Getting Started Checklist`_ - Getting ready to work here
- `Meetings`_ - When we get together and why
- `Mindsets`_ - Shared toolsets we have for solving problems
- `Terminology`_- Shared vocabulary to convey ideas quickly
- `Training`_ - Material available to help us ramp quickly in different areas.

.. contents::
    :backlinks: top

---------------------------------------------------------
Getting Started Checklist
---------------------------------------------------------

Hiring
---------------------------------------------------------

- (People Ops & New Hire) Offer letter accepted via click-sign
- (Logistics) Mail track jacket & socks 

T-minus 1-3 weeks
---------------------------------------------------------

- (People Ops & New Hire) People Ops should find out new hire's preference for laptop, either to be purchased or taken from stock and shipped by People Ops or purchased locally by new hire and expensed. Windows laptops generally cost less than Macs so budget is based on Macs. For non-developers, budget is cost of a Macbook in your local area, for developers budget is cost of a Macbook Pro.
- (New Hire) Read the entirety of Onboarding page for info on meetings, mindsets, terminology and training materials.

T-minus 1 week
---------------------------------------------------------

- (People Ops) Send email invite to New Hire to set up an @mattermost.com email address. New Hire should use this email address on pre-release.mattermost.com (replace personal email with company email if already registered there). `FIRST_NAME@mattermost.com` is the standard naming convention.

- (People Ops & New Hire) Set up payroll. 
  - US FTE - Receive email to complete TriNet sign-up, payroll, benefits enrollment, I-9 form, banking information, personal information, tax forms.  
  - Non-US Employee/Non-Canada Employee, complete bank info form for monthly wire transfer 
  - Non-US Resident Contractor, complete W8-BEN form
  - US Contractor, complete W-9 form

First Day
---------------------------------------------------------

- (Manager) Posts welcome message in stand-up channel.
- (Manager) Meets New Hire for first 1-1 meeting.
- (Buddy) Meets New Hire for first 1-1 meeting.
- (People Ops) US FTE - Contact New Hire to verify work authorization and I-9.

3 months 
---------------------------------------------------------

- (People Ops) US FTE - Email regarding 401K account set up.  

---------------------------------------------------------
Meetings
---------------------------------------------------------

This section summarizes norms for public and private meetings for the Mattermost community and for Mattermost Inc. Where possible,

Open Meetings
---------------------------------------------------------

Developer Meeting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Open to the public** - (Developers - 1-2 hours/week) Wednesdays 10:00 (`San Francisco Time <http://everytimezone.com/>`_)

- Goal: Discuss developer issues across Mattermost Inc, key contributors and the contributor community.
- Attendees: (required) Mattermost Inc developers, (optional) key contributors, contributors and anyone who would like to join.

Procedure:

1. (Chair): Post meeting agenda in `Developers channel <https://pre-release.mattermost.com/core/channels/developers>`_ (open to the public), tagged with ``#devmeeting``
2. (Team and Public): At the time of the meeting:

      - Join the **Hangouts** link posted in the meeting agenda in the `Developers channel <https://pre-release.mattermost.com/core/channels/developers>`_

To review past agendas for the Developer meeting in the `Developers channel <https://pre-release.mattermost.com/core/channels/developers>`_ click on the ``#devmeeting`` hashtag in any of the meeting notes, or search for it directly.


Mattermost Inc-only Meetings
----------------------------------------------------

For confidentiality of customers, internal process meetings are limited to Mattermost Inc. only.


Sprint Planning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Mattermost Inc-only** - (Developer - 5-10 minutes/week) Tuesdays between 10:00 and 11:00 (`San Francisco Time <http://everytimezone.com/>`_)

- Goal: Review and discuss tickets selected by Developer for next sprint
- Attendees: (required) Each developer in sequence, plus spint planngers (one dev, one PM) (optional) Mattermost Inc. colleagues welcome

Note:

- This meeting uses a special `Mattermost Inc only BACKLOG query <https://mattermost.atlassian.net/secure/RapidBoard.jspa?rapidView=1&view=planning.nodetail&quickFilter=7>`_ showing tickets by sprint, with tabs across the top for each developer.
- Prior to meeting, developers drag and drop tickets from their backlog to next sprint based on team priorities

     - Developers are welcome at any time to discuss reassigning tickets with colleagues using common sense (if both are okay with the change, add "triage" tag to fix version with comment and triage team will review to make the change)
- During the meeting, developer's next sprint is reviewed, discussed, possibly adjusted and locked

Procedure:

1. (Chair): Just prior to meeting, post **Hangout** link in `Standup private group <https://pre-release.mattermost.com/core/channels/stand-up>`_
2. (Developer): Replies in Standup private group when sprint is ready for review
3. (Chair): Will (at)mention next developer to join **Hangout** to review tickets. Developer joins, tickets are discussed and finalized for next sprint. Developer leaves **Hangout** and next developer rotates in.

Triage Meeting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Mattermost Inc-only** - (Triage team - 1-3 hours/week) Monday, Wednesday, Friday 09:00 (`San Francisco Time <http://everytimezone.com/>`_)

- Goal: To provide consistent review, prioritization and ownership assignment of all tickets
- Attendees: (required) dev and PM from Mattermost Inc., typically leads (optional) other Mattermost Inc. colleagues welcome

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

1. (Chair): Just prior to meeting, post **Hangout** link in `Standup private group <https://pre-release.mattermost.com/core/channels/stand-up>`_ (Mattermost Inc. only)

2. (Attendees): Join the link

3. (Attendees): Review `query for tickets needing triage <https://mattermost.atlassian.net/browse/PLT-1203?filter=10105>`_ and assign owner and fix version

Leads Meeting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Mattermost Inc-only** - (Leads - 1-3 hours/week) Monday, Wednesday, Friday after Triage Meeting (09:00 `San Francisco Time <http://everytimezone.com/>`_)

- Goal: Address leadership and process topics
- Attendees: (required) dev, PM and community/marketing leads from Mattermost Inc. (optional) other Mattermost Inc. colleagues welcome

Note:

- Decisions should go to Leads meetings when there is lack of clarify or ownership

    - When possible, decision-making should belong to the people closes to details
    - Individual developers or PMs should make most decisions, and raise to developer or PM team if things are unclear, and go to Leads if lack of clarify persists.

- To queue an item for Leads ask the dev or PM lead

- Leads is also used for cross-discipline Q&A

    - Rather than randomize individual contributors, cross-discipline discussion (e.g. marketing to PM, community to dev, etc.) can happen in leads

Procedure:

1. (PM & Dev Leads): Stay in **Hangout** after Triage meeting and message community/marketing lead to join.

2. (Attendees): Discuss agenda items in Leads private group

3. (Attendees): Respond to respective colleagues on decisions from Leads meeting

Platform Meeting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Mattermost Inc-only** - (Platform colleagues - 1-2 hours/week) Friday's at 10:10 (`San Francisco Time <http://everytimezone.com/>`_) after platform team standup.

Regular team meeting for platform team at Mattermost Inc.

- Goal: Increase team output by effectively informing and reviewing priority projects and next steps.
- Scope: Mattermost Inc-only meeting given confidential customer issues discussed
- Attendees: Mattermost Inc colleagues working on platform
Procedure:

1. (Chair) 3-hours before standup, post reminders in `Platform private group <https://pre-release.mattermost.com/core/channels/platform-discussion>`_ (Mattermost Inc only)

::

   #### @channel Platform Meeting Reminder
   Everyone please:
   - **Prepare your demos**
   - **Prepare your User Issue or Kaizen**

   @lindsay please:
   - **Prepare your roadmap checkin**

   @[WHOEVER] are you ready for your "Something interesting about my town"?


2. (Team) At time of meeting:

   - Join the **Hangout** link in the header of the `Platform private group <https://pre-release.mattermost.com/core/channels/platform-discussion>`_
   - Open the **Notes** link in the header to see the agenda

3. (Vice-Chair) Post `"Standing Items" template <https://docs.google.com/document/d/1ImSgkF7T03wbKwz_t4-Dr4n3I8LixVbFb2Db_u0FmdM>`_ into Platform Meeting Notes

    - Add **Follow-ups** from previous meeting
    - Add **New items** queued in `Platform private group <https://pre-release.mattermost.com/core/channels/platform-discussion>`_ (Mattermost Inc only)

Meeting Agenda:

- **Warm-up** - Currently: "Share something interesting about your home town."
- **Release countdown** - Review release date, milestones and checklists.
- **Roadmap check-in** - Review of roadmap status in current and next release
- **Demos** - Team members show highlights of what's completed this week. Relevant follow-ups noted.
- **Follow-ups** - Follow-ups from previous meeting are discussed
- **New items** - New team-relevant items are discussed

   - **Kaizen (odd sprints)** - Each colleague shares a potential process improvement. Follow-ups noted.
   - **User Issues (even sprints)** - Each colleage shares unaddressed external user issue of importance. Follow-ups noted.
- **Open Questions** - To find blindspots, meeting does not end until 3 open questions are asked and answered.

Post Meeting:

- Follow-up items are posted to the  `Platform private group <https://pre-release.mattermost.com/core/channels/platform-discussion>`_ (Mattermost Inc only)

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

[LHS](http://docs.mattermost.com/process/terminology.html#lhs) and [RHS](http://docs.mattermost.com/process/terminology.html#rhs) are examples of a very limited number of acronyms to use to speed discussions, specifications, and ticket writing.

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

Discarding an imperfect solution without a clearly thought out alternative. Based on idea of `Tarzan of the Jungle <https://en.wikipedia.org/wiki/Tarzan>`_ letting go of a vine without having a new vine to swing to.

Decking 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A term for shipping something that is below quality standards. This term is used by mountain climbers to describe falling off the side of a mountain, which often involves a series of failures, not just one.

Dev Mana
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A specific type of mana for developers similar to "points" or "jelly beans" in an Agile/Scrum methodology. On average, full time Mattermost developers each complete tickets adding up to approximately 28 mana per week. A "small" item is 2 mana, a "medium" is 4, a "large" is 8 and any project bigger needs to be broken down into smaller tickets.

Expert Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When documentation or on-screen text is written for someone with considerable knowledge or expertise, instead of being designed for a new learner. In general, try to state things simply rather than speaking to just the "experts" reading the the text. 

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

At Mattermost, Inc., "Learn, Master, Teach" cycles are core to our culture.

We want you to constantly grow and cross-train into new skills and responsibilities, develop effective expertise, and then train your replacement as you prepare to take on new challenges.

Cross-training creates a culture of constant growth, protects against "single-points of failure", and challenges each of us to rise to our fullest potential.


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

System Security
^^^^^^^^^^^^^^^

Papers & Course Materials

1. `Framework for Improving Critical Infrastructure Cybersecurity. National Institute of Standards and Technology <https://www.nist.gov/sites/default/files/documents/cyberframework/cybersecurity-framework-021214.pdf>`_ - Standards for internal Mattermost security processes and safeguards.
2. `Computer Security in the Real World. Butler Lampson <http://research.microsoft.com/en-us/um/people/blampson/69-SecurityRealIEEE/69-SecurityRealIEEE.pdf>`_ - Fundamental challenges with system security.
3. `Course notes from CS513: System Security (Cornell University). Fred B. Schneider <http://www.cs.cornell.edu/courses/cs513/2007fa/02.outline.html>`_ - Well written introduction to system security from one of the leaders in the field.



High Performance Teams
^^^^^^^^^^^^^^^^^^^^^^

Books

1. `High Output Management. Andy Grove <https://www.amazon.com/dp/B015VACHOK/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1>`_ - Potentially the most important book on management you'll ever read. From formoer CEO of Intel.
2. `Creativity, Inc. Ed Catmull <https://www.amazon.com/Creativity-Inc-Overcoming-Unseen-Inspiration-ebook/dp/B00FUZQYBO/ref=sr_1_1?s=books&ie=UTF8&qid=1466393928&sr=1-1&keywords=creativity%2C+inc>`_ - Achieving high performance through process and culture. From CEO fo Pixar.
3. `How to Win Friends and Influence People <https://www.amazon.com/How-Win-Friends-Influence-People-ebook/dp/B003WEAI4E/ref=sr_1_1?s=books&ie=UTF8&qid=1466394700&sr=1-1&keywords=how+to+win+friends+and+influence+people>`_ - How to build interpersonal skills to work more effectively in teams.

Articles

1. `Fire & Motion. Joel Spolsky <http://www.joelonsoftware.com/articles/fog0000000339.html>`_ - How to get more things done in less time by doing a little every day.

Culture
^^^^^^^

Video

1. `Tribes. Seth Godin at TED <https://www.ted.com/talks/seth_godin_on_the_tribes_we_lead>`_  (17m) Creating effective teams through bottoms-up culture.

Books

1. `Tribes. Seth Godin <https://www.amazon.com/Tribes-We-Need-You-Lead/dp/1591842336?ie=UTF8&ref_=asap_bc>`_ - Creating effective teams through bottoms-up culture.
2. `Inside Apple. Adam Lashinsky <https://www.amazon.com/Inside-Apple-Americas-Admired---Secretive--Company-ebook/dp/B005LH4Y3G/ref=sr_1_1?s=books&ie=UTF8&qid=1466393946&sr=1-1&keywords=inside+apple>`_ - Achieving high performance in top-down culture.


Marketing
^^^^^^^^^

Video

- `Getting Ideas to Spread. Seth Godin. TED. <https://www.ted.com/talks/seth_godin_on_sliced_bread#t-631421>`_ (17m) - Focus your messaging on a clear target market, not the "average".

Books

1. `Marketing Principles (1-2h read) <http://www.barcharts.com/9781423215042-details.aspx#.V2dn3vkrJ1M>`_ - Crash course on marketing terminology and concepts.
2. `All Marketers Tell Stories, Seth Godin <https://www.amazon.com/All-Marketers-Are-Liars-Works---ebook/dp/B00315QK8M/ref=sr_1_1?s=books&ie=UTF8&qid=1466393785&sr=1-1&keywords=%22all+marketers+are+liars%22>`_ - Ideas for creating compelling messages.

High Performance Mindsets
^^^^^^^^^^^^^^^^^^^^^^^^^

Books

1. `Checklist Manifesto. Atul Gawande <https://www.amazon.com/dp/B0030V0PEW/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1>`_ - How to reduce errors by reducing complexity using checklists.
2. `Getting Things Done. David Allen <https://www.amazon.com/Getting-Things-Done-Stress-Free-Productivity/dp/0142000280>`_ - How to do more in less time.

Software Development Process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. `Scrum. Jeff Sutherland <https://www.amazon.com/Scrum-Doing-Twice-Work-Half/dp/038534645X/ref=sr_1_1?ie=UTF8&qid=1466396699&sr=8-1&keywords=scrum>`_ (256 pages) - One point of view on agile software development, with examples.

2. `ISTQB Certification Study Guide <http://istqbexamcertification.com/>`_ - Common terminology & process in software development.

Quality
^^^^^^^

Video

1. `This is broken. Seth Godin <https://www.ted.com/talks/seth_godin_this_is_broken_1>`_ (~20m) - Why bad design happens.


Interaction Design
^^^^^^^^^^^^^^^^^^

Primer

1. `Stanford Design School "bootcamp bootleg" <https://dschool.stanford.edu/wp-content/uploads/2011/03/BootcampBootleg2010v2SLIM.pdf>`_ (47 pages) - Crash course in "design thinking".

Video

1. `IDEO shopping cart project <https://www.youtube.com/watch?v=taJOV-YCieI>`_ (22m) - Illustration of design thinking

Books

1. `Don't Make Me Think, Revisited. Steven Krug <https://www.amazon.com/Dont-Make-Think-Revisited-Usability/dp/0321965515/ref=sr_1_1?s=books&ie=UTF8&qid=1466393824&sr=1-1&keywords=don%27t+make+me+think>`_ - Principles of effective UX design.
2. `Evil by Design. Chris Nodder <https://www.amazon.com/Evil-Design-Interaction-Lead-Temptation/dp/1118422147/ref=sr_1_1?s=books&ie=UTF8&qid=1466393849&sr=1-1&keywords=evil+by+design>`_ - Pitfalls of effective UX design.

Blogs

1. `Nielsen Norman Group <https://www.nngroup.com/articles/>`_ - Many good articles and concepts on UX design.

Leadership Coaching 
--------------------------

To advanced the skills of senior and functional leaders beyond standard materials and processes, we bring in leading experts to advise our leaders and the company on key functions, including sales, operations, strategy and general management. 

- As an example, `Jono Bacon <http://www.jonobacon.org/about/>`_--a leading author, speaker and consultant on open source community advocacy--meets with our community team regularly to refine our processes and understanding. There's a range of similiarly adept company advisers that help advance our thinking and capabilities in critical ways. 

Many thought leaders and conference speakers are open to consulting projects with the right clients, and Mattermost is an excellent client. There's no travel involved, we meet over video conference, we're easy to work with, and we take advising seriously. Advising is a critical part of growing our people and our company. 

We are also open to bringing in a leader's personal mentors as consultants and company advisers when skill sets are appropriate. 
