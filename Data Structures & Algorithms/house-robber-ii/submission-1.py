class Solution:
    def rob(self , nums: List[int]) ->int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[ : -1]))
    def helper(self, nums: List[int]) -> int:
        res1 , res2 = 0 , 0

        for num in nums:
            res1 , res2 = res2 , max(num + res1 , res2)
        
        return res2