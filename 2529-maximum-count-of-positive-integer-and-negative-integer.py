from typing import List


# Easy Solution
# class Solution:
#     def maximumCount(self, nums: List[int]) -> int:
#         n_nums = 0
#         p_nums = 0

#         for n in nums:
#             if n < 0:
#                 n_nums += 1
#             elif n > 0:
#                 p_nums += 1

#         return max(p_nums, n_nums)


# Binary Search Solution
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n_nums = self.binary_search(nums, 0)
        p_nums = len(nums) - self.binary_search(nums, 1)

        return max(p_nums, n_nums)

    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        result = len(nums)

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
                result = middle

        return result
