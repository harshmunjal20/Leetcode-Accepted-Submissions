class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        def calculateMaxArea(heights : list[int]) -> int:
            maxArea = 0
            stack = []

            for idx in range(len(heights) - 1, -1, -1):
                while stack and heights[stack[-1]] >= heights[idx]:
                    topIdx = stack.pop()
                    nextTopIdx = stack[-1] if stack else len(heights)
                    maxArea = max(maxArea, heights[topIdx] * (nextTopIdx - idx - 1))
                
                stack.append(idx)

            while stack:
                topIdx = stack.pop()
                nextTopIdx = stack[-1] if stack else len(heights)
                maxArea = max(maxArea, heights[topIdx] * (nextTopIdx))

            return maxArea

        rows = len(matrix)
        cols = len(matrix[0])
        maxArea = 0
        heights = [0] * cols

        for rowIdx in range(rows):
            for colIdx in range(cols):
                if matrix[rowIdx][colIdx] == "1":
                    heights[colIdx] += 1
                else:
                    heights[colIdx] = 0
            
            maxArea = max(maxArea, calculateMaxArea(heights))

        return maxArea