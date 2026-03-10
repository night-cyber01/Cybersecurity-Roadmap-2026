# Lab 09: Python Hashing & Password Cracking (Dictionary Attack)

**Date:** 10/03/2026
**Status:** Completed
**Environment:** Kali Linux (Python 3)

## 1. Objective
To understand one-way cryptographic hashing by developing a Python script capable of performing a dictionary attack against an MD5 hash.

## 2. Key Concepts
*   **Hashing vs. Encryption:** Hashing is a one-way mathematical function. It cannot be reversed (decrypted). To "crack" a hash, an attacker must guess the input, hash it, and compare the outputs.
*   **Data Encoding:** Python's `hashlib` requires data to be in byte format (`.encode()`) before hashing.
*   **Data Sanitization:** When reading from a wordlist, hidden newline characters (`\n`) must be removed using `.strip()` to ensure the integrity of the string being hashed.

## 3. Tool Execution & Evidence

**Command Executed:**
```bash
python3 hash_cracker.py d7d3f2824701265b9a710955b253e20e wordlist.txt 

Output:
 
--------------------------------------------------
Target Hash: 8621ffdbc5698829397d97767ac13db3
Wordlist: wordlist.txt
--------------------------------------------------

[+] PASSWORD CRACKED: dragon 

Conclusion
I successfully built a functional password cracker. This lab demonstrated the vulnerability of using fast, outdated hashing algorithms like MD5 without a "salt". It also highlighted the effectiveness of dictionary attacks against weak, predictable passwords.
