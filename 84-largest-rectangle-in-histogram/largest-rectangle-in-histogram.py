class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        maxArea = 0

        for idx in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[idx]:
                topIdx = stack.pop()
                nextTopIdx = stack[-1] if stack else len(heights)
                maxArea = max(maxArea, heights[topIdx] * (nextTopIdx - idx - 1))
            
            stack.append(idx)

        while stack and heights[stack[-1]] >= -1:
            topIdx = stack.pop()
            nextTopIdx = stack[-1] if stack else len(heights)
            maxArea = max(maxArea, heights[topIdx] * (nextTopIdx))

        return maxArea