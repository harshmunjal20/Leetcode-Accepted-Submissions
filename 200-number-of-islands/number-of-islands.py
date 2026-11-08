class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def DFS(rowIdx : int, colIdx : int) -> None:
            if visited[rowIdx][colIdx]:
                return
            
            visited[rowIdx][colIdx] = True

            for (x, y) in directions:
                x_coordinate = x + rowIdx
                y_coordinate = y + colIdx

                if x_coordinate >= 0 and y_coordinate >= 0 and x_coordinate < rows and y_coordinate < cols and grid[x_coordinate][y_coordinate] == '1' and not visited[x_coordinate][y_coordinate]:
                    DFS(x_coordinate, y_coordinate)

        islandsCount = 0

        for rowIdx in range(rows):
            for colIdx in range(cols):
                if grid[rowIdx][colIdx] == '1' and not visited[rowIdx][colIdx]:
                    islandsCount += 1
                    DFS(rowIdx, colIdx)
        
        return islandsCount