class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key= lambda log : log[1])
        ids = sorted(range(len(queries)), key =lambda i : queries[i])
        count = [0] * (n + 1)
        ans = [0] * (len(queries))
        left = right = active = 0

        for idx in ids:
            currQueryEnd = queries[idx]
            currQueryStart = currQueryEnd - x

            while right < len(logs) and logs[right][1] <= currQueryEnd:
                currId = logs[right][0]
                if count[currId] == 0:
                    active += 1
                count[currId] += 1
                right += 1
            
            while left < len(logs) and logs[left][1] < currQueryStart:
                currId = logs[left][0]
                count[currId] -= 1
                if count[currId] == 0:
                    active -= 1
                left += 1
            
            ans[idx] = n - active

        return ans