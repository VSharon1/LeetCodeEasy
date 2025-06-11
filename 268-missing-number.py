from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)

        nums.sort()

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] != mid:
                high = mid
            else:
                low = mid + 1
        return low
