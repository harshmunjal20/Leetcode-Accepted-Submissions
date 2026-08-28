# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans = []
        queue = deque()
        if root:
            queue.append(root)
        currLevel = 0

        while queue:
            sz = len(queue)
            currLevelNodes = []

            while sz > 0:
                node = queue.popleft()
                currLevelNodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                sz -= 1

            ans.append(currLevelNodes)
            currLevel += 1

        return ans