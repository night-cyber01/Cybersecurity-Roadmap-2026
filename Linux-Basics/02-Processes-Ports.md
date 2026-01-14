Lab 02: Linux Process Management & Network Basics
Date: 14/01/2026
Status: Completed
Environment: Kali Linux (VirtualBox)
1. Objective
Simulate a Systems Administrator role to identify and terminate a "ghost" process consuming resources and detect an unauthorized open port (Backdoor).
2. Technical Steps
A. The Ghost Process (Process Management)
I created a background process to simulate a resource hog.
code
Bash
sleep 1000 &
Hunting the PID:
I used ps combined with grep to filter the process list.
code
Bash
ps aux | grep sleep
Output:
code
Text
nightwe+ 45349 0.0 0.0 3020 1628 pts/3 SN 14:44 0:00 sleep 1000
Termination:
I identified PID 45349 and terminated it gracefully using SIGTERM (-15).
code
Bash
kill -15 45349
# Output: [1] + terminated sleep 1000
B. The Backdoor (Networking & Ports)
I used netcat to open a listener on port 4444 (simulating a backdoor).
code
Bash
nc -lvnp 4444
Port Verification:
In a second terminal, I verified the port was open and listening using netstat.
code
Bash
sudo netstat -tulpn
Evidence (Missing in original, added here): 
 
tcp        0      0 0.0.0.0:4444            0.0.0.0:*               LISTEN      88384/nc 

Connection Test:
I established a local connection to the port.
code
Bash
nc 127.0.0.1 4444
Result: The message "Hello Hacker" was successfully received on the listener terminal.
