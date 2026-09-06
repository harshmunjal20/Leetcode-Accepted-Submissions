class Solution(object):
    def gameOfLife(self, grid):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(grid)
        cols = len(grid[0])

        directions = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

        for rowIdx in range(rows):
            for colIdx in range(cols):
                
                neighbourLiveCount = 0
                neighbourDeadCount = 0

                for direction in directions:
                    x = direction[0] + rowIdx
                    y = direction[1] + colIdx

                    if x >= 0 and y >= 0 and x < rows and y < cols:
                        if grid[x][y] == 0 or grid[x][y] == 3:
                            neighbourDeadCount += 1
                        elif grid[x][y] == 1 or grid[x][y] == 2:
                            neighbourLiveCount += 1
                
                if grid[rowIdx][colIdx] == 1:
                    if neighbourLiveCount < 2 or neighbourLiveCount > 3:
                        # we have to make this cell as 0, so make it temporary 2, then we will use it to make it to 0
                        grid[rowIdx][colIdx] = 2

                elif grid[rowIdx][colIdx] == 0:
                    if neighbourLiveCount == 3: # make this cell as 1 , currently we will make it 3 , in the future we will make it to 1
                        grid[rowIdx][colIdx] = 3
        
        for rowIdx in range(rows):
            for colIdx in range(cols):
                if grid[rowIdx][colIdx] == 2:
                    grid[rowIdx][colIdx] = 0
                elif grid[rowIdx][colIdx] == 3:
                    grid[rowIdx][colIdx] = 1