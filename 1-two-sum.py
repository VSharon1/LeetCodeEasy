from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i in range(len(nums)):
            target_diff = target - nums[i]

            if target_diff in nums_dict:
                return [nums_dict[target_diff], i]
            else:
                nums_dict[nums[i]] = i
