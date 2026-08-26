from collections import deque

class Solution(object):
    
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        xDir = [-1, 0, 1, 0]
        yDir = [0, 1, 0, -1]
        queue = deque()
        minMoves = 0
        totalKeys = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    queue.append((i, j, 0)) # third argument is keys
                    visited.add((i, j, 0))
                elif grid[i][j] >= 'a' and grid[i][j] <= 'z':
                    totalKeys += 1

        minMoves = 0

        while queue:
            sz = len(queue)

            while sz > 0:
                i, j, keys = queue.popleft()

                target_mask = (1 << totalKeys) - 1

                if target_mask == keys:
                    return minMoves

                for index in range(4):
                    x = xDir[index] + i
                    y = yDir[index] + j

                    if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] != '#' and ((x, y, keys) not in visited):
                        numKeys = keys

                        if grid[x][y] >= 'A' and grid[x][y] <= 'Z' and (keys & (1 << (ord(grid[x][y]) - ord('A')))) == 0:
                            continue
                        elif grid[x][y] >= 'a' and grid[x][y] <= 'z':
                            numKeys = numKeys | (1 << (ord(grid[x][y]) - ord('a')))
                        
                        visited.add((x, y, numKeys))
                        queue.append((x, y, numKeys))
                
                sz -= 1

            minMoves += 1

        return -1