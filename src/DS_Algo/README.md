30s Explanation (Interview Style)

lengthOfLongestSubstring(self, s: str) -> int: Given a string s, find the length of the longest substring without duplicate characters.
    “I solve this using a sliding window with two pointers. I keep a hash map of each character’s last seen index. As I expand the right pointer, if a duplicate appears inside the window, I move the left pointer just past its previous index. At each step I update the max window size. This ensures each character is visited at most twice, so it runs in O(n) time with O(min(n, alphabet)) space.”
    #  O(n) time where n is the length of the string
    #  O(min(n, m)) space, where m is the size of the character set.

myAtoi(self, s: str) -> int: converts a string to a 32-bit signed integer.
    “I implement atoi by parsing the string step by step. First, I skip leading spaces, then capture the sign if present. Next, I read digits while building the number, checking for overflow before each multiplication. If overflow happens, I clamp to INT_MAX or INT_MIN. Finally, I return the signed integer. This runs in O(n) time with O(1) space since I process each character once.”

romanToInt(self, s: str) -> int: roman numeral to integer.
    “I map each Roman numeral to its integer value and iterate from right to left. If the current numeral is smaller than the previous one, I subtract it; otherwise, I add it. This correctly handles subtractive cases like IV or IX. The solution runs in O(n) time with O(1) extra space since I just scan once.”

threeSum(self, nums: List[int]) -> List[List[int]]: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    “I solve 3Sum by first sorting the array, then fixing one element at a time and using a two-pointer approach to find the other two numbers. Sorting helps both with skipping duplicates and moving pointers efficiently. If the sum is zero, I add the triplet and move both pointers while skipping duplicates; if the sum is too small, I move left; if too large, I move right. Sorting takes O(n log n), and the two-pointer scan gives O(n²) overall time with O(1) extra space.”
    # Time Complexity: O(n²) 
    # Space Complexity: O(1) (excluding output list) . 

removeDuplicates(self, nums: List[int]) -> int: Given an integer array nums sorted in ascending order, remove the duplicates in-place such that each unique element appears only once. 
    “Since the array is sorted, duplicates are adjacent. I use two pointers: one (k) to track the position of the next unique element, and one (i) to scan through the array. Whenever I find a new value, I place it at position k and increment k. This way, the first k elements of the array are unique. It runs in O(n) time with O(1) extra space.”
    # Time Complexity: O(n)
        # The loop runs from i = 1 to len(nums) - 1, so it iterates once per element in the array.
        # Each operation inside the loop is constant time: comparisons, assignments, and increments.
        # Therefore, the total time complexity is linear, or O(n), where n is the length of the input list nums.
    # Space Complexity: O(1)
        # No additional data structures are used.
        # The algorithm modifies the input list in-place.

nextPermutation(self, nums: List[int]) -> None: Given an array of integers nums, find the next lexicographically permutation of nums.
    “To compute the next lexicographical permutation, I scan from the right to find the first index i where nums[i] < nums[i+1]. Then I find the smallest number greater than nums[i] to its right, swap them, and finally reverse the suffix after i to get the next smallest order. If no such i exists, the array is entirely non-increasing, so I reverse the whole thing to get the lowest order. This runs in O(n) time with O(1) space.”
    # Time Complexity:
        # Worst case:  O(n)
            # Finding the pivot: O(n)
            # Finding the successor: O(n)
            # Reversing the suffix: O(n)
    # Space Complexity: O(1) (in-place modification, no extra space used)

multiply(self, num1: str, num2: str) -> str: Given two integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
    “To multiply two numbers given as strings, I simulate grade-school multiplication. I reverse both strings and use a result array of size m+n to store partial sums. For each digit pair, I multiply, add to the correct position, and carry over. After processing all pairs, I strip leading zeros and build the final string, adding a negative sign if needed. This works in O(m·n) time and O(m+n) space.”
    # Time: O(m⋅n)
    # Space: O(m+n)

groupAnagrams(self, strs: List[str]) -> List[List[str]]: Given an array of strings strs, group the anagrams together.
    “I group words by their sorted character sequence. For each word, I sort its letters, use that as a key in a hash map, and append the word to that group. At the end, I return all the grouped values. Sorting each word takes O(k log k), so the overall complexity is O(n·k log k), where n is the number of words and k is the average word length.”
    # Time Complexity:    
        # Sorting each word: O(klogk)
        # For n words:  O(n⋅klogk) Where n is number of words, k is average word length
    # Space Complexity: O(n⋅k) for storing grouped anagrams

addBinaryaddBinary(self, a: str, b: str) -> str: Given two binary strings a and b, return their sum as a binary string.
    “To add two binary strings, I simulate binary addition from right to left. At each step I add the corresponding bits plus a carry, compute the new bit (total % 2), and update the carry (total // 2). I keep appending results and reverse at the end. This handles unequal lengths naturally, and runs in O(n) time with O(n) space, where n is the max length of the inputs.”
    # Time Complexity: O(max(n,m)), Where n and m are lengths of a and b
    # Space Complexity: O(max(n,m)) For storing result  