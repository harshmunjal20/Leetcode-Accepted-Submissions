class Solution:
    def maximalArea(self, heights : list[int]) -> int:
        stack = []
        sz = len(heights)
        maxArea = 0

        for idx in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[idx]:
                topIdx = stack.pop()
                nextTopIdx = stack[-1] if stack else sz
                maxArea = max(maxArea, heights[topIdx] * (nextTopIdx - idx - 1))

            stack.append(idx)

        while stack and heights[stack[-1]] >= -1:
            topIdx = stack.pop()
            nextTopIdx = stack[-1] if stack else sz
            maxArea = max(maxArea, heights[topIdx] * (nextTopIdx))

        return maxArea

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        heights = [0] * len(matrix[0])
        maxArea = 0

        for rowIdx in range(len(matrix)):
            for colIdx in range(len(matrix[0])):
                if matrix[rowIdx][colIdx] == "1":
                    heights[colIdx] += 1
                else:
                    heights[colIdx] = 0

            maxArea = max(maxArea, self.maximalArea(heights))

        return maxArea