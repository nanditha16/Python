# 30s Explanation (Interview Style):  

1. lengthOfLongestSubstring(self, s: str) -> int: Given a string s, find the length of the longest substring without duplicate characters.git add 
    - “I solve this using a sliding window with two pointers. I keep a hash map of each character’s last seen index. As I expand the right pointer, if a duplicate appears inside the window, I move the left pointer just past its previous index. At each step I update the max window size. This ensures each character is visited at most twice, so it runs in O(n) time with O(min(n, alphabet)) space.”
    - Intuition (≈30s): We want the longest substring without repeating chars. Slide a window over s; if we see a repeated char inside the current window, we jump the left edge past the previous occurrence so the window stays duplicate-free. Track the best window length as we go.
    - Approach (≈30s): Keep a map char_index of each char’s last seen position, and two pointers: left (window start) and right (current index). For each right:
        1. If s[right] was seen at or after left, move left = last_index + 1.
        2. Update char_index[s[right]] = right.
        3. Update max_length = max(max_length, right - left + 1). Return max_length
    - Time: O(n). Space: O(min(n, Σ)).
        - O(n) time where n is the length of the string
        - O(min(n, m)) space, where m is the size of the character set.

2. myAtoi(self, s: str) -> int: converts a string to a 32-bit signed integer.
    - “I implement atoi by parsing the string step by step. First, I skip leading spaces, then capture the sign if present. Next, I read digits while building the number, checking for overflow before each multiplication. If overflow happens, I clamp to INT_MAX or INT_MIN. Finally, I return the signed integer. This runs in O(n) time with O(1) space since I process each character once.”
    - Intuition (≈30s): Parse the string the way you’d read a number by hand: skip spaces, read an optional sign, then scan consecutive digits to build the integer. While building, guard against 32-bit overflow: if the next digit would push the value past INT_MAX (or below INT_MIN after sign), clamp to the limit. Stop at the first non-digit.
    - Approach (≈30s): 
        1. Skip leading ' '; set sign from +/- if present.
        2. Iterate digits: num = num*10 + digit.
        3. Before adding a digit, check num > (INT_MAX - digit)//10; if so, return INT_MAX or INT_MIN based on sign.
        4. Return sign * num.
    - Complexity: O(n) time, O(1) space.

3. romanToInt(self, s: str) -> int: roman numeral to integer.
    - “I map each Roman numeral to its integer value and iterate from right to left. If the current numeral is smaller than the previous one, I subtract it; otherwise, I add it. This correctly handles subtractive cases like IV or IX. The solution runs in O(n) time with O(1) extra space since I just scan once.”
    - Intuition (≈30s): Roman numerals use subtraction only when a smaller symbol comes before a larger one (e.g., IV = 4). If you scan the string right→left, you always know whether to add or subtract the current value by comparing it to the previous (right) value you saw.
    - Approach (≈30s): Make a map roman_map. Initialize total=0, prev=0. For each char in reversed(s):
        - val = roman_map[char]
        - If val < prev, do total -= val (subtractive case); else total += val.
        - Set prev = val. Return total.
    - Time: O(n), Space: O(1).

4. threeSum(self, nums: List[int]) -> List[List[int]]: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    - “I solve 3Sum by first sorting the array, then fixing one element at a time and using a two-pointer approach to find the other two numbers. Sorting helps both with skipping duplicates and moving pointers efficiently. If the sum is zero, I add the triplet and move both pointers while skipping duplicates; if the sum is too small, I move left; if too large, I move right. Sorting takes O(n log n), and the two-pointer scan gives O(n²) overall time with O(1) extra space.”
    - Intuition (≈30s): To find triplets summing to zero, sort the array so we can fix one number and then look for a complementary pair that sums to its negative. Sorting lets us use a two-pointer sweep and easily skip duplicates, ensuring unique triplets.
    - Approach (≈30s): 
        1. Sort nums.
        2. For each index i:
            - If nums[i] equals the previous, continue (avoid duplicate first elements).
            - Set left=i+1, right=n-1.
            - While left<right: compute total=nums[i]+nums[left]+nums[right].
                - If total==0, record the triplet, move both pointers, and skip duplicate left/right values.
                - If total<0, increment left; else decrement right.
        3. Return all collected triplets.
    - Complexity: sort O(n log n) + two-pointer loops O(n²) ⇒ O(n²) time; O(1) extra space (output excluded).
        - Time Complexity: O(n²)  
        - Space Complexity: O(1) (excluding output list) . 

5. removeDuplicates(self, nums: List[int]) -> int: Given an integer array nums sorted in ascending order, remove the duplicates in-place such that each unique element appears only once. 
    - “Since the array is sorted, duplicates are adjacent. I use two pointers: one (k) to track the position of the next unique element, and one (i) to scan through the array. Whenever I find a new value, I place it at position k and increment k. This way, the first k elements of the array are unique. It runs in O(n) time with O(1) extra space.”
    - Intuition (≈30s): The array is already sorted, so duplicates are adjacent. Keep a write index k that marks where the next unique value should go. Scan from left to right; whenever nums[i] differs from the last unique value (nums[k-1]), copy it to nums[k] and advance k. Everything before k ends up as the de-duplicated array.
    - Approach (≈30s): 
        1. If empty, return 0. Initialize k = 1.
        2. For i from 1..n-1:
            If nums[i] != nums[k-1]: set nums[k] = nums[i], increment k.
        3. Return k (new length). The first k positions of nums contain uniques in order.
    - Complexity: O(n) time, O(1) extra space.
        - Time Complexity: O(n)
            - The loop runs from i = 1 to len(nums) - 1, so it iterates once per element in the array.
            - Each operation inside the loop is constant time: comparisons, assignments, and increments.
            - Therefore, the total time complexity is linear, or O(n), where n is the length of the input list nums.
        - Space Complexity: O(1)
            - No additional data structures are used.
            - The algorithm modifies the input list in-place.

6. nextPermutation(self, nums: List[int]) -> None: Given an array of integers nums, find the next lexicographically permutation of nums.
    - “To compute the next lexicographical permutation, I scan from the right to find the first index i where nums[i] < nums[i+1]. Then I find the smallest number greater than nums[i] to its right, swap them, and finally reverse the suffix after i to get the next smallest order. If no such i exists, the array is entirely non-increasing, so I reverse the whole thing to get the lowest order. This runs in O(n) time with O(1) space.”
    - Intuition (≈30s): To get the next lexicographic permutation, find the rightmost place where the sequence can be made larger. Scan from the end to find the first ascending pair nums[i] < nums[i+1]. That index i is the “pivot.” To minimally increase, swap nums[i] with the smallest number greater than it to its right, then make the suffix as small as possible by sorting it ascending (which is just reversing because it’s currently non-increasing).
    - Approach (≈30s): 
        1. Scan from right to left to find the first i with nums[i] < nums[i+1]. If none, reverse the whole array (wrap to smallest).
        2. From the end, find the first j with nums[j] > nums[i] and swap nums[i], nums[j].
        3. Reverse the subarray nums[i+1:] to get the smallest suffix.
    - Time: O(n). Space: O(1).
        - Time Complexity:
            - Worst case:  O(n)
                - Finding the pivot: O(n)
                - Finding the successor: O(n)
                - Reversing the suffix: O(n)
        - Space Complexity: O(1) (in-place modification, no extra space used)

7. multiply(self, num1: str, num2: str) -> str: Given two integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
    - “To multiply two numbers given as strings, I simulate grade-school multiplication. I reverse both strings and use a result array of size m+n to store partial sums. For each digit pair, I multiply, add to the correct position, and carry over. After processing all pairs, I strip leading zeros and build the final string, adding a negative sign if needed. This works in O(m·n) time and O(m+n) space.”
    - Intuition (≈30s): Multiply strings like grade-school multiplication. Treat each char as a digit, multiply every digit of num1 with every digit of num2, and place the product at the correct offset (i+j) in an int array. Manage carry as you go. Handle sign up front and the zero shortcut. At the end, strip leading zeros, reverse the array to form the string, and prepend - if needed.
    - Approach (≈30s): 
        1. Determine the sign; strip leading -. If any number is "0", return "0".
        2. Create result = [0] * (m+n); reverse both numbers to align least significant digits.
        3. Double loop: for each i,j, do result[i+j] += digit1*digit2; push carry with: result[i+j+1] += result[i+j] // 10, then result[i+j] %= 10.
        4. Pop trailing zeros from result, reverse, and join to string. Add '-' if negative.
    - Complexity: Time O(m·n), Space O(m+n).
        - Time: O(m⋅n)
        - Space: O(m+n)

8. groupAnagrams(self, strs: List[str]) -> List[List[str]]: Given an array of strings strs, group the anagrams together.
    - “I group words by their sorted character sequence. For each word, I sort its letters, use that as a key in a hash map, and append the word to that group. At the end, I return all the grouped values. Sorting each word takes O(k log k), so the overall complexity is O(n·k log k), where n is the number of words and k is the average word length.”
    - Intuition (≈30s): Anagrams have the same multiset of letters. If you sort a word’s characters, all of its anagrams produce the same sorted key (e.g., "eat","tea","ate" → "aet"). So we can bucket words by this key; each bucket is one anagram group.
    - Approach (≈30s): Create a hashmap key -> list_of_words. For each word, compute key = ''.join(sorted(word)) and append the word to anagram_map[key]. At the end, return all the hashmap’s values.
    - Complexity: Sorting each word of length L costs O(L log L), so total O(Σ L_i log L_i); space O(Σ L_i) for storing groups. (Alternative: use a 26-count tuple as key for O(L) per word.)
        - Time Complexity:    
            - Sorting each word: O(klogk)
            - For n words:  O(n⋅klogk) Where n is number of words, k is average word length
        - Space Complexity: O(n⋅k) for storing grouped anagrams

