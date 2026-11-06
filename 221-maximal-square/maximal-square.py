class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rowsCount = len(matrix)
        colsCount = len(matrix[0])
        dp = [[0 for _ in range(colsCount + 1)] for _ in range(rowsCount + 1)]
        maxArea = 0

        for rowIdx in range(1, rowsCount + 1):
            for colIdx in range(1, colsCount + 1):
                if matrix[rowIdx - 1][colIdx - 1] == "1":
                    dp[rowIdx][colIdx] = 1 + min(dp[rowIdx - 1][colIdx], dp[rowIdx][colIdx - 1], dp[rowIdx - 1][colIdx - 1])
                    maxArea = max(maxArea, dp[rowIdx][colIdx] * dp[rowIdx][colIdx])

        return maxArea