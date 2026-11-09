# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans = []

        def postorderTraversalUtil(root):
            if not root:
                return

            postorderTraversalUtil(root.left)
            postorderTraversalUtil(root.right)
            ans.append(root.val)

        postorderTraversalUtil(root)
        return ans