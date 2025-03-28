class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_i = 0
        w2_i = 0
        result = []

        while w1_i < len(word1) and w2_i < len(word2):
            result.append(word1[w1_i])
            result.append(word2[w2_i])

            w1_i += 1
            w2_i += 1

        result.append(word1[w1_i:])
        result.append(word2[w2_i:])

        merged_string = "".join(result)

        return merged_string
