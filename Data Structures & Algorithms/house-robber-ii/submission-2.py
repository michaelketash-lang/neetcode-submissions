class Solution:
    def rob(self, nums: List[int]) -> int:
        # we need to avoid the cycle attribute => if we take first elem we cant take the last => 
        return max(nums[0] , self.helper(nums[1 : ]) , self.helper(nums[: -1]))
        

    
    def helper(self, nums):
        rob1 , rob2 = 0, 0

        for num in nums:
            temp = max(rob1 + num , rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2