## *** IMPORTANT*** 
9. addBinaryaddBinary(self, a: str, b: str) -> str: Given two binary strings a and b, return their sum as a binary string.
    - “To add two binary strings, I simulate binary addition from right to left. At each step I add the corresponding bits plus a carry, compute the new bit (total % 2), and update the carry (total // 2). I keep appending results and reverse at the end. This handles unequal lengths naturally, and runs in O(n) time with O(n) space, where n is the max length of the inputs.”
    - Intuition (≈30s): Add the two binary strings like grade-school addition from right to left. At each position, sum the two bits plus a carry (0 or 1). The result bit is sum % 2; the new carry is sum // 2. Keep going until you’ve exhausted both strings and any leftover carry.
    - Approach (≈30s): Use two indices i, j at the ends of a and b, and carry = 0. While i >= 0 or j >= 0 or carry:
        1. Read bit_a = int(a[i]) if i >= 0 else 0; same for bit_b.
        2. total = bit_a + bit_b + carry; append str(total % 2) to result.
        3. Update carry = total // 2; decrement i, j. Reverse and join result.
    - Complexity: O(m+n) time, O(m+n) output space (aux O(1)).
        - Time Complexity: O(max(n,m)), Where n and m are lengths of a and b
        - Space Complexity: O(max(n,m)) For storing result  

## *** IMPORTANT*** 
10. minWindow(self, s: str, t: str) -> str: Given two strings s and t of lengths m and n respectively, return  the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string.
    - “I use a sliding window with two pointers. I count required chars from t and scan s with a right pointer, updating a window map and a formed counter when a char meets its needed freq. When all required chars are satisfied (formed == required), I shrink from the left to find the smallest valid window, updating the best answer. Expanding and contracting each pointer at most |s| times gives O(|s| + |t|) time and O(Σ) space for the frequency maps.”
    - Intuition (≈30s): We want the smallest substring of s that covers all chars (with counts) from t. Use a sliding window: expand the right end to include needed chars; once the window has all required counts, shrink from the left to make it as small as possible, keeping track of the best window seen.
    - Approach (≈30s): Count requirements with t_count; track formed = how many required chars meet their needed count in the current window. For each right in s:
        1. Add s[right] to window_counts; if its count hits t_count, increment formed.
        2. While formed == required, update the best window, then move left rightward: decrement window_counts[s[left]] and, if it drops below t_count, decrement formed. Return the recorded min window (or "" if none). 
    - Time: O(|s| + |t|). Space: O(Σ) for the maps.
        - Time Complexity: O(m+n) Each character is visited at most twice (once by right, once by left)
        - Space Complexity: O(n) For storing character counts

11. merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: Merge ascending two arrays into a single array sorted in ascending order.
    - “I merge from the end to avoid shifting and extra space. I keep three pointers: i at the last real element of nums1, j at the end of nums2, and k at the write position (end of nums1). At each step I place the larger of nums1[i] or nums2[j] into nums1[k] and move pointers. When one side finishes, any remaining nums2 elements are copied over. This is O(m+n) time and O(1) extra space.”
    - Intuition (≈30s): We need to merge two sorted arrays into nums1 in-place. If we filled from the front, we’d overwrite useful elements in nums1. So we fill from the back: compare the largest remaining elements of nums1 and nums2, place the larger at the end, and move backward. This preserves order without extra space.
    - Approach (≈30s): Use three pointers: 
        1. i = m-1 (end of valid nums1), j = n-1 (end of nums2), k = m+n-1 (end of buffer in nums1).
        2. While i >= 0 and j >= 0, write the larger of nums1[i] / nums2[j] to nums1[k] and decrement that pointer and k. When one side finishes, copy any remaining nums2 elements into nums1 (leftover nums1 are already in place).
    - Time: O(m+n). Space: O(1).
        - Time Complexity: O(m+n) Each element is visited once
        - Space Complexity: O(1) In-place merge, no extra space used

12. Palindrome varients: Is palindrom using Slicing or two pointers
    - 12a. Method 1 : isPalindrome(self, s: str) -> bool:  using Slicing ([::-1]) - For quick, readable code in small-scale use → Slicing is fine.
    - Intuition (≈30s): Ignore everything that isn’t a letter or digit, and compare case-insensitively. If the cleaned sequence reads the same forwards and backwards, it’s a palindrome.
    - Approach (≈30s): Build filtered = [c.lower() for c in s if c.isalnum()], then return filtered == filtered[::-1] (reverse check).
    - Time: O(n) to filter + O(n) to compare. Space: O(n) for the filtered list (can be O(1) if you use two pointers without building a list).
        - Time Complexity:
            - Reversing the string: O(n)
            - Comparing strings: O(n)
            - Total: O(n)
        - Space Complexity: Creates a new reversed string →  O(n) extra space 
    - 12b. Method 2: is_palindrome(self, s: str) -> bool: using pointers - For performance and memory efficiency, especially with large strings 
        - “I normalize the string to compare only alphanumerics case-insensitively. One approach builds a filtered lowercase list and checks if it equals its reverse — simple and Pythonic, O(n) time, O(n) space. More optimal on space uses two pointers from both ends, skipping non-alphanumerics and comparing lowercase characters; if any mismatch appears, return false, otherwise true. That keeps it O(n) time and O(1) extra space.”
        - Intuition (≈30s): Check if the string reads the same forwards and backwards ignoring non-alphanumeric characters and case. Use two pointers from both ends; skip anything that isn’t a letter/digit, then compare the characters case-insensitively.
        - Approach (≈30s): Set left=0, right=len(s)-1. While left < right:
            1. Move left rightward while s[left] isn’t alphanumeric; move right leftward while s[right] isn’t.
            2. Compare s[left].lower() and s[right].lower(). If different → False.3. Otherwise advance both pointers. If the loop completes, return True.
        - Time: O(n). Space: O(1).
            - Time Complexity: Single pass through the string → O(n) 
            - Space Complexity: No extra space used → O(1)
    - 12c. Method 3: validPalindrome(self, s: str) -> bool: Valid Palindrome - one more 
        - “I use a two-pointer check with one allowed deletion. Move left and right inward while chars match. At the first mismatch, I try both options: skip s[left] or skip s[right], and verify the remaining range is a palindrome with a helper. If either succeeds, the whole string is valid after deleting at most one char. This is O(n) time (each index visited a constant number of times) and O(1) extra space.”
        - Intuition (≈30s): We’re allowed to delete at most one character to make a palindrome. Use two pointers from both ends. As long as chars match, move inward. On the first mismatch, we have one “free delete”: either drop the left char or the right char. If either remaining substring is a palindrome, the whole string can be fixed with one deletion.
        - Approach (≈30s): Set left=0, right=len(s)-1. While left<right:
            1. If s[left]==s[right], move both pointers.
            2. Else, call a helper is_palindrome_range(l, r) that checks a substring. Return is_palindrome_range(left+1, right) OR is_palindrome_range(left, right-1). If the loop finishes, return True.
        - Time: O(n) (two-pointer pass + up to one linear check). Space: O(1).
            - Time Complexity: Single pass through the string → O(n) 
            - Space Complexity: No extra space used → O(1)

13. read(self, buf, n): Read N Characters Given read4
    - “I repeatedly call read4 into a 4-char temp buffer and copy out only what I still need, stopping when I’ve read n chars or read4 hits EOF. Each iteration adds min(count, n - total_read) to the destination buf, and I track total_read as I go. This guarantees we never over-read or write past n. The algorithm is O(n) time and O(1) extra space.”
    - Notes (if asked):
        - Handles partial final chunk and EOF cleanly.
        - For the follow-up (function called multiple times), keep a persistent leftover buffer across calls to store unread chars from the last read4.
    - Intuition (≈30s): read4 gives up to 4 chars per call, but callers may ask for any n and across multiple calls we must continue where we left off. So we keep a persistent 4-char internal buffer plus two pointers: how many chars read4 filled (buf_count) and where we are within it (buf_ptr). Each read(n) first drains leftovers from this buffer before calling read4 again.
    - Approach (≈30s): Maintain buffer[4], buf_ptr, buf_count. Loop while total_read < n:
        1. If buf_ptr == buf_count, refill: buf_count = read4(buffer), reset buf_ptr = 0; if buf_count == 0, EOF → stop.
        2. Copy from buffer[buf_ptr:buf_count] into buf until you reach n or exhaust the internal buffer; advance buf_ptr and total_read. Return total_read. (On LeetCode you write into preallocated buf by index; in local tests you can append.) 
    - Runs in O(n) per call, O(1) extra space.
        - Time Complexity: O(n) Because in the worst case, we read one character at a time up to n.
        - Space Complexity: O(1) Only a fixed-size buffer buf4 of size 4 is used.

14. read(self, buf: List[str], n: int) -> int: Read N Characters Given read4 - Call multiple times.
    - Your read(buf, n) method may be called multiple times, and you must preserve state between calls. - (persistent buffer)
    - “read returns up to n chars using only read4. I keep a persistent 4-char internal buffer across calls (buffer, buf_ptr, buf_count). For each request, I first drain leftovers from that buffer into buf. When it’s empty, I refill by calling read4, reset the pointer, and continue copying until I’ve produced n chars or read4 hits EOF. This guarantees correct behavior across multiple calls without rereading the file. Time is O(n) per call, extra space is O(1) beyond the fixed internal buffer. (In LeetCode, we write into a preallocated buf; in local tests here I append.)”
    - Intuition (≈30s): Two strings are one edit apart if you can make them equal with exactly one insert, delete, or replace. Compare them left-to-right until the first mismatch. At that spot:
        - If lengths are equal → it must be a replace of that char.
        - If lengths differ by 1 → it must be a single insert/delete. If no mismatch appears, they’re one edit apart only if the longer string has one extra trailing character.
    - Approach (≈30s): Let s be the shorter. If len(t)-len(s) > 1, return False. Scan indices:
        1. On first mismatch at i:
            - If equal lengths: check s[i+1:] == t[i+1:] (replace).
            - Else (t longer by 1): check s[i:] == t[i+1:] (insert in s / delete from t). If no mismatch, return len(s)+1 == len(t).
    - Time: O(n). Space: O(1).
        - Time Complexity: O(n) — We read up to n characters.
        - Space Complexity: O(1) — Only a fixed-size buffer is used.

15. isOneEditDistance(self, s: str, t: str) -> bool: Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.
    - “I check if two strings are exactly one edit apart (insert, delete, or replace). I first make s the shorter string; if the length gap > 1, return false. Then I scan until the first mismatch. If lengths are equal, I verify the rest after that index matches (replacement). If lengths differ by 1, I compare s[i:] with t[i+1:] to simulate a single insertion/deletion. If no mismatch appears, it’s true only when t has exactly one extra trailing char. Runs in O(n) time and O(1) space.”
    - Intuition (≈30s):
    - Approach (≈30s): 
    - Time Complexity: O(n) — where n is the length of the shorter string.
    - Space Complexity: O(1) — no extra space used.

## *** IMPORTANT*** 
16. productExceptSelf(self, nums: List[int]) -> List[int]: Product of Array Except Self
    - “I compute the product of all elements except self without division using two passes. First pass builds prefix products: answer[i] = product of everything left of i. Second pass runs right-to-left with a running suffix product and multiplies it into answer[i]. This way each index gets (prefix × suffix) of all other elements. It naturally handles zeros and uses O(n) time and O(1) extra space (excluding the output array).”
    - Intuition (≈30s): For each index, the answer is (product of all left elements) × (product of all right elements). Instead of dividing by nums[i], we can precompute these two products without extra arrays by doing two sweeps: one left→right to store prefixes, and one right→left to multiply in suffixes.
    - Approach (≈30s): 
        1. Init answer with 1s.
        2. Left pass: keep prefix; for each i, set answer[i]=prefix, then prefix*=nums[i].
        3. Right pass: keep suffix; for i from end to start, do answer[i]*=suffix, then suffix*=nums[i]. Return answer. Handles zeros naturally. 
    - Time: O(n). Extra space: O(1) (output excluded).
        - Time Complexity: O(n) — two linear passes.
        - Space Complexity:O(1) extra space if we don't count the output array. Otherwise, O(n) for the output.

## *** IMPORTANT*** 
17. numberToWords(self, num: int) -> str: Integer to English Words
    - “I convert an integer to English words by processing it in 3-digit chunks (ones/tens/hundreds) from right to left. A recursive helper handles numbers <1000: direct lookup for <20, tens lookup plus ones for <100, and "X Hundred" plus the remainder for >=100. I iterate over the chunks, appending the appropriate scale — ["", "Thousand", "Million", "Billion"] — and concatenate non-zero parts. Edge case 0 → "Zero". Finally I strip() spaces. Runs in O(d) where d is digits (effectively constant for 32-bit ints), with O(1) extra space.”
    - Intuition (≈30s): Spell the number in chunks of three digits because English names change every thousand (Thousand, Million, Billion). For any chunk < 1000, you can say it with a small set of rules: direct words for <20, tens words for 20–90, and "X Hundred" plus the remainder.
    - Approach (≈30s): If num == 0 return "Zero". Define lookup tables for <20, tens, and the scales ["", "Thousand", "Million", "Billion"]. A helper helper(n) converts a number <1000:
        - <20 → direct word
        - <100 → tens[n//10] + helper(n%10)
        - otherwise → below_20[n//100] + " Hundred " + helper(n%100). Then iterate over the number, taking num % 1000 each time, prefix the helper’s words plus the proper scale, and divide num //= 1000. Trim spaces and return. 
    - Time: Θ(log₁₀ n) — you process one 3-digit chunk per iteration, i.e., proportional to the number of digits. Space (aux): Θ(log₁₀ n) due to recursion depth of helper across chunks (and a few locals). Often treated as O(1) for fixed-width integers (e.g., 32-bit), since the number of chunks is bounded. Output size: The returned string length is also Θ(log n), which is unavoidable.; space: O(1).
        - Time Complexity: O(log 10​ (n)) — we process each group of 3 digits.
         - Space Complexity: O(1) — fixed-size arrays and recursion depth.

18. moveZeroes
    - 18.a Method 1 : moveZeroes(self, nums: List[int]) -> None: Two pass
        - “I use a two-pass, in-place approach. First pass compacts all non-zeros to the front while tracking last_non_zero, writing each seen non-zero to that index. After this, the first last_non_zero positions are correct but the tail may contain old values; second pass fills the rest with zeros. This preserves the relative order of non-zeros (stable) and uses O(1) extra space. Overall time is O(n).”
        - (If asked for a one-pass variant: swap nums[last_non_zero], nums[i] whenever nums[i] != 0, increment last_non_zero.)
        - Intuition (≈30s): Pack all non-zeros to the front in their original order, then fill the remaining tail with zeros. This avoids lots of swaps and keeps writes minimal: each non-zero is written once to its correct spot, and then we do a single sweep to write the needed zeros.
        - Approach (≈30s): Keep a write index last_non_zero = 0.
            1. First pass: scan left→right; for every nums[i] != 0, write nums[last_non_zero] = nums[i] and increment last_non_zero.
            2. Second pass: set all indices from last_non_zero to end to 0. This is stable, in-place. 
        - Time: O(n). Space: O(1).
            - Time Complexity: O(n)
            - Space Complexity: O(1) (in-place)
            - Writes: Up to n writes (non-zero + zero fill)
    - 18.b Method 2 : moveZeroesOnePass(self, nums: List[int]) -> None: One pass
        - “I keep a write pointer last_non_zero. As I scan, every non-zero goes to last_non_zero; if positions differ, I set the current to zero. That compacts non-zeros stably and pushes zeros to the end in one pass, O(n) time, O(1) space.”
        - Intuition (≈30s): Compact all non-zeros to the front, preserving their order, and let zeros naturally drift to the end. Keep a write pointer last_non_zero that marks where the next non-zero should go. As you scan, whenever you see a non-zero at i, place it at last_non_zero (swap if needed) and advance last_non_zero.
        - Approach (≈30s): Scan i = 0..n-1:
            1. If nums[i] != 0:
                - If i != last_non_zero, swap nums[i] with nums[last_non_zero] (avoids self-swap).
                - Increment last_non_zero. By the end, indices [0..last_non_zero-1] hold all non-zeros in order; the rest are zeros. 
        - Time: O(n). Space: O(1).
            - Time: O(n)
            - Space: O(1)
            - Swaps: Fewer than n, but each swap is 2 writes. - Swapping involves 2 writes per operation, which may be more costly than direct assignment.
    - 18.c Method 3 : moveZeroesFewerWritesThanSwapping(self, nums: List[int]) -> None: optimal for writes without extra passes;
        - “I keep a write index last_non_zero. As I scan once, every non-zero is written to nums[last_non_zero]. If the current index differs, I set the current slot to 0. This compacts non-zeros in stable order and pushes zeros to the end in a single pass. It minimizes writes vs swapping (each non-zero written once; zeros only written when needed). Runs in O(n) time and O(1) extra space.”
        - Intuition (≈30s): We want all non-zeros compacted to the front in order, with zeros pushed to the end—without extra space and with fewer writes than swapping. As we scan, keep a write index last_non_zero pointing to where the next non-zero should go. When we see a non-zero at i, place it at last_non_zero. If i is ahead, set nums[i] to 0—this both moves the value forward and leaves a zero behind.
        - Approach (≈30s): Initialize last_non_zero = 0. For each i:
            1. If nums[i] != 0:
                - Write nums[last_non_zero] = nums[i].
                - If i != last_non_zero, write nums[i] = 0 (avoids self-write).
                - Increment last_non_zero. This is one pass, preserves order, uses O(1) space, and minimizes writes vs swapping. 
        - Time: O(n). Space: O(1).
            - Time: O(n)
            - Space: O(1)
            - Writes: Minimal — only when necessary.

19. lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:  Longest Substring with At Most K Distinct Characters
    - “I use a sliding window with a hash map counting chars. Expand the right pointer, increment the count for s[right]. If the window has > k distinct characters, I shrink from the left: decrement s[left], remove it from the map when its count hits 0, and move left forward until we’re back to ≤ k distinct. After each step I update the best length. Each char enters and leaves the window at most once → O(n) time and O(k) space.”
    - Intuition (≈30s): Use a sliding window to keep the longest substring that contains at most k distinct characters. As you expand the right end, track character frequencies. If you exceed k distinct, move the left end rightward to drop chars until you’re back to ≤ k. The window always represents a valid candidate; track the max length seen.
    - Approach (≈30s): Maintain left, char_count, and iterate right over s:
        1. Add s[right] to char_count.
        2. While len(char_count) > k, decrement s[left]; if its count hits 0, remove it; then left += 1.
        3. Update max_len = max(max_len, right - left + 1) each step. Return max_len. 
    - Time: O(n) (each index enters/leaves window once). Space: O(k) (map holds ≤ k keys).
        - Time Complexity: O(n) — each character is visited at most twice.
        - Space Complexity: O(k) — for the character count dictionary.

20. validIPAddress(self, queryIP: str) -> str: Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.
    - “I validate by trying IPv4 and IPv6 separately. For IPv4, I split on dots into 4 parts; each must be all digits, in [0..255], and no leading zeros unless the part is exactly ‘0’. For IPv6, I split on colons into 8 parts; each part length 1–4 and only hex digits. If IPv4 check passes return ‘IPv4’; else if IPv6 passes return ‘IPv6’; otherwise ‘Neither’. Splits and scans are linear → O(n) time, O(1) extra space.”
    - Intuition (≈30s): Decide whether the string fits IPv4 rules, IPv6 rules, or neither. IPv4 has 4 dot-separated decimal chunks with strict bounds and no leading zeros. IPv6 has 8 colon-separated chunks of 1–4 hex digits. If it passes one set of rules exactly, return that version; otherwise it’s “Neither.”
    - Approach (≈30s): 
        1. IPv4 check: split('.') → need 4 parts; each part must be all digits, value in [0..255], and no leading ‘0’ unless the part is exactly "0".
        2. IPv6 check: split(':') → need 8 parts; each part length 1–4 and every char in [0-9a-fA-F].
        3. Run IPv4 check; if true return "IPv4". Else run IPv6 check; if true return "IPv6". Else return "Neither".
    - Complexity: O(n) time, O(1) extra space.
        - Time Complexity:O(n)
        - Space Complexity: O(1)  — no extra space used beyond a few variables.

21. subarraySum(self, nums: List[int], k: int) -> int: Subarray Sum Equals K
    - “I use a prefix sum + hashmap to count subarrays summing to k. As I scan, let prefix_sum be sum up to the current index. Any earlier prefix x where prefix_sum − x = k implies a subarray (x+1..i) sums to k. So I keep a map prefix_map of how many times each prefix has occurred; at each step I add prefix_map[prefix_sum - k] to the answer, then increment prefix_map[prefix_sum]. Initialize prefix_map[0]=1 for subarrays starting at index 0. Works with negatives, runs in O(n) time and O(n) space.”
    - Intuition (≈30s):  Use running (prefix) sums to spot subarrays that add to k. If the sum up to index i is S, then any earlier prefix sum S - k means the subarray between that earlier point and i sums to k. So as you scan, you just need to know how many times you’ve seen each prefix sum before.
    - Approach (≈30s): Maintain prefix_sum and a hashmap prefix_map counting occurrences of each prefix, seeded with {0:1} (handles subarrays starting at index 0). For each num:
        1. Update prefix_sum += num.
        2. Add prefix_map[prefix_sum - k] to count.
        3. Increment prefix_map[prefix_sum]. Return count. 
    - Time: O(n). Space: O(n). Works with negatives too.
        - Time:  O(n) We traverse the array once..
        - Space:  O(n) We store prefix sums in a hashmap.

22. addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: Add Two Numbers Singly Linked List
    - “I add two numbers stored in reverse-order linked lists using a running carry. I walk both lists simultaneously; for each step I take value1/value2 (0 if a list ended), compute carry, digit = divmod(value1 + value2 + carry, 10), append digit to the result via a dummy head, and advance pointers. The loop continues while either list has nodes or a carry remains, so it naturally handles unequal lengths and a final carry node. Time: O(max(m, n)) (a.k.a. O(m+n)). Space: O(max(m, n)) for the output list; aux space: O(1).”
    - If they ask for edge cases: empty list treated as 0; final carry creates an extra node (e.g., 5→ and 5→ yields 0→1).
    - Intuition (≈30s): Treat the two reverse-order linked lists like numbers you’d add by hand. Walk both lists digit by digit, keep a running carry, and build a new list of result digits. If one list ends earlier, treat missing digits as 0. If a carry remains at the end, append it as a final node.
    - Approach (≈30s): Use a dummy head and pointers p1, p2. While p1 or p2 or carry exists:
        1. Read v1 = p1.val if p1 else 0, v2 = p2.val if p2 else 0.
        2. Compute carry, digit = divmod(v1 + v2 + carry, 10).
        3. Append digit node to the result, advance p1, p2. Return dummy.next. 
    - Time: O(max(m, n)); Space: O(max(m, n)) for the output (aux space O(1)).
        - Time: O(max(n, m)) — we traverse each list once, bounded by the longer one.
        - Space: O(max(n, m)) for the result list (plus a possible extra node for the final carry).
        - Auxiliary space (not counting output): O(1) — just a few pointers and the carry.

23. mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: Merge Two Sorted Lists
    - “I merge two sorted linked lists with a dummy head and a moving tail. I walk both lists, always attaching the smaller current node to current.next and advancing that list; this preserves sorted order. When one list finishes, I append the remaining nodes of the other. Using the dummy avoids edge-case checks for the head. Time: O(m+n) since each node is visited once. Aux space: O(1) (relinks nodes in place).”
    - Intuition (≈30s): Merging two sorted linked lists is like zipping two sorted queues: always take the smaller head next to keep the result sorted. Using a dummy head makes stitching nodes easy and avoids special-casing the first node.
    - Approach (≈30s): Create dummy and a current pointer. While both lists are non-empty, compare list1.val and list2.val; attach the smaller node to current.next and advance that list. Move current forward. When one list ends, append the remaining nodes of the other. Return dummy.next. 
    - Time: O(m+n). Space: O(1) auxiliary (relink existing nodes).
        - Time Complexity: O(n+m) where n and m are the lengths of list1 and list2
        - Space Complexity: O(1) (in-place merge using existing nodes, no extra space except dummy node).

24.  copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]': deep copying a linked list with random pointers. 
    - “I clone a linked list with random pointers in three in-place passes. 
        1. Weave each copy node right after its original (A→A'→B→B'…).
        2. Set each copy’s random via neighbors: if orig.random exists, then orig.next.random = orig.random.next (since every original’s copy is right after it).
        3. Unweave to separate the two lists by restoring original.next and advancing copy.next. This avoids extra hash maps, runs in O(n) time, and uses O(1) extra space.”
    - Intuition (≈30s): We need a deep copy of a list where each node has next and a cross-link random. Hash maps work, but there’s a slick O(1) extra space trick: temporarily weave each clone right after its original (A→A'→B→B'…). Now every original’s clone is one step away, so we can set random for clones by hopping via originals.
    - Approach (≈30s): 
        1. Weave: for each original curr, create curr' and insert it after curr.
        2. Set random: for each original curr, if curr.random exists, set curr'.random = curr.random.next (the clone of the target).
        3. Unweave: restore the original list and extract the cloned list by skipping alternating nodes.
    - Time: O(n). Space: O(1) extra (beyond the output list).
        - Time Complexity: O(n) — each node is visited 3 times.
        - Space Complexity: O(1) — no extra hash maps used; in-place manipulation.

25. reorderList(self, head: Optional[ListNode]) -> None: Reorder List
    - “I reorder the list in three in-place steps. First, I find the middle with slow/fast pointers. Second, I reverse the second half. Third, I merge the two halves by alternating nodes: L0, Ln, L1, Ln-1, …. Splitting at the middle ensures we weave ends inward without extra storage. Each node is visited a constant number of times, so it’s O(n) time and O(1) extra space.”
    - Intuition (≈30s): We want to interleave nodes from the front and the back: L0, Ln, L1, Ln−1, …. If we split the list in the middle, then reverse the second half, we can weave the two halves together by alternating nodes—this naturally produces the required order without extra memory.
    - Approach (≈30s): 
        1. Find middle with slow/fast pointers; cut the list: first = head, second = mid.next, then set mid.next = None.
        2. Reverse second in-place.
        3. Merge by alternating: while second, link first.next = second, second.next = first_next, then advance both pointers.
    - Runs in O(n) time and O(1) extra space.
        - Time Complexity: O(n)
        - Space Complexity: O(1)

## *** IMPORTANT*** 
26. isValidBST(self, root: Optional[TreeNode]) -> bool: Validate Binary Search Tree
    - “I validate a BST with DFS and value bounds. Each node must lie in an open interval (low, high). Starting at (-∞, +∞), when I go left I tighten the upper bound to node.val; when I go right I raise the lower bound to node.val. If any node violates low < val < high, return false; if I finish, it’s valid. This enforces the BST rule globally, not just with immediate children. Time: O(n). Space: O(h) recursion stack (h = tree height). Duplicates are disallowed because of strict <.”
    - Intuition (≈30s): A valid BST requires every node’s value to be strictly between the allowed lower and upper bounds determined by its ancestors. When you go left, everything must be < current.val; when you go right, everything must be > current.val. If any node breaks its (low, high) range, the tree isn’t a BST.
    - Approach (≈30s): Use DFS with bounds: validate(node, low, high).
        1. If node is None, return True.
        2. If not (low < node.val < high), return False.
        3. Recurse left with (low, node.val) and right with (node.val, high). If both subcalls are true, it’s a BST.
    - Complexity: O(n) time (visit each node once), O(h) space for recursion (h = height).
        - Time Complexity: O(n) — each node is visited once.
        - Space Complexity: O(h) — where h is the height of the tree (due to recursion stack).

## *** IMPORTANT*** 
27. flatten(self, root: Optional[TreeNode]) -> None: Flatten Binary Tree to Linked List
    - “I flatten the tree in-place using a preorder-style Morris traversal. At each node, if there’s a left subtree, I find its rightmost node, splice the current right subtree onto that rightmost’s right, then move the entire left subtree to right and set left = None. Then I advance to current.right. This rewiring preserves preorder order without a stack or recursion. Time: O(n) (each node/edge visited a constant number of times). Space: O(1) extra.”
    - Intuition (≈30s): We want a preorder-linked list using only right pointers. If a node has a left subtree, that subtree’s nodes should come immediately after the node, and the original right subtree should come after that. So we splice the left subtree in between the node and its right subtree.
    - Approach (≈30s): Iterate with current. For each node with a left child, find the rightmost node of the left subtree (rightmost). Attach the original right subtree to rightmost.right, move the left subtree to current.right, and set current.left = None. Then advance current = current.right. This is a Morris-style in-place transformation. 
    - Time: O(n) (each edge visited a constant number of times). Space: O(1).
        - Time Complexity	O(n) — each node is visited once
        - Space Complexity	O(1) — no recursion or stack used

## *** IMPORTANT*** 
28. maxPathSum(self, root: Optional[TreeNode]) -> int: Binary Tree Maximum Path Sum
    - “I compute the maximum path sum with a post-order DFS that returns each node’s max gain to its parent. For a node, I take left_gain = max(dfs(left), 0) and right_gain = max(dfs(right), 0)—dropping negative branches. The best path through this node is val + left_gain + right_gain; I update a global max_path_sum with that. The value I return upward is val + max(left_gain, right_gain) since a parent can only extend one side. This visits each node once: O(n) time, O(h) space for recursion (h = tree height).”
    - Intuition (≈30s): The best path either passes through a node (using both left and right branches) or continues up from one side. If a subtree’s best contribution is negative, it only hurts the total—so treat negative gains as 0. For each node, consider the “V-shaped” path left_gain + node.val + right_gain and keep a global maximum.
    - Approach (≈30s): Do a post-order DFS that returns each node’s max gain upward:
        1. Recurse left/right and clamp with max(…, 0) to drop negatives.
        2. Update global_max = max(global_max, node.val + left_gain + right_gain).
        3. Return node.val + max(left_gain, right_gain) to the parent (can only extend one side). After DFS, global_max is the answer. 
    - Time: O(n). Space: O(h) recursion.
        - Time: O(n) — each node is visited once.
        - Space: O(h) — recursion stack, where h is the height of the tree.

## *** IMPORTANT*** 
29. cloneGraph(self, node: Optional['Node']) -> Optional['Node']: deep copy (clone) of the graph.
    - “I clone an undirected graph with DFS + a hash map. The map visited stores the mapping original → clone to avoid re-cloning and to handle cycles. On visiting a node: if it’s already in visited, return its clone; otherwise create a clone, record it, then recursively clone each neighbor and append to the clone’s neighbors. This guarantees every node is copied once and preserves all edges. Time: O(V+E). Space: O(V) for the map, plus O(V) recursion stack in the worst case. (Can do the same with BFS to avoid deep recursion.)”
    - Intuition (≈30s): We need a deep copy of a possibly cyclic graph. The key is to remember which original nodes we’ve already cloned so we don’t reclone them or loop forever. Keep a map visited: original → clone. When you see a node, if it’s already in the map, reuse its clone; otherwise create it and then clone its neighbors.
    - Approach (≈30s): Use DFS with a hash map:
        1. If current is in visited, return visited[current].
        2. Otherwise, create clone = Node(current.val), store visited[current] = clone.
        3. For each neighbor, recursively dfs(neighbor) and append to clone.neighbors.
        4. Return clone from the start node.
    - Complexity: O(V+E) time (visit each node/edge once), O(V) space for the map (plus recursion stack).
        - Time Complexity: O(N+E) where N is the number of nodes and E is the number of edges.
        - Space Complexity: O(N) — for the visited dictionary and recursion stack.

## *** IMPORTANT*** 
30. Binary Tree Right Side View
    - 30a. Method 1: rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        - “I take the right side view using level-order BFS. I push the root into a queue and process level by level; for each level I track its size and when I pop nodes, I record the last node’s value (index i == level_size - 1)—that’s the node visible from the right for that level. I enqueue children left→right so traversal is standard. This visits each node once → O(n) time and uses the queue for at most a level’s nodes → O(w) space, where w is tree width.”
        - (If they ask for DFS: do right-first preorder, recording the first value seen at each depth.)
    - Intuition (≈30s): From the right side, you see the last node at each depth. If you traverse the tree level by level (BFS), the node that gets processed last in a level is exactly the rightmost one for that level. So collect that last node’s value per level to form the right-side view.
    - Approach (≈30s): Run BFS with a queue:
        1. While the queue isn’t empty, get level_size.
        2. Pop level_size nodes; enqueue each node’s children (left, then right).
        3. When processing index i == level_size - 1, append that node’s value to result (it’s the rightmost of the level). Return result. 
    - Time: O(n). Space: O(w), where w is the tree’s max width.
        - Time Complexity: O(n) — each node is visited once.
        - Space Complexity: O(w) — where w is the maximum width of the tree (nodes at the widest level).
    - 30b. Method 2: rightSideViewRecursive(self, root: Optional[TreeNode]) -> List[int]:
        - “I take a right-first DFS and record the first node seen at each depth. In the recursive dfs(node, depth), if depth == len(res), we haven’t added any node for this level yet—so append node.val. Then recurse right before left, ensuring the first visit per depth is the rightmost node. After the traversal, res contains the right-side view from top to bottom. Time: O(n) (visit each node once). Space: O(h) recursion stack (h = tree height).”
        - Intuition (≈30s): See the tree from the right: at each depth, the rightmost node is the first one you’d encounter if you always explore the right side before the left. So if we record the first node visited at each depth, we get the right-side view.
        - Approach (≈30s): Do a right-first DFS with (node, depth).
            1. If depth == len(res), we’re seeing this level for the first time → append node.val.
            2. Recurse to node.right then node.left so rightmost nodes are seen first. Return res after traversal. 
        - Time: O(n). Space: O(h) recursion (h = height).
    - 30c. Method 3: rightSideViewIterative(self, root: Optional[TreeNode]) -> List[int]:
        - “I do an iterative right-first DFS. I keep a stack of (node, depth) and pop nodes; when I first reach a depth (depth == len(res)), I record that node’s value—it’s the rightmost because I always process the right side before the left. To enforce that with a LIFO stack, I push left first, then right, so the right child is visited next. This gives one value per level in top-down order. Time: O(n) (each node once). Space: O(h) for the stack (h = tree height).”
        - Intuition (≈30s): We want the rightmost node at each depth. If we traverse the tree right-first, then the first node we visit at a given depth is exactly the one visible from the right.
        - Approach (≈30s): Do an iterative DFS with a stack of (node, depth). Pop a node; if depth == len(res), it’s the first time we’ve reached this depth → append its value to res. Push left first, then right so that (LIFO) the right child is processed first. Continue until the stack is empty and return res.
        - Complexity: O(n) time (visit each node once), O(h) space for the stack (h = tree height).
        

## *** IMPORTANT*** 
31. numIslands
    - 31a. Method 1 : numIslands(self, grid: List[List[str]]) -> int: Number of Islands
        - “I count islands with DFS flood-fill. I scan the grid; when I hit a '1', that’s a new island, so I increment the count and DFS from that cell, flipping connected '1's to '0' to mark them visited. DFS explores the four directions (up/down/left/right) and prevents revisits by mutating the grid. Each cell is visited at most once → O(R·C) time and O(R·C) worst-case stack space (or O(min(R,C)) average for thin islands).”
        - Intuition (≈30s): Treat the grid as a map where each '1' is land and '0' is water. An island is a connected blob of '1's (4-directional). If you scan every cell and, upon seeing a '1', flood-fill all connected land to water, you’ll count each island exactly once.
        - Approach (≈30s): Iterate all cells. When you find '1', increment count and run a DFS from that cell: bounds-check, return if not '1', otherwise mark it '0' and recurse to its 4 neighbors. This marks the whole island as visited so it won’t be counted again. After the scan, count is the number of islands. 
        - Time: O(R·C) (each cell visited at most once). Space: O(R·C) worst-case recursion stack (O(H) where H is island size).
    - 31b. Method 2 : numIslandsIterative(self, grid: List[List[str]]) -> int: 
        - “I use BFS flood-fill to count islands. Scan the grid; when I find a '1', that’s a new island—increment count, flip it to '0', and push it into a queue. Then BFS pops cells and explores 4 neighbors; any neighbor that’s '1' gets flipped to '0' (mark visited) and enqueued. This removes the whole connected component. Each cell is processed at most once, so it’s O(R·C) time and O(R·C) worst-case space (queue). Mutating the grid avoids an extra visited set and keeps it in-place.”
        - Intuition (≈30s): An island is a group of '1' cells connected 4-directionally. Scan the grid; every time you hit a '1', that’s a new island. From there, do a flood-fill to wipe out (mark '0') the entire connected component so you don’t count it again.
        - Approach (≈30s): Loop all cells. On '1': increment count, set it to '0', and run a BFS from that cell using a queue. Pop cells and push any 4-neighbors that are '1', marking them '0' as you go. When the queue empties, that island is fully processed; continue scanning. 
        - Time: O(R·C) (each cell visited at most once). Space: O(min(R·C, width of a component)) for the queue.
            - Time Complexity: O(m×n) — each cell is visited once
            - Space Complexity: DFS recursion stack: O(m × n) in worst case (all land) Can be reduced using iterative BFS

## *** IMPORTANT*** 
32. lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': Lowest Common Ancestor of a Binary Tree
    - “I find the LCA in a general binary tree with DFS. If the current root is None, or equals p or q, I return it. Otherwise I recurse left and right. If both sides return non-null, it means p and q were found in different subtrees, so the current root is the LCA. If only one side returns non-null, I bubble that up. This checks each node once → O(n) time and O(h) space for recursion (h = tree height). Handles cases where one node is ancestor of the other naturally.”
    - Intuition (≈30s): In a general binary tree (not BST), the LCA of p and q is the first node on both of their paths from the root. If a node’s left subtree contains one target and its right contains the other, that node is their LCA. If both targets are in the same side, the LCA is within that side. If the node itself is p or q, it can be the LCA.
    - Approach (≈30s): Use a recursive DFS:
        1. If root is None or equals p/q, return root.
        2. Recurse into left and right: left = LCA(root.left), right = LCA(root.right).
        3. If both left and right are non-null, current root is the LCA.
        4. Otherwise return the non-null of left or right (bubble up the found node).
    - Time: O(n) visiting each node once. Space: O(h) recursion stack (h = tree height).
        - Time Complexity: O(n)
        - Space Complexity: O(h) for recursion stack, where h is the height of the tree.

## *** IMPORTANT*** 
33. Binary Tree Paths - Return all root-to-leaf paths in a binary tree
    - 33a. Method 1: binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        - “I collect all root-to-leaf paths with a simple DFS. I pass along the current path string; when I hit a leaf (no left/right), I append that path to the result. Otherwise I recurse on children, adding '->' between nodes. This visits each node once, so O(n) time; recursion uses O(h) space for the call stack (h = tree height).”
        - Intuition (≈30s): A root-to-leaf path is just the sequence of node values from the root down to a leaf. If we carry along a running string as we DFS, then every time we land on a leaf we can record that string as one complete path. For internal nodes, we keep exploring children, appending "->" between values.
        - Approach (≈30s): Do a recursive DFS that threads a path string:
            1. On entry, path += str(node.val).
            2. If the node is a leaf, append path to paths.
            3. Otherwise, append "->" and recurse on left and right with the updated path. Return paths after DFS.
        - Complexity: Visits each node once → O(n) nodes; note Python string concatenation at each step can add overhead—backtracking with a list and join at leaves reduces that (same logic, fewer copies).
            - Time: Each path += str(node.val) creates a new string (strings are immutable). For a path of length L, you do ~L concatenations → O(L²) work per path. Across P root-to-leaf paths: ~O(∑ Lᵢ²). In a skewed tree this can reach O(N²).
            - Space: O(H) recursion stack (H = height) + result storage. Extra transient strings created along the way inflate constant factors.
    - 33b. Method 2: binaryTreePathsBacktracking(self, root: Optional[TreeNode]) -> List[str]:
        - (If asked to optimize string ops: carry a list of node values, append/pop during DFS, and paths.append('->'.join(parts)) at leaves.) 
        - “I build paths with backtracking: keep a path list of node values, append on entry and pop on exit. At a leaf, I '->'.join(path) once to form the string. This avoids O(n²) string concatenations, keeps time O(n) overall, and uses O(h) stack space.”
        - The list + join approach avoids quadratic string-building overhead and is the preferred, scalable solution.
        - Intuition (≈30s): A root-to-leaf path is just the sequence of node values you encounter from the root down to a leaf. If we maintain a running list of values as we traverse, then whenever we hit a leaf we can join that list with "->" to form one complete path. Backtracking (undoing the last choice) lets us reuse the same list while exploring different branches.
        - Approach (≈30s): Do a DFS with a shared path list:
            1. On entry to a node, append node.val to path.
            2. If it’s a leaf, add "->".join(path) to res; otherwise recurse left and right.
            3. On exit, pop to backtrack and restore path. This avoids repeated string building (only join at leaves). 
        - Time: O(N + total output chars). Space: O(H) for recursion + O(H) for path (H = tree height).
            - Time: Appends/pops on the list are O(1). At each leaf, join costs O(L) once. Across all paths: O(N + ∑ Lᵢ) = O(N + total_output_chars). (Much better overhead.)
            - Space: O(H) for the call stack + O(H) for the path list + result storage.

## *** IMPORTANT*** 
34. alienOrder(self, words: List[str]) -> str: Alien Dictionary
    - “I infer the alien alphabet by building a graph of letter precedences. First, I init all chars with in-degree 0. Then for each adjacent word pair, I find the first differing character; that gives a directed edge w1[j] → w2[j] and I increment in-degree. If a longer word precedes its exact prefix, it’s invalid (return ''). Finally, I run Kahn’s topological sort: push all zero-in-degree letters, pop/append to the result, decrement neighbors, and enqueue new zeros. If I don’t output all letters, there’s a cycle → return ''. Time: O(V+E). Space: O(V+E).”
    - Intuition (≈30s): Letters’ order can be deduced by comparing adjacent words: the first differing character tells us one letter must come before the other. Collect all such “A → B” constraints into a directed graph. If a longer word comes before its exact prefix, the dictionary is invalid. Once we have the graph, the alien alphabet is any topological ordering of its nodes; if there’s a cycle, no valid order exists.
    - Approach (≈30s): 
        1. Initialize in_degree for every seen letter; build graph by scanning adjacent word pairs and adding one edge at the first mismatch; detect the invalid prefix case early.
        2. Run Kahn’s topological sort: enqueue all letters with in_degree == 0, repeatedly pop, append to result, and decrement neighbors’ in-degrees, enqueuing new zeros.
        3. If the result length ≠ number of unique letters, there’s a cycle → return ""; else join and return.
    - Complexity: O(V + E + total chars) time, O(V + E) space.
        - Time Complexity: O(N × L)
        - Space Complexity: O(V + E)

## *** IMPORTANT*** 
35. Shortest Distance from All Buildings
    - 35a. Method 1: shortestDistance(self, grid: List[List[int]]) -> int: 
        - “I run BFS from every building to accumulate distances to all empty lands. For each building (cell==1), a BFS explores only empty cells (0), marking visited, and for each reached cell adds dist+1 into total_dist[r][c] and increments reach_count[r][c]. After processing all buildings, I scan all empty cells and pick the minimum total_dist among those whose reach_count equals the number of buildings (i.e., reachable from all). If none qualify, return -1. Each BFS touches each cell at most once → Time: O(B·R·C). Space: O(R·C).”
        - Intuition (≈30s): We want an empty land (0) that minimizes the sum of Manhattan distances to all buildings (1) while avoiding obstacles (2). If we run a BFS from each building, we get the shortest distance from that building to every reachable empty cell. Summing those distances over all buildings gives, for each cell, the total travel cost; the best cell is the minimum among those reachable from every building.
        - Approach (≈30s): Initialize two grids: total_dist (sum of distances) and reach_count (how many buildings reached). For each building cell (i,j), run BFS over zeros, marking a local visited; when you pop (x,y,d), add d+1 to total_dist[nx][ny] and increment reach_count[nx][ny]. After processing all buildings, scan all zeros and pick the minimum total_dist where reach_count == building_count. If none qualify, return -1. 
        - Time: O(B·m·n), Space: O(m·n).
            - Time Complexity: O(m × n × b)
            - Space Complexity: O(m × n)
    - 35b. Method 2: shortestDistance_optimized(grid: List[List[int]]) -> int:
        - “I still BFS from each building, but I reuse the grid to avoid extra visited sets and to prune unreachable cells. I keep a walk marker (starting at 0). During a building’s BFS I only step onto empty cells whose value equals walk; when I visit one, I set it to walk-1 and add its distance into dist. After finishing that building, I decrement walk. This means later BFS runs only traverse cells that were reachable from all previous buildings. Finally, among cells marked -buildings, I take the minimum summed distance. Same worst case O(B·R·C) time, but far fewer pushes in practice; space is O(R·C) for dist (no per-BFS visited).”
        - Intuition (≈30s): We still need a BFS from each building, but we can avoid re-visiting useless cells. Reuse the grid itself as an eligibility marker so that after processing one building, only cells reachable from all previous buildings remain eligible for the next BFS. At the same time, accumulate distances into a dist matrix. In the end, any empty land reached by every building will have the smallest total distance candidate.
        - Approach (≈30s): Keep dist[R][C] and a walk marker starting at 0. For each building:
            1. Run BFS; you may step onto an empty cell only if grid[r][c] == walk.
            2. When you visit it, set grid[r][c] = walk - 1 and add d+1 to dist[r][c].
            3. After finishing this building, decrement walk (so next BFS only sees cells reached by all prior buildings).
                - If any building reaches nothing, return -1. Finally, among cells with grid[r][c] == -buildings, return the min dist.
        - Complexity: Worst-case O(B·R·C) time, O(R·C) space (no per-BFS visited; practical constant factors much lower).
            - Time Complexity: O(m × n × b)
            - Space Complexity: O(m × n)

## *** IMPORTANT*** 
36. diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: Diameter of Binary Tree
    - “I compute the tree’s diameter with one post-order DFS. The helper returns each node’s height (max depth of its subtrees). At every node, the longest path through it is left_height + right_height; I update a global max_diameter with that. Then I return 1 + max(left_height, right_height) to the parent. After visiting all nodes, max_diameter is the answer. Time: O(n) (each node once). Space: O(h) recursion stack (h = tree height).”
    - Intuition (≈30s): The tree’s diameter is the longest path between any two nodes. That path must pass through some node as “middle,” using its left height + right height. So if we know the height of every subtree, we can try each node as a middle and keep the best left_height + right_height.
    - Approach (≈30s): Do one post-order DFS that returns the height of each node’s subtree. For a node:
        1. Recursively get left and right heights (0 if None).
        2. Update a global max_diameter = max(max_diameter, left + right).
        3. Return 1 + max(left, right) to the parent. After DFS, max_diameter is the answer.
    - Time: O(n) (visit each node once). Space: O(h) recursion stack (h = height).
        - Time Complexity: O(n)
        - Space Complexity: O(h)

## *** IMPORTANT*** 
37. accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]: Accounts Merge problem using Union-Find (Disjoint Set Union)
    - “I use Union–Find (DSU) to group emails that belong to the same person. For each account, I take the first email as the anchor and union it with every other email in that account. I also map every email → name. After processing all accounts, I find the root parent for each email and collect emails per root (a set). Finally, for each group I output [name] + sorted(emails), using the name associated with the root. Path compression keeps operations near-constant. Time: ~O(N·α(N) + E·logE) where N = emails (union/find), E = emails per group for sorting. Space: O(N) for DSU/maps.”
    - Intuition (≈30s): If two emails ever appear in the same account row, they belong to the same person. So all emails that are connected through these rows should be grouped together. This is exactly a connectivity problem: treat each email as a node and connect (union) all emails in a row; each connected component is one person’s set of emails.
    - Approach (≈30s): Use Disjoint Set Union (Union–Find):
        1. For each account, remember the name and union the first email with every other email in that row (also record email → name).
        2. After processing all rows, find the root of each email and group emails by root.
        3. For each group, output [name] + sorted(emails) where name is from any email in the group.
    - Complexity: near O(N α(N)) for unions/finds over N emails, plus sorting per group (dominates). Space: O(N) for DSU/maps.
        - Time Complexity: O(N × α(N) + M log M)
        - Space Complexity: O(N) for parent map, email-to-name map, and groupings

## *** IMPORTANT*** 
38. treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]': Convert a Binary Search Tree (BST) to a sorted Circular Doubly Linked List in place
    - “I convert a BST to a sorted circular doubly linked list using an in-order DFS. I keep two pointers: first (head) and last (tail). During inorder, when I visit a node, I stitch it after last (last.right = node; node.left = last); if last is None, this is the first node. Then I set last = node and continue. After traversal, I make it circular by linking first.left = last and last.right = first. Inorder guarantees ascending order. Time: O(n). Space: O(h) recursion stack (h = tree height).”
    - Intuition (≈30s): A BST’s in-order traversal visits nodes in sorted order. If we walk in-order and keep two pointers—first (the head) and last (the most recently visited)—we can stitch each visited node after last to form a doubly linked list in ascending order. After the traversal, connect first and last to make it circular.
    - Approach (≈30s): Do an in-order DFS:
        1. Recurse left.
        2. On visit: if last exists, link last.right = node and node.left = last; else set first = node. Then set last = node.
        3. Recurse right. After DFS, close the ring with first.left = last and last.right = first.
    - Time: O(n) (each node once). Space: O(h) recursion (h = tree height).
        - Time	O(n)	Each node is visited once
        - Space	O(h)	Recursion stack, where h is the height of the tree

