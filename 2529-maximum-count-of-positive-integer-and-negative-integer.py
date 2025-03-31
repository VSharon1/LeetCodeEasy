from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p_nums = 0
        n_nums = 0

        for n in nums:
            if n < 0:
                n_nums += 1
            elif n > 0:
                p_nums += 1

        return max(p_nums, n_nums)
