from functools import cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]

        @cache
        def dp(left: int, right: int) -> int:
            if right == left + 1:
                return 0

            best = 0

            for i in range(left + 1, right):
                coins = (
                    dp(left, i)
                    + balloons[left] * balloons[i] * balloons[right]
                    + dp(i, right)
                )
                best = max(best, coins)

            return best

        return dp(0, len(balloons) - 1)