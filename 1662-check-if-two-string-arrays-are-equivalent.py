from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1_i = 0
        w2_i = 0
        w1_char_i = 0
        w2_char_i = 0

        while w1_i < len(word1) and w2_i < len(word2):
            if word1[w1_i][w1_char_i] != word2[w2_i][w2_char_i]:
                return False

            w1_char_i += 1
            w2_char_i += 1

            if w1_char_i == len(word1[w1_i]):
                w1_i += 1
                w1_char_i = 0

            if w2_char_i == len(word2[w2_i]):
                w2_i += 1
                w2_char_i = 0

        if w1_i != len(word1) or w2_i != len(word2):
            return False

        return True
