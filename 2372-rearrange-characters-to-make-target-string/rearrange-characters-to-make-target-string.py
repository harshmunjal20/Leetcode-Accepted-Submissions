from collections import Counter

class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        sFreqMap = Counter(s)
        targetFreqMap = Counter(target)
        ans = 1e10

        for tChar, value in targetFreqMap.items():
            ans = min(ans, sFreqMap[tChar] // value)

        return ans if ans != 1e10 else 0
            

        