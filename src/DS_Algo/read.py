# Read N Characters Given Read4 II - Call multiple times
# Given a file and assume that you can only read the file using a given method read4, 
# implement a method read to read n characters. Your method read may be called multiple times.

# Method read4:
# The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.
# The return value is the number of actual characters read.
# Note that read4() has its own file pointer, much like FILE *fp in C.

# Definition of read4:
#     Parameter:  char[] buf4
#     Returns:    int
# buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].

# File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
# char[] buf4 = new char[4]; // Create buffer with enough space to store characters
# read4(buf4); // read4 returns 4. Now buf4 = "abcd", fp points to 'e'
# read4(buf4); // read4 returns 1. Now buf4 = "e", fp points to end of file
# read4(buf4); // read4 returns 0. Now buf4 = "", fp points to end of file

# Method read:
# By using the read4 method, implement the method read that reads n characters from file 
# and store it in the buffer array buf. Consider that you cannot manipulate file directly.
# The return value is the number of actual characters read.

# Definition of read:
#     Parameters:	char[] buf, int n
#     Returns:	int
# buf[] is a destination, not a source. You will need to write the results to buf[].

# Note:
# Consider that you cannot manipulate the file directly. The file is only accessible for read4 but not for read.
# The read function may be called multiple times.
# Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. Please see here for more details.
# You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
# It is guaranteed that in a given test case the same buffer buf is called by read.

# Constraints:
# 1 <= file.length <= 500
# file consist of English letters and digits.
# 1 <= queries.length <= 10
# 1 <= queries[i] <= 500

# Time Complexity: O(n) — We read up to n characters.
# Space Complexity: O(1) — Only a fixed-size buffer is used.

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

# Explanation
# self.buffer: stores up to 4 characters from read4.
# self.buf_ptr: tracks how many characters have been consumed from self.buffer.
# self.buf_count: tracks how many characters were read by read4.
# Each time read() is called:

# If self.buffer is empty, we refill it using read4.
# We copy characters from self.buffer to buf until:
    # We reach n characters, or
    # We exhaust the file.


from typing import List

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

# Shared file pointer backing read4 mocked - local testing
class File:
    def __init__(self, content: str):
        self.content = content
        self.pointer = 0  # Simulates the file pointer

    def read4(self, buf4: List[str]) -> int:
        count = 0
        while count < 4 and self.pointer < len(self.content):
            buf4[count] = self.content[self.pointer]
            self.pointer += 1
            count += 1
        return count
    
# Global read4 expected by Solution
file = File("abc")
def read4(buf4):
    return file.read4(buf4)


class Solution:
    # Your Solution with persistent internal buffer - leetcode
    # def __init__(self):
    #     self.buffer = [''] * 4  # Internal buffer to store leftover characters
    #     self.buf_ptr = 0        # Pointer to current position in internal buffer
    #     self.buf_count = 0      # Number of valid characters in internal buffer
    
    # Your Solution with persistent internal buffer - local testing 
    def __init__(self, file: File):
        self.file = file
        self.buffer = [''] * 4
        self.buf_ptr = 0
        self.buf_count = 0

    def read(self, buf: List[str], n: int) -> int:
        total_read = 0

        while total_read < n:
            # If internal buffer is empty, call read4
            if self.buf_ptr == self.buf_count:
                # self.buf_count = read4(self.buffer) - leetcode
                self.buf_count = self.file.read4(self.buffer) # local testing
                self.buf_ptr = 0
                if self.buf_count == 0:
                    break  # End of file

            # Copy from internal buffer to buf
            while total_read < n and self.buf_ptr < self.buf_count:
                # buf[total_read] = self.buffer[self.buf_ptr]  # write directly  - leetcode
                buf.append(self.buffer[self.buf_ptr]) # local testing
                self.buf_ptr += 1
                total_read += 1

        return total_read

# Step 1: Create the file object
file = File("abc")  # or any string you want to simulate as file content

# Step 2: Pass the file object to Solution
sol = Solution(file)


buf1 = []
print(sol.read(buf1, 1))  # Output: 1, buf1 = ['a']

buf2 = []
print(sol.read(buf2, 2))  # Output: 2, buf2 = ['b', 'c']

buf3 = []
print(sol.read(buf3, 1))  # Output: 0, buf3 = []

