class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for rowIdx in range(rows):
            for colIdx in range(cols):
                if grid[rowIdx][colIdx] == 1:
                    perimeter += 4

                    if rowIdx > 0 and grid[rowIdx - 1][colIdx] == 1:
                        perimeter -= 2
                    
                    if colIdx > 0 and grid[rowIdx][colIdx - 1] == 1:
                        perimeter -= 2
    
        return perimeter