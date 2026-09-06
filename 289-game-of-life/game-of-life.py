class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0], [-1, 1], [1, -1], [1, 1], [-1, -1]]

        for rowIdx in range(rows):
            for colIdx in range(cols):
                liveCount = 0

                for direction in directions:
                    x = direction[0] + rowIdx
                    y = direction[1] + colIdx
    
                    if x >= 0 and y >= 0 and x < rows and y < cols and (board[x][y] == 1 or board[x][y] == 3):
                        liveCount += 1
                
                if board[rowIdx][colIdx] == 1 and (liveCount < 2 or liveCount > 3):
                    # make it dead
                    board[rowIdx][colIdx] = 3
                elif board[rowIdx][colIdx] == 0 and liveCount == 3:
                    board[rowIdx][colIdx] = 2 # make it live
        
        for rowIdx in range(rows):
            for colIdx in range(cols):
                if board[rowIdx][colIdx] == 2:
                    board[rowIdx][colIdx] = 1
                elif board[rowIdx][colIdx] == 3:
                    board[rowIdx][colIdx] = 0
