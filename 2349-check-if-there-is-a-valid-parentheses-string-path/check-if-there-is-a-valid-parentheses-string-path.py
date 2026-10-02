class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        que = deque()
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0, 1], [1, 0]]
        que.append((0, 0, 1 if grid[0][0] == '(' else -1))
        visited = set()

        while que:
            x, y, sum = que.pop()

            if sum < 0:
                continue

            if x == rows - 1 and y == cols - 1 and sum == 0:
                return True

            for [xDir , yDir] in directions:
                i = x + xDir
                j = y + yDir

                if i >= 0 and j >= 0 and i < rows and j < cols and (i, j, sum) not in visited:
                    visited.add((i, j, sum))
                    que.append((i, j, sum + (1 if grid[i][j] == '(' else -1)))

        return False