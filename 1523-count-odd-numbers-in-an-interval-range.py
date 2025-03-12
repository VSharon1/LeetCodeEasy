# Brutforce method, but time limit exceeded
# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#         result = 0

#         while low <= high:
#             if low % 2 != 0:
#                 result += 1
#             low +=1

#         return result


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1

        count = length // 2

        if length % 2 and low % 2:
            count += 1

        return count
