# Security Policies 

This document summarizes the internal security policies at Mattermost, Inc. 

- [Security benefits of the Mattermost open source platform](#security-benefits-of-an-open-source-platform)
- [Mattermost Development Guidelines](#mattermost-development-guidelines)
  - [Security Review Checklist](#security-review-checklist) 
- [Common Security Related Questions for Enterprises](#common-security-related-questions-for-enterprises)
   - [Governance](#governance)
   - [Access Control](#access-control)
   - [Operational Security](#operational-security)
   - [Software Development Life Cycle (SDLC)](#software-development-life-cycle-sdlc)
   - [Training](#training)
   - [Validation](#validation)
   - [Security Response](#security-response)
   - [Business Resiliency](#business-resiliency)
   - [Compliance](#compliance)
- [Business Continuity Plan](#business-continuity-plan)

## Security benefits of an open source platform

The open source Mattermost Team Edition is used by thousands of teams around the world. Development is aided by hundreds of open source contributors, with full access to the product source code, who have a vested interest in keeping the software secure and vetted. 

As new threats emerge, a [responsible disclosure policy](https://www.mattermost.org/responsible-disclosure-policy/) is in place for the community to confidentially report security issues so they can be addressed by Mattermost, Inc. prior to documenting [security updates](https://about.mattermost.com/security-updates/) publicly. 

The commercial Mattermost Enterprise Edition extends the security and productivity benefits of the open source solution with support for advanced security, management, scale and policy compliance features for complex organizations. 

## Mattermost Development Guidelines

#### Tracking 

* Prior to implementation, potential code changes are discussed and documented in [Mattermost's issue tracking system](https://mattermost.atlassian.net/). 
* Security tickets are confidential to Mattermost, Inc. staff, who are under NDA, and specially tagged to avoid disclosure. 
* All potential code changes are mapped to tickets prior to acceptance, with the exception of trivial changes and bug fixes. 

#### Review 

* To uphold security, quality and reliability standards, all potential changes submitted by open source contributors must pass a [help wanted](https://handbook.mattermost.com/contributors/contributors/help-wanted) vetting process prior to submission. 
* Clarity and readability of code is enforced through [Mattermost style guides](https://docs.mattermost.com/developer/style-guide.html).
* After submission, all proposed changes require at least two code reviews for reliability, quality and system security. 
* All open source contributions are available for public inspection and commentary before and after acceptance. 

#### Reporting 

* Mattermost uses a [responsible disclosure policy](https://www.mattermost.org/responsible-disclosure-policy/) to accept confidential reports of new threats, so they can be addressed either immediately through a dot release, or by the next monthly release depending on potential impact. 
* When Mattermost software undergoes security and penetration testing at customer sites security updates are added to the core software and [publicly documented by release](https://about.mattermost.com/security-updates/). 

#### Patch Management 
* Critical updates are released for urgent, high priority security issues or critical losses of functionality that should not wait for the next monthly release. 
* Mattermost software has a mandatory upgrade policy and customers and users need to be on the latest release to receive critical updates. 
* Critical updates are delivered as dot releases, for example a critical update to release `3.1.0` would be named `3.1.1`.
* Customers and subscribers to the Security Bulletin [mailing list](https://mattermost.com/blog/category/security-updates/) receive notifications about all critical updates. 

### Security Review Checklist 
In addition to checklists for quality and reliability, code changes receive multiple reviews for the following system security design principles: 

- Reducing information disclosure 
- Reducing attack surface 
- Protecting against denial of service vulnerabilities 
- Preventing message spoofing 
- Preventing cross-site scripting 
- Preventing cross-site forgery 
- Preventing remote code execution 

### Security Update Monitoring 

The following resources are monitored for information about new security threats and attack vectors. 

- https://www.iacr.org/
- http://www.acm.org/
- https://www.usenix.org/
- https://www.exploit-db.com/
- https://security.googleblog.com/
- https://groups.google.com/forum/#!forum/golang-announce
- http://www.cert.org/
- https://www.reddit.com/r/netsec/

All dependencies are updated on a regular basis to ensure Mattermost uses the latest security updates.

## Common Security Related Questions for Enterprises

### Governance

1. Do you maintain a quality management system (QMS) approved by management? Does your quality management system (QMS) include coverage for software application security principles?
   - Yes. 

1. Is quality management system (QMS) content published and communicated to all relevant employees?
   - Yes.  

1. Is quality management system (QMS) content reviewed and updated (if appropriate) at least once per year?
   - Yes. 

1. Is there defined management oversight who is responsible for application quality and security reporting & signoff?
   - Yes. 

1. For all IT systems including but not limited to servers, routers, switches, firewalls, databases, and external social spaces, is management approval required prior to creating all user and privileged accounts (e.g., system or security administrator)?
   - Yes.

1. For all IT systems including but not limited to servers, routers, switches, firewalls and databases, are privileged accounts (e.g., system or security administrator) logged at all times and reviewed on at least a quarterly basis?
   - Yes.

1. Are all system, application and device password files encrypted using an industry standard encryption algorithm where technically feasible?
   - Yes

1. For all IT systems including but not limited to servers, routers, switches, firewalls and databases, do privileged accounts (e.g., system or security administrator) that communicate directly with the Internet, contain any personally identifiable information (PII) such as: social security numbers, credit card numbers, patient health record information, or other confidential records?
   - Yes

1. Is all sensitive, protected health information (PHI) and personally identifiable information (PII) protected using an industry standard encryption algorithm where technically feasible?
   - Yes

1. Are information assets classified?
   - Yes.

1. Are security roles and responsibilities of personnel defined and documented in accordance with the organization’s information security policy?
   - Yes.

1. Is a background screening performed prior to allowing personnel access to Scoped Systems and Data?
   - Yes.

1. Are new hires required to sign any agreements upon hire?
   - Yes.

1. Is there a disciplinary process for non-compliance with information security policies?
   - Yes, disclosure of confidential information or egregious disregard for documented security policies is grounds for termination. 

1. Is there a personnel termination or change of status process?
   - Yes.

### Access Control

1. Is access to and maintenance of applications, systems, network components (including routers, databases, firewalls, voice communications servers, voice recording servers, voice response units (VRU) etc), operating systems, virtualization components, hypervisors, or other information objects restricted to authorized personnel only?
   - Yes.

1. Is access to and maintenance of applications, systems, network components (including routers, databases, firewalls, voice communications servers, voice recording servers, voice response units (VRU) etc), operating systems, virtualization components, hypervisors, or other information objects granted based upon need-to-know job function?
   - Yes.

1. Are unique user IDs required for all user and privileged accounts (e.g., system or security administrator) to access all IT systems including but not limited to servers, routers, switches, firewalls and databases?
   - Yes.

1. Are passwords required for all user and privileged accounts (e.g., system or security administrator) to access all IT systems including but not limited to servers, routers, switches, firewalls and databases?
   - Yes.

1. Are there written network password policies and/or procedures?
   - Yes.

1. Is password administration employed for critical systems? 
   - Yes.

1. Are passwords prevented from being displayed in clear text during user authentication or in electronic/printed reports?
   - Yes.

1. If user accounts are assigned to non-permanent personnel (e.g., contractors, consultants)  for troubleshooting purposes, are the accounts disabled or removed after each use?
   - Yes

### Operational Security

1. Is there a risk assessment program that has been approved by management, communicated to appropriate personnel and has an owner to maintain and review the program?
   - Yes.

1. Is there an information security policy that has been approved by management, communicated to appropriate personnel and has an owner to maintain and review the policy?
   - Yes.

1. Is there a vendor management program?
   - Yes.

1. Is there a respondent information security function responsible for security initiatives?
   - Yes.

1. Is there an asset management policy or program that has been approved by management, communicated to appropriate personnel and has an owner to maintain and review the policy?
   - Yes.

1. Are management approved operating procedures utilized?
   - Yes.

1. Is there an operational change management / change control policy or program that has been approved by management, communicated to appropriate personnel and has an owner to maintain and review the policy?
   - Yes.

1. Are system backups performed?
   - Yes.

1. Are firewalls in use for both internal and external connections?
   - Yes.

1. Are firewalls or IPS(s) secured against unauthorized access from the Internet, Extranet and Intranet users?
   - Yes.

1. Are vulnerability assessments, scans or penetration tests performed on internal or external networks?
   - Yes.

1. Are incoming e-mails scanned for questionable file attachments?
   - Yes.

1. Does the company use spam filtering software to reduce the number of unsolicited e-mails?
   - Yes.

1. Are e-mail attachments scanned by anti-virus software?
   - Yes.

### Business Resiliency

For more information on Business Resiliency, see the [Mattermost Business Continuity Plan](https://docs.mattermost.com/process/security.html#business-continuity-plan).

1. Is there an established Business Resiliency program that has been approved by management and communicated to appropriate personnel?
   - Yes.

1. Has a Business Impact Analysis been conducted?
   - Yes.

1. Is there a formal process focused on identifying and addressing risks of disruptive incidents to the organization?
   - Yes.

1. Is there an established Business Resiliency program that has been approved by management and communicated to appropriate personnel?
   - Yes.

1. Are specific response and recovery strategies defined for addressing risks of disruptive incidents to the organization?
   - Yes.

1. Are formal business continuity procedures developed and documented?
   - Yes.

1. Has senior management assigned the responsibility for the overall management of the response and recovery efforts?
   - Yes.

1. Is there a periodic review of your Business Resiliency Program?
   - Yes, annually.

1. Is there an Influenza Pandemic/Infectious Disease Outbreak Plan?
   - Yes.

1. Is there insurance coverage for business interruptions or general services interruption?
   - Yes.

### Compliance

1. Is there an internal audit, risk management or compliance department with responsibility for identifying and tracking resolution of outstanding regulatory issues?
   - Yes.

1. Are there policies and procedures to ensure compliance with applicable legislative, regulatory and contractual requirements to address intellectual property rights on business processes or information technology software products?
   - Yes.

1. Is there a records retention policy covering paper and electronic records, including email in support of applicable regulations, standards and contractual requirements?
   - Yes. For example, records of customers with NDAs are retained in the event an NDA is terminated and requires destruction of records.

1. Is licensing maintained in all jurisdictions where the business operates or where licensing is required?
   - Yes.

1. Is there an internal compliance and ethics program to ensure professional ethics and business practices are implemented?
   - Yes.

1. Are policies and procedures maintained for enabling compliance with applicable legal, regulatory, statutory, or contractual obligations related to any information security requirements?
   - Yes.

1. Is there a formalized governance process to identify and assess changes that could significantly affect the system of internal controls for security, confidentiality and availability?
   - Yes.

### Software Development Life Cycle (SDLC)

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

### Training

1. Is Internal company training available & performed commensurate with personnel roles and responsibilities?
   - Yes.

1. Does training include security awareness?
   - Yes.

1. Does training include education on policies, standards, procedures and updates when needed?
   - Yes.

1. Are personnel training plans and records kept for internal company compliance purposes?
   - Yes.

### Validation

1. Are results from the execution of test plans reported and used to track and justify release readiness?
   - Yes. 

1. Does the quality assurance organization have authority to delay shipment of releases due to non-conformance reasons?
   - Yes.

1. Is some form of static code scanning performed as part of the release acceptance? What tools are used?
   - Yes, static analysis tools include ESLint and gofmt 

1. Is some form of dynamic code scanning performed as part of the release acceptance? What tools are used?
   - Yes, Jenkins is used for dynamic code scanning as part of the release process. 

### Security Response

1. Do you have a documented company security incident response process?
   - Yes. 

1. Do your maintenance releases include fixes for both quality and security related issues?
   - Yes.

1. Do you provide dedicated security patches for software versions that are released and supported in the field? How?
   - Yes. Security patches may be provided on the latest release when applicable. 

1. Is there proactive notification provided to customers and software partners (PTC)?  How?
   - Yes. Security updates are announced via email to customers as well as mailing list subscribers. 

1. Is there a specified response policy that includes the timeframe issues are to be addressed?
   - Yes, please see: [https://about.mattermost.com/support/](https://about.mattermost.com/support/)

## Infrastructure Security Policies

1. Technical infrastructure, including network security, servers and access control protocols are regularly reviewed for potential threats and vulnerabilities.

1. Business process, HR process and policies are regularly reviewed for potential threats and vulnerabilities.

1. A penetration test on the software is performed regularly. A copy of penetration results may be requested by customers upon five (5) day written notice at any time, but no more than once per twelve (12) month period.

## Business Continuity Plan

This document outlines Mattermost, Inc.'s **Disaster Recovery and Business Continuity Plan (DRBCP)** informed by the Federal Financial Institutions Examination Council guidelines on Business Continuity Planning in the context of Mattermost, Inc. being a vendor providing self-hosted software and consulting services to financial institutions. 

Because Mattermost software runs within a customer's data center, behind a customer's firewall and existing layers of security, without dependency to services hosted by Mattermost, the disruption of the business continuity of Mattermost, Inc. does not immediately impact the operating continuity of its customers. It does affect Mattermost's ability to answer support requests, provide consulting services and provide new improvements or patches to Mattermost software. 

At a high level, precautions include: 

- DRBCP is tested, evaluated and refined annually to ensure our processes are working and up-to-date
- As support is the most critical service offered, multiple channels for support engagement are available and monitored, including email, a Mattermost community server available on web, desktop and mobile, online forums, online forms, social media channels (Twitter and Facebook), and for Premier Support customers, we offer a telephone-based call center. 
- Subject Matter Experts for escalations are available in at least three centers in different timezones to provide redundant coverage should communication with one or multiple centers be disrupted. Mattermost staff use a diverse set of operating systems, including Mac, Windows and different distributions of Linux, and a diverse set of global internet service providers, to reduce the potential damage of a single strain of malware, single desktop computing exploit or single telecommunications outage. 
- As further redundancy, we have a network of [partners](https://about.mattermost.com/partners/) around the world skilled in Mattermost technologies to be contacted for assistance for critical customer issues.  
- As further redundancy, we have a community of several hundred engineers around the world and over a thousands contributors to our online forums, who have sufficient access and expertise in Mattermost's open source technologies that could be contact in the highly unlikely event both Mattermost, Inc. and our partner networks are unable to service our customers. 
- As further redundancy, Mattermost provides open source code for its core server technology, mobile applications, desktop applications and a wide array of extensions which allows customers to have transparency into the functionality of the software and solve the issue with their internal technical teams should a massive worldwide failure of Mattermost, Inc., its partners and its community arise. 

Mattermost, Inc. is headquartered in Palo Alto, California with a distributed organization across three timezones, and is therefore not easily affected by typical causes of business disruption, such as local failures of equipment, power, telecommunications, social unrest, fire, or natural disasters. Even so, threats considered in the context of business continuity are categorized by impact of the disruption.

### Priority 1: Outages that would have immediate impact on a Mattermost customer 

#### Key support staff unavailable in case of customer emergency.

Effect: 
- Emergency response times exceed expectations 

Solution(s): 
- Level 1 (Critical Business Impact) and Level 2 (Major Business Impact) support requests are received by on-call support staff, as well as three supervisory staff who can monitor and escalate issues should the assigned staff member appear to be unavailable or unable to respond to the request within the SLA time allotted. 
   - As an additional safeguard, when an L1 or L2 escalation is reported, a notification is sent via the company's internal Mattermost instance to all qualified support staff to be aware of the issue, and any member can step in if it seems follow-up may not be achieved within SLA expectations. 
    
Mitigation(s): 
- Mattermost, Inc. employs support staff and engineers in multiple timezones to increase availability, reduce response times and to reduce the risk that key support staff would be unavailable to service emergency requests. 

#### Downtime for Mattermost Hosted Push Notification Service (HPNS) 

Effect: 
- End users at customer sites deploying on HPNS do not receive mobile push notifications. 
 
Solution(s): 
- Mattermost, Inc. can re-deploy the service from backup to new infrastructure, should its existing infrastructure suffer an outage. 
 
Mitigation(s): 
- HPNS is available [as open source software hosted on GitHub.com](https://github.com/mattermost/push-proxy), allowing enterprises an option to compile and self-host the service, should they choose not to use HPNS hosted by Mattermost, Inc. 

#### Disruption of infrastructure providing support over email, online tickets or Mattermost messaging during customer emergency 

Effect: 
- Unable to communicate with Mattermost, Inc. support team during emergency 

Solution(s): 
- Should a support channel be out-of-service, Mattermost, Inc. provides redundant support options through email, online ticketing and (for customers who have purchased core access premium support) online message via Mattermost.  

### Priority 2: Outages having immediate impact on business continuity 

#### Outage due to malicious software (viruses, works, trojans and similar)

Effect: 
- Reduced capacity to continue business operations, depending on attack.

Solution(s): 
- Mattermost, Inc. staff uses multiple anti-virus solutions for detecting and removing malicious software and regularly backs up key systems to delete infected systems and re-deploy its infrastructure. Moreover, the company uses a range of Windows, Mac and Linux-based workstations, reducing the probability of a company-wide disruption from a single strain of malicious software. 

#### Outage due to online attacks 

Effect: 
- Reduced capacity to continue business operations, depending on attack.

Solution(s): 
- Mattermost, Inc. runs multiple monitoring and alerting services to detect and isolate suspicious traffic and requests in order to minimize downtime from potential online threats.  
- Should our self-hosted Mattermost instance be disrupted we can, if needed, quickly re-deploy the solution within our VPN. 

#### Disruption due to influenza pandemic or infectious disease outbreak

Effect: 
- Reduced capacity to continue business operations

Solution(s): 
- Mattermost, Inc. employs staff and engineers in multiple timezones and geographic areas, reducing the risk of significant disruption that an influenza pandemic or infectious disease outbreak would cause to business operations.

### Priority 3: Outages greater than 72 hours impacting business continuity 

#### Outage of online CRM system 

Effect: 
- Reduced ability to continue sales operations

Solution(s): 
- While there is no current failover plan should our online CRM system become disrupted, we have SLAs with our CRM vendor--which is used by thousands of other organizations--and believe the probability of sustained outage is low. 

### Priority 4: Outages greater than 10 days impacting business continuity 

#### Outage of online HR and intranet systems

Effect: 
- Reduced ability to continue HR and internal operations

Solution(s): 
- While there is no current failover plan should our online HR or intranet system become disrupted, we have SLAs with our  vendors--which is used by thousands of other organizations--and believe the probability of sustained outage is low. 