## *** IMPORTANT*** 
39.  isBipartite(self, graph: List[List[int]]) -> bool: Is Graph Bipartite?
    - “I check bipartiteness by 2-coloring each connected component with BFS. I keep a color array initialized to −1. For every unvisited node, I start a BFS, assign it color 0, and for each edge (u,v) I assign v the opposite color 1 - color[u]. If I ever see a neighbor already colored the same as its parent, there’s an odd cycle → not bipartite, return False. If all components color successfully, return True. Time: O(V+E). Space: O(V) for the queue and color array.”
    - Intuition (≈30s): A graph is bipartite if you can split its nodes into two groups so that no edge stays within the same group. That’s the same as being able to 2-color the graph: adjacent nodes must have opposite colors. If during coloring you ever need to give the same color to both ends of an edge, the graph isn’t bipartite.
    - Approach (≈30s): Run BFS on each unvisited component. Keep a color array initialized to −1. For a new start node, set color 0 and push it. While the queue isn’t empty, pop a node and try to color all neighbors with 1 - color[node].
        - If a neighbor is uncolored, color it and enqueue.
        - If a neighbor already has the same color, return False.
        - If all components color successfully, return True.
    - Complexity: O(V+E) time, O(V) space.
        - Time	O(V + E)	Each node and edge is visited once
        - Space	O(V)	For color array and BFS queue

