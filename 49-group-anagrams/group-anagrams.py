class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashMap = {}

        for currStr in strs:
            sortedStr = ''.join(sorted(currStr))

            if sortedStr not in hashMap:
                hashMap[sortedStr] = [currStr]
            else:
                hashMap[sortedStr].append(currStr)

        return list(hashMap.values())