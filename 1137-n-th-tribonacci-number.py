class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci_nums = [0, 1, 1]

        if n < 3:
            return tribonacci_nums[n]

        for i in range(3, n + 1):
            sum_tribonacci_nums = sum(tribonacci_nums)

            tribonacci_nums[0] = tribonacci_nums[1]
            tribonacci_nums[1] = tribonacci_nums[2]
            tribonacci_nums[2] = sum_tribonacci_nums

        return tribonacci_nums[2]
