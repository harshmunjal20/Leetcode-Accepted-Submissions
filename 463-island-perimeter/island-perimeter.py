class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def getPerimeter(rowIdx : int, colIdx : int) -> None:
            visited[rowIdx][colIdx] = True
            perimeter = 0

            for (x, y) in directions:
                x_coordinate = x + rowIdx
                y_coordinate = y + colIdx
                if x_coordinate < 0 or y_coordinate < 0 or x_coordinate >= rows or y_coordinate >= cols or grid[x_coordinate][y_coordinate] == 0:
                    perimeter += 1
                    continue

                if visited[x_coordinate][y_coordinate]:
                    continue

                perimeter += getPerimeter(x_coordinate, y_coordinate)
                
            return perimeter

        for rowIdx in range(rows):
            for colIdx in range(cols):
                if grid[rowIdx][colIdx] == 1:
                    return getPerimeter(rowIdx, colIdx)

        return -1