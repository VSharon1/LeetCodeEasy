from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        g_i = 0
        s_i = 0

        while g_i < len(g):

            while s_i < len(s) and g[g_i] > s[s_i]:
                s_i += 1

            if s_i < len(s):
                g_i += 1
                s_i += 1
            else:
                break

        return g_i
