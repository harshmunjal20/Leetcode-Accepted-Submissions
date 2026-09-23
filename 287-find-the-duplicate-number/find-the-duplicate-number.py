class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        hashSet = set()

        for num in nums:
            if num in hashSet:
                return num
            
            hashSet.add(num)
    
        return -1