```markdown
# Lab 03: Bash Scripting for Network Reconnaissance

**Date:** 16/01/2026
**Status:** Completed
**Environment:** Kali Linux (VirtualBox)

## 1. Objective
To develop a custom automation tool using Bash scripting that performs a "Ping Sweep". The goal is to identify live hosts on a network segment without relying on third-party tools like Nmap initially.

## 2. Technical Implementation

### A. The Script Logic (`ipsweeper.sh`)
I wrote a script that utilizes a `for` loop to iterate through the last octet of an IP address (1-254).

**Key Concepts Used:**
*   **Shebang (`#!/bin/bash`):** Defines the interpreter.
*   **Input Argument (`$1`):** Takes the network prefix (e.g., `10.0.0`) from the user.
*   **Parallel Processing (`&`):** Allows multiple pings to run simultaneously for speed.
*   **Stream Manipulation:** Used `grep` to filter for successful responses ("64 bytes") and `cut`/`tr` to clean the output.

### B. Execution & Results

**1. Network Identification:**
I identified my own network interface using `ip a`.
*   **My IP:** `10.0.0.51`
*   **Target Subnet:** `10.0.0.x`

**2. Permissions:**
```bash
chmod +x ipsweeper.sh

3. Running the Tool: 

./ipsweeper.sh 10.0.0
4. Findings (Live Hosts):
The script successfully discovered the following active devices on the network:
10.0.0.1 (Gateway)
10.0.0.51 (Host - Kali)
10.0.0.23
10.0.0.6
10.0.0.5
10.0.0.17
3. Conclusion
I successfully automated the process of host discovery. Instead of manually pinging 254 addresses, I created a tool that does it in seconds. This demonstrates the power of Bash scripting for offensive security reconnaissance.
