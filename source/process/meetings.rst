=========
Meetings 
=========

This document summarizes norms for public and private meetings for the Mattermost community and for Mattermost Inc. Where possible, 

Open Meetings 
----------------------------------------------------

Developer Meeting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Open to the public** - (Developers - 1-2 hours/week) Wednesdays 10:00 UTC-7 

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Mattermost Inc-only** - (Developer - 5-10 minutes/week) Tuesdays between 10:00 and 11:00 UTC-7 

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Mattermost Inc-only** - (Triage team - 1-3 hours/week) Monday, Wednesday, Friday 09:00 UTC-7 

- Goal: To provide consistent review, prioritization and ownership assignment of all tickets 
- Attendees: (required) dev and PM from Mattermost Inc., typically leads (optional) other Mattermost Inc. colleagues welcome

Note: 

- ONLY TRIAGE TEAM should set or change the **Fix Verion** of a ticket. 

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

Platform Meeting 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Mattermost Inc-only** - (Platform colleagues - 1-2 hours/week) Friday's at 10:10 UTC-7 after platform team standup.

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
~~~~~~~~

- 2-3 minute exercises designed to learn more a colleagues at the start of a recurring meeting
- Typically rotates alphabetically by first name, one colleague per meeting
- Examples: 

   - "Hobby talk" - sharing about an interesting hobby, past or present
   - "My home town" - sharing something interesting about where you grew up
   - "Two truths and a lie" - share two true facts about yourself and one lie, team guesses which is the lie. 

Open Questions 
~~~~~~~~~~~

- Exercise to find blindspots in team thinking at the end of a meeting
- Meeting does not end until 3 questions are asked and answered, typically at least one of the questions reveals a blindspot or opportunity to improve communication. 
- Examples of questions: 

    - "What's the status on X?" // often an important item that got forgotten
    - "Who owns X?" // reveals need for more clarity or communication 
    - "Why do we do X?" // let's us verify if a process is needed, and if we're handling it the right way
