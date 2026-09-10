class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        rob1 , rob2 = 0,0
        for i in range(len(nums)):
            temp = max(nums[i]+rob1,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

        