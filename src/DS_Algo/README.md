30s Explanation (Interview Style)

#1. lengthOfLongestSubstring(self, s: str) -> int: Given a string s, find the length of the longest substring without duplicate characters.
    “I solve this using a sliding window with two pointers. I keep a hash map of each character’s last seen index. As I expand the right pointer, if a duplicate appears inside the window, I move the left pointer just past its previous index. At each step I update the max window size. This ensures each character is visited at most twice, so it runs in O(n) time with O(min(n, alphabet)) space.”
    #  O(n) time where n is the length of the string
    #  O(min(n, m)) space, where m is the size of the character set.

#2. myAtoi(self, s: str) -> int: converts a string to a 32-bit signed integer.
    “I implement atoi by parsing the string step by step. First, I skip leading spaces, then capture the sign if present. Next, I read digits while building the number, checking for overflow before each multiplication. If overflow happens, I clamp to INT_MAX or INT_MIN. Finally, I return the signed integer. This runs in O(n) time with O(1) space since I process each character once.”

#3. romanToInt(self, s: str) -> int: roman numeral to integer.
    “I map each Roman numeral to its integer value and iterate from right to left. If the current numeral is smaller than the previous one, I subtract it; otherwise, I add it. This correctly handles subtractive cases like IV or IX. The solution runs in O(n) time with O(1) extra space since I just scan once.”

#4. threeSum(self, nums: List[int]) -> List[List[int]]: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    “I solve 3Sum by first sorting the array, then fixing one element at a time and using a two-pointer approach to find the other two numbers. Sorting helps both with skipping duplicates and moving pointers efficiently. If the sum is zero, I add the triplet and move both pointers while skipping duplicates; if the sum is too small, I move left; if too large, I move right. Sorting takes O(n log n), and the two-pointer scan gives O(n²) overall time with O(1) extra space.”
    # Time Complexity: O(n²) 
    # Space Complexity: O(1) (excluding output list) . 

#5. removeDuplicates(self, nums: List[int]) -> int: Given an integer array nums sorted in ascending order, remove the duplicates in-place such that each unique element appears only once. 
    “Since the array is sorted, duplicates are adjacent. I use two pointers: one (k) to track the position of the next unique element, and one (i) to scan through the array. Whenever I find a new value, I place it at position k and increment k. This way, the first k elements of the array are unique. It runs in O(n) time with O(1) extra space.”
    # Time Complexity: O(n)
        # The loop runs from i = 1 to len(nums) - 1, so it iterates once per element in the array.
        # Each operation inside the loop is constant time: comparisons, assignments, and increments.
        # Therefore, the total time complexity is linear, or O(n), where n is the length of the input list nums.
    # Space Complexity: O(1)
        # No additional data structures are used.
        # The algorithm modifies the input list in-place.

#6. nextPermutation(self, nums: List[int]) -> None: Given an array of integers nums, find the next lexicographically permutation of nums.
    “To compute the next lexicographical permutation, I scan from the right to find the first index i where nums[i] < nums[i+1]. Then I find the smallest number greater than nums[i] to its right, swap them, and finally reverse the suffix after i to get the next smallest order. If no such i exists, the array is entirely non-increasing, so I reverse the whole thing to get the lowest order. This runs in O(n) time with O(1) space.”
    # Time Complexity:
        # Worst case:  O(n)
            # Finding the pivot: O(n)
            # Finding the successor: O(n)
            # Reversing the suffix: O(n)
    # Space Complexity: O(1) (in-place modification, no extra space used)

#7. multiply(self, num1: str, num2: str) -> str: Given two integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
    “To multiply two numbers given as strings, I simulate grade-school multiplication. I reverse both strings and use a result array of size m+n to store partial sums. For each digit pair, I multiply, add to the correct position, and carry over. After processing all pairs, I strip leading zeros and build the final string, adding a negative sign if needed. This works in O(m·n) time and O(m+n) space.”
    # Time: O(m⋅n)
    # Space: O(m+n)

#8. groupAnagrams(self, strs: List[str]) -> List[List[str]]: Given an array of strings strs, group the anagrams together.
    “I group words by their sorted character sequence. For each word, I sort its letters, use that as a key in a hash map, and append the word to that group. At the end, I return all the grouped values. Sorting each word takes O(k log k), so the overall complexity is O(n·k log k), where n is the number of words and k is the average word length.”
    # Time Complexity:    
        # Sorting each word: O(klogk)
        # For n words:  O(n⋅klogk) Where n is number of words, k is average word length
    # Space Complexity: O(n⋅k) for storing grouped anagrams

*** IMPORTNAT*** 
#9. addBinaryaddBinary(self, a: str, b: str) -> str: Given two binary strings a and b, return their sum as a binary string.
    “To add two binary strings, I simulate binary addition from right to left. At each step I add the corresponding bits plus a carry, compute the new bit (total % 2), and update the carry (total // 2). I keep appending results and reverse at the end. This handles unequal lengths naturally, and runs in O(n) time with O(n) space, where n is the max length of the inputs.”
    # Time Complexity: O(max(n,m)), Where n and m are lengths of a and b
    # Space Complexity: O(max(n,m)) For storing result  

*** IMPORTNAT*** 
#10. minWindow(self, s: str, t: str) -> str: Given two strings s and t of lengths m and n respectively, return  the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string ""
    “I use a sliding window with two pointers. I count required chars from t and scan s with a right pointer, updating a window map and a formed counter when a char meets its needed freq. When all required chars are satisfied (formed == required), I shrink from the left to find the smallest valid window, updating the best answer. Expanding and contracting each pointer at most |s| times gives O(|s| + |t|) time and O(Σ) space for the frequency maps.”
    # Time Complexity: O(m+n) Each character is visited at most twice (once by right, once by left)
    # Space Complexity: O(n) For storing character counts

#11. merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: Merge ascending two arrays into a single array sorted in ascending order.
    “I merge from the end to avoid shifting and extra space. I keep three pointers: i at the last real element of nums1, j at the end of nums2, and k at the write position (end of nums1). At each step I place the larger of nums1[i] or nums2[j] into nums1[k] and move pointers. When one side finishes, any remaining nums2 elements are copied over. This is O(m+n) time and O(1) extra space.”
    # Time Complexity: O(m+n) Each element is visited once
    # Space Complexity: O(1) In-place merge, no extra space used

#12. isPalindrome(self, s: str) -> bool: Is palindrom using Slicing or two pointers
    “I normalize the string to compare only alphanumerics case-insensitively. One approach builds a filtered lowercase list and checks if it equals its reverse — simple and Pythonic, O(n) time, O(n) space. More optimal on space uses two pointers from both ends, skipping non-alphanumerics and comparing lowercase characters; if any mismatch appears, return false, otherwise true. That keeps it O(n) time and O(1) extra space.”
    # Method i : using Slicing ([::-1]) - For quick, readable code in small-scale use → Slicing is fine.
    # Time Complexity:
        # Reversing the string: O(n)
        # Comparing strings: O(n)
        # Total: O(n)
    # Space Complexity: Creates a new reversed string →  O(n) extra space 

    # Method 2: using pointers - For performance and memory efficiency, especially with large strings 
    # Time Complexity: Single pass through the string → O(n) 
    # Space Complexity: No extra space used → O(1)