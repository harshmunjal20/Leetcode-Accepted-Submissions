# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        minTime = [0]

        def DFS(root):
            if not root:
                return 0

            val1 = DFS(root.left)    
            val2 = DFS(root.right)


            if val1 < 0:
                minTime[0] = max(minTime[0], abs(val1) + val2)
                return val1 - 1
            
            if val2 < 0:
                minTime[0] = max(minTime[0], val1 + abs(val2))
                return val2 - 1
                
            if root.val == start:
                minTime[0] = max(minTime[0], max(val1, val2))
                return -1

            return 1 + max(val1, val2)

        DFS(root)
        return minTime[0]