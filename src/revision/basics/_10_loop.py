import sys
import os


# Demonstration of 'for' loops with comments

# using range
for i in range(3):
	print(f"Iteration {i}")

# Using list - number
for num in [1, 2, 3]:
    print(num)

# Using list - list of strings
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using Index 
for index in range(len(fruits)):
    print(index, fruits[index])

# Using list - String
name = "test"
for char in name:
    print(char)

# Using Tuple - number
numbers = (1, 2, 3)
for num in numbers:
    print(num)

# Tuple + String example (nested loop)
words = ('hi', 'loop')
for word in words:
    for char in word:
        print(char, end=' ')
    print()

# Demonstration of 'while' loops with comments
count = 0
while count < 3:
    print(count)
    count += 1

# NOTE: Always ensure the loop condition changes inside the loop to avoid an infinite loop.
# Loop Controls: - continue
# Using while
i = 0
while i < 5:
    if i == 3:
        i += 1
        continue  # skips printing 3
    print(i)
    i += 1

# Using for 
for i in range(5):
    if i == 3:
        continue  # skips printing 3
    print(i)

# Loop Controls: - break
# Using while
i = 0
while i < 5:
    if i == 3:
        break   # stops loop when i = 3
    print(i)
    i += 1
# Using for
for i in range(5):
    if i == 3:
        break   # stops loop when i = 3
    print(i)

# Demonstrate using pass (does nothing, used when a statement is required syntactically)
# Using while
i = 0
while i < 5:
    if i == 2:
        pass  # Placeholder: does nothing
    else:
        print(i)
    i += 1
# Using for
for i in range(5):
    if i == 2:
        pass  # Placeholder: does nothing
    else:
        print(i)

# Use case: Count how many vowels are in a word
def count_vowels(word):
    vowel_count = 0
    for char in word:
        if char.lower() in "aeiou":
            vowel_count += 1
    return vowel_count

if __name__ == "__main__":
     word = "Python"
     # Use case: Count how many vowels are in a word
     print(f"Number of vowels in '{word}': {count_vowels(word)}")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Demonstration for dict:
import os

def list_files_in_folder(folder_path):
    """Returns a list of files in the given folder with error handling."""
    try:
        abs_path = os.path.abspath(folder_path)

        if not os.path.exists(abs_path):
            raise FileNotFoundError(f"Folder not found: {abs_path}")
        if not os.path.isdir(abs_path):
            raise NotADirectoryError(f"Not a directory: {abs_path}")

        return [f for f in os.listdir(abs_path) if os.path.isfile(os.path.join(abs_path, f))]

    except FileNotFoundError as fnf_error:
        print(f" {fnf_error}")
    except PermissionError as perm_error:
        print(f" Permission denied: {perm_error}")
    except NotADirectoryError as nd_error:
        print(f" {nd_error}")
    except OSError as os_error:
        print(f" OS error: {os_error}")
    except Exception as e:
        print(f" Unexpected error: {e}")

    return []

def main():
    try:
        # Usgae: Enter a list of folder paths separated by space:
        # /workspaces/Python/src /workspaces/Python/utility
        folder_input = input("Enter a list of folder paths separated by space:\n")
        folder_paths = folder_input.strip().split()

        for folder in folder_paths:
            abs_folder = os.path.abspath(folder)
            print(f"\n📁 Files in: {abs_folder}")
            files = list_files_in_folder(folder)
            if files:
                for file in files:
                    print(f"  - {file}")
            else:
                print("  (No files found or folder inaccessible)")
    except KeyboardInterrupt:
        print("\n Interrupted by user.")
    except Exception as e:
        print(f" Unexpected error in main: {e}")

if __name__ == "__main__":
    main()