class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSum , maxiSum = 0 , nums[0]
        for num in nums:
            if curSum < 0 :
                curSum = 0
            
            curSum += num
            maxiSum = max(maxiSum , curSum)
        
        return maxiSum