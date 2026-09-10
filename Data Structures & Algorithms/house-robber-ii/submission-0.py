class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(houses): #implementation of HOUSE ROB 1
            rob1,rob2 = 0,0
            for house in houses:
                tempRob = max(rob1+house,rob2)
                rob1 = rob2
                rob2 = tempRob
            return rob2
        a = helper(nums[1:]) #checks without first house
        b = helper(nums[:-1]) #checks without last house
        return max(a,b,nums[0]) # take the max rob
