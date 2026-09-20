class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        sLen = len(s)

        for index in range(sLen):
            ans += (index + 1) * (123 - ord(s[index]))

        return ans