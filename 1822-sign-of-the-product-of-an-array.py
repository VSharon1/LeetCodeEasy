from typing import List

# # Brutforce method, but it can overflow.
# class Solution:
#     def arraySign(self, nums: List[int]) -> int:
#         result = 1

#         for n in nums:
#             result *= n

#         if result >= 1:
#             return 1

#         if result == 0:
#             return 0

#         if result <= -1:
#             return -1


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative_nums = 0

        for n in nums:
            if n == 0:
                return 0

            negative_nums += 1 if n < 0 else 0

        return -1 if negative_nums % 2 else 1
