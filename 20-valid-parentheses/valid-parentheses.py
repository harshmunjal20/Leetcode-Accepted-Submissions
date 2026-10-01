class Solution:
    def isValid(self, s: str) -> bool:
        validOpening = {'}' : '{', ')' : '(', ']' : '['}
        stack = []

        for char in s:
            if stack and (char == ')' or char == '}' or char == ']'):
                if stack[-1] == validOpening[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack
