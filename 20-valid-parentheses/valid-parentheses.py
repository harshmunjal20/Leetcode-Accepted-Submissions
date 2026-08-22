class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for ch in s:
            if (stack and ((ch == ')' and stack[-1] == '(') or (ch == '}' and stack[-1] == '{') or (ch == ']' and stack[-1] == '['))):
                stack.pop()
            elif (stack and ((ch == ')' and stack[-1] != '(') or (ch == '}' and stack[-1] != '{') or (ch == ']' and stack[-1] != '['))):
                return False
            else:
                stack.append(ch)

        return len(stack) == 0
        