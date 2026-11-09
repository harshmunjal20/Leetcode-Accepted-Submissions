# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []

        def preorderTraversalUtil(root):
            if not root:
                return
            
            ans.append(root.val)
            preorderTraversalUtil(root.left)
            preorderTraversalUtil(root.right)
        
        preorderTraversalUtil(root)
        return ans