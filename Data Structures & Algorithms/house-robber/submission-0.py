class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 =0,0
        #[1,1,3,3]
        for house in nums:
            temp =max(rob1+house,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2