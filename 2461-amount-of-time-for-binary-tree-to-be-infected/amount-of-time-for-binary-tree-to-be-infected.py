# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque

class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        parentsMap = {}
        startNode = []

        def DFS(root, parentNode):
            if not root:
                return
            
            if root.val == start:
                startNode.append(root)

            parentsMap[root] = parentNode
            DFS(root.left, root)
            DFS(root.right, root)

        visited = set()
        DFS(root, None)
        queue = deque()
        queue.append(startNode[0])
        visited.add(startNode[0])
        totalMinutes = 0

        while queue:
            sz = len(queue)

            for _ in range(sz):
                node = queue.popleft()

                for neighbour in (parentsMap[node], node.left, node.right):
                    if neighbour and neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)

            if queue:
                totalMinutes += 1

        return totalMinutes