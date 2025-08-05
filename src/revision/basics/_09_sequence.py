# Demonstration for Lists:

# Creating Lists
my_list = [1, 2, 3, 'apple', 'banana']

# List Indexing
first_element = my_list[0]  # Access the first element (1)
print("First element:", first_element)

# List Length
list_length = len(my_list)  # Length of the list (5)
print("List length:", list_length)

# Appending to a List
my_list.append(4)  # Adds 4 to the end of the list
print("List after append 4:", my_list)

# Removing from a List
my_list.remove('apple')  # Removes 'apple' from the list
print("List after remove 'apple':", my_list)

# Slicing a List
subset = my_list[1:4]  # Creates a new list with elements at index 1, 2, and 3
print("Subset (slice):", subset)

# Concatenating Lists
new_list = my_list + [5, 6]  # Concatenates my_list with [5, 6]
print("New concatenated list with [5, 6]:", new_list)


# Checking for an Element
is_present = 'banana' in my_list  # Checks if 'banana' is in the list (True)
print("Is 'banana' present?:", is_present)
is_not_present = 'bananaaa' not in my_list  # Checks if 'bananaaa' is not in the list (True)
print("Is 'bananaaa' not present?:", is_not_present)

# Sorting a List
# To sort, ensure all elements are of the same (comparable) type
numeric_list = [1, 2, 3, 4]
numeric_list.sort()  # Sorts the list in ascending order
print("numeric_list after ascending sort:", numeric_list)
numeric_list.sort(reverse=True)  # Sorts the list in descending order
print("numeric_list after descending sort:", numeric_list)

# Popping from a List
popped_element = my_list.pop()  # Removes and returns the last element
print("Popped element:", popped_element)
print("List after pop:", my_list)

# Insert in a list
my_list.insert(1, 'orange')  # Insert 'orange' at index 1 in the list
print("List after insert at index 1:", my_list)

# Count occurrences in a list
count_banana = my_list.count('banana')  # Count occurrences of 'banana' in the list
print("Count of 'banana':", count_banana)

# Find index of the element in a list
index_banana = my_list.index('banana')  # Find index of the first occurrence of 'banana'
print("Index of 'banana':", index_banana)

# Extend the list 
my_list.extend(['grape', 'melon'])  # Extend the list by appending elements from another list
print("List after extend:", my_list)

 # shallow copy of a list
copy_list = my_list.copy()  # Make a shallow copy of the list
print("Copy of the list:", copy_list)

 # Clear all items from the list, 
my_list.clear()  # Remove all items from the list, resulting in an empty list
print("List after clear:", my_list)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Demonstration for Tuple:

# Creating Tuple
my_tuple = (1, 2, 'apple', 'banana')

# Tuple Indexing
first_element_tuple = my_tuple[0]  # Access the first element (1)
print("First element of tuple:", first_element_tuple)

# Tuple Length
tuple_length = len(my_tuple)  # Length of the tuple (4)
print("Tuple length:", tuple_length)

# Accessing Tuple Elements
second_element = my_tuple[1]  # Access the second element (2) | can only access their elements.
print("Second element of tuple:", second_element)

# Tuple Packing and Unpacking
coordinates = (3, 4)
x, y = coordinates  # Unpack the tuple into x and y (x=3, y=4)
print("Coordinates unpacked: x =", x, ", y =", y)

# Concatenating Tuples
new_tuple = my_tuple + (3.14, 'cherry')  # Concatenates my_tuple with a new tuple
print("New concatenated tuple with 'cherry' : ", new_tuple)

# Checking for an Element in Tuple
is_present_tuple = 'apple' in my_tuple  # Checks if 'apple' is in the tuple (True)
print("Is 'apple' present in tuple?:", is_present_tuple)
is_not_present_tuple = 'bananaaa' not in my_tuple  # Checks if 'bananaaa' is not in the tuple (True)
print("Is 'bananaaa' not present in tuple?:", is_not_present_tuple)

# Using Tuples for Multiple Return Values
# Tuples are often used to return multiple values from a function.
def get_coordinates():
    return (3, 4)

x, y = get_coordinates()  # Unpack the returned tuple (x=3, y=4)
print("Returned coordinates: x =", x, ", y =", y)
