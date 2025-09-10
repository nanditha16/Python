# Convert a non-negative integer num to its English words representation.

# Constraints:
# 0 <= num <= 2^31 - 1

# Time Complexity: O(log 10​ (n)) — we process each group of 3 digits.
# Space Complexity: O(1) — fixed-size arrays and recursion depth.

# #Explanation:
# To convert a non-negative integer num to its English words representation, 
# we can break the number into chunks of three digits (thousands, millions, billions), 
# and convert each chunk using a helper function.
    # We define arrays for:
        # Numbers below 20
        # Tens (20, 30, ..., 90)
        # Thousands (to handle chunks like thousand, million, billion)
    # function converts numbers less than 1000 to words.
    # We process the number in chunks of 3 digits from right to left.
    # We build the result string by prepending each chunk's word representation.

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # Define mappings
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                    "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n: int) -> str:
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        for i in range(len(thousands)):
            if num % 1000 != 0:
                res = helper(num % 1000) + thousands[i] + " " + res
            num //= 1000

        return res.strip()


sol = Solution()

print(sol.numberToWords(123))        # "One Hundred Twenty Three"
print(sol.numberToWords(12345))      # "Twelve Thousand Three Hundred Forty Five"
print(sol.numberToWords(123000))     # "One Hundred Twenty Three Thousand"
print(sol.numberToWords(1000010))    # "One Million Ten"
print(sol.numberToWords(0))          # "Zero"
