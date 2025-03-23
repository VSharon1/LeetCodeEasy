from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_seen = set(nums1)

        result = []

        for n in nums2:
            if n in num_seen:
                result.append(n)
                num_seen.remove(n)

        return result
