# [4,2,3,7] 

# Naive solution: Exploration

from collections import defaultdict

class Solution:
    def __init__(self):
        self.DP = defaultdict(int)
        self.DP[()] = 0

    @staticmethod
    def _compute_value(array, pos) -> int:
        result = array[pos]
        if pos - 1 >= 0:
            result *= array[pos-1]
        if pos + 1 < len(array):
            result *= array[pos+1]
        return result

    def _go(self, array) -> int:
        if not array:
            return self.DP[()]
        if len(array) == 1:
            return self.DP[array[0],]
        
        ans = 0
        for i in range(len(array)):
            new_array = tuple(array[:i] + array[i+1:])
            if new_array in self.DP:
                ans = max(ans, self._compute_value(array, i) + self.DP[new_array])
            else:
                self.DP[new_array] = self._go(new_array)
                ans = max(
                    ans, 
                    self._compute_value(array, i) + self.DP[new_array]
                )
        
        return ans
            

    def maxCoins(self, nums: List[int]) -> int:
        for n in nums:
            self.DP[n,] = n # Any number alone is 1*n*1

        return self._go(tuple(nums))
            



        