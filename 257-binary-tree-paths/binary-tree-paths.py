# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        path = []
        paths = []

        def DFS(root):
            if not root:
                return
            
            if not root.left and not root.right:
                path.append(str(root.val))
                paths.append("".join(path))
                path.pop()
                return
            
            path.append(str(root.val))
            path.append('->')
            DFS(root.left)
            DFS(root.right)
            path.pop()
            path.pop()
        
        DFS(root)
        return paths