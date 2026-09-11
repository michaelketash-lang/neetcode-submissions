class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #solution: two passes
        """
        -build output array in two passes
        -each pass kepp a single running product ,write it into res[i]
        -res[i] = prefix
        prefix *= nums[i]
        -same for suffix
        """


        prefix = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res