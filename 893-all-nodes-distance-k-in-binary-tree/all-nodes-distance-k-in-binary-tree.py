class Solution(object):
    def distanceK(self, root, target, k):
        ans = []

        def collectDown(node, distance):
            if not node:
                return

            if distance == k:
                ans.append(node.val)
                return

            collectDown(node.left, distance + 1)
            collectDown(node.right, distance + 1)

        def dfs(node):
            if not node:
                return -1

            # Found target
            if node == target:
                collectDown(node, 0)
                return 0

            leftDistance = dfs(node.left)

            if leftDistance != -1:
                distance = leftDistance + 1

                if distance == k:
                    ans.append(node.val)
                else:
                    collectDown(node.right, distance + 1)

                return distance

            rightDistance = dfs(node.right)

            if rightDistance != -1:
                distance = rightDistance + 1

                if distance == k:
                    ans.append(node.val)
                else:
                    collectDown(node.left, distance + 1)

                return distance

            return -1

        dfs(root)
        return ans