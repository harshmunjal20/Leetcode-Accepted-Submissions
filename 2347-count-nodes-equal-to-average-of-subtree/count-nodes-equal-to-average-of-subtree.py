# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = [0]

        def DFS(root):
            if not root:
                return (0, 0)
            
            if not root.left and not root.right:
                count[0] += 1
                return (root.val, 1)
            
            leftValCountPair = DFS(root.left)
            rightValCountPair = DFS(root.right)

            sum = root.val + leftValCountPair[0] + rightValCountPair[0]
            nodesCount = 1 + leftValCountPair[1] + rightValCountPair[1]
            average = sum / nodesCount

            count[0] += int(average == root.val)
            return (sum, nodesCount)

        DFS(root)
        return count[0]