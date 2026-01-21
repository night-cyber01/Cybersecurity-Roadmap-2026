# Lab 04: Network Traffic Sniffing with Tcpdump

**Date:** 21/01/2026
**Status:** Completed
**Environment:** Kali Linux (VirtualBox)

## 1. Objective
To practically analyze the OSI Model (specifically Layer 3 - Network) by intercepting and inspecting real-time traffic. The goal was to capture ICMP packets to verify the request/reply flow and confirm that Ping uses ICMP, not TCP or UDP.

## 2. Technical Implementation

### A. Interface Identification
First, I identified the active network interface assigned to my machine.
```
ip a
# Interface identified: eth0
# IP Address: 10.0.0.59
B. Setting up the Sniffer
I used tcpdump, a command-line packet analyzer, to listen on interface eth0. I applied a filter to capture only icmp traffic, ignoring everything else.

sudo tcpdump -i eth0 icmp 

C. Generatring Traffic
In a separate terminal, I sent a single ICMP Echo Request to Google's DNS.

ping -c 1 8.8.8.8 

3. Evidence & Analysis
Captured Traffic (From Tcpdump):

09:29:38.382559 IP 10.0.0.59 > dns.google: ICMP echo request, id 255, seq 1, length 64
09:29:38.419948 IP dns.google > 10.0.0.59: ICMP echo reply, id 255, seq 1, length 64
Packet Breakdown:
The Request: The log shows traffic going FROM my IP (10.0.0.59) TO Google (dns.google). The flag echo request confirms the outgoing question.
The Reply: The log shows traffic coming FROM Google TO my IP. The flag echo reply confirms the successful answer. 

4. Conclusion
I successfully intercepted network traffic "on the wire". This lab proved that the ping utility utilizes the ICMP protocol. By using tcpdump, I was able to see the invisible handshake that occurs during a simple connectivity test.
