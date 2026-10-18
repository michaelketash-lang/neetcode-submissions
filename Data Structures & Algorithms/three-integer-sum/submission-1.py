class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =[]
        nums_sorted = sorted(nums)

        for i , val in enumerate(nums_sorted):
            if val > 0:
                break
            
            if i > 0 and val == nums_sorted[i - 1]:
                continue
            
            l , r = i + 1 , len(nums_sorted) - 1

            while l < r:
                target = nums_sorted[l] + nums_sorted[r] + val

                if target > 0:
                    r -= 1
                
                elif target < 0 :
                    l += 1
                
                else:
                    res.append([nums_sorted[l] , nums_sorted[r] , val])
                    l += 1
                    while l < r and nums_sorted[l] == nums_sorted[l - 1]:
                        l += 1
        
        return res