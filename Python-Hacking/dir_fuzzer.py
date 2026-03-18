import requests
import sys

# 1. Target Validation
if len(sys.argv) != 3:
    print("Invalid Syntax")
    print("Usage: python3 dir_fuzzer.py <TARGET_URL> <WORDLIST_FILE>")
    print("Example: python3 dir_fuzzer.py http://example.com dir_wordlist.txt")
    sys.exit()

target_url = sys.argv[1]
wordlist_file = sys.argv[2]

# Ensure URL ends with a slash for clean concatenation
if not target_url.endswith('/'):
    target_url += '/'

print("-" * 50)
print(f"Target URL: {target_url}")
print(f"Wordlist:   {wordlist_file}")
print("Starting Directory Fuzzing...")
print("-" * 50)

# 2. The Fuzzing Process
try:
    with open(wordlist_file, "r") as file:
        for line in file:
            # Clean the word (remove \n)
            directory = line.strip()
            
            # Construct the full URL to test
            test_url = target_url + directory
            
            try:
                # Send HTTP GET request
                # timeout=3 prevents hanging on slow servers
                response = requests.get(test_url, timeout=3)
                
                # Analyze the Status Code
                if response.status_code == 200:
                    print(f"[+] FOUND (200 OK): {test_url}")
                elif response.status_code == 403:
                    print(f"[*] FORBIDDEN (403): {test_url} - (Potential Target)")
                elif response.status_code in [301, 302]:
                    print(f"[~] REDIRECT ({response.status_code}): {test_url}")
                # We silently ignore 404 (Not Found)
                
            except requests.exceptions.RequestException as e:
                # Handle connection errors gracefully without crashing
                print(f"[!] Error connecting to {test_url}")

    print("\n[-] Fuzzing Complete.")

except FileNotFoundError:
    print("Error: Wordlist file not found.")
    sys.exit()
except KeyboardInterrupt:
    print("\n[!] User aborted the scan.")
    sys.exit()
