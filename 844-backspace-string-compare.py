class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def buildString(string):
            result = []

            for char in string:
                if char != "#":
                    result.append(char)
                elif result:
                    result.pop()

            return "".join(result)

        return buildString(s) == buildString(t)
