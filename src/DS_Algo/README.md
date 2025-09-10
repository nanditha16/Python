# 30s Explanation (Interview Style):  

1. lengthOfLongestSubstring(self, s: str) -> int: Given a string s, find the length of the longest substring without duplicate characters.git add 
    - “I solve this using a sliding window with two pointers. I keep a hash map of each character’s last seen index. As I expand the right pointer, if a duplicate appears inside the window, I move the left pointer just past its previous index. At each step I update the max window size. This ensures each character is visited at most twice, so it runs in O(n) time with O(min(n, alphabet)) space.”
    - O(n) time where n is the length of the string
    - O(min(n, m)) space, where m is the size of the character set.

2. myAtoi(self, s: str) -> int: converts a string to a 32-bit signed integer.
    - “I implement atoi by parsing the string step by step. First, I skip leading spaces, then capture the sign if present. Next, I read digits while building the number, checking for overflow before each multiplication. If overflow happens, I clamp to INT_MAX or INT_MIN. Finally, I return the signed integer. This runs in O(n) time with O(1) space since I process each character once.”

3. romanToInt(self, s: str) -> int: roman numeral to integer.
    - “I map each Roman numeral to its integer value and iterate from right to left. If the current numeral is smaller than the previous one, I subtract it; otherwise, I add it. This correctly handles subtractive cases like IV or IX. The solution runs in O(n) time with O(1) extra space since I just scan once.”

4. threeSum(self, nums: List[int]) -> List[List[int]]: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    - “I solve 3Sum by first sorting the array, then fixing one element at a time and using a two-pointer approach to find the other two numbers. Sorting helps both with skipping duplicates and moving pointers efficiently. If the sum is zero, I add the triplet and move both pointers while skipping duplicates; if the sum is too small, I move left; if too large, I move right. Sorting takes O(n log n), and the two-pointer scan gives O(n²) overall time with O(1) extra space.”
    - Time Complexity: O(n²)  
    - Space Complexity: O(1) (excluding output list) . 

5. removeDuplicates(self, nums: List[int]) -> int: Given an integer array nums sorted in ascending order, remove the duplicates in-place such that each unique element appears only once. 
    - “Since the array is sorted, duplicates are adjacent. I use two pointers: one (k) to track the position of the next unique element, and one (i) to scan through the array. Whenever I find a new value, I place it at position k and increment k. This way, the first k elements of the array are unique. It runs in O(n) time with O(1) extra space.”
    - Time Complexity: O(n)
        - The loop runs from i = 1 to len(nums) - 1, so it iterates once per element in the array.
        - Each operation inside the loop is constant time: comparisons, assignments, and increments.
        - Therefore, the total time complexity is linear, or O(n), where n is the length of the input list nums.
    - Space Complexity: O(1)
        - No additional data structures are used.
        - The algorithm modifies the input list in-place.

6. nextPermutation(self, nums: List[int]) -> None: Given an array of integers nums, find the next lexicographically permutation of nums.
    - “To compute the next lexicographical permutation, I scan from the right to find the first index i where nums[i] < nums[i+1]. Then I find the smallest number greater than nums[i] to its right, swap them, and finally reverse the suffix after i to get the next smallest order. If no such i exists, the array is entirely non-increasing, so I reverse the whole thing to get the lowest order. This runs in O(n) time with O(1) space.”
    - Time Complexity:
        - Worst case:  O(n)
            - Finding the pivot: O(n)
            - Finding the successor: O(n)
            - Reversing the suffix: O(n)
    - Space Complexity: O(1) (in-place modification, no extra space used)

7. multiply(self, num1: str, num2: str) -> str: Given two integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
    - “To multiply two numbers given as strings, I simulate grade-school multiplication. I reverse both strings and use a result array of size m+n to store partial sums. For each digit pair, I multiply, add to the correct position, and carry over. After processing all pairs, I strip leading zeros and build the final string, adding a negative sign if needed. This works in O(m·n) time and O(m+n) space.”
    - Time: O(m⋅n)
    - Space: O(m+n)

