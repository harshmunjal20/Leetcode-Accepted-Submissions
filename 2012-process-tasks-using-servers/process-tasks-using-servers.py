import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        serversQueue = []
        currExecutionQueue = []
        ans = [0] * len(tasks)
        runningTime = 0

        for idx, weight in enumerate(servers):
            heapq.heappush(serversQueue, (weight, idx))
        
        for idx, task in enumerate(tasks):
            currTime , weight, serverIdx = 0, 0, 0
            while currExecutionQueue and currExecutionQueue[0][0] <= runningTime:
                currTime, weight, serverIdx = heapq.heappop(currExecutionQueue) 
                heapq.heappush(serversQueue, (weight, serverIdx))

            if serversQueue:
                weight, serverIdx = heapq.heappop(serversQueue)
            else:
                runningTime = currExecutionQueue[0][0]
                currTime, weight, serverIdx = heapq.heappop(currExecutionQueue)

            heapq.heappush(currExecutionQueue, (runningTime + task, weight, serverIdx))
            ans[idx] = serverIdx
            runningTime = max(runningTime, idx + 1)

        return ans