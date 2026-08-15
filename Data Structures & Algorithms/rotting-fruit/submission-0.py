from collections import deque

class Solution:
    @staticmethod
    def get_adjacent(r, c, rows, cols) -> list:
        adjacent = []

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_r = r + dr
            next_c = c + dc

            if 0 <= next_r < rows and 0 <= next_c < cols:
                adjacent.append((next_r, next_c))

        return adjacent

    def orangesRotting(self, grid: List[List[int]]) -> int:
        next_rotten = deque()
        total_fresh = 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == 2: # rotten
                    next_rotten.append(((r,c), 0))
                elif grid[r][c] == 1: # fresh
                    total_fresh += 1

        if not total_fresh:
            return 0
        max_minute = 0
        visited = set()
        while next_rotten:
            pos, index = next_rotten.popleft()
            max_minute = max(max_minute, index)
            visited.add(pos)
            ajdacent = self.get_adjacent(pos[0], pos[1], len(grid), len(grid[0]))
            for next_r, next_c in ajdacent:
                if grid[next_r][next_c] == 1:
                    grid[next_r][next_c] = 2
                    next_rotten.append(((next_r, next_c), index+1))
                    total_fresh -= 1

        if total_fresh > 0:
            return -1

        return max_minute
        