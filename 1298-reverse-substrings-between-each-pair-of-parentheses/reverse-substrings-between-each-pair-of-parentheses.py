class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        stack.append([''])

        for char in s:
            if char == '(':
                stack.append([''])
            elif char == ')':
                reversedStr = stack.pop()[::-1]
                if stack:
                    stack[-1].extend(reversedStr)
                else:
                    stack.append(reversedStr)
            else:
                stack[-1].append(char)

        return "".join(stack[-1])