class Solution(object):
    def countPairsOfConnectableServers(self, edges, signalSpeed):
        """
        :type edges: List[List[int]]
        :type signalSpeed: int
        :rtype: List[int]
        """
        def DFS(node, parent, weight, adj):
            nodes = 0

            if weight % signalSpeed == 0:
                nodes += 1

            for neighbour, neighbourWeight in adj[node]:
                if neighbour != parent:
                    nodes += DFS(neighbour, node, weight + neighbourWeight, adj)

            return nodes

        countNodes = len(edges) + 1
        adj = [[] for _ in range(countNodes)]
        count = [0] * countNodes

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        for node in range(countNodes):
            nodesSeen = 0
            parent = node
            
            for neighbour, weight in adj[node]:
                currBranchNodes = DFS(neighbour, parent, weight, adj)
                count[node] += currBranchNodes * nodesSeen
                nodesSeen += currBranchNodes
    
        return count