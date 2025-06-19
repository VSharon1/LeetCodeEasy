from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1

        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        while low < high:
            mid = low + (high - low) // 2
            guess = letters[mid]

            if guess > target:
                high = mid
            else:
                low = mid + 1

        return letters[low]
