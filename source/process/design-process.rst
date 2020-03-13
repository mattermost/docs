Design Process
===================

Goal
----

The goal of this design process is to increase Mattermost popularity by improving overall product quality, through a consistent design process that ensures we are designing the right features at the highest quality level possible. 

Principles
----------
1. Every feature should have a convincing reason for why it should be built
2. Every design should start with a story
3. Make time for exploration - it's okay to explore a design that doesn't work and throw it away, as long as we learn from it

Process
-------

1. **Define the "Why"**

    - Research customer/user requirements
    - Write the user stories (potentially for different personas) based on the requirements
    - Write the goal statement
    - Justify why the feature should be built
      
      - Link back to customer and user data / feedback
      - Link back to company objectives 
      - Explain why it is important and the expected impact
      
    - Before continuing with design work, queue a discussion with Product Managers to review the feature proposal and evaluate whether the feature should be added to the roadmap
       
    - *Questions this stage should address:* 
    
      - Who is this for? What do we know about them?
      - What are we trying to build? 
      - Why are we building it? 
      - Should we build this, or should we not? 
      
2. **Brainstorm**
    
    - Research a variety of existing solutions
    - Brainstorm different design concepts
    
      - Consider pair brainstorm
      - Do not go into depth on any one design, the goal is to identify various approaches to evaluate later
      
    - *Questions this stage should address:* 
    
      - What are the design options for the given scenarios?
     
3. **Evaluate options**

    - Identify the most promising design concepts
    
      - Wireframe/develop concepts as needed
      
    - List pros/cons for each option
    - Evaluate each option based on:
    
      - How well each design addresses user stories
      - Principles for this plan
      - Mattermost design principles
      
    - Have pair or group discussions as needed
    
      - Invite developers into the discussion early
      - Set the context for meetings, so people understand this is exploratory design
      
    - *Questions this stage should address:*
    
        - Is this design concept the right approach to the problem? 
        - How well does this design work for the given scenarios? 
        - What are the constraints we need to consider? 
        - How does this design compare to existing solutions? 
    
4. **Develop prototype**

    - Summarize context for the design (preferably in Google Slides), including: 
    
      - Goal/“Why"
      - User Stories
      - Success Metrics
      
        - Define how the success of the feature will be measured
        
      - Designs Considered
      
        - Link back to the various designs considered, and the evaluation 
        
      - Out of Scope
      
        - List things that are purposefully left out, to be addressed at another time
        
    - Work on prototype/mockups for the selected design
    
      - Consider pair design
      - Use mockups (preferably in slideshow or prototyping software), with text that supports the design
      - Include flow of screens, so transitions are clear
      - Make sure to think about: 
      
        - Mobile apps (mobile view and tablet view)
        - Notifications (desktop, email, and push)
        - Both single and multiple team cases
        - Potential performance issues
        
    - Add Questions
    
      - List out any questions about the design that still need to be answered
      
    - *Questions this stage should address:*
    
      - How is the information structured? What is important to see, and when? 
      - What is the layout like? 
      - What does the text say? 
      - What does the UI look like? 
      
5. **Review, test, and iterate**

    - Pair review with someone
    - Share with team
    
      - Post draft with @channel in Spec Review channel, asking to review and add comments
      - Set the context for what stage the design is at, and what they should be reviewing
      
    - Share with interested customers and users
    - Test the prototype/mockups
    
      - If possible, find someone to test the design on
      - Give tasks based on the already defined user stories
      - Observe and have them think aloud
      
    - Iterate based on feedback
   
   - *Questions this stage should answer:*
    
      - Are there any potential issues with the design? 
      
6. **Final review**

    - Identify people who should sign off on the design before implementation (include UX Design, PM, Dev, and Test)
    - Hold a meeting to review the design
    
      - Set the context that this is a final review, and people should look for any potential issues
      - Ask people to review the design and add comments/questions beforehand
      - Define example areas that should be covered (different people may focus on different things):
      
        - How well does the design address the listed scenarios?
        - Are there any technical concerns? 
        - Potential usability issues? 
        - Is the product text clear?
        - Does the design follow UX guidelines? 
        - Is it consistent with the rest of the product? 
        - How could this design be used in the future?
        - Are all corner cases addressed? Check for: 
        
          - Mobile apps (mobile view and tablet view)
          - Notifications (desktop, email, and push)
          - Both single and multiple team cases
          - Potential performance issues
          
    - Update design based on feedback until everyone signs off
    
    - *Questions this stage should answer:*
    
      - Is this design ready to be implemented? 
    
7. **Break into tickets**

    - Dev breaks the spec into tickets, and reviews with PM so everyone is on the same page about the plan
