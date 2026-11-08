class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def getPerimeter(rowIdx : int, colIdx : int) -> None:
            if rowIdx < 0 or colIdx < 0 or rowIdx >= rows or colIdx >= cols or grid[rowIdx][colIdx] == 0:
                return 1
            
            if visited[rowIdx][colIdx]:
                return 0

            visited[rowIdx][colIdx] = True
            perimeter = 0

            for (x, y) in directions:
                x_coordinate = x + rowIdx
                y_coordinate = y + colIdx
                perimeter += getPerimeter(x_coordinate, y_coordinate)
                
            return perimeter

        for rowIdx in range(rows):
            for colIdx in range(cols):
                if grid[rowIdx][colIdx] == 1:
                    return getPerimeter(rowIdx, colIdx)

        return -1