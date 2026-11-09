# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        # iterative postorderTraversal => root right left
        if not root:
            return []
            
        stack = []
        ans = []
        stack.append(root)

        while stack:
            node = stack.pop()
            ans.append(node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        ans.reverse()
        return ans