class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        rowsServersCount = [0] * rows
        colsServersCount = [0] * cols
        connectedCount = 0

        for rowIdx in range(rows):
            currRowCount = 0
            for colIdx in range(cols):
                if grid[rowIdx][colIdx] == 1:
                    colsServersCount[colIdx] += 1
                    currRowCount += 1
            
            rowsServersCount[rowIdx] = currRowCount
        
        for rowIdx in range(rows):
            for colIdx in range(cols):
                if grid[rowIdx][colIdx] == 1 and (rowsServersCount[rowIdx] > 1 or colsServersCount[colIdx] > 1):
                    connectedCount += 1
            
        return connectedCount