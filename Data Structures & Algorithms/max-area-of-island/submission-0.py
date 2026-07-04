class Solution:
    def DFS(
        self,
        root: tuple[int, int],
        visited: set[int]
    ) -> int: # Returns found island number
        if (
            root in visited or
            root[0] < 0 or
            root[1] < 0 or
            root[0] > self.n_rows - 1 or
            root[1] > self.n_cols - 1 or
            self._map[root[0]][root[1]] == 0
        ):
            return 0
        
        visited.add(root)

        left = self.DFS((root[0]-1, root[1]), visited)
        right = self.DFS((root[0]+1, root[1]), visited)
        up = self.DFS((root[0], root[1]-1), visited)
        down = self.DFS((root[0], root[1]+1), visited)

        return 1 + left + right + up + down



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.n_rows = len(grid)
        self.n_cols = len(grid[0])
        self._map = grid
        ans = 0
        visited = set()

        for r in range(self.n_rows):
            for c in range(self.n_cols):
                ans = max(ans, self.DFS((r,c),visited))
        
        return ans
        
