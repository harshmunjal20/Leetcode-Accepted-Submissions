import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        serversQue = []
        currExecutionQue = []
        runningTime = 0
        ans = [0] * len(tasks)

        for idx, serverWeight in enumerate(servers):
            heapq.heappush(serversQue, (serverWeight, idx))

        for idx, task in enumerate(tasks):
            while currExecutionQue and currExecutionQue[0][0] <= runningTime:
                currTime, weight, serverIdx = heapq.heappop(currExecutionQue)
                heapq.heappush(serversQue, (weight, serverIdx))

            weight, serverIdx = 0, 0

            if serversQue:
                weight, serverIdx = heapq.heappop(serversQue)
            else:
                runningTime, weight, serverIdx = heapq.heappop(currExecutionQue)
            
            heapq.heappush(currExecutionQue, (runningTime + task, weight, serverIdx))
            ans[idx] = serverIdx
            runningTime = max(runningTime, idx + 1)

        return ans