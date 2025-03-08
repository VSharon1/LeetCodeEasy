class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0 
        right = x
        result = 0

        while left <= right:
            middle = left + ((right - left) // 2)

            if middle**2 > x:
                right = middle - 1
            elif middle**2 < x:
                left = middle + 1
                result = middle
            else:
                return middle

        return result
