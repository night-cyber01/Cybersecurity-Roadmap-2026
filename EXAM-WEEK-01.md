# Exam Week 01: Operation Broken Chain

**Date:** 26/01/2026
**Status:** PASSED
**Role:** Cybersecurity Trainee

## 🚩 Objective 1: Infrastructure Setup (Linux)
**Goal:** Create a secure "evidence locker" directory with strict permission controls and log root processes.

### 1. User & Directory Management
I created a restricted user agent and a secured directory.
```bash
# Creating the agent
sudo adduser ghost_agent

# Creating the directory
mkdir ~/evidence_locker

# Setting Ownership (User: Me, Group: Agent)
sudo chgrp ghost_agent ~/evidence_locker 

2. Access Control (Permissions)
I applied Octal Permissions 750 to ensure the agent can read/execute but not write, and others have no access. 

chmod 750 ~/evidence_locker 

Verification:

drwxr-x--- 2 nightweaver01 ghost_agent 4096 Jan 26 16:35 evidence_locker  

3. Process Logging
I captured all running processes owned by root using stream redirection.

ps aux | grep root > ~/evidence_locker/target_log.txt
 
Log Sample: 

root           1  0.0  0.0  24252 14476 ?        Ss   08:37   0:01 /sbin/init splash
root           2  0.0  0.0      0     0 ?        S    08:37   0:00 [kthreadd]
root         782  1.3  1.4 513384 238772 tty7    Ssl+ 08:37   6:39 /usr/lib/xorg/Xorg 

🚩 Objective 2: Web Infiltration (SQL Injection) 

Goal: Bypass the authentication mechanism of a corporate portal to access the administrator account without a password. 

1. Vulnerability Analysis 

The login form is vulnerable to SQL Injection. The application likely uses a query similar to:
SELECT * FROM users WHERE username = '$user' AND password = '$pass' 

2. The Attack Vector
 
I used a SQL comment sequence to neutralize the password verification check.
 
Target Field: Username
 
Payload: administrator'--
Logic:
administrator matches the target user.
' closes the data field.
-- comments out the rest of the query (ignoring the password requirement).

3. Execution & Proof
I intercepted the login request with Burp Suite (or modified the input directly) and injected the payload.
Result:
The application accepted the modified query and logged me in as the Administrator, bypassing the password check entirely.
(Status: Lab Solved)
