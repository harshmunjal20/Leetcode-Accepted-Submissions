class Solution(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        :type edges: List[List[int]]
        :type signalSpeed: int
        :rtype: List[int]
        """
        def DFS(node, weight, parent, adj):
            countNodes = 0
            if weight % signalSpeed == 0:
                countNodes += 1

            for neighbourNode , neighbourWeight in adj[node]:
                if neighbourNode != parent:
                    countNodes += DFS(neighbourNode, weight + neighbourWeight, node, adj)
            
            return countNodes
                    

        nodesCount = len(edges) + 1
        count = [0] * nodesCount
        adj = [[] for _ in range(nodesCount)]

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        for node in range(nodesCount):
            parent = node
            connectableNodes = 0

            for neighbourNode , weight in adj[node]:
                currCount = DFS(neighbourNode, weight, parent, adj)
                count[node] += currCount * connectableNodes
                connectableNodes += currCount

        return count


        