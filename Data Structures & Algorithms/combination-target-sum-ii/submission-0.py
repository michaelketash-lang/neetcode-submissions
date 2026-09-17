class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i , sum1):
            if sum1 == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or sum1 > target:
                return
            
            subset.append(candidates[i])
            dfs(i + 1, sum1 + candidates[i])
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, sum1)
        
        dfs(0 , 0)
        return res