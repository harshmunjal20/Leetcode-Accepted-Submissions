class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        hashMap = {}

        for idx in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[idx]:
                stack.pop()
            
            if stack:
                hashMap[nums2[idx]] = stack[-1]
            else:
                hashMap[nums2[idx]] = -1

            stack.append(nums2[idx])
        
        return [hashMap[val] for val in nums1]
