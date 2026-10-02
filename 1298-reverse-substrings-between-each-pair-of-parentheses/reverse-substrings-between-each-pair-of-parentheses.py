class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for idx in range(len(s)):
            if s[idx] == ')':
                temp = []

                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                
                stack.pop()
                stack.extend(temp)
            else:
                stack.append(s[idx])

        return "".join(stack)