class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1

        while l <= r:
            mid = (r + l) // 2
            # step 1: check if we found target
            if target == nums[mid]:
                return mid

            # step 2: check if the left portion is sorted if yes we want to check if target
            #is between nums[l] <= target < nums[mid]
            if nums[mid] > nums[r]: 
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # step 3: check if the right portion is sorted if yes we want to check if target
            #is between nums[mid] < target <= nums[r]
            else: # which means nums[mid] <= nums[r]
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1 # step toward the right portion
                else:
                    r = mid - 1 # step toward left portion
        return -1

        