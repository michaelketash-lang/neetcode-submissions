class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i , sum1):                
            if sum1 == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or sum1 > target:
                return
            
            subset.append(nums[i])
            dfs(i, sum1 + nums[i])
            subset.pop()
            dfs(i + 1, sum1)
        dfs(0, 0)
        return res

        