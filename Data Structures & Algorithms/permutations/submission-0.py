class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(cur):
            if len(cur) == len(nums):
                ans.append(cur[:]) # we can use copy either
                return
            
            for number in nums:
                if number not in cur:
                    cur.append(number)
                    dfs(cur)
                    cur.pop()
        dfs([])
        return ans
        