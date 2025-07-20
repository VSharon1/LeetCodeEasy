class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict_count = {}
        t_dict_count = {}

        for i in range(len(s)):
            s_dict_count[s[i]] = 1 + s_dict_count.get(s[i], 0)
            t_dict_count[t[i]] = 1 + t_dict_count.get(t[i], 0)

        for i in s_dict_count:
            if s_dict_count[i] != t_dict_count.get(i, 0):
                return False

        return True
