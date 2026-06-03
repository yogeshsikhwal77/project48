
text = "hello WORLD"

# Capitalizes only the very first letter of the string.
print("capitalize() :", text.capitalize())  # Output: Hello world

# Converts all characters to uppercase.
print("upper()      :", text.upper())       # Output: HELLO WORLD

# Converts all characters to lowercase.
print("lower()      :", text.lower())       # Output: hello world

# Capitalizes the first letter of every word.
print("title()      :", text.title())       # Output: Hello World

# Swaps cases: lower becomes upper, upper becomes lower.
print("swapcase()   :", text.swapcase())    # Output: HELLO world

# Aggressive lowercasing, mostly used for caseless matching.
print("casefold()   :", text.casefold())    # Output: hello world

text = "banana"

# Counts how many times a substring appears.
print("count('a')   :", text.count("a"))      # Output: 3

# Returns the lowest index position of a substring (-1 if not found).
print("find('n')    :", text.find("n"))       # Output: 2

# Returns the highest index position of a substring (searching from the right).
print("rfind('n')   :", text.rfind("n"))      # Output: 4

# Like find(), but crashes (ValueError) if the substring isn't found.
print("index('a')   :", text.index("a"))      # Output: 1

# Returns True if the string starts with the given substring.
print("startswith() :", text.startswith("b")) # Output: True

# Returns True if the string ends with the given substring.
print("endswith()   :", text.endswith("na"))  # Output: True

text = "  hello  "
text_num = "42"

# Removes whitespace from both ends.
print("strip()      :", repr(text.strip()))   # Output: 'hello'

# Removes whitespace from the left side only.
print("lstrip()     :", repr(text.lstrip()))  # Output: 'hello  '

# Removes whitespace from the right side only.
print("rstrip()     :", repr(text.rstrip()))  # Output: '  hello'

# Pads the string with zeros on the left until it reaches the specified length.
print("zfill(5)     :", text_num.zfill(5))    # Output: 00042

# Centers the string within a specific width, padding with a chosen character.
print("center(8,'-'):", text_num.center(8, '-')) # Output: ---42---

# Left-justifies the string, padding with a chosen character.
print("ljust(5,'*') :", text_num.ljust(5, '*'))  # Output: 42***

# Right-justifies the string, padding with a chosen character.
print("rjust(5,'*') :", text_num.rjust(5, '*'))  # Output: ***42


print("\n--- 4. SPLITTING AND JOINING ---")
text = "apple,banana,cherry"

# Splits the string into a list at the specified separator.
print("split(',')   :", text.split(","))      # Output: ['apple', 'banana', 'cherry']

# Splits the string at line breaks (\n).
text_lines = "Line1\nLine2"
print("splitlines() :", text_lines.splitlines()) # Output: ['Line1', 'Line2']

# Splits into a 3-part tuple: (before_separator, separator, after_separator).
text_part = "user@email.com"
print("partition('@'):", text_part.partition("@")) # Output: ('user', '@', 'email.com')

# Joins elements of an iterable (like a list) using the string as a separator.
my_list = ["A", "B", "C"]
print("join()       :", "-".join(my_list))   # Output: A-B-C


print("\n--- 5. REPLACING AND MODIFYING ---")
text = "I like cats"

# Replaces all occurrences of a substring with a new string.
print("replace()    :", text.replace("cats", "dogs")) # Output: I like dogs

# Removes a specific prefix (Python 3.9+).
text_pre = "prefix_data"
print("removeprefix():", text_pre.removeprefix("prefix_")) # Output: data

# Removes a specific suffix (Python 3.9+).
text_suf = "data_suffix"
print("removesuffix():", text_suf.removesuffix("_suffix")) # Output: data


print("\n--- 6. VALIDATION (IS... METHODS) ---")
# These all return Boolean values (True/False)

# True if ALL characters are letters (no spaces, no numbers).
print("isalpha()    :", "abc".isalpha())      # Output: True

# True if ALL characters are numbers.
print("isdigit()    :", "123".isdigit())      # Output: True

# True if ALL characters are letters OR numbers.
print("isalnum()    :", "a1".isalnum())       # Output: True

# True if ALL characters are whitespace (spaces, tabs, newlines).
print("isspace()    :", "   ".isspace())      # Output: True

# True if the string is Title Cased.
print("istitle()    :", "Hello World".istitle()) # Output: True

# True if ALL letters in the string are lowercase.
print("islower()    :", "abc".islower())      # Output: True

# True if ALL letters in the string are uppercase.
print("isupper()    :", "ABC".isupper())      # Output: True


# escape charactors 
# \n newline       \t tab       \' single quote   \\ backslash

a = 'Harry is a good boy\nbut not a bad \'boy\''


print(a)