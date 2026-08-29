from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def BFS(src, dest, adj):
            if src == dest:
                return 1.0
            
            queue = deque()
            queue.append((src, 1.0))
            visited = set()
            visited.add(src)

            while queue:
                node, currProd = queue.popleft()

                if node == dest:
                    return currProd

                for neighbour , value in adj[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((neighbour, currProd * value))
            
            return -1.0


        adj = defaultdict(list)
        ans = []

        for idx in range(len(equations)):
            u = equations[idx][0]
            v = equations[idx][1]
            wt = values[idx]

            adj[u].append((v, wt))
            adj[v].append((u, 1.0 / wt))

        for query in queries:
            src = query[0]
            dest = query[1]

            if src not in adj or dest not in adj:
                ans.append(-1)
            else:
                ans.append(BFS(src, dest, adj))
        
        return ans