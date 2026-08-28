# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        parentsMap = {}
        queue = deque()
        queue.append(root)
        parentsMap[root] = None

        # make a map

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                parentsMap[node.left] = node

            if node.right:
                queue.append(node.right)
                parentsMap[node.right] = node
        
        ans = []
        currLevel = 0
        visited = set()
        queue.append(target)
        visited.add(target)

        while queue:
            sz = len(queue)

            for _ in range(sz):
                node = queue.popleft()

                if currLevel == k:
                    ans.append(node.val)

                for neighbour in (parentsMap[node], node.left, node.right):
                    if neighbour and neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)


            currLevel += 1
            
            if currLevel > k:
                break

        return ans

