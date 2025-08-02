# This file demonstrates basic string operations in Python.

# String creation
my_string = "Hello, World!"
print(my_string) # Output: Hello, World!

# String concatenation
greeting = "Hello" 
name = "Alice"
message = greeting + ", " + name + "!"
print(message) # Output: Hello, Alice!

# String methods
print(my_string.replace("World", "Python")) # Output: Hello, Python!

# String case conversion
print(my_string.lower())  # Output: hello, world!
print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.capitalize())  # Output: Hello, world!
print(my_string.title())  # Output: Hello, World!

# String isdigit, isalpha, isalnum, isspace
print("123".isdigit())  # Output: True
print("abc".isalpha())  # Output: True
print("abc123".isalpha())  # Output: False
print("abc123".isalnum())  # Output: True
print("abc 123".isalnum())  # Output: False
print("   ".isspace())  # Output: True
print("abc".isspace())  # Output: False

# String formatting
age = 30
formatted_string = f"{name} is {age} years old."
print(formatted_string) # Output: Alice is 30 years old. 

# Multiline strings and String splitlines
multiline_string = """This is a string that spans
multiple lines."""
print(multiline_string) # Output: This is a string that spans
# multiple lines.

print(multiline_string.splitlines()) # Output: ['This is a string that spans', 'multiple lines.']

# String interpolation using format method
formatted_string = "Hello, {}. You are {} years old.".format(name, age)
print(formatted_string) # Output: Hello, Alice. You are 30 years old.

# String interpolation using f-strings
formatted_string_f = f"Hello, {name}. You are {age} years old."
print(formatted_string_f) # Output: Hello, Alice. You are 30 years old.

# String interpolation using percent formatting
formatted_string_percent = "Hello, %s. You are %d years old." % (name, age)
print(formatted_string_percent) # Output: Hello, Alice. You are 30 years old.

# String format with keyword arguments
formatted_string_keyword = "Hello, {name}. You are {age} years old.".format(name=name, age=age)
print(formatted_string_keyword) # Output: Hello, Alice. You are 30 years old.

# String format_map
data = {'name': 'Alice', 'age': 30}
formatted_string = "Hello, {name}. You are {age} years old.".format_map(data)
print(formatted_string) # Output: Hello, Alice. You are 30 years old.

# String interpolation with dictionaries
formatted_string_dict = "Hello, {name}. You are {age} years old.".format_map(data)
print(formatted_string_dict) # Output: Hello, Alice. You are 30 years old.

# Escape characters
escaped_string = "She said, \"Hello!\""
print(escaped_string)  # Output: She said, "Hello!"

# Raw strings
raw_string = r"C:\Users\Alice\Documents"
print(raw_string)  # Output: C:\Users\Alice\Documents

# String repetition
print(my_string * 2)  # Output: Hello, World!Hello, World!

# Checking string length
print(len(my_string))  # Output: 13
print(len(multiline_string))  # Output: 43

# String iteration
for char in my_string:
    print(char, end=' ')  # Output: H e l l o ,   W o r l d !
print()  # New line after iteration

# String comparison
print(my_string == "Hello, World!")  # Output: True
print(my_string != "Hello, World!")  # Output: False
print(my_string < "Hello, World!")   # Output: False
print(my_string > "Hello, World!")   # Output: False

# String indexing
print(my_string[0])  # Output: H
print(my_string[-1])  # Output: !
print(my_string[7])  # Output: W

# String methods for searching and counting
print(my_string.index("World"))  # Output: 7
# print(my_string.index("Python"))  # Raises ValueError if not found

# String count
print(my_string.count("o"))  # Output: 2
print(my_string.count("l"))  # Output: 3

# String rfind
print(my_string.rfind("World"))  # Output: 7
print(my_string.rfind("Python"))  # Output: -1 (not found)

# String find
print(my_string.find("World"))  # Output: 7
print(my_string.find("Python"))  # Output: -1 (not found)

# String startswith and endswith
print(my_string.startswith("Hello"))  # Output: True
print(my_string.endswith("!"))         # Output: True

# String slicing
print(my_string[0:5])  # Output: Hello
print(my_string[7:12])  # Output: World

# String slicing with step
print(my_string[::2])  # Output: Hlo ol!
print(my_string[1::2])  # Output: el,Wrd

# String slicing with negative indices
print(my_string[-6:-1])  # Output: World
print(my_string[-7:])    # Output:  World!

# String slicing with step and negative indices
print(my_string[::-1])  # Output: !dlroW ,olleH
print(my_string[-1::-1])  # Output: !dlroW ,olleH

# String slicing with step and range
print(my_string[0:5:1])  # Output: Hello
print(my_string[7:12:1])  # Output: World

# String slicing with step and negative range
print(my_string[-6:-1:1])  # Output: World

# Checking for substring
print("World" in my_string)  # Output: True
print("Python" in my_string)  # Output: False

# Checking for substring with if statement
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")
else:
    print(substring, "not found in the text")

# Splitting a string
print(my_string.split(","))  # Output: ['Hello', ' World!']

# String split and rsplit
print(my_string.split(","))  # Output: ['Hello', ' World!']
print(my_string.rsplit(",", 1))  # Output: ['Hello', ' World!']

# Joining a list of strings
print(", ".join(['Hello', 'World!']))  # Output: Hello, World!

# String strip
print(my_string.strip())  # Output: Hello, World!
print(my_string.strip("!"))  # Output: Hello, World
print(my_string.strip("Hello, "))  # Output: World!

# String lstrip and rstrip
print(my_string.lstrip("Hello, "))  # Output: World!
print(my_string.rstrip("!"))  # Output: Hello, World

# String ljust, rjust, and center
print(my_string.ljust(20))  # Output: Hello, World!
print(my_string.rjust(20))  # Output:      Hello, World!
print(my_string.center(20))  # Output:   Hello, World!

# String swapcase
print(my_string.swapcase())  # Output: hELLO, wORLD!

# String zfill
print("42".zfill(5))  # Output: 00042
print("hello".zfill(10))  # Output: 00000hello

# String partition
print(my_string.partition("World"))  # Output: ('Hello, ', 'World', '!')
print(my_string.partition("Python"))  # Output: ('Hello, World!', '', '')

# String rpartition
print(my_string.rpartition("World"))  # Output: ('Hello, ', 'World', '!')
print(my_string.rpartition("Python"))  # Output: ('', '', 'Hello, World!')

# String casefold
print(my_string.casefold())  # Output: hello, world!

# String translate
translation_table = str.maketrans("aeiou", "12345")
print(my_string.translate(translation_table))  # Output: H2ll4, W4rld!

# String encode and decode
encoded_string = my_string.encode('utf-8')
print(encoded_string)  # Output: b'Hello, World!'
decoded_string = encoded_string.decode('utf-8')
print(decoded_string)  # Output: Hello, World!

# String isprintable
print(my_string.isprintable())  # Output: True
print("Hello\nWorld".isprintable())  # Output: False

