class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        maximumArea = 0

        while i < j:
            if height[i] < height[j]:
                maximumArea = max(maximumArea, height[i] * (j - i))
                i += 1
            else:
                maximumArea = max(maximumArea, height[j] * (j - i))
                j -= 1

        return maximumArea