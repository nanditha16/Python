# Demonstration for Lists:

# Creating Lists
my_list = [1, 2, 3, 'apple', 'banana']

# List Indexing
first_element = my_list[0]  # Access the first element (1)
print("First element:", first_element) # Output: First element: 1

# List Length
list_length = len(my_list)  # Length of the list (5)
print("List length:", list_length) # Output: List length: 5

# Appending to a List
my_list.append(4)  # Adds 4 to the end of the list
print("List after append 4:", my_list) # Output: List after append 4: [1, 2, 3, 'apple', 'banana', 4]

# Removing from a List
my_list.remove('apple')  # Removes 'apple' from the list
print("List after remove 'apple':", my_list) # Output: List after remove 'apple': [1, 2, 3, 'banana', 4]

# Slicing a List
subset = my_list[1:4]  # Creates a new list with elements at index 1, 2, and 3
print("Subset (slice):", subset) # Output: Subset (slice): [2, 3, 'banana']

# Concatenating Lists
new_list = my_list + [5, 6]  # Concatenates my_list with [5, 6]
print("New concatenated list with [5, 6]:", new_list) # Output: New concatenated list with [5, 6]: [1, 2, 3, 'banana', 4, 5, 6]


# Checking for an Element
is_present = 'banana' in my_list  # Checks if 'banana' is in the list (True)
print("Is 'banana' present?:", is_present) # Output: Is 'banana' present?: True
is_not_present = 'bananaaa' not in my_list  # Checks if 'bananaaa' is not in the list (True)
print("Is 'bananaaa' not present?:", is_not_present) # Output: Is 'bananaaa' not present?: True

# Sorting a List
# To sort, ensure all elements are of the same (comparable) type
numeric_list = [1, 2, 3, 4]
numeric_list.sort()  # Sorts the list in ascending order
print("numeric_list after ascending sort:", numeric_list) # Output: numeric_list after ascending sort: [1, 2, 3, 4]
numeric_list.sort(reverse=True)  # Sorts the list in descending order
print("numeric_list after descending sort:", numeric_list) # Output: numeric_list after descending sort: [4, 3, 2, 1]

# Popping from a List
popped_element = my_list.pop()  # Removes and returns the last element
print("Popped element:", popped_element) # Output: Popped element: 4
print("List after pop:", my_list) # Output: List after pop: [1, 2, 3, 'banana']

# Insert in a list
my_list.insert(1, 'orange')  # Insert 'orange' at index 1 in the list
print("List after insert at index 1:", my_list) # Output: List after insert at index 1: [1, 'orange', 2, 3, 'banana']

# Count occurrences in a list
count_banana = my_list.count('banana')  # Count occurrences of 'banana' in the list
print("Count of 'banana':", count_banana) # Output: Count of 'banana': 1

# Find index of the element in a list
index_banana = my_list.index('banana')  # Find index of the first occurrence of 'banana'
print("Index of 'banana':", index_banana) # Output: Index of 'banana': 4

# Extend the list 
my_list.extend(['grape', 'melon'])  # Extend the list by appending elements from another list
print("List after extend:", my_list) # Output: List after extend: [1, 'orange', 2, 3, 'banana', 'grape', 'melon']

 # shallow copy of a list
copy_list = my_list.copy()  # Make a shallow copy of the list
print("Copy of the list:", copy_list) # Output: Copy of the list: [1, 'orange', 2, 3, 'banana', 'grape', 'melon']

 # Clear all items from the list, 
my_list.clear()  # Remove all items from the list, resulting in an empty list
print("List after clear:", my_list) # Output: List after clear: []

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Demonstration for Tuple:

# Creating Tuple
my_tuple = (1, 2, 'apple', 'banana')

# Tuple Indexing
first_element_tuple = my_tuple[0]  # Access the first element (1)
print("First element of tuple:", first_element_tuple) # Output: First element of tuple: 1

# Tuple Length
tuple_length = len(my_tuple)  # Length of the tuple (4)
print("Tuple length:", tuple_length) # Output: Tuple length: 4

# Accessing Tuple Elements
second_element = my_tuple[1]  # Access the second element (2) | can only access their elements.
print("Second element of tuple:", second_element) # Output: Second element of tuple: 2

# Tuple Packing and Unpacking
coordinates = (3, 4)
x, y = coordinates  # Unpack the tuple into x and y (x=3, y=4)
print("Coordinates unpacked: x =", x, ", y =", y) # Output: Coordinates unpacked: x = 3 , y = 4

# Concatenating Tuples
new_tuple = my_tuple + (3.14, 'cherry')  # Concatenates my_tuple with a new tuple
print("New concatenated tuple with 'cherry' : ", new_tuple) # Output: New concatenated tuple with 'cherry' :  (1, 2, 'apple', 'banana', 3.14, 'cherry')

# Checking for an Element in Tuple
is_present_tuple = 'apple' in my_tuple  # Checks if 'apple' is in the tuple (True)
print("Is 'apple' present in tuple?:", is_present_tuple) # Output: Is 'apple' present in tuple?: True
is_not_present_tuple = 'bananaaa' not in my_tuple  # Checks if 'bananaaa' is not in the tuple (True)
print("Is 'bananaaa' not present in tuple?:", is_not_present_tuple) # Output: Is 'bananaaa' not present in tuple?: True

# Using Tuples for Multiple Return Values
# Tuples are often used to return multiple values from a function.
def get_coordinates():
    return (3, 4)

x, y = get_coordinates()  # Unpack the returned tuple (x=3, y=4)
print("Returned coordinates: x =", x, ", y =", y) # Output: Returned coordinates: x = 3 , y = 4