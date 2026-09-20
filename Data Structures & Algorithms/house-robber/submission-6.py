class Solution:
    def rob(self, nums: List[int]) -> int:
        res1 ,res2 = 0 , 0

        for num in nums:
            res1 , res2 = res2 , max(num + res1 , res2)
        
        return res2

        