8. groupAnagrams(self, strs: List[str]) -> List[List[str]]: Given an array of strings strs, group the anagrams together.
    - “I group words by their sorted character sequence. For each word, I sort its letters, use that as a key in a hash map, and append the word to that group. At the end, I return all the grouped values. Sorting each word takes O(k log k), so the overall complexity is O(n·k log k), where n is the number of words and k is the average word length.”
    - Time Complexity:    
        - Sorting each word: O(klogk)
        - For n words:  O(n⋅klogk) Where n is number of words, k is average word length
    - Space Complexity: O(n⋅k) for storing grouped anagrams

## *** IMPORTNAT*** 
9. addBinaryaddBinary(self, a: str, b: str) -> str: Given two binary strings a and b, return their sum as a binary string.
    - “To add two binary strings, I simulate binary addition from right to left. At each step I add the corresponding bits plus a carry, compute the new bit (total % 2), and update the carry (total // 2). I keep appending results and reverse at the end. This handles unequal lengths naturally, and runs in O(n) time with O(n) space, where n is the max length of the inputs.”
    - Time Complexity: O(max(n,m)), Where n and m are lengths of a and b
    - Space Complexity: O(max(n,m)) For storing result  

## *** IMPORTNAT*** 
10. minWindow(self, s: str, t: str) -> str: Given two strings s and t of lengths m and n respectively, return  the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string.
    - “I use a sliding window with two pointers. I count required chars from t and scan s with a right pointer, updating a window map and a formed counter when a char meets its needed freq. When all required chars are satisfied (formed == required), I shrink from the left to find the smallest valid window, updating the best answer. Expanding and contracting each pointer at most |s| times gives O(|s| + |t|) time and O(Σ) space for the frequency maps.”
    - Time Complexity: O(m+n) Each character is visited at most twice (once by right, once by left)
    - Space Complexity: O(n) For storing character counts

11. merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: Merge ascending two arrays into a single array sorted in ascending order.
    - “I merge from the end to avoid shifting and extra space. I keep three pointers: i at the last real element of nums1, j at the end of nums2, and k at the write position (end of nums1). At each step I place the larger of nums1[i] or nums2[j] into nums1[k] and move pointers. When one side finishes, any remaining nums2 elements are copied over. This is O(m+n) time and O(1) extra space.”
    - Time Complexity: O(m+n) Each element is visited once
    - Space Complexity: O(1) In-place merge, no extra space used

12. isPalindrome(self, s: str) -> bool: Is palindrom using Slicing or two pointers
    - 12a. Method 1 : using Slicing ([::-1]) - For quick, readable code in small-scale use → Slicing is fine.
        - Time Complexity:
            - Reversing the string: O(n)
            - Comparing strings: O(n)
            - Total: O(n)
        - Space Complexity: Creates a new reversed string →  O(n) extra space 
    - 12b. Method 2: using pointers - For performance and memory efficiency, especially with large strings 
        - “I normalize the string to compare only alphanumerics case-insensitively. One approach builds a filtered lowercase list and checks if it equals its reverse — simple and Pythonic, O(n) time, O(n) space. More optimal on space uses two pointers from both ends, skipping non-alphanumerics and comparing lowercase characters; if any mismatch appears, return false, otherwise true. That keeps it O(n) time and O(1) extra space.”
        - Time Complexity: Single pass through the string → O(n) 
        - Space Complexity: No extra space used → O(1)
    - 12c. Method 3: Valid Palindrome - one more 
        - “I use a two-pointer check with one allowed deletion. Move left and right inward while chars match. At the first mismatch, I try both options: skip s[left] or skip s[right], and verify the remaining range is a palindrome with a helper. If either succeeds, the whole string is valid after deleting at most one char. This is O(n) time (each index visited a constant number of times) and O(1) extra space.”
        - Time Complexity: Single pass through the string → O(n) 
        - Space Complexity: No extra space used → O(1)

13. read(self, buf, n): Read N Characters Given read4
    - “I repeatedly call read4 into a 4-char temp buffer and copy out only what I still need, stopping when I’ve read n chars or read4 hits EOF. Each iteration adds min(count, n - total_read) to the destination buf, and I track total_read as I go. This guarantees we never over-read or write past n. The algorithm is O(n) time and O(1) extra space.”
    - Notes (if asked):
        - Handles partial final chunk and EOF cleanly.
        - For the follow-up (function called multiple times), keep a persistent leftover buffer across calls to store unread chars from the last read4.
    - Time Complexity: O(n) Because in the worst case, we read one character at a time up to n.
    - Space Complexity: O(1) Only a fixed-size buffer buf4 of size 4 is used.

14. read(self, buf: List[str], n: int) -> int: Read N Characters Given read4 - Call multiple times.
    - Your read(buf, n) method may be called multiple times, and you must preserve state between calls. - (persistent buffer)
    - “read returns up to n chars using only read4. I keep a persistent 4-char internal buffer across calls (buffer, buf_ptr, buf_count). For each request, I first drain leftovers from that buffer into buf. When it’s empty, I refill by calling read4, reset the pointer, and continue copying until I’ve produced n chars or read4 hits EOF. This guarantees correct behavior across multiple calls without rereading the file. Time is O(n) per call, extra space is O(1) beyond the fixed internal buffer. (In LeetCode, we write into a preallocated buf; in local tests here I append.)”
    - Time Complexity: O(n) — We read up to n characters.
    - Space Complexity: O(1) — Only a fixed-size buffer is used.

15. isOneEditDistance(self, s: str, t: str) -> bool: Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.
    - “I check if two strings are exactly one edit apart (insert, delete, or replace). I first make s the shorter string; if the length gap > 1, return false. Then I scan until the first mismatch. If lengths are equal, I verify the rest after that index matches (replacement). If lengths differ by 1, I compare s[i:] with t[i+1:] to simulate a single insertion/deletion. If no mismatch appears, it’s true only when t has exactly one extra trailing char. Runs in O(n) time and O(1) space.”
    - Time Complexity: O(n) — where n is the length of the shorter string.
    - Space Complexity: O(1) — no extra space used.

## *** IMPORTNAT*** 
16. productExceptSelf(self, nums: List[int]) -> List[int]: Product of Array Except Self
    - “I compute the product of all elements except self without division using two passes. First pass builds prefix products: answer[i] = product of everything left of i. Second pass runs right-to-left with a running suffix product and multiplies it into answer[i]. This way each index gets (prefix × suffix) of all other elements. It naturally handles zeros and uses O(n) time and O(1) extra space (excluding the output array).”
    - Time Complexity: O(n) — two linear passes.
    - Space Complexity:O(1) extra space if we don't count the output array. Otherwise, O(n) for the output.

## *** IMPORTNAT*** 
17. numberToWords(self, num: int) -> str: Integer to English Words
    - “I convert an integer to English words by processing it in 3-digit chunks (ones/tens/hundreds) from right to left. A recursive helper handles numbers <1000: direct lookup for <20, tens lookup plus ones for <100, and "X Hundred" plus the remainder for >=100. I iterate over the chunks, appending the appropriate scale — ["", "Thousand", "Million", "Billion"] — and concatenate non-zero parts. Edge case 0 → "Zero". Finally I strip() spaces. Runs in O(d) where d is digits (effectively constant for 32-bit ints), with O(1) extra space.”
    - Time Complexity: O(log 10​ (n)) — we process each group of 3 digits.
    - Space Complexity: O(1) — fixed-size arrays and recursion depth.

18. moveZeroes
    - 18.a Method 1 : moveZeroes(self, nums: List[int]) -> None: Two pass
        - “I use a two-pass, in-place approach. First pass compacts all non-zeros to the front while tracking last_non_zero, writing each seen non-zero to that index. After this, the first last_non_zero positions are correct but the tail may contain old values; second pass fills the rest with zeros. This preserves the relative order of non-zeros (stable) and uses O(1) extra space. Overall time is O(n).”
        - (If asked for a one-pass variant: swap nums[last_non_zero], nums[i] whenever nums[i] != 0, increment last_non_zero.)
        - Time Complexity: O(n)
        - Space Complexity: O(1) (in-place)
        - Writes: Up to n writes (non-zero + zero fill)
    - 18.b Method 2 : moveZeroesOnePass(self, nums: List[int]) -> None: One pass
        - “I keep a write pointer last_non_zero. As I scan, every non-zero goes to last_non_zero; if positions differ, I set the current to zero. That compacts non-zeros stably and pushes zeros to the end in one pass, O(n) time, O(1) space.”
        - Time: O(n)
        - Space: O(1)
        - Swaps: Fewer than n, but each swap is 2 writes. - Swapping involves 2 writes per operation, which may be more costly than direct assignment.
    - 18.c Method 3 : moveZeroesFewerWritesThanSwapping(self, nums: List[int]) -> None: optimal for writes without extra passes;
        - “I keep a write index last_non_zero. As I scan once, every non-zero is written to nums[last_non_zero]. If the current index differs, I set the current slot to 0. This compacts non-zeros in stable order and pushes zeros to the end in a single pass. It minimizes writes vs swapping (each non-zero written once; zeros only written when needed). Runs in O(n) time and O(1) extra space.”
        - Time: O(n)
        - Space: O(1)
        - Writes: Minimal — only when necessary.

19. lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:  Longest Substring with At Most K Distinct Characters
    - “I use a sliding window with a hash map counting chars. Expand the right pointer, increment the count for s[right]. If the window has > k distinct characters, I shrink from the left: decrement s[left], remove it from the map when its count hits 0, and move left forward until we’re back to ≤ k distinct. After each step I update the best length. Each char enters and leaves the window at most once → O(n) time and O(k) space.”
    - Time Complexity: O(n) — each character is visited at most twice.
    - Space Complexity: O(k) — for the character count dictionary.

20. validIPAddress(self, queryIP: str) -> str: Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.
    - “I validate by trying IPv4 and IPv6 separately. For IPv4, I split on dots into 4 parts; each must be all digits, in [0..255], and no leading zeros unless the part is exactly ‘0’. For IPv6, I split on colons into 8 parts; each part length 1–4 and only hex digits. If IPv4 check passes return ‘IPv4’; else if IPv6 passes return ‘IPv6’; otherwise ‘Neither’. Splits and scans are linear → O(n) time, O(1) extra space.”
    - Time Complexity:O(n)
    - Space Complexity: O(1)  — no extra space used beyond a few variables.

21. subarraySum(self, nums: List[int], k: int) -> int: Subarray Sum Equals K
    - “I use a prefix sum + hashmap to count subarrays summing to k. As I scan, let prefix_sum be sum up to the current index. Any earlier prefix x where prefix_sum − x = k implies a subarray (x+1..i) sums to k. So I keep a map prefix_map of how many times each prefix has occurred; at each step I add prefix_map[prefix_sum - k] to the answer, then increment prefix_map[prefix_sum]. Initialize prefix_map[0]=1 for subarrays starting at index 0. Works with negatives, runs in O(n) time and O(n) space.”
    - Time:  O(n) We traverse the array once..
    - Space:  O(n) We store prefix sums in a hashmap.

22. addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: Add Two Numbers Singly Linked List
    - “I add two numbers stored in reverse-order linked lists using a running carry. I walk both lists simultaneously; for each step I take value1/value2 (0 if a list ended), compute carry, digit = divmod(value1 + value2 + carry, 10), append digit to the result via a dummy head, and advance pointers. The loop continues while either list has nodes or a carry remains, so it naturally handles unequal lengths and a final carry node. Time: O(max(m, n)) (a.k.a. O(m+n)). Space: O(max(m, n)) for the output list; aux space: O(1).”
    - If they ask for edge cases: empty list treated as 0; final carry creates an extra node (e.g., 5→ and 5→ yields 0→1).
    - Time: O(max(n, m)) — we traverse each list once, bounded by the longer one.
    - Space: O(max(n, m)) for the result list (plus a possible extra node for the final carry).
    - Auxiliary space (not counting output): O(1) — just a few pointers and the carry.

23. mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: Merge Two Sorted Lists
    - “I merge two sorted linked lists with a dummy head and a moving tail. I walk both lists, always attaching the smaller current node to current.next and advancing that list; this preserves sorted order. When one list finishes, I append the remaining nodes of the other. Using the dummy avoids edge-case checks for the head. Time: O(m+n) since each node is visited once. Aux space: O(1) (relinks nodes in place).”
    - Time Complexity: O(n+m) where n and m are the lengths of list1 and list2
    - Space Complexity: O(1) (in-place merge using existing nodes, no extra space except dummy node).

24.  copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]': deep copying a linked list with random pointers. 
    - “I clone a linked list with random pointers in three in-place passes. 
        1. Weave each copy node right after its original (A→A'→B→B'…).
        2. Set each copy’s random via neighbors: if orig.random exists, then orig.next.random = orig.random.next (since every original’s copy is right after it).
        3. Unweave to separate the two lists by restoring original.next and advancing copy.next. This avoids extra hash maps, runs in O(n) time, and uses O(1) extra space.”
    - Time Complexity: O(n) — each node is visited 3 times.
    - Space Complexity: O(1) — no extra hash maps used; in-place manipulation.

