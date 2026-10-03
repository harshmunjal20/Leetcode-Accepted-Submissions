class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinceCount = 0
        visited = [False] * (n + 1)

        def DFS(rowIdx : int) -> None:
            if visited[rowIdx + 1]:
                return

            visited[rowIdx + 1] = True

            for colIdx in range(n):
                if isConnected[rowIdx][colIdx] and not visited[colIdx + 1]:
                    DFS(colIdx)

        for rowIdx in range(n):
            for colIdx in range(n):
                if isConnected[rowIdx][colIdx] and not visited[rowIdx + 1]:
                    provinceCount += 1
                    DFS(rowIdx)
                    break

        return provinceCount