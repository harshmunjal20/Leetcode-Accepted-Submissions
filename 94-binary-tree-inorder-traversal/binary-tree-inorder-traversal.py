# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        stack = []
        ans = []
        node = root

        while node:
            stack.append(node)
            node = node.left

        while stack:
            node = stack.pop()
            ans.append(node.val)

            if node.right:
                stack.append(node.right)
                node = node.right

                while node.left:
                    stack.append(node.left)
                    node = node.left

        return ans