# Lab 05: HTTP Request Interception & Manipulation

**Date:** 22/01/2026
**Status:** Completed
**Environment:** Kali Linux (Burp Suite Community)

## 1. Objective
To configure a local proxy environment using Burp Suite and perform a "Man-in-the-Middle" (MITM) style interception. The goal was to capture an HTTP request in transit and modify its parameters before it reached the server, effectively bypassing client-side controls.

## 2. Tools Used
*   **Burp Suite Community Edition:** Proxy tool for intercepting HTTP/S traffic.
*   **Burp's Embedded Browser (Chromium):** Pre-configured browser to route traffic through the proxy.

## 3. Technical Steps

### A. Environment Setup
1.  Launched Burp Suite from the Kali terminal.
2.  Navigated to the **Proxy** tab and enabled **"Intercept is On"**.
3.  Opened the embedded browser to ensure traffic flow.

### B. The Interception
1.  **Target Action:** In the browser, I initiated a search query for the term `GATO`.
2.  **Capture:** The browser hung (loading state) because Burp Suite intercepted the outbound request.
3.  **Analysis:** I inspected the raw HTTP GET request in the Proxy tab.

**Original Request (Snippet):**
```http
GET /?search=GATO HTTP/1.1
Host: www.google.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 

C. The Manipulation
I manually edited the query parameter in the raw text area.
Changed search=GATO to search=HACKER.
Clicked "Forward" to release the modified packet to the server.
4. Results & Conclusion
The browser loaded the result page showing search results for "HACKER", despite the original user input being "GATO".
Security Implication:
This demonstrates that client-side input validation is insufficient. A malicious actor can bypass the browser's interface and communicate directly with the server, modifying any data (prices, user IDs, permissions) that isn't strictly validated on the backend.