## *** IMPORTANT*** 
40. verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]: Binary Tree Vertical Order Traversal
    - “I do a BFS with column indices. Start at the root with column 0, push (node, col) into a queue. When I pop a node, I append its value to column_table[col], then push left with col−1 and right with col+1. While traversing, I track min_col/max_col. BFS preserves top-to-bottom, left-to-right order within each column. At the end, I output columns from min_col to max_col. Time: O(n) to visit nodes; Space: O(n) for the table and queue.”
    - Intuition (≈30s): Think of each node having a column index: root at 0, left child at col−1, right child at col+1. If we traverse the tree level by level (BFS) while tracking columns, all nodes that share the same column form one “vertical” slice. BFS naturally preserves top-to-bottom, left-to-right order within each column.
    - Approach (≈30s): Use a queue of (node, col) starting with (root, 0). Pop a node, append its value to column_table[col], update min_col/max_col, then push left with col−1 and right with col+1. After BFS ends, output columns in order from min_col to max_col using column_table. 
    - Complexity: O(n) time to visit each node once; O(n) space for the table and queue.
        - Time	O(n)	Each node is visited once
        - Space	O(n)	For queue and column table

## *** IMPORTANT*** 
41. letterCombinations(self, digits: str) -> List[str]: Letter Combinations of a Phone Number
    - “I generate all phone keypad combinations with backtracking. At position index, I iterate the letters mapped from digits[index], append one letter to the current path, recurse to the next index, and backtrack. When index == len(digits), I add the built string to result. This explores the full Cartesian product in lexical order. Time: O(3^m · 4^n) where m digits map to 3 letters and n to 4 (7/9), since we must output all combos; space: O(L) recursion depth (L = number of digits) plus output size.”
    - Intuition (≈30s): Each digit maps to a small set of letters. The result is the Cartesian product of these sets in digit order. So we can build combinations by walking digit-by-digit and appending one letter choice at a time until we’ve picked one letter per digit.
    - Approach (≈30s): Use backtracking:
        1. If index == len(digits), push the built string path to results.
        2. Otherwise, loop the letters mapped from digits[index], append one to path, recurse on index+1, then return (implicit backtrack since path is passed as a new string). 
    - Complexity: Output-size bound: O(3^m · 4^n) where digits 7/9 contribute 4 letters and others 3; recursion depth O(L) (number of digits).
        - Time	O(4ⁿ)	Each digit can map to up to 4 letters (e.g., '7', '9')
        - Space	O(n)	Recursion depth and path string

