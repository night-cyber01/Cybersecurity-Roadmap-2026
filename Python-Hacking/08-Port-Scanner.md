Objective: Develop a basic Port Scanner using Python's socket library to identify open TCP ports on a target system.
Key Libraries:
socket: To create network connections.
sys: To handle command-line arguments.
Code Logic:
Input: Takes an IP address as an argument.
Loop: Iterates through a range of ports (1-85).
Connection: Uses s.connect_ex() which returns 0 on success (Open Port) and an error code on failure (Closed/Filtered).
Timeout: Set to 1 second to prevent hanging.
Evidence: 


Escaneando objetivo: 10.0.0.1
Hora de inicio: 2026-03-04 16:01:12.175042
--------------------------------------------------
Puerto 53 esta ABIERTO
Puerto 80 esta ABIERTO
