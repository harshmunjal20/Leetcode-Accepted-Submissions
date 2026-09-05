from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashMap = defaultdict(list)
        ans = []

        for currStr in strs:
            sortedStr = ''.join(sorted(currStr))
            hashMap[sortedStr].append(currStr)

        for value in hashMap.values():
            ans.append(value)

        return ans