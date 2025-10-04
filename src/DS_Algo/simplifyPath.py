# You are given an absolute path for a Unix-style file system, 
# which always begins with a slash '/'. Your task is to transform 
# this absolute path into its simplified canonical path.

# The rules of a Unix-style file system are as follows:
#     A single period '.' represents the current directory.
#     A double period '..' represents the previous/parent directory.
#     Multiple consecutive slashes such as '//' and '///' are treated 
#     as a single slash '/'.
#     Any sequence of periods that does not match the rules above should 
#     be treated as a valid directory or file name. For example, '...'
#     and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:
#     The path must start with a single slash '/'.
#     Directories within the path must be separated by exactly one 
#     slash '/'.
#     The path must not end with a slash '/', unless it is the root 
#     directory.
#     The path must not have any single or double periods ('.' and '..')
#      used to denote current or parent directories.
# Return the simplified canonical path.

# Example:
# Input: path = "/home/"
# Output: "/home"
# Explanation:
# The trailing slash should be removed.

# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation:
# Multiple consecutive slashes are replaced by a single one.

# Input: path = "/home/user/Documents/../Pictures"
# Output: "/home/user/Pictures"
# Explanation:
# A double period ".." refers to the directory up a level (the parent directory).

# Input: path = "/../"
# Output: "/"
# Explanation:
# Going one level up from the root directory is not possible.

# Input: path = "/.../a/../b/c/../d/./"
# Output: "/.../b/d"
# Explanation:
# "..." is a valid name for a directory in this problem.

# Constraints:
#     1 <= path.length <= 3000
#     path consists of English letters, digits, period '.', slash '/' or '_'.
#     path is a valid absolute Unix path.

# Time Complexity - Total: O(n)
#     Splitting path: O(n)
#     Iterating parts: O(n)
#     Stack operations: O(1) per operation
# Space Complexity - Total: O(n)
#     Stack: O(n) in worst case (all valid directories)

# Step-by-Step Explanation
# Example: Input: path = "/.../a/../b/c/../d/./"
# Step 1: Split the path
#     parts = ['', '...', 'a', '..', 'b', 'c', '..', 'd', '.', '']
# Step 2: Process each part using a stack
#     Part Action Stack
#     '' skip []
#     '...'append['...']
#     'a'append['...', 'a']
#     '..'pop['...']
#     'b'append['...', 'b']
#     'c'append['...', 'b', 'c']
#     '..'pop['...', 'b']
#     'd'append['...', 'b', 'd']
#     '.'skip['...', 'b', 'd']
#     ''skip['...', 'b', 'd']
# Step 3: Join the stack
#     Output: "/.../b/d"

# Edge Case Handling
#     Multiple slashes: '//' and '///' are treated as one → handled by split('/')
#     Single period .: Ignored as current directory
#     Double period ..: Pops from stack if possible
#     Other period sequences like '...' or '....': Treated as valid directory names
#     Root directory /: Returns '/' if stack is empty

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')

        for part in parts:
            if part == '' or part == '.':
                continue  # Skip empty and current directory
            elif part == '..':
                if stack:
                    stack.pop()  # Go up one directory
            else:
                stack.append(part)  # Valid directory or file name

        # Join the stack to form the canonical path
        return '/' + '/'.join(stack)
