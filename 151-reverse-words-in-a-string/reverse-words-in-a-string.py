class Solution:
    def reverseWords(self, s: str) -> str:
        splitWords = s.split()
        splitWords.reverse()
        return " ".join(splitWords)