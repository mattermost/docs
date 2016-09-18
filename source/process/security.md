# Security Policies 

This document summarizes the internal security policies at Mattermost, Inc. 

- [Security benefits of the Mattermost open source platform](#open-source-security)
- [Mattermost Development Guidelines](#development-guidelines)
- [Security Checklist](#security-checklist) 
- [Common Security Related Questions for Enterprises](#common-security-related-questions)
   - [Governance](#governance)
   - [Software Development Life Cycle (SDLC)](#sdlc)
   - [Training](#training)
   - [Validation](#validation)
   - [Security Response](#security-response)
- [Business Continuity Plan](#business-continuity-plan)

## Security benefits of an open source platform <a name="open-source-security"></a>

The open source Mattermost Team Edition is used by thousands of teams around the world. Development is aided by hundreds of open source contributors, with full access to the product source code, who have a vested interest in keeping the software secure and vetted. 

As new threats emerge, a [responsible disclosure policy](https://www.mattermost.org/responsible-disclosure-policy/) is in place for the community to confidentially report security issues so they can be addressed by Mattermost, Inc. prior to documenting [security updates](https://about.mattermost.com/security-updates/) publicly. 

The commercial Mattermost Enterprise Edition extends the security and productivity benefits of the open source solution with support for advanced security, management, scale and policy compliance features for complex organizations. 

## Mattermost Development Guidelines<a name="development-guidelines"></a>

TRACKING 
* Prior to implementation, potential code changes are discussed and documented in [Mattermost's issue tracking system](https://mattermost.atlassian.net/). 
* Security tickets are confidential to Mattermost, Inc. staff, who are under NDA, and specially tagged to avoid disclosure. 
* All potential code changes are mapped to tickets prior to acceptance, with the exception of trivial changes and bug fixes. 

REVIEW 
* To uphold security, quality and reliability standards, all potential changes submitted by open source contributors must pass an [accepting pull requests](https://docs.mattermost.com/process/accepting-pull-request.html) vetting process prior to submission. 
* Clarity and readability of code is enforced through [Mattermost style guides](https://docs.mattermost.com/developer/style-guide.html).
* After submission, all proposed changes require at least two code reviews for reliability, quality and system security. 
* All open source contributions are available for public inspection and commentary before and after acceptance. 

REPORTING 
* Mattermost uses a [responsible disclosure policy](https://www.mattermost.org/responsible-disclosure-policy/) to accept confidental reports of new threats, so they can be addressed either immediately through a dot release, or by the next monthly release depending on potential impact. 
* When Mattermost software undergoes security and penetration testing at customer sites security updates are added to the core software and [publicly documented by release](http://about.mattermost.com/security-updates/). 

### Security Review Checklist<a name="security-checklist"></a> 

Among other design principles to increase system security, code changes receive multiple reviews for: 

- Reducing information disclosure 
- Reducing attack surface 
- Protecting against denial of service vulnerabilities 
- Preventing message spoofing 
- Preventing cross-site scripting 
- Preventing cross-site forgery 
- Preventing remote code execution 

## Common Security Related Questions for Enterprises<a name="common-security-related-questions"></a>

### Governance<a name="governance"></a>

1. Do you maintain a quality management system (QMS) approved by management? Does your quality management system (QMS) include coverage for software application security principles?
   - Yes. 

1. Is quality management system (QMS) content published and communicated to all relevant employees?
   - Yes.  

1. Is quality management system (QMS) content reviewed and updated (if appropriate) at least once per year?
   - Yes. 

1. Is there defined management oversight who is responsible for application quality and security reporting & signoff?
   - Yes. 

1. Is access to and maintenance of applications, systems, network components (including routers, databases, firewalls, voice communications servers, voice recording servers, etc), operating systems, virtualization components, hypervisors, or other information objects restricted to authorized personnel only?
   - Yes.

1. Is access to and maintenance of applications, systems, network components (including routers, firewalls, voice communications servers, voice recording servers, voice response units (VRU) etc), operating systems, virtualization components, hypervisors, or other information objects granted based upon need-to-know job function?
   - Yes.

1. For all IT systems including but not limited to servers, routers, switches, firewalls, databases, and external social spaces, is management approval required prior to creating all user and privileged accounts (e.g., system or security administrator)?
   - Yes.

1. For all IT systems including but not limited to servers, routers, switches, firewalls, databases are privileged accounts (e.g., system or security administrator) logged at all times and reviewed on at least a quarterly basis?
   - Yes.

1. Are passwords prevented from being displayed in clear text during user authentication or in electronic/printed reports?
   - Yes.

1. Are all system, application and device password files encrypted using an industry standard encryption algorithm where technically feasible?
   - Yes

1. If user accounts are assigned to non-permanent personnel (e.g., contractors, consultants)  for troubleshooting purposes, are the accounts disabled or removed after each use?
   - Yes

### Software Development Life Cycle (SDLC)<a name="sdlc"></a>

1. Are there documented processes, procedures, standards and templates used in your SDLC process?  
   - Yes. 

1. Do the materials above include references to application security best-practices and principles being followed?
   - Yes.

1. Are design and code reviews performed as part of your SDLC processes?
   - Yes.

1. Are security considerations (checklists, standards and policies) referenced in the design and code review?
   - Yes.

1. Is application code managed in a secure configuration management system with access controls?
   - Yes.

1. Is there a configuration management plan and are release artifacts maintained in a configuration management system?
   - Yes.

1. Are test plans and records kept that reflects the tests performed and results observed for each release?
   - Yes.

1. Is a release criteria defined, measured and reported on to confirm targeted release quality is achieved?
   - Yes.

1. Do you work with third parties that may have access to your IP and sensitive data?
   - Yes, we may employ vendors and consultants, including 3rd party security analysts. 

1. If so, is access to data controlled by terms of Non-Disclosure Agreements?
   - Yes.

### Training<a name="training"></a>

1. Is Internal company training available & performed commensurate with personnel roles and responsibilities?
   - Yes.

1. Does training include security awareness?
   - Yes.

1. Does training include education on policies, standards, procedures and updates when needed?
   - Yes.

1. Are personnel training plans and records kept for internal company compliance purposes?
   - Yes.

### Validation<a name="validation"></a>

1. Are results from the execution of test plans reported and used to track and justify release readiness?
   - Yes. 

1. Does the quality assurance organization have authority to delay shipment of releases due to non-conformance reasons?
   - Yes.

1. Is some form of static code scanning performed as part of the release acceptance? What tools are used?
   - Yes, static analysis tools include ESLint and gofmt 

1. Is some form of dynamic code scanning performed as part of the release acceptance? What tools are used?
   - Yes, Jenkins is used for dynamic code scanning as part of the release process. 

### Security Response<a name="security-response"></a>

1. Do you have a documented company security incident response process?
   - Yes. 

1. Do your maintenance releases include fixes for both quality and security related issues?
   - Yes.

1. Do you provide dedicated security patches for software versions that are released and supported in the field? How?
   - Yes. Security patches may be provided on the latest release when applicable. 

1. Is there proactive notification provided to customers and software partners (PTC)?  How?
   - Yes. Security updates are announced via email to customers as well as mailing list subscribers. 

1. Is there a specified response policy that includes the timeframe issues are to be addressed?
   - Yes, please see: https://about.mattermost.com/support/

## Business Continuity Plan<a name="business-continuity-plan"></a>

Mattermost, Inc. is headquartered in Palo Alto, California with a distributed organization across three timezones, and is therefore not easily affected by typical causes of business disruption, such as local failures of equipment, power, telecommunications, social unrest, fire, or natural disasters. Even so, threats considered in the context of business continuity are categorized by impact of the disruption.

### P1: Outage would have immediate impact on a Mattermost customer / user operations

1. Disruption of Mattermost Hosted Push Notification Service (HPNS)

   - Effect: A loss of availability of Mattermost hosted infrastructure for relaying push notifications from a customer's private cloud to hosted mobile apps in iTunes and Google Play could result in loss of push notifications in live deployments using HPNS.
   - Solution(s): The Mattermost Hosted Push Notification Service can be re-deployed from backup to new infrastructure, should its existing infrastructure suffer an outage. Moreover, the code base of HPNS is available as open source software available on GitHub.com, allowing enterprises an option to compile and self-host the service rather than use the solution hosted by Mattermost, Inc. 
