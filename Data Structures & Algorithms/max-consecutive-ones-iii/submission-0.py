class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        ans = 0
        L, R = 0, 0

        while R < len(nums):
            if nums[R] == 1:
                ans = max(ans, R-L+1)             
                R += 1
            else:
                if k > 0:
                    ans = max(ans, R-L+1)
                    k -= 1                
                    R += 1
                else:
                    while nums[L] == 1:
                        L += 1
                    k += 1
                    L += 1

        return ans
