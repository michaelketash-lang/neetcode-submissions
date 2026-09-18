class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst, res = [], []

        def dfs(open_prant , close_prant):
            # i will count number of open and number of close finish when both are == n:
            if open_prant == n and close_prant == n:
                res.append("".join(lst)) # convert lst to a string
                return
            
            if open_prant < n:
                #try to add (
                lst.append("(")
                dfs(open_prant + 1 , close_prant)
                lst.pop()
            
            if close_prant < open_prant: # we can try to add )
                lst.append(")")
                dfs(open_prant , close_prant + 1)
                lst.pop()
        dfs(0 , 0)
        return res
        