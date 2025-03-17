from typing import List


# # Bruteforce method, but Runtime Error, because ValueError: Exceeds the limit
# # (4300 digits) for integer string conversion.
# class Solution:
#     def addToArrayForm(self, num: List[int], k: int) -> List[int]:
#         num_string = ""
#         result = 0
#         result_list = []

#         for n in num:
#             num_string += str(n)

#         result = int(num_string) + k

#         for n in str(result):
#             result_list.append(int(n))

#         return result_list


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num.reverse()
        num_i = 0

        while k:
            k_last_digit = k % 10

            if num_i < len(num):
                num[num_i] += k_last_digit
            else:
                num.append(k_last_digit)

            carry_value = num[num_i] // 10

            num[num_i] = num[num_i] % 10

            k = k // 10

            k += carry_value

            num_i += 1

        num.reverse()
        return num
