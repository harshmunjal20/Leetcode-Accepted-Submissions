class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rowsCount = len(matrix)
        colsCount = len(matrix[0])
        dp = [0 for _ in range(colsCount + 1)]
        maxArea = 0

        for rowIdx in range(1, rowsCount + 1):
            prevVal = 0

            for colIdx in range(1, colsCount + 1):
                currVal = dp[colIdx]
                if matrix[rowIdx - 1][colIdx - 1] == "1":
                    dp[colIdx] = 1 + min(dp[colIdx], dp[colIdx - 1], prevVal)
                    maxArea = max(maxArea, dp[colIdx] * dp[colIdx])
                else:
                    dp[colIdx] = 0

                prevVal = currVal

        return maxArea