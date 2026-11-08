from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        hashMap = Counter(s)
        sortedMap = dict(sorted(hashMap.items(), key = lambda item : -item[1]))
        ans = ['a'] * len(s)
        currIdx = 0
        maxFreq = next(iter(sortedMap.values()))

        if maxFreq > (len(s) + 1) // 2:
            return ""

        for key, value in sortedMap.items():
            while value > 0:
                if currIdx >= len(s):
                    currIdx = 1
                
                ans[currIdx] = key
                currIdx += 2
                value -= 1

        return "".join(ans)