# Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

# Method read4:
#     The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.
#     The return value is the number of actual characters read.
#     Note that read4() has its own file pointer, much like FILE *fp in C.

# Definition of read4:
#     Parameter:  char[] buf4
#     Returns:    int
# buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].

# Example:
# File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
# char[] buf4 = new char[4]; // Create buffer with enough space to store characters
# read4(buf4); // read4 returns 4. Now buf4 = "abcd", fp points to 'e'
# read4(buf4); // read4 returns 1. Now buf4 = "e", fp points to end of file
# read4(buf4); // read4 returns 0. Now buf4 = "", fp points to end of file

# Method read:

# By using the read4 method, implement the method read that reads n characters from file 
# and store it in the buffer array buf. Consider that you cannot manipulate file directly.
# The return value is the number of actual characters read.

#  Definition of read:
#     Parameters:	char[] buf, int n
#     Returns:	int

# buf[] is a destination, not a source. You will need to write the results to buf[].

# Note:
# Consider that you cannot manipulate the file directly. The file is only accessible for read4 but not for read.
# The read function will only be called once for each test case.
# You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.

# Constraints:
#     1 <= file.length <= 500
#     file consist of English letters and digits.
#     1 <= n <= 1000

# Time Complexity: O(n) Because in the worst case, we read one character at a time up to n.
# Space Complexity: O(1) Only a fixed-size buffer buf4 of size 4 is used.

"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class File:
    def __init__(self, content):
        self.content = content
        self.pointer = 0  # Simulates the file pointer

    def read4(self, buf4):
        count = 0
        while count < 4 and self.pointer < len(self.content):
            buf4[count] = self.content[self.pointer]
            self.pointer += 1
            count += 1
        return count

# Step-by-Step Explanation
#     Initialize a temporary buffer buf4 of size 4 to store characters read by read4.
#     Track the total number of characters read using total_read.
#     Loop until either:
#       We've read n characters, or
#       read4 returns 0 (end of file).
#     In each iteration:
#       Call read4(buf4) to read up to 4 characters.
#       Copy the minimum of count and n - total_read characters from buf4 to buf.
#       Update total_read accordingly.
#       Return the actual number of characters read.

class Solution:

    def __init__(self, file):
        self.file = file  # Instance of File class

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf4 = [''] * 4  # Temporary buffer for read4
        total_read = 0   # Total characters read so far

        while total_read < n:
            count = self.file.read4(buf4)
            # count = read4(buf4)  # Read up to 4 characters
            if count == 0:
                break  # End of file reached

            # Copy characters from buf4 to buf
            for i in range(min(count, n - total_read)):
                buf[total_read] = buf4[i]
                total_read += 1

        return total_read
    

# Step 1: Create the file object
file = File("abcdefghijk")  # or any string you want to simulate as file content

# Step 2: Pass the file object to Solution
sol = Solution(file)

# Step 3: Prepare the buffer and call read
buf = [''] * 1000  # buffer large enough to hold n characters
n = 7
actual_read = sol.read(buf, n)

# Step 4: Print results
print("Characters read:", actual_read)
print("Buffer content:", ''.join(buf[:actual_read]))

