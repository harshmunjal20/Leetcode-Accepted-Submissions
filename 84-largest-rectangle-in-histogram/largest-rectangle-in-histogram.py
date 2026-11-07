class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # maintain strictly decreasing values on stack
        stack = []
        maxArea = 0
        heights.insert(0, -1)
        sz = len(heights)
        
        for idx in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[idx]:
                topIdx = stack.pop()
                nextTopIdx = stack[-1] if stack else sz
                maxArea = max(maxArea, heights[topIdx] * (nextTopIdx - idx - 1))

            stack.append(idx)

        return maxArea