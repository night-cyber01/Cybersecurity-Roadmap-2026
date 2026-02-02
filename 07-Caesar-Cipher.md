# Lab 07: Python Basics & Classical Cryptography (Caesar Cipher)

**Date:** 02/02/2026
**Status:** Completed
**Environment:** Kali Linux (Python 3)

## 1. Objective
To understand the fundamentals of Python programming and classical cryptography by developing a script that encrypts messages using the Caesar Cipher algorithm.

## 2. Key Concepts
*   **ASCII Conversion:** Computers process text as numbers. 
    *   `ord()` converts a character to its ASCII integer (e.g., 'A' = 65).
    *   `chr()` converts an integer back to a character.
*   **Modulo Operator (`%`):** Used to wrap the alphabet around. If the shift goes past 'Z' (90), the modulo operator (`% 26`) ensures it loops back to 'A' (65), acting like a clock.

## 3. Code Logic
The script processes the input string character by character:
1.  **Convert** the letter to its ASCII value.
2.  **Normalize** the value to a 0-25 scale (by subtracting 65).
3.  **Shift** the value by the key and apply `% 26` to handle wrap-around.
4.  **Denormalize** back to the ASCII scale (by adding 65).
5.  **Convert** the new ASCII value back to a character.

## 4. Execution & Evidence

**Test 1: Standard Shift**
```text
Ingresa el mensaje (MAYUSCULAS): HOLA
Ingresa la clave numerica (ej. 3): 1
Mensaje Original: HOLA
Mensaje Cifrado:  IPMB 

Test 2: Wrap-around Test (Z to A) 

Ingresa el mensaje (MAYUSCULAS): ZAPATO
Ingresa la clave numerica (ej. 3): 1
Mensaje Original: ZAPATO
Mensaje Cifrado:  ABQBUP
5. Conclusion
I successfully wrote my first cryptographic tool in Python. This lab demonstrated how mathematical operations (specifically the modulo operator) are used to manipulate data streams and secure information.
