# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        queue = deque()
        queue.append(root)
        parentsMap = {}
        parentsMap[root] = None
        startNode = None

        while queue:
            node = queue.popleft()

            if node.val == start:
                startNode = node

            if node.left:
                parentsMap[node.left] = node
                queue.append(node.left)

            if node.right:
                parentsMap[node.right] = node
                queue.append(node.right)

        minTime = 0
        visited = set()
        queue.append(startNode)
        visited.add(startNode)

        while queue:
            sz = len(queue)

            for _ in range(sz):
                node = queue.popleft()

                for neighbour in (parentsMap[node], node.left, node.right):
                    if neighbour and neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)

            if queue:
                minTime += 1

        return minTime