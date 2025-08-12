from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        left = 0
        right = left + 1

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right = left + 1
            else:
                profit = max(profit, prices[right] - prices[left])
                right += 1

        return profit
