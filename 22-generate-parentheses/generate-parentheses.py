class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        validPair = []
        allValidPairs = []
        
        def generateParenthesisUtil(open, close) -> void:
            if open + close == 2 * n:
                allValidPairs.append("".join(validPair))
                return
            
            if open < n:
                validPair.append("(")
                generateParenthesisUtil(open + 1, close)
                validPair.pop()

            if close < open:
                validPair.append(")")
                generateParenthesisUtil(open, close + 1)
                validPair.pop()
        
        open, close = 0, 0
        generateParenthesisUtil(open, close)
        return allValidPairs