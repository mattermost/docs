# Terminology 

Designing world-class software means bringing people together across disciplines and cultures. We want to create a limited amount of shared terminology to help us work better together, while being careful not to make it difficult for newcomers to follow our conversation. 

Perhaps in future we'll have a bot that helps teach newcomers about the terminology in-context. Until then we have this guide. 

## Purpose

We use Mattermost terminology to achieve specific benefits: 

#### 1) to increase precision in communication through unambiguous definitions of terms that could otherwise have many interpretations

For example, "0/5" and "5/5" help convey the level of conviction behind an opinion. A precise classification of tickets as "Bug" or "Improvement" is critical since it affects scheduling and decision making. 

#### 2) to increase the speed of communication via a small number of frequently used acronyms 

LHS and RHS are examples of a very limited number of acronyms to use to speed discussions, specifications, and ticket writing. 

#### 3) to reduce repeated mistakes by naming very specific undesirable behaviors

Naming a specific repeated mistake lets us remember it as an organization and identify patterns. It also helps innoculate newcomers to mistakes of the past as they learn our organization's termniology. 

## List of Terms

#### 0/5, 1/5, 2/5, 3/5, 4/5, 5/5 

We use "x/5" to concisely communicate conviction. 0/5 means you don't have a strong opinion, you are just sharing an idea or asking a question. 5/5 means you are highly confident and would stake your reputation on the opinion you're expressing. 

#### APR

Acronym for [Accepting Pull Request](http://docs.mattermost.com/process/accepting-pull-request.html) tickets, which are vetted changes to the source code open for community contributions.  

#### Bug

An obvious error in Mattermost software. Changes required to accomodate unsupported 3rd party software (such as browsers or operating systems) are not considered bugs, they are considered improvements. 

#### Crimson Force Field

When on screen text, particularly error messages, isn't helpful to its intended audience we call it a "Crimson Force Field" situation. This implies the text presented is not substantially better than using random words like "Crimson Force Field" to explain things, and may even be worse, if the text ends up misleading its audience. The words "Crimson Force Field" are intended to reproduce for the reader the feeling of confusion and awkwardness a user feels when software is cryptic and unclear. 

#### Dead Tarzan 

Discarding an imperfect solution without a clearly thought out alternative. Based on idea of [Tarzan of the Jungle](https://en.wikipedia.org/wiki/Tarzan) letting go of a vine without having a new vine to swing to. 

#### Dev Mana

A specific type of mana for developers similar to "points" or "jelly beans" in an Agile/Scrum methodology. On average, full time Mattermost developers each complete tickets adding up to approximately 28 mana per week. A "small" item is 2 mana, a "medium" is 4, a "large" is 8 and any project bigger needs to be broken down into smaller tickets. 

#### Improvement 

A beneficial change to code that is not fixing a bug. 

#### LHS

The "Left-Hand Sidebar" in the Mattermost team site, used for navigation.

#### Mana

An estimate of total energy, attention and effort required for a task. 

A one-line change to code can cost more mana than a 100-line change due to risk and the need for documentation, testing, support and all the other activities needed. 

Every feature added has an initial and on-going mana cost, which is taken into account in feature decsions. 

#### RHS

The "Right-Hand Sidebar" in the Mattermost team site, used for navigation.

#### Windows Vista approach

An attempt to add functionality through a massive, complex one-time re-write hoping to improve the architecture, but which likely ends in repeated delays, wasted effort, buggy code and limited architectural improvement (compared to re-writing the architecture in phases). This tempting, high risk approach is named after Microsoft's "Windows Vista" operating system, one of its most famous examples.
