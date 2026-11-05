# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def goodNodesUtil(root: TreeNode, maxVal : int) -> None:
            if not root:
                return
            
            if root.val >= maxVal:
                maxVal = root.val
                self.count += 1
            
            goodNodesUtil(root.left, maxVal)
            goodNodesUtil(root.right, maxVal)
        
        goodNodesUtil(root, -1e10)
        return self.count