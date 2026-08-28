# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque, defaultdict

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        parentsMap = {}

        def DFS(root, parentNode):
            if not root:
                return

            parentsMap[root] = parentNode
            DFS(root.left, root)
            DFS(root.right, root)
        
        DFS(root, None)
        visited = set()
        queue = deque()
        queue.append(target)
        visited.add(target)
        ans = []
        currLevel = 0

        while queue:
            sz = len(queue)

            for _ in range(sz):
                node = queue.popleft()

                if currLevel == k:
                    ans.append(node.val)

                for neighbour in (parentsMap[node], node.left, node.right):
                    if neighbour and neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)


            currLevel += 1
            if currLevel > k:
                break


        return ans