25. reorderList(self, head: Optional[ListNode]) -> None: Reorder List
    - “I reorder the list in three in-place steps. First, I find the middle with slow/fast pointers. Second, I reverse the second half. Third, I merge the two halves by alternating nodes: L0, Ln, L1, Ln-1, …. Splitting at the middle ensures we weave ends inward without extra storage. Each node is visited a constant number of times, so it’s O(n) time and O(1) extra space.”
    - Time Complexity: O(n)
    - Space Complexity: O(1)

## *** IMPORTNAT*** 
26. isValidBST(self, root: Optional[TreeNode]) -> bool: Validate Binary Search Tree
    - “I validate a BST with DFS and value bounds. Each node must lie in an open interval (low, high). Starting at (-∞, +∞), when I go left I tighten the upper bound to node.val; when I go right I raise the lower bound to node.val. If any node violates low < val < high, return false; if I finish, it’s valid. This enforces the BST rule globally, not just with immediate children. Time: O(n). Space: O(h) recursion stack (h = tree height). Duplicates are disallowed because of strict <.”
    - Time Complexity: O(n) — each node is visited once.
    - Space Complexity: O(h) — where h is the height of the tree (due to recursion stack).

## *** IMPORTNAT*** 
27. flatten(self, root: Optional[TreeNode]) -> None: Flatten Binary Tree to Linked List
    - “I flatten the tree in-place using a preorder-style Morris traversal. At each node, if there’s a left subtree, I find its rightmost node, splice the current right subtree onto that rightmost’s right, then move the entire left subtree to right and set left = None. Then I advance to current.right. This rewiring preserves preorder order without a stack or recursion. Time: O(n) (each node/edge visited a constant number of times). Space: O(1) extra.”
    - Time Complexity	O(n) — each node is visited once
    - Space Complexity	O(1) — no recursion or stack used

