from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_distinct = {}

        for i in range(len(nums)):
            if nums[i] in nums_distinct:
                return True
            else:
                nums_distinct[nums[i]] = nums[i]

        return False
