# Software & Hardware Requirements
___

## Deployment Overview

Please see [Mattermost Deployment Overview](https://github.com/mattermost/docs/blob/master/source/install/network-diagram.png) for a summary of components listed here. 

![image](https://cloud.githubusercontent.com/assets/177788/13199970/49774126-d7eb-11e5-8f07-95ddd33e9d72.png)

[View Mattermost Network Diagram](https://cloud.githubusercontent.com/assets/177788/13199970/49774126-d7eb-11e5-8f07-95ddd33e9d72.png)

## Software 

### Client Software 

##### PC Web Experience

- PC: Windows 7, Windows 8, Windows 10 (IE 11, Chrome 43+, Firefox 38+, Edge)  
- Mac: OS 10 (Safari 9, Chrome 43+)  
- Linux: Arch 4.0.0  (Chrome 43+)  

##### Mobile App Experience

- iPhone 4s and later with iOS 9+ 
- Android devices with Android 4.40+

##### Mobile Web Experience

- iPhone 4s and higher (Safari on iOS 9+, Chrome 43+)  
- Android 5 and higher (Chrome 43+)  

##### Email Client

- _Desktop clients:_ Outlook 2010+, Apple Mail version 7+, Thunderbird 38.2+  
- _Web based clients:_ Office 365, Outlook, Gmail, Yahoo, AOL  
- _Mobile clients:_ iOS Mail App (iOS 7+), Gmail Mobile App (Android, iOS)

### Server Software 

##### Mattermost Server Operating System

- Ubuntu 14.04, Debian Jessie, CentOS 6.6+, CentOS 7.1+, RedHat Enterprise Linux 6.6+, RedHat Enterprise Linux 7.1+, Oracle Linux 6.6+, Oracle Linux 7.1+

The Mattermost roadmap does not currently include production support for Fedora, FreeBSD or Arch Linux. 

##### Database Software

- MySQL 5.6+
- PostgreSQL 9.4+

Deployments requiring searching in Chinese, Japanese and Korean languages require MySQL 5.7.6+ and the configuration of [ngram Full-Text parser](https://dev.mysql.com/doc/refman/5.7/en/fulltext-search-ngram.html). See [CJK discussion](https://github.com/mattermost/platform/issues/2033#issuecomment-183872616) for details. 

## Hardware

Mattermost offers both real-time communication and file sharing. CPU and Memory requirements are driven by the number of concurrent users using real-time messaging. Storage requirements are driven by number and size of files shared. 

The below guidelines offer estimates based on real world usage of Mattermost configured to serve multiple independent teams of 10-100 registered users per team with moderate activity. 

### CPU

- 2 cores is the recommended number of cores and supports up to 250 registered users
- 4 cores supports up to 1,000 users
- 8 cores supports up to 2,500 users
- 16 cores supports up to 5,000 users
- 32 cores supports up to 10,000 users
- 64 cores supports up to 20,000 users

### Memory

- 2GB RAM is the recommended memory size and supports up to 50 registered users
- 4GB RAM supports up to 500 users
- 8GB RAM supports up to 1,000 users
- 16GB RAM supports up to 2,000 users
- 32GB RAM supports up to 4,000 users
- 64GB RAM supports up to 8,000 users
- 128GB RAM supports up to 16,000 users

### Storage 

To estimate initial storage requirements, begin with a Mattermost server approximately 600 MB to 800 MB in size including operating system and database, then add the multiplied product of:

- Estimated storage per user per month (see below), multipled by 12 months in a year
- Estimated mean average number of users in a year
- A 1-2x safety factor

**Estimated storage per user per month**

File usage per user varies significantly across industries. The below benchmarks are recommended: 

- **Low usage teams** (1-5 MB/user/month) - Primarily use text-messages and links to communicate. Examples would include software development teams that heavily use web-based document creation and management tools, and therefore rarely upload files to the server. 
 
- **Medium usage teams** (5-25 MB/user/month) - Use a mix of text-messages as well as shared documents and images to communicate. Examples might include business teams that may commonly drag and drop screenshots, PDFs and Microsoft Office documents into Mattermost for sharing and review. 

- **High usage teams** - (25-100 MB/user/month) - Heaviest utlization comes from teams uploading a high number of large files into Mattermost on a regular basis. Examples include creative teams who share and store artwork and media with tags and commentary in a pipeline production process. 
 
*Example:* A 30-person team with medium usage (5-25 MB/user/month) with a safety factor of 2x would require between 300 MB (30 users * 5 MB * 2x safety factor) and 1500 MB (30 users * 25 MB * 2x safety factor) of free space in the next year. 

It's recommended to review storage utilization at least quarterly to ensure adequate free space is available. 