## *** IMPORTNAT*** 
28. maxPathSum(self, root: Optional[TreeNode]) -> int: Binary Tree Maximum Path Sum
    - “I compute the maximum path sum with a post-order DFS that returns each node’s max gain to its parent. For a node, I take left_gain = max(dfs(left), 0) and right_gain = max(dfs(right), 0)—dropping negative branches. The best path through this node is val + left_gain + right_gain; I update a global max_path_sum with that. The value I return upward is val + max(left_gain, right_gain) since a parent can only extend one side. This visits each node once: O(n) time, O(h) space for recursion (h = tree height).”
    - Time: O(n) — each node is visited once.
    - Space: O(h) — recursion stack, where h is the height of the tree.

## *** IMPORTNAT*** 
29. cloneGraph(self, node: Optional['Node']) -> Optional['Node']: deep copy (clone) of the graph.
    - “I clone an undirected graph with DFS + a hash map. The map visited stores the mapping original → clone to avoid re-cloning and to handle cycles. On visiting a node: if it’s already in visited, return its clone; otherwise create a clone, record it, then recursively clone each neighbor and append to the clone’s neighbors. This guarantees every node is copied once and preserves all edges. Time: O(V+E). Space: O(V) for the map, plus O(V) recursion stack in the worst case. (Can do the same with BFS to avoid deep recursion.)”
    - Time Complexity: O(N+E) where N is the number of nodes and E is the number of edges.
    - Space Complexity: O(N) — for the visited dictionary and recursion stack.
