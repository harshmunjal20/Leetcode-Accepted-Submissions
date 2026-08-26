class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        queue = deque()
        visited = set()
        totalKeys = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@':
                    queue.append((i * cols + j, 0))
                    visited.add((i * cols + j, 0))
                elif 'a' <= grid[i][j] <= 'f':
                    totalKeys += 1
        
        target = (1 << totalKeys) - 1
        totalMoves = 0

        while queue:
            sz = len(queue)

            while sz > 0:
                decodedNum , keys = queue.popleft()
                i = decodedNum / cols
                j = decodedNum % cols

                if keys == target:
                    return totalMoves

                for dirX, dirY in directions:
                    x = dirX + i
                    y = dirY + j

                    if x >= 0 and x < rows and y >= 0 and y < cols and grid[x][y] != '#' and not (x * cols + y, keys) in visited:
                        numKeys = keys

                        if 'A' <= grid[x][y] <= 'F' and not (numKeys & (1 << (ord(grid[x][y]) - ord('A')))):
                            continue
                        elif 'a' <= grid[x][y] <= 'f' :
                            numKeys = numKeys | (1 << (ord(grid[x][y]) - ord('a')))

                        visited.add((x * cols +  y, numKeys))
                        queue.append((x * cols + y, numKeys))

                sz -= 1

            totalMoves += 1
        
        return -1
