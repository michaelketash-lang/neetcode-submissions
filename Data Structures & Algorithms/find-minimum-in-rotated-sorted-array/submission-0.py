class Solution:
    def findMin(self, nums: List[int]) -> int:
        # initialize l,r pointers two implement binary search
        l , r = 0 , len(nums) -1
        #initialize res to be nums[0]
        res = nums[0]

        while l <= r :
            if nums[l] < nums[r]: # this happens iff the array is sorted
                res = min(res, nums[l])
                break

            mid = (r + l) // 2
            res = min(res,nums[mid])
            if nums[mid] >= nums[l]:#it means nums[mid] is part of the ascending sequence so
            #we need to look at the second portion
                l = mid + 1
            else:
                r = mid - 1
        return res


        