import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        serversQue = []
        currExecutionQue = []
        ans = [0] * len(tasks)
        runningTime = 0

        for idx, serverWeight in enumerate(servers):
            heapq.heappush(serversQue, (serverWeight, idx))

        for idx, timeExecution in enumerate(tasks):
            while currExecutionQue and currExecutionQue[0][0] <= runningTime:
                currTime, serverWeight, serverIdx = heapq.heappop(currExecutionQue)
                heapq.heappush(serversQue, (serverWeight, serverIdx))
            
            serverWeight, serverIdx = 0, 0

            if serversQue:
                serverWeight, serverIdx = heapq.heappop(serversQue)
            else:
                runningTime, serverWeight, serverIdx = heapq.heappop(currExecutionQue)
            
            heapq.heappush(currExecutionQue, (runningTime + timeExecution, serverWeight, serverIdx))
            ans[idx] = serverIdx
            runningTime = max(runningTime, idx + 1)

        return ans