class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        runningUnique = 0
        maxLen = 0
        i , j = 0, 0
        prevChar = 'z'

        while j < len(word):
            if word[j] > prevChar:
                runningUnique += 1
            elif word[j] < prevChar:
                runningUnique = 0
                i = j

            if runningUnique == 4:
                maxLen = max(maxLen, j - i + 1)

            prevChar = word[j]
            j += 1

        return maxLen