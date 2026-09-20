class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        res = [0] * n
        res[0] , res[1] = nums[0] , max(nums[0],nums[1])

        for i in range(2 , n ):
            res[i] = max(res[i-1] , res[i - 2] + nums[i])
        
        return res[-1]