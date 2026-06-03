"""
===================================================
TOPIC 2: MEMORY MANAGEMENT & REFERENCE COUNTING
===================================================

1. MEMORY MANAGEMENT IN PYTHON
------------------------------
- Python uses Automatic Memory Management.
- Developers don't manually allocate/free memory like in C.
- Everything in Python is an object stored in a private heap space.

2. REFERENCE COUNTING (The Primary Mechanism)
---------------------------------------------
- Every object in Python maintains a "reference count".
- This count increases when:
    - You assign the object to a new variable (b = a)
    - You put the object in a list/dict (my_list.append(a))
    - You pass it as an argument to a function
- This count decreases when:
    - A variable goes out of scope (e.g., a function ends)
    - You delete the variable (del a)
    - The variable is reassigned to something else
- RULE: When the reference count hits ZERO, the memory is immediately freed.

3. HOW TO CHECK REFERENCE COUNTS
--------------------------------
import sys
a = "hello world"
# sys.getrefcount(a) returns the count. 
# (Note: passing 'a' into the function temporarily adds +1 to the count!)
print(sys.getrefcount(a)) 

4. CYCLIC GARBAGE COLLECTION (The Backup Mechanism)
---------------------------------------------------
- What if list_1 contains list_2, and list_2 contains list_1?
- This is a "Circular Reference". Their counts will never naturally reach 0.
- Python has a built-in "Garbage Collector" (GC) module that periodically 
  detects these useless cycles and deletes them to prevent memory leaks.
"""
import sys
a = "hello world"
x = sys.getrefcount(a) 
print(x)