from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        
        @cache
        def dp(i , target):
            if i >= len(nums):
                return target == 0
            
            if target < 0 :
                return False
            
            return dp(i + 1 , target) or dp(i + 1, target - nums[i])
        
        return dp(0 , sum_nums // 2)
        