class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        startIdx, endIdx = 0, 0
        idx = 0
        sz = len(s)

        while idx < sz:
            if s[idx] == '(':
                stack.append(s[idx])
            elif s[idx] == ')':
                currStr = stack[-1]

                while stack and stack[-1] != '(':
                    currStr = stack.pop()
                    if stack[-1] != '(':
                        stack.append(stack.pop() + currStr)
                    else:
                        stack.pop()
                        stack.append(currStr[::-1])
                        break
                
                if currStr ==  '(':
                    stack.pop()
            else:
                startIdx = idx

                while idx < sz and s[idx] != '(' and s[idx] != ')':
                    idx += 1
                
                # now we are one index more
                endIdx = idx
                stack.append(s[startIdx : endIdx])
                idx -= 1

            idx += 1
        
        while len(stack) > 1:
            currStr = stack.pop()
            stack.append(stack.pop() + currStr)

        return stack[-1]