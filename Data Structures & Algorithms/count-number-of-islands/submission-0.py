from collections import deque

class Solution:
    @staticmethod
    def _is_valid_next(r, c, num_rows, num_cols) -> bool:
        return not ((r < 0 or r >= num_rows) or (c < 0 or c >= num_cols))

    def _get_neighbors(self, r, c, num_rows, num_cols) -> list:
        neighbors = []
        if self._is_valid_next(r+1, c, num_rows, num_cols):
            neighbors.append((r+1, c))
        if self._is_valid_next(r-1, c, num_rows, num_cols):
            neighbors.append((r-1, c))
        if self._is_valid_next(r, c+1, num_rows, num_cols):
            neighbors.append((r, c+1))
        if self._is_valid_next(r, c-1, num_rows, num_cols):
            neighbors.append((r, c-1))
        return neighbors

    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0   
        visited = set()
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):    
                if (r,c) not in visited and grid[r][c] == '1':
                    nexts = deque()
                    nexts.append((r,c))
                    total += 1
                    while nexts:
                        current_r, current_c = nexts.popleft()
                        if (current_r, current_c) in visited: 
                            continue    
                        visited.add((current_r, current_c))
                        if grid[current_r][current_c] == '1':
                            neighbors = self._get_neighbors(
                                current_r, current_c, len(grid), len(grid[0])
                            )
                            nexts.extend(neighbors)
        return total


                        


