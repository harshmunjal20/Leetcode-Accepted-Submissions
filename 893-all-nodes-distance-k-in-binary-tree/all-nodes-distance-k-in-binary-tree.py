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
        parentsMap = defaultdict(lambda: TreeNode())

        def DFS(root, parentNode):
            if not root:
                return

            parentsMap[root.val] = parentNode
            DFS(root.left, root)
            DFS(root.right, root)
        
        DFS(root, None)
        queue = deque()
        queue.append(target)
        visited = set()
        ans = []
        currLevel = 0

        while queue:
            sz = len(queue)

            while sz > 0:
                node = queue.popleft()

                sz -= 1

                if node.val in visited:
                    continue

                visited.add(node.val)

                if currLevel == k:
                    ans.append(node.val)

                if parentsMap[node.val]:
                    queue.append(parentsMap[node.val])

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            currLevel += 1
            if currLevel > k:
                break


        return ans


