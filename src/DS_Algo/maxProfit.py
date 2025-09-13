# You are given an array prices where prices[i] is the price of a given 
# stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one 
# stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

# Constraints:
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^4

# Example:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not 
# allowed because you must buy before you sell.

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Method 1: one-pass algorithm.
# Step-by-Step Explanation
# 1. Initialize:
#     min_price to infinity (we want to find the lowest price).
#     max_profit to 0.
# 2. Iterate through prices:
#     If current price is lower than min_price, update min_price.
#     Else, calculate profit (price - min_price) and update max_profit if it's higher.
# 3. Return max_profit:
#     This is the maximum profit achievable with one transaction.

# Edge Case Handling
#     If prices are in descending order (e.g., [7,6,4,3,1]) → returns 0
#     If prices are all the same → returns 0
#     If prices has only one element → returns 0 (no transaction possible)

# Time Complexity: O(n) — single pass through the array.
# Space Complexity: O(1) — only two variables used.

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # Update the lowest price seen so far
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit