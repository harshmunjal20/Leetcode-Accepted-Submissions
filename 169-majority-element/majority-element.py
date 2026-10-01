from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashMap = Counter(nums)
        maxElem = 0
        maxFreq = 0

        for num, freq in hashMap.items():
            if freq > maxFreq :
                maxElem = num
                maxFreq = freq
        
        return maxElem