from collections import defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        M = defaultdict(int)
        M.update({0: 0, 1:1, 2:2})
        for i in range(3, n+1): 
          M[i] = M[i-1] + M[i-2]
        
        return M[n]