42. Permutations
    - 42a. Method 1 : permute(self, nums: List[int]) -> List[List[int]]:
        - “I generate all permutations with backtracking + in-place swapping. At position start, I try each choice i ∈ [start..n-1]: swap nums[start] with nums[i] to fix that element, recurse on the next position, then swap back to restore state. When start == n, I copy the current arrangement into result. This explores every ordering exactly once. Time: O(n · n!) (n! permutations, ~n work to copy), space: O(n) recursion (excluding output).”
        - If they ask for an alternative: use a used set and build a path list instead of swapping.
        - Intuition (≈30s): We can generate all permutations by fixing one position at a time. At index start, try every remaining element in that spot. Place a candidate there (swap), recursively permute the rest, then swap back to restore the array before trying the next candidate. This explores every ordering exactly once.
        - Approach (≈30s): Use backtracking with in-place swaps:
            1. If start == len(nums), append a copy of nums to result.
            2. For each i from start to n-1:
                - swap(nums[start], nums[i]) to fix nums[start].
                - Recurse with start + 1.
                - Backtrack: swap back to undo the change. 
        - Complexity: Time O(n · n!) (n! permutations, up to n to copy each), Aux space O(n) recursion (output excluded).
            - Time	O(n!)	There are n! permutations
            - Space	O(n)	Recursion stack depth is n
    - 42b. Method 2 : permuteNoInplaceSwaps(nums: List[int]) -> List[List[int]]:
        - “I build permutations by growing a path and tracking which indices are used. For each position, I iterate all indices; if unused, I mark it, append the number, recurse, then backtrack (pop + unmark). When path length reaches n, I record a permutation. This avoids in-place swaps. Time: O(n·n!), space: O(n) recursion + O(n) for used (excluding output).”
        - If you have duplicates in nums, add a sort and a “skip duplicates” guard inside the loop.
        - Intuition (≈30s): Build permutations by choosing one unused element at a time. Keep a growing path of chosen numbers and a used array to mark which indices are already in the path. When path reaches length n, you’ve formed one full ordering. Backtrack (undo the last choice) to explore all other possibilities.
        - Approach (≈30s): Initialize used=[False]*n, path=[], res=[]. In dfs():
            1. If len(path)==n, append a copy to res and return.
            2. Loop i in [0..n-1]: if not used[i], then:
                - mark used[i]=True, path.append(nums[i])
                - recurse dfs()
                - backtrack: path.pop(), used[i]=False. Return res after dfs()
        - Complexity: Time O(n·n!) (n! perms, copy cost up to n); Aux space O(n) for path+used (output excluded).
    - 42c. Method 3 : permuteUnique(self, nums: List[int]) -> List[List[int]]: Permutations II - Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
        - “I generate unique permutations with backtracking. I first sort nums so duplicates are adjacent. At each position I iterate indices; if an index is already used, skip. To avoid duplicate branches, I also skip a value if it’s the same as the previous and the previous hasn’t been used yet (i>0 and nums[i]==nums[i-1] and not used[i-1]): that ensures we only place the first copy of a duplicate before its twins at a given depth. I append, recurse, then backtrack (pop + unmark). Time: O(n·n!) in worst case; space: O(n) recursion + used (excluding output).”
        - Intuition (≈30s): We need all unique permutations even when numbers repeat. If we sort the array first, equal numbers sit next to each other. Then while building a permutation, we can avoid duplicate branches by never picking the same value twice at the same tree level—i.e., if nums[i] == nums[i-1] and the previous twin hasn’t been used yet, skip nums[i].
        - Approach (≈30s): Use backtracking with a used array:
            1. Sort nums.
            2. At each step, loop i over indices:
                - Skip if used[i] is True.
                - Duplicate guard: skip if i>0 and nums[i]==nums[i-1] and not used[i-1].
                - Choose nums[i] → mark used[i]=True, append to path, recurse.
                - Backtrack → pop and unmark.
                - When path length equals n, add a copy to results. 
        - Complexity: worst case O(n·n!) time to output all perms; pruning removes duplicates. Space: O(n) recursion + used (excluding output).
            - Time	O(n × n!)	Worst-case with all unique elements
            - Space	O(n)	Recursion depth and used array

