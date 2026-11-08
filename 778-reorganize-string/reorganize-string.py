from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        hashMap = Counter(s)
        maxHeap = []
        ans = ['a'] * len(s)
        currIdx = 0

        for key, value in hashMap.items():
            heapq.heappush(maxHeap, (-value, ord(key)))

        if -maxHeap[0][0] > ((len(s) + 1) // 2):
            return ""

        while maxHeap:
            value, key = heapq.heappop(maxHeap)

            while value < 0:
                if currIdx >= len(s):
                    currIdx = 1
                ans[currIdx] = chr(key)
                value += 1
                currIdx += 2

        return "".join(ans)