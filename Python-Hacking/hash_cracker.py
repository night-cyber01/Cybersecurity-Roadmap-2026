import hashlib
import sys

# 1. Target Validation
if len(sys.argv) != 3:
    print("Invalid Syntax")
    print("Usage: python3 hash_cracker.py <MD5_HASH> <WORDLIST_FILE>")
    sys.exit()

target_hash = sys.argv[1]
wordlist_file = sys.argv[2]

print("-" * 50)
print(f"Target Hash: {target_hash}")
print(f"Wordlist: {wordlist_file}")
print("-" * 50)

# 2. The Cracking Process (Dictionary Attack)
try:
    # Open the wordlist in read mode
    with open(wordlist_file, "r") as file:
        for line in file:
            # Remove hidden newline characters (\n) from the text file
            word = line.strip()
            
            # Convert string to bytes, hash it with MD5, and get the hex format
            hashed_word = hashlib.md5(word.encode()).hexdigest()
            
            # Compare our generated hash with the target hash
            if hashed_word == target_hash:
                print(f"\n[+] PASSWORD CRACKED: {word}")
                sys.exit()
                
    # If the loop finishes without finding a match
    print("\n[-] Password not found in the wordlist.")

except FileNotFoundError:
    print("Error: Wordlist file not found.")
    sys.exit()
