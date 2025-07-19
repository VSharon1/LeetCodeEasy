from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Hash Set Method:
        nums_set = set(nums)

        for i in range(len(nums) + 1):
            if i not in nums_set:
                return i

        # Hash Table Method:
        # nums_dict = {num: num for num in nums}

        # for i in range(len(nums) + 1):
        #     if i not in nums_dict:
        #         return i

        # Binary Search Method:
        # low = 0
        # high = len(nums)

        # nums.sort()

        # while low < high:
        #     mid = low + (high - low) // 2

        #     if nums[mid] != mid:
        #         high = mid
        #     else:
        #         low = mid + 1

        # return low
