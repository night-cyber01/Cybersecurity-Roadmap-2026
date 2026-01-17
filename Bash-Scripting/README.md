# IP Sweeper

A lightweight Bash script designed for network reconnaissance. It performs a Ping Sweep across a specified subnet to identify active hosts (Live Hosts).

## 📋 Features
- **Fast Execution:** Uses multi-threading (background processes) to scan 254 hosts in seconds.
- **Clean Output:** Filters response data to show only active IP addresses.
- **Input Validation:** Ensures the user provides the necessary network argument.

## 🚀 Usage

1. **Grant execution permissions:**
   ```bash
   chmod +x ipsweeper.sh
 
Run the script:
Provide the first three octets of the network you want to scan.

./ipsweeper.sh <Network_Prefix> 

💡 Example
If your IP is 10.0.0.51, you scan the 10.0.0.x range like this: 

./ipsweeper.sh 10.0.0 

Output:
 
10.0.0.1
10.0.0.5
10.0.0.6
...
