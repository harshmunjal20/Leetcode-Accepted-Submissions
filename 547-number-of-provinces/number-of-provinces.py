class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinceCount = 0

        def DFS(rowIdx : int) -> None:
            if visited[rowIdx]:
                return
            
            visited[rowIdx] = True

            for colIdx in range(n):
                if isConnected[rowIdx][colIdx] and not visited[colIdx]:
                    DFS(colIdx)

        for rowIdx in range(n):
            if not visited[rowIdx]:
                provinceCount += 1
                DFS(rowIdx)
            
        return provinceCount