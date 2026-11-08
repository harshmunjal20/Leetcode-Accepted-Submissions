class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        rowsServerCount = [0] * rows
        colsServerCount = [0] * cols
        connectedServers = 0

        for rowIdx in range(rows):
            currRowServerCount = 0

            for colIdx in range(cols):
                if grid[rowIdx][colIdx] == 1:
                    colsServerCount[colIdx] += 1
                    currRowServerCount += 1

            rowsServerCount[rowIdx] = currRowServerCount

        for rowIdx in range(rows):
            for colIdx in range(cols):
                if grid[rowIdx][colIdx] == 1 and (rowsServerCount[rowIdx] > 1 or colsServerCount[colIdx] > 1):
                    connectedServers += 1

        return connectedServers