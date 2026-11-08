from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ['a'] * len(s)
        hashMap = Counter(s)
        currIdx = 0
        sortedMap = dict(sorted(hashMap.items(), key = lambda item : -item[1]))
        maxFreq = max(sortedMap.values())

        if maxFreq > ((len(s) + 1) // 2):
            return ""
            
        for key, value in sortedMap.items():
            while value > 0:
                if currIdx >= len(s):
                    currIdx = 1
                ans[currIdx] = key
                value -= 1
                currIdx += 2

        return "".join(ans)