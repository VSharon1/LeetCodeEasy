from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            left = 0
            right = len(word) - 1

            while word[left] == word[right]:
                if left >= right:
                    return word

                left += 1
                right -= 1

        return ""
