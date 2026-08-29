class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        maxLen = 0
        i, j = 0, 0
        runningUnique = 0
        prevChar = 128

        while j < len(word):
            if ord(word[j]) > prevChar:
                runningUnique += 1
            elif ord(word[j]) < prevChar:
                runningUnique = 0
                i = j

            if runningUnique == 4:
                maxLen = max(maxLen, j - i + 1)

            prevChar = ord(word[j])
            j += 1

        return maxLen