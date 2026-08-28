# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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

            depthLeft = DFS(root.left)
            depthRight = DFS(root.right)

            if depthLeft < 0:
                minTime[0] = max(minTime[0], depthRight + abs(depthLeft))
                return depthLeft - 1

            if depthRight < 0:
                minTime[0] = max(minTime[0], depthLeft + abs(depthRight))
                return depthRight - 1

            if root.val == start:
                minTime[0] = max(minTime[0], max(depthLeft, depthRight))
                return -1

            return 1 + max(depthLeft, depthRight)

            
        DFS(root)
        return minTime[0]