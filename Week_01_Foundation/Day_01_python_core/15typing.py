"""
=========================================
TOPIC 1: DYNAMIC VS. STATIC TYPING
=========================================

1. STATIC TYPING (e.g., C, C++, Java)
-------------------------------------
- Types are checked at COMPILE-TIME (before the code runs).
- You must declare the type of a variable explicitly.
- The VARIABLE has the type, not just the data.
- Example in C:
    int x = 5; 
    x = "hello"; // ERROR! x can only ever be an integer.

2. DYNAMIC TYPING (e.g., Python, JavaScript)
--------------------------------------------
- Types are checked at RUNTIME (while the code is running).
- You do not declare variable types.
- The OBJECT in memory has a type, the variable is just a nametag pointing to it.
- Example in Python:
    x = 5         # x points to an integer object
    x = "hello"   # x now points to a string object (Perfectly valid!)

PROS & CONS:
- Static: Faster execution, catches errors early, requires more verbose code.
- Dynamic: Faster development, highly flexible, but bugs might only show up when the code runs.
"""