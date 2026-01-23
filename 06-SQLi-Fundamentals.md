# Lab 06: SQL Injection (SQLi) - Retrieving Hidden Data

**Date:** 23/01/2026
**Status:** Solved
**Environment:** PortSwigger Academy (Burp Suite Repeater)

## 1. Objective
To exploit a SQL Injection vulnerability in the `WHERE` clause of a product filter to bypass logic and retrieve unreleased products.

## 2. Vulnerability Analysis
The application constructs a SQL query by directly concatenating user input without sanitization.
*   **Injection Point:** The `category` parameter in the URL.
*   **Goal:** Inject a boolean condition (`OR 1=1`) that always evaluates to TRUE.

## 3. Technical Steps
1.  Intercepted the request using **Burp Suite Proxy**.
2.  Sent the request to **Repeater** for testing.
3.  Identified the injection point: `GET /filter?category=Gifts`
4.  **Payload Construction:**
    *   `'` : Closes the string literal.
    *   `OR 1=1` : The "True" condition.
    *   `--` : The comment indicator.
    *   `+` : URL-encoded space (Critical for the comment to work).
5.  **Final Payload:** `Gifts'+OR+1=1--+`

## 4. Execution & Result
*   **Modified Request:**
    ```http
    GET /filter?category=Gifts'+OR+1=1--+ HTTP/2
    ...
    ```
*   **Response:** The server returned a `200 OK` and displayed all products, including those with `released=0`. The lab was marked as "Solved".

## 5. Conclusion
I learned that syntax precision is vital in SQLi. A missing space (represented by `+` in the URL) caused the initial payload to fail. The injection successfully neutralized the rest of the original query using the comment sequence.