## *** IMPORTANT*** 
43. removeInvalidParentheses(self, s: str) -> List[str]: Remove Invalid Parentheses
    - “I solve it with BFS over strings formed by deleting one parenthesis at a time. BFS ensures the first valid level we reach uses the minimum removals; once any string at a level is valid, I collect all valid strings at that same level and don’t expand deeper. I keep a visited set to avoid revisiting duplicates. Validity is checked by a single pass counter that never lets closes exceed opens and ends at zero. Time (worst case): O(2^P · n)—we may generate and validate exponentially many candidates (P = number of parentheses, n = length for validation). Space (worst case): O(2^P) for the queue + visited.”
    - Intuition (≈30s): We want all valid strings formed by removing the fewest parentheses. If we explore strings by deleting one char at a time, then the first level where we find any valid strings must already be minimum removals (because BFS explores by distance). So the plan: level-by-level delete one paren, stop expanding deeper as soon as we see a valid string, and collect all valid strings at that level.
    - Approach (≈30s): Use BFS with a queue and visited set. Start with s. While the queue isn’t empty:
        1. Pop a string; if it’s valid (single pass counter never drops below 0, ends at 0), add to result and mark found=True.
        2. If found, skip generating children (ensures minimum removals).
        3. Otherwise, generate next states by removing one parenthesis at each index (skip non-paren chars) and enqueue unseen strings. Return result (or [""] if none). 
    - Worst-case: Time O(2^P · n), Space O(2^P) (P = # of parentheses, n = length).
        - Time	O(2ⁿ × n)	Worst-case: generate all substrings
        - Space	O(2ⁿ)	For queue and visited set
    
44. Regular Expression Matching 
    - 44a. isMatch(self, s: str, p: str) -> bool:  using Dynamic Programming,
        - “We build a table that answers: ‘Do the first i letters of the text match the first j letters of the pattern?’ We fill it left-to-right, top-to-bottom. A normal letter or dot . matches one character: we just look diagonally up-left (did the previous parts match?). A star * means the previous thing can appear zero times (skip the pair, look two cells left) or one/more times (stay on the same pattern column but move up one row if the current text char fits). Initialize empty=empty as True and allow patterns like a* to match empty. The final cell tells us if the whole strings match. Runs in O(m·n) time, O(m·n) space (O(n) with 1D DP).”
        -  “I do regex matching with DP over prefixes. Let dp[i][j] mean s[:i] matches p[:j]. Base: dp[0][0]=True; also prefill the first row for patterns like a*, a*b* where * can delete its preceding char: dp[0][j]=dp[0][j-2] when p[j-1]=='*'. For transitions: if p[j-1] is a literal or '.', match it with s[i-1] → dp[i][j]=dp[i-1][j-1]. If p[j-1]=='*', either use zero of the preceding char → dp[i][j]=dp[i][j-2], or use one+ if p[j-2] equals s[i-1] (or '.') → dp[i][j]|=dp[i-1][j]. Answer is dp[m][n]. Time: O(m·n). Space: O(m·n) (can be reduced to O(n) with row DP).”
        - Intuition (≈30s): We decide if the prefix of the text matches the prefix of the pattern. Normal letters must match exactly; . matches any single char; * means “the previous token can appear zero or more times.” So at each position we ask: did the smaller prefixes match, and does the current token fit (possibly using * to either skip the token or consume one more char)?
        - Approach (≈30s): Let dp[i][j] mean s[:i] matches p[:j].
            1. Base: dp[0][0]=True. Prefill row 0 for patterns like a*, a*b* via dp[0][j]=dp[0][j-2] when p[j-1]=='*'.
            2. Transition:
                - If p[j-1] is a letter or . and matches s[i-1]: dp[i][j]=dp[i-1][j-1].
                - If p[j-1]=='*':
                    - Zero uses of prev token: dp[i][j] |= dp[i][j-2].
                    - One+ uses if prev token matches s[i-1] (or is .): dp[i][j] |= dp[i-1][j].
            3. Answer is dp[m][n]. 
        - Complexity: O(m·n) time, O(m·n) space (can reduce to O(n) with 1D DP).
            - Time	O(m × n)	Nested loops over s and p
            - Space	O(m × n)	DP table of size (m+1) × (n+1)
    - 44b. def isMatchRecurssive(self, s: str, p: str) -> bool: Recursive Version with Memoization
        - “I match the text and pattern from their current positions. A normal letter must match the same letter; a dot . matches any one letter. If the next pattern symbol is a star *, it means ‘the previous thing can repeat’: I try two options—either skip that x* entirely (use it zero times) or, if the current letter fits, use it once and stay on the same pattern spot to keep repeating. I memoize results for each (text, pattern) position so I don’t rework the same cases. This covers all possibilities efficiently (about m×n cases).”
        - “I do regex match with top-down recursion + memo. dp(i, j) asks: do s[i:] and p[j:] match? 
            Base: if pattern is finished, we must also be at the end of the string.Compute first_match = current chars match (or pattern has .).
            If the next pattern char is *, we try two choices: skip the x* (zero uses) → dp(i, j+2), or use it if first_match (consume one char from s) → dp(i+1, j).
            Otherwise, advance both on a match → dp(i+1, j+1).
            lru_cache memoizes subproblems, making it O(m·n) time and O(m·n) space.”
        - Intuition (≈30s): Match the text and pattern from their current positions. A normal letter must match the same letter; a dot . matches any single char. If the next pattern symbol is *, it means “the previous thing can repeat.” So at each step we either skip x* (use it zero times) or, if the current char fits, consume one char from the text and try to match x* again. Memoize results for each (i, j) to avoid recomputing.
        - Approach (≈30s): Define dp(i, j) = does s[i:] match p[j:]?
            1. Base: if j == len(p), return i == len(s).
            2. first_match = i < len(s) and (p[j] == s[i] or p[j] == '.').
            3. If j+1 < len(p) and p[j+1] == '*':
                - Zero uses: dp(i, j+2) (skip x*).
                - One+ uses: if first_match, dp(i+1, j) (consume a char, keep x*).
            4. Else (no *): return first_match and dp(i+1, j+1). Use @lru_cache on (i, j).
        - Time: O(m·n). Space: O(m·n) for memo (stack up to O(m+n)).
            - Time	O(m × n)	Memoized calls for each (i, j) pair
            - Space	O(m × n)	Cache and recursion stack

45. subsets(self, nums: List[int]) -> List[List[int]]: Subsets
    - “I list every subset by walking a decision tree: for each number I can take it or skip it. I keep a small list called path with what I’ve taken so far. At every step I first record the current path (that’s one valid subset), then I try adding the next number, go deeper, and undo (pop) to try the next option. Doing this for all positions systematically produces all combinations. There are 2^n subsets total; we spend up to n steps building each, so about  O(n⋅2^n) time; extra space is O(n) for the current path.”
    - “I generate all subsets with backtracking. Starting at index 0, I add the current path to results (that’s one subset), then for each next index i I choose nums[i], recurse on the remainder, and backtrack (pop) to try other choices. This systematically explores the ‘take it / skip it’ tree for every element, so we get all 2^n subsets. Time: O(n⋅2^n) (each subset built up to length n). Space: O(n) recursion (excluding the output).”
    - Intuition (≈30s): Think of building subsets by walking a decision tree: for each element you can take it or skip it. If you explore all take/skip choices in order, every path you record along the way is a valid subset. This naturally produces all combinations, from the empty set to the full set.
    - Approach (≈30s): Use backtracking with a growing path and a start index.
        1. At each call, record the current path (it’s one subset).
        2. Loop i from start to end:
            - Choose nums[i] → path.append(nums[i]).
            - Recurse with backtrack(i+1, path) to pick further elements.
            - Un-choose → path.pop() to try the next option. This explores all 2ⁿ subsets.  
    - Time	O(n2ⁿ) Extra space: O(n) recursion (output excluded).
        - Time	O(n2ⁿ)	Each element has two choices: include or exclude
        - Space	O(n)	Recursion depth and temporary path

46. findStrobogrammatic(self, n: int) -> List[str]: Strobogrammatic Number II - all strobogrammatic numbers of length n
    - “I build strobogrammatic numbers from the middle outward using valid mirror pairs: (0,0),(1,1),(6,9),(8,8),(9,6). Recursively generate all valid middles for length n-2, then wrap each middle with every pair a…b. For odd n, the middle can be only 0,1,8. To avoid leading zeros, when filling the outermost layer I skip the (0,0) pair. This produces all numbers whose 180° rotation is itself. Time is exponential—about O(5^{⌊n/2⌋}) to generate all outputs; recursion depth is O(n).”
    - Intuition (≈30s): A strobogrammatic number looks the same when rotated 180°. That only happens with specific mirror pairs of digits: (0,0) (1,1) (6,9) (8,8) (9,6), and for the center of an odd-length number, only 0, 1, 8 work. So we can build numbers from the middle outward, wrapping valid pairs symmetrically. Return the collected strings.
    - Approach (≈30s): 
        1. Use recursion on length n.
            - Base: n==0 → [""], n==1 → ["0","1","8"].
            - For n≥2, first build all valid middles of length n-2, then for each middle, wrap with every pair (a,b) to form a + middle + b.
            - To avoid leading zeros, skip (0,0) at the outermost layer (when n == total_len).
    - Complexity: Generates all answers: about O(5^{⌊n/2⌋}) time and O(n) recursion depth (output dominates).
        - Time	O(5^(n/2))	Each level adds up to 5 pairs
        - Space	O(5^(n/2))	Result list and recursion stack
    
47. divide(self, dividend: int, divisor: int) -> int: Divide Two Integers Without Using Multiplication, Division, or Modulus Operators
    - “I implement integer division using repeated doubling with bit shifts. After handling the INT_MIN / -1 overflow case and figuring out the sign, I work with positives. While the dividend ≥ divisor, I double (<<) the divisor (temp_divisor) and a multiple until doubling would exceed the dividend. Then I subtract that biggest chunk from the dividend and add multiple to the quotient. Repeat until the dividend is smaller than the divisor, then apply the sign. This simulates long division efficiently using powers of two. Time: about O(log² N) in worst case (doubling inside a loop), Space: O(1).”
    - Intuition (≈30s): "Long division by hand repeatedly subtracts big chunks of the divisor from the dividend. We can mimic that fast by using powers of two: keep doubling the divisor (via bit shifts) to find the largest multiple that still fits into the remaining dividend, subtract it, and add that multiple to the answer. Repeat until what’s left is smaller than the divisor. Handle sign and the one overflow case (INT_MIN / -1)." 
    - Approach (≈30s): 
        1. Handle overflow: if dividend == INT_MIN and divisor == -1, return INT_MAX
        2. Compute the sign; work with absolute values.
        3. While dividend ≥ divisor:
            - Set temp = divisor, mul = 1.
            - While (temp << 1) ≤ dividend: do temp <<= 1, mul <<= 1 (double both).
            - Subtract: dividend -= temp; accumulate: quotient += mul.
        4. Apply sign to quotient and return.
    - Complexity: ~O(log² N) worst case (outer loop × inner doubling), O(1) space.
        - Time	O(log n)	Each loop halves the dividend
        - Space	O(1)	Constant space used

## *** IMPORTANT*** 
48. isAlienSorted(self, words: List[str], order: str) -> bool: Verifying an Alien Dictionary
    - “I verify the dictionary order by mapping each alien letter to its rank, then comparing adjacent words. For each pair, I scan characters left→right; at the first difference, I check if word1’s char rank < word2’s—if not, it’s unsorted. If all compared chars are equal, the shorter word must come first (to handle prefix cases). Do this for every adjacent pair; if none violate the rule, it’s sorted. Time: O(total characters across all words). Space: O(1) for the 26-char map (or O(Σ) for the alphabet size).”
    - Intuition: We just need to know the ordering of letters in the alien alphabet and then check whether the list of words respects that order. If you compare each pair of adjacent words the same way a dictionary does—scan left to right and stop at the first differing character—you can tell if the earlier word should indeed come first. One extra edge case: if one word is a prefix of the other, the shorter word must come first.
    - Approach: 
        1. Build a map order_index[ch] = rank from the alien order.
        2. For each adjacent pair (w1, w2), compare chars c1, c2 left→right:
            - If ranks differ, ensure rank(c1) < rank(c2); otherwise return False.
            - If all compared chars are equal, ensure len(w1) <= len(w2) (prefix rule).
        3. If all pairs pass, return True. 
    - Complexity: Time O(total characters), Space O(Σ) for the rank map (Σ = alphabet size).
        - Time complexity: O(N⋅L) Where: N is the number of words. L is the average length of the words. We compare each pair of words character by character.
        - Space complexity: O(1) - The character-to-index mapping uses a fixed size of 26 characters, so it’s constant space.

## *** IMPORTANT*** 
49. minRemoveToMakeValid(self, s: str) -> str: Minimum Remove to Make Valid Parentheses
    - “I scan once, matching parentheses with a stack. Unmatched ')' get marked immediately; unmatched '(' left on the stack after the scan are also marked. Then I rebuild the string, skipping only those marked indices—this yields a valid string with the minimum removals. Runs in O(n) time, O(n) space.”
    - Intuition: We want to remove the fewest parentheses so the string is valid. Scan once to determine which parens are unmatched: push indices of '(' onto a stack; when we see ')', pop a '(' if available, otherwise mark this ')' as invalid. Any '(' left in the stack at the end are also invalid. Finally, rebuild the string skipping all invalid indices. 
    - Approach: 
        1. Traverse s with a stack of indices for '(' and a set to_remove.
        2. On '(' → push index. On ')':
            - If stack non-empty → pop (matched).
            - Else → add index to to_remove (unmatched right).
        3. After the scan, add any leftover '(' indices from the stack to to_remove.
        4. Build the result by concatenating chars whose indices are not in to_remove.
    - Time: O(n). Space: O(n) in worst case for the stack/set.
        - Time Complexity: O(n)
            One pass to identify invalid parentheses.
            One pass to build the result string.
        - Space Complexity: O(n)
            Stack and to_remove set can grow up to size of input in worst case.
            Result list also takes up to O(n) space.

## *** IMPORTANT*** 
50. Nested List Weight Sum
    - 50a. Method 1: depthSum_Recursive_DFS(self, nestedList: List[NestedInteger]) -> int:
        - “I treat the nested list as a tree and do a DFS carrying the current depth. If I see an integer, I add value * depth; if I see a sublist, I recurse with depth+1 and add that sum. Starting at depth 1, this naturally multiplies deeper integers more. It visits each element once—O(N) time, O(D) stack.”
        - Intuition: A nested list is like a tree: each list is a node whose children are either integers (leaves) or sublists. The problem says “weight by depth,” so every time we go one level deeper, that integer’s contribution should be multiplied by +1 depth. A natural fit is a depth-first traversal that carries the current depth along.
        - Approach: Use a recursive DFS dfs(nlist, depth):
            1. Initialize total = 0.
            2. For each item:
                - If it’s an integer, add item.getInteger() * depth.
                - Otherwise, recurse on item.getList() with depth + 1 and add the result.
            3. Return total.
                - Call dfs(nestedList, 1) and return the sum.
        - Time: O(N) where N is total integers + lists. Space: O(D) recursion stack, D = max depth.
            - Time Complexity: O(n) Where n is the total number of integers and lists in the structure. Each element is visited once.
            - Space Complexity: O(d) Where d is the maximum depth of nesting due to recursive call stack.
    - 50b. Method 2: depthSum_Iterative(self, nestedList: List['NestedInteger']) -> int:
        - “I do a BFS over the nested structure, carrying the current depth in the queue. For each popped list, every integer adds value * depth; every sublist gets enqueued with depth+1. This visits everything once and accumulates the weighted sum. Time O(N), space O(W).”
        - Intuition: Treat the nested list like a tree where each sublist is a node and each integer is a leaf. Since each integer’s contribution is weighted by its depth, traverse level by level and multiply each integer by the depth at which you encounter it. A simple BFS naturally tracks depth as you go.
        - Approach: Use a queue of (list, depth), initialized with (nestedList, 1). While the queue isn’t empty, pop a pair and scan its items:
            1. If item.isInteger(): add item.getInteger() * depth to total.
            2. Else: push (item.getList(), depth + 1) back into the queue. Return total after processing all levels.
        - Complexity: O(N) time over all integers and lists; O(W) space for the queue (W = max breadth).
            - Time Complexity:  O(n) — each element is visited once.
            - Space Complexity: O(n) — queue stores elements at each level.

51. search(self, nums: List[int], target: int) -> int: Search in Rotated Sorted Array using binary search
    - “I run a binary search that, at each step, figures out which side is sorted. If the left side [left..mid] is sorted and the target lies inside its range, I search there; otherwise I search the right side. If the right side is sorted, I apply the same logic symmetrically. This halves the search space each time and returns the index if found, or -1. O(log n) time, O(1) space.”
    - Intuition: In a rotated sorted array, at any time one half is still sorted. If we pick the middle, either the left half [left..mid] is sorted or the right half [mid..right] is sorted. If the target falls within the sorted half’s range, we discard the other half; otherwise we discard this half. Repeat like binary search.
    - Approach: Do a modified binary search:
        1. Compute mid. If nums[mid] == target, return mid.
        2. If nums[left] <= nums[mid], left half is sorted:
            - If nums[left] <= target < nums[mid], move right = mid - 1; else left = mid + 1.
        3. Else, right half is sorted:
            - If nums[mid] < target <= nums[right], move left = mid + 1; else right = mid - 1.
            - If not found, return -1. 
    - Time: O(log n). Space: O(1).
        - Time Complexity: O(logn) — binary search.
        - Space Complexity: O(1) — constant space.

52. searchRange(self, nums: List[int], target: int) -> List[int]: Find First and Last Position of Element in Sorted Array using binary search
    - “I run two binary searches. The first, when it hits target, keeps going left to nail the first index; the second keeps going right to nail the last index. If the value isn’t found, I return [-1, -1]. This is O(log n) time and constant space.”
    - Intuition: In a sorted array, all occurrences of target form one contiguous block. We can find the first and last indices separately with binary search variants: when we see target, keep searching left to find the earliest index, and right to find the latest. If target doesn’t exist, both searches return -1.
    - Approach: Write a helper find_bound(is_left) that does binary search:
        1. Maintain left, right, and bound = -1.
        2. While left <= right: compute mid.
            - If nums[mid] == target: set bound = mid, then
                if is_left: move right = mid - 1 (push left),
                else: move left = mid + 1 (push right).
            - Else if nums[mid] < target: left = mid + 1;
            - Else: right = mid - 1. 
            - Run start = find_bound(True) and end = find_bound(False), return [start, end].
    - Time: O(log n) per search → O(log n) total. Space: O(1).
        - Time Complexity: O(logn) — binary search twice.
        - Space Complexity: O(1) — no extra space used.

53. myPow(self, x: float, n: int) -> float: Pow(x, n) using binary exponentiation
    - “I use fast exponentiation. Treat n in binary: while n > 0, if the current bit is 1, multiply result by x. Each step I square x and halve n. For negative powers, flip to (1/x) and use -n. This computes x^n in O(log n) multiplications and constant space.”
    - Intuition: Raising x to n doesn’t need n multiplications. Use the fact that:
        if n is even, x^n = (x^2)^(n/2)
        if n is odd, x^n = x * x^(n-1)
        So we can square x and halve n repeatedly, multiplying into the answer only when the current bit of n is 1. For negative n, compute x^{-n} as (1/x)^n.
    - Approach: 
        1. If n < 0, set x = 1/x, n = -n.
        2. Initialize result = 1.
        3. While n > 0:
            If n is odd (n % 2 == 1), result *= x.
            Square x (x *= x) and integer-divide n //= 2.
        4. Return result.
    - Complexity: O(log n) time (processes bits of n), O(1) space.
        - Time Complexity: O(logn) — binary exponentiation.
        - Space Complexity: O(1) — constant space.

54. merge(self, intervals: List[List[int]]) -> List[List[int]]: Merge Intervals using sorting and iteration
    - “I sort by start so overlaps come adjacent. Walk once, keeping a merged tail. If the next interval’s start is within the last merged end, I extend the end; if not, I start a new interval. That single pass after sorting yields all merged ranges. Runs in O(n log n) time, O(1) extra space.”
    - Intuition: Overlaps are easiest to see when intervals are sorted by start. Then you only need to compare each interval to the last merged one: if the current start is ≤ last end, they overlap and should be merged; otherwise, start a new block.
    - Approach: 
        1. Sort intervals by start.
        2. Initialize merged with the first interval.
        3. For each current:
            Let last = merged[-1].
            If current.start ≤ last.end, set last.end = max(last.end, current.end) (merge).
            Else, merged.append(current) (no overlap).
            Return merged. 
    - Time: O(n log n) (sorting), Space: O(1) extra (in-place list of results).
        - Time Complexity: O(nlogn) — due to sorting
        - Space Complexity: O(n) — for storing the merged intervals
        - Auxiliary space (excluding output): O(1) — we sort in place and only keep a few variables.
        - Total space (including output): O(n) — for the merged result.

55. findPeakElement(self, nums: List[int]) -> int: Find Peak Element
    - “I run a slope-following binary search. At mid, compare with mid+1: if it’s rising, a peak must be right, so move left = mid+1; if it’s falling, a peak is at/left, so set right = mid. Strict inequality guarantees we always shrink the search space. When pointers meet, that index is a peak. Time O(log n), space O(1).”
    - Intuition: A peak sits where the array stops rising and starts falling. If at some index mid we see nums[mid] < nums[mid+1], we’re on an uphill—there must be a peak to the right. If nums[mid] > nums[mid+1], we’re on a downhill—a peak lies at mid or to the left. Since adjacent values are all different, each comparison gives a strict direction to move.
    - Approach: Do a binary search over indices:
        1. Initialize left=0, right=n-1.
        2. While left < right:
            mid = (left+right)//2
            If nums[mid] > nums[mid+1]: set right = mid (keep left side).
            Else: set left = mid + 1 (go right).
            When the loop ends, left == right at a peak index. This works because “follow the slope” never skips all peaks.
    - Complexity: Time O(log n), space O(1).
        - Time Complexity: O(logn) — binary search.
        - Space Complexity: O(1) — constant space.

56. firstBadVersion(self, n: int) -> int:  First Bad Version problem using binary search, which minimizes the number of calls to the isBadVersion(version) API
    - “I do a binary search on version numbers. Check mid: if it’s bad, the first bad is at or before mid → move high = mid. If it’s good, the first bad is after mid → move low = mid + 1. When low meets high, that index is the first bad version. This runs in O(log n) time and constant space.”
    - Intuition: Versions switch from good → bad at some unknown point and stay bad afterward. That monotonic pattern is perfect for binary search: if a middle version is bad, the first bad is at or before it; if it’s good, the first bad is after it. Repeatedly halving the search space finds the earliest bad version quickly.
    - Approach: Maintain low=1, high=n. While low < high:
        1. Compute mid = low + (high - low)//2 (avoids overflow).
        2. If isBadVersion(mid) is True, set high = mid (candidate could be earlier).
        3. Else set low = mid + 1 (must be later). When the loop ends, low == high and points to the first bad version.
    - Complexity: O(log n) time, O(1) space.
        - Time Complexity: O(logn) — binary search.
        - Space Complexity: O(1) — constant space.

57. intersection(self, nums1: List[int], nums2: List[int]) -> List[int]: Intersection of Two Arrays 
    - “I remove duplicates by converting both arrays to sets, then take their intersection to get the distinct values present in both. Convert that intersection back to a list and return it. Runs in linear time overall with linear extra space.”
    - Intuition: We only care about unique numbers that appear in both arrays. Sets naturally represent uniqueness and support fast membership checks and intersections. So, turning both lists into sets and intersecting them gives exactly the distinct common elements.
    - Approach: 
        1. Convert nums1 and nums2 to sets: set1, set2 (deduplicate).
        2. Compute set1 & set2 (set intersection).
        3. Return it as a list.
    - Complexity: Building sets is O(n + m) expected time; intersection is O(min(n, m)); overall O(n + m) time and O(n + m) space.
        - Time Complexity: O(n+m) Where n and m are the lengths of nums1 and nums2
        - Space Complexity: O(n+m) For storing the sets.

58. Intersection of Two Arrays II where each element in the result must appear as many times as it shows in both arrays.
    - 58a. Method 1: intersect(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        - “I compute frequencies for both arrays, then for each value present in both, I add it to the output min(count in nums1, count in nums2) times. That directly models intersection with duplicates. Runs in linear time with linear extra space for the counts.”
        - Intuition: This is the intersection with multiplicity: if 2 appears 3 times in nums1 and 1 time in nums2, it should appear min(3,1)=1 time in the result. So just count how many times each value occurs in each array, then for every common key, take the minimum count.
        - Approach: Build two frequency maps: count1 = Counter(nums1), count2 = Counter(nums2). 
        1. Iterate keys of the smaller map (or count1 as in your code):
            If the key exists in count2, append [key] * min(count1[key], count2[key]) to the result. Return the built list.
        - Complexity: Time O(n + m) to count + up to O(U) to merge (U = unique keys). Space O(n + m) for the counters.
            - Time Complexity: O(n+m) Where n and m are the lengths of nums1 and nums2.
            - Space Complexity: O(n+m) For storing the frequency maps.
    - 58b. Method 2: intersectTwoPointer(self, nums1: List[int], nums2: List[int]) -> List[int]: two-pointer version for sorted arrays
        - When to Use This:
            - When arrays are already sorted, this method avoids extra space and is very efficient.
            - Especially useful when working with large datasets or streamed data.
        - “I sort both lists and sweep with two pointers. When they’re equal, I record the value and move both; otherwise I advance the pointer with the smaller value. This collects the intersection with correct multiplicities in one pass after sorting. Time: O(n log n + m log m) for sorting + O(n+m) scan; Space: O(1) extra (output aside).”
        - Intuition: If both arrays are sorted, common elements appear in the same order. Walk them with two pointers: when values match, it’s part of the intersection; otherwise, advance the pointer on the side with the smaller value to catch up. This naturally handles duplicates (each match consumes one occurrence on both sides).
        - Approach: Sort nums1 and nums2. Initialize pointers i=j=0 and an empty result. While i < len(nums1) and j < len(nums2):
            If nums1[i] == nums2[j]: append to result, increment both.
            Else if nums1[i] < nums2[j]: increment i.
            Else: increment j.
            Return result.
        - Time: O(n log n + m log m) for sorting + O(n+m) scan; Space: O(1) extra (output aside).
            - Time Complexity: O(nlogn+mlogm) for sorting, O(n+m) for traversal→ Total: O(nlogn+mlogm)
            - Space Complexity: O(1) extra space (excluding result)
    - 58c. Method 3: (Pseudo simulation) intersect_streaming(self, nums1, nums2_stream): disk-based streaming scenario for the intersection of two arrays with duplicates, where nums2 is too large to fit into memory.
        - “I preload the small array into a Counter and then scan the huge array streaming from disk. For each streamed number, if the counter says we still need it, I output it and decrement the count. This preserves multiplicities, uses memory proportional to the small array (not the big one), and runs in linear time over both inputs.”
        - Intuition: When one array fits in memory and the other is too big (e.g., on disk), build a frequency map of the in-memory array. Then stream the large array in chunks, and for each element, emit it only if the map still has remaining count. This yields the correct intersection with multiplicities while keeping memory bounded.
        - Approach: 
            1. Counter(nums1) stores how many times each value can still match.
            2. Read nums2 chunk-by-chunk (generator).
            3. For each number in a chunk: if count1[num] > 0, append to result and decrement.
            4. Continue until the stream ends; return result.
        - Complexity: Time O(n + m) where n=len(nums1), m=len(nums2); Memory O(U1) for the counter (U1 = unique in nums1) plus O(chunk_size). Works without sorting and with duplicates.
            - Time Complexity: O(n+m) — where n is size of nums1, m is total elements in nums2.
            - Space Complexity:O(n) — for storing frequency map of nums1.

59. Longest Palindromic Substring
    - 59a. Method 1: longestPalindrome(self, s: str) -> str: Longest Palindromic Substring using the expand-around-center technique
        - “I try each index as a center and expand outwards for odd and even palindromes. The helper expands while characters match and returns the length. If this center’s palindrome is longer than my current best, I update [start, end]. After scanning all centers, I return the substring s[start:end+1]. It’s simple, in-place, and runs in O(n²) time.”
        - Intuition: Every palindrome is defined by a center and expands symmetrically. For each index, there are two possible centers: the character itself (odd-length) and the gap between it and the next character (even-length). If we expand outward while ends match, we can find the longest palindrome centered there. Taking the best over all centers yields the answer.
        - Approach: Loop i over all indices. For each i, compute:
            1. len1 = expand(i, i) for odd palindromes,
            2. len2 = expand(i, i+1) for even palindromes.
            3. Pick max_len = max(len1, len2). If it beats the current best [start, end], update: 
            start = i - (max_len - 1)//2, end = i + max_len//2.
            expand(l, r) moves l--, r++ while in-bounds and s[l]==s[r], then returns length r - l - 1. Finally return s[start:end+1]. 
        - Time: O(n²) worst case, Space: O(1).
            - Time Complexity: O(n^2) — each center expansion can take up to O(n).
            - Space Complexity: O(1) — no extra space used beyond variables.
    - 59b. Method 2: longestPalindromeDP(self, s: str) -> str: using dynamic programming 
        - “I fill a DP table where dp[i][j] tells if s[i..j] is a palindrome. Singles are true; doubles are true if the two chars match; longer ones are true when ends match and the middle dp[i+1][j-1] is true. I iterate lengths from small to large, updating the best window whenever I mark True. Finally I slice out that longest palindromic substring.”
        - Intuition: A substring s[i..j] is a palindrome iff the ends match (s[i]==s[j]) and the inside is a palindrome (s[i+1..j-1]). That gives a natural DP substructure: build answers for short substrings and reuse them to decide longer ones. Track the longest true window as you go.
        - Approach: Create dp[i][j] = True if s[i..j] is palindromic.
            1. Base cases: all length-1 substrings are True; check length-2 pairs (s[i]==s[i+1]).
            2. For lengths 3..n, for each start i (end j=i+len-1): set dp[i][j] = (s[i]==s[j] and dp[i+1][j-1]).
            3. Whenever dp[i][j] becomes True, update start and max_len.
            Return s[start:start+max_len].
        - Complexity: Time O(n²), space O(n²).
            - Time Complexity: O(n^2) — nested loops for all substrings.
            - Space Complexity: O(n^2) — DP table.
    - 59c. Method 3: longestPalindromeManacher(self, s: str) -> str: using Manacher’s Algorithm Optimal
        - “I insert # between characters so all palindromes are odd. As I scan, I keep the rightmost-known palindrome and use its mirror to prefill the radius at i, then only expand beyond the known boundary. If we beat the boundary, update the center/right. In the end, the largest radius maps directly to the longest palindromic substring.”
        - Intuition: Center-expansion is O(n²) because many centers repeat work. Manacher’s algorithm avoids this by keeping the rightmost palindrome seen so far (center, radius) and using mirror symmetry: the palindrome radius at position i is at least the mirror’s radius clipped to the current right boundary. Then we try to expand only the uncovered part. Preprocessing with separators (#a#b#…) makes odd/even palindromes uniform.
        - Approach: 
            1. Preprocess: t = '#' + '#'.join(s) + '#', so every palindrome has odd length.
            2. Maintain center and right boundary radius. For each index i:
                - Let mirror = 2*center - i. If i < right, seed radii[i] = min(right - i, radii[mirror]).
                - Expand around i while chars match, increasing radii[i].
                - If i + radii[i] > right, update center=i, right=i + radii[i].
            3. Take the index with max radius, map back to original string: start = (max_center - max_len)//2, answer is s[start:start+max_len].
        - Complexity: O(n) time, O(n) space.
            - Time Complexity: O(n) — linear scan with efficient reuse of previous computations.
            - Space Complexity: O(n) — for the radii array and preprocessed string.

## *** IMPORTANT*** 
60. Longest Valid Parentheses problem - 
    Optimal Solution?
    1. Best Overall: - Two-Pass Counter Method
        Constant space
        Linear time
        Elegant and handles all edge cases
    2. Best for Tracking Indices: - Stack Method
        Useful if you need to recover the actual substring or track positions
    3. Best for Substring Lengths: - Dynamic Programming
        Good for problems that require more detailed state tracking
    - 60a. Method 1: using a stack-based approach
        - “I walk the string with a stack of indices. I push '(' indices; on ')' I pop. If the stack empties, that ')' becomes the new base index; otherwise, the current valid length is i - stack[-1], and I update the max. A sentinel -1 handles prefixes cleanly. This finds the longest valid parentheses in O(n) time.”
        - Intuition: Use indices as anchors to measure valid spans. A closing ')' needs a matching '(' before it; if not, it resets the base of any future valid substring. A stack of indices tracks the last unmatched '('. Keeping an initial -1 sentinel lets us compute lengths directly as i - stack[-1] whenever we find a match.
        - Approach: Scan s with a stack of indices:
            1. Start stack = [-1], max_len = 0.
            2. On '(', push its index.
            3. On ')', pop once (using up one '(' if available).
                If stack becomes empty, push current index i (new base).
                Else, update max_len = max(max_len, i - stack[-1]) (length since last unmatched index). Return max_len. 
        - Time: O(n). Space: O(n).
            - Time Complexity: O(n) — single pass through the string.
            - Space Complexity: O(n) — stack stores indices.
    - 60b. Method 2: using Dynamic Programming (DP)
        - “I use DP where dp[i] is the length of the longest valid substring ending at i. When I see ')', either it pairs with i-1 (forming "()") or it pairs with a '(' that sits just before the valid block ending at i-1. In both cases I add 2 and, if applicable, chain with earlier lengths. Track the maximum over all i. Runs in O(n) time, O(n) space.”
        - Intuition: Let dp[i] be the length of the longest valid parentheses substring that ends at i. If s[i] is '(', it can’t end a valid substring. If s[i] is ')', there are two ways to close something: either it directly closes '(' at i-1 → "()", or it closes a '(' that sits just before the longest valid block ending at i-1. This captures nesting and concatenation by reusing previously computed lengths.
        - Approach: Initialize dp = [0]*n, max_len = 0. For i from 1..n-1:
            1. If s[i] == ')':
                - Case 1: if s[i-1] == '(' → dp[i] = (dp[i-2] if i>=2 else 0) + 2.
                - Case 2: else let prev = dp[i-1]. If i-prev-1 >= 0 and s[i-prev-1] == '(', then dp[i] = prev + 2 + (dp[i-prev-2] if i-prev-2 >= 0 else 0) (attach to earlier block). Update max_len = max(max_len, dp[i]). Return max_len.
        - Time: O(n). Space: O(n).
            - Time Complexity: O(n) We iterate through the string once.
            - Space Complexity: O(n) We use a DP array of size n.
    - 60c. Method 3: (Optimal) Two-pass counter approach (also known as the left-right scan method)
        - “I do two counter sweeps. Left→right: count '(' and ')'; when counts match, record length; if ')' ever exceeds '(', reset. Right→left: same idea but roles flipped to catch left-heavy tails. The best length from either pass is the answer. This runs in O(n) time and O(1) space.”
        - Intuition: Balanced parentheses require equal counts of '(' and ')' and never more ')' than '(' in a valid prefix. A single left→right pass misses cases that are “left-heavy” near the end, so we do two passes: left→right to catch segments where ')' doesn’t overrun, and right→left to catch segments where '(' doesn’t overrun.
        - Approach: Scan left→right with counters left, right:
            1. Increment left on '(', right on ')'.
            2. If left == right, update max_len = max(max_len, 2*right).
            3. If right > left, reset both to 0 (invalid prefix). Then scan right→left symmetrically:
            4. Increment right on ')', left on '('.
            5. If left == right, update max_len = max(max_len, 2*left).
            6. If left > right, reset. Return max_len. 
        - Time: O(n). Space: O(1).
            - Time Complexity: O(n) Two linear scans of the string.
            - Space Complexity: O(1) Only counters are used, no extra space proportional to input size.

61. Decode Ways 
    - 61a. Method 1: numDecodingsDP(self, s: str) -> int: Dynamic Programming
        - “I count ways to decode prefixes. At position i, if the last char is non-zero, I can extend all decodings of s[:i-1]. If the last two chars form 10..26, I can also extend all decodings of s[:i-2]. Summing those gives dp[i]. Start with dp[0]=1, handle leading zero, and iterate once. Answer is dp[n].”
        - Intuition: Think of decoding as ways to partition the string into valid codes: a single digit '1'..'9' or a two-digit '10'..'26'. The number of ways to decode up to position i depends on whether the last one or two digits form a valid letter. This creates a natural recurrence: choices at the end build on counts from earlier positions.
        - Approach: Use DP where dp[i] = ways to decode the prefix s[:i]. Initialize dp[0]=1 (empty string) and dp[1]=1 if the first char isn’t '0'. For each i from 2..n:
            1. If s[i-1] is '1'..'9', add dp[i-1] (take last one digit).
            2. If s[i-2:i] is '10'..'26', add dp[i-2] (take last two digits). Return dp[n]. 
        - Time: O(n). Space: O(n) (can be O(1) with two rolling variables).
            - Time Complexity: O(n) — one pass through the string.
            - Space Complexity: O(n) — for the dp array.
            - Can be optimized to  O(1) using two variables instead of an array.
    - 61b. Method 2: numDecodingsRecursiveDP(self, s: str) -> int: Recursive Dynamic Programming
        - “I iterate backward. At each position i, if it’s '0', there are 0 ways. Otherwise, I can take the single digit (add dp[i+1]), and if the next two digits form 10..26, also take the pair (add dp[i+2]). I seed dp[len(s)] = 1 for the empty tail and finally return dp[0]. This counts all valid partitions.”
        - Intuition: Decoding ways depend only on the tail you choose next. From index i, you can take one digit (if s[i] != '0') or two digits (if 10..26), then the problem reduces to the suffix starting at i+1 or i+2. So the total ways at i is the sum of ways from those next positions—classic overlapping subproblems → use DP.
        - Approach: Build a memo dp from right to left with base dp[len(s)] = 1 (empty suffix). For each i:
            - If s[i] == '0': dp[i] = 0 (no code starts with zero).
            - Else set dp[i] = dp[i+1] (use one digit).
            - If the two-digit number s[i:i+2] is valid ('10'..'26'), add dp[i+2]. Return dp[0].
        - Complexity: O(n) time, O(n) space (can be reduced to O(1) with two rolling vars).
            - Time Complexity: O(n) — each index is processed once.
            - Space Complexity: O(n) — dictionary dp stores results for each index.

## *** IMPORTANT*** 
62. maxProfit(self, prices: List[int]) -> int: Best Time to Buy and Sell Stock
    - “I sweep once, tracking the lowest price so far and the best profit if I sold today. Each step: update the low, compute price - min_price, and keep the max. That yields the optimal single-transaction profit in linear time with constant space.”
    - Intuition: You want the best single buy–sell profit. As you scan prices left→right, keep track of the cheapest price seen so far. At each day, the best profit if you sell today is price - min_price. Update the max profit with that, and keep lowering min_price whenever you see a new low. One pass gives the answer.
    - Approach: Initialize min_price = prices[0], max_profit = 0. For each price:
        If price < min_price, set min_price = price (better buy).
        Else update max_profit = max(max_profit, price - min_price) (sell today).
        Return max_profit.
    - Complexity: O(n) time, O(1) space.
        - Time Complexity: O(n) — single pass through the array.
        - Space Complexity: O(1) — only two variables used.

63. Word Break
    - 63a. Method 1: wordBreakForward(self, s: str, wordDict: List[str]) -> bool: Dynamic Programming    
        - “I run DP on prefixes. dp[i] means s[:i] is splittable. For each end i, I try cuts j<i:
        if we already know s[:j] is valid and s[j:i] is in the dictionary, mark dp[i]=True and move on. After filling the table, dp[n] tells if the whole string can be segmented. Runs in O(n²) time, O(n) space.”
        - Intuition: We’re asking: can the prefix s[0:i] be split into dictionary words for every i? If some earlier cut j is valid and s[j:i] is a word, then s[0:i] is valid too. That “current depends on earlier” pattern is perfect for DP over prefixes.
        - Approach: Use dp[i] = True iff s[:i] can be segmented. Seed dp[0]=True (empty string). For each i from 1..n, scan j from 0..i-1: if dp[j] is true and s[j:i] is in word_set, set dp[i]=True and break (no need to check more j). Return dp[n].
        - Complexity: Time O(n²) substring checks with O(1) set lookups; Space O(n).
            - Time Complexity: O(n^2) — nested loop over i and j, and substring checks.
            - Space Complexity: O(n+m) — dp array of size n+1, and word_set of size m.
    - 63b. Method 2: wordBreakBackward(self, s: str, wordDict: List[str]) -> bool:  Dynamic Programming
        - “I do backward DP on suffixes. Starting from the end, at each index i I try every dictionary word w. If w matches at i and the rest dp[i+len(w)] is True, then dp[i]=True. I break early when I find a match. After filling, dp[0] tells if the whole string is segmentable. Runs in O(n·k·L) time (k words, max length L), O(n) space.”
        - Intuition: Ask from each index i: “Can the suffix s[i:] be segmented?” If some word w in the dictionary matches s[i:i+len(w)] and the remainder s[i+len(w):] is segmentable, then s[i:] is segmentable. This flips the usual prefix DP to a suffix DP, letting us reuse answers we’ve already computed for later positions.
        - Approach: Create a DP array dp where dp[i] is True iff s[i:] can be split; seed dp[n]=True (empty suffix). Iterate i from n-1 down to 0. For each word w in wordDict, if s[i:i+len(w)] == w, set dp[i] = dp[i+len(w)]. Break early once dp[i] becomes True. Finally return dp[0].
        - Complexity: Runs in O(n·k·L) time (k words, max length L), O(n) space.
            - Time Complexity: Worst-case:  O(n⋅m⋅k)
                Where:
                    n = length of s
                    m = number of words in wordDict
                    k = average length of words
            - Space Complexity: O(n) — for the dp array
    - 63c. Method 3: Trie-based optimization 
        - “I insert all dictionary words into a Trie and run a memoized DFS over s. Starting at index i, I follow Trie edges along s; when I land on a word end, I try to recurse from the next index. I cache each i to prevent repeated work. If any path reaches the end, segmentation is possible.”
        - Intuition: We want to see if s can be split into dictionary words. Instead of checking every substring against a hash set, a Trie lets us walk character-by-character and quickly stop when no word can start here. Use DFS from each start index and memoize results so each position in s is solved once.
        - Approach: Build a Trie from wordDict (is_word marks word ends). Define dfs(i) = can s[i:] be segmented? From i, walk the Trie along s[i:]; every time you hit a Trie node with is_word=True, recursively try dfs(next_index). Cache dfs(i) in memo to avoid recomputation. If any path reaches the end of s, return True; else False.
        - Building Trie: O(Σ|w|). DFS: O(n·L) states/steps on average, where n is len(s) and L is max word length (each index explores at most L chars), thanks to memoization. Space: O(Σ|w| + n) for Trie + memo.
            - Time Complexity: Worst-case: O(n^2 ) But often faster due to early pruning via Trie.
            - Space Complexity: O(n+m⋅k)
                n for memoization
                m = number of words
                k = average word length (Trie size)

64.  sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int: Range Sum Query 2D - Immutable
    - “I preprocess a padded 2D prefix sum so each cell holds the sum from the origin to that cell. Then any rectangular sum is computed via inclusion–exclusion of four prefix corners in O(1). Building the prefix is O(m·n); each sumRegion query is O(1).”
    - Intuition: Precompute a 2D prefix-sum so any rectangle sum can be answered in O(1). With a padded prefix grid, each cell prefix[i+1][j+1] stores the sum of the submatrix from (0,0) to (i,j). Then any query rectangle is just inclusion–exclusion of four prefix values.
    - Approach: 
        1. Build prefix of size (m+1)×(n+1) with a zero top row/left col:
            prefix[i+1][j+1] = matrix[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]
        2. To get sum of (row1,col1)..(row2,col2):
            prefix[row2+1][col2+1] - prefix[row1][col2+1] - prefix[row2+1][col1] + prefix[row1][col1]
    - Complexity: Preprocessing O(m·n) time, O(m·n) space; each query O(1).
        - Initialization (__init__):
                Time:  O(m⋅n)
                Space: O(m⋅n)
        - Query (sumRegion):
                Time: O(1)
                Space: O(1)

65. checkSubarraySum(self, nums: List[int], k: int) -> bool: Continuous Subarray Sum  using an  efficient prefix sum with modulo and hashmap approach.
    - “I compute running sums and their remainder mod k. If a remainder repeats, the subarray between those positions sums to a multiple of k. I keep the first index of each remainder so the subarray is as long as possible, and I ensure its length ≥ 2. A seed {0:-1} handles subarrays starting at the beginning. This is O(n) time and O(min(n, k)) space.”
    - Intuition: If two prefix sums have the same remainder mod k, their difference (i.e., the sum of the subarray between them) is a multiple of k. So as we scan, we track the earliest index where each remainder first appeared. When we see the same remainder again at index i, the subarray from the first index+1 to i sums to a multiple of k. We also need length ≥ 2.
    - Approach: Keep cumulative_sum, and a map mod_map from remainder → earliest index, seeded with {0: -1} to allow subarrays starting at 0. For each i:
        - Add nums[i] to cumulative_sum. If k != 0, set cumulative_sum %= k.
        - If this remainder was seen before at index j, check if i - j > 1; if yes, return True.
        - Otherwise, store the remainder’s first occurrence: mod_map[rem] = i.
        If the loop ends, return False.
    - Complexity: O(n) time and O(min(n, k)) space.”
        - Time Complexity: O(n) — single pass through the array.
        - Space Complexity: O(k) — hashmap stores remainders (bounded by k).

66. class LRUCache: LRU Cache
    - “I pair a hash map with a doubly linked list. The map finds nodes in O(1); the list orders them by recency. On every get/put, I remove the node from its spot and append it near the tail (most recent). When capacity is hit, I evict the node right after the head (least recent). All operations are O(1) time, O(capacity) space.”
    - Intuition: LRU needs O(1) get/put and a way to evict the least-recently used item. A hash map gives O(1) key→node lookup; a doubly linked list maintains recency order: most-recent at the tail, least-recent at the head. Every access promotes the node to “most recent”; when full, evict the node at the head.
    - Approach: Store cache: key → Node. The DLL has dummy head/tail to simplify inserts/removals.
        1. get(k): if present, unlink node and move it to tail; return value; else -1.
        2. put(k,v): if present, update value and move to tail. Else, if at capacity, remove head.next (LRU) and delete from map; then create a new node, add to map, and append to tail.
        3. Helper methods _remove(node) and _add_to_tail(node) do O(1) list ops.
    - All operations are O(1) time, O(capacity) space.
        - get	O(1)	Hashmap lookup + constant-time list operations
        - put	O(1)	Hashmap insert/update + constant-time list operations
        - Space	O(capacity)	Stores up to capacity nodes and hashmap entries

67. class BSTIterator: Binary Search Tree Iterator
    - “I simulate an in-order traversal with a stack. On init, I push the leftmost chain. Each next() pops the current smallest and, if it has a right child, I push that child’s left chain. hasNext() checks if the stack isn’t empty. This gives ascending outputs with O(1) amortized time per call and O(h) space (h = tree height).”
    - Intuition: An in-order traversal of a BST yields values in ascending order. To iterate lazily (O(1) amortized per call), keep a stack of the path to the next node. Initially push the leftmost path (smallest). Each next() pops one node (the current smallest) and, if it has a right child, pushes that right child’s leftmost path—which makes the following smallest ready.
    - Approach: 
        1. Constructor: call _push_left(root) to push root, root.left, … until None.
        2. next(): pop top node. If node.right exists, _push_left(node.right) to preload the next run of smallers. Return node.val.
        3. hasNext(): stack non-empty? then there’s a next.
        4. Helpers do all work in O(height) per expansion but O(1) amortized per next().
    - O(1) amortized time per call and O(h) space (h = tree height).
        - get	O(1)	Hashmap lookup + constant-time list operations
        - put	O(1)	Hashmap insert/update + constant-time list operations
        - Space	O(capacity)	Stores up to capacity nodes and hashmap entries

68. class WordDictionary: Add and Search Word - Data structure design
    - “I store words in a Trie. To search, I walk the Trie; a normal character follows one edge, while . tries all child edges at that level via recursion. If any path reaches a node marked is_end exactly at the word’s length, it’s a match. Adds are linear in word length; searches are linear on average, branching only on ..”
    - Intuition: We need a dictionary that supports normal word lookups and wildcard . (matches any single letter). A Trie is perfect: it stores words character-by-character. For wildcards, instead of a single path, we can branch to all children at that position. Recursing down the Trie naturally handles both exact chars and ..
    - Approach: 
        1. addWord: insert chars into the Trie, creating nodes as needed; mark is_end=True at the last node.
        2. search(word): recursive DFS:
            If we reach the end of the word, return node.is_end.
            If word[i] is a normal char, follow that child (if missing → False).
            If it’s ., try all children; if any recursive call returns True, succeed.
            This explores only necessary branches.
    - Complexity:
        - addWord(word)
            Time: O(n), where n is the length of the word
            Space: O(n) for new nodes
        - search(word)
            Time: Worst-case: O(n × 26^d), where:
                n = length of the word
                d = number of . wildcards
                In practice: much faster due to early pruning, worst-case with many . can branch to O(Σ^d) where d is number of wildcards (Σ = alphabet size).
            Space: O(h) for recursion stack (h = length of word)

## *** IMPORTANT*** 
69. class Codec: Serialize and Deserialize Binary Tree
    - “I run a preorder DFS, writing each value and "null" for absent children. That string is a complete blueprint. To rebuild, I read tokens in order: on a value, create a node and recursively build its left and right; on "null", return None. Since both processes use the same traversal, structure and values line up perfectly.”
    - Intuition: Serialize the tree with a preorder DFS (root, left, right), writing "null" for missing children. This uniquely captures structure and values. To deserialize, read the same sequence back in preorder: when you see a value, make a node; when you see "null", return None. Because encode/decode traverse in the same order, the tree reconstructs exactly.
    - Approach: 
        1. Serialize: Do a recursive DFS. Append str(node.val) for real nodes; append "null" for None. Join with commas.
        2. Deserialize: Split by commas, turn into an iterator, and recursively rebuild:
            - Read next token; if "null", return None.
            - Else create TreeNode(int(val)), then set left = dfs(), right = dfs(). Return the root from the top call.
    - Complexity: Both serialize and deserialize visit each node once → O(n) time, O(n) space for the output/input string; recursion uses O(h) call stack (h = tree height).
        - Serialization
            Time Complexity: O(n) Each node is visited once.
            Space Complexity: O(n) Output list + recursion stack.
        - Deserialization
            Time Complexity: O(n) Each value is processed once.
            Space Complexity: O(n) Recursion stack + tree nodes.

70. addOperators(self, num: str, target: int) -> List[str]: Expression Add Operators
    - “I do a DFS that splits the string into numbers and inserts +/-/*. I carry a running value and the last operand so multiplication can retroactively apply before addition/subtraction (value = value - last + last*curr). I skip numbers with leading zeros. Whenever I reach the end and the value equals target, I add the expression.”
    - Intuition: We need to place +, -, * (or nothing for the first chunk) between digits so the expression evaluates to target. This is a classic backtracking over all ways to split num into numbers and interleave operators. The trick is handling * without re-parsing the whole expression: keep the running value and the last operand so we can “fix up” precedence (e.g., … + last * curr).
    - Approach: DFS over num[index:]. At each step, choose a substring curr_str = num[index:i+1] (skip leading-zero numbers).
        - If it’s the first number, start the path with it: (path=curr_str, value=curr, last=curr).
        - Otherwise branch three ways:
            +: value + curr, last = +curr
            -: value - curr, last = -curr
            *: undo the last add/sub: value - last + last*curr, and set last = last*curr. When index == len(num), if value == target, record path.
    - Complexity: In worst case ~O(3^{n-1}) states (three operators between each of n digits), with O(n) work per state building strings → exponential overall; O(n) recursion depth.
        - Time Complexity: Worst case: O(4^n) 
            Each digit can be followed by 3 operators or be part of a longer number.
            Exponential due to recursive branching.
        - Space Complexity: O(n) for recursion stack and path string.

71. findAnagrams(self, s: str, p: str) -> List[int]: Find All Anagrams in a String
    - “I keep a 26-length frequency array for p and another for the current window of size len(p) in s. As I expand right, I increment that char; if the window gets too big, I decrement the left char and move left. Whenever window size equals m and the two arrays match, I push left to the result. Runs in O(n) time, O(1) space.”
    - Intuition: An anagram of p is just a reordering of its letters. So as we slide a window of length len(p) over s, we only need to check if the window’s letter frequencies match p’s frequencies. Keep counts for a..z and update them incrementally as the window moves, instead of recomputing from scratch.
    - Approach: Precompute target_freq[26] for p. Sweep s with a sliding window [left..right]:
        1. Add s[right] to window_freq.
        2. If window size exceeds m, remove s[left] and increment left.
        3. When window size equals m, if window_freq == target_freq, record left.
            his uses two fixed-size arrays (26) and O(1) updates per step.
    - Complexity: Let: n=len(s), mad=len(p)
        - Time Complexity: O(n) — each character is processed once in the sliding window.
        - Space Complexity: O(1) — fixed-size arrays of 26 elements (constant space).

72. checkInclusion(self, s1: str, s2: str) -> bool: Permutation in String
    - “I keep two 26-length counters: one for s1, one for a moving window in s2 of the same length. I initialize on the first window, then slide: increment the entering char, decrement the leaving char. If the counters ever match, that window is a permutation of s1 → return True. Otherwise, return False. Linear time, constant space.”
    - Intuition: We’re checking if any substring of s2 is a permutation of s1. Two strings are permutations if their letter counts match. So keep a sliding window of length len(s1) over s2 and compare frequency arrays (size 26). Update counts in O(1) as the window moves; if a window’s counts equal s1’s counts, we found a permutation.
    - Approach: 
        1. Build s1_freq[26] and the first window’s window_freq[26] from s2[0:len_s1].
        2. If they match, return True.
        3. Slide the window from left to right:
            Add the new right char, remove the old left char from window_freq.
            After each slide, if window_freq == s1_freq, return True.
        4. If no match by the end, return False.
    - Complexity: Time O(n) over s2 with O(1) work per step; Space O(1) (two fixed 26-length arrays). Let: n=len(s2), m=len(s1)
        - Time Complexity: O(n) — each character is processed once in the sliding window.
        - Space Complexity: O(1) — fixed-size arrays of 26 elements (constant space).

73. intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]: Interval List Intersections
    - “I sweep both sorted lists with two pointers. For each pair, if they overlap, I record [max start, min end]. Then I advance the interval that ends first, since it can’t intersect future intervals. One linear pass yields all intersections.”
    - Intuition: Two sorted interval lists overlap only around the intervals that are currently “active.” If the current pair overlaps, their intersection is simply [max(starts), min(ends)]. After processing a pair, advance the pointer of the interval that finishes first—it can’t intersect anything later.
    - Approach: Use two pointers i, j over firstList and secondList. While both in-bounds:
        1. Let [s1,e1]=first[i], [s2,e2]=second[j].
        2. If they overlap (s1 ≤ e2 and s2 ≤ e1), append [max(s1,s2), min(e1,e2)].
        3. Move the pointer whose end is smaller: i += 1 if e1 < e2, else j += 1.Return all collected intersections.
    - Complexity: O(m + n) time, O(1) extra space (output aside). Let: n=len(firstList), m=len(secondList)
        - Time Complexity: O(n+m) — each interval is processed once.
        - Space Complexity: O(k) — where k is the number of intersections (output size).
