class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_seen = prices[0]
        max_profit = 0

        for n in prices:
            min_seen = min(min_seen, n)
            max_profit = max(max_profit, n - min_seen)
        
        return max_profit