# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodesUtil(self, root: TreeNode, maxVal : int) -> None:
        if not root:
            return
        
        if root.val >= maxVal:
            self.count += 1
        
        self.goodNodesUtil(root.left, max(maxVal, root.val))
        self.goodNodesUtil(root.right, max(maxVal, root.val))

    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.goodNodesUtil(root, -1e10)
        return self.count