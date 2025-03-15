class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_i = 0
        word2_i = 0
        result = []

        while word1_i < len(word1) and word2_i < len(word2):
            result.append(word1[word1_i])
            result.append(word2[word2_i])

            word1_i += 1
            word2_i += 1

        result.append(word1[word1_i:])
        result.append(word2[word1_i:])

        merged_string = "".join(result)

        return merged_string
