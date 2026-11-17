class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def dfs(i , sublist, total):
            if total == target:
                res.append(sublist[:])
                return
            
            if total > target or i == len(candidates):
                return
            
            sublist.append(candidates[i])
            dfs(i + 1 , sublist , total + candidates[i])
            sublist.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1 , sublist , total)
            return
        dfs(0 , [] , 0)

        return res