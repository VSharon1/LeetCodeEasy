from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_i = 0
        word2_i = 0
        word1_char_i = 0
        word2_char_i = 0

        while word1_i < len(word1) and word2_i < len(word2):
            if word1[word1_i][word1_char_i] != word2[word2_i][word2_char_i]:
                return False

            word1_char_i += 1
            word2_char_i += 1

            if word1_char_i == len(word1[word1_i]):
                word1_i += 1
                word1_char_i = 0

            if word2_char_i == len(word2[word2_i]):
                word2_i += 1
                word2_char_i = 0

        if word1_i != len(word1) or word2_i != len(word2):
            return False

        return True
