# Lab 10: Python Web Exploitation (Directory Fuzzing)

**Date:** 17/03/2026
**Status:** Completed
**Environment:** Kali Linux (Python 3, `requests` library)

## 1. Objective
To automate the discovery of hidden directories and files on a web server by developing a custom Directory Fuzzer in Python. The tool leverages a wordlist to perform brute-force HTTP requests and analyzes the server's response codes to identify potential attack vectors.

## 2. Key Concepts
*   **HTTP Request Automation:** Using the `requests.get()` method to programmatically send HTTP queries.
*   **Status Code Analysis:**
    *   `200 OK`: Directory/File exists and is accessible.
    *   `403 Forbidden`: Directory/File exists, but access is denied (High-value target).
    *   `301/302`: Redirection occurred.
    *   `404 Not Found`: Ignored to reduce noise in the output.
*   **Exception Handling:** Implementing `try-except` blocks (like `requests.exceptions.RequestException`) ensures the script continues running even if individual requests time out or fail.

## 3. Tool Execution & Evidence

**Command Executed:**
```bash
python3 dir_fuzzer.py http://example.com dir_wordlist.txt
Output:
code
Text
--------------------------------------------------
Target URL: http://example.com/
Wordlist:   dir_wordlist.txt
Starting Directory Fuzzing...
--------------------------------------------------

[-] Fuzzing Complete.
(Note: Output may vary based on the target and wordlist used. example.com is a static page, so no hidden directories from the short wordlist were expected to return 200/403, validating the 404 filtering logic).
4. Conclusion
I successfully built an automated web reconnaissance tool. This lab demonstrated how attackers map out a web application's hidden surface area. It also reinforced the importance of interpreting HTTP status codes programmatically to separate valuable intelligence from noise.
