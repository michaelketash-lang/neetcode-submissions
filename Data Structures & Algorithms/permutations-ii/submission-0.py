class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])  # Append a copy of the current permutation
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs(path)
                path.pop()
                dfs(path)
                used[i] = False
        dfs([])
        return res
